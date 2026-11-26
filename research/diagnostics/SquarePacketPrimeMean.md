# A power-width central Goldbach mean at twice prime squares

For an integer $m$ put $H_m=\lfloor(m^2)^\theta\rfloor$, $T_m=\lfloor(m^2)^{21/40}\rfloor$ and
$$
 G_\theta(m)=\sum_{2T_m<v\le H_m}\vartheta(m^2-v)\vartheta(m^2+v),
 \qquad
 s_0=2\prod_{\ell>2,\ \ell\ {\rm prime}}(1-(\ell-1)^{-2}).
$$
Here $\vartheta(n)=\log n$ at primes and zero otherwise. Each pair is counted once. Take $P\to\infty$ through integers, $Y=P^2$, $L=\log Y$, $H=\lfloor Y^\theta\rfloor$, $\Delta=\lfloor H/L^8\rfloor$, and $U=\lfloor H/(100P L^8)\rfloor$. For $P\le x\le2P$ let $\mathcal P_x$ be the primes in $(x,x+U]$ and $K_x=|\mathcal P_x|$.

**Deduction from published estimates.** For fixed $2/3<\theta<1$,
$$
 \frac{1}{\pi(2P)-\pi(P)}
 \sum_{P<p\le 2P}\frac{G_\theta(p)}{H_p}\longrightarrow s_0. \tag{1}
$$
In particular, a positive proportion of these prime indices have $\gg_\theta H_p/L^2$ genuine central representations of $2p^2$. In fact the same normalized mean tends to $s_0$ within $\mathcal P_x$ for all but $O_{\theta,A}(P/L^A)$ integer starts, for any fixed $A$. For $13/16<\theta<1$ it does so at **every** start. The statement about starts concerns an average over the primes inside each interval. The endpoint $\theta=2/3$ for prime indices and an individual prescribed target remain open here. The [previous prime-square estimate](PrimeSquarePairDistribution.md) allowed central windows of size $Y/\log^B Y$. No priority claim is made for (1).

## The signed sum of differences

Put $t_p=2p^2$, $T(x)=\lfloor(x^2)^{21/40}\rfloor$, $H(x)=\lfloor(x^2)^\theta\rfloor$. Use the upper interval
$$
 I_x=(x^2+2T(x)+2\Delta,\ x^2+H(x)]\cap\mathbb Z,\qquad h_x=|I_x|.
$$
For $x<p\le x+U$, $p^2-x^2<\Delta/10$ eventually. Hence $I_x$ is inside every upper window, omitting $O(\Delta)$ sites per center. All lower endpoints lie in $J_x=[x^2-8H,x^2+8H]\cap\mathbb Z$. For even $d>0$ let $s(d)=s_0\prod_{\ell\mid d,\ \ell>2}(\ell-1)/(\ell-2)$ over prime divisors. Write
$$
 Q_{pr}=\sum_{a\in I_x}\vartheta(t_p-a)\vartheta(t_r-a)-h_xs(|t_p-t_r|),
 \qquad A_x=\frac{L}{h_x K_x^2}\sum_{p\ne r\in\mathcal P_x} Q_{pr}.
$$
Pairs of indices in this formula are ordered. In the two ranges of starts stated above we obtain $|A_x|\ll_{\theta,A}L^{-A}$, choosing the exceptional set for that $A$. This evaluates the wider-window version of the signed quantity in [equation (4) of the preceding note](CentralPrimePairDifferences.md#a-signed-test-for-the-square-subsequence-mean).

## The quadratic Fourier sum on prime indices

Use $e(t)=\exp(2\pi i t)$. Fix a sufficiently large saving exponent $B$, to be chosen from the desired $A$. For some $Q=L^{C}$ with $C=C(B,\theta)$, set $D=\lfloor U^2/(10Q)\rfloor$ and let $\mathfrak M$ be the union of arcs of radius $1/(2D)$ around fractions of denominator at most $2Q$ on the circle. Then
$$
 \sup_{\alpha\notin\mathfrak M}
 \left|\sum_{p\in\mathcal P_x} e(2\alpha p^2)\right|\ll U L^{-B}. \tag{2}
$$
For $\theta>2/3$, $U\ge P^{1/3+\eta}$ for some fixed $\eta>0$. Apply Corollary 1.2(ii) of Matomäki–Radziwiłł–Shao–Tao–Teräväinen. A large von Mangoldt sum requires, outside the allowed exceptional starts, $q\le Q$ with $U^2\|2q\alpha\|\le Q$. This already places $\alpha$ in $\mathfrak M$, without using the linear coefficient. For the uniform supremum in (2), apply the corollary to a measurable choice of a near-maximizing minor phase at each start (a countable dense choice suffices). Its small-denominator alternative is then impossible anywhere. If $\theta>13/16$, $U\ge P^{5/8+\eta}$ and the all-interval Corollary 1.3(ii) of Matomäki–Shao–Tao–Teräväinen gives (2) at every start. Proper prime powers cost $O((1+U/\sqrt P)L^2)$ in weight by counting roots of each exponent. Replacing the remaining $\log p$ by $\log x$ costs $O(U^2/P)$. Both errors save a power. The short-interval prime number theorem gives $K_x\sim U/\log x$ on the same type of good set, by the averaged input below at root scale, or pointwise in the all-start range. [Almost-all intervals, Corollary 1.2](https://doi.org/10.1007/s00222-026-01408-6) · [All intervals, Corollary 1.3](https://arxiv.org/pdf/2204.03754v4#page=5)

## How much endpoint energy can lie on these arcs?

Choose $z=L^Z$ after $C$ is fixed, with $Z$ larger than $C$ and than the desired logarithmic error exponents. Let $C_z(n)=1_{(n,\prod_{\ell\le z}\ell)=1}/\prod_{\ell\le z}(1-1/\ell)$ and $F=\vartheta-C_z$. For $q\le2Q$ all prime factors of $q$ are at most $z$. On any interval of $D$ consecutive integers at height comparable to $Y$, the sum of $C_z$ in a unit class mod $q$ is $D/\varphi(q)+O_M(D L^{-M})$ for every fixed $M$. In a nonunit class both weights vanish. To see the unit-class formula, sieve only primes not dividing $q$, use Bonferroni truncations at consecutive orders around $(\log L)^2$, and apply CRT. The sum of rounding errors is $Y^{o(1)}$, and the factorial tail times $1/V(z)$ beats every power of $1/L$, where $V(z)=\prod_{\ell\le z}(1-1/\ell)$. The factors at $\ell\mid q$ supply $q/\varphi(q)$.

For a fraction $b/q$ in the arc list define $B(t)=\sum_{t<n\le t+D}F(n)e(bn/q)$. Uniformly in that list,
$$
 \int_{Y/2}^{5Y}|B(t)|^2\,dt\ll_M YD^2 L^{-M}. \tag{3}
$$
Indeed $D=Y^{2\theta-1+o(1)}$, which exceeds $Y^{1/6+\eta'}$. Koukoulopoulos, Theorem 1.1 with the unconditional density exponent specified immediately after it, gives an $L^1$ bound $O_N(YD L^{-N})$ for the maximal prime progression error at any $q\le 2Q$. Apply it on a bounded dyadic cover with the same $D$ and sum over the classes against $e(bn/q)$. Multiplication by the trivial pointwise bound $O(DL)$ gives (3) with arbitrary logarithmic saving. In the all-start range $2\theta-1>5/8$, the pointwise short-interval Bombieri–Vinogradov theorem (its modulus range contains every polylogarithmic modulus) yields $|B(t)|\ll_M DL^{-M}$ instead. [Koukoulopoulos, Theorem 1.1](https://arxiv.org/pdf/1405.6592v2#page=2) · [Perelli–Pintz–Salerno, equation (2) and theorem on p. 530](https://www.numdam.org/item/ASNSP_1984_4_11_4_529_0.pdf#page=3)

Write $\widehat F_x(\alpha)=\sum_{n\in J_x}F(n)e(\alpha n)$. The box form of Gallagher's inequality gives
$$
 \int_{|\beta|\le1/(2D)}|\widehat F_x(b/q+\beta)|^2\,d\beta
 \ll D^{-2}\int_{\mathbb R}
 \left|\sum_{t<n\le t+D,\ n\in J_x}F(n)e(bn/q)\right|^2 dt .
$$
Indeed convolving the finite mass with a length-$D$ interval and applying Plancherel multiplies its transform by a sinc factor of size at least $2D/\pi$ on this arc. At the two ends of $J_x$ there are $O(D)$ starts $t$ with partially intersecting intervals. Their cost after division by $D^2$ is $O(DL^2)$; $D/H$ saves a power because $\theta<1$. For fully contained intervals, a fixed $t$ occurs for a set of real $x\in[P,2P]$ of measure $O(H/P)$, since $x^2$ has derivative at least $2P$. Integrate first in $x$ and use (3). After summing the $O(Q^2)$ arcs, dividing by $P$, and choosing the exponents in (3) last, the average arc energy is $O_M(HL^{-M})$. Markov gives this conclusion outside $O_A(P/L^A)$ starts at any desired saving. The pointwise version of (3) gives it for all starts in the wider range.

## Returning to the actual prime pairs

Plancherel for discrete convolution bounds
$$
 E_x=\sum_{a\in I_x}\left|\sum_{p\in\mathcal P_x}F(t_p-a)\right|^2
 \ \le\int_0^1|\widehat F_x(\alpha)|^2
                   \left|\sum_{p\in\mathcal P_x}e(2p^2\alpha)\right|^2\,d\alpha
 \ \ll_M h_x K_x^2 L^{-M}. \tag{4}
$$
The restriction to $I_x$ only decreases the sum of squares. On $\mathfrak M$ use the arc energy bound and the trivial prime sum bound $K_x$. Off the arcs use (2) and $\int|\widehat F_x|^2\ll H L^2$. The choice of constants is sequential: first the desired saving in (4), then $B$, then $Q,D,z$, and finally the saving in (3).

The uniform mixed and model-pair estimates from the [preceding note](CentralPrimePairDifferences.md#removing-the-local-main-terms-uniformly) apply on $I_x$ with errors $O_N(h_xL^{-N})$ when $Z$ is sufficiently large for $N$. Here $h_x\asymp Y^\theta$ and $\theta\ge2/3$, within the cited short-interval theorem. For example, the tail of the singular product costs $O((\log L)L/(z\log z))$. Expanding (4) therefore gives $\sum_{p\ne r}Q_{pr}=E_x-\sum_p\sum_{a\in I_x}F(t_p-a)^2+O_N(h_x K_x^2 L^{-N})$. The diagonal costs $O(K_x h_x L^2)$, negligible since $K_x$ grows by a power. This proves the asserted bound on $A_x$ without a bound on each individual spacing.

Pair (4) with the upper vector $\vartheta(a)$ using Cauchy–Schwarz. The mixed estimate gives $\sum_{a\in I_x}\vartheta(a)C_z(t_p-a)=h_xs(t_p)+O_N(h_xL^{-N})$, where $s(t_p)=s_0(1+O(1/P))$. The true mean on $I_x$ is consequently $(s_0+o(1))h_x$. Extending each sum to the full upper window costs $O(\Delta L^2)=o(H_p)$, and $h_x/H_p\to1$ uniformly. The calculations allowed real starts. For $x\in[j,j+1)$ the prime packet is identical to that at $j$; its endpoint windows differ by $O(P)$ sites, with total weighted cost $O(PL^2)=o(H L^{-N})$ per pair for any fixed $N$. Thus the exceptional-set bounds for the stated means and $A_x$ also hold for integer starts.

Finally integrate the packet sums over $P\le x\le2P$. Each interior prime occurs for a length $U$ of starts. The end regions contain $O(U)$ integers, negligible relative to $P/\log P$. The two-form upper sieve gives $G_\theta(p)\ll_\theta H_p s(2p^2)\ll_\theta H_p$ at every prime index. Bad starts cost $O_A(PU/L^A)$ using even the trivial $K_x\le U+1$. Division by $U$ gives (1). Since the individual normalized weights are bounded above, a positive mean gives a positive proportion exceeding $s_0/2$; each pair carries weight at most $O(L^2)$. [Two-form upper sieve used here](CentralPrimePairsNearOneCenter.md#removing-a-central-coefficient-while-preserving-short-interval-counts)

## Two checks at the boundary of the argument

* At the exact width $\theta=2/3$, replacing prime indices by **all integer** indices gives a true prime-pair mean in almost all packets: $U^{-1}\sum_{x<m\le x+U}G_{2/3}(m)/H_m=2+o(1)$. In (2) use ordinary quadratic differencing, which yields $|\sum_m e(2\alpha m^2)|^2\ll U+\sum_{d\le U}\min(U,1/\|4\alpha d\|)$. Dirichlet approximation to $4\alpha$ with order $U^2/L^C$ bounds the latter by $O((U/q+1)(U+q\log(2q)))$ for the approximating denominator $q$: in blocks of length at most $q/2$ the frequencies are $1/(2q)$-separated. Small $q$ puts $\alpha$ on the same type of rational arcs (allow denominators up to $4Q$); otherwise $C$ can be chosen to give (2). Equation (3) still applies since $D=Y^{1/3+o(1)}$. The local model now averages $s(2m^2)$. Its mean is $2+o(1)$ uniformly over these packets: expand $\prod_{\ell\mid m,\ell>2}(1+1/(\ell-2))$ over odd squarefree divisors, round the count of multiples with total error $O((\log P)^{O(1)}/U)$, and use the absolutely convergent Euler product $\prod_{\ell>2}(1+1/(\ell(\ell-2)))=2/s_0$. The prime-index inverse theorem demands $U\ge P^{1/3+\eta}$, whereas the actual length at this endpoint is $\asymp P^{1/3}/L^8$.
* In the prime-index range $\theta>2/3$, (4) also transfers the [four-factor enrichment mean](FourPrimeEnrichment.md) to these packets, with the wider radius $H_m$ and the same factor gates. For clarity, the fixed upper four-factor set on $I_x$ has mass $(c'+o(1))h_x/\log(x^2)$ and equidistribution to all the Bonferroni moduli $Y^{o(1)}$. To deduce this from the [original upper-site estimate](FourPrimeDistribution.md), tile the interval consecutively by lengths $\lfloor v^{2/3}\rfloor$ at left endpoints $v\asymp x^2$. Adding back the trimmed $O(v^{21/40})$ portion in each tile and discarding the final incomplete tile incurs a power saving, still so after multiplication by $Y^{o(1)}$. Moving the two exponent gates from $v^\gamma$ to $(x^2)^\gamma$ costs in the whole interval $O((1+HY^{\gamma-1})(1+H/Y^\gamma))$ per gate, a power saving for $\gamma=67/400,2/5$. Summing the tile distribution errors over moduli first preserves their arbitrary logarithmic saving. For a prime center the mixed model mass on this set is thus $(s_0+o(1))$ times its cardinality. Testing (4) against its indicator incurs $o(h_x/L)$ per prime on average. Restoring each center's own interval and gates changes the log-weighted count by $O(\Delta L)$ plus a power-saving boundary error. In the notation of the previous note this gives $\overline Z\to1$ for the widened windows. The proof of (1) does not require this four-factor distribution input.

[Finite checks of reflection, the averaging kernel and endpoint multiplicity](CheckSquarePacketPrimeMean.py)
