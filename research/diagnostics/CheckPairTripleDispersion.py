"""Rational certificates and finite identities for PairTripleDispersion.md."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import gcd, lcm

from CheckSemiprimeRecords import factors


def ceil_div(a, b):
    return -(-a//b)


def geometric_nodes(grid, panels):
    """Upper endpoints for (1/16)*(6/5)**(i/panels), in grid units."""
    nodes = []
    for i in range(panels+1):
        lo, hi = grid//16-1, 3*grid//40
        target = grid**panels * 6**i
        while hi-lo > 1:
            mid = (lo+hi)//2
            if (16*mid)**panels * 5**i >= target:
                hi = mid
            else:
                lo = mid
        nodes.append(hi)
    return nodes


LAMBDA_UP = sum(Fraction((-1)**(k+1), k*5**k) for k in range(1, 10))
SCALE = 10**7


def mean_certificate(n=24):
    grid = 2400*n*10000
    linear = [grid//16+i*grid//(80*n) for i in range(n+1)]
    geo = geometric_nodes(grid, n)
    tau = [17*grid//50+i*grid//(100*n) for i in range(n+1)]
    weights = [1]+[2]*(n-1)+[1]
    sums = Counter({0: 1})
    for nodes, factor in ((tau, 1), (linear, 2), (geo, 2), (geo, 2)):
        new = Counter()
        for x, mass in sums.items():
            for y, weight in zip(nodes, weights):
                new[x+factor*y] += mass*weight
        sums = new
    assert max(sums) < grid and sum(sums.values()) == (2*n)**4
    expectation = Fraction(sum(mass*ceil_div(SCALE*grid, grid-x) for x, mass in sums.items()),
                           SCALE*(2*n)**4)
    return 2*Fraction(131, 200)*LAMBDA_UP*expectation


def exact_two_certificate(n=80, panels=16):
    grid = 2400*n*10000
    geo = geometric_nodes(grid, panels)
    weights = [1]+[2]*(panels-1)+[1]
    tau = [17*grid//50+i*grid//(100*n) for i in range(n+1)]
    xs = [grid//16+i*grid//(80*n) for i in range(n+1)]
    # For a box use C at its three upper endpoints and a lower bound for its density.
    @lru_cache(None)
    def reciprocal_sum(offset):
        assert offset+2*geo[-1] < grid
        return sum(w*ceil_div(SCALE*grid, grid-offset-2*t) for t, w in zip(geo, weights))

    top, bottom = LAMBDA_UP.numerator, LAMBDA_UP.denominator
    total = 0
    for i in range(n):
        tau_lo, tau_hi = tau[i:i+2]
        c_den = grid*bottom*panels*SCALE
        for x_hi in xs[1:]:
            for y_hi in xs[1:]:
                c_num = (grid-tau_hi)*top*reciprocal_sum(tau_hi+2*x_hi+2*y_hi)
                if c_num >= c_den:
                    continue
                # (beta-alpha)/I >= 13/20; (v-u)=1/80.
                dens_num = 13*grid**2*bottom
                dens_den = 20*80*(grid-tau_lo)*top*y_hi
                total += (SCALE*(c_den-c_num)*dens_num)//(c_den*dens_den)
    return Fraction(total, SCALE*n**3)


def test_reduced_phases():
    checked = coincidences = 0
    for d, f in product((15, 21, 35, 55, 65, 77), repeat=2):
        modulus = lcm(d, f)
        for m, n in product(range(1, 7), repeat=2):
            delta = Fraction(m, d)-Fraction(n, f)
            q = delta.denominator
            assert modulus % q == 0
            excluded = {p for p in factors(modulus) if q % p != 0}
            for v in range(15, 48):
                mask = int(gcd(v, q) == 1)
                mask *= sum((-1)**len(t) * int(all(v % p == 0 for p in t))
                            for k in range(len(excluded)+1) for t in combinations(excluded, k))
                assert mask == int(gcd(v, modulus) == 1)
                if mask:
                    left = Fraction(m*pow(v, -1, d), d)-Fraction(n*pow(v, -1, f), f)
                    right = 0 if q == 1 else Fraction(delta.numerator*pow(v, -1, q), q)
                    assert (left-right).denominator == 1
                    checked += 1
                    coincidences += delta == 0
    assert coincidences > 0
    return checked, coincidences


def test_completion():
    # Finite Fourier completion in a field with all q-th roots, without rounding.
    field = 2311
    assert factors(field) == (field,)
    count = 0
    for q in (15, 21, 35, 55, 77):
        root = next(g for g in range(2, field) if pow(g, q, field) == 1
                    and all(pow(g, q//p, field) != 1 for p in factors(q)))
        powers = [pow(root, j, field) for j in range(q)]
        for a in (1, q-2):
            sums = [sum(powers[(a*pow(b, -1, q)+j*b) % q]
                        for b in range(q) if gcd(b, q) == 1) % field for j in range(q)]
            for lo, hi in ((5, 14), (13, 96), (30, 203)):
                weight = lambda n: (n+1)*(n+3)
                direct = sum(weight(n)*powers[(a*pow(n, -1, q)) % q]
                             for n in range(lo, hi) if gcd(n, q) == 1)
                completed = sum(sums[j]*sum(weight(n)*powers[-j*n % q] for n in range(lo, hi))
                                for j in range(q))
                assert (q*direct-completed) % field == 0
                count += 1
    return count


def test_pair_weights():
    band = (11, 13, 17, 19)
    mass = Counter()
    first = by_triple = 0
    # Odd semiprimes b and rough squarefree reflections in actual toy windows.
    centers = [(a+b)//2 for a, b in ((11*13*317, 127*353),
                                      (11*13*17*23, 127*439),
                                      (11*13*17*19, 127*359))]
    for s in centers:
        for b in range(s-1100, s-40):
            ps = factors(b)
            if len(ps) != 2 or not 79 <= ps[0] <= 151 or ps[0] == ps[1] or gcd(b, 2*s) > 1:
                continue
            a = 2*s-b
            fs = factors(a)
            if gcd(a, 30) != 1 or len(set(fs)) != len(fs):
                continue
            hits = set(band).intersection(fs)
            for p, q in combinations(sorted(hits), 2):
                weight = ps[0].bit_length()*(p.bit_length()+q.bit_length())
                mass[len(hits)] += weight
                first += weight*(len(hits)-2)
            for t in combinations(hits, 3):
                by_triple += 2*ps[0].bit_length()*sum(p.bit_length() for p in t)
    assert first == by_triple and all(mass[k] > 0 for k in (2, 3, 4))
    assert mass[2] >= sum(mass.values())-first
    return dict(sorted(mass.items()))


if __name__ == "__main__":
    mean = mean_certificate()
    two = exact_two_certificate()
    print("Upper integral for the mean <", ceil_div(mean.numerator*100000, mean.denominator), "/100000")
    print("Lower integral for exactly two >", two.numerator*100000//two.denominator, "/100000")
    assert mean < Fraction(98461, 100000)
    assert two > Fraction(2513, 100000)
    print("Reduced phase and mask identities (including coincidences):", test_reduced_phases())
    print("Finite Fourier completions:", test_completion())
    print("Toy marked weights by multiplicity:", test_pair_weights())
