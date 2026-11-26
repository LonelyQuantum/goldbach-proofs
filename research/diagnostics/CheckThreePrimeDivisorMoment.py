"""Exact finite checks for ThreePrimeDivisorMoment.md. Run with Python 3."""

from fractions import Fraction
from itertools import combinations
from math import gcd, prod

from CheckHybridSemiprimeFrontier import phi, primitive_kernel
from CheckProperDivisorScales import data


def subsets(items, size):
    return (frozenset(x) for x in combinations(items, size))


def check_character_cutoffs():
    # All pair conductors times j lie below the cut; the full triple lies above.
    # j=15 exercises two independent wheel primes simultaneously.
    band = (53, 59, 61, 67)
    tested = 0
    for triple in combinations(band, 3):
        d = prod(triple)
        worst_pair = triple[1] * triple[2]
        for j in (1, 3, 5, 15):
            m = d*j
            for cut in (worst_pair*j, d-1):
                assert worst_pair*j <= cut < d
                high = [f for f in data(m)[0] if f > cut]
                assert set(high) == {d*k for k in data(j)[0]}
                for a in data(m)[0]:
                    direct = Fraction(data(m)[1] * sum(primitive_kernel(f, a) for f in high), phi(m))
                    predicted = data(j)[1] * int(a % j == 0) * prod(
                        Fraction(1, p-1) - int(a % p == 0) for p in triple)
                    assert predicted == direct
                    tested += 1
                # At the other boundary the primitive conductor d itself is omitted.
                assert d not in [f for f in data(m)[0] if f > d]
    return tested


def check_pair_reference():
    # Only characters principal on k remain. Summing the wheel gives the
    # exact congruence on j even when it fails at this integer difference.
    tested = 0
    for k in (11, 13, 11*13, 11*17):
        for j in (1, 3, 5, 15):
            assert gcd(j, k) == 1
            for a in data(j*k)[0]:
                retained = Fraction(sum(primitive_kernel(f, a) for f in data(j)[0]), phi(j*k))
                assert retained == Fraction(int(a % j == 0), phi(k))
                tested += 1
    return tested


def check_models():
    primes = (17, 19, 23, 29, 31, 37, 41, 47)
    c = {p: Fraction(1, p-1) for p in primes}
    assert sum(c.values()) < Fraction(1, 2)
    base = [b for size in range(4) for b in subsets(primes, size)]
    triples = list(subsets(primes, 3))
    pairs = list(subsets(primes, 2))
    # Finite closeness mask for checking the algebra, not an asymptotic test.
    def close(t):
        return any(abs(p-q) <= 3 for p, q in combinations(t, 2))
    # A completely additive integer substitute checks every logarithmic identity.
    def weight(t):
        return sum(p.bit_length() for p in t)

    pair_ref = sum(weight(b)*prod(c[i] for i in b) for b in pairs)
    third_ref = sum(weight(b)*prod(c[i] for i in b) for b in triples)
    separated = sum(weight(b)*prod(c[i] for i in b) for b in triples if not close(b))
    assert 0 < separated < third_ref
    for multiplier in (0, 1, 2):
        incl = {b: prod(c[i] for i in b) * (multiplier if len(b) == 3 and not close(b) else 1)
                for b in base}
        mass = {b: sum((-1)**(len(t)-len(b))*incl[t] for t in base if b <= t)
                for b in base}
        assert min(mass.values()) >= 0 and sum(mass.values()) == 1
        assert all(sum(mass[t] for t in base if b <= t) == incl[b] for b in base)

        denominator = extra_pairs = actual = centered = 0
        for hits, prob in mass.items():
            pair_weight = sum(weight(p) for p in pairs if p <= hits)
            triple_weight = sum(weight(t) for t in triples if t <= hits)
            assert max(0, len(hits)-2)*pair_weight == 2*triple_weight
            denominator += prob * pair_weight
            extra_pairs += prob * max(0, len(hits)-2)*pair_weight
            actual += prob * triple_weight
            centered += prob * sum(weight(t)*prod(c[p] - int(p in hits) for p in t)
                                   for t in triples)
        assert denominator == pair_ref and extra_pairs == 2*actual
        assert centered == third_ref - actual == (1-multiplier)*separated
    return len(base), len(triples), sum(not close(b) for b in triples)


def check_reflected_window():
    from CheckSemiprimeRecords import factors

    a0, b0 = 11*13*17*19, 127*359
    n = a0 + b0
    band = (11, 13, 17, 19)
    assert n % 2 == 0 and all(n % p for p in (*band, 5))
    triples = list(combinations(band, 3))
    direct = arithmetic = reference = actual = lower_errors = 0
    records = hits = 0
    for b in range(n//2 - 1000, n//2 - 40):
        primes = factors(b)
        if len(primes) != 2 or not 41 <= primes[0] <= 170 or primes[0] == primes[1]:
            continue
        a = n-b
        if gcd(n, b) > 1 or not data(a)[1]:
            continue
        records += 1
        for t in triples:
            d = prod(t)
            weight = primes[0].bit_length() * sum(p.bit_length() for p in t)
            for j in (1, 5):
                m = d*j
                kernel = sum(primitive_kernel(f, a) for f in data(m)[0] if f > 1800)
                direct += weight * Fraction(data(m)[1] * kernel, phi(m))
            if a % 5 == 0:
                continue
            c = [Fraction(1, p-1) for p in t]
            x = [int(a % p == 0) for p in t]
            arithmetic += weight * prod(c[i] - x[i] for i in range(3))
            reference += weight * prod(c)
            actual += weight * prod(x)
            hits += prod(x)
            for i in range(3):
                j, k = (i+1) % 3, (i+2) % 3
                lower_errors += weight * (c[i]*(x[j]*x[k] - c[j]*c[k])
                                          - (x[i] - c[i])*c[j]*c[k])
    assert hits >= 4 and lower_errors != 0
    assert direct == arithmetic == reference - actual + lower_errors
    return n, records, hits


if __name__ == "__main__":
    print("High-conductor identities:", check_character_cutoffs())
    print("Pair reference identities:", check_pair_reference())
    print("Three laws (configurations per law, triples, separated triples):", check_models())
    print("Reflected window (target, semiprimes before wheel, triple incidences after wheel):", check_reflected_window())
