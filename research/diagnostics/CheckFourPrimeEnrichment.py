"""Uniform sampling of four-prime upper sites in the trimmed square window."""
from array import array
from bisect import bisect_left, bisect_right
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt, log, prod
from random import Random

from CheckSharedPrimeCenters import floor_root


BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
STRONG_PSEUDOPRIME_LIMIT = 318665857834031151167461
SITES = 16000


def prime(n):
    if not 0 <= n < STRONG_PSEUDOPRIME_LIMIT:
        raise ValueError("Input outside the certified twelve-base range")
    if n < 2 or any(n % q == 0 for q in BASES):
        return n in BASES
    odd, powers = n-1, 0
    while odd % 2 == 0:
        odd //= 2
        powers += 1
    for base in BASES:
        v = pow(base, odd, n)
        if v in (1, n-1):
            continue
        for _ in range(powers-1):
            v = v*v % n
            if v == n-1:
                break
        else:
            return False
    return True


def adjacent_prime(x, step):
    n = x+step
    while not prime(n):
        n += step
    return n


def sieve(limit):
    flags = bytearray(b"\1")*(limit+1)
    flags[:2] = b"\0\0"
    for q in range(2, isqrt(limit)+1):
        if flags[q]:
            flags[q*q::q] = bytes((limit-q*q)//q+1)
    return array("I", (n for n, flag in enumerate(flags) if flag))


def bins(primes, lower, upper):
    result = []
    edge = lower
    while edge <= upper:
        end = min(upper+1, 1 << edge.bit_length())
        left, right = bisect_left(primes, edge), bisect_left(primes, end)
        if left < right:
            result.append((left, right-left))
        edge = end
    return result


class SiteSampler:
    def __init__(self, lo, hi, lower, upper):
        self.lo, self.hi, self.upper = lo, hi, upper
        max_q = min(upper, floor_root(hi, 4))
        max_r = min(upper, floor_root(hi//lower, 3))
        max_t = min(upper, isqrt(hi//lower**2))
        self.primes = primes = sieve(max_t)
        self.boxes, self.ends = [], []
        total = 0
        for qs, rs, ts in product(*(bins(primes, lower, m) for m in (max_q, max_r, max_t))):
            q0, r0, t0 = (primes[i] for i, size in (qs, rs, ts))
            q1, r1, t1 = (primes[i+size-1] for i, size in (qs, rs, ts))
            if q0 > r1 or r0 > t1 or q0*r0*t0*t0 > hi or q1*r1*t1*upper <= lo:
                continue
            cap = (hi-lo)//(q0*r0*t0)+1
            total += qs[1]*rs[1]*ts[1]*cap
            self.boxes.append((qs, rs, ts, cap))
            self.ends.append(total)
        self.total = total

    def decode(self, ticket):
        b = bisect_right(self.ends, ticket)
        qs, rs, ts, cap = self.boxes[b]
        offset = ticket-(self.ends[b-1] if b else 0)
        offset, j = divmod(offset, cap)
        offset, k = divmod(offset, ts[1])
        i, h = divmod(offset, rs[1])
        q, r, t = (self.primes[qs[0]+i], self.primes[rs[0]+h], self.primes[ts[0]+k])
        if not q <= r <= t:
            return None
        m = q*r*t
        u = self.lo//m+1+j
        if t <= u <= self.upper and m*u <= self.hi and prime(u):
            return m*u
        return None


def toy_check():
    for lo, hi, lower, upper in [(500, 8000, 3, 19), (4000, 8000, 5, 17)]:
        sampler = SiteSampler(lo, hi, lower, upper)
        decoded = [v for ticket in range(sampler.total)
                   if (v := sampler.decode(ticket)) is not None]
        direct = []
        repeated = 0
        for value in range(lo+1, hi+1):
            n, fs = value, []
            for q in range(2, upper+1):
                while n % q == 0:
                    fs.append(q)
                    n //= q
            if n == 1 and len(fs) == 4 and min(fs) >= lower:
                direct.append(value)
                repeated += len(set(fs)) < 4
        assert sorted(decoded) == direct and repeated > 0
        print("toy bijection", sampler.total, len(direct), repeated, flush=True)


def constants_and_local_factors():
    s, beta = Q(67,400), Q(2,5)
    large_sector_lower = (1-beta-3*s)**3/(36*beta*((1-beta)/3)**3)
    c_upper = Q(".0731696")-large_sector_lower
    assert 1+Q(".0147")/c_upper > Q("1.225")
    primes = sieve(1000)
    partial = prod(1-Q(1,(q-1)**2) for q in primes if q > 2)
    # Tail of sum_{m>=1000} 1/m^2 <= 1/999 by integral comparison.
    assert 2*partial*(1-Q(1,999))*Q("1.225") > Q("1.615")
    wheel = (3,5,7,11,13)
    coprime_mean = 2*prod(1-Q(1,(q-1)**2) for q in wheel)
    assert prod(wheel) == 15015 and 1-coprime_mean/Q("1.615") > Q(".167")
    assert 1-1/Q("1.225") == Q(9,49)
    for primes_w in ((3,), (3,5), (3,5,7)):
        w = prod(primes_w)
        units = [a for a in range(w) if gcd(a,w) == 1]
        for b in range(w):
            compatible = sum(gcd(2*b-a,w) == 1 for a in units)
            observed = Q(2*w*compatible, len(units)**2)
            predicted = 2*prod(1-Q(1,(q-1)**2) for q in primes_w)*prod(
                Q(q-1,q-2) for q in primes_w if b % q == 0)
            assert observed == predicted


def upper_endpoint(successes, count):
    """One-sided Bernoulli KL bound, union bound for six reported endpoints."""
    rate = successes/count
    if rate == 1:
        return 1.0
    low, high = rate, 1.0
    for _ in range(50):
        mid = (low+high)/2
        kl = ((rate*log(rate/mid) if rate else 0)
              + (1-rate)*log((1-rate)/(1-mid)))
        if count*kl <= log(600):
            low = mid
        else:
            high = mid
    return high


def experiment(p, seed, sites):
    x = p*p
    lo = x+2*floor_root(x**21, 40)
    hi = x+floor_root(x*x, 3)
    largest = floor_root(x*x, 5)
    lower = floor_root(x**67, 400)+1
    sampler = SiteSampler(lo, hi, lower, largest)
    cutoff = floor_root(x, 48)
    small = [q for q in BASES if q <= cutoff]
    assert 2 <= cutoff <= BASES[-1] and hi < STRONG_PSEUDOPRIME_LIMIT
    modulus = prod(small)
    local = prod(1-1/q for q in small)
    rng = Random(seed)
    accepted = rough = pairs = unit3 = draws = 0
    while accepted < sites:
        draws += 1
        a = sampler.decode(rng.randrange(sampler.total))
        if a is None:
            continue
        accepted += 1
        n = 2*x-a
        unit3 += n % 3 != 0
        if gcd(n, modulus) == 1:
            rough += 1
            pairs += prime(n)
    rate, raw_scaled = pairs/rough, log(x)*pairs/accepted
    print(f"p={p} seed={seed} zfloor={cutoff} tickets={draws} accepted={accepted} "
          f"unit3={unit3} rough={rough} primes={pairs} rate={rate:.7f} "
          f"rough_upper={upper_endpoint(pairs,rough):.7f} "
          f"finite_threshold={1.2/(log(x)*local):.7f} "
          f"raw_scaled={raw_scaled:.7f} raw_upper={log(x)*upper_endpoint(pairs,accepted):.7f}",
          flush=True)


if __name__ == "__main__":
    toy_check()
    constants_and_local_factors()
    for i, p in enumerate([adjacent_prime(2**25, 1),
                           adjacent_prime(3**24, -1), adjacent_prime(3**24, 1)]):
        experiment(p, 2026112601+i, SITES)
