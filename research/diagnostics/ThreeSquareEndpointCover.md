# Recovering individual central Goldbach pairs from two lists of neighboring pairs

Fix an integer $Y$, write $L=\log Y$, $H_s=\lfloor s^{2/3}\rfloor$, $T_s=\lfloor s^{21/40}\rfloor$, and let $I=\{v:2T_Y<v\le H_Y\}$ consist of integer offsets. Put $a=Y+v$, $b=Y-v$. Write $\mathcal R=\{v\in I:a,b\text{ are prime}\}$ and $r=|\mathcal R|$. A central pair at any center $s$ is unordered, with offset of absolute value in $(2T_s,H_s]$.

For each sufficiently large $Y$, there is a set of $O((\log Y)^2)$ positive shifts, the same set for all offsets, with the following property. List the primes appearing in actual central pairs at the chosen neighboring targets on each side of $2Y$. An offset $v$ in the admissible classes below belongs to $\mathcal R$ exactly when $Y+v$ appears on the positive side and $Y-v$ appears on the negative side. Both neighbors have many representations. Even a single central representation survives this operation. The construction uses sums of **three** prime squares and independent choices on the two sides. The [single-square estimate](SquareShiftDispersion.md) had an exceptional set of endpoints. This note gives an unconditional deduction from published estimates and the [local packet calculation](CentralPrimePairPacket.md), with no claim of priority.

## A family of shifts that works at every endpoint

Fix $5/8<\eta<2/3$, and $D=\lfloor Y^\eta\rfloor$. Start with the integers $D<n\le 2D$ in the four classes $3,27,51,99\bmod 120$. Keep $n$ when it has a representation by three **distinct** prime squares with the largest and smallest roots differing by at most $4D^{9/20}$. Count each $n$ once. Also require that at **both** $s=Y\pm15n$ the trimmed prime-log pair count is at least $\tfrac12 H_s\mathfrak S(2s)$, where $\mathfrak S$ is the usual binary singular series. Call the retained set $S$.

The congruences express $n\equiv3\bmod24$ and $5\nmid n$. For the square condition use Kumchev–Li, definition (1.3) and Theorem 4 with $\theta=9/10$. Their exception bound $O_\epsilon(X^{31/35+\epsilon})$ is local on $|n-X|\le X^{19/20}$. Cover $(D,2D]$ with $O(D^{1/20})$ such intervals, with $D\le X\le2D$. The total is $O_\epsilon(D^{131/140+\epsilon})$. In each representation obtained there all roots are within $X^{9/20}$ of $\sqrt{n/3}$. The number of integers with any such repeated-root representation is $O(D^{19/20})$, by writing $2p^2+q^2$ and counting $O(\sqrt D)$ choices of $p$ and $O(D^{9/20})$ choices of $q$ near $p$. This also allows $p=q$. [Kumchev and Li, J. Number Theory 132 (2012), definition and Theorem 4](https://arxiv.org/pdf/1109.5594v1#page=3)

For each sign the shifted centers lie in an interval of length $15D$ at height $Y+O(D)$. Cover it by $O(1)$ packets of length comparable to $Y^\eta$ and use the [local packet estimate (1)](CentralPrimePairPacket.md) with modulus one. Removing the inner $2T_s$ offsets costs $O(T_s L^2)$, and the singular series on even targets has an absolute positive floor. Since $n\mapsto Y\pm15n$ is injective for each sign, the failure of either richness condition removes $O_A(D/L^A)$ labels for every fixed $A>0$. It follows that $|S|=D/30+O_A(D/L^A)$. The two earlier estimates used here concern distinct integers and permit the exceptions to be removed before specifying an endpoint.

For **every** integer $x=Y+O(H_Y)$ with $(x,30)=1$, separately for each sign,
$$
 \#\{n\in S:x\pm30n\text{ prime}\}=\frac{D}{8L}+O_A(D/L^A). \tag{1}
$$
Indeed $x\pm30n$ traverses four distinct reduced classes modulo $3600$ on an interval of length $30D$. All prime divisors of the modulus divide 30. The prime number theorem in short intervals for this fixed modulus gives $30D/(\varphi(3600)L)$ per class, up to $O_A(D/L^A)$, and $\varphi(3600)=960$. This follows, for example, from Perelli–Pintz–Salerno's short-interval Bombieri–Vinogradov estimate since $\eta>5/8>3/5$. Removing prime powers costs $O(\sqrt Y L^2)$ even on the full dyadic range. Replacing $\log p$ by $L$ costs a power saving here since $p=Y+O(H_Y)$. Each deleted $n$ costs at most one at a given $x$. Uniformity includes composite $x$ coprime to 30. The two signs may use different labels. [Perelli, Pintz and Salerno, pp. 529–530, equation (2) and theorem](https://www.numdam.org/item/ASNSP_1984_4_11_4_529_0.pdf#page=3)

## Matching the two observations at one offset

Restrict to the eligible offsets $\mathcal V=\{v\in I:(ab,30)=1\}$, which include every genuine pair for large $Y$. For $n\in S$ use the following two sets from neighboring pair lists.

- $P_n$ consists of $v\in\mathcal V$ such that $a$ occurs in a central prime pair summing to $2(Y+15n)$. Its partner must be $b+30n$.
- $M_n$ consists of $v\in\mathcal V$ such that $b$ occurs in a central prime pair summing to $2(Y-15n)$. Its partner must be $a-30n$.

In each case the neighboring absolute offset is $|v-15n|$. It is permissible for the named prime to change sides of the midpoint. The upper cutoff is automatic for all $v\in I$ and all large $Y$, since $|v-15n|\le\max(30D,H_Y-15D)$ while $H_{Y\pm15n}=H_Y+O(1+DY^{-1/3})$. At each $v$ the lower cutoff discards only $O(1+Y^{21/40})$ labels for either sign, by the length of the interval for $15n$. This costs $O_A(D/L^A)$. In particular the extreme offsets of the original window need no additional trimming.

Writing $\lambda=D/(8L)$, each prime $a$ in the eligible set belongs, through its offset, to $\lambda+O_A(D/L^A)$ positive lists, and each prime $b$ belongs to that many negative lists. A composite anchor belongs to none on its side. This gives the exact union identity and the uniform multiplicative count
$$
 \mathcal R=\left(\bigcup_{n\in S} P_n\right)\cap
             \left(\bigcup_{m\in S} M_m\right),\qquad
 \sum_{n,m\in S}|P_n\cap M_m|
   =\lambda^2 r\,(1+O_B(L^{-B})) \quad(B>0).                  \tag{2}
$$
For the second identity, at each $v\in\mathcal R$ multiply its two degrees, then sum over $v$. For $r=0$ the double sum is exactly zero.

The same union identity holds for a common subset $F\subset S$ of at most $\lceil(8/45+\epsilon)L^2\rceil$ labels, for each fixed $\epsilon>0$ and all large $Y$. Draw that number of uniform labels independently with replacement. At every required signed endpoint the fraction of labels serving it is $(15/4+o(1))/L$. The chance of missing any required endpoint is at most $2H_Y\exp[-(15/4+o(1))|{\rm draws}|/L]=o(1)$. Remove duplicate labels after selection. One can even demand coverage for every eligible offset in both directions before testing whether the anchor is prime, by testing its potential partner and the window condition. For that stronger demand one needs at least $(4/15-o(1))L$ labels if the positive direction is required for every $b\in[Y-H_Y,Y]$ coprime to 30. Indeed each label covers at most $(1+o(1))H_Y/L$ such integers by the short-interval PNT, out of $(4/15+o(1))H_Y$ candidates. The upper bound extends to this full interval, by the same union bound (with offset $v=Y-b$).

## What a pointwise lower bound would need to distinguish

Let $\nu=\prod_{\ell\mid30}(\ell-|\{0,2Y\bmod\ell\}|)$ with prime $\ell$, and $h=|I|$. Write $P=\bigcup P_n$, $M=\bigcup M_n$. From the individual endpoint coverage,
$$
 |\mathcal V|=\nu h/30+O(1),\qquad
 |P|,\ |M|=\frac{\nu h}{8L}+O_A(h/L^A).
$$
The two marginals count primes in $\nu$ reduced classes modulo 30 in reflected intervals of the same length. The exact excess over the independent count on $\mathcal V$ is therefore
$$
 |P\cap M|-\frac{|P|\,|M|}{|\mathcal V|}
     =r-\frac{30\nu}{64}\frac{h}{L^2}+O_A(h/L^A).             \tag{3}
$$
An isolated failure forces the whole negative term in (3). A fixed positive fractional improvement over this negative baseline at each $Y$ would suffice. In the four primality tests of (2), the two original forms $Y+v,Y-v$ still have proportional linear parts when $Y$ is fixed, for any number of free neighboring labels. This is the binary case excluded by the finite-complexity hypothesis for linear patterns in primes. [Green and Tao, *Linear equations in primes*](https://annals.math.princeton.edu/2010/171-3/p08)

If one demands **the same label** on the two sides, then at $v\in P_n\cap M_n$ the other two primes sum to $2Y$ as well, with signed offset $v-30n$. If this second offset is required to be in the original trimmed window in absolute value, it gives a *different* unordered representation. Equality with the original one would require $v=15n$ since $n>0$, and the neighboring offsets would both be zero. Thus the same-label test with this extra cutoff cannot certify a solitary trimmed pair, whereas (2) detects it. Without the extra cutoff the second pair can lie in the discarded inner part. The three squares label a total displacement. Primality at intermediate partial displacements is not asserted. A pointwise lower bound on $r$ is open here.

[Exact finite checks](CheckThreeSquareEndpointCover.py)
