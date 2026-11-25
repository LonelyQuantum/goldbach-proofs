"""Exact finite checks for SharedPrimeCenters.md. Standard library only."""

from itertools import combinations, product
from math import comb, isqrt, prod
from collections import Counter


def floor_root(n, degree):
    low, high = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while high - low > 1:
        mid = (low + high) // 2
        if mid**degree <= n:
            low = mid
        else:
            high = mid
    return low


def primes_through(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = bytes(len(range(p*p, limit + 1, p)))
    return flags


def rough_squarefree_five(n, cutoff):
    factors = 0
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            n //= p
            factors += 1
            if p < cutoff or n % p == 0:
                return False
    return factors + int(n > 1) <= 5 and (n == 1 or n >= cutoff)


def common_neighbors(center, primes):
    half = floor_root(center**2, 3)
    count = floor_root(center**21, 40)
    lower = [a for a in range(center-half+count, center) if primes[a]]
    upper = [a for a in range(center+2*count+1, center+half+1)
             if primes[a] and rough_squarefree_five(2*center-a, 11)]
    deleted = {a for a in range(center+1, center+half+1)
               if primes[a] and primes[2*center-a]}
    best = None
    checks = 0
    # Short finite blocks test the double count, independently of asymptotic constants.
    for endpoints in (lower, upper):
        for width, order in ((6, 2), (9, 3)):
            for start in range(1, count-width+2, width):
                block = range(start, start+width)
                hits = {j: {a for a in endpoints if primes[2*(center+j)-a]}
                        for j in block}
                from_tuples = 0
                for shifts in combinations(block, order):
                    common = set.intersection(*(hits[j] for j in shifts))
                    from_tuples += len(common)
                    for a in common:
                        assert all(0 < abs(center+j-a) <= floor_root((center+j)**2, 3)
                                   for j in shifts)
                    if endpoints is upper:
                        assert not common or all(j % 3 != 1 for j in shifts)
                        surviving = {a for a in common if a not in deleted and
                                     all(2*(center+j)-a not in deleted for j in shifts)}
                        assert common-surviving == {a for a in common if primes[2*center-a]}
                        if order == 2 and common:
                            exact = sum(primes[2*center-a] for a in common)
                            candidate = (len(common), exact, shifts)
                            if best is None or candidate > best:
                                best = candidate
                from_endpoints = sum(comb(sum(a in hits[j] for j in block), order)
                                     for a in endpoints)
                assert from_tuples == from_endpoints
                checks += 1
    return checks, best


def exact_anchor(center, primes):
    half = floor_root(center**2, 3)
    count = floor_root(center**21, 40)
    assert 2*count <= half
    records = []
    for h in range(1, half+1):
        if not (primes[center-h] and primes[center+h]):
            continue
        fixed, partner = (center-h, center+h) if h <= count else (center+h, center-h)
        shifts = {j for j in range(1, count+1) if primes[partner+2*j]}
        for j in shifts:
            assert fixed+partner+2*j == 2*(center+j)
            assert 1 <= abs(fixed-center-j) <= floor_root((center+j)**2, 3)
        records.append((h, shifts))
    for r in (1, 2):
        from_pairs = sum(comb(len(shifts), r) for _, shifts in records)
        from_shifts = sum(sum(all(j in shifts for j in subset) for _, shifts in records)
                          for subset in combinations(range(1, count+1), r))
        assert from_pairs == from_shifts
    return {h <= count for h, _ in records}


def all_coin_assignments(center, primes):
    half = floor_root(center**2, 3)
    reflected = [(center-h, center+h) for h in range(1, half+1)
                 if primes[center-h] and primes[center+h]]
    assert 0 < len(reflected) <= 10
    lower = list(range(center-half+6, center))
    upper = [a for a in range(center+13, center+half+1)
             if rough_squarefree_five(2*center-a, 11)]
    assert any(a in upper and any(primes[2*center-a+2*j] for j in range(1, 7))
               for _, a in reflected)
    subsets = [s for r in range(4) for s in combinations(range(1, 7), r)]
    tests = [(side, subset) for side in (0, 1) for subset in subsets]
    endpoints = (lower, upper)
    totals = dict.fromkeys(tests, 0)

    def correlation(weights, side, subset):
        # Nonconstant, signed deterministic coefficients also preserve the identity.
        return sum((a % 13 - 6) * a * weights[a] *
                   prod((2*(center+j)-a)*weights[2*(center+j)-a] for j in subset)
                   for a in endpoints[side])

    for choices in product((0, 2), repeat=len(reflected)):
        w = list(primes)
        for (a, b), value in zip(reflected, choices):
            w[a], w[b] = value, 2-value
        assert all(w[center-h]*w[center+h] == 0 for h in range(1, half+1))
        for side, subset in tests:
            totals[side, subset] += correlation(w, side, subset)
    for side, subset in tests:
        assert totals[side, subset] == (1 << len(reflected))*correlation(primes, side, subset)
    return len(tests)


def partner_factor_ranges():
    """Check (1)'s change of variables and the ordered boxes on actual candidates."""
    center = 1009**2
    half, shifts_max = floor_root(center**2, 3), floor_root(center**21, 40)
    flags = primes_through(center + half + 2*shifts_max)
    small_primes = [q for q in range(2, isqrt(center)+1) if flags[q]]
    shifts, cutoff = (2, 3), 5
    low, high = center-half, center-2*shifts_max  # low inclusive, high exclusive
    candidates = {}
    boxes = Counter()
    for b in range(low, high):
        if not flags[2*center-b] or not all(flags[b+2*j] for j in shifts):
            continue
        n, factors = b, []
        for q in small_primes:
            if q*q > n:
                break
            while n % q == 0:
                factors.append(q)
                n //= q
        if n > 1:
            factors.append(n)
        admissible = min(factors) >= cutoff and len(set(factors)) == len(factors) <= 5
        assert admissible == rough_squarefree_five(b, cutoff)
        if not admissible:
            continue
        candidates[b] = factors
        m = len(factors)
        if m == 1:
            continue
        t = 2*m//3
        divisor = prod(factors[:t])
        assert divisor**m <= b**t
        if m == 3:
            assert divisor**2 <= b*factors[0]
        box = tuple(1 << (q.bit_length()-1) for q in factors[:t])
        boxes[m, box] += 1
    composite = sum(len(ff) > 1 for ff in candidates.values())
    assert sum(boxes.values()) == composite and composite and composite < len(candidates)
    divisors = {1, 5, 7, 35}
    for ff in candidates.values():
        if len(ff) > 1:
            divisors.add(prod(ff[:2*len(ff)//3]))
    for d in divisors:
        direct = {b for b in candidates if b % d == 0}
        from_cofactors = {d*t for t in range((low+d-1)//d, (high+d-1)//d)
                          if flags[2*center-d*t] and all(flags[d*t+2*j] for j in shifts)
                          and rough_squarefree_five(d*t, cutoff)}
        assert direct == from_cofactors
        for ell in (2, 3, 5, 7, 11, 13):
            if d % ell == 0:
                continue
            roots = {t for t in range(ell) if
                     t*(2*center-d*t)*prod(d*t+2*j for j in shifts) % ell == 0}
            assert {d*t % ell for t in roots} == {
                residue % ell for residue in (0, 2*center, *(-2*j for j in shifts))}
    return len(candidates), composite, len(divisors), len(boxes)


if __name__ == "__main__":
    flags = primes_through(22000)
    assert 9763 == 13*751 and not flags[9763]
    assert all(flags[n] for n in (10639, 9929, 9931, 10501, 10067, 10069, 9901))
    for a, partners in ((10639, (9763, 9929, 9931)), (10501, (9901, 10067, 10069))):
        assert [a+b for b in partners] == [2*(101**2+j) for j in (0, 83, 84)]
    tests, best = common_neighbors(101**2, flags)
    assert exact_anchor(101**2, flags) == {False, True}
    assert exact_anchor(113, flags) == set()
    moments = all_coin_assignments(13**2, flags)
    assert best is not None
    n, n_exact, js = best
    print(f"{tests} block identities, both anchor orientations, one empty center, "
          f"and {moments} exact expected correlations verified.")
    print(f"s=101^2, shifts={js}, {n} common upper primes with squarefree "
          f"11-rough partners of at most five factors at s; {n_exact} partners are prime.")
    total, composite, divisors, boxes = partner_factor_ranges()
    print(f"s=1009^2, shifts=(2, 3), cutoff=5: {total} candidates, {composite} "
          f"composite partners, {divisors} divisor checks, {boxes} occupied factor boxes.")
