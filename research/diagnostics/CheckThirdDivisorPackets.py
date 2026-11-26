"""Integer and rational checks for ThirdDivisorPackets.md (standard library)."""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd, prod

from CheckProperDivisorScales import additive_log, data
from CheckSemiprimeRecords import factors


@lru_cache(None)
def ramanujan(q, n):
    # All moduli here are squarefree. This is the complete reduced-numerator sum.
    return prod(p - 1 if n % p == 0 else -1 for p in factors(q))


def centered(a, triple):
    return prod(Fraction(1, p) - int(a % p == 0) for p in triple)


def wheel_terms(primes, order):
    return {prod(t): (-1)**i for i in range(order + 1) for t in combinations(primes, i)}


def spectrum(triple, wheel):
    d = prod(triple)
    small_denominators = {k for j in wheel for k in data(j)[0]}
    return {d*k: -sum(Fraction(mu, d*j) for j, mu in wheel.items() if j % k == 0)
            for k in small_denominators}


def spectral_value(a, coeff):
    return sum(weight * ramanujan(q, a % q) for q, weight in coeff.items())


def test_packet():
    # The fixed semiprime support includes b=127*359 opposite 11*13*17*19.
    center = (127*359 + 11*13*17*19)//2
    records = []
    for b in range(center-650, center-40):
        ps = factors(b)
        if len(ps) == 2 and 100 <= ps[0] <= 136 and ps[0] < ps[1]:
            records.append((b, ps[0].bit_length()))
    assert any(b == 127*359 for b, _ in records)
    triples = list(combinations((11, 13, 17, 19), 3))
    hits = checks = 0
    for order in (1, 2):
        wheel = wheel_terms((3, 5), order)
        coefficients = {t: spectrum(t, wheel) for t in triples}
        for s in range(center-8, center+9):
            direct_labels = {}
            transformed_labels = {}
            for t in triples:
                direct = transformed = 0
                for b, w in records:
                    a = 2*s-b
                    wheel_value = sum(mu for j, mu in wheel.items() if a % j == 0)
                    direct += w * wheel_value * centered(a, t)
                    transformed += w * spectral_value(a, coefficients[t])
                    if order == 2 and wheel_value and a % prod(t) == 0:
                        hits += 1
                    checks += 1
                for size in (0, 2, 3):
                    for label in combinations(t, size):
                        weight = additive_log(prod(label or t))
                        direct_labels[label] = direct_labels.get(label, 0) + weight*direct
                        transformed_labels[label] = transformed_labels.get(label, 0) + weight*transformed
            assert direct_labels == transformed_labels
    assert hits >= 4
    return len(records), checks, hits


def test_common_denominators():
    triples = list(combinations((5, 7, 11, 13), 3))
    wheel = wheel_terms((3,), 1)
    denominators = {t: set(spectrum(t, wheel)) for t in triples}
    tests = 0
    for size in (0, 2, 3):
        for label in {e for t in triples for e in combinations(t, size)}:
            qs = {q for t in triples if set(label) <= set(t) for q in denominators[t]}
            fractions = [Fraction((2*a) % q, q) for q in qs for a in range(1, q) if gcd(a, q) == 1]
            ordered = sorted(fractions)
            assert len(ordered) == len(set(ordered))
            floor = Fraction(prod(label), max(qs)**2)
            gaps = [b-a for a, b in zip(ordered, ordered[1:])]
            gaps.append(1+ordered[0]-ordered[-1])
            assert min(gaps) >= floor
            tests += len(gaps)
    return tests


def count_linear(n, slope, modulus, lo, length):
    common = gcd(slope, modulus)
    if n % common:
        return 0, Fraction(0)
    step = modulus//common
    residue = 0 if step == 1 else (n//common)*pow(slope//common, -1, step) % step
    count = (lo+length-1-residue)//step - (lo-1-residue)//step
    return count, Fraction(1, step)


def test_type_i():
    triple = (5, 7, 11)
    tested = 0
    largest = Fraction(0)
    for n in (44, 70, 103):
        for slope in (29, 29*2, 29*5, 29*7*11, 29*15):
            assert any(slope % p for p in triple)
            for j in (1, 2, 3, 6):
                for lo, length in ((-11, 19), (4, 73), (89, 130)):
                    direct = sum(centered(n-slope*w, triple) for w in range(lo, lo+length)
                                 if (n-slope*w) % j == 0)
                    value = density = Fraction(0)
                    for size in range(4):
                        for ps in combinations(triple, size):
                            e = prod(ps)
                            weight = Fraction((-1)**size * e, prod(triple))
                            count, freq = count_linear(n, slope, e*j, lo, length)
                            value += weight*count
                            density += weight*freq
                    assert density == 0 and direct == value and abs(value) < 8
                    largest = max(largest, abs(value))
                    tested += 1
    assert largest > 0
    return tested, largest


def test_vaughan():
    # Completely additive integer log gives an exact prime-power von Mangoldt weight.
    def prime_power_weight(n):
        ps = factors(n)
        return ps[0].bit_length() if ps and len(set(ps)) == 1 else 0

    tests = 0
    for cap in (2, 5, 9):
        for t in range(1, 501):
            divisors = data(t)[0]
            short_log = sum(data(k)[1]*additive_log(t//k) for k in divisors if k <= cap)
            short_double = sum(data(k)[1]*prime_power_weight(j) for k in divisors if k <= cap
                               for j in data(t//k)[0] if j <= cap)
            long = sum(prime_power_weight(n) * sum(data(k)[1] for k in data(t//n)[0] if k > cap)
                       for n in divisors if n > cap)
            expected = short_log - short_double + (t <= cap)*prime_power_weight(t) + long
            assert expected == prime_power_weight(t)
            tests += 1
    return tests


if __name__ == "__main__":
    print("Frozen semiprime window (records, kernel checks, true triple incidences):", test_packet())
    print("Gaps between doubled frequencies checked:", test_common_denominators())
    print("Type I CRT intervals and largest absolute remainder:", test_type_i())
    print("Exact Vaughan identities:", test_vaughan())
