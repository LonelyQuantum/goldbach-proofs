# The many-factor tail of the mixed Selberg weight at a fixed center

Fix $\rho=1/100$. We use the positive arithmetic sum and the two block-dependent Selberg roots in [CompositePartnerWeight.md](CompositePartnerWeight.md). In particular $N=2s$, $L=\log s$, $h\asymp s^{2/3}$, $\eta=(\log L)^{-3}$, $z=s^\eta$. The records have $b=rt\in[s-\lfloor s^{2/3}\rfloor,s-2\lfloor s^{21/40}\rfloor)$, $s^{.34}<r\le s^{.35}$ prime, and a product $d$ of three distinct primes in $(s^{1/16},s^{3/40}]$ dividing $a=N-rt$. The small wheels, coprimalities, squarefree reflection, orientations and log weights are as in the linked note. Brackets divide by the genuine marked-prime-pair mass $A_2$. On dyadic blocks $(R,2R],(D,2D]$, put $K_*=s/((2R)(2D)^2)$, $B_-^2=K_*s^{-3\rho}$, $B_+^2=K_*s^\rho$. Write $F_\pm=F_{B_\pm}(t)$ and $k=\#\{z<p\le B_+:p\mid t\}$.

For every fixed $a_0>0$, the following bound is obtained in the fixed-center dispersion framework:
$$
 \limsup_{s\to\infty}\langle 1_{k\ge J}|F_- F_+|\rangle_s
       \ll_{a_0,\rho} J^{-a_0} \qquad (J\ \text{sufficiently large}).       \tag{1}
$$
In particular the negative mass on $k\ge J(s)$ is $o(A_2)$ before normalization for every $J(s)\to\infty$. All limits run through the individual integer centers. For the original radii we also give an explicit upper limit of $0.000066$ at $J=4096$ in (7). The desired numerical estimate concerns the entire negative mass.

## Marking many divisors in the short square

Use $k_*=\#\{z<p\le s^{3/20}:p\mid t\}$. It dominates $k$, since $B_+\le s^{.1475+O(1/L)}$. Also $k_*\le1/\eta$, since $t<s$. Below, admissible implied constants may depend on a fixed integer $m$ and on $\rho$. An error denoted $O_A(L^{-A})$ can be made smaller than any fixed inverse power. We use the signed transfer and normalization from the [mixed-weight calculation](CompositePartnerWeight.md#total-and-composite-square-weights) and [the dispersion estimate (2)](PairTripleDispersion.md#a-distribution-estimate-with-an-unrestricted-integer-factor).

For $\eta\le v\le\rho/2$,
$$
 \langle F_-^2\,1_{\exists\,z<p\le s^v:\,p\mid t}\rangle_s
       \ll_\rho v+O_A(L^{-A}).                                           \tag{2}
$$
The cost of the tag lies within the $3\rho$ short-square slack. In the independent divisibility mean, relative to the unrestricted square $1/G(B_-)$, one marked $p$ has mass
$(G^{(p)}(B_-)-G^{(p)}(B_-/p))/(pG(B_-))$, where the superscript deletes multiples of $p$. This is $\ll (\log p)/(pL)$. Indeed both endpoints are fixed positive powers of $s$, the constant term in the harmonic-prefix expansion cancels, and the deleted shell is bounded by the full positive shell. Here $G(X)=W_z(\log X+c_z)+O_A(L^{-A})$ at such endpoints, with $W_z=\prod_{p\le z}(1-1/p)\asymp1/(\eta L)$; see the [harmonic convolution](FourthDivisorSieve.md#four-distinct-divisors-at-one-center). Summing uses $\sum_{p\le X}(\log p)/p\ll \log X$.

Uniformly for $K_0(m,\rho)\le K\le1/\eta$,
$$
 \langle 1_{k_*\ge K}F_-^2\rangle_s
    \ll_{m,\rho} K^{-m}(1+\log K)^m+O_{m,A,\rho}(L^{-A}).                \tag{3}
$$
If there is a relevant prime of exponent at most $K^{-m}$, use (2), with empty range when $K^{-m}<\eta$. Otherwise at least $K/2$ of the primes counted on this event have exponent at most $2/K$, by $\log t<L$. Mark $m$ distinct such primes and divide the resulting positive sum by $\binom{\lfloor K/2\rfloor}{m}$. Their product $P\le s^{2m/K}$ fits within $B_-^2P\le K_*s^{-2\rho}$ if $K_0\ge2m/\rho$. In the marked square the coefficients $\sum_{\ell\mid P,\ j\ell\le B_-}\mu(\ell)$ have magnitude at most $2^m$. Orthogonality bounds the tagged model mean by $4^m/(P G(B_-))$. The reciprocal prime sum on $(s^{\max(\eta,K^{-m})},s^{2/K}]$ is $O_m(1+\log K)$ by partial summation. The transfer treats the entire tag sum in each block, with at most a fixed divisor power of representations per resulting modulus. All tags are smaller than the primes of $d$ after increasing $K_0$.

## A maximal estimate for the long root on a fixed grid

Write $H_B=G(B)F_B$, with the orthogonal terms $\mu(j)h_j(t)/\varphi(j)$ of the previous note. Let $G_0=G(s^{.09})\asymp 1/\eta$. For any fixed list of $n\ll L^2$ endpoints $s^{.09}\le b_1<\cdots<b_n\le s^{.15}$, fixed for the given $s$ independently of the record,
$$
  \left\langle \max_i |H_{b_i}/G_0|^2\right\rangle_s
                     \ll (1+\log(2n))^2.                                \tag{4}
$$
An integer $a<2s$ has at most 16 distinct band divisors that are prime, for large $s$. The sum of the oriented triple weights at $a$, omitting $\log r$, is $O(L)$. Drop the triples at this cost, keeping both small wheels. Pad the disjoint blocks of indices $j$ ending at the $b_i$ to a power of two. The first block begins at one. Every prefix is a union of at most one node at each depth of the binary tree. Cauchy–Schwarz bounds its square by the number of depths times the sum of squared node increments over the tree. At a given depth their independent-model means sum to $G(b_n)$ because the blocks partition the support and the terms are orthogonal.

For the arithmetic sum without the triples, each squared increment expands into $e\mid t,\ e\le s^{.30}$ with coefficients $s^{o(1)}$. Indeed the coefficient of $m\mid t$ in an individual unnormalized increment is bounded by $(m/\varphi(m))G(s^{.15})$ before squaring. With the two truncated wheels the CRT count of each available residue class has rounding error $O(1)$; there are at most $s^{.35+.30+o(1)}=o(h L^{-A})$ tuples after grouping by $r,e$. The small wheel moduli have size $s^{o(1)}$. One may upper-bound both wheels by their nonnegative even Bonferroni sums in each nonnegative square. Their zero mode gives $W_z\delta_z(N)+O_A(L^{-A})$, since the $j$-primes are all above $z$; retain $r\nmid N$ and sieve $a$ only at primes not dividing $N$. The number of tree nodes is $O(L^2)$. The normalization uses $A_2\asymp h\delta_z L$, $\sum_r(\log r)/r\ll L$. Thus the cost at one depth, divided by $G_0^2$, is $O(LW_zG(b_n)/G_0^2)=O(1)$. This is the binary-tree proof of the [Rademacher–Menshov maximal inequality](https://arxiv.org/abs/1106.0871) applied to transferred squared increments. The $O(L)$ triple cost alone would be too large without the roughness on both sides.

## Recovering the moving cutoff

Localize to a shell $K\le k_*<2K$ and $y\le x_{\min}<2y$, where $x_{\min}$ is the least counted prime exponent and $y=2^i\eta$. Nonempty shells have $y\le2/K$. Put $v=\max(\eta,y/2)$. On the shell there is no divisor $p\mid t$ with $z<p\le s^v$. Use $K_0$ large enough that $2y\le\rho/2$. Choose $\Delta=2^{-10K}y^4$.

If $\Delta<L^{-1}$, use the list of all possible dyadic $B_+$ values in (4), at most $O(L^2)$. Otherwise round $\log B_+/L$ down to a regular grid of mesh $\Delta$ starting at $.09$, and call the corresponding radius $b$. Its list has $O(1+\Delta^{-1})$ elements. In both cases $\log(2n)\ll 1+K+|\log y|$. In the rounded case, on the full sample with the no-divisor restriction just described,
$$
 \left\langle 1_{\rm no\ divisor}\,|H_{B_+}-H_b|/G_0\right\rangle_s
      \ll (\Delta+L^{-1})/y^2+O_A(L^{-A}).                              \tag{5}
$$
Here the endpoints depend on $R,D$. To prove (5), sum absolute terms with $b<j\le B_+$. For $p\mid j,\ p\le s^v$, $|h_p|=1$ on the restricted set. For the remaining $p\mid j$ use $|h_p|=1+(p-2)1_{p\mid t}$. On the restricted set the auxiliary square $F_{s^v}^2$ equals one. Multiplying the positive expanded product by this square therefore gives a global majorant. The auxiliary square uses only primes in $(z,s^v]$, disjoint from the positive expansion primes. The model square mean is $1/G(s^v)\ll \eta/y$. For the last inequality, the trivial bound $G\ge1$ suffices for $v=O(\eta)$. Otherwise restrict the Euler product to primes $z<p\le s^{cv}$, with $c>0$ a sufficiently small absolute constant. Under its normalized subset weights the mean of the logarithm of the product is $\sum(\log p)/p\le vL/2$. At least half its mass is below $s^v$, and Mertens gives total mass $\gg v/\eta$.

In each $R,D$ block the sieve level in (5) is at most $B_+s^{2v}$. Since $\log K_*/L\ge .20+O(1/L)$, $2v\le .01$ and $\log B_+/L=(\log K_*/L+\rho)/2$, this has fixed power slack. The $j$-sum is on the divisor side of the dispersion bound. After its positive expansion, the coefficient of $e\mid t$ is at most $(e/\varphi(e))G(s^{.15})$, by writing $j=e j'$. The auxiliary square adds a divisor convolution of size $s^{o(1)}$. Thus the aggregate dispersion error is $O_A(L^{-A})$, uniformly over these blocks and cutoffs. The small-wheel truncations are justified as in the signed transfer: the absolute expanded sum before the auxiliary square is bounded by $G(s^{.15})\sum_{e\mid t}e/\varphi(e)$, so fixed divisor moments suffice. In the zero mode factors $p\mid d$ force $1_{p\mid t}=0$, which only reduces the positive majorant. Such primes do not occur in the auxiliary square.

For fixed $R,j$, $b<j\le B_+$ confines $\log d/L$ to an interval of length $O(\Delta+L^{-1})$, since $B_+$ is proportional to $1/D$ for fixed $R$ and $D<d\le2D$. Its oriented reciprocal $d$-sum with logarithmic weight is $O(L(\Delta+L^{-1}))$: fix two band primes and split the interval for the third into $O(1+L\Delta)$ ordinary dyadic intervals. Each has reciprocal prime sum $O(1/L)$ by Chebyshev, the other two reciprocal sums are bounded, and the orientation costs $O(L)$. Summing $j$ now costs at most
$$
 \sum_{j\le s^{.15}}^*\frac{1}{\varphi(j)}
     \prod_{\substack{p\mid j\\p>s^v}}\big(1+(p-2)/p\big)
 \ll \frac{y}{\eta}\frac1{y^2}.
$$
This follows by extending the positive Euler products up to $s^v$ and from there to $s^{.15}$, respectively. The base two-wheel normalization and unrestricted $r,d$ log weights give $O(LW_z)=O(1/\eta)$. Multiplying the interval width, the $j$-cost, $1/G_0\ll\eta$, and the auxiliary gain $\ll\eta/y$ proves (5).

For any $B\le s^{.15}$, $|H_B|\le 2^{k_*}G(s^{.15})$. Expand first over subsets of the primes dividing $t$ to get this deterministic bound. Consequently on $k_*<2K$ the squared normalized rounding error is at most $O(2^{2K})$ times its absolute value. In the rounded case $1/L\le\Delta$, so (5) gives $O(2^{-8K}y^2)+O_A(L^{-A})$, increasing the input log saving since $2^{2K}\le L^{1/5}$. The exact-list case has zero rounding error. Using $G(B_+)\ge G_0$ in (4) gives
$$
 \langle 1_{\rm shell} F_+^2\rangle_s \ll (1+K+|\log y|)^2.           \tag{6}
$$

## Summation and the remaining constant

Combine (2), (3) and (6) by Cauchy–Schwarz. Each shell contributes at most
$$
 O_{m,\rho}\!\left((1+K+|\log y|)
       \min\{\sqrt y,\ K^{-m/2}(1+\log K)^{m/2}\}\right)+O_{m,A,\rho}(L^{-A}).
$$
Above $y=K^{-m}$ there are $O_m(1+\log K)$ dyadic shells. Below this threshold both $\sqrt y$ and $|\log y|\sqrt y$ are geometrically summable, giving a bound $O_m((1+K+\log K)K^{-m/2})$ for this lower range. Sum $K=2^i J$ up to $1/\eta$, using $m>2a_0+8$. The errors are uniform and the total number of bins is at most a power of $\log L$. This proves (1) with $k_*$, hence with $k$.

Let $b_J=\limsup_s\langle 1_{k<J}(F_-F_+)_-\rangle_s$, where $x_-=\max(0,-x)$. Then $b_J$ increases to $\limsup_s P_s^-$. The previous fixed-multiplicity estimate takes $\rho$ to zero after fixing $J$; it supplies no numerical constant for $b_J$ at $\rho=.01$. On $k\le2$ the negative mass is $o(1)$. For $k=3$ it is localized to the product strip $B_-^2\le p_1p_2p_3\le B_+^2$ up to negligible mass. A compactly supported four-factor example shows why pointwise per-record truncation at .034 would fail even for the limiting profiles. Take $\log K_*/L\to .24$, permitted, for instance, by $\log r/L\to .345$ and three distinct band exponents tending to numbers summing to $.2075$. The limiting radii are $w_-=.105,\ w_+=.125$. Use four distinct partner exponents $(.042,.043,.0435,.044)$. All pairs fit below $w_-$ and all triples exceed $w_+$. Hence the four-factor profile is $f_w=3-2(\sum x_i)/w$ at both radii. Its values are $-2/7,6/25$, with negative product of magnitude $12/175>0.034$. The remaining exponent of $t$ can lie above $w_+$. This open set of profiles has unknown arithmetic mass. The values are per record and cannot be compared directly with the total after dividing by $A_2$.

## An explicit cutoff at 4096 factors

At the same $\rho=.01$ the estimates give
$$
 \limsup_s\langle 1_{k\ge4096}|F_-F_+|\rangle_s <0.000066.             \tag{7}
$$
We use (1) first to discard $k_*$ escaping to infinity. For each fixed $K=2^b$, $b\ge12$, it is enough to sum fixed bands $y=2^{-j}\le x_{\min}<2y$. Indeed (2) and (6), on the original dyadic mesh starting at $\eta$, bound the part with $x_{\min}\le t_0$ by $O_K(\sqrt{t_0}(1+|\log t_0|))+o_K(1)$. Thus the fixed bands exhaust the shell after taking upper limits. Both exhaustion steps are needed before one uses profile errors depending on $K$.

Write $q=(\beta-\alpha)\log(6/5)/\log(66/65)<.12$. The unrestricted short-square main mass is at most $q/.085<1.42$ in the limit. In (2) the upper limit for a fixed exponent cutoff $v$ is at most $qv/.085^2<17v$: use the upper harmonic shell $W_z\log p+O_A(L^{-A})$ before summing tags, $\sum_{p\le s^v}(\log p)/p\sim vL$, and $G(B_-)\ge(.085-o(1))W_z L$. In particular the fixed $(K,y)$ shell has limiting short-root norm at most $6\sqrt y$. Here and below a norm on a shell is the square root of the restricted bracket of the square.

For a second bound split at $K^{-8}$, and mark 48 distinct factors with exponents between $K^{-8}$ and $2/K$. On the complement of the tiny-factor event there are at least $K/2$ choices of individual primes. The level cost is at most $s^{96/K}$, and $96/4096<.03$, so there is fixed power slack. The limiting reciprocal prime sum in this fixed band is $\log(2K^7)\le8\log K$. Use the unordered tag sum and $48!\binom{K/2}{48}\ge(K/3)^{48}$. The upper limit of the short-square mass is therefore at most
$$
 17K^{-8}+1.42(96\log K/K)^{48}\ \le\ 18.42 K^{-8}.
$$
Here $96\log K\le K^{5/6}$ from $K=4096$ onwards by monotonicity of $K^{5/6}/\log K$. The resulting norm is bounded by $5K^{-4}$.

For the long root at fixed $K,y$ use exponent mesh $2^{-2K}y$ starting at $.09$ in (4). The depth count is at most $2K+j+3$. In the proof of (4) the cost per depth after division by $G_0^2$ has upper limit at most
$$
 \frac{(16\cdot15\cdot14)(.075)(\beta-\alpha)}{\log(66/65)(3/40-1/16)\log(6/5)}
            \frac{.15}{.09^2} < 1500^2 .
$$
The factor counts all oriented triples. For each fixed $K$, the actual roots at both the moving and rounded endpoint converge uniformly on the shell to their finite profiles with error $o_K(1)$, by the harmonic-prefix approximation in the previous note. Use the same set of at most $2K$ primes up to $s^{.15}$ for both profiles. Each summand $(1-x/w)_+$ is $1/.09$-Lipschitz in $w\ge.09$. Thus the normalized root changes by at most $12y+o_K(1)$ on rounding. The limiting mass of the shell is at most $2q/y$: upper-bound it by the square of radius $s^{y/2}$, equal to one there, and transfer at this fixed radius. The square-root norm error is at most $6\sqrt y$ in the limit. By the triangle inequality the limiting long-root norm is at most $2000(2K+j+4)$.

Cauchy–Schwarz now gives an upper bound per shell of $2000(2K+j+4)\min(6\,2^{-j/2},5K^{-4})$. For $j\le8b$ the sum is at most $270000bK^{-3}$, using $2K+8b+4\le3K$ and $8b+1\le9b$. For $j=8b+n$, $n\ge1$, use $\sum 2^{-n/2}<3$, $\sum n2^{-n/2}<9$. This part costs at most $120000K^{-3}$. Summing the larger allowance $300000(b+1)8^{-b}$ over $b\ge12$ gives $300000\,8^{-12}(13\cdot8/7+8/49)<0.000066$. Qualitative tightness above permits passage from finite sums to the full arithmetic tail. This proves (7), uniformly in the individual centers in the upper-limit sense.

## A numerical debit for four factors in a band

Here is an explicit partial bound at the original moving radii. Let $E(l,u)$ mean $k=4$ and all four relevant exponents belong to $[l,u]$. For $0<c<l<u<.085$ and $4u+2c<.20$,
$$
 \limsup_s \langle 1_{E(l,u)}(F_-F_+)_-\rangle_s
 \le \frac{9(.02)^2}{4(.085)(.105)}
    \frac{(\beta-\alpha)\log(6/5)}{c\log(66/65)}
    \frac{\log^4(u/l)}{4!}.                                           \tag{8}
$$
In particular $E(.030,.045)$ costs less than $0.001507 A_2$ asymptotically, using $c=.009$. Its subset $E(.042,.044)$, containing the four-factor profile displayed above, costs less than $0.0000002351 A_2$ using $c=.010$. The bounds are nested.

To see the uniform bound for one record, set $g(w)=w f_w(S)$ in the limiting profile of the previous note. Pair the subsets differing by the least exponent $x$. At every point of differentiability the derivative is an alternating sum over subsets of the remaining three exponents with sum in $(w-x,w)$, with endpoints immaterial. This family is an antichain because adding an exponent increases the sum by at least $x$. Its size is at most three: count incidences with the six maximal chains of subsets of three elements, each subset belonging to at least two chains. Thus $g$ is 3-Lipschitz. More generally the bound is the central binomial coefficient of order $k-1$, by the same chain count. Opposite signs give $4(g_-g_+)_-\le(g_+-g_-)^2$. Here $w_+-w_-=.02$ exactly and the limiting lower bounds for $w_-,w_+$ are $.085,.105$. The previous uniform fixed-$k$ approximation shows that the limiting per-record bound for $E$ is the first factor in (8).

To bound the actual normalized mass of $E$, sum over four unordered distinct tags in the band dividing $t$ and multiply by $F_{s^c}(t)^2$. On $E$ there is exactly one such quartet and this auxiliary square is one since all primes up to $s^c$ above the small wheel are absent. In the model the quartet costs its reciprocal product independently of the auxiliary square. In the arithmetic transfer the level is at most $s^{4u+2c}$, with fixed power slack even in the worst triple block. All tag primes are below the reflected prime band since the level condition implies $u<.05$. The prime quartet reciprocal sum is at most $(\log(u/l)+o(1))^4/4!$. The unrestricted triple sum with this fixed auxiliary radius, after division by $A_2$, tends to $(\beta-\alpha)\log(6/5)/(c\log(66/65))$: use $1/G(s^c)\sim1/(W_z cL)$ in the same triple zero mode as the previous mixed moment. This bounded mass also absorbs the uniform profile error. This proves (8).

Together (7) and (8) leave a sufficient budget of $0.032427 A_2$ for the negative mass on $3\le k\le4095$ outside $E(.030,.045)$. Alternatively one can bound $P_s^--P_s^+$ in the signed identity. The known sufficient target stays $0.945494+0.034=0.979494<0.980$. Equation (1) alone does not lower the established numerical upper bound $M_s<0.98458$. The [finite checker](CheckMixedMultiplicityTail.py) exercises the conditional square, gate, maximal estimate and four-factor sign calculation.
