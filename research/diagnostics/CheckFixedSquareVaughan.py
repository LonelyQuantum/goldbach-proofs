"""Rational sieve constants and finite divisor identities in FixedSquareVaughan.md."""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import prod


SCALE = 10**12


def grid_lower(x):
    return F(x.numerator * SCALE // x.denominator, SCALE)


def grid_upper(x):
    return -grid_lower(-x)


@lru_cache(None)
def log_bounds(x):
    """Atanh series with a geometric upper bound on its positive tail."""
    x = F(x)
    assert 1 <= x <= 5
    y = (x - 1) / (x + 1)
    power = y
    partial = F(0)
    for j in range(35):
        partial += 2 * power / (2*j + 1)
        power *= y*y
    return grid_lower(partial), grid_upper(partial + 2*power / (71*(1-y*y)))


def trap_integral(end, extra_log):
    # On [2,4] the three factors log(t-1), 1/t, log(4/(1+t)) (last
    # factor used only up to t=3) and each of their first two derivatives
    # have absolute value <=2. The reciprocal and its derivatives are <=1,
    # as are derivatives of both logs. The product rule gives |f''| <=30.
    cells = 1024
    step = F(end-2, cells)
    low = high = F(0)
    for j in range(cells+1):
        t = 2+j*step
        a, b = log_bounds(t-1)
        if extra_log:
            c, d = log_bounds(4/(t+1))
            a, b = a*c, b*d
        weight = F(1, 2) if j in (0, cells) else 1
        low += weight*grid_lower(a/t)
        high += weight*grid_upper(b/t)
    error = 30 * (end-2) * step**2 / 12
    return low*step-error, high*step+error


def constants():
    lo, hi = trap_integral(3, True)
    f = (12*(log_bounds(4)[0]+lo), 12*(log_bounds(4)[1]+hi))
    lo, hi = trap_integral(4, False)
    upper = (12*(1+lo), 12*(1+hi))
    eta = F(251, 3000)
    semi = tuple(12*v for v in log_bounds(4*eta/(F(1, 6)-eta)))
    assert F('16.814') < f[0] <= f[1] < F('16.815')
    assert F('16.872') < upper[0] <= upper[1] < F('16.874')
    assert F('16.731') < semi[0] <= semi[1] < F('16.732')
    assert f[0] - semi[1] > F('0.08')
    positive = F(85, 9)*log_bounds(2)[0]*log_bounds(F(5, 3))[0]**2
    assert positive > F('1.70')


def identity_checks(limit):
    divisors = [[] for _ in range(limit+1)]
    for d in range(1, limit+1):
        for n in range(d, limit+1, d):
            divisors[n].append(d)
    primes = {n for n in range(2, limit+1) if len(divisors[n]) == 2}
    factors = [Counter() for _ in divisors]
    mu = [0, 1] + [0]*(limit-1)
    power_base = [0]*(limit+1)
    for n in range(2, limit+1):
        q = divisors[n][1]
        factors[n] = factors[n//q].copy()
        factors[n][q] += 1
        mu[n] = 0 if factors[n][q] > 1 else -mu[n//q]
        if len(factors[n]) == 1:
            power_base[n] = q

    checked = 0
    mixed_signs = set()
    for cutoff in (3, 7, 15, 35):
        for n in range(cutoff+1, limit+1):
            # Compute each formal coefficient of log(prime) independently.
            coeffs = Counter()
            tail_primes = Counter()
            for m in divisors[n]:
                if not mu[m]:
                    continue
                cofactor = n//m
                if m <= cutoff:
                    for q, exponent in factors[cofactor].items():
                        coeffs[q] += mu[m]*exponent
                for v in divisors[cofactor]:
                    q = power_base[v]
                    if not q:
                        continue
                    if m <= cutoff and v <= cutoff:
                        coeffs[q] -= mu[m]
                    if m > cutoff and v > cutoff:
                        coeffs[q] += mu[m]
                        if v == q:
                            tail_primes[q] += mu[m]
            for q in factors[n]:
                assert coeffs[q] == int(q == power_base[n])
            au = sum(mu[d] for d in divisors[n] if d <= cutoff)
            for q in factors[n]:
                expected = -au if q > cutoff and n not in primes else 0
                assert tail_primes[q] == expected
            small = sorted(q for q in factors[n] if q <= cutoff)
            if small:
                r = small[0]
                assert au == sum(mu[e] for e in divisors[n]
                                 if e % r and e <= cutoff < e*r)
                if len(small) == 1:
                    assert au == 0
                if len(small) == 2:
                    assert au == -int(prod(small) > cutoff)
                if len(small) == 3:
                    assert (au > 0) == (prod(small) > cutoff >= small[1]*small[2])
                if au > 0:
                    assert len(small) >= 3 and r*r <= cutoff
                if any(q > cutoff for q in factors[n]):
                    mixed_signs.add((au > 0)-(au < 0))
            checked += 1
    assert mixed_signs == {-1, 0, 1}
    return checked


if __name__ == "__main__":
    constants()
    checked = identity_checks(6000)
    print(f"{checked} formal logarithm identities and cofactor sign checks passed.")
    print("Rational enclosures: f in (16.814,16.815), F in (16.872,16.874), "
          "semiprime cap in (16.731,16.732); survivor margin >0.08, "
          "positive subfamily >1.70 (normalized units).")
