"""Exact finite checks for LargeLeastPrimeSemiprimes.md; Python standard library."""

from collections import Counter
from itertools import accumulate
from math import gcd, prod

from CheckProperDivisorScales import additive_log, data
from CheckSemiprimeRecords import factors, floor_power, sieve


def row_checks():
    rows = semis = switched = as_full = 0
    for b in range(15, 400):
        db, mb, _ = data(b)
        ps = factors(b)
        if not mb or len(ps) < 2:
            continue
        for r_cut in (2, 4, 6):
            if min(ps) <= r_cut:
                continue
            for a in range(b + 1, b + 26):
                da, ma, _ = data(a)
                if not ma or gcd(a, b) != 1:
                    continue
                for d in da:
                    if d <= r_cut:
                        continue
                    # Include exact equality at one and two prime-factor thresholds.
                    for threshold in {0, d*ps[0]-1, d*ps[0], d*ps[1], b//2}:
                        if threshold >= d*b:
                            continue
                        actual = sum(data(e)[1]*additive_log(e) for e in db
                                     if e > r_cut and d*e > threshold)
                        boundary = -sum(data(e)[1]*additive_log(e) for e in db
                                        if 1 < e and d*e <= threshold)
                        assert actual == boundary
                        rows += 1
                        if len(ps) != 2:
                            continue
                        p, q = ps
                        assert actual == (d*p <= threshold)*additive_log(p) + (
                            d*q <= threshold)*additive_log(q)
                        semis += 1
                        if d == a and threshold < a:
                            assert actual == 0
                            as_full += 1
                        # Use a finite switch size below p, to isolate e=b on the
                        # reflected switch, exactly as the large-prime input does.
                        for switch in (0, min(p-1, d*d)):
                            filtered = sum(data(e)[1]*additive_log(e) for e in db
                                           if e > r_cut and d*e > threshold
                                           and (a//d)*e*e > switch and (b//e)*d*d > switch)
                            assert filtered == boundary - (d*d <= switch)*additive_log(b)
                            switched += 1
    assert rows > semis and switched and as_full
    return rows, semis, switched, as_full


def active_switch():
    # Keep p>d^2, so the reflected switch genuinely removes the e=b term.
    a, b, d, cut = 3*503, 31*43, 3, 2
    assert gcd(a, b) == 1
    checks = 0
    for threshold in (2, 3*31, 3*43):
        for switch in (8, 9, 10):
            total = sum(data(e)[1]*additive_log(e) for e in data(b)[0]
                        if e > cut and d*e > threshold
                        and (a//d)*e*e > switch and (b//e)*d*d > switch)
            expected = sum(additive_log(r) for r in (31, 43) if d*r <= threshold)
            assert total == expected - (d*d <= switch)*additive_log(b)
            checks += 1
    return checks


def dyadic_cover(lo, hi, size):
    lo += size
    hi += size
    nodes = []
    while lo < hi:
        if lo % 2:
            nodes.append(lo)
            lo += 1
        if hi % 2:
            hi -= 1
            nodes.append(hi)
        lo //= 2
        hi //= 2
    return nodes


def interval_maximum():
    checks = 0
    primes = [p for p, flag in enumerate(sieve(50)) if flag]
    size = 1 << (len(primes)-1).bit_length()
    for s in range(180, 260):
        leaves = []
        for p in primes:
            signed = 0
            for b in range(s-80, s-3):
                if factors(b)[:1] == (p,) and len(factors(b)) == 2 and b//p > p:
                    signed += data(2*s-b)[1]
            leaves.append(signed)
        tree = [0]*size + leaves + [0]*(size-len(leaves))
        for k in range(size-1, 0, -1):
            tree[k] = tree[2*k] + tree[2*k+1]
        prefix = [0] + list(accumulate(leaves))
        for lo in range(len(leaves)):
            for hi in range(lo+1, len(leaves)+1):
                nodes = dyadic_cover(lo, hi, size)
                assert sum(tree[k] for k in nodes) == prefix[hi]-prefix[lo]
                assert max(Counter(k.bit_length() for k in nodes).values()) <= 2
                checks += 1
    return checks


def example():
    s = 1009**2
    n = 2*s
    h, trim = floor_power(s, 2, 3), 2*floor_power(s, 21, 40)
    # Deliberately finite diagnostic settings (not the asymptotic sieve or Z).
    wheel = prod(p for p, flag in enumerate(sieve(29)) if flag)
    threshold = h-trim
    r_cut = floor_power(s, 1, 7)
    signs = Counter()
    pi = Counter()
    signed_all = signed_whole = signed_boundary = nonzero_rows = 0
    for a in range(s+trim+1, s+h+1):
        b = n-a
        ps = factors(b)
        if len(ps) != 2 or ps[0] == ps[1] or ps[0]**3 <= n:
            continue
        da, ma, _ = data(a)
        if not ma or gcd(a*b, wheel) > 1 or gcd(a, n) > 1:
            continue
        signs[ma] += 1
        db = (ps[0], ps[1], b)
        for d in da:
            if d <= r_cut:
                continue
            row = sum(data(e)[1]*additive_log(e) for e in db if d*e > threshold)
            total = data(d)[1]*additive_log(d)*row
            signed_all += total
            if a == d:
                assert total == 0
                signed_whole += total
            nonzero_rows += row != 0
            for r in ps:
                if d*r <= threshold:
                    pi[r, d] += 1
    # Build the progression counts independently by scanning t at fixed r,d.
    flags = sieve(n)
    independent = Counter()
    for r in range(2, threshold//(r_cut+1)+1):
        if not flags[r] or r**3 <= n or n % r == 0:
            continue
        for d in range(r_cut+1, threshold//r+1):
            if not data(d)[1] or gcd(d, n*r*wheel) > 1:
                continue
            low = (s-h+r-1)//r
            high = (s-trim-1)//r
            residue = n*pow(r, -1, d) % d
            for t in range(low+(residue-low) % d, high+1, d):
                if t == r or not flags[t] or t**3 <= n:
                    continue
                a = n-r*t
                if data(a)[1] and gcd(a*r*t, wheel) == gcd(a, n) == 1:
                    independent[r, d] += 1
    assert independent == pi
    for (r, d), count in independent.items():
        signed_boundary += count*additive_log(r)*data(d)[1]*additive_log(d)
    assert signed_boundary == signed_all
    return dict(Y=s, wheel_cutoff=29, R=r_cut, Z=threshold, positive=signs[1],
                negative=signs[-1], complete_whole_row=signed_whole,
                nonzero_frontier_rows=nonzero_rows, integer_weighted_frontier=signed_boundary)


if __name__ == "__main__":
    print("Rows (composites, semiprimes, switches, full-row zeros):", row_checks())
    print("Switch threshold tests:", active_switch())
    print("Ordered-prime interval decompositions:", interval_maximum())
    print(example())
