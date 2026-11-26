"""Exact Selberg-root checks and directed constants for CompositePartnerWeight.md."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import prod

from CheckPairTripleDispersion import ceil_div, geometric_nodes


def log_bounds(inv):
    lower = sum(F((-1)**(j+1), j*inv**j) for j in range(1, 13))
    return lower, lower + F(1, 13*inv**13)


def exponent_sums(n, upper):
    grid = 2400*n*100000
    if upper:
        nodes = range(0, 2*n+1, 2)
        weights = [1]+[2]*(n-1)+[1]
    else:
        nodes = range(1, 2*n, 2)
        weights = [1]*n
    geo = geometric_nodes(grid, 2*n)
    tau = [17*grid//50 + i*grid//(200*n) for i in nodes]
    flat = [grid//16 + i*grid//(160*n) for i in nodes]
    log_nodes = [geo[i]-int(not upper) for i in nodes]
    counts = Counter({0: 1})
    for xs, multiplier in ((tau, 1), (flat, 2), (log_nodes, 2), (log_nodes, 2)):
        new = Counter()
        for a, mass in counts.items():
            for x, w in zip(xs, weights):
                new[a+multiplier*x] += mass*w
        counts = new
    return counts, grid, sum(weights)**4


def constants(n=48):
    lam_lo, lam_hi = log_bounds(5)
    i_lo, i_hi = log_bounds(65)
    scale = 10**9
    values = {}
    for upper in (False, True):
        counts, grid, total = exponent_sums(n, upper)
        assert sum(counts.values()) == total
        factor = F(2, 100) * (lam_hi/i_lo if upper else lam_lo/i_hi)
        for sigma, power in ((F(0), 1), (F(1, 40), 1), (F(1, 40), 2), (-F(1, 100), 1)):
            shift = grid*sigma
            assert shift.denominator == 1
            gaps = ((grid-int(shift)-x, w) for x, w in counts.items())
            value = 0
            for gap, w in gaps:
                assert gap > 0
                numer, denom = scale*grid**power, gap**power
                value += w*(ceil_div(numer, denom) if upper else numer//denom)
            values[sigma, power, upper] = factor*F(value, scale*total)
    zero_lo, zero_hi = (values[0, 1, end] for end in (False, True))
    coarse_lo, coarse_hi = (values[F(1, 40), 1, end] for end in (False, True))
    mixed_hi = values[-F(1, 100), 1, True]
    # log 2 = 2 atanh(1/3), positive series.
    log2_lo = 2*sum(F(1, (2*k+1)*3**(2*k+1)) for k in range(6))
    tagged = F(2, 200)*F(2, 3)*log2_lo*values[F(1, 40), 2, False]
    assert zero_lo > F(98455, 100000) and zero_hi < F(98459, 100000)
    assert coarse_lo-zero_hi > F(1134, 10000) and coarse_hi < F(10982, 10000)
    assert tagged > F(233, 10000) and mixed_hi < F(9456, 10000)
    assert 1-lam_hi/zero_lo > F(814, 1000)
    def directed(x, up):
        a = x*10**6
        return ceil_div(a.numerator, a.denominator) if up else a.numerator//a.denominator
    return {"C0 lower/upper": (directed(zero_lo, False), directed(zero_hi, True)),
            "coarse lower/upper": (directed(coarse_lo, False), directed(coarse_hi, True)),
            "tagged lower": directed(tagged, False), "mixed upper": directed(mixed_hi, True)}


def root_data(cut, primes):
    support = [t for size in range(len(primes)+1) for t in combinations(primes, size) if prod(t) <= cut]
    mass = sum(F(1, prod(p-1 for p in t)) for t in support)
    return support, mass


def root(support, mass, hit):
    return sum(F((-1)**len(t)*prod(p-1 if p in hit else -1 for p in t),
                 prod(p-1 for p in t)) for t in support)/mass


def finite_checks():
    primes = (3, 5, 7, 11, 13, 17, 19)
    short, gs = root_data(23, primes)
    long, gl = root_data(49, primes)
    moment = Counter()
    witness = None
    marked = (3, 5)
    for size in range(len(primes)+1):
        for t in combinations(primes, size):
            h = set(t)
            prob = prod(F(1 if p in h else p-1, p) for p in primes)
            f, g = root(short, gs, h), root(long, gl, h)
            moment["short"] += prob*f*f
            moment["mixed"] += prob*f*g
            moment["long"] += prob*g*g
            for tag in ((3,), (5,), marked):
                if set(tag) <= h:
                    moment[tag] += prob*f*f
            if len(h) <= 1:
                assert f*g >= 0
            if f*g < 0 and witness is None:
                witness = (tuple(t), f, g)
    assert moment["short"] == 1/gs and moment["mixed"] == moment["long"] == 1/gl
    for tag in ((3,), (5,), marked):
        local = F(0)
        for j in short:
            if not set(j).isdisjoint(tag):
                continue
            alt = sum((-1)**k for k in range(len(tag)+1) for u in combinations(tag, k)
                      if prod(j)*prod(u) <= 23)
            local += F(alt**2, prod(p-1 for p in j))
        assert moment[tag] == local/(prod(tag)*gs**2)
    assert witness
    for y in range(101):
        assert F(4*y-y*(y-1), 6) <= int(y > 0)
    return 2**len(primes), witness


def profile_checks():
    tested = 0
    for k in (1, 2, 3):
        for xs in combinations_with_replacement(range(1, 9), k):
            total = sum(xs)
            for h in range(1, total+3):
                val = sum((-1)**j*max(h-sum(t), 0) for j in range(k+1)
                          for t in combinations(xs, j))
                if k <= 2:
                    assert val >= 0
                else:
                    assert val*(total-2*h) >= 0
                    if total == 2*h:
                        assert val == 0
                tested += 1
    return tested


if __name__ == "__main__":
    print("Certified constants in millionths:", constants())
    print("Exact atoms and a negative mixed-root witness:", finite_checks())
    print("Finite-difference sign checks:", profile_checks())
