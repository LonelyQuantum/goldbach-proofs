"""Rational checks for the full four-prime distribution and the arc obstruction."""
from fractions import Fraction as Q
from math import factorial


def density_bounds(n):
    # u_i = (67*n + 132*(i+t))/(400*n), 0 <= t <= 1 in a cell.
    # Integrate the three reciprocal factors after eliminating the fourth.
    scale = 10**16
    low = high = sixths = 0
    for i in range(n):
        for j in range(i, n-i):
            for k in range(j, n-i-j):
                room = n-i-j-k
                volume = (1 if room == 1 else 5 if room == 2 else 6)
                perms = 1 if i == k else 3 if i == j or j == k else 6
                sixths += perms*volume
                num = perms*volume*132**3*scale
                a,b,c = (67*n+132*m for m in (i,j,k))
                low += num//(36*(a+132)*(b+132)*(c+132))
                high += -((-num)//(36*a*b*c))
    assert sixths == n**3
    return Q(low, scale), Q(high, scale)


def moment_budgets():
    s, v, largest = Q(67, 400), Q(1, 3)+Q(1, 1200), Q(1, 4)
    assert v < 2*s and v < largest*Q(7, 5)
    assert 1+Q(7, 5)+2*Q(3, 4) == Q(39, 10) < 4
    assert 4+Q(7, 5)-2*Q(3, 4) == Q(39, 10)
    # Test the limited spatial arc separation, with integral arithmetic.
    for k in (24, 28, 32):
        n, q = 2**(3*k), 2**k
        h = 256*q*((n+2).bit_length()-1)**2
        assert 4*q*(16*h+q) < 16*n
        assert (4*q)**2 < 8*n


def local_densities():
    for target in (30, 42, 90, 98, 154, 2*101**2):
        for prime in (2, 3, 5, 7, 11, 13):
            survivors = sum((target-a) % prime != 0 for a in range(1, prime))
            expected = prime-1 if target % prime == 0 else prime-2
            assert survivors == expected


if __name__ == "__main__":
    moment_budgets()
    local_densities()
    lo, hi = density_bounds(192)
    assert Q(".0715511") < lo < hi < Q(".0731696")
    log2_lower = 2*(Q(1, 3)+Q(1, 3)**3/3)
    assert 12*log2_lower*lo > Q(".5936") and 12*hi < Q(".8781")
    # gamma <= H_8-log(8) < log(2) supplies exp(gamma)<2.
    assert sum(Q(1,i) for i in range(1,9)) < 4*log2_lower
    width = hi*4/(8*factorial(7))
    assert width < Q(".0000073") and hi+width < Q(".07318")
    assert Q(".0297")-Q(".2")*Q(".07318")-Q(".0000073") > Q(".0150")
    print("c4 enclosure", lo, hi, float(lo), float(hi))
    print("rough lower and upper certificates", float(12*log2_lower*lo), float(12*hi))
