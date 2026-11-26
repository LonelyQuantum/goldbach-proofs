"""Exact finite checks and directed quadrature for FourthDivisorSieve.md."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, prod

from CheckSemiprimeRecords import factors


def quadrature(n=16):
    # In units 1/grid every linear grid point below is an exact integer.
    grid = 2400 * n * 10000
    weights = [1] + [2] * (n-1) + [1]
    tau = [17*grid//50 + i*grid//(100*n) for i in range(n+1)]
    uniform = [grid//16 + i*grid//(80*n) for i in range(n+1)]
    log_uniform = []
    for i in range(n+1):
        # Smallest k/grid >= (1/16)*(6/5)**(i/n), certified by integer powers.
        lo, hi = grid//16-1, 3*grid//40
        while hi-lo > 1:
            mid = (lo+hi)//2
            if (16*mid)**n * 5**i >= grid**n * 6**i:
                hi = mid
            else:
                lo = mid
        log_uniform.append(hi)

    offsets = Counter({0: 1})
    for nodes in [tau, uniform] + [log_uniform]*3:
        next_offsets = Counter()
        for a, mass in offsets.items():
            for x, w in zip(nodes, weights):
                next_offsets[a+x] += mass*w
        offsets = next_offsets
    assert sum(offsets.values()) == (2*n)**5
    scale = 10**7
    total = 0
    for offset, mass in offsets.items():
        gap = 2*grid//3 - offset
        assert gap > 0
        total += mass * ((scale*grid + gap-1)//gap)
    reciprocal = Fraction(total, scale*(2*n)**5)
    log_upper = sum(Fraction((-1)**(k+1), k*5**k) for k in range(1, 10))
    half_moment = Fraction(131, 200) * log_upper**2 * reciprocal
    return reciprocal, half_moment


def test_moments():
    center = (127*359 + 11*13*17*19)//2
    prime_band = (11, 13, 17, 19)
    records = pairs = four_hits = 0
    for s in range(center-8, center+9):
        a2 = a3 = a4 = first = second = 0
        for b in range(s-650, s-40):
            fs = factors(b)
            if len(fs) != 2 or not 100 <= fs[0] <= 136 or fs[0] >= fs[1] or gcd(b, 2*s) != 1:
                continue
            a = 2*s-b
            af = factors(a)
            if gcd(a, 30) != 1 or len(af) != len(set(af)):
                continue
            records += 1
            hits = [p for p in prime_band if a % p == 0]
            four_hits += len(hits) == 4
            z = len(hits)-2
            for p, q in combinations(hits, 2):
                weight = fs[0].bit_length() * (p.bit_length() + q.bit_length())
                pairs += 1
                a2 += weight
                first += z*weight
                second += z*(z-1)*weight
            for k in (3, 4):
                mass = fs[0].bit_length() * sum(sum(p.bit_length() for p in d)
                                                  for d in combinations(hits, k))
                if k == 3:
                    a3 += mass
                else:
                    a4 += mass
        assert first == 2*a3 and second == 6*a4
        assert 2*first <= 2*a2 + second
    assert four_hits > 0
    return records, pairs, four_hits


def test_local_density():
    wheel = (2, 3, 5, 7)
    period = prod(wheel)
    cases = 0
    for target in (22, 30, 42, 210):
        for d in (13, 13*17):
            for k in (1, 19, 19*23):
                r = 29
                assert gcd(r*d*k, period) == 1
                residue = k * (target*pow(r*k, -1, d) % d)
                valid = sum(gcd(t*(target-r*t), period) == 1
                            for t in range(residue, residue+period*d*k, d*k))
                nu = [1 + int(target % p != 0) for p in wheel]
                assert valid == prod(p-v for p, v in zip(wheel, nu))
                delta = prod(Fraction(p-2, p-1) for p in wheel if target % p)
                assert Fraction(valid, prod(p-1 for p in wheel)) == delta
                cases += 1
    return cases


def test_inclusion_model():
    band = (23, 29, 31, 37, 41)
    subsets = [frozenset(t) for k in range(len(band)+1) for t in combinations(band, k)]
    c = {p: Fraction(1, p-1) for p in band}
    lam = sum(c.values())
    inc = {t: prod((c[p] for p in t), start=Fraction(1)) for t in subsets}
    moments = {t: inc[t] if len(t) < 3 else inc[t]/lam if len(t) == 3 else 0 for t in subsets}
    atoms = {t: sum((-1)**(len(k)-len(t))*moments[k] for k in subsets if t <= k) for t in subsets}
    assert min(atoms.values()) >= 0 and sum(atoms.values()) == 1
    for t in subsets:
        assert sum(atoms[k] for k in subsets if t <= k) == moments[t]
    weight = lambda t: sum(p.bit_length() for p in t)
    pair_mass = sum(inc[t]*weight(t) for t in subsets if len(t) == 2)
    independent_triples = sum(inc[t]*weight(t) for t in subsets if len(t) == 3)
    extra = sum(atoms[k] * (len(k)-2) * sum(weight(t) for t in combinations(k, 2)) for k in subsets)
    assert extra/pair_mass == 2*independent_triples/(lam*pair_mass)
    return len(atoms)


if __name__ == "__main__":
    bound, half = quadrature()
    print("16-panel quadrature: E[1/gap] <", (int(bound*10000)+1), "/10000")
    print("Half factorial moment: limsup <", (int(half*100000)+1), "/100000")
    assert bound < Fraction(218007, 10000) and half < Fraction(47467, 100000)
    print("Genuine toy windows (records, marked pairs, four-hit records):", test_moments())
    print("CRT wheel densities:", test_local_density())
    print("Nonnegative model atoms checked:", test_inclusion_model())
