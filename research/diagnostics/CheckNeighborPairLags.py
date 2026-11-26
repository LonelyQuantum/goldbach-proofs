"""Exact finite checks for NeighborPairLags.md, using only the standard library."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def neighbor_lists(y, n, primes, inner, outer, block):
    # Test membership at both signed endpoints independently for each neighbor.
    plus, minus = set(), set()
    for x in range(-outer, outer + 1):
        if not inner < abs(x - 15*n) <= outer:
            continue
        partner = 30*n - x
        if x not in block and partner not in block:
            continue
        if y+x in primes and y+partner in primes:
            plus.add(x)
        if y-x in primes and y-partner in primes:
            minus.add(x)
    assert {30*n-x for x in plus} == plus
    assert {30*n-x for x in minus} == minus
    return plus, minus


def check_lags(y, primes, inner, outer, binsize):
    labels = (1, 2, 3, 4)
    target = {v for v in range(inner + 1, outer + 1)
              if y+v in primes and y-v in primes}
    diagonal_sum = nonzero_readings = tested = 0
    for lo in range(inner + 1, outer + 1, binsize):
        block = range(lo, min(lo + binsize, outer + 1))
        lists = {n: neighbor_lists(y, n, primes, inner, outer, block)
                 for n in labels}
        for n, m in product(labels, repeat=2):
            a, b = lists[n][0], lists[m][1]
            k = 30*(m-n)
            counts = Counter(w-x for x in a for w in b)
            assert all(counts[d] == counts[k-d] for d in counts)
            assert len(a)*len(b) - sum(c for d, c in counts.items()
                                          if d not in (0, k)) == (
                (2 if n != m else 1) * len(a & b))
            assert all(abs(x) in target for x in a & b)
            if n != m:
                diagonal_sum += 2 * len(a & b)
                nonzero_readings += counts[k]
            tested += 1
    assert diagonal_sum == 2 * nonzero_readings
    return tested, diagonal_sum


def model_sets(y, orbits, background):
    # The even part is small enough to enumerate every possible outcome.
    fixed_zero, fixed_one = set(background), set(background)
    if len(orbits) % 2:
        v = orbits[-1]
        donor = min(background)
        fixed_zero.add(y+v)
        fixed_one.update((y-v, y+v))
        fixed_one.remove(donor)
        orbits = orbits[:-1]
    zero = [fixed_zero | {y + sign*v for sign, v in zip(signs, orbits)}
            for signs in product((-1, 1), repeat=len(orbits))]
    one = [fixed_one | {y + sign*v for v in chosen for sign in (-1, 1)}
           for chosen in combinations(orbits, len(orbits)//2)]
    return zero, one


def counts(points):
    return Counter(a+b for a in points for b in points)


def check_comparison(y, available, r):
    orbits = sorted(v for v in range(1, y) if y-v in available and y+v in available)
    background = {p for p in available if 2*y-p not in available}
    zero, one = model_sets(y, orbits[:r], background)
    sets = zero + one
    assert all(s <= available and len(s) == len(sets[0]) for s in sets)
    assert all(counts(s)[2*y] == 0 for s in zero)
    assert all(counts(s)[2*y] == 2*((r+1)//2) for s in one)
    for z in (zero[0], zero[-1]):
        for o in (one[0], one[-1]):
            cz, co = counts(z), counts(o)
            assert sum(cz[t]-co[t] for t in cz.keys() | co.keys()
                       if t != 2*y) == 2*((r+1)//2)
    # For even r check the exact two distributions on representative four-form
    # queries, including repeated sites and isolated complementary sites.
    exact_means = 0
    if r % 2 == 0 and r:
        for n, m, d in ((1, 2, 10), (1, 2, 30), (1, 1, 0),
                        (1, 2, 60), (1, 1, -30)):
            for x in range(-95, 96):
                sites = {y+x, y-x+30*n, y-x-d, y+x+d-30*m}
                if not sites <= available:
                    continue
                if not sites <= (background | {y+t*v for v in orbits[:r]
                                                for t in (-1, 1)}):
                    continue
                edited = sites - background
                involved = {abs(p-y) for p in edited}
                k = len(involved)
                both = len(edited) > k
                prob_a = Fraction(0) if both else Fraction(1, 2**k)
                prob_b = Fraction(1)
                for j in range(k):
                    prob_b *= Fraction(max(r//2-j, 0), r-j)
                assert prob_a == Fraction(sum(sites <= s for s in zero), len(zero))
                assert prob_b == Fraction(sum(sites <= s for s in one), len(one))
                if not both:
                    assert abs(prob_a-prob_b) <= Fraction(k*(k-1), 2*r)
                exact_means += 1
        # The four-form queries need not realize every possible orbit
        # multiplicity in a small prime sample. Check these separately.
        edited_sites = [y+sign*v for v in orbits[:r] for sign in (-1, 1)]
        for length in (1, 2, 3, 4):
            for query in combinations(edited_sites, length):
                sites = set(query)
                k = len({abs(p-y) for p in sites})
                p0 = Fraction(sum(sites <= s for s in zero), len(zero))
                p1 = Fraction(sum(sites <= s for s in one), len(one))
                assert p0 == (Fraction(0) if k < length else Fraction(1, 2**k))
                expected = Fraction(1)
                for j in range(k):
                    expected *= Fraction(max(r//2-j, 0), r-j)
                assert p1 == expected
                if k == length:
                    assert abs(p0-p1) <= Fraction(k*(k-1), 2*r)
                exact_means += 1
    return len(sets), exact_means


def check_divisor_average():
    tested = 0
    for cutoff in (7, 17, 23):
        divisors = {1: Fraction(1)}
        for p in range(3, cutoff + 1):
            if is_prime(p):
                divisors.update({d*p: weight / (p-2)
                                 for d, weight in list(divisors.items())})
        for start, width in product((1000, 2310, 51051), (1, 7, 31)):
            direct = Fraction(0)
            for n in range(start, start+width):
                f = Fraction(1)
                for p in range(3, cutoff + 1):
                    if is_prime(p) and n % p == 0:
                        f *= Fraction(p-1, p-2)
                direct += f
            expanded = sum(g * ((start+width-1)//d - (start-1)//d)
                           for d, g in divisors.items())
            assert direct == expanded <= sum(g * (Fraction(width, d)+1)
                                             for d, g in divisors.items())
            tested += 1
    return tested


if __name__ == "__main__":
    y, inner, outer = 600, 15, 260
    numbers = {y+s*v for v in range(inner+1, outer+1) for s in (-1, 1)}
    primes = {p for p in numbers if is_prime(p)}
    toy_lags = [check_lags(y, primes, inner, outer, b) for b in (1, 11, 65, 245)]
    assert all(mass > 0 for _, mass in toy_lags)
    print("bin/label checks and exact omitted masses by bin width:", toy_lags)
    comparisons = [check_comparison(y, primes, r) for r in (0, 1, 4, 5, 6, 8)]
    assert sum(n for _, n in comparisons) > 0
    print("subset outcomes and exact query expectations:", comparisons)
    print("exact local divisor sums:", check_divisor_average())
