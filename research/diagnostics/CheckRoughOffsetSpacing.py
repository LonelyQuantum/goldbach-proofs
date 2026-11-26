"""Finite checks for RoughOffsetSpacing.md using exact integer arithmetic.

The finite window uses the stated powers of Y. The cutoff 29 and bin widths
are illustrative finite parameters. Run with Python 3.8+.
"""
from bisect import bisect_right
from fractions import Fraction
from itertools import combinations, product
from math import isqrt
from random import Random


def sieve(n):
    flags = bytearray([1]) * (n+1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(n)+1):
        if flags[p]:
            flags[p*p::p] = bytes((n-p*p)//p + 1)
    return flags


def integer_root(n, degree):
    a, b = 0, 1 << ((n.bit_length()+degree-1)//degree)
    while a+1 < b:
        mid = (a+b)//2
        if mid**degree <= n:
            a = mid
        else:
            b = mid
    return a


def check_roots():
    count = 0
    for p in (2, 3, 5, 7, 11, 17, 29, 43):
        for y, d in product(range(p), repeat=2):
            n = 2*y
            roots = {y % p, -y % p, (y-d) % p, (-y-d) % p}
            actual = {x for x in range(p)
                      if ((y+x)*(y-x)*(y+x+d)*(y-x-d)) % p == 0}
            assert actual == roots
            overlaps = (2*(n % p == 0) + 2*(d % p == 0)
                        + ((n-d) % p == 0) + ((n+d) % p == 0))
            assert 4-len(roots) <= overlaps
            if p > 2:
                assert 4-len(roots) == overlaps-3*int(n % p == d % p == 0)
            admissible = ((p != 2 or d % 2 == 0)
                          and (p != 3 or y % 3 == 0 or d % 3 == 0))
            assert (len(roots) < p) == admissible
            for anchor in roots:
                forbidden = {(r-anchor) % p for r in roots} - {0}
                assert len(forbidden) == len(roots)-1
                assert (1-Fraction(len(forbidden), p-1)
                        == Fraction(p-len(roots), p)/Fraction(p-1, p))
            if p >= 7:
                assert (Fraction(p-len(roots), p-4)
                        <= (1+Fraction(20, p*p))*Fraction(p-1, p-2)**overlaps)
            count += 1
    return count


def check_bin_extremes():
    families = 0
    for size in range(8):
        sites = range(size)
        for u, v in product(range(size+1), repeat=2):
            plus = set(range(u))
            possible = set()
            for minus in combinations(sites, v):
                i = len(plus.intersection(minus))
                j, k, c = u-i, v-i, size-u-v+i
                lower, upper = max(0, u+v-size), min(u, v)
                assert i-lower == min(i, c) and upper-i == min(j, k)
                assert upper-lower <= i*c + j*k <= size*(size-1)//2
                possible.add(i)
            assert possible == set(range(max(0, u+v-size), min(u, v)+1))
            families += 1
    return families


def anchor_counts(y, sites, primes, cutoff, upper):
    """Compare full and thinned anchor marks on the same integer companions."""
    squarefree = bytearray([1]) * (upper+1)
    for p in range(2, isqrt(upper)+1):
        if primes[p]:
            sq = p*p
            squarefree[sq::sq] = bytes(upper//sq)
    assert (cutoff+1)**40 > upper  # Rough toy companions also have <=39 factors.
    result, witnesses = {}, {}
    for d in (2, 6, 12):
        anchors = [set() for _ in range(4)]
        for x in sites:
            if x+d not in sites:
                continue
            args = (y+x, y-x, y+x+d, y-x-d)
            if all(squarefree[t] for t in args):
                for j, t in enumerate(args):
                    if primes[t]:
                        anchors[j].add(t)
        counts = tuple(map(len, anchors))
        if d % 3 and y % 3:
            assert counts == (0,)*4
        result[d], witnesses[d] = counts, anchors
    doubles = sorted(x for x in sites if primes[y+x] and primes[y-x])
    rng = Random(20261126)
    for _ in range(100):
        deleted = {y + rng.choice((-1, 1))*x for x in doubles}
        assert all(y+x in deleted or y-x in deleted for x in doubles)
        kept = {d: tuple(len(group-deleted) for group in groups)
                for d, groups in witnesses.items()}
        if all(3*k >= n for d in result for k, n in zip(kept[d], result[d])):
            return result, kept
    raise AssertionError("No finite witness in the seeded thinning trials")


def test_window(y, cutoff, widths):
    hmax, trim = integer_root(y*y, 3), 2*integer_root(y**21, 40)
    low, high = trim+1, hmax
    primes = sieve(y+high)
    small = [p for p in range(2, cutoff+1) if primes[p]]
    rough = [x for x in range(low, high+1)
             if all((y+x) % p and (y-x) % p for p in small)]
    plus = {x for x in rough if primes[y+x]}
    minus = {x for x in rough if primes[y-x]}
    pairs = plus & minus
    direct = {x for x in range(low, high+1) if primes[y+x] and primes[y-x]}
    assert pairs == direct
    cases = []
    for width in widths:
        lower = upper = in_bin = 0
        start = 0
        for left in range(low, high+1, width):
            end = bisect_right(rough, left+width-1, lo=start)
            block = set(rough[start:end])
            size = len(block)
            u, v = len(block & plus), len(block & minus)
            lower += max(0, u+v-size)
            upper += min(u, v)
            in_bin += size*(size-1)//2
            start = end
        assert start == len(rough)
        close = sum(bisect_right(rough, x+width)-i-1 for i, x in enumerate(rough))
        blocks = (high-low+width)//width
        assert 2*blocks*in_bin >= len(rough)**2 - blocks*len(rough)
        assert lower <= len(pairs) <= upper
        assert upper-lower <= in_bin <= close
        iso = {x for i, x in enumerate(rough)
               if (i == 0 or x-rough[i-1] > width)
               and (i+1 == len(rough) or rough[i+1]-x > width)}
        assert len(rough)-len(iso) <= 2*close
        for marks in (rough, sorted(plus), sorted(pairs)):
            gaps = [t-s for s, t in zip(marks, marks[1:])]
            assert sum(g <= width for g in gaps) <= close
            assert sum(g > width for g in gaps)*width <= high-low
        # Compare the two sets of actual primes via their signed marks.
        chosen = sorted(iso & pairs)
        half = len(chosen)//2
        chosen = chosen[:2*half]
        first, second = set(chosen[:half]), set(chosen[half:])
        plus0, minus0 = plus - second, (minus - pairs) | second
        plus1, minus1 = plus - second, (minus - pairs) | first
        assert len(plus0) == len(plus1) and len(minus0) == len(minus1)
        assert not (plus0 & minus0) and len(plus1 & minus1) == half
        deleted = len(plus) + len(minus) - len(plus0) - len(minus0)
        assert deleted == len(pairs)
        for i, x in enumerate(rough):
            for t in rough[i+1:bisect_right(rough, x+width)]:
                for marks0, marks1 in ((plus0, plus1), (minus0, minus1)):
                    for other0, other1 in ((plus0, plus1), (minus0, minus1)):
                        assert ((x in marks0 and t in other0)
                                == (x in marks1 and t in other1))
        cases.append((width, lower, upper, len(iso & pairs), close))
    return len(rough), len(pairs), cases, anchor_counts(y, set(rough), primes, cutoff, y+high)


if __name__ == "__main__":
    ratio = 40*(Fraction(1, 6)-Fraction(1, 4000))
    assert ratio == Fraction(1997, 300) and ratio > Fraction(665, 100) > Fraction(6641, 1000)
    print("prime/residue tests:", check_roots())
    print("bin marginal families:", check_bin_extremes())
    print("Y, sifted sites, true pairs, (bin, lower, upper, isolated pairs, close pairs),"
          " counts by lag for the four prime anchor choices (full, then thinned)")
    for center in (1_000_003, 1009**2, 1_021_020):
        print(center, *test_window(center, 29, (1, 4, 16, 64)))
