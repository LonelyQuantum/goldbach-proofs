"""Exact checks of the oriented mixed-window parametrization and its row bound."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt


def primes_in_interval(x):
    return {n for n in range(x, 2*x + 1)
            if all(n % d for d in range(2, isqrt(n) + 1))}


def check(x, width, support, direct):
    span = width - 1
    m = span // 2
    origins = list(range(x, 2*x + 1, width))
    cells = {u: sorted(support.intersection(range(u, min(u + width, 2*x + 1))))
             for u in origins}
    differences = defaultdict(list)
    for u, cell in cells.items():
        for c, a in combinations(cell, 2):
            differences[a*a - c*c].append((u, c, a))

    counts = Counter()
    sample = None
    for representations in differences.values():
        local = Counter(u for u, _, _ in representations)
        for u, multiplicity in local.items():
            counts[u, u] += 2 * multiplicity**2
        for (u, c, a), (v, b, d) in combinations(representations, 2):
            if u == v:
                continue
            assert a*a + b*b == c*c + d*d
            counts[u, v] += 2
            counts[v, u] += 2
            sample = sample or (a, b, c, d)

    reconstructed = Counter()
    for u in origins:
        for r in range(1, m + 1):
            for s in range(1, m + 1):
                if gcd(r, s) != 1 or r > 2*s or s > 2*r:
                    continue
                for t in range(1, span // (2 * max(r, s)) + 1):
                    first = (u + r*t + s - 1) // s
                    last = (u + span - r*t) // s
                    for w in range(first, last + 1):
                        a, c, d, b = s*w+r*t, s*w-r*t, r*w+s*t, r*w-s*t
                        if not all(n in support for n in (a, b, c, d)):
                            continue
                        v = x + ((b - x) // width) * width
                        if d >= v + width:
                            continue
                        assert -span*s <= s*v-r*u <= 2*span*s
                        reconstructed[u, v] += 2
    assert reconstructed == counts

    if direct:
        for i, u in enumerate(origins):
            for v in origins[i:]:
                sums = Counter(a*a + b*b for a in cells[u] for b in cells[v])
                assert sum(n*(n-1) for n in sums.values()) == counts[u, v]
    bound = 4*span**2 * sum((Fraction(1, j) for j in range(1, m+1)), Fraction()) + 2*span*m
    rows = [sum(counts[u, v] for v in origins) for u in origins]
    for u in origins:
        assert sum(counts[u, v] > 0 for v in origins if v != u) <= 3*m*m
    assert max(rows) <= bound
    variance = 2 * sum(len(entries)**2 for entries in differences.values())
    assert sum(rows) == variance
    active_pairs = sum(counts[u, v] > 0 for u, v in combinations(origins, 2))
    return len(origins), active_pairs, max(rows), variance, sample


def check_whole_interval(primes):
    values = sorted(primes)
    full = Counter(a*a + b*b for a in values for b in values)
    unit_energy = sum(n*n for n in full.values())
    k = len(values)
    off = unit_energy - (2*k*k-k)
    z = {p: (1, -1, 0, -1, 1)[i % 5] for i, p in enumerate(values)}
    sums, differences = Counter(), Counter()
    for a in values:
        for b in values:
            sums[a*a+b*b] += z[a]*z[b]
            differences[a*a-b*b] += z[a]*z[b]
    energy = sum(n*n for n in sums.values())
    assert energy == sum(n*n for n in differences.values())
    mass = sum(w*w for w in z.values())
    signed_error = energy - (2*mass*mass - sum(w**4 for w in z.values()))
    assert abs(signed_error) <= off
    return k, unit_energy, off, signed_error


if __name__ == "__main__":
    for x, h in [(17, 1), (37, 8), (100, 13), (240, 45), (1000, 26), (2500, 55)]:
        for name, support in [("odd", set(range(x | 1, 2*x+1, 2))),
                              ("prime", primes_in_interval(x))]:
            print(x, h, name, *check(x, h, support, direct=True))
        print("whole", x, *check_whole_interval(primes_in_interval(x)))
