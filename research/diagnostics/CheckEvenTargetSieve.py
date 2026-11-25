"""Exact checks for EvenTargetsAndFiveFactorRemainder.md (Python standard library)."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt, lcm, prod

from CheckSixFactorSwitch import lower_log_sum


def prime(n):
    return n > 1 and all(n % j for j in range(2, isqrt(n) + 1))


def good_partner(a, z):
    count = 0
    for ell in range(2, isqrt(a) + 1):
        if a % ell == 0:
            if ell < z or a % (ell * ell) == 0:
                return False
            a //= ell
            count += 1
    if a == 1:
        return count <= 6
    return a >= z and count + 1 <= 6


def check_markers():
    classes = genuine = 0
    z = 8
    for X in (101**2, 105, 210, 231, 385, 840, 2310):
        H = min(X - 2, 251)
        for d in (1, 2, 6, 15):
            eligible = [ell for ell in (3, 5, 7) if d % ell]
            bad = [ell for ell in eligible if (2*X) % ell == 0]
            choices = list(product(*(range(1, ell) for ell in bad)))
            multiplicity = prod(ell - 2 for ell in bad)
            if X == 210 and d == 1:
                assert len(choices) == 48 and multiplicity == 15
            for a in range(1, 2*z*z):
                joint_hits = sum(all(a % ell in (0, (-c) % ell)
                                     for ell, c in zip(bad, marks)) for marks in choices)
                predicted = prod(1 if a % ell == 0 else F(1, ell-1) for ell in bad)
                assert joint_hits == len(choices) * predicted
            for b in range(d):
                if gcd(b, d) > 1 or gcd(2*X-b, d) > 1:
                    continue
                offsets = [h for h in range(1, H+1) if (X+h) % d == b
                           and prime(X+h) and good_partner(X-h, z)]
                total = sum(all((X+h) % ell != c for ell, c in zip(bad, marks))
                            for h in offsets for marks in choices)
                assert total == multiplicity * len(offsets)
                classes += 1
                genuine += len(offsets)
    assert genuine > 0
    return classes, genuine


def check_grouped_square(X, d, b):
    # Small cutoffs permit direct enumeration of every divisor and endpoint.
    H, R, z = 97, 14, 7
    primes = [ell for ell in range(2, R) if prime(ell) and d % ell]
    roots = {}
    for ell in primes:
        nres = 2*X % ell
        roots[ell] = {nres}
        if 2 < ell < z:
            marker = nres or 1
            roots[ell].add((nres-marker) % ell)
            assert len(roots[ell]) == 2

    factors = {prod(ss): ss for k in range(len(primes)+1)
               for ss in combinations(primes, k)}
    nu = {n: prod(len(roots[ell]) for ell in ss) for n, ss in factors.items()}
    g = {n: prod((F(len(roots[l]), l-len(roots[l])) for l in ss), start=F(1))
         for n, ss in factors.items()}
    support = [n for n in factors if n < R]
    G = sum(g[n] for n in support)
    coeff = {i: sum((-1)**(len(factors[n//i])+len(factors[n])) * g[n]
                    for n in support if n % i == 0) / (G * F(nu[i], i))
             for i in support}
    assert coeff[1] == 1 and all(abs(v) <= 1 for v in coeff.values())
    C = defaultdict(F)
    for i in support:
        for j in support:
            C[lcm(i, j)] += coeff[i] * coeff[j]

    def hit(a, n):
        return all(a % l in roots[l] for l in factors[n])

    observed = main = error = F(0)
    for q, weight in ((7, F(3, 4)), (11, F(1, 2)), (13, F(1, 3)), (17, F(1, 5))):
        if gcd(q, 2*X*d) > 1:
            continue
        points = [a for a in range(X-H, X) if (2*X-a) % d == b and a % q == 0]
        observed += weight * sum(sum(coeff[i] for i in support if hit(a, i))**2
                                 for a in points)
        local = F(0)
        for n, value in C.items():
            hits = sum(hit(a, n) for a in points)
            if n % q == 0:
                assert hits == 0
                continue
            mean = F(H * nu[n], d*q*n)
            local += value * F(nu[n], n)
            main += weight * value * mean
            error += weight * value * (hits - mean)
            assert abs(hits - mean) <= nu[n]
        assert 0 <= local <= F(q, q-1)/G
    assert observed == main + error

    # Exact product-law lower bound on the optimal denominator.
    doubled = [l for l in primes if 2 < l < z]
    V = prod(1 - F(1, l-1) for l in doubled)
    lower = F(0)
    for L, chosen in factors.items():
        if not set(chosen).issubset(doubled):
            continue
        prob = prod(F(1, l-1) if l in chosen else 1-F(1, l-1) for l in doubled)
        one_root = sum(F(1, prod(l-1 for l in ss)) for n, ss in factors.items()
                       if n*L < R)
        lower += prob * one_root
    assert V*G >= lower


def check_constants():
    A, a, C = F(41, 10), F(7, 9), F(27, 2)
    margin = lower_log_sum([(F(299, 100), F(3)), (-1, F(28, 9)), (-F(1, 2), F(27, 8)),
                            (-C/A, 2/a), (C/A * (A/2-1), (A-a)/(A-2))])
    assert margin > F(1, 60)
    harmonic = sum(F(1, k) for k in range(1, 513))
    assert lower_log_sum([(-9, F(2)), (-1, F(513, 512)), (-1, F(16, 9))], harmonic) > 0
    A, u, C = F(59, 18), F(5, 8), F(25, 2)
    wide = lower_log_sum([(F(63, 25), F(3)), (-1, F(16, 5)),
                          (-F(3, 8), F(15, 4)), (-C/A, F(2)),
                          (C/A * (A*u-1), (A-F(4, 5))/(A-F(8, 5)))])
    assert wide > F(1, 40) and 6 - F(63, 25) - u/F(9, 50) == F(7, 900)


if __name__ == "__main__":
    check_constants()
    classes, offsets = check_markers()
    cases = 0
    for X in (105, 210, 385, 1009):
        for d in (1, 3, 10):
            for b in range(d):
                if gcd(b, d) == gcd(2*X-b, d) == 1:
                    check_grouped_square(X, d, b)
                    cases += 1
    print(f"Exact marker counts for {classes} classes ({offsets} qualifying offsets counted).")
    print(f"Checked {cases} grouped squares, their conditional main terms and denominators.")
    print("Certified the 2/3 main-term margin > 1/60 and unconditional 17/25 margin > 1/40.")
