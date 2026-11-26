"""Exact finite checks for the pair-difference implication."""
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, prod


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def check_wheel():
    primes = (2, 3, 5, 7)
    period = prod(primes)
    units = [a for a in range(period) if gcd(a, period) == 1]
    scale = Fraction(period, len(units))
    for d in range(period):
        density = prod(Fraction(q * (q - len({0, d % q})), (q - 1)**2)
                       for q in primes)
        count = sum(gcd(d - a, period) == 1 for a in units)
        assert scale**2 * count == period * density
        shifted = sum(gcd(a + d, period) == 1 for a in units)
        assert shifted == count
    return period


def check_projection():
    # Finite toy weights. Deleting upper endpoints enforces the hypothesis;
    # the true lower primes and all off-diagonal counts are retained.
    sites = range(1200, 1630)
    targets = (2230, 2242, 2254, 2266, 2278)
    real = [[int(prime(t-a)) for a in sites] for t in targets]
    model = [[Fraction(15, 4) * (gcd(t-a, 30) == 1) for a in sites]
             for t in targets]
    residual = [[p-c for p, c in zip(row, ref)] for row, ref in zip(real, model)]
    four = [int(four_prime_factors(a)) for a in sites]
    checked = 0
    for k in range(1, len(targets)+1):
        for ix in combinations(range(len(targets)), k):
            upper = [int(prime(a) and all(not real[i][j] for i in ix))
                     for j, a in enumerate(sites)]
            assert sum(upper) and sum(four) and dot(upper, four) == 0
            total = [sum(residual[i][j] for i in ix) for j in range(len(sites))]
            assert dot(upper, total) == -sum(dot(upper, model[i]) for i in ix)
            diagonal = sum(dot(residual[i], residual[i]) for i in ix)
            off = sum(dot(real[i], real[j]) - dot(real[i], model[j])
                      - dot(model[i], real[j]) + dot(model[i], model[j])
                      for i in ix for j in ix if i != j)
            assert diagonal + off == dot(total, total)
            projections = dot(upper, total)**2 / sum(upper) + dot(four, total)**2 / sum(four)
            assert off >= projections - diagonal
            checked += 1
    return checked


def four_prime_factors(n):
    count = 0
    d = 2
    while d*d <= n:
        while n % d == 0:
            n //= d
            count += 1
        d += 1
    return count + (n > 1) == 4


def check_differences():
    for p in range(2, 501):
        u = isqrt(p-1)
        gaps = [b*b-a*a for a, b in combinations(range(p, p+u+1), 2)]
        assert len(gaps) == len(set(gaps))
    c_lower = Fraction(3, 4) * Fraction(15, 16) * (1 - Fraction(1, 8))
    assert (2*c_lower)**2 > Fraction(3, 2)


if __name__ == "__main__":
    shifts = check_wheel()
    families = check_projection()
    check_differences()
    print(f"{shifts} local shifts, {families} exact projections, 499 square packets passed")
