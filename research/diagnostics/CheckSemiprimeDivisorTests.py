"""Finite identities and parameter checks for SemiprimeDivisorTests.md."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, gcd, isqrt, prod

from CheckFixedSquareVaughan import identity_checks
from CheckSharedPrimeCenters import floor_root, primes_through


def exponent_checks():
    beta = Q(7, 36)
    y, length = 1 - beta, Q(2, 3) - beta
    assert length - Q(7, 12) * y == Q(1, 432)
    assert length - Q(11, 20) * y == Q(7, 240) > Q(1, 36)
    assert Q(1, 6) - beta / 2 > Q(7, 240)
    assert min(Q(1, 2) - 5*v/6 for v in (Q(1, 3), Q(1, 2))) == Q(1, 12)
    e_low = sum(Q(1, factorial(j)) for j in range(7))
    e_high = e_low + Q(8, 7 * factorial(7))
    assert Q(3, 20) < Q(301, 2000) < 14 / (29 * e_high + 14)
    assert 14 / (29 * e_low + 14) < Q(151, 1000)
    # The lower band's lower odds are 14/(29e).
    assert (beta / (1 - beta)) / Q(14, 29) == Q(1, 2)


def lower_factor_in_bands(x, q):
    if q**3 >= x:
        return q*q <= x
    if q**36 > x**7 or q**2000 <= x**301:
        return False
    # These finite examples have no prime in the rational bracket around alpha.
    assert q**1000 >= x**151
    return True


def check_factors_and_screen(p):
    x = p*p
    h = floor_root(x**2, 3)
    trim = 2 * floor_root(x**21, 40)
    low, stop = x - h, x - trim
    prime = primes_through(x + h)
    small = [q for q in range(2, isqrt(stop) + 1) if prime[q]]
    pairs = {}
    for q in small:
        if not lower_factor_in_bands(x, q):
            continue
        first = max(q + 1, (low + q - 1) // q)
        for t in range(first, (stop - 1) // q + 1):
            if prime[t]:
                assert q*t not in pairs
                pairs[q*t] = (q, t)

    primes_in_window = []
    for n in range(low, stop):
        if prime[n]:
            primes_in_window.append(n)
            assert n not in pairs
            continue
        q = next(q for q in small if n % q == 0)
        t = n // q
        qualifies = q < t and prime[t] and lower_factor_in_bands(x, q)
        assert (n in pairs) == bool(qualifies)

    for d in range(1, 38):
        switched = Counter()
        for q in small:
            if not lower_factor_in_bands(x, q) or gcd(q, d) > 1:
                continue
            residue = 2*x * pow(q, -1, d) % d
            start = max(q + 1, (low + q - 1) // q)
            start += (residue - start) % d
            for t in range(start, (stop - 1) // q + 1, d):
                if prime[t]:
                    switched[q*t] += 1
        expected = {n: 1 for n, (q, _) in pairs.items()
                    if (2*x - n) % d == 0 and gcd(q, d) == 1}
        assert switched == expected

    sieve_primes = (3, 5, 7, 11, 13)
    for sites in (primes_in_window, pairs):
        rough = sum(all((2*x-n) % ell for ell in sieve_primes) for n in sites)
        partial = 0
        for j in range(len(sieve_primes) + 1):
            for subset in combinations(sieve_primes, j):
                modulus = prod(subset)
                partial += (-1)**j * sum((2*x-n) % modulus == 0 for n in sites)
            assert partial <= rough if j % 2 else partial >= rough
        assert partial == rough
    return len(pairs)


def check_smoothing():
    x, h, trim, z = 101**2, 470, 250, 3
    low, high = x - h - 1, x - trim - 1
    prime = primes_through(high + z)
    moduli = (1, 2, 5, 11)
    tests = 0
    for m in range(22, 30):
        a, b = Q(low, m), Q(high, m)
        integers = range(int(a) + 1, int(b + z) + 1)
        cuts = sorted({a, b, *(Q(j) for j in integers if a < j < b)})
        for d in moduli:
            for r in range(d):
                sites = [t for t in integers if prime[t] and t % d == r]
                # Integrate the count by cutting the y-axis at its jumps.
                integral = sum((v-u) * sum(u < t <= u+z for t in sites)
                               for u, v in zip(cuts, cuts[1:]))
                # Independently integrate by interchanging the t and y sums.
                by_site = sum(max(0, min(b, t) - max(a, t-z)) for t in sites)
                assert integral == by_site
                actual = sum(a < t <= b for t in sites)
                assert abs(by_site / z - actual) <= 2 * (1 + Q(z, d))
                tests += 1
    # The overlap changes only at endpoints. Test boundaries and open cells.
    ends = sorted({Q(n, m) for m in range(22, 30) for n in (low, high)})
    for y in ends + [(u+v)/2 for u, v in zip(ends, ends[1:])]:
        overlap = sum(low < m*y <= high for m in range(22, 30))
        assert overlap <= 1 + Q(high - low, 1) / y
    return tests


if __name__ == "__main__":
    exponent_checks()
    centers = (101, 211, 401, 1009)
    counts = [check_factors_and_screen(p) for p in centers]
    print(f"Semiprime counts at squares of {centers}: {counts}; "
          f"{37*len(centers)} reflected-modulus checks.")
    print(f"{check_smoothing()} rational smoothing checks; endpoint overlaps passed.")
    print(f"{identity_checks(1200)} exact Vaughan logarithm identities passed.")
