# Two sieve radii on the high four-factor range

Fix each even target $N=2s$. Keep the extended arithmetic records, the mass $A_2$, the excluded four-prime box $E$, $a=1-.02/b$, $T=2-.01/b$ and $G$ of the [four-factor calculation](FourFactorScales.md). All four normalized exponents $x_i=\log p_i/\log B_+$ lie in $(0,1]$, in increasing order. Write $S=\sum_i x_i$ and $W=(-G(a)G(1))_+/a$. Brackets divide the actual reflected-triple weights by $A_2$. The high part of the negative mixed product has limiting support $G(a)>0>G(1)$ and hence
$$
 x_1+x_2>a,\qquad x_1+x_2+x_3>2a,\qquad 3a<S<3.
$$
The [previous fixed-center transfer](PairTripleDispersion.md#a-distribution-estimate-with-an-unrestricted-integer-factor) and the uniform fixed-four-factor profile approximate the roots on this sample. The statements below are research deductions in that framework. They concern all sufficiently large individual centers in the upper-limit sense.

Let $e=2^{-15}$. The high contributions in the following table already include the exterior normalization; the rows shown first are for $x_1\ge e$. The old high allowance in these units was $0.0239171$.

| Upper-limit calculation on the whole high part, $x_1\ge e$ | Upper bound after division by $A_2$ |
|---|---:|
| Old arithmetic tests, with the objective bounded on smaller subboxes | $0.0201193$ |
| Same cells, expanded single-radius tests | $0.0201193$ |
| Add internal two-radius tests | $0.0201065$ |
| Also use the forced outer-prime mark where the level permits | $0.0201065$ |

The old low bound $0.0084545$ and the shared tiny-coordinate allowance $0.0000003$ are charged once. This gives a strict upper limit **$0.0285613$** for the entire still-unaccounted $k=4$ part. The outstanding sufficient budget across $4\le k\le4095$ is $0.009140$. The table compares concrete outward certificates. Their successive differences describe improvements in the computed bounds; they do not estimate the actual negative mass. The reduction from $0.032372$ is $0.0038107$, or about $11.77\%$. Of this, $0.0037978$ comes from tightening the old high objective. The two-radius improvement over the recomputed single-radius certificate is approximately $0.0000128$.

| High subfamily, $x_1\ge e$ | Size restriction only | Include one external prime, single square | Include two-radius squares on that marked cofactor |
|---|---:|---:|---:|
| $\Omega(m)\ge2$ | $0.0201030$ | $0.0200829$ | $0.0200804$ |
| $\Omega(m)=3$ | $0.0068504$ | $0.0047566$ | $0.0045641$ |

These two controls use the same refined objective and the original internal tests. The row for three outer primes is contained in the row for at least two. A separate upper bound for the slice $m<B_+^2$ is $0.0081832$ for $x_1\ge e$ using the full high tests. With the tiny allowance each individual subfamily bound increases by less than $0.0000003$. Neither a bound for a subfamily nor the reduction in its certificate may be subtracted from the bound for all records.

The following upward-rounded block prices are in billionths **before** multiplying by their exterior factors. Aggregating the displayed integers with the rational exterior weights in the verifier already gives the two quoted high ceilings.

| Lower block label ($1000b$ rounded down to a multiple of five) | All high records | Forced-prime slice |
|---:|---:|---:|
| 105 | 28673033 | 0 |
| 110 | 26036188 | 0 |
| 115 | 23695719 | 0 |
| 120 | 21639312 | 168 |
| 125 | 19893029 | 16519327 |
| 130 | 18317747 | 18251608 |
| 135 | 16926998 | 16926998 |
| 140 | 15675373 | 15675373 |

## The joint square and which primes it can see

Fix disjoint exponent intervals for marked primes and counts $j_i$. Let $L$ be the sum of their upper exponent endpoints with multiplicity. Write $C_J=\prod_i \ell_i^{j_i}/j_i!$ for their harmonic mass, $\ell_i=\log(u_i/l_i)$. After taking out the exterior factor $q/b$ from the preceding calculation, the price of the nonnegative test $(A F_c+B F_d)^2$ on the integer left after removing those marks is
$$
 C_J Q,\qquad Q=A^2(1/c-1/d)+(A+B)^2/d,\qquad 0<c\le d,\quad L+2d\le T.                 \tag{1}
$$
Here the radii are $B_+^c,B_+^d$. The price follows by expanding the square and using the nested-root cross moment. Leave fixed power slack during transfer, take the center limit, then approach boundary radii. The test is nonnegative when the other factor restrictions are dropped. A fixed finite set of such tests with nonnegative multipliers gives an arithmetic upper bound as soon as it dominates the target on every retained exponent box. [Nested moment and transfer](CompositePartnerWeight.md#a-mixed-product-below-the-old-reference-constant)

On the high support no triple of internal exponents is below $d$, since $S-x_4>3a-1>1$. If at least one internal prime with exponent $u$ was tagged, no pair of untagged exponents $v,w$ can be below the radius in sum. In fact $u+v+w>2a$ and $v+w>a$, whence $u+2(v+w)>3a>T$. Thus only one-coordinate ramps are needed for these marked tests. In the absence of internal marks there can also be pair ramps.

With two internal tags, at least one remaining exponent exceeds $d$, since otherwise $L+2d\ge S>T$ for their actual exponent cost. With three tags, writing $u$ for the remaining exponent gives $L+2u\ge S+u>T$, so $u>d$. In this last case the two roots both equal one, and the least price per unit of squared amplitude in (1) is $1/d$, attained by the long square alone. For a tagged prime $m$ in the forced range, $d\le(T-H)/2<(114/59-83/59)/2<.263$, while $x_2>a/2>.4$. Only the smallest band exponent can affect either root there.

Let $m=t/\prod_{i=1}^4 p_i$ on squarefree records. Its factors exceed $B_+$. In each exterior block put $H=(1-\tau)/b-S$, with $\tau=\log r/\log s$. Then $\log m/\log B_+=H+o(1)$ and $83/59<H<27/7$ in the high limiting range. In particular $1\le\Omega(m)\le3$. Below the exact threshold $m<B_+^2$ it is prime. The finite-to-limiting estimates include a boundary margin tending to zero. Any test in (1) that marks only internal primes has $d<1$. Every divisor involving a prime of $m$ then lies above both radii, so the two profiles on the remaining band factors are identical for all factorizations of $m$ at those exponents.

## Direct use of the remaining integer

One can mark one prime of $m$ in an interval $(B_+^u,B_+^v]$ when $1\le u<v<T$. Its cost is $C_J=\log(v/u)$ before the radius factor in (1). Two such marks always exceed the available level. When a cell forces $u\le H\le v<T<2$, the sole outer prime is $m$ and supplies exactly one mark. Endpoint inclusions are implemented by arbitrarily small outward intervals and then a limit. Arithmetic coefficients still factor separately from the reflected triple. The prime sum contributes the reciprocal-prime mass, with the same small-wheel and negligible collision estimates as the previous transfer.

When $\Omega(m)\ge h$ with $h=2$ or $3$, marking one exterior prime can give several incidences. If $H\le H_+$ on an exponent cell, the number of its exterior primes of exponent at most $v>1$ is at least
$$
 \max\{0,\ h-\lfloor(H_+-h)/(v-1)\rfloor\} .                              \tag{2}
$$
For exactly $j$ exterior factors, each exponent above $v$ consumes more than $v-1$ of the excess above $j$. The resulting lower bound on marks increases with $j$. Cells with $H_+<h$ can be discarded for this subproblem. During transfer use an outward tolerance at equality. On removing any counted prime, the remaining exterior primes are still above both radii, so each marked occurrence has the same internal-root profiles. Formula (2) multiplies a lower bound on that square. It does not multiply the right-hand price. The subfamily with $\Omega(m)\ge2$ includes the three-factor case.

The threshold $H<2$ alone does not give a transferable mark. For example take $b=.14$, $\tau=.345$ and four exponents near $.68$ with sum $2.72$. The required reflected exponent sum $.1925$ is admissible. Both strict high sign conditions hold and $H=1371/700$ lies strictly between $T=27/14$ and $2$. The sole outer prime already costs more than $T$ before adding any positive radius. These are admissible limiting exponents, not an asserted arithmetic realization.

More generally, on $H\ge T$ any exponent-space measure satisfying the internal-mark upper tests admits an extension assigning one outer-prime label of exponent $H$ to every point. This preserves all internal-mark profiles and satisfies the size and factor-count conditions. Every incidence with an outer tag at an allowed positive radius is then zero. Thus upper tests which require such a tag cannot tighten that projection on $H\ge T$ without further information on the prime-labelled part. This is a statement about the relaxed inequalities. The distribution of true prime remainders at a specific center is an additional arithmetic question.

A direct change of the free integer also hits an explicit limit of the existing dispersion estimate $VD^2<s^{1-\epsilon}$. Write $d_0=\log D/\log s$ for the reflected triple exponent. If the free variable is the whole $m$, the coefficient contains $r\prod p_i$, costing $S>T$ in addition to $r$. If the free variable is $r$, the coefficient contains $t$, and $1-\tau+2d_0\ge .65+2(3/16)=1.025$. Both exceed that lemma's level even before detecting primality in the free variable. A treatment of this slice by switching would therefore need a different decomposition or distribution input.

## A joint test genuinely stronger than all single radii on one projection

Take $b=.144,\ \tau=.345,\ H=8/5$ and $S=(1-\tau)/b-H=2123/720$. The reflected exponent sum $(1.01-\tau-2b)/2=.1885$ is interior. Mark the forced outer prime. Choose $c=1/16$, $d=1/8$, so $H+2d<T$. Let the smallest internal exponent $x$ take the two values $c,d$. Place the three others at $(S-x)/3$ and this value plus and minus $.001$. Then $G(a)=x>0$, $G(1)=S-3<0$. All three large internal exponents exceed even the maximum radius $(T-H)/2$. Thus on this projection the root at any permitted exponent $r$ equals $f_r(x)=\min(1,x/r)$.

In units per unit harmonic mass of the exterior tag, assign masses $U=d/[c(c+d)]$ at $x=c$ and $V=1/(c+d)$ at $x=d$. Every individual test satisfies $\int f_r^2\le1/r$. Below $c$ this follows from $U+V=1/c$, above $d$ from $Uc^2+Vd^2=d$. In between, after multiplication by $r^2$, the excess equals $V(r-c)(r-d)\le0$. Yet $\int f_cf_d=2/(c+d)>1/d$, so
$$
 \int (f_c+f_d)^2=136/3>40=1/c+3/d .
$$
This example concerns one conditional projection, with the exterior exponent fixed. It gives no lower bound for actual integer targets, and makes no claim of satisfying the other tag projections. It shows that the mixed entry in (1) can exclude behavior compatible with every single-radius bound on this projection.

## Finite certificates

Run from the diagnostics directory with Python, NumPy, Numba and SciPy:

~~~text
python -B CheckFourFactorTwoRadii.py --check
python -B CheckFourFactorTwoRadii.py
python -B CheckFourFactorTwoRadii.py --tail 2
python -B CheckFourFactorTwoRadii.py --tail 3
~~~

The old mesh has 44 principal panels, smaller cells near zero, and a $2^{21}$ integer endpoint grid. Each coordinate interval is divided into six for the objective bound only. On each resulting subbox the verifier applies the two high-profile formulas from the previous note and the cap $9(1-a)^2/(4a)$. It takes the largest upper bound over the subboxes, retaining the original counting cells. This produces the first control for the comparison of radii.

For a selected dual row, enclose each ramp $A(1-w/c)_++B(1-w/d)_+$ at its interval endpoints and any interior knots $c,d$. Sum with its inclusion-exclusion sign, take the distance of the resulting interval from zero, and round down before squaring. Every coefficient in the covering system is a lower bound, with mark multiplicities included. The harmonic prices are rounded upwards. Floating-point linear programs only propose rows and multipliers. Rounded nonnegative duals are repaired and checked on every cell in integer arithmetic; prices and exterior weights are combined with exact rational arithmetic. The additional directions search zero, one or two internal marks. The group with lower $b$ boundary $.125$ uses at most one additional internal mark and multipliers of absolute value at most three. This smaller cover was replayed separately after the larger candidate LP for this group hit a 45-second solve limit in a diagnostic run. Forcing $m$ to be prime uses intervals with endpoints in sixteenths, and (2) uses endpoints in thirty-seconds. No optimization over all possible choices of tests is claimed. The 1,600 independent profile checks use the defining subset sum, including tagged cofactors, and the projected example uses rational arithmetic. [Verifier](CheckFourFactorTwoRadii.py) · [Underlying high-range cells and coverage checker](CheckFourFactorScales.py)
