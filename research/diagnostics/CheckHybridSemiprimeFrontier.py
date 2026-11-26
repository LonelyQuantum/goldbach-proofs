"""Exact finite checks for HybridSemiprimeFrontier.md (standard library)."""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import gcd, prod

from CheckProperDivisorScales import additive_log, data
from CheckSemiprimeRecords import factors, sieve


@lru_cache(None)
def phi(n):
    value = n
    for prime in set(factors(n)):
        value -= value // prime
    return value


@lru_cache(None)
def primitive_kernel(f, difference):
    # On units, Mobius inversion of character orthogonality at divisors of f.
    return sum(data(f // e)[1] * phi(e)
               for e in data(f)[0] if difference % e == 0)


def check_projectors():
    tests = 0
    for m in range(1, 101):
        for target in (14, 33, 50, 103):
            if gcd(m, target) > 1:
                continue
            for b in range(1, m + 1):
                if gcd(b, m) > 1:
                    continue
                recovered = sum(primitive_kernel(f, target - b) for f in data(m)[0])
                assert recovered == phi(m) * ((target - b) % m == 0)
                tests += 1
    return tests


def complementary_kernel(m, difference, cutoff):
    return sum(data(e)[1] * phi(e) *
               sum(data(v)[1] for v in data(m // e)[0] if v*cutoff < m)
               for e in data(m)[0] if difference % e == 0)


def check_conductor_switch():
    tests = 0
    for m in range(1, 131):
        if not data(m)[1]:
            continue
        for diff in data(m)[0]:  # The kernels depend only on gcd(m, N-b).
            for cutoff in sorted({1, 7, 13, m, *data(m)[0]}):
                high = sum(primitive_kernel(f, diff) for f in data(m)[0] if f > cutoff)
                assert data(m)[1] * high == complementary_kernel(m, diff, cutoff)
                tests += 1
    return tests


def check_window(n, threshold, order, prime_floor=22):
    left, right = n // 2 - 850, n // 2 - 25
    primes = [p for p, flag in enumerate(sieve((right - 1) // prime_floor))
              if flag and p >= prime_floor and n % p]
    rough_d = [d for d in range(6, prime_floor)
               if gcd(d, 30 * n) == 1 and data(d)[1]]
    wheel = prod(p for p in (2, 3, 5) if n % p)
    small = [j for j in data(wheel)[0] if data(j)[2] <= order]
    cutoff = 11
    exact = truncated = exceptional = boundary = 0
    for b in range(left, right):
        ps = factors(b)
        a = n - b
        if (len(ps) != 2 or ps[0] == ps[1] or min(ps) < prime_floor
                or gcd(b, n) != 1 or not data(a)[1]):
            continue
        weights = sum(additive_log(r) * data(d)[1] * additive_log(d)
                      for r in ps for d in data(a)[0] if d in rough_d and d*r <= threshold)
        if weights:
            boundary += sum(d*r == threshold for r in ps for d in rough_d if a % d == 0)
        wheel_sum = sum(data(j)[1] for j in small if a % j == 0)
        exact += weights * (gcd(a, wheel) == 1)
        truncated += weights * wheel_sum
        if data(gcd(a, wheel))[2] > order:
            exceptional += weights * (wheel_sum - (gcd(a, wheel) == 1))
        else:
            assert wheel_sum == (gcd(a, wheel) == 1)

    # Independent enumeration over d,j and ordered primes. The cutoff depends
    # on d. Primitive characters are summed exactly by the integer kernel.
    by_f = defaultdict(Fraction)
    moduli = set()
    for d in rough_d:
        for j in small:
            m = d*j
            assert m not in moduli
            moduli.add(m)
            coeff = data(d)[1] * additive_log(d) * data(j)[1]
            for r in primes:
                if d*r > threshold:
                    continue
                for t in primes:
                    b = r*t
                    if r == t or not left <= b < right or not data(n-b)[1]:
                        continue
                    assert gcd(m, b*n) == 1
                    for f in data(m)[0]:
                        kernel = primitive_kernel(f, n-b)
                        by_f[f] += Fraction(coeff * additive_log(r) * kernel, phi(m))

    low = sum(mass for f, mass in by_f.items() if f <= cutoff)
    high = sum(mass for f, mass in by_f.items() if f > cutoff)
    assert low + high == truncated == exact + exceptional
    return exact, low, high, exceptional, boundary


if __name__ == "__main__":
    count = check_projectors()
    cases = [(n, z, order) for n in (9806, 10018, 10202) for z in (7*31, 900, 2100)
             for order in (0, 1, 2, 3)]
    results = [check_window(*args) for args in cases]
    assert any(row[0] and row[1] and row[2] for row in results)
    assert any(row[3] for row in results)
    assert sum(row[4] for row in results) > 0
    assert all(results[i][3] == 0 for i, args in enumerate(cases) if args[2] >= 2)
    switches = check_conductor_switch()
    print(f"{count} unit-class projectors; {switches} conductor switches; {len(cases)} exact weighted windows")
    print("Example (N, Z, wheel order):", (10018, 900, 2))
    print("arithmetic, low, high, wheel error, cutoff equalities:",
          check_window(10018, 900, 2))
