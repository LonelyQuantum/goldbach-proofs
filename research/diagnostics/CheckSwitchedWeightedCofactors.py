"""Exact bounds and finite arithmetic checks for SwitchedWeightedCofactors.md."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import gcd, isqrt

from CheckFixedSquareVaughan import grid_lower, grid_upper, log_bounds, trap_integral
from CheckSharedPrimeCenters import primes_through


ALPHA, DELTA = Q(1, 30), Q(1, 6)
B, ETA, LAM = Q(3, 20), Q(9, 100), Q(7, 3)


def log_interval(x):
    """Reduce the argument before using the existing rational log bounds."""
    extra = 0
    while x > 5:
        x /= 2
        extra += 1
    lo, hi = log_bounds(x)
    l2, u2 = log_bounds(2)
    return lo + extra*l2, hi + extra*u2


def penalty_primitive(s):
    # The second log coefficient is negative.
    a, b = log_interval(s/ALPHA)
    c, d = log_interval((DELTA-ALPHA)/(DELTA-s))
    k = 2*(1/DELTA-1/B)
    return grid_lower(2*a/DELTA+k*d), grid_upper(2*b/DELTA+k*c)


def budget_inputs(cells):
    il, iu = trap_integral(3, True)
    rough = (12*(log_bounds(4)[0]+il), 12*(log_bounds(4)[1]+iu))
    step = Q(1, cells)
    lower = upper = Q(0)
    for i in range(cells):
        left = 2+i*step
        right = left+step
        # The moving upper integration limit decreases as t increases.
        lower += grid_lower(log_bounds(left-1)[0]/right *
                            penalty_primitive(DELTA-ALPHA*(right+1))[0])
        upper += grid_upper(log_bounds(right-1)[1]/left *
                            penalty_primitive(DELTA-ALPHA*(left+1))[1])
    lo, hi = penalty_primitive(B)
    return rough, ((lo+step*lower)/LAM, (hi+step*upper)/LAM)


def switched_bounds(eta, cells):
    c, k = 1-1/LAM, 1/(B*LAM)
    one = tuple(12*(c*log_interval(eta/ALPHA)[i]
                    + (c+k)*log_interval((1-ALPHA)/(1-eta))[i]) for i in (0, 1))
    width = (eta-2*ALPHA)/cells
    lower = upper = Q(0)
    for i in range(cells):
        left = 2*ALPHA+i*width
        right = left+width
        lower += grid_lower((1-(2-left/B)/LAM) * log_bounds((left-ALPHA)/ALPHA)[0]
                            / (right*(1-left)))
        upper += grid_upper((1-(2-right/B)/LAM) * log_bounds((right-ALPHA)/ALPHA)[1]
                            / (left*(1-right)))
    return one, (12*width*lower, 12*width*upper)


def certificate(cells=2048):
    rough, penalty = budget_inputs(cells)
    for eta, target in ((ETA, Q('0.34')), (Q('0.092'), Q('0.03')), (Q('0.093'), None)):
        one, two = switched_bounds(eta, cells)
        if eta == ETA:
            assert rough[0] > Q('16.814') and penalty[1] < Q('6.769')
            assert one[1] < Q('9.297') and two[1] < Q('0.407')
        if target is None:
            assert rough[1]-penalty[0]-one[0]-two[0] < -Q('0.10')
        else:
            assert rough[0]-penalty[1]-one[1]-two[1] > target


def factor_list(n):
    remainder = n
    factors = []
    for p in range(2, isqrt(n)+1):
        while remainder % p == 0:
            factors.append(p)
            remainder //= p
    if remainder > 1:
        factors.append(remainder)
    return factors


def finite_checks():
    # Enlarged finite cutoffs exercise one- and two-prime cofactors at this size.
    center, width, rough_min, limit = 211**2, 800, 5, 150
    low, high = center-width, center-100
    flags = primes_through(2*center)
    direct = {}
    balanced = 0
    for n in range(low, high):
        factors = factor_list(n)
        if len(factors) < 2 or len(set(factors)) != len(factors) or min(factors) <= rough_min:
            continue
        m, largest = n//max(factors), max(factors)
        if m <= limit:
            direct[n] = (m, largest)
        # Verify the canonical-divisor equivalence with T^2 < sqrt(n).
        cutoff = 12
        ds = [d for d in range(cutoff+1, isqrt(n)+1) if n % d == 0]
        assert bool(ds) == (m > cutoff)
        if ds:
            assert ds[0] <= n//ds[0] and ds.count(ds[0]) == 1
            balanced += 1
    switched = {}
    for m in range(rough_min+1, limit+1):
        ff = factor_list(m)
        if len(set(ff)) != len(ff) or min(ff) <= rough_min:
            continue
        for t in range((low+m-1)//m, (high-1)//m+1):
            if flags[t] and t > m:
                n = m*t
                assert n not in switched
                switched[n] = (m, t)
    assert switched == direct and {len(factor_list(m)) for m, _ in direct.values()} == {1, 2}
    moduli = [d for d in range(1, 130) if gcd(2*center, d) == 1]
    coprimality_omissions = 0
    for d in moduli:
        actual = {n for n in direct if (2*center-n) % d == 0}
        predicted = {m*t for m,t in switched.values()
                     if gcd(m,d) == 1 and (m*t-2*center) % d == 0}
        assert actual == predicted
        coprimality_omissions += sum(gcd(m, d)>1 for m, _ in switched.values())
    assert coprimality_omissions
    # Symbolic prime exponents are measured in units of 1/100.
    # Sum <100 represents n<X exactly, including cases at both weight boundaries.
    checked = 0
    for j in range(1, 11):
        for uv in combinations_with_replacement((4, 5, 7, 9, 12, 15, 18, 31, 84, 91), j):
            if sum(uv) != 99:
                continue
            positive = sum(max(0, 15-u) for u in uv) < 35
            if positive:
                assert j <= 8 and sum(uv[:-1]) > 15*j-50
            if j > 1 and sum(uv[:-1]) <= 9:
                assert j in (2, 3) and sum(max(0,15-u) for u in uv) == 15*(j-1)-sum(uv[:-1])
            checked += 1
    assert checked > 0
    return len(direct), len(moduli), balanced, checked


if __name__ == "__main__":
    certificate()
    print("Rational bounds: rough >16.814, penalty <6.769, one-prime cofactor <9.297,"
          " two-prime cofactor <0.407; simultaneous margin >0.34.")
    print("Fixed-weight budget: margin >0.03 at 0.092, below -0.10 at 0.093.")
    print("Finite checks (switched products, moduli, balanced products, exponent patterns):",
          finite_checks())
