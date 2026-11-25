"""Rigorous tail constants and finite wheel checks. Run with Python 3."""

from fractions import Fraction as F
from math import ceil, floor, gcd, lcm, prod

from CheckCentralFive import sieve_table, upper_integral
from CheckSixFactorSwitch import log_bounds, lower_log_sum


def constants():
    grid, scale = 2400, 10**12
    lower_sieve, upper = sieve_table(grid, scale)
    u, start, split = F(11, 20), F(1, 6), F(2, 3)

    def small_upper(left, right):
        return (1/left-u) * F(upper[ceil(6*grid*(1-left))], scale) / (1-right)

    small_hi = upper_integral(start, split, grid, scale, small_upper)
    # At i/grid >= 2 each increment of log(s-1) is at least 1/(i-grid).
    log_lo = [0] * (5*grid+1)
    for i in range(2*grid+1, len(log_lo)):
        log_lo[i] = log_lo[i-1] + scale // (i-grid)
    width = (split-start)/grid
    small_lo = 0
    for j in range(grid):
        left, right = start+j*width, start+(j+1)*width
        value = F(log_lo[floor(6*grid*(1-right))], scale)
        small_lo += floor(scale * width * (1/right-u) * value / (1-left))
    small_lo = F(small_lo, scale)
    assert small_lo > F(167, 100) and small_hi < F(206, 100)
    assert F(169, 100)*lower_sieve > F(284, 100)

    harmonic = sum(F(1, k) for k in range(1, 513))
    assert lower_log_sum([(-9, F(2)), (-1, F(513, 512)), (-1, F(16, 9))],
                         harmonic) > 0
    _, log_hi = log_bounds(1/(u*split))
    ideal_hi = F(27, 16)*(log_hi-1+u*split)
    assert ideal_hi < F(5, 8)
    radius = 3 * (4-1/u)
    assert radius == F(72, 11)
    two_root = 1+1/(radius-2)**2
    one_root = 1+F(1, 2)/(radius-1)**2
    assert two_root < F(21, 20) and one_root < F(51, 50)
    assert F(21, 20)*F(5, 8)+F(11, 100) < F(77, 100)
    assert F(7, 6)*F(21, 20)*F(5, 8) < F(77, 100)
    assert F(51, 50)*F(5, 8) < F(64, 100)
    assert 1-F(64, 77) > F(1, 6)
    print(f"Small contribution is bracketed by {small_lo} and {small_hi} at leading order.")
    print(f"Minimum radius exponent {radius}; Cantelli factors {one_root} and {two_root}.")


def wheels():
    def phi(n):
        return sum(gcd(j, n) == 1 for j in range(n))

    cases = 0
    for d in (1, 2, 3, 4, 6, 9, 10):
        for primes in ((), (3,), (5,), (3, 5), (5, 7)):
            w = prod(primes)
            if gcd(d, w) > 1:
                continue
            m, mod_a = d*w, lcm(2, d*w)
            normalization = F(2*m*phi(d), phi(2*m)*mod_a)
            target = prod((F(p-2, p-1) for p in primes), start=F(1))
            for c in range(m):
                marker = prod((F(p-1, p-2) for p in primes if c % p == 0), start=F(1))
                for b in range(d):
                    if gcd(b, d) != 1 or gcd(2*c-b, d) != 1:
                        continue
                    actual = sum((2*c-a-b) % d == 0 and gcd(a*(2*c-a), w) == 1
                                 for a in range(1, mod_a, 2))
                    assert normalization * actual / marker == target
                    cases += 1
    print(f"Enumerated {cases} center/prime classes for the wheel identity.")


if __name__ == "__main__":
    constants()
    wheels()
