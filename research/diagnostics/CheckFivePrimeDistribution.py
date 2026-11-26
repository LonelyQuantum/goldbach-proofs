"""Check the constants and finite counting identities in FivePrimeDistribution.md."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial, gcd, prod

from CheckLocalizedVaughan import factors
from CheckSharedPrimeCenters import floor_root, primes_through


def four_upper(s, beta, pieces=2048):
    width = (1-3*s-beta)/pieces
    scale = 10**12
    grid_total = 0
    for i in range(1, pieces+1):
        y = i*width
        value = y*y/(12*s*s*(s+y)*(1-3*s-y))
        grid_total += -((-scale*value.numerator)//value.denominator)
    return width*grid_total/scale


def constants():
    s = Q(67, 400)
    assert 2*s-Q(1, 3) == Q(1, 600)
    assert 2*Q(9, 25)+2*s > 1
    volume = (1-5*s)**4/factorial(4)
    c5_low = 5**5*volume/factorial(5)
    c5_high = volume/(factorial(5)*s**4*(1-4*s))
    assert Q(".00075660") < c5_low < c5_high < Q(".00093207")
    c4_large = four_upper(s, Q(2, 5))
    c4_middle = four_upper(s, Q(9, 25))
    assert c4_large < Q(".00904") and c4_middle < Q(".02434")
    assert 12*c5_high < Q(".01119")
    assert Q(".3457") - 12*c5_high > Q(".3345")
    assert Q(".3457") - 12*(c5_high+c4_middle) > Q(".0424")
    assert Q(".1395") - 11*(c5_high+c4_large) > Q(".0297")
    other = sum(map(Q, (".025614", ".004683", ".007201", ".003097")))
    assert Q(".1395") - other - 11*c5_high > Q(".08865")
    print("Five-factor density and both four-factor integrals enclosed; "
          "all four residual margins certified.")


def labelled_products(limit, ranges):
    """Dirichlet convolution retaining the multiplicity of ordered slots."""
    counts = Counter({1: 1})
    for i, choices in enumerate(ranges):
        cap = limit//prod(primes[0] for primes in ranges[i+1:])
        fresh = Counter()
        for m, multiplicity in counts.items():
            for q in choices:
                if m*q > cap:
                    break
                fresh[m*q] += multiplicity
        counts = fresh
    return counts


def toy_window():
    x = 503**2
    start = x+2*floor_root(x**21, 40)+1
    stop = x+floor_root(x**2, 3)+1
    flags = primes_through(stop)
    primes = [q for q in range(5, stop) if flags[q]]
    large = [q for q in primes if q > 107]
    assert large[0]**2 * primes[0]**2 >= stop
    site_factors = {a: factors(a) for a in range(start, stop)}
    for slots, divisor, distinguished in [([primes]*5, 120, False),
                                          ([primes]*3+[large], 6, True)]:
        counts = labelled_products(stop-1, slots)
        direct = set()
        repeated = rough = 0
        for a, fs in site_factors.items():
            good = (len(fs) == len(slots) and fs[0] >= 5
                    and (not distinguished or fs[-1] > 107))
            if not good:
                assert counts[a] == 0
                continue
            direct.add(a)
            freely_ordered = fs[:-1] if distinguished else fs
            multiplicities = Counter(freely_ordered).values()
            assert counts[a]*prod(factorial(m) for m in multiplicities) == divisor
            repeated += int(len(set(fs)) < len(fs))
            rough += int(gcd(2*x-a, 2*3*5*7) == 1)
        assert direct and repeated and rough
        switched = {a for a in counts if start <= a < stop}
        assert direct == switched
        for d in (1, 2, 3, 6, 9, 12, 18):
            in_class = sum(a % d == (2*x) % d for a in direct)
            assert in_class == sum((2*x-a) % d == 0 for a in switched)
        print(f"{len(slots)} factors: {len(direct)} toy sites, {repeated} repeated, "
              f"{rough} reflections rough through 7.")


def log_volume_checks():
    # The minimum product estimate and the symmetry removing a denominator
    # both hold pointwise in these rational prime-exponent coordinates.
    s = Q(67, 400)
    b = 1-5*s
    for first in product(range(7), repeat=4):
        last = 6-sum(first)
        if last < 0:
            continue
        u = [s+b*i/6 for i in (*first, last)]
        assert sum(u) == 1
        assert s**4*(1-4*s) <= prod(u) <= Q(1, 5)**5
        assert sum(1/prod(u[:i]+u[i+1:]) for i in range(5)) == 1/prod(u)


if __name__ == "__main__":
    constants()
    log_volume_checks()
    toy_window()
