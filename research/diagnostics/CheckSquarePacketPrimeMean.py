"""Finite exact checks of the window and convolution identities in the packet proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def check_reflections():
    # Nonsymmetric data and absolute coordinates detect a wrong reflection sign.
    cases = 0
    for start in range(14, 31):
        centers = [2*m*m for m in range(start+1, start+10) if prime(m)]
        left, right = start*start-13, start*start+18
        f = {n: 8*int(prime(n))-30*int(gcd(n, 30) == 1)
             for n in range(left, right+1)}
        support = {t-n for t in centers for n in f}
        energy = {a: sum(f.get(t-a, 0) for t in centers)**2 for a in support}
        signed = sum(fn*f.get(n+s-t, 0) for t in centers for s in centers
                     for n, fn in f.items())
        assert sum(energy.values()) == signed
        window = (a for a in support if start*start < a <= start*start+30)
        assert sum(energy[a] for a in window) <= signed
        cases += 1
    return cases


def check_box_kernel():
    # Twist by quarter turns. All real and imaginary components are integers.
    phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
    cases = 0
    for left, width, d in product(range(-4, 5), (7, 14), range(1, 13)):
        f = {}
        for n in range(left, left+width):
            a, b = phases[n % 4]
            weight = (n*n+n+3) % 7 - 3
            f[n] = (weight*a, weight*b)
        total = 0
        for t in range(left-d, left+width):
            box = [v for n, v in f.items() if t < n <= t+d]
            total += sum(v[0] for v in box)**2 + sum(v[1] for v in box)**2
        gram = sum(max(0, d-abs(n-m))*(a*c+b*e)
                   for n, (a, b) in f.items() for m, (c, e) in f.items())
        assert total == gram
        cases += 1
    return cases


def check_overlap():
    for p, radius in product(range(9, 31), (8, 20, 49, 80)):
        hits = Counter(t for x in range(p, 2*p+1)
                       for t in range(x*x-radius, x*x+radius+1))
        assert max(hits.values()) <= 1+radius//p


def check_exponents():
    critical = Fraction(2, 3)
    uniform = Fraction(13, 16)
    assert 2*critical-1 == Fraction(1, 3)
    assert 2*uniform-1 == Fraction(5, 8)
    for theta in (critical, critical+Fraction(1, 1000), uniform, Fraction(9, 10)):
        assert Fraction(1, 6) < 2*theta-1 < theta
    assert Fraction(5, 8) > Fraction(7, 12)


if __name__ == "__main__":
    reflections = check_reflections()
    kernels = check_box_kernel()
    check_overlap()
    check_exponents()
    print(f"{reflections} reflection identities, {kernels} box kernels, "
          "88 overlap counts and exponent checks passed")
