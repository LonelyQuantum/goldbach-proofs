"""Outward bounds for the two four-factor sign-change regions."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
from itertools import combinations, combinations_with_replacement
from math import factorial, prod

import numpy as np
from numba import njit

from CheckCompositePartnerWeight import log_bounds
from CheckThreeFactorStrip import log_sandwich

GRID = 1 << 21
CUTOFF = GRID // (1 << 15)


def ceil_ratio(p, q):
    return -(-p // q)


def mesh(step, pieces):
    # Small coordinates need relative accuracy as well as absolute accuracy.
    fine = [CUTOFF]
    while fine[-1] < GRID:
        end = fine[-1]
        fine.append(min(GRID, end + min(max(1, end // pieces), GRID // step)))
    return np.array(fine, dtype=np.int64)


@njit
def low_sum(edges, log_width, amin, amax, band_lower, band_upper, separation=0):
    n = len(edges) - 1
    g = GRID
    # Bands (2^(-j-1), 2^(-j)] up to one. Include both bins at an edge.
    band_lo = np.zeros(n, dtype=np.int64)
    band_hi = np.zeros(n, dtype=np.int64)
    for index in range(n):
        for power in range(1, 15):
            boundary = CUTOFF << power
            band_lo[index] += edges[index] > boundary
            band_hi[index] += edges[index + 1] >= boundary
    out = np.int64(0)
    for i in range(n):
        x, X = edges[i], edges[i + 1]
        if 2 * x >= 3 * g // 4:
            break  # x <= S/4 < 3/8
        for j in range(i, n):
            y, Y = edges[j], edges[j + 1]
            if 2 * (x + y) >= 3 * g // 2:
                break
            first = log_width[i] * log_width[j] / (2 if j == i else 1)
            for k in range(j, n):
                v, V = edges[k], edges[k + 1]
                if 2 * v >= g or 2 * (x + y + 2 * v) >= 3 * g:
                    break
                three = first * log_width[k] / (3 if i == k else (2 if j == k else 1))
                lo3, hi3 = x + y + v, X + Y + V
                # S>1 and S-R>amin. For fixed first three, S-R is increasing in z.
                min_z = max(
                    g - hi3, min(amin - V, (2 * amin - hi3) // 2, (3 * amin) // 2 - hi3)
                )
                start = max(k, np.searchsorted(edges, min_z) - 1)
                for l in range(start, n):
                    z, Z = edges[l], edges[l + 1]
                    if separation == 1 and 2 * Z < 5 * y:
                        continue
                    if separation == 2 and (Y < 2 * x or V < 2 * y or Z < 2 * v):
                        continue
                    if separation == 3:
                        second = max(band_lo[j], band_lo[i] + 1)
                        third = max(band_lo[k], second + 1)
                        fourth = max(band_lo[l], third + 1)
                        if (
                            second > band_hi[j]
                            or third > band_hi[k]
                            or fourth > band_hi[l]
                        ):
                            continue
                    slo, shi = lo3 + z, hi3 + Z
                    if v + z >= g or 2 * slo >= 3 * g:
                        break
                    if x >= band_lower and Z <= band_upper:
                        continue
                    if max(6 * (V + Z), 3 * (hi3 + 2 * Z), 4 * shi) <= 6 * amin:
                        continue
                    gp = min(shi - g, X, g - v - z, 2 * g - slo - z, 3 * g - 2 * slo)
                    if gp <= 0:
                        continue
                    left = max(0, min(X, amax - v, X + Y - amin + V))
                    right = max(0, min(X, amax - z, X + Y - amin + Z))
                    back = max(0, min(x, amin - V - Z, x + y - amax + v + z))
                    neg = max(0, left + right - back)
                    if neg == 0:
                        continue
                    # 2(T-S) = 3+a-2S for T=(3+a)/2.
                    twice_level = 3 * g + amin - 2 * min(shi, 3 * g // 2)
                    copies = 4 if i == l else (3 if j == l else (2 if k == l else 1))
                    # gp*neg/(g*amin) times 4*g/(3*g+amin-2*S)
                    term = (
                        (4.0 * gp * neg)
                        / (amin * twice_level)
                        * three
                        * log_width[l]
                        / copies
                    )
                    add = np.int64(np.ceil(term * (1.0 + 2.0**-40) * 2.0**58))
                    if add < 0 or out > 9223372036854775807 - add:
                        raise OverflowError("positive upper sum")
                    out += add
    return out


def physical_bins(count=14, panels=32):
    from CheckPairTripleDispersion import geometric_nodes

    scale = 2400 * panels * 100000
    geo = geometric_nodes(scale, panels)
    # Joint histogram of lower and upper sums of reflected exponents and tau.
    hist = Counter({(0, 0): 1})
    intervals = [
        [
            (
                scale * 34 // 100 + scale * i // (100 * panels),
                scale * 34 // 100 + scale * (i + 1) // (100 * panels),
            )
            for i in range(panels)
        ],
        [
            (
                2 * (scale // 16 + scale * i // (80 * panels)),
                2 * (scale // 16 + scale * (i + 1) // (80 * panels)),
            )
            for i in range(panels)
        ],
    ]
    log_intervals = [(2 * (geo[i] - 1), 2 * geo[i + 1]) for i in range(panels)]
    for choices in intervals + [log_intervals] * 2:
        nxt = Counter()
        for (lo, hi), mass in hist.items():
            for l, u in choices:
                nxt[lo + l, hi + u] += mass
        hist = nxt
    boxes = Counter()
    for (lo, hi), mass in hist.items():
        blo = max(F(105, 1000), F(101 * scale // 100 - hi, 2 * scale))
        bhi = min(F(1475, 10000), F(101 * scale // 100 - lo, 2 * scale))
        # Coarsen exponent box outwards to increments 1/(1000*count).
        q = 1000 * count
        boxes[(int(blo * q), ceil_ratio(bhi.numerator * q, bhi.denominator))] += mass
    return boxes, q, panels**4


def high_edges(n):
    edges = sorted(
        set(
            [CUTOFF, GRID]
            + [GRID * i // n for i in range(1, n)]
            + [
                GRID // (n * 2**j)
                for j in range(1, 20)
                if GRID // (n * 2**j) > CUTOFF
            ]
        )
    )
    return edges


def log_width_upper(lo, hi):
    t = F(hi - lo, hi + lo)
    return 2 * (
        sum(t ** (2 * k + 1) / (2 * k + 1) for k in range(8))
        + t**17 / (17 * (1 - t * t))
    )


def high_certificate(delta_hi, n=28):
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    from math import ceil

    edges = high_edges(n)
    nb = len(edges) - 1
    g = GRID
    unit = 10**11
    amin = g - delta_hi
    # floor of T in grid units, and exact lower auxiliary radius per tag set.
    level = (3 * g + amin) // 2
    cap_cache = {}
    row_prices = []
    widths = [log_width_upper(l, u) for l, u in zip(edges, edges[1:])]

    def options(tags):
        if tags not in cap_cache:
            e = (level - sum(edges[i + 1] for i in tags)) // 2
            if e < 1:
                cap_cache[tags] = []
            else:
                gates = {e, CUTOFF}
                gates.update(min(e, g * j // 12) for j in range(1, 13))
                gates.update(min(e, g // (2**j)) for j in range(5, 15))
                # Keeping only these fixed gates is sufficient for a valid cover.
                size = (
                    prod(widths[i] for i in tags)
                    / prod(factorial(k) for k in Counter(tags).values())
                    if tags
                    else F(1)
                )
                choices = []
                for c in sorted(gates):
                    if c > e:
                        continue
                    choices.append((c, len(row_prices)))
                    row_prices.append(size * g / c)
                cap_cache[tags] = choices
        return cap_cache[tags]

    rows = []
    cols = []
    coeffs = []
    weights = []
    for i in range(nb):
        x, X = edges[i : i + 2]
        if 4 * x >= 3 * g:
            break
        for j in range(i, nb):
            y, Y = edges[j : j + 2]
            if X + Y <= amin:
                continue
            for k in range(j, nb):
                v, V = edges[k : k + 2]
                if X + Y + V <= 2 * amin:
                    continue
                if x + y + 2 * v >= 3 * g:
                    break
                for l in range(k, nb):
                    z, Z = edges[l : l + 2]
                    lo = (x, y, v, z)
                    hi = (X, Y, V, Z)
                    if sum(lo) >= 3 * g:
                        break
                    pos = min(X, X + Y - amin, X + Y + V - 2 * amin, sum(hi) - 3 * amin)
                    if pos <= 0:
                        continue
                    neg = min(
                        3 * g
                        - sum(lo)
                        - sum(max(0, g - u - w) for u, w in combinations(hi, 2)),
                        sum(min(X, g - u) for u in lo[1:])
                        - x
                        - sum(max(0, g - u - w) for u, w in combinations(hi[1:], 2)),
                    )
                    if neg <= 0:
                        continue
                    w = ceil_ratio(
                        unit * min(4 * pos * neg, 9 * delta_hi**2), 4 * g * amin
                    )
                    col = len(weights)
                    weights.append(w)
                    cfg = (i, j, k, l)
                    for length in (0, 1, 2, 3):
                        for tags, count in Counter(combinations(cfg, length)).items():
                            left = list(cfg)
                            for tag in tags:
                                left.remove(tag)
                            lim = edges[left[0]]
                            for c, row in options(tags):
                                if c <= lim:
                                    coefficient = 1024 * count
                                elif length == 3:
                                    coefficient = 1024 * count * lim**2 // c**2
                                elif length == 2:
                                    other = edges[left[1]]
                                    tent = max(0, min(c, lim, other, lim + other - c))
                                    coefficient = 1024 * count * tent**2 // c**2
                                else:
                                    break
                                if not coefficient:
                                    continue
                                rows.append(row)
                                cols.append(col)
                                coeffs.append(coefficient)
    mat = coo_matrix(
        (coeffs, (rows, cols)), shape=(len(row_prices), len(weights))
    ).tocsc()
    # Optimize in floating point, then certify all box inequalities in integers.
    sol = linprog(
        -np.array(weights) / unit,
        A_ub=mat,
        b_ub=np.array([1024 * float(c) for c in row_prices]),
        bounds=(0, None),
        method="highs-ipm",
    )
    if not sol.success:
        raise ArithmeticError(sol.message)
    dual = [max(0, ceil(-float(x) * unit)) for x in sol.ineqlin.marginals]
    prices = [float(c) for c in row_prices]
    for j, w in enumerate(weights):
        a, b = mat.indptr[j : j + 2]
        ids = mat.indices[a:b]
        mult = mat.data[a:b]
        missing = w - sum(dual[int(row)] * int(q) for row, q in zip(ids, mult))
        if missing > 0:
            h = min(range(len(ids)), key=lambda m: prices[ids[m]] / mult[m])
            dual[ids[h]] += ceil_ratio(missing, int(mult[h]))
    kw = np.array(dual, dtype=np.int64)
    assert max(dual) * 6144 * int(max(np.diff(mat.indptr))) < 2**63 - 1
    assert np.min(mat.T @ kw - np.array(weights, dtype=np.int64)) >= 0
    # Round each row cost outwards before summing to bound denominator growth.
    price_unit = 10**13
    value = sum(
        v * ceil_ratio(c.numerator * price_unit, c.denominator)
        for v, c in zip(dual, row_prices)
        if v
    )
    return F(1024 * value, unit * price_unit), len(weights), len(row_prices)


@njit
def trial_value(idx, n, parts, amin, amax, masses, probabilities):
    value = np.int64(0)
    for i in range(parts):
        for j in range(parts):
            for k in range(parts):
                for l in range(parts):
                    offsets = (i, j, k, l)
                    lo = np.empty(4, np.int64)
                    hi = np.empty(4, np.int64)
                    prob = 1 << 24
                    for t in range(4):
                        v = idx[t] * parts + offsets[t]
                        lo[t] = v * GRID // (n * parts)
                        hi[t] = ceil_num((v + 1) * GRID, n * parts)
                        prob = (prob * probabilities[idx[t], offsets[t]]) // (1 << 24)
                    lo.sort()
                    hi.sort()
                    x, y, v, z = lo
                    X, Y, V, Z = hi
                    sl = x + y + v + z
                    sh = X + Y + V + Z
                    # Ignore all possibly precharged boxes in the lower calculation.
                    if 1475 * X >= 300 * GRID and 105 * z <= 45 * GRID:
                        continue
                    pos = min(
                        sl - GRID, x, GRID - V - Z, 2 * GRID - sh - Z, 3 * GRID - 2 * sh
                    )
                    highneg = 3 * GRID - sh
                    for t in range(4):
                        for u in range(t):
                            highneg -= max(0, GRID - lo[t] - lo[u])
                    if pos <= 0 and highneg <= 0:
                        continue
                    average = 0
                    for m in range(len(amin)):
                        a = amin[m]
                        A = amax[m]
                        w = 0
                        if pos > 0 and sh < 3 * GRID // 2:
                            one = max(0, min(x, a - V, x + y - A + v))
                            two = max(0, min(x, a - Z, x + y - A + z))
                            last = max(0, min(X, A - v - z, X + Y - a + V + Z))
                            w = pos * max(0, one + two - last)
                        if sl > 2 * GRID and highneg > 0:
                            first = min(x, x + y - A, x + y + v - 2 * A, sl - 3 * A)
                            w = max(w, first * highneg)
                        average += masses[m] * ((w * (1 << 19)) // (GRID * A))
                    value += prob * (average // (1 << 19))
    return value


@njit
def ceil_num(p, q):
    return (p + q - 1) // q


def comparison(regenerate=False):
    assert F(1194, 10000) < log_bounds(5)[0] / (100 * log_bounds(65)[1])
    assert log_sandwich() < F(12, 100)
    n, parts = 32, 3
    witness_path = Path(__file__).with_name("FourFactorGateWitness.json")
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix

    u = 10**10
    bs, q, total = physical_bins(count=1, panels=16)
    marg = Counter()
    for (bl, bh), m in bs.items():
        bl = 5 * (bl // 5)
        bh = 5 * ceil_ratio(bh, 5)
        marg[bl, bh] += m
    amin = np.array([GRID - ceil_ratio(20 * GRID, bl) for bl, bh in marg])
    amax = np.array([GRID - (20 * GRID // bh) for bl, bh in marg])
    masses = np.array(
        [
            int(F(1194, 10000) * 1000 / bh * m / total * (1 << 22))
            for (bl, bh), m in marg.items()
        ]
    )
    probabilities = np.zeros((n, parts), dtype=np.int64)
    for i in range(1, n):
        upper = log_width_upper(i, i + 1)
        for h in range(parts):
            probabilities[i, h] = int(F(1 << 24, (i * parts + h + 1)) / upper)
    assert max(sum(probabilities[i]) for i in range(n)) <= 1 << 24
    assert sum(masses) < 2 * (1 << 22)
    support = []
    wts = []
    rows = []
    cols = []
    coeffs = []
    caps = []
    # The model density is uniform in log within each occupied (unordered) cell.
    # To cover every finer tag window, include the full conditional row at the
    # top of each interval of possible gates, with MORE level than any center.
    @lru_cache(None)
    def gates(tags):
        tmax = F(2) - F(1, 2) * F(8, 59)  # delta_min=.02/.1475=8/59
        max_c = min(F(1), (tmax - sum(F(i, n) for i in tags)) / 2)
        if max_c <= 0:
            return []
        size = F(1)
        for i in tags:
            t = F(1, 2 * i + 1)
            size *= 2 * sum(t ** (2 * k + 1) / (2 * k + 1) for k in range(8))
        size /= prod(factorial(v) for v in Counter(tags).values())
        cs = sorted(
            set([F(j, n) for j in range(1, n + 1) if F(j, n) < max_c] + [max_c])
        )
        result = []
        for c in cs:
            cap = size / c
            result.append((c, len(caps)))
            caps.append(cap.numerator * u // cap.denominator)
        return result

    for cfg in combinations_with_replacement(range(1, n), 4):
        i, j, k, l = cfg
        if not (
            sum(cfg) + 4 > n
            and 2 * sum(cfg) < 3 * n
            or 100 * (sum(cfg) + 4) > 242 * n
            and sum(cfg) < 3 * n
            and 100 * (i + j + 2) > 80 * n
        ):
            continue
        val = trial_value(np.array(cfg), n, parts, amin, amax, masses, probabilities)
        weight = int(val) * u // (1 << 46)
        if not weight:
            continue
        col = len(wts)
        wts.append(weight)
        support.append(cfg)
        for h in range(5):
            for tags, count in Counter(combinations(cfg, h)).items():
                rest = list(cfg)
                for p in tags:
                    rest.remove(p)
                top = F(rest[0] + 1, n) if rest else F(1)
                for c, r in gates(tags):
                    if c > top:
                        break
                    rows.append(r)
                    cols.append(col)
                    coeffs.append(count)
    mat = coo_matrix((coeffs, (rows, cols)), shape=(len(caps), len(wts))).tocsc()
    csr = mat.tocsr()
    if regenerate:
        res = linprog(
            -np.array(wts) / u,
            A_ub=mat,
            b_ub=np.array(caps) / u,
            bounds=(0, None),
            method="highs",
        )
        if not res.success:
            raise ArithmeticError(res.message)
        mu = np.maximum(0, np.floor(res.x * u).astype(np.int64))
        assert int(max(mu)) * 6 * len(wts) < 2**63 - 1
        for i, used in enumerate(csr @ mu):
            if used <= caps[i]:
                continue
            a, b = csr.indptr[i : i + 2]
            js = csr.indices[a:b]
            mu[js] = np.array(
                [int(mu[j]) * caps[i] // int(used) for j in js], dtype=np.int64
            )
    else:
        entries = json.loads(witness_path.read_text(encoding="utf-8"))
        points = {tuple(row[:4]): row[4] for row in entries}
        assert len(points) == len(entries) and points.keys() <= set(support)
        mu = np.array([points.get(cell, 0) for cell in support], dtype=np.int64)
    assert int(max(mu)) * 6 * len(wts) < 2**63 - 1 and min(mu) >= 0
    assert np.all(csr @ mu <= np.array(caps))
    if regenerate:
        entries = [[*cell, int(m)] for cell, m in zip(support, mu) if m]
        witness_path.write_text(
            "[\n" + ",\n".join(json.dumps(row) for row in entries) + "\n]\n",
            encoding="utf-8",
        )
    return F(sum(int(m) * h for m, h in zip(mu, wts)), u * u), len(wts), len(caps)


def square_separation():
    rows = json.loads(
        Path(__file__)
        .with_name("FourFactorGateWitness.json")
        .read_text(encoding="utf-8")
    )
    lower = F(0)
    for *bins, mass in rows:
        copies = bins.count(25) * (bins.count(25) - 1) // 2
        if not copies:
            continue
        rem = list(bins)
        rem.remove(25)
        rem.remove(25)
        tent = max(0, min(4, rem[0], rem[1], sum(rem) - 4))
        lower += F(mass * copies * tent * tent, 16 * 10**10)
    upper = 4 * log_width_upper(25, 26) ** 2
    assert F(2 * 26 + 2 * 4, 32) < F(40, 21)  # min T = 2-(4/21)/2
    assert lower > F(6319, 10**6) and upper < F(61531, 10**7)
    return lower


def check_profile():
    tested = 0
    for cfg in combinations_with_replacement(range(1, 10), 4):
        x, y, v, z = cfg
        S = sum(cfg)
        six_R = min(6 * (x + y), 3 * (x + y + v), 2 * S)
        for h in range(6 * S + 1):
            # w=h/6 contains every candidate transition as an exact point.
            G = sum(
                (-1) ** j * max(0, h - 6 * sum(sub))
                for j in range(5)
                for sub in combinations(cfg, j)
            )
            assert (G > 0) == (0 < h < six_R or 6 * S - six_R < h < 6 * S)
            tested += 1
    return tested


def bounds():
    boxes, q, total = physical_bins(count=1, panels=16)
    edges = mesh(320, 32)
    widths = np.diff(edges) / edges[:-1]
    low = F(0)
    high = F(0)

    @lru_cache(None)
    def upper_at(bl):
        return high_certificate(ceil_ratio(20 * GRID, bl), 44)[0]

    for (lo, hi), m in boxes.items():
        amin = GRID - ceil_ratio(GRID * q, 50 * lo)
        amax = GRID - (GRID * q // (50 * hi))
        bl = ceil_ratio(3 * GRID * q, 100 * lo)
        bu = 45 * GRID * q // (1000 * hi)
        scale = F(m * q, lo * total) * log_sandwich()
        low += scale * F(int(low_sum(edges, widths, amin, amax, bl, bu)), 1 << 58)
        high += scale * upper_at(5 * (lo // 5))
    # log((1/4)/2^-15) = 13 log 2 < 9.1.
    h = F(91, 10)
    eps = F(1, 1 << 15)
    small = (
        F(12, 100)
        * 2
        / (F(85, 1000) * F(1, 4))
        * eps**2
        / 2
        * (1 + h + F(1, 2) + (h * h + h + F(1, 2)) / 2)
    )
    assert low <= F(84545, 10**7) and high <= F(239171, 10**7)
    assert small < F(3, 10**7) and low + high + small < F(32372, 10**6)
    return [
        ceil_ratio(v.numerator * 10**7, v.denominator)
        for v in (low, high, small, low + high + small)
    ]


def separated_bounds():
    boxes, q, total = physical_bins(count=1, panels=16)
    edges = mesh(170, 22)
    widths = np.diff(edges) / edges[:-1]
    estimates = [F(3, 10**7)] * 3  # Add the certified tiny-coordinate tail.
    for (lo, hi), mass in boxes.items():
        amin = GRID - ceil_ratio(GRID * q, 50 * lo)
        amax = GRID - GRID * q // (50 * hi)
        lower = ceil_ratio(3 * GRID * q, 100 * lo)
        upper = 45 * GRID * q // (1000 * hi)
        scale = F(mass * q, lo * total) * log_sandwich()
        for mode in (1, 2, 3):
            val = low_sum(edges, widths, amin, amax, lower, upper, mode)
            estimates[mode - 1] += scale * F(int(val), 1 << 58)
    assert estimates[0] < F(3752, 10**6)
    assert estimates[1] < F(874, 10**7)
    assert estimates[2] < F(11475, 10**7)
    return [ceil_ratio(v.numerator * 10**7, v.denominator) for v in estimates]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild-witness", action="store_true")
    parser.add_argument("--witness-only", action="store_true")
    args = parser.parse_args()
    print("sign and endpoint checks", check_profile(), flush=True)
    ref, cells, rows = comparison(args.rebuild_witness)
    print(
        "comparison lower in billionths",
        int(ref * 10**9),
        "boxes",
        cells,
        "constraints",
        rows,
        flush=True,
    )
    assert ref > F(111546, 10**7)
    print("two-tag square lower on stored witness", square_separation(), flush=True)
    if not args.witness_only:
        print(
            "separated upper bounds in ten-millionths", separated_bounds(), flush=True
        )
        print(
            "arithmetic upper bounds in ten-millionths, low/high/tiny/total", bounds()
        )
