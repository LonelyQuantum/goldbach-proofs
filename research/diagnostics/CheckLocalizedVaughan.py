"""Rational enclosures and finite identities for LocalizedVaughanComparison.md."""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, isqrt, prod

from CheckFixedSquareVaughan import grid_lower, grid_upper, log_bounds, trap_integral
from CheckSharedPrimeCenters import floor_root, primes_through


def certify_constants():
    c, b = Q(17, 50), Q(33, 200)
    step = (Q(1, 2) - c) / 512
    low = high = Q(0)
    for j in range(512):
        u = c + j * step
        v = u + step
        # Both numerator and denominator increase on this interval.
        low += step * grid_lower((1 + log_bounds(6*u - 1)[0]) / (v*(1-v)))
        high += step * grid_upper((1 + log_bounds(6*v - 1)[1]) / (u*(1-u)))
    assert Q('.92') < low < high < Q('.93')
    odds_b = b / (1 - b)
    for a, is_lower in [(Q('.154'), True), (Q('.156'), False)]:
        lower_log, upper_log = log_bounds(odds_b*(1-a)/a)
        if is_lower:
            assert 1 - low < lower_log
        else:
            assert upper_log < 1 - high

    def rho_upper(u):
        return 1 - log_bounds(u)[0] + trap_integral(u, False)[1]

    r4 = 1 + trap_integral(4, False)[1] - log_bounds(4)[0] - trap_integral(3, True)[0]
    assert r4 < Q('.005')
    assert rho_upper(Q(5, 2)) < Q('.131') and rho_upper(Q(3)) < Q('.05')
    assert Q(70, factorial(9)) + 2*r4/5 < Q('.0022')
    assert 10*r4 + 2*rho_upper(Q(3)) < Q('.15')
    assert 10*r4 + 2*rho_upper(Q(5, 2)) < Q('.312')
    assert Q(7, 240) - Q(1, 72) == Q(11, 720)
    print("Rational enclosures for the composite bands and all three error bounds passed.")


@lru_cache(None)
def factors(n):
    result = []
    q = 2
    while q*q <= n:
        while n % q == 0:
            result.append(q)
            n //= q
        q += 1
    if n > 1:
        result.append(n)
    return tuple(result)


@lru_cache(None)
def divisors(n):
    ds = [1]
    for q, exponent in Counter(factors(n)).items():
        ds = [d*q**j for d in ds for j in range(exponent+1)]
    return ds


def mobius(n):
    fs = factors(n)
    return (-1)**len(fs) if len(fs) == len(set(fs)) else 0


def check_columns():
    cases = 0
    for z, y in ((3, 7), (5, 17), (11, 23)):
        for a in range(50, 1601):
            removed, short_model, high = Counter(), Counter(), Counter()
            for k in divisors(a):
                fs = factors(k)
                if k <= z or len(set(fs)) != 1:
                    continue
                q, j = fs[0], a // k
                if z < k <= y:
                    removed[q] += sum(mobius(e) for e in divisors(j) if e > z)
                    short_model[q] -= sum(mobius(e) for e in range(1, z+1) if a % (e*k) == 0)
                elif j > z:
                    high[q] += sum(mobius(e) for e in divisors(j) if e > z)
            keys = set(factors(a))
            assert all(removed[q] == short_model[q] for q in keys)
            fs = factors(a)
            if min(fs) > z and len(fs) == len(set(fs)):
                for q in fs:
                    assert high[q] == -int(len(fs) > 1 and q > y)
                    # Formal coefficient of log(q) in log(a)*P(a) + log(a)*W(a)
                    # with the normalization in this finite identity taken as log(a).
                    assert int(len(fs) == 1) - high[q] == 1 - int(z < q <= y)
            cases += 1
    print(f"{cases} column identities checked coefficient by coefficient in log(prime).")


def small_band(x, q):
    if q**200 > x**33 or q**500 <= x**77:
        return False
    # No boundary prime in the selected finite examples lies in the enclosure.
    assert q**250 >= x**39
    return True


def check_composites(p):
    x = p*p
    low = x - floor_root(x**2, 3)
    stop = x - 2*floor_root(x**21, 40)
    flags = primes_through(x)
    products = {}
    for m in range(2, isqrt(low-1)+1):
        fs = factors(m)
        short = flags[m] and small_band(x, m)
        balanced = (m**50 >= x**17 and
                    (flags[m] or (len(fs) == 2 and fs[0] < fs[1] and fs[0]**6 > x)))
        if short or balanced:
            for t in range((low+m-1)//m, (stop-1)//m + 1):
                if flags[t]:
                    assert t > m and m*t not in products
                    products[m*t] = m

    counts = Counter()
    for n in range(low, stop):
        fs = factors(n)
        m = prod(fs[:-1])
        short = len(fs) == 2 and fs[0] < fs[1] and small_band(x, fs[0])
        balanced = (len(fs) in (2, 3) and len(set(fs)) == len(fs) and
                    m**50 >= x**17 and m*m < low and
                    (len(fs) == 2 or fs[0]**6 > x))
        assert products.get(n) == (m if short or balanced else None)
        if n in products:
            assert fs[0]**20 > x**3
            counts[len(fs)] += 1
    return counts


if __name__ == "__main__":
    certify_constants()
    check_columns()
    totals = Counter()
    for p in (101, 211, 401, 1009):
        totals.update(check_composites(p))
    assert totals[2] and totals[3]
    print(f"Unique lower products in four square windows: {totals[2]} with two factors, "
          f"{totals[3]} with three.")
