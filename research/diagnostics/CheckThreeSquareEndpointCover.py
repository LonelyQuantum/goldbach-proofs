"""Finite arithmetic and incidence checks for ThreeSquareEndpointCover.md.

The window in the incidence test is a toy interval with fixed integer cutoffs.
Run directly with Python 3.8+ and the standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt


def sieve(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((limit - p*p) // p + 1)
    return flags


def check_classes():
    residues = {n for n in range(120) if n % 24 == 3 and n % 5}
    assert residues == {3, 27, 51, 99}
    units = {b for b in range(3600) if gcd(b, 30) == 1}
    assert len(units) == 960
    for b in units:
        for sign in (-1, 1):
            images = {(b + sign * 30 * t) % 3600 for t in residues}
            assert len(images) == 4 and images <= units
    assert Fraction(30 * len(residues), len(units)) == Fraction(1, 8)
    for y in range(30):
        actual = sum(gcd(a * (2*y-a), 30) == 1 for a in range(30))
        predicted = 1
        for p in (2, 3, 5):
            predicted *= p - len({0, (2*y) % p})
        assert actual == predicted
    return 2 * len(units)


def square_labels(d, flags):
    roots = [p for p in range(7, isqrt(2*d) + 1) if flags[p]]
    labels = set()
    representations = 0
    for p, q, t in combinations(roots, 3):
        n = p*p + q*q + t*t
        if d < n <= 2*d and (t-p)**20 <= 4**20 * d**9:
            assert n % 24 == 3 and n % 5
            representations += 1
            labels.add(n)
    return sorted(labels), representations


def in_neighbor(center, endpoint, flags, inner, outer):
    # Recover the unordered pair from its absolute offset and test both ends.
    offset = abs(endpoint - center)
    return (inner < offset <= outer
            and flags[center - offset] and flags[center + offset])


def cover(required, rows):
    # Deterministic set cover on the finite toy data, with no asymptotic cutoff.
    missing = set(required)
    selected = []
    while missing:
        best = max(rows, key=lambda n: len(rows[n] & missing))
        hits = rows[best] & missing
        assert hits, "finite data did not cover all candidates"
        missing -= hits
        selected.append(best)
    return selected


def check_neighbors():
    y, d, inner, outer = 3_000_001, 3200, 1600, 210_000
    flags = sieve(y + outer + 60*d)
    labels, representations = square_labels(d, flags)
    offsets = set(range(inner + 1, outer + 1, 113)) | {outer}
    for n in labels:
        for change in (-inner-1, -inner, 0, inner, inner+1):
            offsets.add(15*n + change)
    offsets = {v for v in offsets if inner < v <= outer
               and gcd((y+v)*(y-v), 30) == 1}
    prime_plus = {v for v in offsets if flags[y+v]}
    prime_minus = {v for v in offsets if flags[y-v]}
    pairs = prime_plus & prime_minus
    potential, plus, minus = {}, {}, {}
    opposite_orientation = same_label = 0
    for n in labels:
        plus[n], minus[n], potential[n] = set(), set(), set()
        for v in offsets:
            admissible = inner < abs(v-15*n) <= outer
            hits_plus = bool(admissible and flags[y-v+30*n])
            hits_minus = bool(admissible and flags[y+v-30*n])
            if hits_plus:
                potential[n].add((1, v))
            if hits_minus:
                potential[n].add((-1, v))
            in_plus = in_neighbor(y+15*n, y+v, flags, inner, outer)
            in_minus = in_neighbor(y-15*n, y-v, flags, inner, outer)
            assert bool(in_plus) == (hits_plus and v in prime_plus)
            assert bool(in_minus) == (hits_minus and v in prime_minus)
            if in_plus:
                plus[n].add(v)
                opposite_orientation += int(v < 15*n)
            if in_minus:
                minus[n].add(v)
            if in_plus and in_minus:
                w = v - 30*n
                assert flags[y+w] and flags[y-w] and abs(w) != v
                same_label += int(inner < abs(w) <= outer)
    required = {(sign, v) for sign in (-1, 1) for v in offsets}
    chosen = cover(required, potential)
    assert set.union(*(plus[n] for n in chosen)) == prime_plus
    assert set.union(*(minus[n] for n in chosen)) == prime_minus
    assert set.union(*(plus[n] for n in chosen)) & set.union(
        *(minus[n] for n in chosen)) == pairs
    direct = sum(len(p & m) for p in plus.values() for m in minus.values())
    product = sum(sum(v in p for p in plus.values())
                  * sum(v in m for m in minus.values()) for v in pairs)
    assert direct == product > 0 and same_label and opposite_orientation
    # Test delicate zero/singleton cases on restrictions of the real data.
    one = min(pairs)
    empty = next(v for v in offsets if v not in pairs)
    for v, expected in ((one, 1), (empty, 0)):
        visible = any(v in plus[n] for n in chosen) and any(
            v in minus[n] for n in chosen)
        assert int(visible) == expected
        assert not any(v in plus[n] & minus[n] and abs(v-30*n) == v
                       for n in labels)
    return (len(labels), representations, len(offsets), len(chosen),
            len(pairs), direct, same_label, opposite_orientation)


if __name__ == "__main__":
    print("signed residue-class checks:", check_classes())
    print("labels, square triples, eligible offsets, cover size, central pairs,"
          " ordered matches, trimmed same-label matches, reversed plus hits:",
          check_neighbors())
