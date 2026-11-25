"""Exact bounds and finite sieve checks for OrderedPrimeFactors.md."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import factorial, gcd, lcm, prod

from CheckLocalizedVaughan import factors
from CheckSharedPrimeCenters import floor_root, primes_through


def ordered_cap(j, k, s, lower_cutoff):
    weights = list(range(j, j-k, -1))
    # Each unit increment at position i increases every later exponent by one.
    for i, weight in enumerate(weights):
        exponents = [int(h >= i) for h in range(k)]
        assert sum(exponents[:-1]) + (j-k+1)*exponents[-1] == weight
    radius = min(s, lower_cutoff, (Q(2, 3)-Q(k, j))/2)
    volume = (1-j*s)**k / (factorial(k)*prod(weights))
    return 2*volume / (radius**2*s**k)


def constants():
    h = Q(1, 6)
    caps = [8*((b-r*h)/h)**r / ((Q(2, 3)-b)**2*factorial(r)**2)
            for r, b in [(1, Q(".1668")), (2, Q(".336"))]]
    for j, k, s in [(3, 1, Q(".3333")), (4, 2, Q(".249")), (5, 3, Q(".19"))]:
        caps.append(ordered_cap(j, k, s, 1))
    rounded = list(map(Q, (".025614", ".004683", ".007201", ".003097", ".091122")))
    assert all(0 < cap < ceiling for cap, ceiling in zip(caps, rounded))
    assert Q(".1395") - sum(rounded) > Q(".00778")
    five = ordered_cap(5, 3, Q(".19"), Q(1, 18))
    assert caps[-1] == five == Q(625, 6859)
    assert Q(".3457") - five > Q(".2545")
    s = Q(67, 400)
    projected_volume = (1-5*s)**3/360
    assert 648*125*projected_volume == Q(".965478515625")
    assert 8*125*projected_volume/(Q(2, 3)-3*s)**2 > Q(".4422")
    print(f"All five rational caps checked; balanced five-factor cap = {five}.")


def finite_square(target, m, radius):
    squarefree = {d: factors(d) for d in range(1, radius+1)
                  if len(factors(d)) == len(set(factors(d)))}
    primes = [d for d, fs in squarefree.items() if len(fs) == 1]
    roots = {q: (1 if (m*target) % q == 0 else 2) for q in primes}
    for q in primes:
        assert roots[q] == sum(t*(target-m*t) % q == 0 for t in range(q))

    def density(d):
        return Q(prod(roots[q] for q in set(factors(d))), d)

    h = {d: prod((Q(roots[q], q-roots[q]) for q in fs), start=Q(1))
         for d, fs in squarefree.items()}
    total = sum(h.values())
    weights = {}
    for d, fs in squarefree.items():
        coprime_sum = sum(h[e] for e in squarefree if d*e <= radius and gcd(d, e) == 1)
        weights[d] = ((-1)**len(fs)*coprime_sum/total
                      * prod(Q(q, q-roots[q]) for q in fs))
    assert weights[1] == 1 and max(map(abs, weights.values())) == 1
    main = sum(weights[d]*weights[e]*density(lcm(d, e))
               for d in weights for e in weights)
    assert main == 1/total
    start, stop = 47, 258
    observed = Q(0)
    for t in range(start, stop):
        value = t*(target-m*t)
        square = sum(w for d, w in weights.items() if value % d == 0)**2
        assert square >= int(all(value % q for q in primes))
        observed += square
    remainder_bound = sum(prod(roots[q] for q in set(factors(lcm(d, e))))
                          for d in weights for e in weights)
    assert abs(observed-(stop-start)*main) <= remainder_bound


def factor_windows():
    x = 1009**2
    start = x+2*floor_root(x**21, 40)+1
    stop = x+floor_root(x**2, 3)+1
    flags = primes_through(stop)
    small_primes = [q for q in range(5, 32) if flags[q]]
    upper_factors = {a: factors(a) for a in range(start, stop)
                     if gcd(2*x-a, 6) == 1}
    sizes = []
    repeated = 0
    for j, k in [(2, 1), (3, 1), (4, 2), (5, 3)]:
        direct = {a for a, fs in upper_factors.items()
                  if len(fs) == j and fs[0] >= 5 and fs[k-1] <= 31}
        switched = set()
        for prefix in combinations_with_replacement(small_primes, k):
            m = prod(prefix)
            for t in range((start+m-1)//m, (stop-1)//m+1):
                n = 2*x-m*t
                if gcd(n, 6) != 1:
                    continue
                tail = factors(t)
                if len(tail) == j-k and tail[0] >= prefix[-1]:
                    assert gcd(t*n, 6) == 1 and m*t not in switched
                    switched.add(m*t)
                    repeated += int(len(set(prefix)) < k)
        assert direct == switched and direct
        sizes.append(len(direct))
    assert repeated > 0
    print(f"Toy window counts for 2, 3, 4, 5 factors: {sizes}; "
          f"{repeated} sites had a repeated frozen prime.")


if __name__ == "__main__":
    constants()
    for m in (3, 5, 7, 15, 25):
        finite_square(2*11**2, m, 13)
    print("Five exact Selberg quadratic forms and 1055 pointwise squares checked.")
    factor_windows()
