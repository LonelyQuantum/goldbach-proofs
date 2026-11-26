"""Directed bounds for the three-factor strip and its mixed Selberg debit."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement

from CheckCompositePartnerWeight import log_bounds


def ceil_div(a, b):
    return -(-a // b)


def log_sandwich():
    lam_lo, lam_hi = log_bounds(5)
    i_lo, i_hi = log_bounds(65)
    assert lam_lo > 0 and i_hi < 1
    return lam_hi / (100*i_lo)


def prefix_profile(w, values):
    return sum((-1)**size * max(0, w-sum(group))
               for size in range(4) for group in combinations(values, size))


def max_product_times_four(a, c, r, delta):
    # Twice the maximizing t, allowing the vertex to be a half-integer.
    t2 = min(2*r, max(2*delta, a+delta+c))
    return max(0, 2*a-max(0, t2-2*delta)) * max(0, t2-2*c)


def finite_checks():
    count = 0
    for scale in (24, 36):
        for delta in range(3, scale//5+1):
            for x, p, v in combinations_with_replacement(range(1, scale+1), 3):
                total = x+p+v
                gm = prefix_profile(scale-delta, (x,p,v))
                gp = prefix_profile(scale, (x,p,v))
                if not 2*(scale-delta) <= total <= 2*scale:
                    assert gm*gp >= 0
                    continue
                for y, missing in ((p,v),(v,p)):
                    t = scale-missing
                    a = min(x, max(0, x+y-scale+delta))
                    c = max(0, x+y-scale)
                    assert gm == a-min(x,max(0,t-delta))
                    assert -gp == min(x,t)-c
                    r = min(x,scale-x)
                    assert 4*max(0,-gm*gp) <= max_product_times_four(a,c,r,delta)
                    count += 1
    return count


def log_bounds_integer(n):
    def twice_atanh(t):
        terms = sum(t**(2*j+1)/(2*j+1) for j in range(8))
        return 2*terms, 2*(terms+t**17/(17*(1-t*t)))
    shift = n.bit_length()-1
    low2, high2 = twice_atanh(F(1,3))
    t = F(n-2**shift,n+2**shift)
    low, high = twice_atanh(t)
    return shift*low2+low, shift*high2+high


def arithmetic_record():
    from math import gcd, isqrt, prod

    def prime(n):
        return n >= 2 and all(n%j for j in range(2,isqrt(n)+1))

    large = 2**61-1
    factors = (2,3,3,5,5,7,11,13,31,41,61,151,331,1321)
    assert prod(factors) == large-1 and all(prime(p) for p in set(factors))
    assert pow(37,large-1,large) == 1
    assert all(pow(37,(large-1)//p,large) != 1 for p in set(factors))
    # Thus 37 has order large-1 modulo large, forcing large to be prime.
    reflected = (29,37,43)
    tags = (3,31,409)
    r, n = 87958907, 31798879949
    assert all(prime(p) for p in reflected+tags+(r,n))
    d, P = prod(reflected), prod(tags)
    a, bpos = d*large, r*P*n
    s = (a+bpos)//2
    assert 2*s == a+bpos and gcd(a,bpos) == 1
    assert (s-bpos)**3 <= s*s and ((s-bpos)//2)**40 > s**21
    assert r**50 > s**17 and r**20 <= s**7
    assert all(p**16>s and p**40<=s**3 for p in reflected)
    ls0, ls1 = log_bounds_integer(s)
    assert 52 < ls0 < ls1 < 54
    low = 52/log_bounds_integer(54)[1]**3
    high = 54/log_bounds_integer(52)[0]**3
    assert log_bounds_integer(2)[1] < low <= high < log_bounds_integer(3)[0]
    # z is between two and three. The starred support is odd and squarefree.
    Q = (1<<r.bit_length())*(1<<d.bit_length())**2
    for exponent, rad in ((97,193),(101,560)):
        assert (Q*rad**2)**100 <= s**exponent < (Q*(rad+1)**2)**100
    assert s**97 <= (Q*P)**100 <= s**101
    def root(rad):
        harmonics = weighted = F(0)
        for j in range(1,rad+1,2):
            primes = [p for p in range(3,j+1,2) if j%p==0 and prime(p)]
            if any(j%(p*p)==0 for p in primes):
                continue
            weight = F(1,prod(p-1 for p in primes))
            harmonics += weight
            weighted += weight*prod(1-p for p in primes if p in tags)
        return weighted/harmonics
    fm, fp = root(193), root(560)
    assert F(3675,100000) < fm < F(3676,100000)
    assert -F(26382,100000) < fp < -F(26381,100000)
    return s


def certificate(n=768, panels=64):
    # The sole rounding unit for the inner integrals. Python integers do not overflow.
    unit = 10**13
    assert n % 4 == 0

    @lru_cache(None)
    def integrals(d):
        assert 0 < 5*d < n
        # Returns the integrals before the outer factor q/(2b).
        debit = ceil_div(4*unit, n*n)  # 0 <= X < 1/n
        raw_quarter = 0
        for i in range(1, 2*n//3+1):
            for j in range(max(i, n-2*d-i-2), min(n-1, 2*n-2*i)+1):
                den = 4*n-d-2*(i+j+2)
                assert den > 0
                if i >= n//4:
                    raw_quarter += ceil_div(4*n*unit, den*i*j)
                a = min(i+1, max(0,i+j+2-n+d))
                c = max(0,i+j-n)
                r = min(i+1,n-i)
                value4 = max_product_times_four(a,c,r,d)
                debit += ceil_div(unit*value4, (n-d)*den*i*j)
        # Leading small-X logarithm: a right upper bound for the reciprocal
        # sieve radius and a left upper bound for the prime harmonic weight.
        raw_log = 0
        for j in range(n-2*d, n):
            raw_log += ceil_div(4*n*unit, j*(4*n-d-2*(j+1)))
        return (debit, raw_quarter, raw_log)

    # A log-uniform exponent on [1/16,3/40] is stochastically dominated
    # by a uniformly distributed exponent on the same interval.
    bins = Counter({0: 1})
    for weight in (2,5,5,5):
        updated = Counter()
        for a, mass in bins.items():
            for j in range(1, panels+1):
                updated[a+weight*j] += mass
        bins = updated
    q = log_sandwich()
    totals = [F(0)]*3
    for index, mass in bins.items():
        b = F(59*panels-index, 400*panels)
        d = F(n,50)/b
        vals = integrals(ceil_div(d.numerator,d.denominator))
        for j,value in enumerate(vals):
            totals[j] += F(mass*value, unit*panels**4)*q/(2*b)
    return [ceil_div(t.numerator*10**6,t.denominator) for t in totals]


if __name__ == "__main__":
    print("ordered profile checks:", finite_checks())
    print("genuine mixed-sign record at s =", arithmetic_record())
    values = certificate()
    assert all(value <= cap for value, cap in zip(values, (23287,862723,340225)))
    assert F(23287,32427) < F(7182,10000) and 32427-23287 == 9140
    print("directed upper bounds in millionths (debit, quarter strip, raw log):", values)
