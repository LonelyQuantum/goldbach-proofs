"""Finite CRT, convolution and truncation checks for CentralPrimePairPacket.md."""

from fractions import Fraction as F
from math import comb, gcd, lcm, prod


def local_products():
    primes = (2, 3, 5, 7)
    wheel = prod(primes)
    density = prod(F(p-1, p) for p in primes)
    cases = 0
    for d in (1, 2, 4, 6, 9, 10, 15):
        period = lcm(wheel, d)
        for center in range(wheel):
            n = 2 * center
            for b in range(d):
                if gcd(b, d) != 1 or gcd(n-b, d) != 1:
                    continue
                hits = sum(gcd(a*(n-a), wheel) == 1
                           for a in range((n-b) % d, period, d))
                expected = F(1, d) * prod(
                    1-F(len({0, n % p}), p) for p in primes if d % p)
                assert F(hits, period) / density**2 == expected / density**2
                cases += 1
    return cases


def convolution():
    wheel = 2*3*5
    def model(n):
        return F(15, 4) if gcd(n, wheel) == 1 else F(0)
    def signal(n):
        return (n**2 + 3*n + 7) % 13
    lower = range(40, 79)
    panels = [range(j, min(j+7, lower.stop)) for j in range(lower.start, lower.stop, 7)]
    for x in range(80, 92):
        mixed = [F(0)] * 4
        direct = 0
        for block in panels:
            for a in block:
                t = 2*x-a
                if t % 3 != 1:
                    continue
                direct += signal(a)*signal(t)
                m, k = model(a), model(t)
                e, f = signal(a)-m, signal(t)-k
                for i, value in enumerate((m*k, e*k, m*f, e*f)):
                    mixed[i] += value
        assert direct == sum(mixed)


def truncations():
    for hits in range(24):
        for r in range(1, 12):
            upper_or_lower = sum((-1)**j * comb(hits, j) for j in range(r))
            other = upper_or_lower + (-1)**r * comb(hits, r)
            assert min(other, upper_or_lower) <= int(hits == 0) <= max(other, upper_or_lower)
            assert abs(other-upper_or_lower) == comb(hits, r)
    assert F(72, 11) - F(1, 2) - 2 > 4
    assert F(4, 4**4) == F(1, 64)
    assert F(1, 1-F(1, 64)) - 1 == F(1, 63)
    assert (F(51, 50) - F(62, 63)) * F(5, 8) < F(23, 1000)


if __name__ == "__main__":
    cases = local_products()
    convolution()
    truncations()
    print(f"Verified {cases} local class factors, 12 panel identities, "
          "Bonferroni brackets and the signed excess budget < 0.023.")
