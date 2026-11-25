"""Finite counting checks for SemiprimePackets.md. Run with Python 3.10 or later."""

from collections import Counter
from itertools import combinations
from math import isqrt

from CheckSharedPrimeCenters import floor_root, primes_through


def products_in_interval(lo, hi, cutoff, primes):
    """Index products of distinct retained primes by their unique smaller factor."""
    products = {}
    for q in range(cutoff, isqrt(hi - 1) + 1):
        if not primes[q]:
            continue
        first = max(q + 1, (lo + q - 1) // q)
        for t in range(first, (hi - 1) // q + 1):
            if primes[t]:
                assert q * t not in products
                products[q * t] = q
    return products


def check_packet(start, length, cutoff):
    stop = start + length
    h0 = floor_root(start**2, 3)
    primes = primes_through(start + h0 + 3 * length + 10)
    lo, hi = start - h0, stop
    products = products_in_interval(lo, hi, cutoff, primes)
    for b in range(lo, hi):
        q = next((q for q in range(2, isqrt(b) + 1) if b % q == 0), None)
        qualifies = q is not None and q >= cutoff and q < b // q and primes[b // q]
        assert products.get(b) == (q if qualifies else None)

    frozen = Counter()
    moving = Counter()
    retained_incidents = 0
    witnessed_shifted_loss_test = False
    for s in range(start, stop):
        half = floor_root(s**2, 3)
        trim = 2 * floor_root(s**21, 40)
        lower = range(s - half, s - trim)
        retained = primes.copy()
        for h in range(1, half + 1):
            if primes[s - h] and primes[s + h]:
                retained[s + h] = 0
        after = products_in_interval(lower.start, lower.stop, cutoff, retained)
        assert after == {b: products[b] for b in lower if b in products}
        assert all(not (retained[b] and retained[2*s-b]) for b in lower)
        n_prime = sum(primes[b] for b in lower)
        n_semi = sum(b in products for b in lower)
        exact = sum(primes[2*s-b] * primes[b] for b in lower)
        semi = sum(primes[2*s-b] for b in lower if b in products)
        centered = sum((7 * primes[2*s-b] - 2) *
                       (n_prime * (b in products) - n_semi * primes[b])
                       for b in lower if b % 2)
        assert centered == 7 * (n_prime * semi - n_semi * exact)
        moving.update(prime=exact, semiprime=semi)

        for size in range(3):
            for shifts in combinations((2, 3, 5, 6), size):
                before = {(b, products[b]) for b in lower if b in products and primes[2*s-b]
                          and all(primes[b+2*j] for j in shifts)}
                surviving = {(b, after[b]) for b in after if retained[2*s-b]
                             and all(retained[b+2*j] for j in shifts)}
                assert before == surviving
                retained_incidents += len(before)
                witnessed_shifted_loss_test |= bool(shifts and before and exact)

        for b in range(lo, start):
            if primes[2*s-b]:
                frozen["prime"] += primes[b]
                frozen["semiprime"] += b in products

    transposed = Counter()
    for b in range(lo, start):
        if not b % 2:
            continue
        upper_primes = sum(primes[2*start-b:2*stop-b])
        transposed["prime"] += primes[b] * upper_primes
        transposed["semiprime"] += (b in products) * upper_primes
    assert transposed == frozen
    assert witnessed_shifted_loss_test
    return moving["prime"], moving["semiprime"], retained_incidents


if __name__ == "__main__":
    for start, length, cutoff in ((101**2, 23, 5), (211**2, 47, 7), (1009**2, 31, 11)):
        exact, semi, incidences = check_packet(start, length, cutoff)
        print(f"X={start}, K={length}, q_min={cutoff}: {exact} prime pairs, "
              f"{semi} oriented semiprime pairs, {incidences} preserved incidences.")
