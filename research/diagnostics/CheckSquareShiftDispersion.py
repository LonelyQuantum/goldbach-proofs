"""Exact finite checks of the second moment and the fixed-center witness."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def check_fourier():
    # For real integer coefficients, conjugation in the Fourier identity is
    # evaluation at the inverse root. Work in a finite field without rounding.
    size, modulus = 32, 193
    z = next(r for r in range(2, modulus)
             if pow(r, size, modulus) == 1 and pow(r, size//2, modulus) != 1)
    phases = [pow(z, k, modulus) for k in range(size)]
    u = [2*int(prime(40+a)) + ((a+1) % 5 == 0) for a in range(size)]
    f = [3*int(prime(70+a)) - 2*int(gcd(a+3, 10) == 1) for a in range(size)]

    def transform(sequence, k):
        return sum(value*phases[k*n % size] for n, value in enumerate(sequence))

    g = [transform(u, k)*transform(f, k) % modulus for k in range(size)]
    conv = [sum(u[n]*f[(t-n) % size] for n in range(size)) for t in range(size)]
    checked = 0
    for j, origin, start in product((-3, -1, 0, 1, 2), (3, 14), (0, 5)):
        roots = range(start+1, start+8)
        kernel = [sum(phases[(2*j*m*m*d) % size] for m in roots)
                  for d in range(size)]
        terms = sum(g[a]*g[-b]*phases[(origin*(b-a)) % size]*kernel[(b-a) % size]
                    for a in range(size) for b in range(size))
        direct = sum(conv[(origin+2*j*m*m) % size]**2 for m in roots)
        assert (terms-direct*size**2) % modulus == 0
        if j == 0:
            assert set(kernel) == {len(roots)}
        checked += 1
    return checked


def check_reflections():
    checked = shared = clean = 0
    for center, d in product(range(110, 253), (-4, -1, 2, 6)):
        for a in range(center+20, center+40):
            b = 2*(center+d)-a
            if not (prime(a) and prime(b)):
                continue
            assert (a-2*d)+(b-2*d) == 2*(center-d)
            middle = {(min(a, 2*center-a), max(a, 2*center-a)),
                      (min(b, 2*center-b), max(b, 2*center-b))}
            exists = any(prime(x) and prime(y) for x, y in middle)
            assert exists == (prime(a-2*d) or prime(b-2*d))
            shared += exists
            clean += not exists
            checked += 1
    assert shared > 0 and clean > 0
    return checked, shared, clean


def check_wheel():
    primes = (2, 3, 5, 7, 11)
    period = prod(primes)
    units = [r for r in range(period) if gcd(r, period) == 1]
    for b in (13, 17, 23, 29, 37, 41, 43, 47):
        expected = Fraction(1)
        for p in primes:
            roots = sum((b+6*r*r) % p == 0 for r in range(1, p))
            assert roots <= 2 and (p > 3 or roots == 0)
            expected *= Fraction(p*(p-1-roots), (p-1)**2)
        survivors = sum(gcd(b+6*r*r, period) == 1 for r in units)
        assert expected == Fraction(period*survivors, len(units)**2)
    return period


if __name__ == "__main__":
    print("Discrete Fourier identities:", check_fourier())
    print("Reflections (all, shared, two composites):", check_reflections())
    print("Quadratic unit densities checked for eight primes modulo:", check_wheel())
