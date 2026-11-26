"""Exact combinatorial checks for ProperDivisorScales.md (standard library)."""

from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import gcd, isqrt, lcm, prod

from CheckSemiprimeRecords import factors, floor_power, sieve


@lru_cache(None)
def data(n):
    primes = factors(n)
    divisors = [1]
    for p, exponent in Counter(primes).items():
        divisors = [d * p**j for d in divisors for j in range(exponent + 1)]
    squarefree = len(primes) == len(set(primes))
    return divisors, (-1)**len(primes) if squarefree else 0, len(set(primes))


def divisor(d):
    return data(d)[1]


def additive_log(n):
    # An additive integer substitute is used only to check identities exactly.
    return sum(p.bit_length() for p in factors(n))


def packet_identities():
    tested = 0
    for n in range(2, 2500):
        ds, sign, _ = data(n)
        if not sign:
            continue
        assert sum((-2)**data(d)[2] for d in ds) == sign
        for c in (2, 3, 4):
            packet = [d for d in ds if n <= (c*d)**2 and d*d <= c*c*n]
            assert {n//d for d in packet} == set(packet)
            for d in packet:
                assert divisor(n//d) == sign * divisor(d)
            twice = 2 * sum(divisor(d) * additive_log(d) for d in packet)
            if sign > 0:
                assert twice == additive_log(n) * sum(map(divisor, packet))
            else:
                assert twice == sum(divisor(d) * (2*additive_log(d) - additive_log(n))
                                    for d in packet)
            tested += 1
    for n, expected in ((15, -2), (210, 4)):
        assert divisor(n) == 1
        assert sum(divisor(d) for d in data(n)[0] if n <= (2*d)**2 and d*d <= 4*n) == expected
    return tested


def truncated_wheel():
    cases = signed_cases = 0
    wheel = (2, 3, 5, 7, 11)
    modulus = prod(wheel)
    for n in range(1, 1001):
        k = sum(n % p == 0 for p in wheel)
        for order in range(5):
            value = sum((-1)**j * sum(n % prod(subset) == 0 for subset in combinations(wheel, j))
                        for j in range(order + 1))
            if k <= order:
                assert value == int(gcd(n, modulus) == 1)
            else:
                signed_cases += 1
            assert abs(value) <= len(data(n)[0])
            cases += 1
    return cases, signed_cases


def factor_lists():
    small = (2, 3, 5, 7, 11)
    lists = data(prod(small))[0]
    checks = exceptional = 0
    for n in range(2, 1200):
        t = prod(p for p in small if n % p == 0)
        ds, _, count = data(t)
        for order in (1, 2, 3, 5):
            recovered = Counter()
            for m in ds:
                if data(m)[2] <= order:
                    for s in data(m)[0]:
                        recovered[s] += divisor(m//s)
            distance = sum(abs(recovered[s] - int(t == s)) for s in lists)
            if count <= order:
                assert distance == 0
            else:
                assert distance <= 1 + 3**count
                exceptional += 1
            checks += 1
    return checks, exceptional


def progression_roots():
    cases = 0
    for p in (2, 3, 5, 7, 11):
        for n in range(0, 2*p, 2):
            for u in range(1, p):
                for m in range(1, p):
                    if gcd(u, m) != 1:
                        continue
                    v0 = n * pow(u, -1, m) % m
                    roots = {t for t in range(p) if (v0 + m*t)*(n - u*(v0 + m*t)) % p == 0}
                    assert len(roots) == 1 + (n % p != 0)
                    cases += 1
    return cases


def proper_strip_map():
    cases = incidences = 0
    for n in range(170, 501, 10):
        y = n // 2
        for a in range(y + 1, y + y//3):
            b = n - a
            for endpoint in (a, b):
                ds = data(endpoint)[0]
                for power in range(endpoint.bit_length()):
                    lower = 2**power
                    requested = {d for d in ds if lower < d <= 2*lower and 1 < d < endpoint}
                    slots = Counter(min(d, endpoint//d) for d in requested)
                    for u, count in slots.items():
                        assert 1 < u <= isqrt(endpoint) and count <= 2
                        assert (lower < u <= 2*lower
                                or y <= 4*lower*u and lower*u <= 2*y)
                    rebuilt = {d for u in slots for d in (u, endpoint//u) if lower < d <= 2*lower}
                    assert rebuilt == requested
                    cases += 1
                    incidences += len(requested)
    return cases, incidences


def whole_term_regrouping():
    def bin_index(n):
        # (2^i,2^(i+1)] for n>1
        return (n - 1).bit_length() - 1

    cases = terms = parity_assignments = 0
    for n in range(302, 502, 4):
        for wheel in (2, 6, 30):
            bins = Counter()
            raw = marginal = 0
            for a in range(n//2 + 1, n//2 + 60):
                b = n - a
                da, ma, _ = data(a)
                db, mb, _ = data(b)
                if not ma or not mb or gcd(a, n) != 1 or gcd(a*b, wheel) != 1:
                    continue
                la, lb = additive_log(a), additive_log(b)
                marginal += ma * la * lb
                for d in da:
                    for e in db:
                        if min(d, e) <= 3 or lcm(d, e) <= 35:
                            continue
                        score = divisor(d)*divisor(e)*additive_log(d)*additive_log(e)
                        raw += score
                        terms += 1
                        if d < a:
                            bins["left", bin_index(d)] += score
                        elif e < b:
                            bins["right", bin_index(e)] += score
                        elif mb == 1:
                            p = min(factors(b))
                            assert 1 < p < b and b % p == 0
                            bins["right", bin_index(p)] += 2 * ma * la * lb
                            parity_assignments += 1
            assert raw == sum(bins.values()) - marginal
            cases += 1
    assert terms and parity_assignments
    return cases, terms, parity_assignments


def sample():
    # The wheel here is specified for a finite diagnostic. The asymptotic theorem
    # uses z=exp(log(Y)/(log log(Y))^3) and supplies no numerical cutoff at this Y.
    y = 1009**2
    n, h, trim = 2*y, floor_power(y, 2, 3), 2*floor_power(y, 21, 40)
    wheel_primes = [p for p, flag in enumerate(sieve(29)) if flag]
    wheel = prod(wheel_primes)
    signs = Counter()
    prime_pairs = proper_hits = both_balanced = 0
    marked_a = Counter()
    for a in range(y + trim + 1, y + h + 1):
        b = n - a
        if gcd(a*b, wheel) != 1 or gcd(a, n) != 1:
            continue
        da, ma, _ = data(a)
        db, mb, _ = data(b)
        if not ma or not mb:
            continue
        signs[ma, mb] += 1
        prime_pairs += len(da) == len(db) == 2
        pa = [d for d in da if 1 < d < a and a <= (2*d)**2 and d*d <= 4*a]
        pb = [e for e in db if 1 < e < b and b <= (2*e)**2 and e*e <= 4*b]
        proper_hits += bool(pa or pb)
        both_balanced += bool(pa and pb)
        for m in db:
            marked_a[m] += ma
    direct = sum(s*t*count for (s, t), count in signs.items())
    low = sum((-2)**data(m)[2]*v for m, v in marked_a.items() if m <= 61)
    high = sum((-2)**data(m)[2]*v for m, v in marked_a.items() if m > 61)
    assert low + high == direct
    return dict(Y=y, wheel_cutoff=29, retained=sum(signs.values()),
                parity_counts={str(k): signs[k] for k in ((1, 1), (1, -1), (-1, 1), (-1, -1))},
                prime_pairs=prime_pairs, at_least_one_balanced=proper_hits,
                both_balanced=both_balanced, parity_sum=direct,
                divisor_expansion_up_to_61=low, divisor_expansion_above_61=high)


if __name__ == "__main__":
    print("Complementary packets:", packet_identities())
    print("Truncated wheel (cases, above truncation):", truncated_wheel())
    print("Exact factor-list inversion (cases, above truncation):", factor_lists())
    print("Sieve roots on progressions:", progression_roots())
    print("Proper strips (intervals tested, divisor incidences):", proper_strip_map())
    print("Whole-term regrouping (cases, original terms, parity assignments):",
          whole_term_regrouping())
    print(sample())
