"""Rational checks for the marked square, prefix tree and finite profile bounds."""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import comb, prod

from CheckCompositePartnerWeight import log_bounds


def subsets(xs):
    for j in range(len(xs) + 1):
        yield from combinations(xs, j)


def profile(w, xs):
    return sum((-1)**len(u) * max(F(0), 1 - sum(u)/w) for u in subsets(xs))


def directed_box_bounds():
    lam_lo, lam_hi = log_bounds(5)
    i_lo, i_hi = log_bounds(65)
    debit = F(9) * F(2, 100)**2 / (4*F(85, 1000)*F(105, 1000))
    boxes = [(30, 45, 9, F(1507, 10**6)), (42, 44, 10, F(2351, 10**10))]
    for low, high, cutoff, threshold in boxes:
        assert 4*high + 2*cutoff < 200 and cutoff < low < high < 85
        # log(high/low) = 2 atanh((high-low)/(high+low)), upper geometric tail.
        x = F(high-low, high+low)
        upper_log = 2*(sum(x**(2*j+1)/(2*j+1) for j in range(10))
                       + x**21/(21*(1-x*x)))
        upper = debit * F(10, cutoff)*lam_hi/i_lo * upper_log**4/24
        assert upper < threshold
        print(f"four factors [{low},{high}]/1000: certified < {threshold}")
    assert lam_lo > 0 and i_hi < 1 and F(945494, 10**6)+F(34, 1000) < F(980, 1000)


def explicit_tail_bound():
    low_lam, high_lam = log_bounds(5)
    low_i, _ = log_bounds(65)
    q = F(1, 100)*high_lam/low_i
    assert q < F(12, 100) and q/F(85, 1000)**2 < 17
    assert q/F(85, 1000) < F(142, 100)
    depth_cost = 16*15*14*F(75, 1000)*F(1, 100)/(low_i*F(1, 80)*low_lam)
    assert depth_cost*F(15, 100)/F(9, 100)**2 < 1500**2
    k = 4096
    assert F(96, k) < F(3, 100) and F(k, 2)-47 >= F(k, 3)
    log2_upper = 2*(F(1, 3) + F(1, 81)/(1-F(1, 9)))
    assert (96*12*log2_upper)**6 < k**5
    assert F(71, 100)**2 > F(1, 2)
    assert F(71, 29) < 3 and F(7100, 29**2) < 9
    upper = F(300000, 8**12)*(F(13*8, 7)+F(8, 49))
    assert upper < F(66, 10**6)
    assert F(34, 1000)-F(66, 10**6)-F(1507, 10**6) == F(32427, 10**6)
    print("k >= 4096: certified dyadic budget < 66/1000000")


def profile_checks():
    wm, wp = F(105, 1000), F(125, 1000)
    xs = [F(i, 10000) for i in [420, 430, 435, 440]]
    assert max(map(sum, combinations(xs, 2))) < wm < wp < min(map(sum, combinations(xs, 3)))
    assert (profile(wm, xs), profile(wp, xs)) == (-F(2, 7), F(6, 25))
    assert -profile(wm, xs)*profile(wp, xs) == F(12, 175) > F(34, 1000)
    checks = 0
    for count in range(1, 7):
        for config in combinations_with_replacement(range(1, 5), count):
            # Test every open interval between integer knots at its midpoint.
            signs = [((-1)**len(u), sum(u)) for u in subsets(config)]
            slopes = [sum(sign for sign, knot in signs if knot <= left)
                      for left in range(sum(config)+1)]
            assert max(map(abs, slopes)) <= comb(count-1, (count-1)//2)
            checks += len(slopes)
    return checks


def divisibility_model():
    primes = (3, 5, 7, 11, 13, 17, 19)
    records = [(prod(u), u, (-1)**len(u), prod(p-1 for p in u))
               for u in subsets(primes) if prod(u) <= 150]
    endpoints = [7, 12, 17, 31, 50, 77, 109, 150]
    marked = (3, 7, 11)
    cut = endpoints[-1]
    target = sum(F(sum((-1)**len(v) for v in subsets(marked) if j*prod(v) <= cut)**2, phi)
                 for j, u, sign, phi in records if not set(u).intersection(marked))/prod(marked)
    accumulated = F(0)
    tree_mass = [F(0)]*4
    max_mass = F(0)
    gate_mass = F(0)
    prefix_mass = sum(F(1, phi) for j, u, sign, phi in records)
    aux_mass = sum(F(1, phi) for j, u, sign, phi in records if j <= 5)
    for atom in subsets(primes):
        hits = set(atom)
        probability = F(prod(p-1 for p in primes if p not in hits), prod(primes))
        terms = [(j, F(sign*prod(p-1 if p in hits else -1 for p in u), phi))
                 for j, u, sign, phi in records]
        prefixes = [sum(v for j, v in terms if j <= b) for b in endpoints]
        assert abs(prefixes[-1]) <= 2**len(atom)*prefix_mass
        if set(marked) <= hits:
            accumulated += probability*prefixes[-1]**2
        pieces = [b-a for a, b in zip([0]+prefixes, prefixes)]
        cost = F(0)
        for depth in range(4):
            squares = sum(v*v for v in pieces)
            tree_mass[depth] += probability*squares
            cost += squares
            pieces = [a+b for a,b in zip(pieces[::2], pieces[1::2])]
        maximum = max(v*v for v in prefixes)
        assert maximum <= 4*cost
        max_mass += probability*maximum
        # Auxiliary radius 5 excludes 3 and 5. Test the majorant including
        # j divisible by gate primes, then its disjoint-support expectation.
        aux = sum(v for j,v in terms if j <= 5)/aux_mass
        positive = sum(F(prod(1+(p-2)*(p in hits) for p in u if p > 5), phi)
                       for j, u, sign, phi in records if 31 < j <= 109)
        gated = abs(prefixes[-2]-prefixes[3]) if hits.isdisjoint((3,5)) else 0
        assert gated <= aux**2*positive
        gate_mass += probability*aux**2*positive
    independent = sum(F(1, phi)*prod(1+F(p-2,p) for p in u if p>5)
                      for j,u,sign,phi in records if 31 < j <= 109)/aux_mass
    assert accumulated == target and gate_mass == independent
    assert tree_mass == [prefix_mass]*4 and max_mass <= 16*prefix_mass
    return 2**len(primes)


if __name__ == "__main__":
    explicit_tail_bound()
    directed_box_bounds()
    print(f"checked {profile_checks()} profile slopes and four-factor signs")
    print(f"checked {divisibility_model()} exact atoms for the tag, gate and prefix tree")
