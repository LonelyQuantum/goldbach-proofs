"""Exact finite checks for reflected residuals and prescribed residue counts."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import isqrt, lcm


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


if __name__ == "__main__":
    print("decompositions, refinements:", *check_projections())
    print("configurations, profiles:", *check_minima())
    prime_example()
