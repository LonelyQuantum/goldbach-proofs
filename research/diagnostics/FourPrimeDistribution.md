# Four prime factors at a prescribed square and the remaining prime-density test

Use the notation of the [five-prime estimate](FivePrimeDistribution.md): $X=p^2$, $p$ a large odd prime, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T_0=\lfloor X^{21/40}\rfloor$, $I=(X+2T_0,X+H]$, $h=H-2T_0$, $n=2X-a$ and $K=2C_2H/L^2$. Write $s=67/400$, $V(z)=\prod_{\ell\le z}(1-1/\ell)$ over primes, $P$ for the prime indicator, $P_\lambda(n)=1_{P^-(n)>X^\lambda}$ and $A(n)=1_{P^-(n)>\sqrt L}/(LV(\sqrt L))$. Write $N_f(E)=\sum_{a\in E}f(n)$.

Let $E$ consist of **all** $a\in I$ with four prime factors counted with multiplicity, each $>X^s$. No factor is required to be larger than $X^{1/3}$. For every fixed $\delta<1/6$, $\delta>0$, its reduced-class counts have the estimate

$$
\sum_{d\le X^\delta}\max_{(b,d)=1}
\left|\#\{a\in E:a\equiv b\bmod d\}-\frac{h c_4}{L\varphi(d)}\right|
\ll_{\delta,B}H L^{-B}\qquad(B>0). \tag{1}
$$

With $u_4=1-u_1-u_2-u_3$, the constant is $c_4=(1/24)\int_{\min u_i>s}du_1du_2du_3/\prod_{i=1}^4 u_i$. In particular at each sufficiently large square,

$$
 0.5936K<N_{P_{1/18}}(E)<0.8781K.
$$

The rough sites alone are numerous enough to accommodate the $0.3345K$ forced insertions in the earlier monotone replacement model. Constructing a replacement that also satisfies its other constraints remains a separate question.

**Every even target.** For $N=2X$ with arbitrary integer $X\to\infty$, put
$$
 K_N=\frac{2C_2H}{(\log X)^2}
       \prod_{\substack{\ell\mid N\\\ell>2\ {\rm prime}}}\frac{\ell-1}{\ell-2}.
$$
In the same upper window, the number of $a\in E$ for which $N-a$ has no prime factor $\le X^{1/18}$ is between $0.5936K_N$ and $0.8781K_N$ for **every sufficiently large even $N$**. Indeed the proof of (1) below uses only the location and length of $I$, with constants independent of the integer center. At odd sieve primes $\ell\mid N$, every upper site already avoids $\ell$, so the corresponding sieve density for the reflection is zero. At the other odd primes it is $1/(\ell-1)$. Removing the former primes preserves the upper dimension-one product condition uniformly, and multiplies the survival product by $\prod_{\ell\mid N,\,2<\ell\le X^{1/18}}(\ell-1)/(\ell-2)$. Extending this product to all odd prime divisors changes it by $1+o(1)$ uniformly, since at most $\log N/\log z$ divisors can be distinct primes above $z=X^{1/18}$. For odd squarefree $d$ supported on the remaining primes, the required residue $N\bmod d$ is reduced, exactly as in (1). Applying the same two sieve functions proves the assertion. The signed dichotomy below uses an earlier prime-square estimate and retains that hypothesis.

## A fourth moment of a multiplicative Dirichlet polynomial

In a dyadic prime box $\prod_{i=1}^4 M_i\asymp X$ contributing to $I$, every $M_i\gg X^s$ and the largest $M\gg X^{1/4}$. Take time cutoff $V_0=X^{1/3+\epsilon}$, with $0<\epsilon<\min(1/1200,1/6-\delta)$. Each $M_i^2$ exceeds $V_0$ by a power and $2V_0\le M^{7/5}$ eventually. Split into two pairs for the large-conductor argument of the five-prime estimate. The new step is the small-conductor bound when all four factors are near $X^{1/4}$.

For $D(t)=\sum_{M<m\le 2M}a_m m^{-it}$, $|a_m|\le1$, the following spaced-values bound retains an explicit logarithm. For $U\ge M^{3/4}$, the number of 1-separated points in an interval of length $2V_0$ at which $|D|\ge U$ satisfies
$$
 R\ll \log(2X)\big(M^2/U^2+V_0 M^4/U^6\big). \tag{2}
$$
Partition the time interval into blocks of length $c U^4/M^2$, with a sufficiently small absolute $c$. For the $R_b$ points in one block, the row-sum bound for the Gram matrix of the vectors $(m^{it_j})_{M<m\le2M}$ gives
$$
 R_b U^2\le \sum_m |a_m|^2\,
       \max_i\sum_j\left|\sum_{M<m\le2M}m^{i(t_j-t_i)}\right|.
$$
The diagonal costs $O(M)$. For $1\le v=|t_j-t_i|\le M$, the first derivative of $v\log x/(2\pi)$ is monotone, of size $\asymp v/M$ and bounded away from 1. The first derivative test gives $O(M/v)$, summing to $O(M\log(2X))$ by spacing. For $v>M$ the second derivative test gives $O(\sqrt v+M/\sqrt v)=O(\sqrt v)$. Each such entry is $O(\sqrt c\,U^2/M)$, so their contribution after multiplication by $\sum|a_m|^2\ll M$ is absorbed into the left side. Thus $R_b\ll M^2\log(2X)/U^2$. Summation over blocks proves (2). This is the classical large-values argument in the range needed here. [Guth–Maynard, review of the classical large-value bound, §1](https://arxiv.org/abs/2405.20552)

Now take $a_m=\chi(m)1_{m\text{ prime}}$ with the box cutoff included. For primitive conductors $\le L^C$, Pliego–Sun–Wang's prime-polynomial lemma and partial summation give $|D(t)|\ll_J M L^{-J}$ on all $|t|\le V_0$ for nonprincipal characters. For the principal character use this estimate on $L^{J+3}\le |t|\le V_0$. Denote the respective time set by $\mathcal T$. The classical mean square gives
$$
\int_{\mathcal T\cap\{|D|\le M^{3/4}\}}|D|^4\,dt
\ll M^{3/2}(M+V_0)M\ll M^{39/10}.
$$
For a dyadic level $U\le |D|<2U$ starting at $M^{3/4}$, choose a point of the level set in each occupied unit interval. The two parities of interval indices give two 1-separated sets. Its measure is therefore bounded by twice the bound in (2). Its fourth-moment cost is $\ll L(M^2U^2+V_0 M^4/U^2)$. The first term inside the parentheses is $\ll_J M^4 L^{-2J}$ and the second is $\ll M^{39/10}$. There are $O(L)$ levels. Consequently, for any desired $B$, choosing $J$ sufficiently large gives $\int_{\mathcal T}|D|^4\ll_B M^4 L^{-B}$. [Pliego–Sun–Wang, Lemma 3.1](https://arxiv.org/pdf/2503.02962v1#page=5)

Each of the three other prime polynomials has ordinary fourth moment $O(M_i^4)$ over the entire time range: its square has bounded coefficients and length $O(M_i^2)$, and $V_0\ll M_i^2$. Hölder now gives an arbitrary log saving on the integral of the product of all four, after increasing the log saving in the largest factor fourfold. Fourier inversion contributes $O(H/X)$. For the principal low frequencies use the classical prime number theorem as before. The $2+2$ hybrid large sieve, window smoothing, summation over induced characters, and removal of repeated prime factors have precisely the bounds in the [proof of (3) for five factors](FivePrimeDistribution.md#distribution-in-reduced-residue-classes), with $4!$ for labelled products. In particular removing repetitions in all residue classes costs $O(H X^{-s}\log X+D_0\sqrt X)$ with $D_0=X^\delta$. Changing the final continuous integral to product and exponent coordinates gives $hc_4/L$ up to power savings. This proves (1). [Montgomery–Vaughan, Corollary 26.4 and equation (26.22)](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)

## How much of the four-factor excess needs real lower primes?

Let $E'=E\setminus\mathcal Q_{2/5}$, i.e. retain only four-factor products with largest factor $\le X^{2/5}$. By subtraction (1) holds there with $c'=c_4-c_4(2/5)>0$. For either set write its density as $c$. Set $z=X^{1/48}$ and $A_z(n)=1_{P^-(n)>z}/(LV(z))$. The odd local factors are again $1/(\ell-1)$, so $N_A/K\to c$. At cutoff $X^{1/18}$ the one-dimensional sieve gives lower and upper limiting bounds $12\log(2)c$ and $12c$. At cutoff $z$, after normalizing by $LV(z)$ it gives $cf(8)$ and $cF(8)$ in the limit $\delta\uparrow1/6$ taken after $X\to\infty$. Since $f(8)\le1\le F(8)$, the absolute discrepancy from $c$ is at most $c(F(8)-f(8))$. The linear sieve delay equations give $F(v)-f(v)=2e^\gamma\rho(v-1)/v$ at $v\ge2$; $\rho(7)\le1/7!$ by the Dickman integral identity. [Delay equations and the normalization](LocalizedVaughanComparison.md#localizing-the-signed-remainder)

Using $e^\gamma<2$ and the certified bounds $0.0715511<c_4<0.0731696$ yields, for each of $E,E'$,
$$
|N_{A_z}-N_A|<0.0000073K,\qquad N_{A_z}<0.07318K
$$
eventually. To enclose $c_4$, use $\sum u_i=1$ and permutation symmetry to remove the fourth denominator and change the prefactor to $1/6$. Tile the three independent excess coordinates $u_i-s$ with meshes of side $(1-4s)/192$. Use the monotone reciprocal integrand at opposite corners and the exact clipped volume in each cube (fractions $1/6,5/6,1$ at integer intercepts $1,2,\ge3$). The checker uses integer outward rounding for each contribution.

Define $D_{\rm else}$ as the previous signed upper-composite sum against $P(n)-A(n)$ with the original semiprime strip, the full five-factor sector above $X^s$, and the full four-factor sector above $X^s$ omitted. If there is no central prime pair at a sufficiently large square, at least one of the following must hold:

* $D_{\rm else}>0.0150K$.
* Within $E'$, the fraction of $z$-rough lower sites that are true primes exceeds $1.20/(LV(z))$, whose limit is $1.20e^\gamma/48$ (about $4.45\%$).

Indeed the [previous signed inequality](FivePrimeDistribution.md#consequences-for-reflected-partners) leaves $R+D_{\rm else}+N_P(E')-N_A(E')>0.0297K+o(K)$. On squarefree members of $E'$ the log weight is $1+O(H/(XL))$; the repeated-factor sites contribute $o(K)$. Failure of the second alternative gives $N_P(E')\le1.20N_{A_z}(E')$. The contribution of $E'$ is then at most $(0.2\cdot0.07318+0.0000073+o(1))K$, leaving the claimed strictly positive margin. Neither alternative has been ruled out.

## Relation to the public deep-arc fourth-moment task

The moment in (2) uses phases $m^{-it}$ in multiplicative Fourier inversion. The public task uses $S_n(t)=\sum_{\ell\le n,\ \ell\ {\rm prime}}\log\ell\,e(\ell t)$ with $e(t)=e^{2\pi i t}$ and **additive** frequencies. Two submissions flag the latter's $n^{2+\eta}$ bound. The following short paper check follows their prime-denominator argument. [PR #2496](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2496) · [PR #2508](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2508)

Put $Q=\lfloor n^{1/3}\rfloor$ and use prime denominators $2Q<r\le4Q$. Take intervals of radius $d=1/(16n)$ at $a/r$, $1\le a<r$. They are disjoint by Farey separation and disjoint from the registered wide arcs: for any old denominator $q\le Q$, Farey separation gives disjointness as soon as $r(H_{\rm arc}+qn d)<n$, where $H_{\rm arc}=256Q\lfloor\log_2(n+2)\rfloor^2$. This last inequality holds for large $n$. For $|t|\le d$ the exact Ramanujan identity gives
$$
\sum_{a=1}^{r-1}S_n(a/r+t)=r\log r\,e(rt)-S_n(t).
$$
Its magnitude is $\gg n$ by $\Re S_n(t)\ge\cos(\pi/8)\vartheta(n)$ and $r\log r=o(n)$. Hölder over $a$, integration over $t$ and the prime number theorem on $(2Q,4Q]$ give a lower bound $\gg n^3/(Q^2\log Q)\gg n^{7/3}/\log n$ for the registered deep fourth moment. This invalidates its universal upper bound, for example at $\eta=1/6$. It does not determine the sign of the Goldbach coefficient. Our multiplicative estimate requires no upper bound on that additive moment.

[Exact grid, exponent, and separation checks](CheckFourPrimeDistribution.py)
