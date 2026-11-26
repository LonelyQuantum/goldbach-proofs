# Which differences between neighboring Goldbach pairs detect the prescribed sum?

Write $L=\log Y$, $H=\lfloor Y^{2/3}\rfloor$, $T=\lfloor Y^{21/40}\rfloor$, $I=(2T,H]\cap\mathbb Z$, $h=|I|$ and $W=Y+(I\cup(-I))$. Let $r$ count unordered prime pairs in $W$ summing to $2Y$. We use the [preceding endpoint estimate](ThreeSquareEndpointCover.md) with $5/8<\eta<2/3$, $D=\lfloor Y^\eta\rfloor$, $\lambda=D/(8L)$ and its set $S\subset(D,2D]$ of distinct labels. For every $x=Y+O(H)$ coprime to 30, there are $\lambda+O_A(D/L^A)$ labels making $x+30n$ prime, and separately the same estimate holds with a minus sign. Each label is a sum of three distinct nearly equal prime squares, and both neighboring centers are rich. These inputs apply to the full primes. All conclusions below are paper deductions or explicitly stated finite constructions.

## An exact identity using differences other than the two distinguished values

Use signed offsets. For $n\in S$, $A_n$ is the set of $x$ such that $Y+x,Y+30n-x$ are primes in $W$, and their pair is in the trimmed central window at $Y+15n$. For $m\in S$, $B_m$ is the set of $y$ such that $Y-y,Y+y-30m$ are primes in $W$, and their pair is central at $Y-15m$. Both orientations of each pair are included. For each bin $Q$ of a partition of the **positive** offsets $I$ into consecutive blocks of at most $b$ integers, put
$$
 A_{n,Q}=\{x\in A_n:\{x,30n-x\}\cap Q\ne\varnothing\},\qquad
 B_{m,Q}=\{y\in B_m:\{y,30m-y\}\cap Q\ne\varnothing\}.
$$
The bin condition is invariant under exchanging the two prime endpoints. Define $J_{nmQ}(d)=\#\{x\in A_{n,Q}:x+d\in B_{m,Q}\}$ and $K=30(m-n)$. Exchanging the endpoints on both sides sends $(x,x+d)$ to $(30n-x,30m-x-d)$. Hence $J(d)=J(K-d)$. For $n\ne m$ one obtains the exact nonnegative difference
$$
 |A_{n,Q}|\,|B_{m,Q}|-\sum_{d\notin\{0,K\}}J_{nmQ}(d)=2J_{nmQ}(0).       \tag{1}
$$
Indeed the sum over all differences is the product of the two list sizes. When $n=m$, the missing difference is counted once. We omit these diagonal label pairs below.

There are exactly two values of $d$ giving a complementary pair identically in $x$. Of the four primes $Y+x,\ Y-x+30n,\ Y-x-d,\ Y+x+d-30m$, the first and third sum to $2Y$ at $d=0$, and the second and fourth do so at $d=K$. The other opposite-slope sums equal the two neighboring targets. At any other difference, two equal-slope forms can sum to $2Y$ only at $2x=30m-d$ or $2x=30n-d$. These are at most two offsets, even if some forms repeat. A match at the second distinguished difference is the very same observation read with both prime pairs reversed.

Let $\mathcal D_b$ be the sum of the left side of (1) over all bins and all ordered distinct $n,m\in S$, and $\mathcal B_b$ the corresponding sum of the products of list sizes. Uniformly for $1\le b\le h$,
$$
 (2-o(1))\lambda^2r\ \le\ \mathcal D_b\ \le\ (8+o(1))\lambda^2r.        \tag{2}
$$
To prove the lower bound, assign each genuine positive $v$ its unique bin. When extending its two endpoints independently to the two neighbors, the extra requirement that the translated partners still belong to $W$ excludes $O(1+T)$ labels on each side from the inner cut $|v-30n|\le2T$. The outer cut holds automatically since $v>0$, $30n\le60D=o(H)$ and $v\le H$. The neighbor's own inner cut costs $O(1+T)$ via $|v-15n|$ as in the preceding note. Each direction therefore has $(1+o(1))\lambda$ choices, including for the extreme offsets. Removing $m=n$ costs $O(\lambda)$ per $v$. For the upper bound, a match at 0 gives one of at most $2r$ signed offsets. Each direction has at most $(1+o(1))\lambda$ choices by the unrestricted endpoint estimate, and each chosen ordered label pair can use at most two bins for that signed offset. This proves (2), including exact zero when $r=0$.

## How large are the counts being subtracted?

A bound for the product term that is useful even for very short bins is
$$
 \mathcal B_b\ll_\eta \lambda^2\,\frac{h}{L^2}\,(b+\log L).             \tag{3}
$$
Let $u_Q$ count $x\in Q$ for which $Y+x$ is prime and $Y-x$ is coprime to 30. Define $v_Q$ by reversing the signs. Every pair in a list for $Q$ has at least one anchor in $Q$, and each such anchor supplies at most $(1+o(1))\lambda$ labels by the endpoint estimate. An anchor with a nonunit complement supplies none, since 30 divides every displacement and all the primes here exceed 5. Allowing both orientations gives $\sum_n |A_{n,Q}|\ll\lambda u_Q$ and $\sum_m |B_{m,Q}|\ll\lambda v_Q$. Thus it suffices to bound $\sum_Q u_Qv_Q$.

Two positive offsets in the same bin differ by an integer $\delta$ with $|\delta|<b$. Ignore the class and bin cuts after fixing $\delta$. The two required primes have sum $t=2Y-\delta$, with one endpoint in an interval of length $h$. An odd sum is impossible here. For even $t$ the uniform two-linear-form upper sieve gives $\ll h F(t)/L^2$, where $F(t)=\prod_{\ell\mid t,\ell>2}(1+1/(\ell-2))$ over prime $\ell$. One direct derivation applies a Selberg square with radius $h^{1/20}$ and sieve primes up to $h^{1/160}$. The roots coincide at odd primes dividing $t$. The reciprocal product for distinct roots supplies the two logarithms, and the ratio at each coincident odd prime is $(\ell-1)/(\ell-2)$. The CRT rounding loss is a power smaller than $h$. [Uniform Selberg square and truncation details](CentralPrimePairsNearOneCenter.md#removing-a-central-coefficient-while-preserving-short-interval-counts)

Uniformly for $t\asymp Y$, the factors above $L$ contribute $\exp(O(1/\log L))$, since at most $O(L/\log L)$ such primes divide $t$. Expand the remaining product in squarefree divisors with $g(d)=\prod_{\ell\mid d}1/(\ell-2)$ on odd squarefree $d$ with all prime factors at most $L$. In an interval of fewer than $2b$ integers, each divisor contributes at most $2b/d+1$ multiples. The Euler products give $\sum g(d)/d=O(1)$ and $\sum g(d)\ll\log L$ by Mertens' theorem. This proves (3) without assuming any law for primes inside the individual bins.

Take $b=\lceil\log L\rceil$. If the central pair count has order at least $h/L^2$, its contribution accounts for at least a constant times $1/\log L$ of the product term. If there is just one pair, the guaranteed fraction is $\gg L^2/(h\log L)$. A strict shortfall of the summed ordinary-difference counts below $\mathcal B_b$ would already suffice for any positive count. The estimates above control the size of the product term and the sensitivity of this subtraction. They leave its sign beyond nonnegativity undetermined at a prescribed $Y$. At $b=1$ the test explicitly singles out individual anchors.

## Why accurate estimates for separate differences still allow an isolated failure

Here is a comparison between two equal-size **subsets of the genuine primes in $W$**. For any fixed polynomial-size family (in $Y$) of ordinary-difference tests $J_{nmQ}(d)$, including all of them for the bins above with $d\notin\{0,K\}$, one can choose subsets $E_0,E_1$ having zero and $\lceil r/2\rceil$ original unordered pairs respectively, with
$$
 |J^{E_1}_{nmQ}(d)-J^{E_0}_{nmQ}(d)|\ll 1+\sqrt{r\log Y}               \tag{4}
$$
simultaneously. Here the labels, windows and bins are fixed before constructing the subsets. One can also include the separate list sizes and all ordinary noncentral two-summand counts. The estimate concerns the difference **between the two subsets**. Each deletes just $r$ primes from $W$, and the two-form bound above gives $r\ll h\log L/L^2$. The short-interval PNT gives $\asymp h/L$ original primes in $W$.

For even $r=R>0$, the $R$ disjoint two-element reflection orbits supporting genuine pairs account for all possible edits. Retain every other prime. For $E_0$ independently retain one fair endpoint in each orbit. For $E_1$ retain both endpoints in a uniform sample of exactly $R/2$ orbits and neither in the rest. For odd $r$ first set aside one orbit and one unpaired prime. Such a prime exists for large $Y$ by the preceding two bounds. In $E_0$ keep one endpoint of this orbit and the unpaired prime. In $E_1$ keep the whole orbit and drop that unpaired prime. Apply the even construction to $R=r-1$. The odd correction affects any fixed test below by $O(1)$. The cases $R=0$ need no random choices.

More generally a test can sum products of at most $k$ indicators at unit-slope affine forms in one variable against any predetermined weight of absolute value at most one on finite support, with $k$ fixed. Exclude tests with an identically complementary pair of forms. Equal sites count once. At all but $O(k^2)$ offsets no two distinct queried sites are mates in the same reflection orbit: complementary forms of equal slope fix one offset and the opposite-slope case was excluded. At a remaining offset whose $s$ queried sites lie in distinct edited orbits (ignoring unedited sites), the probabilities for retaining them are $2^{-s}$ and $(R/2)_s/(R)_s$ respectively, with falling factorials. Coupling draws of $s$ indices with and without replacement bounds the difference by $\binom{s}{2}/R$. At most $2kR$ offsets hit any edited orbit since each form is injective. The difference of the two expected test sums is therefore $O_k(1)$.

Changing one fair choice changes at most two sites, each in at most $k$ terms. Expose the uniform half-sample using a random ordering of the $R$ orbits. Two possibilities at any exposure step can be coupled by a transposition in the remaining completion, changing at most four sites. The Doob martingales have $O(R)$ bounded increments of size $O(k)$. Azuma–Hoeffding and a union bound over the predetermined family give (4), with a constant depending on $k$ and the polynomial degree. This also covers repeated forms after collapsing equal sites. All the ordinary differences in (1) meet the affine-form condition. [Bounded differences method](https://doi.org/10.1017/CBO9781107359949.008)

The equal-cardinality constraint has an exact consequence. If $C_E(t)$ counts ordered pairs in $E^2$ of sum $t$, then $\sum_{t\ne2Y}(C_{E_0}(t)-C_{E_1}(t))=2\lceil r/2\rceil$, since the total mass is $|E|^2$. On a full window (4) saves every fixed logarithmic power relative to $h$. In a bin of size $b$ an individual $J$ is at most $2b$, so (4) can be vacuous there. The comparison leaves open the accuracy of small-bin tests and of signed sums of a growing number of errors. A proof using (1) needs an aggregate estimate tied to the true primes, or a direct positive match.

[Exact finite checks of the two differences, localization and subset construction](CheckNeighborPairLags.py)
