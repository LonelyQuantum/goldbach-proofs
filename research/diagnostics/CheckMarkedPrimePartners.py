"""Rational constants, local densities and marked-factor identities."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, prod

from CheckFixedSquareVaughan import grid_lower, grid_upper, log_bounds, trap_integral
from CheckLocalizedVaughan import factors
from CheckSharedPrimeCenters import floor_root


def euler_exp_bounds():
    n = 8192
    lower_h = sum(grid_lower(Q(1, j)) for j in range(1, n + 1))
    upper_h = sum(grid_upper(Q(1, j)) for j in range(1, n + 1))
    log2_lo, log2_hi = log_bounds(2)
    lo = lower_h - 13*log2_hi - Q(1, n)
    hi = upper_h - 13*log2_lo
    assert 0 < lo < hi < 1
    lower_e = sum(lo**j / factorial(j) for j in range(14))
    upper_e = sum(hi**j / factorial(j) for j in range(14)) + Q(2, factorial(14))
    return grid_lower(lower_e), grid_upper(upper_e)


def constants():
    lo, hi = euler_exp_bounds()
    u, v, lam = Q(921, 10000), Q(923, 10000), Q(1, 30)
    s = (Q(1, 6) - v)/lam
    r_lower = 2*lo*log_bounds(s - 1)[0]/s
    assert s == Q(2231, 1000) and r_lower > Q('.331')
    c_upper = hi / (30*log_bounds(v/u)[0])
    assert 11*u > 1 and r_lower/(10*c_upper) > Q('.0012')
    assert v + Q(1, 10) + Q(14, 30) < Q(2, 3)
    r4_upper = 1 + trap_integral(4, False)[1] - log_bounds(4)[0] - trap_integral(3, True)[0]
    gap = Q(1, 10500)
    assert 2*hi*r4_upper/(7*6*5) < gap
    error = 2*gap*(1 + gap)
    i_lower = trap_integral(3, True)[0]
    for eta, threshold in ((Q(1, 15), '.25'), (Q(1, 12), '.17'), (Q(1, 10), '.004')):
        s_star = 5 - 30*eta
        main = r_lower + 12*log_bounds(4)[0] + 10*i_lower - 2*log_bounds(4/s_star)[1]
        result = main - (30/lo)*(1 - (eta-lam) + error*(1 + eta-lam))
        assert result > Q(threshold)
        digits = result.numerator * 10000 // result.denominator
        print(f"eta={eta}, certified lower coefficient > {digits//10000}.{digits%10000:04d}")


def crt_counts():
    # Count in a complete period; 2 is a coincident root on the two endpoints.
    target = 2*101**2
    sieve = (2, 3, 5, 7)
    cases = 0
    for q, r in product((11, 13), (1, 11, 13, 17)):
        period = prod(sieve)*q*(r if r != q else 1)
        actual = sum((target-n) % r == 0 and all(n % ell and (target-n) % ell for ell in sieve)
                     for n in range(0, period, q))
        expected = 0 if r == q else prod(ell - len({0, target % ell}) for ell in sieve)
        assert actual == expected
        cases += 1
    for hits1, hits2 in product(range(7), repeat=2):
        def bracket(hits):
            upper = 1 - hits + comb(hits, 2)
            return upper - comb(hits, 3), upper
        low1, high1 = bracket(hits1)
        low2, high2 = bracket(hits2)
        exact = int(hits1 == hits2 == 0)
        assert low1*high2 + high1*low2 - high1*high2 <= exact <= high1*high2
    return cases


def marked_identity():
    # Toy cutoffs deliberately place several marks and squares in a small window.
    x, z, c = 1009**2, 5, Q(5, 4)
    low, stop = x - floor_root(x**2, 3), x - 2*floor_root(x**21, 40)
    checked = multi = squareful = 0
    for n in range(low, stop):
        a = 2*x - n
        fs = factors(n)
        af = Counter(factors(a))
        p_lower = int(len(fs) == 1)
        p_upper = int(len(af) == 1 and sum(af.values()) == 1)
        lower_marks = set(fs).intersection((11, 13, 17))
        weight = c*len(lower_marks) if min(fs) > z and len(set(fs)) == len(fs) else 0
        multi += int(weight > c)
        rough_squarefree = int(min(af) > z and max(af.values()) == 1)
        squareful += int(min(af) > z and max(af.values()) > 1)
        for y in (7, 17, 23):
            for ell, mult in af.items():
                # Identity (3) with log(a) replacing L and squarefree on both
                # rough screens. Compare the coefficient of each log(ell).
                large = int(rough_squarefree and not p_upper and ell > y)
                small = int(rough_squarefree and z < ell <= y)
                lhs = mult*p_lower*p_upper - (weight-p_lower)*large
                rhs = mult*weight*p_upper + (p_lower-weight)*(mult*rough_squarefree-small)
                assert lhs == rhs
                checked += 1
    assert multi and squareful
    return checked, multi, squareful


if __name__ == "__main__":
    constants()
    print(f"{crt_counts()} CRT periods and 49 vector-sieve sign checks passed.")
    checks, multiple, squares = marked_identity()
    print(f"{checks} formal log coefficients passed, with {multiple} multiply tagged "
          f"lower sites and {squares} rough squareful upper sites at toy cutoffs.")
