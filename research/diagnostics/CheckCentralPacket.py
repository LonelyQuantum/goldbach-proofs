"""Finite CRT, convolution and truncation checks for CentralPrimePairPacket.md."""

from fractions import Fraction as F
from bisect import bisect_right
from math import comb, gcd, isqrt, lcm, prod


def local_products():
    primes = (2, 3, 5, 7)
    wheel = prod(primes)
    density = prod(F(p-1, p) for p in primes)
    cases = 0
    for d in (1, 2, 4, 6, 9, 10, 15):
        period = lcm(wheel, d)
        for center in range(wheel):
            n = 2 * center
            for b in range(d):
                if gcd(b, d) != 1 or gcd(n-b, d) != 1:
                    continue
                hits = sum(gcd(a*(n-a), wheel) == 1
                           for a in range((n-b) % d, period, d))
                expected = F(1, d) * prod(
                    1-F(len({0, n % p}), p) for p in primes if d % p)
                assert F(hits, period) / density**2 == expected / density**2
                cases += 1
    return cases


def convolution():
    wheel = 2*3*5
    def model(n):
        return F(15, 4) if gcd(n, wheel) == 1 else F(0)
    def signal(n):
        return (n**2 + 3*n + 7) % 13
    lower = range(40, 79)
    panels = [range(j, min(j+7, lower.stop)) for j in range(lower.start, lower.stop, 7)]
    for x in range(80, 92):
        mixed = [F(0)] * 4
        direct = 0
        for block in panels:
            for a in block:
                t = 2*x-a
                if t % 3 != 1:
                    continue
                direct += signal(a)*signal(t)
                m, k = model(a), model(t)
                e, f = signal(a)-m, signal(t)-k
                for i, value in enumerate((m*k, e*k, m*f, e*f)):
                    mixed[i] += value
        assert direct == sum(mixed)


def truncations():
    for hits in range(24):
        for r in range(1, 12):
            upper_or_lower = sum((-1)**j * comb(hits, j) for j in range(r))
            other = upper_or_lower + (-1)**r * comb(hits, r)
            assert min(other, upper_or_lower) <= int(hits == 0) <= max(other, upper_or_lower)
            assert abs(other-upper_or_lower) == comb(hits, r)
    assert F(72, 11) - F(1, 2) - 2 > 4
    assert F(4, 4**4) == F(1, 64)
    assert F(1, 1-F(1, 64)) - 1 == F(1, 63)
    assert (F(51, 50) - F(62, 63)) * F(5, 8) < F(23, 1000)


def reflected_prime_intervals():
    limit = 12000
    prime = bytearray([1]) * (limit + 1)
    prime[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p*p::p] = bytes(len(range(p*p, limit + 1, p)))
    cubes = [i**3 for i in range(1, 600)]

    def half_window(x):
        assert x*x < cubes[-1]
        return bisect_right(cubes, x*x)

    def pairs(x):
        return {(a, 2*x-a) for a in range(x-half_window(x), x)
                if prime[a] and prime[2*x-a]}

    packets = 0
    for start in (47, 64, 113, 997, 1024, 10201):
        h = half_window(start)
        for length in (1, 2, 7, 13):
            frozen = {(a, 2*x-a) for x in range(start, start+length)
                      for a in range(start-h, start) if prime[a] and prime[2*x-a]}
            transposed = set()
            for a in range(start-h, start):
                if not prime[a]:
                    continue
                u = 2*start-a
                for m in (u, u+length):
                    transposed.update((a, q) for q in range(m, m+length) if prime[q])
            assert frozen == transposed
            moving = set().union(*(pairs(x) for x in range(start, start+length)))
            restored = {(a, q) for a in range(start-h, start+length) if prime[a]
                        for q in range(2*start-a, 2*(start+length)-a) if prime[q]
                        and 1 <= (q-a)//2 <= half_window((q+a)//2)}
            assert moving == restored
            packets += 1

    assert not pairs(113)  # The diagonal 113+113 lies outside the positive offsets.
    marks = (101, 101**2)
    deleted = {q for s in marks for _, q in pairs(s)}
    cases = 0
    for s in marks:
        assert pairs(s) and all(q in deleted for _, q in pairs(s))
        for x in range(s-45, s+46):
            if x == s:
                continue
            original = pairs(x)
            lost = {pair for pair in original if deleted.intersection(pair)}
            # Integer prime weights n replace log n to make both sums exact.
            lost_weight = sum(a*q for a, q in lost)
            triple_weight = sum(n*(2*x-n) for n in deleted
                                if 1 <= abs(n-x) <= half_window(x)
                                and 1 <= n-s <= half_window(s)
                                and prime[2*x-n] and prime[2*s-n])
            assert lost_weight <= triple_weight <= 2*lost_weight
            cases += 1
    return packets, cases


if __name__ == "__main__":
    cases = local_products()
    convolution()
    truncations()
    packets, off_center = reflected_prime_intervals()
    print(f"Verified {cases} local class factors, 12 panel identities, "
          f"{packets} transposed prime packets, {off_center} off-center deletion bounds, "
          "Bonferroni brackets and the signed excess budget < 0.023.")
