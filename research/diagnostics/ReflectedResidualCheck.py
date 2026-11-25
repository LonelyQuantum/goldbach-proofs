"""Exact finite checks for reflected residuals and prescribed residue counts."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, lcm


def reflected_product(values):
    return sum(x * y for x, y in zip(values, reversed(values)))


def project(values, origin, modulus):
    classes = [(origin + i) % modulus for i in range(len(values))]
    capacities = Counter(classes)
    masses = defaultdict(int)
    for label, value in zip(classes, values):
        masses[label] += value
    means = [Fraction(masses[b], capacities[b]) for b in classes]
    total = 2 * origin + len(values) - 1
    coarse = sum(Fraction(masses[b] * masses[(total - b) % modulus], size)
                 for b, size in capacities.items())
    residual = reflected_product([x - y for x, y in zip(values, means)])
    assert coarse == reflected_product(means)
    assert coarse + residual == reflected_product(values)
    return means, coarse, residual


def check_projections():
    refinements = 0
    for size in range(1, 9):
        for values in product((0, 1), repeat=size):
            for origin in (0, 7):
                for q in (1, 2, 3, 5):
                    v, coarse, residual = project(values, origin, q)
                    w, fine, remainder = project(values, origin, 2 * q)
                    change = [x - y for x, y in zip(w, v)]
                    assert reflected_product(change) == fine - coarse == residual - remainder
                    refinements += 1
    return 2 * refinements, refinements


def predicted_minimum(counts, capacities, total, modulus):
    return sum(max(0, counts[b] + counts[(total - b) % modulus] - size)
               for b, size in capacities.items())


def check_minima():
    configurations = profiles = 0
    for size in range(1, 12):
        for origin in (0, 7):
            for modulus in range(1, 9):
                labels = [(origin + i) % modulus for i in range(size)]
                capacities = Counter(labels)
                minima = {}
                for values in product((0, 1), repeat=size):
                    counts = Counter(b for b, value in zip(labels, values) if value)
                    profile = tuple(counts[b] for b in range(modulus))
                    minima[profile] = min(reflected_product(values), minima.get(profile, size))
                    configurations += 1
                for counts, hits in minima.items():
                    assert hits == predicted_minimum(counts, capacities, 2 * origin + size - 1, modulus)
                profiles += len(minima)
    return configurations, profiles


def relocation_plan(values, labels):
    """List optimal same-label moves, leaving a central fixed site untouched."""
    full, empty = defaultdict(list), defaultdict(list)
    for i in range(len(values) // 2):
        j = len(values) - 1 - i
        source_side, other = sorted((i, j), key=lambda k: labels[k])
        key = labels[source_side], labels[other]
        if values[i] == values[j] == 1:
            full[key].append(source_side)
        elif values[i] == values[j] == 0:
            empty[key].append(source_side)
    return [move for key, sites in full.items() for move in zip(sites, empty[key])]


def check_move_budgets():
    budgets = 0
    for size in range(1, 9):
        for modulus in range(1, 9):
            labels = [i % modulus for i in range(size)]
            profiles = defaultdict(list)
            for values in product((0, 1), repeat=size):
                counts = Counter(b for b, v in zip(labels, values) if v)
                fixed = values[size // 2] if size % 2 else 0
                pairs = (reflected_product(values) - fixed) // 2
                profiles[tuple(sorted(counts.items())), fixed].append((values, pairs))
            for family in profiles.values():
                for values, pairs in family:
                    moves = relocation_plan(values, labels)
                    current = list(values)
                    best = [size] * (size + 1)
                    for other, hits in family:
                        distance = sum(a > b for a, b in zip(values, other))
                        best[distance] = min(best[distance], hits)
                    optimum = size
                    for r in range(size + 1):
                        optimum = min(optimum, best[r])
                        if 0 < r <= len(moves):
                            i, j = moves[r - 1]
                            assert labels[i] == labels[j] and current[i] == 1 and current[j] == 0
                            current[i], current[j] = 0, 1
                        assert reflected_product(current) // 2 == optimum == pairs - min(r, len(moves))
                        budgets += 1
    return budgets


def check_separate_counts(primes, center, window):
    # Destinations are offsets from p². Each source is the smaller member of a true pair.
    offsets = (
        -10092, -9720, -9270, -8388, -7908, -7788, -6900, -6402, -6150, -4722,
        -4590, -4338, -4008, -3372, -3132, -2982, -2322, -1260, -1218, -1188,
        -558, -450, -270, -198, -138, -12, 402, 840, 1062, 1068, 1158, 1320,
        1572, 2130, 2160, 2250, 2292, 2952, 3138, 3330, 3558, 3708, 3810, 3948,
        4212, 5358, 6288, 6540, 6780, 7452, 7782, 7920, 7968, 8022, 8082, 8190,
        9042, 9138, 9342, 9432, 9450, 9600, 9732, 9912,
    )
    removed = {x for x in primes if x < center and 2 * center - x in primes}
    added = {center + offset for offset in offsets}
    assert len(removed) == len(added) == len(offsets) == 64
    assert all(x in window and x not in primes and 2 * center - x not in primes for x in added)
    assert all(gcd(x * (2 * center - x), lcm(840, 99)) == 1 for x in added)
    repaired = (primes - removed) | added
    assert not any(2 * center - x in repaired for x in repaired)
    for modulus in (*range(1, 12), 840, 99):
        assert Counter(x % modulus for x in primes) == Counter(x % modulus for x in repaired)
    return len(removed), len(primes & repaired)


def prime_example():
    p = 1009
    center = p * p
    low, high = 0, center
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** 3 <= p ** 4:
            low = mid
        else:
            high = mid
    window = range(center - low, center + low + 1)
    prime = bytearray([1]) * window.stop
    prime[:2] = bytes(2)
    for divisor in range(2, isqrt(window.stop - 1) + 1):
        if prime[divisor]:
            start = divisor * divisor
            prime[start::divisor] = bytes((window.stop - 1 - start) // divisor + 1)
    print("p, H, window size, primes, ordered prime pairs:", p, low, len(window),
          sum(prime[x] for x in window), sum(prime[x] * prime[2 * center - x] for x in window))
    modulus = 1
    for z in range(1, 12):
        modulus = lcm(modulus, z)
        counts = Counter(x % modulus for x in window if prime[x])
        capacities = Counter(x % modulus for x in window)
        print(z, modulus, predicted_minimum(counts, capacities, 2 * center, modulus))
    primes = {x for x in window if prime[x]}
    print("moved, retained with both separate histograms:", *check_separate_counts(primes, center, window))


if __name__ == "__main__":
    print("decompositions, refinements:", *check_projections())
    print("configurations, profiles:", *check_minima())
    print("fixed-center move budgets:", check_move_budgets())
    prime_example()
