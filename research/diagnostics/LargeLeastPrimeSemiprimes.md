# The two large primes in a reflected semiprime

Let $N=2s$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $h=H-2T$, and $I_s=(s+2T,s+H]$. Write $a\in I_s$, $b=2s-a$, and $z_s=\exp(L/(\log L)^3)$. Work on the set $\mathcal A_s$ where $a,b$ are squarefree and coprime to one another, and neither has a prime factor $\le z_s$. Let $S_s=h\mathfrak S(2s)$, with the even-target singular series as in the [proper-divisor estimate](ProperDivisorScales.md). In the even-parity sector $\mu(b)=1$, a least prime factor exceeding $w_s=(2s)^{1/3}$ forces $b=pq$, for distinct primes $w_s<p<q$. We examine the actual signed sum
$$
 F_s(B)=\sum_{\substack{a\in\mathcal A_s,\ b=pq\\w_s<p<q,\ p\in B}}
              \mu(a)\log a\log b ,
$$
and its unsigned counterpart $M_s(B)$, obtained by omitting $\mu(a)$. Here $B$ is an interval of smaller prime factors unless otherwise stated. The added contribution to the right bins of the preceding note, equation (8), is $2F_s(B)$.

## What cancels at each individual target

Take $R=s^{1/7}$ and $Z=h\exp[-4L/(\log L)^{3/2}]$. First use equation (2) of the preceding note **before** its optional switched exclusions. For every $a\in\mathcal A_s$ with this semiprime $b$, and each $d\mid a$, $d>R$, the sum over $e\mid b$, $e>R$, $[d,e]>Z$, excluding the common factor $\mu(d)\log d$, is exactly
$$
       (\log p)1_{dp\le Z}+(\log q)1_{dq\le Z}.                      \tag{1}
$$
Indeed the only nonzero possibilities are $p,q,b$ with coefficients $-\log p,-\log q,+\log b$. Their sum is zero. Since $(a,b)=1$, $[d,e]=de$ and $db>Z$. Removing the two possible small-modulus terms proves (1), including the strict cutoff at equality. Without any modulus cutoff every such semiprime contributes zero to the double-long sum separately for **each** $d$.

Thus the $d=a$ row contributes exactly zero for all these $b$, at every center. More generally the only surviving $d$ in (1) satisfy $R<d\le Z/p<s^{1/3}$ for large $s$. If both endpoints are products of two primes greater than $w_s$, the whole sector vanishes. If the optional exclusions $x e^2\le s^{1/3-\epsilon}$ or $y d^2\le s^{1/3-\epsilon}$ with $x=a/d,y=b/e$ are made, subtract $(\log b)1_{d^2\le s^{1/3-\epsilon}}$ from (1): the first exclusion is empty and the second can remove only $e=b$. This still leaves $d=a$ identically zero. The surviving signed terms in (1) are weighted by $\mu(d)\log d$. They must be controlled alongside the other sectors; their putative signs are not the signs of $\mu(a)$.

The row identity does not assert that $F_s(B)$ vanishes. The preceding regrouping replaced the whole-divisor term using a single-endpoint mean over **all** partners. Restricting that replacement to a chosen set of semiprimes can lose a term equal to $F_s(B)$. Equation (1) shows why a pointwise bound on $F_s(B)$ is not necessary for handling the full-divisor row of this sector.

There is a general form. For any squarefree composite $b$ with $P^-(b)>R$ and any $d>R$ dividing the coprime reflection, the unswitched surviving inner sum is
$$
 -\sum_{\substack{e\mid b\\1<e\le Z/d}}\mu(e)\log e .
$$
The complete log-divisor sum is zero on composites and every nontrivial divisor exceeds $R$. In particular every row with $dP^-(b)>Z$ is zero on that sector. When $Z/d$ is below the product of the two smallest prime factors of $b$, the displayed sum is just the sum of the logarithms of its prime factors up to $Z/d$. These are exact cancellations inside the arithmetic expansion and do not require a parity hypothesis.

### An explicit discrepancy for the surviving contribution

Let $J_r=\{t>w_s:s-H\le rt<s-2T\}$ and $v_r=\int_{J_r}dt/\log t$. Let $\Pi_{r,d}$ count primes $t\in J_r$, $t\ne r$, for which $a=2s-rt\in\mathcal A_s$ and $d\mid a$. Put $P=\prod_{\ell\le z_s}\ell$ and $U=\prod_{\ell\le z_s,\ \ell\nmid N}(1-1/(\ell-1))$. The contribution of this entire partner class to the unswitched remainder equals
$$
 \sum_{\substack{w_s<r\le Z/R\\ r\ {\rm prime},\ r\nmid N}}
  (\log r)\!
  \sum_{\substack{R<d\le Z/r\\(d,NrP)=1}}
     \mu(d)\log d
     \left(\Pi_{r,d}-\frac{U v_r}{\varphi(d)}\right)
  +O_A(h L^{-A}).                                                     \tag{1a}
$$
In fact the $\Pi$ term is (1) summed exactly: choose each prime factor $r$ whose logarithm survives, so both may be chosen. The constraint on $d$ is forced for actual records by squarefreeness of the Möbius summand, roughness and coprimality of the endpoints. $U$ is the product for avoiding the small divisors of $N-rt$ among prime $t$ in a reduced class. We use it as a comparison and make no per-progression approximation here.

For the comparison term alone, uniformly for $R\le u\le s$,
$$
 \sum_{\substack{R<d\le u\\(d,NrP)=1}}\frac{\mu(d)\log d}{\varphi(d)}
    \ll_A L^{-A}.
$$
Subtract the sharp prefixes at $u$ and $R$. Each has the same constant by the one-variable Euler correction of [the strong-sieve calculation, steps 2–3](ProperDivisorScales.md#recovering-the-main-term-after-strengthening-the-sieve): on primes dividing $NrP$ the numerator of the correction is 1, elsewhere it is $1-\ell^{-s'}/(\ell-1)$, and the denominator is $1-\ell^{-1-s'}$. At $\sigma=1/\log z_s$ its absolute coefficient norm is $L^{O(1)}$, uniformly also after adjoining $r$. The coefficient tail above $\sqrt R$ is smaller than every log power; below that cutoff both Möbius log-prefixes have the same constant by the zero-free-region PNT. Since $v_r\ll h/(rL)$ and the prime reciprocal sum on the fixed exponent range is bounded, the comparison contributes only the stated error. No sign estimate for the discrepancy has been used.

Every surviving prime satisfies $r\le Z/R<s^{11/21}$. For any fixed $\delta>0$, if the smaller factor $p\le s^{10/21-\delta}$, only $r=p$ can occur in (1a); its partner $q\ge(s-H)/p$ is already too large. This separates an asymmetric range from the range near $\sqrt s$.

## How large can the isolated sum be?

Uniformly at each large $s$ and even for an arbitrary subset $B$ of the smaller primes,
$$
 |F_s(B)|\le M_s(B)\ll S_s\frac{L}{\log z_s}
     \sum_{\substack{w_s<p\le\sqrt s\\p\in B}}\frac1p
     +O_A(h L^{-A}).                                                 \tag{2}
$$
In particular, any collection of $o(L/(\log L)^3)$ dyadic intervals of $p$ contributes $o(S_s)$, and all of them together have absolute mass $O(S_s(\log L)^3)$. For the sparse collection use $\sum_{P<p\le2P}1/p\ll1/L$ on this range. The remainder in (2) is uniform in the entire collection.

For fixed $p$, let $v$ be an integer in the interval for $q$, of length $h/p$, and put $D=s^{1/50}$. Upper-bound the true primes there using a Selberg square $(\sum_{d\mid v}\lambda_d)^2$ with $\lambda_1=1$, squarefree $d\le D$ supported on primes $>z_s$. Also sieve $v,2s-pv$ at all primes $\ell\le z_s$. A counted prime $v>p$ passes the square with value one. For $r=[d,e]$ from the square, impose $r\mid v$. On that progression the forbidden small residues for $v$ have multiplicity $\nu_\ell=1+1_{\ell\nmid 2s}$, since $p,r$ are units there. If $V=\prod_{\ell\le z_s}(1-\nu_\ell/\ell)$, the count is
$$
 (h/(pr))V + O_J\big((h/(pr))L^{-J} + s^{o(1)}\big).
$$
One may enlarge the $v$ interval to the whole interval for the product, dropping $p<v$ for this upper bound. Bonferroni at consecutive orders near $(\log L)^{3/2}$ gives the displayed error: the density tail is bounded by $(O(\log L))^j/j!$ and the rounding by $(1+2z_s)^{j+2}$. Here $V\asymp\mathfrak S(2s)/(\log z_s)^2$ uniformly.

For clarity, the Selberg quadratic form $\sum\lambda_d\lambda_e/[d,e]$ is $1/G$ for the usual minimizing weights, where $G=\sum_{d\le D,\ d\ {\rm supported\ on\ primes}>z_s}\mu^2(d)/\varphi(d)$. Indeed put $t_k=\sum_{k\mid d}\lambda_d/d$ on this divisor-closed support. The form is $\sum_k\varphi(k)t_k^2$, and $\lambda_1=\sum_k\mu(k)t_k$. Equality in Cauchy–Schwarz gives $t_k=\mu(k)/(\varphi(k)G)$; inversion gives $|\lambda_d|\le d/\varphi(d)\ll L$. Also $G\gg\log D/\log z_s$. To see this take all squarefree products of primes $z_s<\ell\le D^{1/4}$, weighted by $1/\varphi(d)$. Their total Euler product is $\asymp\log D/\log z_s$. Under the normalized weights the mean of $\log d$ is $\sum(\log\ell)/\ell\le(1/4+o(1))\log D$, so at least half the weight has $d\le D$.

The reciprocal modulus sum over $d,e\le D$ is $O(L^3)$ by writing $d=gu,e=gv$, $g=(d,e)$. Summing the rounding over $p,d,e$ costs $s^{1/2+2/50+o(1)}$, even after the log weights. Increasing $J$ absorbs all remaining log factors. The resulting bound $O((h/p)V/G)$ summed over $p$ and multiplied by $O(L^2)$ gives (2).

## Cancellation on almost all centers of each short packet

For every fixed $5/8<\theta<2/3$, every sufficiently large integer $X$, $K=\lfloor X^\theta\rfloor$, and every $A>0$,
$$
 \left(\sum_{X\le s<X+K}\sup_{B\ {\rm interval}} |F_s(B)|^2\right)^{1/2}
       \ll_{A,\theta} H_X\sqrt K\,(\log X)^{-A}.                     \tag{3}
$$
In particular, outside $O_{A,C,\theta}(K/(\log X)^A)$ centers, **every** interval of smaller primes at that center has $|F_s(B)|\le H_X/(\log X)^C$. The interval may be selected after seeing the center. The bound does not assert a small sum for the specifically prescribed $s=X$, nor does it give the same assertion for arbitrary subsets of primes.

Here are details of the analytic input and the two decompositions. Write $L_X=\log X$ and freeze the lower interval for $b$ to the reflection of $I_X$. This changes $O(K+1)$ integers per center. The cutoff $w_s$ moves by $O(KX^{-2/3})=o(1)$. At most one integer prime can cross, costing $O(H_X/X^{1/3}+1)$ multiples. Similarly the variation of $z_s$ is $o(1)$, with a possible crossing costing $O(H_X/z_X+1)$. The conditions on $(a,b)$ cost $O(H_X/X^{1/3}+1)$ per center, since a common prime is one of the $O(1)$ prime factors of $2s$ exceeding $w_s$; $\mu$ already kills nonsquarefree $a$. All these costs, including logarithmic weights, are $O_{A,\theta}(H_X L_X^{-A})$. Replace $\log a\log b$ by $L_X^2$ using an error $O(L_X H_X/X)$ per position.

Let $g(n)=\mu(n)1_{(n,\prod_{\ell\le z_X}\ell)=1}$. On any interval $J'$ of length comparable to $K$ and height $X+O(H_X)$,
$$
 \sup_\alpha\left|\sum_{n\in J'}g(n)e(\alpha n)\right|
       \ll_{A,\theta} K L_X^{-A}.                                    \tag{4}
$$
Use the exact convolution $g(n)=\sum_{c\mid n,\ \ell\mid c\Rightarrow\ell\le z_X}\mu(n/c)$. Fix $\eta>0$ small enough that $K/c\gg(X/c)^{5/8+\delta}$ for $c\le X^\eta$ and some fixed $\delta>0$ (also take $2\eta<\theta$). Large $c$ require a smooth divisor in $[X^\eta,X^\eta z_X]$. Counting its multiples on $J'$ and using Rankin at $\sigma=1/\log z_X$ gives $O_A(KL_X^{-A})$ such positions: the Euler product $\prod_{\ell\le z_X}(1-\ell^{-1+\sigma})^{-1}\ll L_X^{O(1)}$ is outweighed by $X^{-\eta\sigma}$. The rounding is $O(X^\eta z_X)$. The extra multiplicity $\tau(n)$ on these positions costs only logarithmic powers by Cauchy–Schwarz and the fixed short-interval divisor moments (the short-divisor proof in the preceding note applies also at length $K$). For the smaller $c$ use the linear-phase case of Matomäki–Shao–Tao–Teräväinen on the dilated interval and sum $K/c$. This proves (4) with arbitrary $A$. [Theorem 1.1(i), equation (1.5)](https://arxiv.org/pdf/2204.03754v4#page=3)

Split the frozen $b$ interval into $O(H_X/K)$ integer cells of length at most $K$. For each cell take a single interval $J'$ of length comparable to $K$ covering every $2s-b$ in the packet. Regard the indicator of semiprimes in the cell as a sequence on $b$, labeled by its unique smaller prime. Pad the ordered prime list to a power of two and form its binary interval tree. For a tree node $V$, let $f_V$ be the subindicator with labels in $V$. At each fixed depth, $\sum_V\|f_V\|_2^2\le K+1$ because each integer has at most one label. Parseval for additive convolution and (4) bound $\sum_V\|(g1_{J'})*f_V\|_2^2$ by $O_{A,\theta}(K^3 L_X^{-2A})$ at that depth, including when sampled only at the even indices $2s$. Each interval of labels is the union of at most two nodes per depth. Its maximum contribution at $2s$ is bounded by twice the sum, over depths, of the square root of the sum of squared node contributions there. Minkowski's inequality and the $O(L_X)$ depths finish the maximal estimate on one cell. Sum over the physical cells and restore the two log weights, increasing $A$ beforehand. This proves (3).

## The unsigned comparison has a different scale

With $B$ the whole band and the same packet,
$$
 \frac1K\sum_{X\le s<X+K}M_s(B)
     =(2e^{-\gamma}\log 2+o(1))\,H_X\frac{L_X}{\log z_X}.           \tag{5}
$$
Here $\gamma$ is Euler's constant. The [short-interval semiprime count, equation (1)](SemiprimePackets.md#counting-the-lower-semiprimes) applies to the fixed exponent band $1/3<u<1/2$: the frozen lower interval contains $(\log2+o(1))H_X/L_X$ such $b$, from $\int_{1/3}^{1/2} du/[u(1-u)]$. Changing $X^{1/3}$ to $(2X)^{1/3}$ costs $o(H_X/L_X)$ by squeezing between fixed exponents tending to $1/3$. This input is a deduction from a prime short-interval exceptional-set estimate. [Gafni–Tao, definition and Lemma 1.1](https://arxiv.org/pdf/2505.24017#page=4)

For each such odd $b$, $2s-b$ runs over $K$ odd integers of step two. Sieving just the odd primes $\ell\le z_X$ gives $(2e^{-\gamma}+o(1))K/\log z_X$ rough values, uniformly in $b$, by the same truncated inclusion-exclusion and Mertens' product. When aggregated, nonsquarefree rough $a$ cost $O(H_X/z_X+\sqrt X)$ per center by summing over squares of primes $>z_X$; this estimate is on the full upper window, not on a packet for a single fixed $b$. The other changes are paid as in (3). This proves (5).

As a consequence, in each such packet a positive proportion of centers have both signs of $\mu(2s-pq)$ contributing unsigned log weight $\gg_\theta H_X(\log L_X)^3$ each. Indeed $\sum_{X\le s<X+K}\mathfrak S(2s)^2\ll K$: expand the squared odd correction as $\sum_{d\mid s}g(d)$ with squarefree support, $g(\ell)=((\ell-1)/(\ell-2))^2-1=O(1/\ell)$. Then $\sum g(d)/d=O(1)$ and $\sum_{d\le 2X}g(d)\ll L_X^{O(1)}$. Equation (2) and Cauchy–Schwarz applied to the mean in (5) give a positive proportion with large mass; discard the exceptional centers in (3). Thus direct absolute summation across all $p$ loses an unbounded factor on actual data. The packet estimate supplies no uniform sign saving for the isolated sum at every center.

For fixed-target work the next arithmetic question is the **sum of the remaining small-divisor expressions in (1)** together with the complementary partner classes. On $\mathcal A_s$, $pq\equiv N\bmod d$ is a reduced class. Holding one prime factor $r\in\{p,q\}$ fixed puts the other in an interval of length $h/r$ at height about $s/r$. The $y/\sqrt{x}$ modulus range used in the earlier short-interval prime estimate has size at most $O(s^{1/6}/\sqrt r)=O(1)$ here, even before its logarithmic losses, whereas $d>s^{1/7}$. So that estimate for each single $r$ cannot handle the surviving moduli. A further estimate must exploit averaging or a different arithmetic input. [Short-interval modulus range, (1.1)](https://arxiv.org/pdf/1405.6592v2#page=1)

At $s=1009^2$, with diagnostic sieve cutoff 29, $R=7$ and illustrative $Z=7270$, 64 retained starts have a large-least-prime semiprime partner. The signs of $\mu(a)$ split 34 positive to 30 negative, while the complete $d=a$ row vanishes at every start. Three nonzero boundary rows remain. In the checker the logarithm is replaced by an additive integer weight to verify the regrouping exactly; its numerical sum is not an estimate of the analytic signed weight. [Exact finite checks](CheckLargeLeastPrimeSemiprimes.py)
