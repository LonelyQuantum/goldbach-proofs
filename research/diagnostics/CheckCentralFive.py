"""Directed rational enclosures for the v=6 central five-factor sieve."""

from fractions import Fraction as F
from math import ceil

from CheckSixFactorSwitch import lower_log_sum


def sieve_table(mesh, scale):
    """Outward-rounded multiples of 1/scale at s=i/mesh, for 0 <= s <= 6."""
    size = 6 * mesh + 1
    low_l, high_l = [0] * size, [0] * size
    low_u, high_u = [scale] * size, [scale] * size

    def advance(i, lower, upper, delayed_lower, delayed_upper):
        # On [(i-1)/mesh, i/mesh], bound the increasing delayed
        # numerator and the positive denominator separately.
        j = i - mesh
        lower[i] = lower[i-1] + delayed_lower[j-1] // j
        upper[i] = upper[i-1] + (delayed_upper[j] + j-2) // (j-1)

    for i in range(2 * mesh + 1, size):
        advance(i, low_l, high_l, low_u, high_u)
        if i > 3 * mesh:
            advance(i, low_u, high_u, low_l, high_l)
    return F(low_l[-1], scale), high_u


def upper_integral(start, end, pieces, scale, upper_value):
    step = (end - start) / pieces
    total = 0
    for j in range(pieces):
        left = start + j * step
        total += ceil(scale * step * upper_value(left, left + step))
    return F(total, scale)


def certificate(theta, u, weight, max_factors, claimed_margin):
    mesh, scale = 2400, 10**12
    lower, upper = sieve_table(mesh, scale)
    split = F(6, 7)
    delta = theta - F(1, 2)
    slack = max_factors + 1 - weight - u/delta
    assert slack > 0
    intercept = theta/delta - F(1, 3)
    assert intercept > 1/u

    def small_cell(left, right):
        delayed = F(upper[ceil(mesh * 6 * (1-left))], scale)
        return (1/left - u) * delayed / (1-right)

    def large_cell(left, right):
        return (1/left - u) * F(27, 8) / (delta * (intercept-right))

    small = upper_integral(F(1, 6), split, mesh, scale, small_cell)
    large = upper_integral(split, 1/u, mesh, scale, large_cell)
    margin = weight * lower - small - large
    assert margin > claimed_margin
    print(f"H exponent {theta}, P{max_factors}: L(6) >= {lower}, "
          f"small penalty <= {small}, switched penalty <= {large}")
    print(f"Normalized margin >= {margin} > {claimed_margin}; sign slack = {slack}.")


if __name__ == "__main__":
    # gamma >= H_512 - log(513) > log(16/9).
    harmonic = sum(F(1, k) for k in range(1, 513))
    assert lower_log_sum([(-9, F(2)), (-1, F(513, 512)), (-1, F(16, 9))],
                         harmonic) > 0
    certificate(F(2, 3), F(11, 20), F(269, 100), 5, F(3, 100))
    certificate(F(11, 15), F(2, 3), F(427, 200), 4, F(1, 50))
