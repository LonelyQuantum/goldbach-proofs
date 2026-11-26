"""Exact finite checks for SignedDivisorsAtSmallerTargets.md (standard library)."""

from collections import Counter
from fractions import Fraction
from math import gcd, lcm, prod

from CheckSemiprimeRecords import factors, floor_power, sieve


def divisor_tables(limit):
    """An additive integer weight in place of log, so every equality is exact."""
    weight = [0] * (limit + 1)
    mangoldt = [0] * (limit + 1)
    signed = [[] for _ in weight]
    for n in range(2, limit + 1):
        fs = factors(n)
        weight[n] = sum(2 * p - 1 for p in fs)
        if len(set(fs)) == 1:
            mangoldt[n] = 2 * fs[0] - 1
        if len(fs) != len(set(fs)):
            continue
        coeff = (-1) ** (len(fs) + 1) * weight[n]
        for multiple in range(n, limit + 1, n):
            signed[multiple].append((n, coeff))
    assert all(sum(c for _, c in ds) == mangoldt[n] for n, ds in enumerate(signed))
    return mangoldt, signed


def divisor_partition():
    mangoldt, signed = divisor_tables(700)
    cases = positions = proper_lcm = negative = higher_powers = 0
    for n in range(202, 901, 16):
        for wheel, cutoff, modulus_limit in ((2, 3, 52), (6, 5, 80), (30, 7, 120)):
            cases += 1
            for a in range(n // 2 + 1, n // 2 + 60):
                b = n - a
                if gcd(a * b, wheel) != 1:
                    continue
                short_a = sum(c for d, c in signed[a] if d <= cutoff)
                short_b = sum(c for e, c in signed[b] if e <= cutoff)
                medium = tail = 0
                for d, cd in signed[a]:
                    for e, ce in signed[b]:
                        assert n % gcd(d, e) == 0
                        if min(d, e) <= cutoff:
                            continue
                        if lcm(d, e) <= modulus_limit:
                            medium += cd * ce
                            proper_lcm += d * e > modulus_limit
                        else:
                            tail += cd * ce
                            negative += cd * ce < 0
                actual = mangoldt[a] * mangoldt[b]
                assert actual == (mangoldt[a] * short_b + short_a * mangoldt[b]
                                  - short_a * short_b + medium + tail)
                higher_powers += bool(actual and (len(factors(a)) > 1 or len(factors(b)) > 1))
                positions += 1
    assert proper_lcm and negative and higher_powers
    return cases, positions, proper_lcm, negative, higher_powers


def local_factors():
    checks = 0
    for p in (2, 3, 5, 7, 11, 13):
        for target in range(0, p if p > 2 else 1):
            divides = target == 0
            roots = len({0, target})
            v = Fraction(p - roots, p)
            unit = Fraction(p - 1, p)
            series = v / unit**2
            for on_wheel in (False, True):
                if on_wheel:
                    u1 = 1 if divides else 1 - Fraction(1, p - 1)
                    mixed, double = 1 / unit, 1 / unit**2
                else:
                    u1 = 1
                    mixed = (1 if divides else 1 - Fraction(1, p - 1)) / unit
                    double = (1 - Fraction(2 - int(divides), p)) / unit**2
                assert u1 * mixed == (v if on_wheel else 1) * double == series
                checks += 1
    return checks


def crt_periods():
    cases = 0
    for n in (42, 70, 90, 98, 110):
        for wheel in (2, 6, 30):
            allowed = prod(1 - Fraction(len({0, n % p}), p) for p in factors(wheel))
            divs = [d for d in (1, 3, 5, 7, 11, 15, 21, 35) if gcd(d, wheel) == 1]
            for d in divs:
                for e in divs:
                    period = lcm(d, e) * wheel
                    hits = sum((n - a) % e == 0 and gcd(a * (n - a), wheel) == 1
                               for a in range(0, period, d))
                    expected = allowed / lcm(d, e) if n % gcd(d, e) == 0 else 0
                    assert Fraction(hits, period) == expected
                    cases += 1
    return cases


def switched_progressions():
    limit = 1000
    fs = [()] + [factors(i) for i in range(1, limit + 1)]
    mu = [(-1) ** len(ps) if len(set(ps)) == len(ps) else 0 for ps in fs]
    log_weight = [sum(2 * p - 1 for p in ps) for ps in fs]
    divisors = [[] for _ in fs]
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            divisors[n].append(d)
    cases = nonzero = large_c = shared = 0
    for n in (602, 630, 770, 842, 900):
        lo, hi = n // 2 + 1, n // 2 + 100
        for wheel in (6, 30, 42):
            allowed_j = [j for j in divisors[wheel] if gcd(j, n) == 1]
            for x in range(1, 9):
                if gcd(x, wheel) > 1:
                    continue
                e_values = [e for e in range(5, 25) if mu[e] and gcd(e, wheel) == 1]
                direct = Counter()
                for a in range(lo, hi + 1):
                    if a % x or gcd(a * (n - a), wheel) > 1:
                        continue
                    d = a // x
                    for e in e_values:
                        if (n - a) % e == 0:
                            direct[e] += mu[d] * log_weight[d] * mu[e] * log_weight[e]
                expanded = Counter()
                for e in e_values:
                    e0 = gcd(e, n)
                    r = e0 // gcd(e0, x)
                    for c in range(1, hi // (x * r) + 1):
                        if any(wheel * r % p for p in fs[c]):
                            continue
                        for j in allowed_j:
                            modulus = e // e0 * j
                            scale = x * r * c
                            if gcd(scale, modulus) != 1:
                                continue
                            residue = n * pow(scale, -1, modulus) % modulus
                            lower = (lo - 1) // scale + 1
                            first = lower + (residue - lower) % modulus
                            for t in range(first, hi // scale + 1, modulus):
                                expanded[e, c > 3] += (mu[r] * mu[t] * mu[e] * mu[j]
                                                       * log_weight[r * c * t] * log_weight[e])
                    assert direct[e] == expanded[e, False] + expanded[e, True]
                    shared += gcd(e, n) > 1 and direct[e] != 0
                cases += 1
                nonzero += sum(direct.values()) != 0
                large_c += any(expanded[e, True] for e in e_values)
    assert nonzero and large_c and shared
    return cases, nonzero, large_c, shared


def label_map():
    """Count labels directly; rebuild them independently from primes at M."""
    d = 24
    cases = 0
    for y in (101, 119, 150):
        n = 2 * y
        flags = sieve(n)
        for a in range(y + 2 + (1 - (y + 2) % 2), y + 32, 2):
            b = n - a
            direct = Counter()
            for s in range(1, d + 1):
                q, rem = divmod(b + 2 * s, 3)
                if rem or not flags[q]:
                    continue
                for t in range(1, d + 1):
                    u, rem = divmod(a + 2 * t, 3)
                    if not rem and flags[u]:
                        direct[q + u] += 1
            for m in range(2, n, 2):
                k = (3 * m - n) // 2
                if not 2 <= k <= 2 * d:
                    assert direct[m] == 0
                    continue
                lo, hi = max(1, k - d), min(d, k - 1)
                lower, upper = b + 2 * (lo - 1), b + 2 * hi
                assert upper - lower == 2 * (hi - lo + 1)
                pairs = sum(flags[q] and flags[m - q] for q in range(3, m, 2)
                            if lower < 3 * q <= upper)
                assert pairs == direct[m]
                cases += 1
    return cases


def pooling_bound():
    """Check the Lipschitz comparison for empty bins and signed deviations."""
    bins = [(s, n) for n in range(5) for s in range(n + 1)]

    def baseline(s, n):
        return Fraction(s * s, n) if n else 0

    tests = 0
    for s, n in bins:
        for t, m in bins:
            assert abs(baseline(s, n) - baseline(t, m)) <= 2 * abs(s - t) + abs(n - m)
            for v in (Fraction(0), Fraction(1, 3), Fraction(3, 4), Fraction(1)):
                separate = baseline(s, n) + baseline(t, m)
                pooled = baseline(s + t, n + m)
                ds = abs(s - v * (s + t)) + abs(t - (1 - v) * (s + t))
                dn = abs(n - v * (n + m)) + abs(m - (1 - v) * (n + m))
                assert 0 <= separate - pooled <= 2 * ds + dn
                tests += 1
    return tests


def square_example():
    y = 1009**2
    n, d = 2 * y, floor_power(y, 16, 25)
    h, trim = floor_power(y, 2, 3), 2 * floor_power(y, 21, 40)
    flags = sieve(y + h)
    targets = [m for m in range((n + 2) // 3 // 2 * 2, (n + 4 * d) // 3 + 1, 2)
               if 4 * d <= 5 * ((3 * m - n) // 2) <= 6 * d]
    bounds = {m: (2 * floor_power(m // 2, 21, 40), floor_power(m // 2, 2, 3))
              for m in targets}
    offsets = [x for x in range(trim + 1, h + 1) if flags[y + x] and flags[y - x]]
    coverage = Counter()
    positive = []
    for x in offsets:
        a, b = y + x, y - x
        by_target = Counter()
        qs = [q for q in range(b // 3 + 1, (b + 2 * d) // 3 + 1) if flags[q]]
        us = [u for u in range(a // 3 + 1, (a + 2 * d) // 3 + 1) if flags[u]]
        for q in qs:
            for u in us:
                m = q + u
                if m in bounds and bounds[m][0] < abs(q - m // 2) <= bounds[m][1]:
                    by_target[m] += 1
        positive.extend(by_target.values())
        coverage.update(by_target.keys())
    assert positive
    return dict(Y=y, central_pairs=len(offsets), interior_targets=len(targets),
                targets_carrying_every_pair=sum(coverage[m] == len(offsets) for m in targets),
                min_pairs_detected=min(coverage[m] for m in targets),
                min_positive_multiplicity=min(positive), max_multiplicity=max(positive))


if __name__ == "__main__":
    print("Divisor partitions (configurations, positions, lcm extensions, negative tails,"
          " prime-power pairs):", divisor_partition())
    print("Euler factors:", local_factors())
    print("Complete CRT periods:", crt_periods())
    print("Switched sums (cases, nonzero totals, cases with smooth tails,"
          " nonzero imprimitive components):", switched_progressions())
    print("Smaller-target endpoint/label comparisons:", label_map())
    print("Pooling comparisons:", pooling_bound())
    print(square_example())
