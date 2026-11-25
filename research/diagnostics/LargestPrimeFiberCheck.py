"""Exact finite checks for the largest-prime grouping and mask threshold."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def check_constants():
    positive_product = negative_product = Fraction(1)
    partial = Fraction(0)
    for ell in range(3, 1002, 2):
        if prime(ell):
            weight = Fraction(1, (ell - 1) ** 2)
            partial += positive_product * weight
            positive_product *= Fraction(ell, ell - 1)
            negative_product *= 1 - weight
    c_low = partial
    c_high = partial + positive_product / 1000
    twin_low = negative_product * (1 - Fraction(1, 2000))
    twin_high = negative_product
    k_low = (5 * twin_low - 3 * c_high - 1) / 4
    k_high = (3 * twin_high - c_low - 1) / 2
    assert Fraction(1, 5) < k_low <= k_high < Fraction(1, 4)
    print("K in millionths, rounded outwards:",
          k_low * 10**6 // 1, -(-k_high * 10**6 // 1))


def check_fibers():
    counts = 0
    for p in (1009, 1013):
        n = 2 * p**2
        for q in range(3, 351):
            if any(q % (d*d) == 0 for d in range(2, isqrt(q) + 1)):
                continue
            ell = max(d for d in range(3, q + 1, 2) if q % d == 0 and prime(d))
            t = q // ell
            common = gcd(t, 2)
            s = t // common
            residual = []
            for r in range(t):
                if gcd(r, t) != 1:
                    continue
                lifts = list(range(r, q, t))
                missing, = [a for a in lifts if gcd(a, q) != 1]
                phases = [(-n*a) % q for a in lifts]
                assert len(set(phases)) == ell and len({b % t for b in phases}) == 1
                assert missing % ell == 0
                b = missing // ell
                reduced = (-n // common * b) % s
                assert (-n*b) % t == reduced * common
                residual.append(reduced)
                counts += 1
            assert sorted(residual) == [a for a in range(s) if gcd(a, s) == 1]
    print("verified fibers:", counts)


def check_mask_identity():
    cases = 0
    for length in range(1, 5):
        for values in product((-2, 0, 1), repeat=length):
            coarse = min(0, sum(values))
            fine = sum(min(0, v) for v in values)
            for denominator in (2, 3):
                for spread in range(denominator + 1):
                    predicted = (denominator - spread) * coarse + spread * fine
                    feasible = (weights for weights in product(range(denominator + 1),
                                                                repeat=length)
                                if max(weights) - min(weights) <= spread)
                    actual = min(sum(w*v for w, v in zip(weights, values))
                                 for weights in feasible)
                    assert predicted == actual
                    cases += 1
    print("verified finite mask optima:", cases)


if __name__ == "__main__":
    check_constants()
    check_fibers()
    check_mask_identity()
