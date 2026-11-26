# Central prime-pair counts on both sides of a prescribed even target

For a center $s>0$ and a fixed $0<\theta<1$ put $H_s=\lfloor s^\theta\rfloor$, $T_s=\lfloor s^{21/40}\rfloor$, and use the one-sided weighted count
$$
 G_\theta(s)=\sum_{2T_s<v\le H_s}\vartheta(s+v)\vartheta(s-v).
$$
Here $\vartheta(n)=\log n$ on positive primes and zero otherwise. Write $\mathfrak S(2s)=2C_2\prod_{\ell\mid s,\,\ell>2}(\ell-1)/(\ell-2)$, with products over prime divisors and $C_2$ the twin-prime constant.

**At a prescribed center.** Fix $5/8<\eta<2/3$ and $A,B,D>0$. For every sufficiently large integer $Y$, let $L=\log Y$, $U=\lfloor Y^{\eta/2}\rfloor$. Apart from $O_{\eta,A,B,D}(U/L^A)$ integers $1\le m\le U$, one has simultaneously for every nonzero integer $|j|\le L^D$, with $s=Y+jm^2$,
$$
 G_{2/3}(s)=H_s\mathfrak S(2s)+O_{\eta,A,B,D}(H_s/L^B).                 \tag{1}
$$
In particular almost every **prime** step index $m$ in $(U/2,U]$ works on both sides and for all these $j$. Each of those targets has $\gg H_s/L^2$ different pairs of genuine primes. The starting even number $2Y$ is arbitrary, including a hypothetical counterexample. The estimate does not treat $j=0$.

**At twice prime squares.** For each fixed $2/3<\theta<1$ and every $A,B>0$, all but $O_{\theta,A,B}(P/(\log P)^A)$ integers $P<m\le2P$ satisfy
$$
 G_\theta(m^2)=H_{m^2}\mathfrak S(2m^2)+O_{\theta,A,B}(H_{m^2}/(\log P)^B). \tag{2}
$$
The exceptional count therefore applies to prime $m$, giving relative density one there. The [preceding deduction](SquarePacketPrimeMean.md) gave a first moment and positive proportion for prime indices. The argument below estimates a second moment over **integer** indices before restricting them. Perelli's polynomial theorem uses the full summand interval. Coppola–Laporta's almost-equal summand estimate counts exceptions over the ambient even integers. We have not established priority for these localized deductions. [Perelli, Theorem 1](https://doi.org/10.4171/RMI/205) · [Coppola–Laporta, Theorem 1](https://www.giovannicoppola.name/files/articoli/8_giovanni_coppola_number_theory_seminar_politecnico_torino_245.pdf)

## Why the second moment needs translated arcs

Use $e(t)=\exp(2\pi i t)$ and $\widehat v(\alpha)=\sum_n v(n)e(n\alpha)$. Freeze the upper interval $I$, of length $h\asymp H$, and a lower interval $J$ of length $O(H)$ containing every reflection $t_m-I$ to be used. Let $u=\vartheta 1_I$ and $f=(\vartheta-C)1_J$, where $C(n)=1_{(n,\prod_{\ell<R}\ell)=1}\prod_{\ell<R}(1-1/\ell)^{-1}$ and $R=\exp((\log X)^{1/10})$ at the relevant scale $X\asymp Y$. Put $g=\widehat u\,\widehat f$ on the unit circle. Thus $E_m=\int g(\alpha)e(-t_m\alpha)\,d\alpha$ is the error in replacing the lower prime weight by $C$. For $t_m=t_0+2jm^2$ and $m$ in an interval of $U$ integers define $K(\delta)=\sum_m e(2jm^2\delta)$. One has exactly
$$
 \sum_m |E_m|^2
 =\iint g(\alpha)\overline{g(\beta)}e(t_0(\beta-\alpha))K(\beta-\alpha)\,d\alpha\,d\beta.       \tag{3}
$$
There is a single index $m$ in this expansion. By Parseval and Cauchy–Schwarz, $\|\widehat u\|_2\ll\sqrt H L$ and $\|g\|_1\ll H L^2$. Suppose $|K|\ll U L^{-b}$ off $\mathcal M$ and
$$
 \sup_\tau\int_{\tau+\mathcal M}|\widehat f(\alpha)|^2\,d\alpha\ll HL^{-b}.                  \tag{4}
$$
Off $\mathcal M$ the difference variable in (3) costs $O(UH^2 L^{4-b})$. On it, $\int_{\tau+\mathcal M}|g|\ll H L^{1-b/2}$, so the contribution is $O(UH^2 L^{3-b/2})$. Arbitrarily large $b$ yields all logarithmic savings in the second moment. Control of the unshifted arcs alone would only justify the previous first-moment argument.

For any $b$ use Dirichlet approximation to $4j\delta$ of order $\lfloor U^2/L^c\rfloor$, $c$ sufficiently large in terms of $b$. Quadratic differencing gives
$$
 |K(\delta)|^2\ll U+\sum_{1\le k\le U}\min(U,\|4j\delta k\|^{-1})
 \ll U+(1+U/q)(U+q\log(2q))
$$
if the reduced approximant has denominator $q$. In blocks of length at most $q/2$ the frequencies are $1/(2q)$-separated; $q=1$ belongs to the major arcs. Thus (for $U$ polynomial in the height) all large values lie within distance $O(L^c/U^2)$ of fractions with denominator at most $4|j| L^c$. This is uniform in the start of the index interval. Enlarge $c$ or absolute constants to include rounding.

The mixed comparison is uniform for all the even targets here:
$$
 \sum_{a\in I}\vartheta(a) C(t_m-a)=h\mathfrak S(t_m)+O_N(HL^{-N})\quad(N>0).
$$
Use the [two-form calculation](CentralPrimePairDifferences.md#removing-the-local-main-terms-uniformly) with the cutoff above. The consecutive Bonferroni truncations at orders around $(\log L)^2$ involve only moduli $R^{O((\log L)^2)}=Y^{o(1)}$. The omitted product terms are bounded by $(O(\log L))^k/k!$ for $k\asymp(\log L)^2$, enough after normalization by $O(L^{1/10})$. The short-interval Bombieri–Vinogradov theorem applies at the upper-interval lengths used here. The missing Euler factors above $R$ cost $O((\log L)(1+L)/R)$ uniformly. This calculation uses no asymptotic for two true primes at a fixed spacing. [Perelli–Pintz–Salerno, equation (2) and theorem on p. 530](https://www.numdam.org/item/ASNSP_1984_4_11_4_529_0.pdf#page=3)

## Arbitrary central target and the nonzero square shifts

In (1) take $H=\lfloor Y^{2/3}\rfloor$, $I=(Y+2T_Y,Y+H]\cap\mathbb Z$, $J=[Y-4H,Y+4H]\cap\mathbb Z$, $X=Y$. Moving to the true upper interval for $s$ changes $O(1+L^D U^2)$ sites. Even with both log weights, this costs $o(H/L^N)$ for every fixed $N$, since $\eta<2/3$. Replacing $h$ by $H_s$ in the main term has the same precision since $T_Y$ is smaller by a power and $\mathfrak S(2s)\ll\log L$.

Take $d=\lfloor U^2/(100L^{c+1})\rfloor$; all arcs above fit in radii $1/(2d)$ eventually. On any translate of any one arc, the box form of Gallagher's inequality bounds the energy by
$$
 \ll d^{-2}\int_{\mathbb R}
 \left|\sum_{t<n\le t+d,\ n\in J}(\vartheta(n)-C(n))e(\gamma n)\right|^2dt
$$
for the translated center $\gamma$. This follows by Plancherel for a length-$d$ box. Here $d\ge Y^{5/8+\epsilon}$ for some fixed $\epsilon>0$. The all-interval theorem of Matomäki–Shao–Tao–Teräväinen, Theorem 1.1(ii) for a linear phase on the circle, bounds the inner absolute value by $O_M(d/L^M)$ **uniformly in $\gamma$**. Its maximal form includes the intersection with $J$. The theorem uses the cutoff at the interval start $t$; for $|t-Y|\ll H$ it moves by $o(1)$, by differentiation. If a prime crosses the cutoff, its normalization and the affected multiples contribute $O(L^{1/10}(1+d/R))$, within the error. Removing proper prime powers costs $O((1+d/\sqrt Y)L^2)$ by counting roots of each exponent. The range of $t$ has length $O(H)$. There are only polynomially many arcs in $L$, even with all $|j|\le L^D$. This proves (4) at any desired saving. [All-interval theorem, definitions and Theorem 1.1(ii)](https://arxiv.org/pdf/2204.03754v4#page=3)

Apply Chebyshev to (3) at threshold $H L^{-B}$ and take a union over the $O(L^D)$ multipliers. This gives (1). The prime number theorem on $(U/2,U]$ permits restriction to prime $m$, by choosing the saving in the integer exceptional bound large enough.

## What would be visible if the middle failed?

There is also an elementary consequence for the prime pairs themselves. Use any successful shift $d'=jm^2$ in (1) and take a pair $a+b=2(Y+d')$ with $a$ the upper prime. Restrict, if necessary, to $2T_Y+3L^DU^2+3<a-Y<H-3L^DU^2-3$. The removed portion is negligible on the scale $H/L^2$. If the middle has no central representation, **both** $a-2d'$ and $b-2d'$ are composite: $a+(b-2d')=b+(a-2d')=2Y$, and the two middle offsets are in its trimmed range. These composites form a pair at the opposite target $2(Y-d')$. By choosing $j$ divisible by the product of primes through a fixed multiple of $\log L$, both shifted values inherit the prime endpoints' coprimality to that product. Such a $j$ is available on choosing $D$ sufficiently large, by the prime number theorem.

This consequence has limited discriminatory power. Even without absence at the middle, the number of neighbor pairs with *either* shifted endpoint prime is $O(H(\log L)^{O(1)}/L^3)$ uniformly in $0<|d'|\le L^D U^2$. Each option imposes three true prime values on unit-slope linear forms in $a$ with three distinct rational roots. Their differences have size $O(Y)$; only primes dividing their product cause an extra local factor, bounded in total by $(\log L)^{O(1)}$. Use the [uniform three-form upper sieve](CentralPrimePairsNearOneCenter.md#removing-a-central-coefficient-while-preserving-short-interval-counts). Thus already an asymptotic proportion one of the pairs just described gives two composites at the opposite target. Distinguishing an exact zero of the remaining triple count requires another lower bound.

## A test using the same prime endpoint

Fix the scales $Y,H,L,U$ of (1). For $b$ prime in $[Y-H,Y]$, ask how often $b+6q^2$ is prime with $U/2<q\le U$ prime. The coefficient 6 avoids an obstruction at 3. Outside $O_A(H/L^A)$ possible prime values of $b$, the answer is $\gg_\eta U/L^{2+1/10}$. This estimate is local in $b$ at **every** sufficiently large $Y$.

Here are the uniformity details. Put $V=\sum_{U/2<q\le U}\vartheta(q)\asymp U$, summing over integers with the prime-log convention. For each subset $\mathcal B$ of the eligible $b$, use (3) at $t_m=6m^2$ with $u(-b)=1_{\mathcal B}(b)$ and with $J$ containing the endpoints $b+6m^2$ near $Y$. The same translated-arc estimate and quadratic differencing apply to the half interval of integer roots. The absolute values of the Fourier norms of $u$ required in the proof are at most their previous bounds. Cauchy–Schwarz in $m$, with weights $\vartheta(m)$, then gives, uniformly in $\mathcal B$,
$$
 \left|\sum_{b\in\mathcal B} V^{-1}\sum_{U/2<m\le U}\vartheta(m)
                 (\vartheta-C)(b+6m^2)\right|\ll_N H L^{-N}.
$$
Choosing the subsets on which the inner residual has either sign gives the same bound for the sum of its absolute values.

For each such $b$ the corresponding average with $C$ equals $M_b+O_N(L^{-N})$, where
$$
 M_b=\prod_{\ell<R}\frac{1-\rho_b(\ell)/(\ell-1)}{1-1/\ell},\qquad
 \rho_b(\ell)=\#\{v\bmod\ell:(v,\ell)=1,\ b+6v^2=0\bmod\ell\}.
$$
Use the two Bonferroni truncations from the mixed calculation, now in the prime root variable. CRT gives at most $2^{\omega(d)}$ unit classes at a squarefree modulus $d=U^{o(1)}$. The weighted progression errors still save every log power: writing $e_d$ for the maximum absolute prime-log progression error relative to interval length divided by $\varphi(d)$, one has $\sum e_d\ll_N U L^{-N}$ by Bombieri–Vinogradov, and $e_d\ll UL^2/d$ trivially in this modulus range. Cauchy–Schwarz and $\sum_{d\le U}4^{\omega(d)}/d\ll L^{O(1)}$ absorb the multiplicities. Normalizing by $V$ instead of $U/2$ costs arbitrary log savings by the prime number theorem. The Bonferroni main-term tail has the same factorial bound as above. At 2 and 3 there are no roots. At each other prime $\rho_b(\ell)\le2$ and the local factor is at least $(1-1/\ell)(1-O(1/\ell^2))$ with a positive ratio for every $\ell\ge5$. Thus $M_b\gg1/\log R=L^{-1/10}$. The absolute residual bound and Markov prove the assertion after division by the two logarithmic prime weights.

Consequently, among the representations of $2Y$ in the interior window, at most $O_A(H/L^A)$ lower endpoints can fail to extend to $\gg U/L^{2+1/10}$ different neighboring targets $2(Y+3q^2)$ using the **same upper prime**. Conversely, if $2Y$ fails, all such shared-endpoint triples vanish exactly. This gives a lower bound for the signal when the center is rich in pairs and identifies the exceptional endpoint set that could still hide a single pair. A positive shared-endpoint triple would already supply a representation at the center.

Equivalently, let $r_Y$ count the central pairs in the interior used above and let $W_Y$ count their extensions, weighted by $\vartheta(q)\vartheta(b+6q^2)/V$. One can compute $W_Y$ from the neighboring representations by requiring their lower endpoint minus $6q^2$ to be prime and inside that original interior. With absolute positive constants (and an error constant depending on $N,\eta$), the calculation gives
$$
 c\,r_Y L^{-1/10}-O_N(HL^{-N})\ \le W_Y\le C'\,r_Y L^{1/10}+O_N(HL^{-N}).
$$
The upper bound uses $M_b\le 1/V(R)\ll L^{1/10}$, where $V(R)=\prod_{\ell<R}(1-1/\ell)$. Any uniform proof that the neighboring count $W_Y$ is strictly positive would eliminate the isolated failure. The abundance of ordinary neighboring pairs in (1) supplies no such lower bound by itself.

## Dyadic square indices and translated energy for almost all starts

For (2) set $Y=P^2$, $H=\lfloor Y^\theta\rfloor$, $L=\log Y$, and $U=\lfloor H/(100P L^{B+10})\rfloor$. Take consecutive integer indices $x<m\le x+U$ with $x$ an integer in $[P,2P]$, $j=1$ and $t_0=0$. Put $H(x)=\lfloor(x^2)^\theta\rfloor$ and use $I=(x^2+2T_{x^2},x^2+H(x)]$, $J=[x^2-8H,x^2+8H]$, restricted to integers. Freezing costs $O((1+PU)L^2)$ in the true weight per root, absorbed in $O(HL^{-B})$; the analogous main-term change is absorbed too.

Now $d=\lfloor U^2/(100L^{c+1})\rfloor=Y^{2\theta-1+o(1)}$ exceeds $Y^{1/3+\epsilon}$. Apply Matomäki–Radziwiłł–Shao–Tao–Teräväinen, Theorem 1.1(ii) for the linear phase. It gives the maximal bound $d/L^M$ uniformly over phases, outside start sets of measure $O_M(Y/L^M)$. To keep the same model in a packet, cover $[Y,4Y]$ by a fixed number of overlapping dyadic intervals $[X,2X]$, chosen so that each $J+[-d,0]$ lies inside one for large $P$. For each packet use that interval's $R=\exp((\log X)^{1/10})$. Take the union of the finitely many exceptional sets. For an exceptional endpoint start $t$ use the trivial bound $O(dL)$. Its contribution after division by $d^2$ is $O(L^2)$ per unit length of these starts. Each fixed $t$ can belong to $J+[-d,0]$ for at most $O(1+H/P)=O(H/P)$ integer root starts $x$. Hence their total contribution, summed over $x$, per arc, is $O_M(PH L^{2-M})$. The bound is independent of the translate; the exceptional sets in the source are uniform over phases. Sum over the polylogarithmically many arcs and apply Markov. This proves (4) except at $O_N(P/L^N)$ root starts, for any requested saving. [Published almost-all theorem, Theorem 1.1(ii)](https://doi.org/10.1007/s00222-026-01408-6) · [Choice of the model and maximal norm](https://arxiv.org/html/2411.05770v1#S1)

At all other starts, (3) and Chebyshev give $O_N(U/L^N)$ exceptional integer roots. At a bad start use the bound $U$. Summing over starts counts each interior root $U$ times, and the $O(U)$ end roots are negligible since $\theta<1$. This proves (2), hence also its claim for prime roots by restriction. This saves arbitrary powers of a logarithm in the number of exceptions; it is not a power saving in $P$.

There is a stronger local version when $\theta>3/4$. Then $U^2/P$ exceeds a positive power of $P$. After the quadratic differencing step, write a large frequency as $\delta=a/q+\beta$ with $q\le L^{O(1)}$ and $|\beta|\ll L^{O(1)}/U^2$. In each residue class mod $q$, remove the factor $e(2\beta(m-x)^2)$ by partial summation at cost $1+O(|\beta|U^2)$. The remaining linear geometric sum has increment $4xq\beta$. Largeness $|K|>U/L^b$ forces $\|4xq\beta\|\ll L^{O(1)}/U$ (including exact resonance). Since $4xq|\beta|=o(1)$, this gives $|\beta|\ll L^{O(1)}/(PU)$. The arcs now have total length $L^{O(1)}/H$. On the whole interval $J$ the all-interval linear-phase theorem gives $\sup|\widehat f|\ll_M H/L^M$, using the model at $x^2$ as in the all-start proof. This yields (4) for every translate and **every** start. Each such packet has only $O_A(U/L^A)$ exceptional integer roots. A proportion statement specifically among primes inside an individual packet additionally requires a lower bound for their count there.

None of these moment estimates forces a representation at an isolated center. In (1) the zero shift makes $K$ identically $U$, and the minor-arc saving in (3) disappears. At the endpoint $\theta=2/3$ in (2), $d=Y^{1/3}/L^{O(1)}$ falls outside the cited almost-all theorem. These are distinct obstacles.

[Exact finite checks of the double frequency sum and the reflected pairs](CheckSquareShiftDispersion.py)
