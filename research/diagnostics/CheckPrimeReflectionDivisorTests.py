"""Finite algebra and coupled 0-1 edits in PrimeReflectionDivisorTests.md."""
from itertools import combinations
from math import prod
from random import Random

from CheckLocalizedVaughan import factors
from CheckSharedPrimeCenters import primes_through


def check_window():
    x, z, y = 1009**2, 7, 160
    upper = range(x+3000, x+10001)
    flags = primes_through(upper.stop)
    small_sector = set()
    eligible = set()
    tagged = set()
    prime_sites = set()
    two_factor = 0
    for a in upper:
        n = 2*x-a
        ff = factors(a)
        m = a//max(ff)
        if min(ff) > z and len(ff) == len(set(ff)) and 1 < m <= y:
            qs = [q for q in ff if z < q <= y]
            pairs = sum(q*t <= y for q, t in combinations(qs, 2))
            # These two tests equate the constant and every prime log coefficient.
            assert len(qs)-pairs == 1 and prod(qs) == m
            two_factor += int(len(qs) == 2)
            small_sector.add(n)
        lower = factors(n)
        if min(lower) <= 5 or len(lower) != len(set(lower)):
            continue
        eligible.add(n)
        if flags[a]:
            prime_sites.add(n)
        if len(ff) == 2 and 173 < ff[0] <= 251 and ff[0] < ff[1]:
            tagged.add(n)
            assert ff[0] > y and m > y
    assert two_factor and prime_sites and tagged
    assert tagged.isdisjoint(prime_sites | small_sector)
    assert prime_sites.isdisjoint(small_sector)

    # Exact expectation calibration on these toy supports, in integer tickets.
    np, ng = len(prime_sites), len(tagged)
    total = 2*(np+ng)
    rng = Random(1728)
    ref, swapped = set(), set()
    for n in sorted(eligible):
        ticket = rng.randrange(total)
        if ticket < ng:
            ref.add(n)
        second = 0 if n in prime_sites else ng+np if n in tagged else ng
        if ticket < second:
            swapped.add(n)
    assert np*ng == ng*((ng+np)-ng)
    removed = sorted(ref-swapped)
    added = sorted(swapped-ref)
    size = min(len(removed), len(added))
    ref.difference_update(removed[size:])
    swapped.difference_update(added[size:])
    assert len(ref) == len(swapped) and size > 0
    assert ref-swapped == ref & prime_sites and swapped-ref <= tagged
    assert len(ref & prime_sites) == size and not swapped & prime_sites
    assert ref & small_sector == swapped & small_sector

    # Add some small-factor sites to exercise the union bound with real overlaps.
    odd_primes = [q for q in range(3, y+1) if flags[q]]
    extra = {2*x-a for a in upper if a % 15 == 0 and a % 2 == 1} - ref
    perturbed = swapped | extra
    new = perturbed-ref
    covered = set()
    hits = 0
    for q in odd_primes:
        b = 2*x % q
        in_class = {n for n in new if n % q == b}
        diff = sum(n % q == b for n in perturbed) - sum(n % q == b for n in ref)
        assert diff == len(in_class)
        covered.update(in_class)
        hits += diff
    assert covered == extra and hits > len(covered) > 0
    print(f"{len(upper)} upper integers, {len(small_sector)} eligible small cofactors, "
          f"{two_factor} two-prime cofactors; all formal identities passed.")
    print(f"Equal-size sets of {len(ref)} sites, {size} genuine upper partners "
          f"replaced; {len(covered)} small-factor additions gave {hits} class hits.")


if __name__ == "__main__":
    check_window()
