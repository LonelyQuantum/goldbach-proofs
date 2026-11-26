"""Exact finite checks for SemiprimeRecordsAtSmallerTargets.md. Python 3.8+."""
from bisect import bisect_right
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def sieve(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((limit - p*p)//p + 1)
    return flags


def factors(n):
    result = []
    for d in range(2, isqrt(n) + 1):
        while n % d == 0:
            result.append(d)
            n //= d
        if n == 1:
            break
    if n > 1:
        result.append(n)
    return tuple(result)


def full_records(n, allowed):
    pairs = {p for p in allowed if n-p in allowed}
    records = set()
    for p in allowed:
        if p >= n:
            continue
        fs = factors(n-p)
        if len(fs) >= 2 and all(q in allowed for q in fs):
            records.add((p, fs))
    return pairs, records


def test_mask():
    flags = sieve(512)
    prime = {p for p, value in enumerate(flags) if value}
    tuples = 0
    for n in range(8, 513, 2):
        pairs, records = full_records(n, prime)
        keep = prime - {p for p in pairs if 2*p >= n}
        pruned_pairs, pruned_records = full_records(n, keep)
        assert not pruned_pairs and pruned_records == records
        for m in range(4, n//2+1, 2):
            assert all(p in keep and m-p in keep for p in range(2, m)
                       if flags[p] and flags[m-p])
        w14 = {p for p, fs in records if len(fs) == 2 and fs[0]**10 <= fs[1]**9}
        for cutoff in (0, n//4, n//2):
            semis = sum(n-p > cutoff for p in w14)
            true = sum(n-p > cutoff for p in pairs)
            signed = sum((-1)**len(factors(n-p)) for p in w14 | pairs if n-p > cutoff)
            assert signed == semis-true and (semis+true)-signed == 2*true
        tuples += len(records)
    return tuples


def test_small_lists():
    y, d = 105, 20
    n = 2*y
    prime = {p for p, value in enumerate(sieve(n+2*d)) if value}
    central = {p for p in prime if 5 <= abs(p-y) <= 24}
    pairs = [(a, n-a) for a in sorted(central) if a > y and n-a in central]
    rows = [(s, a, q) for s in range(1, d+1) for a in central for q in prime
            if a + 3*q == n + 2*s]
    assert pairs and all(q < min(central) for _, _, q in rows)
    w = Counter(a for _, a, _ in rows)
    observed = []
    for selected in product(*pairs):
        keep = prime - set(selected)
        assert not any(a in keep and b in keep for a, b in pairs)
        kept = sum(a in keep and q in keep and 3 in keep for _, a, q in rows)
        observed.append(len(rows)-kept)
    assert min(observed) == sum(min(w[a], w[b]) for a, b in pairs)
    total = matched = 0
    for s, a, q in rows:
        if a <= y:
            continue
        for t, b, u in rows:
            if b >= y:
                continue
            total += 1
            assert (a+b == n) == (3*(q+u) == n+2*(s+t))
            if a+b == n:
                matched += 1
                assert q+u < y and q+u == (n+2*(s+t))//3
    assert matched == sum(w[a]*w[b] for a, b in pairs) > 0
    return len(pairs), min(observed), total, matched


def test_local_sieve():
    count = 0
    for ell in (3, 5, 7, 11, 17, 29):
        for n, r in product(range(ell), repeat=2):
            roots = {q for q in range(ell) if q*(n-r*q) % ell == 0}
            if r == n == 0:
                assert len(roots) == ell
            else:
                assert len(roots) == (1 if r == 0 or n == 0 else 2)
            count += 1
    for m in range(2, 512, 2):
        f2 = Fraction(1)
        expansion = {1: Fraction(1)}
        for p in sorted(set(factors(m)) - {2}):
            local = Fraction(p-1, p-2)**2
            f2 *= local
            expansion.update({p*d: w*(local-1) for d, w in expansion.items()})
        assert sum(expansion.values()) == f2
    return count


def test_covariance():
    # Keep both orientations and filter both ends with the same finite wheel.
    cases = 0
    for y in (105, 150, 210):
        n, d = 2*y, 20
        prime = {p for p, bit in enumerate(sieve(n+2*d)) if bit}
        for wheel in (2, 6, 30):
            buckets = {}
            for a in range(y-24, y+25):
                b = n-a
                if abs(a-y) < 5 or gcd(a*b, wheel) > 1:
                    continue
                left = [q for q in prime if n < a+3*q <= n+2*d and (a+3*q) % 2 == 0]
                right = [u for u in prime if n < b+3*u <= n+2*d and (b+3*u) % 2 == 0]
                for q, u in product(left, right):
                    if q == u:  # A symmetric illustrative inner trim.
                        continue
                    buckets.setdefault(q+u, []).append((int(a in prime), int(b in prime)))
            baseline = covariance = 0
            hits = marks = size = 0
            for rows in buckets.values():
                total = len(rows)
                first = sum(i for i, _ in rows)
                assert first == sum(j for _, j in rows)
                alpha = Fraction(first, total)
                baseline += total*alpha**2
                covariance += sum((i-alpha)*(j-alpha) for i, j in rows)
                hits += sum(i*j for i, j in rows)
                size += total
                marks += first
            assert size and baseline+covariance == hits
            assert baseline >= Fraction(marks**2, size)
            cases += 1
    return cases


def floor_power(y, a, b):
    target = y**a
    lo, hi = 0, 1 << ((target.bit_length()+b-1)//b)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**b <= target:
            lo = mid
        else:
            hi = mid
    return lo


def square_example():
    y = 1009**2
    n, h, trim, d = 2*y, floor_power(y, 2, 3), 2*floor_power(y, 21, 40), floor_power(y, 16, 25)
    flags = sieve(y+h)
    offsets = [x for x in range(trim+1, h+1) if flags[y+x] and flags[y-x]]
    small = [q for q in range((y-h)//3, (y+h+2*d)//3+1) if flags[q]]

    def partners(a):
        lo = bisect_right(small, (n-a)//3)
        hi = bisect_right(small, (n-a+2*d)//3)
        return small[lo:hi]

    loss = sum(min(len(partners(y+x)), len(partners(y-x))) for x in offsets)
    x = max(offsets)
    a, b = y+x, y-x
    counts = Counter(q+u for q in partners(a) for u in partners(b))
    limits = {m: (2*floor_power(m//2, 21, 40), floor_power(m//2, 2, 3)) for m in counts}
    trimmed = Counter()
    for q in partners(a):
        for u in partners(b):
            m = q+u
            s, t = (a+3*q-n)//2, (b+3*u-n)//2
            assert 1 <= s <= d and 1 <= t <= d and n+2*(s+t) == 3*m
            inside, outside = limits[m]
            if inside < abs(q-m//2) <= outside:
                trimmed[m] += 1
    assert trimmed and sum(counts.values()) == len(partners(a))*len(partners(b))
    return dict(Y=y, label_count=d, central_pairs=len(offsets), minimum_loss=loss,
                offset=x, matches=sum(counts.values()), trimmed_matches=sum(trimmed.values()),
                smaller_targets_with_trimmed_match=len(trimmed))


if __name__ == "__main__":
    print("Two-form local root checks:", test_local_sieve())
    print("Exact covariance tests:", test_covariance())
    print("Composite tuples across 253 even targets:", test_mask())
    print("Toy unordered pairs, minimum loss, cross checks, matches:", test_small_lists())
    print(square_example())
