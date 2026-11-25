"""Exact arithmetic checks for CentralPrimeSixFactors.md. Python standard library."""

from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm, prod


def log_bounds(x, terms=160):
    """Rational bounds for log(x), x >= 1, by the atanh series."""
    s = (x - 1) / (x + 1)
    partial = 2 * sum(s ** (2*j + 1) / (2*j + 1) for j in range(terms))
    tail = 2 * s ** (2*terms + 1) / ((2*terms + 1) * (1 - s*s))
    return partial, partial + tail


def lower_log_sum(terms, constant=F(0)):
    lower = constant
    for coefficient, argument in terms:
        lo, hi = log_bounds(argument)
        lower += coefficient * (lo if coefficient > 0 else hi)
    return lower


def check_margins():
    six = lower_log_sum([(F(13, 6), F(3)), (-1, F(18, 5)), (-F(1, 5), F(15, 2)),
                         (-13, F(25, 18))], F(91, 25))
    five = lower_log_sum([(F(299, 100), F(3)), (-1, F(28, 9)), (-F(1, 2), F(27, 8)),
                          (-F(9, 2), F(18, 7))], F(11, 4))
    harmonic = sum(F(1, j) for j in range(1, 33))
    gamma_gap = lower_log_sum([(-2, F(33)), (-1, F(145, 48))], 2*harmonic)
    assert six > F(3, 50) and five > F(1, 25) and gamma_gap > 0
    assert F(13, 6) + F(24, 5) == 7 - F(1, 30)
    print("Certified six-factor margin > 3/50. Conditional five-factor margin > 1/25.")


def check_finite_sieve():
    """Test the local counts and the Selberg quadratic form at small cutoffs."""
    center = 101**2
    z, w, cutoff = 6, 13, 21
    primes = (2, 3, 5, 7, 11)
    cases = 0
    for d in (1, 2, 3, 5, 6, 10, 15, 30, 99):
        active = [ell for ell in primes if d % ell]
        period = prod(active)
        for q in (29, 31):
            nu = {}
            for ell in active:
                residues = {m for m in range(ell) if (ell < z and m == 0)
                            or (ell < w and (2*center - q*m) % ell == 0)}
                nu[ell] = len(residues)
            product = prod(1 - F(nu[ell], ell) for ell in active)
            predicted = (prod(1 - F(1, ell) for ell in active)
                         * prod(1 - F(1, ell-1) for ell in active if 2 < ell < z))
            assert predicted == product
            for b in range(d):
                if gcd(b, d) != 1 or gcd(2*center-b, d) != 1:
                    continue
                first = (2*center-b) * pow(q, -1, d) % d
                survivors = sum(all((ell >= z or m % ell) and (2*center-q*m) % ell
                                    for ell in active)
                                for m in range(first, first+d*period, d))
                assert survivors == product * period
                cases += 1

            rho, g, mu = {}, {}, {}
            for size in range(len(active)+1):
                for subset in combinations(active, size):
                    j = prod(subset)
                    rho[j] = prod((F(nu[ell], ell) for ell in subset), start=F(1))
                    g[j] = prod((F(nu[ell], ell-nu[ell]) for ell in subset), start=F(1))
                    mu[j] = (-1)**size
            support = [j for j in g if j < cutoff]
            total = sum(g[j] for j in support)
            coeff = {j: sum(mu[k//j]*mu[k]*g[k] for k in support if k % j == 0)
                     / (total*rho[j]) for j in support}
            assert coeff[1] == 1 and all(abs(v) <= 1 for v in coeff.values())
            main = sum(coeff[i]*coeff[j]*rho[lcm(i, j)] for i in support for j in support)
            assert main == 1/total and product * sum(g.values()) == 1
    print(f"Verified {cases} admissible-class periods and all 18 finite Selberg forms.")


def check_five_factor_obstruction():
    A, C, T = F(31, 8), F(67, 5), F(179, 100)
    b = (C-A)/(C-1)
    L = F(3, 4)/(1-b)
    j0 = [(1, 4*b), (1, L), (C/A, T*(A-b)/(b*(A-T)))]
    j1 = [(1, L), (C, (A-b)/(A-T))]
    assert lower_log_sum(j0) > F(660, 100)
    assert -lower_log_sum([(-k, x) for k, x in j1]) < F(659, 100)
    lo, hi = log_bounds(F(3))
    assert F(659, 100) < 6*lo <= 6*hi < F(660, 100)
    harmonic = sum(F(1, n) for n in range(1, 129))
    assert lower_log_sum([(1, 24/C), (7, F(2))], -harmonic) > 0
    start = F(7, 9)
    tail = [(C/A, 2/start), (-C/A*(A/2-1), (A-start)/(A-2))]
    assert lower_log_sum(tail) > F(1638, 1000)
    print("Certified the separate-sieve obstruction for all fixed Richert parameters at v=4.")


if __name__ == "__main__":
    check_margins()
    check_finite_sieve()
    check_five_factor_obstruction()
