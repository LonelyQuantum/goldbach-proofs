"""Directed two-radius and external-prime tests for the high four-factor debit."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import factorial, prod
import argparse

import numpy as np
from numba import njit
from scipy.sparse import coo_matrix, vstack

from CheckFourFactorScales import (
    GRID,
    ceil_ratio,
    certified_cover,
    high_edges,
    high_problem,
    solve_cover,
    log_sandwich,
    log_width_upper,
    physical_bins,
)


@njit
def ramp_combo(u, c, d, A, B):
    return A * d * max(0, c - u) + B * c * max(0, d - u)


@njit
def interval(lo, hi, c, d, A, B):
    start = ramp_combo(lo, c, d, A, B)
    end = ramp_combo(hi, c, d, A, B)
    lower, upper = min(start, end), max(start, end)
    if lo < c < hi:
        val = ramp_combo(c, c, d, A, B)
        lower, upper = min(lower, val), max(upper, val)
    if lo < d < hi:
        lower, upper = min(lower, 0), max(upper, 0)
    return lower, upper


@njit
def coefficients(lower, upper, copies, c, d, A, B, pair_terms):
    values = np.empty(len(lower), dtype=np.int64)
    den = c * d
    for i in range(len(lower)):
        left = right = (A + B) * den
        for j in range(lower.shape[1]):
            l, h = interval(lower[i, j], upper[i, j], c, d, A, B)
            left -= h
            right -= l
            if pair_terms:
                for k in range(j):
                    l, h = interval(
                        lower[i, j] + lower[i, k], upper[i, j] + upper[i, k], c, d, A, B
                    )
                    left += l
                    right += h
        dist = (4096 * max(0, left, -right)) // den
        values[i] = (copies[i] * dist * dist) // 16384
    return values


def project(configurations, edges, max_tags):
    # Group all occurrences with the same unresolved tag bins and multiplicity.
    groups = {}
    for col, box in enumerate(configurations):
        for ntag in range(max_tags + 1):
            for tags, copies in Counter(combinations(box, ntag)).items():
                rem = list(box)
                for tag in tags:
                    rem.remove(tag)
                groups.setdefault(tags, []).append((col, copies, rem))
    result = []
    grid = np.array(edges)
    for tags, items in groups.items():
        cols, copies, rem = zip(*items)
        ids = np.array(rem)
        widths = prod(log_width_upper(edges[k], edges[k + 1]) for k in tags)
        widths /= prod(factorial(k) for k in Counter(tags).values())
        result.append(
            (
                tags,
                np.array(cols),
                np.array(copies),
                grid[ids],
                grid[ids + 1],
                F(widths),
            )
        )
    return result


@lru_cache(None)
def candidates(limit, joint):
    if limit < 4:
        return []
    radii = sorted({limit * j // 12 for j in range(2, 13)} - {0})
    if not joint:
        return [(d, d, 0, 1) for d in radii]
    return [
        (c, d, A, B)
        for d in radii[3::2] + [limit]
        for c in radii
        if c < d
        for A, B in (
            (1, -1),
            (1, -2),
            (2, -1),
            (1, 1),
            (1, 2),
            (2, 1),
            (2, -3),
            (3, -2),
            (1, -4),
            (1, -8),
            (1, -16),
            (1, 4),
            (1, 8),
            (1, 16),
            (4, -1),
            (4, 1),
        )
    ]


@lru_cache(None)
def price(c, d, A, B):
    return GRID * (F(A * A, d * c) * (d - c) + F((A + B) ** 2, d))


def best_rows(group, edges, level, sol, existing, joint, keep, max_multiplier):
    tags, cols, copies, lower, upper, size = group
    primal = sol[cols]
    active = primal > 1.0e-12
    if not np.any(active):
        return []
    limit = (level - sum(edges[i + 1] for i in tags)) // 2
    lp, small_lo, small_hi, small_copies = (
        primal[active],
        lower[active],
        upper[active],
        copies[active],
    )
    pool = []
    for c, d, A, B in candidates(limit, joint):
        if max(abs(A), abs(B)) > max_multiplier:
            continue
        key = (tags, c, d, A, B)
        if key in existing:
            continue
        p = size * price(c, d, A, B)
        data = coefficients(small_lo, small_hi, small_copies, c, d, A, B, not tags)
        score = np.dot(lp, data) / (1024 * float(p))
        if score > 1.0001:
            pool.append((score, key, p))
    selected = []
    for _, key, p in sorted(pool, key=lambda entry: -entry[0]):
        if key in existing:
            continue
        _, c, d, A, B = key
        data = coefficients(lower, upper, copies, c, d, A, B, not tags)
        mask = data > 0
        selected.append((cols[mask], data[mask], p))
        existing.add(key)
        if len(selected) >= keep:
            break
    return selected


def append_rows(mat, prices, rows):
    if not rows:
        return mat, prices
    rownum = np.concatenate(
        [np.full(len(cols), i) for i, (cols, _, _) in enumerate(rows)]
    )
    cols = np.concatenate([r[0] for r in rows])
    data = np.concatenate([r[1] for r in rows])
    add = coo_matrix((data, (rownum, cols)), shape=(len(rows), mat.shape[1]))
    return vstack([mat, add], format="csc"), prices + [r[2] for r in rows]


def external_squares(lower, upper, counts, d, width, mixed):
    tests = (
        [(d, 0, 1)]
        if not mixed
        else [
            (c, A, B)
            for c in {d // 2, 3 * d // 4, 7 * d // 8}
            if c > 0
            for A, B in ((1, -1), (1, -2), (1, 2), (1, -4), (1, 4))
        ]
    )
    for c, A, B in tests:
        vals = coefficients(lower, upper, counts, c, d, A, B, True)
        nz = np.flatnonzero(vals)
        if len(nz):
            yield nz, vals[nz], width * price(c, d, A, B)


def external_rows(configurations, edges, level, bl, bh):
    # m necessarily prime when its upper exponent is below 2. Tag that prime.
    ee = np.asarray(edges)
    configs = np.asarray(configurations)
    lower, upper = ee[configs], ee[configs + 1]
    mlo = (650 * GRID // bh) - np.sum(upper, axis=1)
    mhi = ceil_ratio(660 * GRID, bl) - np.sum(lower, axis=1)
    rows = []
    # The true tau and b ranges are enclosed in the bounds used here.
    for j in range(16, 31):
        for k in (j + 1, j + 2, j + 4, j + 8):
            u, v = j * GRID // 16, k * GRID // 16
            d = (level - v) // 2
            if d <= 0:
                continue
            cols = np.flatnonzero((mlo >= u) & (mhi <= v))
            if len(cols) == 0:
                continue
            # Under the level test, v<2, so the tag equals the whole tail m.
            for mixed in (False, True):
                counts = np.ones(len(cols), dtype=np.int64)
                for nz, coef, p in external_squares(
                    lower[cols], upper[cols], counts, d, log_width_upper(u, v), mixed
                ):
                    rows.append((cols[nz], coef, p))
    return rows, mlo


def tail_bound(mat, prices, weights, configs, edges, level, bl, min_factors):
    # If m has h factors, each missed by (1,v] consumes more than v-1
    # of the excess H-h. The resulting lower bound increases in h.
    grid = np.asarray(edges)
    box = np.asarray(configs)
    low, high = grid[box], grid[box + 1]
    top = ceil_ratio(660 * GRID, bl) - np.sum(low, axis=1)
    ids = np.flatnonzero(top >= min_factors * GRID)
    if not len(ids):
        return (F(0),) * 3
    m = mat[:, ids].tocsc()
    w = np.asarray(weights)[ids].tolist()
    raw = certified_cover(m, prices, w)[0]
    extra, mixed_rows = [], []
    top, low, high = top[ids], low[ids], high[ids]
    for j in range(1, 30):
        v = GRID + j * GRID // 32
        d = (level - v) // 2
        if d <= 0:
            continue
        count = np.maximum(0, min_factors - (top - min_factors * GRID) // (v - GRID))
        # Each actual mark is a prime divisor of m; all its other outer factors exceed d.
        width = log_width_upper(GRID, v)
        extra.extend(external_squares(low, high, count, d, width, False))
        mixed_rows.extend(external_squares(low, high, count, d, width, True))
    if not extra:
        return raw, raw, raw
    m, new_prices = append_rows(m, prices, extra)
    single = min(raw, certified_cover(m, new_prices, w)[0])
    m, new_prices = append_rows(m, new_prices, mixed_rows)
    return raw, single, min(single, certified_cover(m, new_prices, w)[0])


@njit
def finer_prices(configs, edges, amin, subdivisions):
    """Bound W on subboxes using outward integer edges and the two high profiles."""
    out = np.zeros(len(configs), dtype=np.int64)
    delta = GRID - amin
    for j in range(len(configs)):
        e = edges[configs[j]]
        end = edges[configs[j] + 1]
        lo = np.empty((4, subdivisions), dtype=np.int64)
        hi = np.empty((4, subdivisions), dtype=np.int64)
        for i in range(4):
            for h in range(subdivisions):
                lo[i, h] = e[i] + (end[i] - e[i]) * h // subdivisions
                hi[i, h] = (
                    e[i]
                    + ((end[i] - e[i]) * (h + 1) + subdivisions - 1) // subdivisions
                )
        best = 0
        for ix in range(subdivisions):
            x, X = lo[0, ix], hi[0, ix]
            for iy in range(subdivisions):
                y, Y = lo[1, iy], hi[1, iy]
                if x > Y or X + Y <= amin:
                    continue
                for iv in range(subdivisions):
                    v, V = lo[2, iv], hi[2, iv]
                    if y > V or X + Y + V <= 2 * amin:
                        continue
                    for iz in range(subdivisions):
                        z, Z = lo[3, iz], hi[3, iz]
                        if v > Z:
                            continue
                        sl = x + y + v + z
                        pos = min(
                            X,
                            X + Y - amin,
                            X + Y + V - 2 * amin,
                            X + Y + V + Z - 3 * amin,
                        )
                        if sl >= 3 * GRID or pos <= 0:
                            continue
                        pairs = (
                            max(0, GRID - Y - V)
                            + max(0, GRID - Y - Z)
                            + max(0, GRID - V - Z)
                        )
                        neg = min(
                            3 * GRID
                            - sl
                            - pairs
                            - max(0, GRID - X - Y)
                            - max(0, GRID - X - V)
                            - max(0, GRID - X - Z),
                            min(X, GRID - y)
                            + min(X, GRID - v)
                            + min(X, GRID - z)
                            - x
                            - pairs,
                        )
                        if neg > 0:
                            best = max(best, min(4 * pos * neg, 9 * delta * delta))
        out[j] = best
    # best is 4*GRID^2 times a numerator upper. Final scaling uses Python integers.
    return out


def refined_weights(configs, edges, delta, subdivisions):
    amin = GRID - delta
    raw = finer_prices(np.asarray(configs), np.asarray(edges), amin, subdivisions)
    return [ceil_ratio(10**11 * int(val), 4 * GRID * amin) for val in raw]


def run_block(bl, bh, n, rounds, max_tags, prime_slice):
    # The level changes between exterior blocks; keep their direction grids local in memory.
    candidates.cache_clear()
    price.cache_clear()
    delta = ceil_ratio(20 * GRID, bl)
    mat, prices, weights, configs, edges, level = high_problem(delta, n)
    base_weights = weights
    weights = refined_weights(configs, edges, delta, 6)
    assert all(w <= v for w, v in zip(weights, base_weights))
    # In this exterior panel the larger single-radius candidate problem stalls.
    # Its separately verified smaller cover suffices for the reported bound.
    compact = bl == 125
    groups = project(configs, edges, min(1, max_tags) if compact else max_tags)
    current = solve_cover(mat, prices, weights)
    values = [certified_cover(mat, prices, weights, current)[0]]
    existing = set()
    for joint in (False, True):
        for j in range(rounds):
            rows = []
            for g in groups:
                rows.extend(
                    best_rows(
                        g,
                        edges,
                        level,
                        current.x,
                        existing,
                        joint,
                        2 if g[0] else 6,
                        3 if compact else 16,
                    )
                )
            if not rows:
                break
            mat, prices = append_rows(mat, prices, rows)
            current = solve_cover(mat, prices, weights)
        values.append(
            min(values[-1], certified_cover(mat, prices, weights, current)[0])
        )
    ext, mlo = external_rows(configs, edges, level, bl, bh)
    if ext:
        mat, prices = append_rows(mat, prices, ext)
        current = solve_cover(mat, prices, weights)
    values.append(min(values[-1], certified_cover(mat, prices, weights, current)[0]))
    if prime_slice:
        # Every configuration with actual log(m)/log(B+) < 2 satisfies this outer mask.
        # Include equality for the limiting window and its vanishing endpoint shifts.
        selected = np.flatnonzero(mlo <= 2 * GRID)
        if len(selected):
            m = mat[:, selected].tocsc()
            w = np.asarray(weights)[selected].tolist()
            values.append(min(values[-1], certified_cover(m, prices, w)[0]))
        else:
            values.append(F(0))
    return values, len(ext)


def audit(n, rounds, max_tags, prime_slice=True, min_factors=0):
    if min_factors:
        print(
            "minimum outer factor count",
            min_factors,
            "columns: size / marked single / marked joint",
            flush=True,
        )
    else:
        print(
            "columns: refined baseline / internal singles / internal joint / plus outer marks / forced-prime slice",
            flush=True,
        )
    boxes, q, total = physical_bins(count=1, panels=16)
    by_block = {}
    for (lo, hi), mass in boxes.items():
        bl = 5 * (lo // 5)
        _, last, old = by_block.get(bl, (bl, 0, F(0)))
        by_block[bl] = (
            bl,
            max(last, hi),
            old + F(mass * q, lo * total) * log_sandwich(),
        )
    totals = [F(0)] * (3 if min_factors else (5 if prime_slice else 4))
    for bl, bh, scale in sorted(by_block.values()):
        if min_factors:
            delta = ceil_ratio(20 * GRID, bl)
            if F(660, bl) - 3 * (1 - F(20, bl)) < min_factors:
                vs = (F(0),) * 3
            else:
                mat, prices, _, configs, edges, level = high_problem(delta, n)
                weights = refined_weights(configs, edges, delta, 6)
                vs = tail_bound(
                    mat, prices, weights, configs, edges, level, bl, min_factors
                )
            r = None
        else:
            vs, r = run_block(bl, bh, n, rounds, max_tags, prime_slice)
        totals = [t + scale * v for t, v in zip(totals, vs)]
        print(
            "block",
            bl,
            bh,
            "external rows",
            r,
            "upper in billionths",
            [ceil_ratio(v.numerator * 10**9, v.denominator) for v in vs],
            flush=True,
        )
    print(
        "high upper in ten-millionths",
        [ceil_ratio(t.numerator * 10**7, t.denominator) for t in totals],
        flush=True,
    )
    if n == 44 and (min_factors or (max_tags == 2 and rounds == 2 and prime_slice)):
        ceilings = {
            0: (201193, 201193, 201065, 201065, 81832),
            2: (201030, 200829, 200804),
            3: (68504, 47566, 45641),
        }[min_factors]
        assert len(totals) == len(ceilings)
        assert all(t <= F(cap, 10**7) for t, cap in zip(totals, ceilings))
    return totals


def marked_prime_example():
    b, tau, H = F(18, 125), F(69, 200), F(8, 5)
    a, T, S = 1 - F(1, 50) / b, 2 - F(1, 100) / b, (1 - tau) / b - H
    c, d = F(1, 16), F(1, 8)
    d0 = (F(101, 100) - tau - 2 * b) / 2
    assert F(3, 16) < d0 < F(9, 40) and H + 2 * d < T < 2
    for x in (c, d):
        y = (S - x) / 3
        band = (x, y - F(1, 1000), y, y + F(1, 1000))
        assert max(band) < 1 and min(band[1:]) > max(a, (T - H) / 2)
        assert x + band[1] > 1 and 3 * a < S < 3 and 1 < H < 2
        for r, expected in ((a, x), (F(1), S - 3)):
            actual = sum(
                (-1) ** k * max(0, r - sum(U))
                for k in range(5)
                for U in combinations(band, k)
            )
            assert actual == expected
    L, M = d / (c * (c + d)), 1 / (c + d)
    assert (
        L + M == 1 / c and L * c * c + M * d * d == d and L * c / d + M == 2 / (c + d)
    )
    # Between c and d the difference is exactly M*(r-c)*(r-d).
    assert M * (c + d) == 1 and L * c * c == M * c * d
    observed = L * (1 + c / d) ** 2 + 4 * M
    assert observed == F(136, 3) and 1 / c + 3 / d == 40
    return observed


def verify_profiles():
    """Check against the defining signed subset sum, independently of the enclosures."""
    from random import Random

    rng = Random(20261126)
    g = GRID

    def root(xs, r):
        return sum(
            (-1) ** k * max(0, r - sum(U))
            for k in range(len(xs) + 1)
            for U in combinations(xs, k)
        )

    seen = 0
    boxes, exact_values = [], []
    edges = high_edges(24)
    while seen < 1600:
        xs = sorted(rng.randrange(1, g) for _ in range(4))
        a = rng.randrange(17 * g // 21, 51 * g // 59 + 1)
        if root(xs, a) <= 0 or root(xs, g) >= 0:
            continue
        lo = np.array([max(1, x - rng.randrange(1, g // 64)) for x in xs])
        hi = np.array([min(g, x + rng.randrange(1, g // 64)) for x in xs])
        tags = rng.sample(range(4), rng.randrange(3))
        level = (3 * g + a) // 2
        limit = (level - sum(hi[i] for i in tags)) // 2
        if limit < 3:
            continue
        c = rng.randrange(1, limit)
        d = rng.randrange(c + 1, limit + 1)
        A, B = rng.choice([(1, -1), (3, -2), (2, 1), (0, 1)])
        rem = [i for i in range(4) if i not in tags]
        marks = rng.randint(1, 6)
        w = coefficients(
            lo[None, rem], hi[None, rem], np.array([marks]), c, d, A, B, not tags
        )[0]
        factors = [xs[i] for i in rem]
        val = F(A * root(factors, c), c) + F(B * root(factors, d), d)
        assert 0 <= w <= 1024 * marks * val * val
        if xs[0] >= edges[0]:
            boxes.append(np.searchsorted(edges, xs, side="right") - 1)
            exact_values.append(F(-root(xs, a) * root(xs, g), a * g))
        seen += 1
    bound = refined_weights(boxes, edges, g - 17 * g // 21, 6)
    assert all(10**11 * exact <= upper for exact, upper in zip(exact_values, bound))
    # Test the multiplicity bound also when the gate meets a prime exactly.
    for z in range(2, 20):
        for u, v, w in combinations(range(1, 24), 3):
            excess = u + v + w
            assert max(0, 3 - excess // z) <= sum(t <= z for t in (u, v, w))
    return seen


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=44)
    p.add_argument("--rounds", type=int, default=2)
    p.add_argument("--tags", type=int, default=2, choices=(0, 1, 2))
    p.add_argument("--block", type=int, choices=range(105, 145, 5))
    p.add_argument(
        "--tail",
        type=int,
        choices=(2, 3),
        default=0,
        help="require at least this many primes in the remainder",
    )
    p.add_argument(
        "--check",
        action="store_true",
        help="test interval enclosures against exact subset sums",
    )
    args = p.parse_args()
    if args.check:
        print("independent profile checks", verify_profiles())
        print("marked-prime joint square", marked_prime_example(), "versus 40")
    elif args.block:
        boxes, _, _ = physical_bins(count=1, panels=16)
        hi = max(hi for lo, hi in boxes if 5 * (lo // 5) == args.block)
        vals, ext = run_block(args.block, hi, args.n, args.rounds, args.tags, True)
        print(
            "block",
            args.block,
            hi,
            "external rows",
            ext,
            "upper in billionths",
            [ceil_ratio(x.numerator * 10**9, x.denominator) for x in vals],
        )
    else:
        audit(args.n, args.rounds, args.tags, min_factors=args.tail)
