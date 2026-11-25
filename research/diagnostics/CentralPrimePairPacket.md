# Central prime pairs and the four-factor penalty in a short interval of centers

Fix $d\ge1$, $x\equiv c\bmod d$, $(b,d)=(2c-b,d)=1$. Put $H_x=\lfloor x^{2/3}\rfloor$ and count positive offsets $h\le H_x$ with $x+h\equiv b\bmod d$. Write $\vartheta(n)=\log n$ for primes and $0$ otherwise. All sums over offsets in this note use this residue condition. The one-sided weighted count is
$$G(x)=\sum_{h}\vartheta(x-h)\vartheta(x+h).$$
For $T=X^\eta$, $5/8<\eta<2/3$, given $A,B>0$, in **each** interval $[X,X+T)$ all but $O_{A,B,d,\eta}(T/\log^A X)$ centers in the specified class satisfy
$$G(x)=H_x\,\mathcal S_d(2x)+O_{B,d,\eta}(H_x/\log^B X). \tag{1}$$
Here
$$
\mathcal S_d(n)=\frac1d\prod_{\ell\mid d}(1-1/\ell)^{-2}
\prod_{\ell\nmid d}\frac{1-\nu_\ell(n)/\ell}{(1-1/\ell)^2},
\qquad \nu_\ell(n)=|\{0,n\bmod\ell\}|.
$$
Products indexed by $\ell$ are over primes. The factor is bounded below by a positive constant depending only on $d$ for even $n$. In particular the unweighted count is $\gg_d H_x/\log^2 x$ at successful centers. Also, away from $O_{A,d,\eta}(T/\log^A X)$ centers, the [previous four-factor penalty](FourFactorTailInShortIntervals.md) satisfies $P_{\rm tail}-B_x<0.023$; its sufficient budget was $0.11$. The two conclusions hold simultaneously after taking the union of the exceptional sets.

These are paper deductions. The published Fourier input below gives the stated $5/8$ range; using the cited 2026 preprint gives the same deductions for $3/5<\eta<2/3$. For the binary conclusion there is substantial prior work: Coppola–Laporta prove an almost-equal summand asymptotic over dyadic target intervals in Theorem 1 and discuss earlier local lower bounds. We make no priority claim. The aim here is to put the residue class, true divisor penalty, and remaining **individual-center** error in the same normalization. [Coppola–Laporta, pp. 245–247](https://www.giovannicoppola.name/files/articoli/8_giovanni_coppola_number_theory_seminar_politecnico_torino_245.pdf)

## The Fourier estimate and the center average

Write $L=\log X$, $w=\exp(L^{1/10})$, $V_1(w)=\prod_{\ell<w}(1-1/\ell)$, $C(n)=\mathbf1_{(n,\prod_{\ell<w}\ell)=1}/V_1(w)$ and $E=\vartheta-C$. On every panel of length comparable to $T$ within $O(X^{2/3})$ of $X$ one has
$$\sup_\alpha\left|\sum_{n\ {\rm in\ panel}} E(n)e(\alpha n)\right|\ll_{M,\eta}T L^{-M} \tag{2}$$
for every fixed $M$. Use the degree-one torus case of Theorem 1.1(ii) of Matomäki–Shao–Tao–Teräväinen. For the extended range use Theorem 1.2, equation (1.4), of Matomäki–Pandey–Pliego–Teräväinen–Wang, v1. A fixed residue condition is allowed by finite Fourier expansion. Prime powers cost $O(\sqrt X L^2)$. Replacing a panel's cutoff $w_U$ by $w_X$ changes the threshold by $o(1)$ by differentiation; at most one prime $\ell\asymp w$ is crossed. Its multiples cost $O((T/\ell+1)L)$, and the change of normalization costs $O(TL/\ell)$. Both are absorbed by (2). [Published theorem](https://doi.org/10.1017/fmp.2023.28) · [2026 preprint, Theorem 1.2](https://arxiv.org/html/2610.09567v1)

Freeze the lower endpoint interval at $I=[X-H_X,X)$, with integer arguments throughout. Uniformly over the centers this costs $O(T)$ terms, negligible to every fixed log saving at scale $H_X$, even with weights $O(L^2)$. Partition $I$ into $O(H_X/T)$ intervals $J$ of length at most $\lceil T\rceil$. For each $J$ the upper arguments $2x-a$ fit into a single panel of length $3\lceil T\rceil+O(1)$ independent of $x$. An upper condition $2x-a\equiv b\bmod d$ goes into the panel weight. Let $\beta$ be a fixed lower weight on $J$ bounded by $O(L^j)$ for fixed $j$. Parseval for convolution on $\mathbb Z$ and (2) give
$$
\Big\|\sum_{a\in J}\beta(a)E(2x-a)\mathbf1_{2x-a\equiv b(d)}\Big\|_{\ell^2(X\le x<X+T)}
\le \|\widehat {E_{\rm panel}}\|_\infty\,\|\beta\|_2
\ll T^{3/2}L^{j-M}.
$$
The panel on the right includes the class restriction. Restricting convolution indices to $2x$ can only decrease their squared sum. The triangle inequality over $J$ gives $O(H_X\sqrt{T}L^{j-M})$. Taking $M$ as large as necessary and applying Chebyshev yields error $O(H_XL^{-B})$ outside $O(TL^{-A})$ centers. In particular $\beta=E$ is admissible. This argument bounds a norm over centers and permits exceptional individual values.

## Cancelling the two mixed terms at every center

There is a stronger pointwise treatment for convolution terms with one factor $C$. Put $r=\lfloor L^{1/3}\rfloor$. Inclusion–exclusion for avoiding all sieve primes can be bracketed by adjacent Bonferroni sums of orders $r-1,r$. The gap counts $r$ simultaneous hits. In an interval of length $h\asymp H_X$ and fixed reduced class modulo $m$ (here $m$ may vary up to $d w^r$), for conditions at primes coprime to $m$ with at most two bad residues each, its sum is bounded by
$$
\frac h m\,\frac{(2\sum_{\ell<w}1/\ell)^r}{r!}+O(2^r w^r).
$$
This follows by counting the CRT classes for each squarefree product. Rounding over the whole truncated sum has the same $X^{o(1)}$ bound up to polynomial factors in $r$. The factorial term decays faster than $L^{-D}$ for every fixed $D$; even multiplying by $O(L^j)$ preserves arbitrary log savings. The same bracket bounds the independent product model. In particular the model-model term equals $H_x\mathcal S_d(2x)+O_D(H_xL^{-D})$ pointwise. Extending its product from $w$ to infinity costs relative $O((1+L)/w)$: primes not dividing $2x$ contribute $1+O(1/\ell^2)$ and at most $O(L/\log w)$ larger primes divide $2x$. The truncated factor grows at most polylogarithmically.

For $C(a)E(2x-a)$ expand the small-prime avoidance of $a$ by the same bracket. Each squarefree $k\le w^r$ appears once with coefficient of magnitude at most one before the common factor $1/V_1(w)$. A factor of $k$ dividing $d$ is incompatible with the unit class of $a$. If $(k,2x)>1$, both $\vartheta(2x-a)$ and $C(2x-a)$ vanish for $k\mid a$, since $2x-a$ is large. Otherwise $2x-a$ is in a reduced class modulo $dk$. The sum of discrepancies of $\vartheta$ from $H_x/\varphi(dk)$ over these moduli is $O_D(H_xL^{-D})$ by Cai–Lu, Lemma 3 at $\beta=0$, level $X^{1/6}/L^{O_D(1)}$. Here $dw^r=X^{o(1)}$ is within that level. Convert their ordinary prime counts to log weights by partial summation or freezing $\log p$ at $\log x$ (the error per term is $O(H_x/x)$); all intervals have length $H_x$ and starting point near $x$. The same estimate for $C$ follows directly by the preceding bracket inside the class: the uniform error per $k$ is $O_D(H_x L^{-D}/(dk)+X^{o(1)})$ and the expected value is $H_x/\varphi(dk)$ because every prime of $dk$ is below $w$. Summation costs at most $\sum 1/k\ll\log w$ in the main error. Reflection exchanges the roles in the other mixed term, with the admissible lower class $2x-b\bmod d$. [Cai–Lu, Lemma 3, p. 313](https://bibliotekanauki.pl/articles/1216105.pdf#page=3)

Consequently, writing $Q(x)$ for the sum defining $G(x)$ with both $\vartheta$ replaced by $E$, at **every** center in the packet
$$G(x)=H_x\mathcal S_d(2x)+Q(x)+O_{D,d}(H_xL^{-D}). \tag{3}$$
Here (3) also works for each individual center by taking $X=x$. Applying the panel estimate to the frozen form of $Q$ proves (1). A lower bound $Q(x)\ge -(1-\epsilon)H_x\mathcal S_d(2x)$ for one fixed $\epsilon>0$ and every sufficiently large $x$ would force central binary representations. The $\ell^2$ estimate above does not establish it.

## The signed four-factor comparison

Use $D_x=x^{1/6}/(d\log^B x)$, $z_x=D_x^{1/6}$, $u=11/20$ and the normalization and marker average in the [tail note](FourFactorTailInShortIntervals.md). Write $J_0=3e^{-\gamma}(\log(30/11)-1+11/30)<5/8$. The panel estimate implies
$$P_{\rm tail}\le(51/50+o(1))J_0+o(1) \tag{4}$$
outside $O_A(TL^{-A})$ centers. To see this, majorize the lower weight by the fixed $z_X$-rough indicator times $\sum_{q\mid a}(1-u\log q/\log D_{X+T})$ for $D_X^{2/3}\le q<D_{X+T}^{1/u}$. This weight is bounded since all counted prime divisors exceed $X^{1/9-o(1)}$. The boundary costs $O(TL)$ with log weights. Replace the upper prime by $C$ by (2), dividing by $\log X$ with negligible error. The resulting nonnegative count can be bounded for each $q$ by the Selberg square at radius squared $H_X/(qL^{12})$. It forbids $0\bmod\ell$ on the lower endpoint for $\ell<z_X$ outside $d$ and also $2x\bmod\ell$ for $\ell<w$. Coincident classes are counted once. The independent divisor law in that square has mean at most $(1+o(1))\log z_X$ and variance at most $(1/2+o(1))\log^2 z_X$, because $\log w=o(\log z_X)$. The one-root Cantelli factor $51/50$ of the tail note therefore applies uniformly.

For the Euler products, the extra $1/V_1(w)$ cancels the one-root factors below $w$, with the primes of $d$ supplying $d/\varphi(d)$. At odd $\ell<w$ outside $d$ the second factor is $1-1/(\ell-1)$ when $\ell\nmid 2x$ and $1$ otherwise. This is precisely the old $V$ times the exceptional-prime factor there. Between $w$ and $z_X$ the remaining ratio to the true normalization is bounded above by $\prod_{\ell\ge w}(1+1/(\ell(\ell-2)))=1+o(1)$; the extra exceptional factors occur in the denominator. The dyadic rounding estimate and the prime reciprocal integral from the tail note now give (4). Freezing endpoints enlarges the upper range by $1+o(1)$ relatively and leaves the integral unchanged. Since the marker factor is at least one, the exceptional-set error also stays negligible after normalization.

For a lower bound on the previous **two-root** integer comparison $B_x$, use Buchstab's identity between $w$ and $z=z_x$ on each $q$-progression and each tuple of markers. The initial $w$-rough count has its product main term by the CRT bracket above with interval length $H_x/(dq)$; summing the $X^{o(1)}$ errors over $q\le X^{10/33+o(1)}$ is harmless. For a first bad prime $w\le s<z$, the subtracted count is upper-sieved below $s$ in each forbidden class modulo $dqs$, using radius $R_s^2=H_x/(qsL^{12})$. Let $J_s$ have the independent divisor law with inclusion probabilities $\nu_\ell/\ell$ for sieve primes $\ell<s$, where $\nu_\ell=2$ except at 2 and the fixed omitted primes. The fourth central moment of $\log J_s$ is at most $(7/2+o(1))\log^4s$. Indeed it is bounded by three variance squares plus $\sum_{\ell<s}(\nu_\ell/\ell)(\log\ell)^4$ (a centered Bernoulli fourth moment is at most its success probability). These terms are $(3+o(1))\log^4s$ and $(1/2+o(1))\log^4s$ respectively.

Put $v=\log s/\log z$. Since $\log R_s-\mathbf E\log J_s\ge(72/11-1/2-2-o(1))\log z>4\log z$, the missing denominator probability is at most $v^4/64$ for large $X$. Thus the excess of the optimal upper main term over its product density is at most $v^4/63$ times that density. If $V_2(s)$ denotes the two-root survival product below $s$, then $V_2(s)/V_2(z)=(1+o(1))v^{-2}$ uniformly for $s\ge w$. Buchstab's product main terms telescope. Relative to the final full product, the total excess subtracted is at most
$$\frac{1+o(1)}{63}\sum_{w\le s<z}\frac{\nu_s}{s}v^2\le 1/63+o(1).$$
The absolute rounding errors sum over $q,s$ to $O(H_x/L^5)$ by the sixfold divisor bound from the tail note and the radii just specified. The primes $q\mid 2xd$ omitted from $B_x$ have negligible reciprocal mass. Restoring the same weight and normalization gives $B_x\ge(62/63-o(1))J_0$ **at every center**. With (4), the excess on the good centers is at most $(51/50-62/63)J_0+o(1)<0.023$ for sufficiently large $X$. The argument does not bound the true tail at a prescribed exceptional center.

The companion [exact finite checks](CheckCentralPacket.py) verify the local class factor, the convolution expansion, and the truncation constants. The analytic inputs and the exceptional-set argument are paper mathematics.

For $d=1$, a [shorter-packet estimate and a deletion construction](CentralPrimePairsNearOneCenter.md) quantify how much these means determine at one prescribed center.
