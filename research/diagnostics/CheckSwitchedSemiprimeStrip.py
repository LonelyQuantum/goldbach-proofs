"""Rational bounds and finite checks for SwitchedSemiprimeStrip.md."""
from fractions import Fraction as Q
from math import gcd, prod

from CheckFixedSquareVaughan import log_bounds
from CheckLocalizedVaughan import factors
from CheckSharedPrimeCenters import floor_root, primes_through


def constants():
    lo, hi = Q(4, 25), Q(1, 6)
    odds_ratio = hi*(1-lo)/(lo*(1-hi))
    assert odds_ratio == Q(21, 20)
    cap = log_bounds(odds_ratio)[1]
    assert 12*cap < Q(".5855") and 1-12*cap > Q(".4145")
    assert 11*cap < Q(".5367") and Q(".6762")-11*cap > Q(".1395")
    left, right = Q(83, 500), Q(67, 400)
    level_t, level_n = 3*Q(11, 100), 3*Q(1, 18)
    assert right + level_t + level_n < Q(2, 3)
    assert left < hi < right and 6*right > 1
    assert right/left == Q(335, 332)
    factor = (2/level_t)*(2/level_n)
    assert factor == Q(800, 11)
    assert 1-factor*log_bounds(right/left)[1] > Q(".3457")
    print("All strip constants and exponent margins certified by rational bounds.")


def root_periods():
    target = 2*1009**2
    count = 0
    for q in (13, 17, 19, 23):
        for small, extra in (((2, 3, 5), (7, 11)), ((2, 3), (5,))):
            all_primes = small+extra
            period = prod(all_primes)
            actual = sum(gcd(t, period) == 1 and gcd(target-q*t, prod(small)) == 1
                         for t in range(period))
            allowed = prod(ell-len({0, target*pow(q, -1, ell) % ell}) for ell in small)
            assert actual == allowed*prod(ell-1 for ell in extra)
            count += 1
    print(f"{count} complete CRT periods passed, with the shared root at 2.")


def finite_strips():
    x = 1009**2
    h, trim = floor_root(x**2, 3), 2*floor_root(x**21, 40)
    low, stop = x+trim+1, x+h+1
    flags = primes_through(stop)
    qs = [q for q in range(14, 48) if flags[q]]
    direct, switched = set(), set()
    rough, paired = set(), set()
    middle, middle_witnesses, repeated = set(), set(), set()
    for a in range(low, stop):
        n = 2*x-a
        fs = factors(a)
        if len(fs) == 2 and fs[0] in qs:
            direct.add(a)
            if min(factors(n)) > 5:
                rough.add(a)
            if flags[n]:
                paired.add(a)
        if len(fs) >= 2 and fs[0] in qs and min(factors(n)) > 5:
            middle.add(a)
            if fs[1] == fs[0]:
                repeated.add(a)
    for q in qs:
        for t in range((low+q-1)//q, (stop-1)//q+1):
            a = q*t
            if flags[t]:
                assert t > q and a not in switched
                switched.add(a)
            if min(factors(t)) > 11 and min(factors(2*x-a)) > 5:
                middle_witnesses.add(a)
    assert direct == switched and paired < rough < direct
    assert repeated and middle <= middle_witnesses
    print(f"{len(direct)} switched semiprimes, {len(rough)} rough lower partners, "
          f"{len(paired)} prime lower partners; {len(middle)} least-factor sites "
          f"covered, including {len(repeated)} repeated least factors.")


if __name__ == "__main__":
    constants()
    root_periods()
    finite_strips()
