"""Rational certificates and finite factor partitions for BalancedPrimeCofactors.md."""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import factorial, gcd, prod

from CheckFixedSquareVaughan import log_bounds, trap_integral
from CheckLocalizedVaughan import factors
from CheckMarkedPrimePartners import euler_exp_bounds
from CheckSharedPrimeCenters import floor_root, primes_through


def certify():
    log2, log3, log4 = (log_bounds(i) for i in (2, 3, 4))
    integral = trap_integral(3, True)
    j3, j4 = (trap_integral(i, False) for i in (3, 4))
    total_low = 12*log4[0] + 10*integral[0] - 2*log2[1]
    total_high = 12 + 10*j4[1]
    u_low, u_high = log3[0]+j3[0], log3[1]+j3[1]
    assert Q('1.2458') < u_low <= u_high < Q('1.2459')
    assert total_low > Q('15.3980') and total_high < Q('16.0612')
    assert 12*u_high < Q('14.9501') and total_low-12*u_high > Q('.4480')
    middle = 2*log_bounds(Q(20, 17))[1]
    assert total_low-12*u_high-middle > Q('.1230')

    exp_low, exp_high = euler_exp_bounds()
    relative = Q(4, factorial(15))
    center_low = (30/exp_high)*(14-16*relative)/15-1
    center_high = (30/exp_low)*(14+16*relative)/15-1
    assert Q('14.7199') < center_low <= center_high < Q('14.7219')
    assert Q('13.4740') < center_low-u_high <= center_high-u_low < Q('13.4761')
    assert total_low-center_high > Q('.6762')
    assert total_low > Q('1.0459')*center_high
    print("Certified bounds for the full count, both cofactor sectors and the 1.0459 ratio.")


def finite_checks():
    # Toy thresholds permit both one- and two-prime small cofactors, and multiple large marks.
    x, w, z, y, high_mark = 1009**2, 5, 7, 160, 250
    h, t = floor_root(x**2, 3), floor_root(x**21, 40)
    first, stop = x+2*t+1, x+h+1
    primes = primes_through(stop)
    small_primes = [ell for ell in range(2, w+1) if primes[ell]]
    primorial = prod(small_primes)
    divisors = [(prod(cs), (-1)**k) for k in range(len(small_primes)+1)
                for cs in combinations(small_primes, k)]
    direct, switched = {}, {}
    weight_parts = {"prime": Counter(), "reference": Counter()}
    weight_all = {name: Counter() for name in weight_parts}
    shapes = Counter()
    for a in range(first, stop):
        n = 2*x-a
        keep = gcd(n, primorial) == 1
        assert keep == sum(sign for d, sign in divisors if n % d == 0)
        fs = factors(a)
        if len(fs) < 2 or min(fs) <= z or len(fs) != len(set(fs)):
            continue
        r = max(fs)
        m = a//r
        marks = [q for q in fs if q > y]
        assert all((a//q <= y) == (m <= y) for q in marks)
        if m <= y:
            assert r > m and marks == [r]
            direct[a] = m, r
        for name, accept in (("prime", primes[n]), ("reference", keep)):
            if not accept:
                continue
            # The coefficient of each individual log(q) in the sum.
            weight_all[name].update(marks)
            if m <= y:
                weight_parts[name].update([r])
                shapes[name, len(fs)-1] += 1
            else:
                medium = [q for q in fs if y < q <= high_mark]
                large = [q for q in fs if q > high_mark]
                assert all(a//q >= m > y for q in large)
                weight_parts[name].update(medium+large)
                shapes[name, "multiple large marks"] += int(len(marks) >= 2)

    for m in range(z+1, y+1):
        fs = factors(m)
        if min(fs) <= z or len(fs) != len(set(fs)):
            continue
        for r in range((first+m-1)//m, (stop-1)//m+1):
            if primes[r]:
                assert r > y and m*r not in switched
                switched[m*r] = m, r
    assert direct == switched
    assert weight_all == weight_parts
    for name in weight_parts:
        assert all(shapes[name, k] > 0 for k in (1, 2, "multiple large marks"))
    print(f"Checked {stop-first} upper integers, {len(switched)} switched products, "
          "and both marked-prime coefficient partitions.")


if __name__ == "__main__":
    certify()
    finite_checks()
