# Isolated failures of the signed minor-arc bound in a density-one subset of the primes

Can a linear deficit at one target $2p^2$ be propagated to nearby prime-square targets from their representation counts and small major arcs? There is an obstruction even when the weights are ordinary logarithms supported entirely on genuine primes. The construction below changes the set of primes used as summands. A separate identity at the end concerns the original primes.

Write $w_B(x)=\mathbf 1_{x\in B}\log x$ on positive integers and zero elsewhere, for $B\subseteq\mathbb P$. Put $S_{B,m}(t)=\sum_{x\le m}w_B(x)e(xt)$ with $e(t)=\exp(2\pi it)$. Let $J_B(m)$ and $I_B(m)$ be the signed integrals of $S_{B,m}(t)^2e(-mt)$ over the desk's major and minor arcs. The major arcs have radii $Q_m/(qm)$ around reduced $a/q$ for $q\le Q_m=\lfloor\log_2(m+2)\rfloor^2$. The full coefficient is $R_B(m)=\sum_x w_B(x)w_B(m-x)=J_B(m)+I_B(m)$. All these coefficients are real by reflection. [Desk conventions and the fixed-mask question](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/453)

**Claim.** There is a single set $B\subset\mathbb P$ of relative density one, also of relative density one in the primes of every fixed reduced residue class, and an infinite sequence $h_j=2p_j^2$ with the following properties.

- $R_B(h_j)=0$ and $I_B(h_j)/h_j\to-2C_2$, where $C_2=\prod_{\ell>2,\ \ell\ {\rm prime}}(1-1/(\ell-1)^2)$. The selected centers have $R_{\mathbb P}(h_j)/h_j\to 2C_2$.
- For every fixed $K>0$, eventually the $\lfloor(\log p_j)^K\rfloor$ preceding and following **consecutive prime indices** $q$ all have $|I_B(2q^2)|/(2q^2)=o(1)$ uniformly across that block. In particular they all have representations in $B+B$.
- For every fixed $0<\eta<1$, at **all** even $m\notin\{h_j\}$,
$$
 |R_B(m)-R_{\mathbb P}(m)|+|I_B(m)-I_{\mathbb P}(m)|
 \ll_\eta m/(\log m)^{1-\eta}
$$
as $m\to\infty$. The same error controls $|J_B(m)-J_{\mathbb P}(m)|$ even at the selected centers.

These are paper deductions from the published restriction estimate of Green and Tao and the polynomial Goldbach estimate of Perelli, together with the prior major-arc comparison. Alsetri and Shao, Theorem 1.2, give related conditions for a dense subset of the primes to cover almost all evens. The question here concerns the signed coefficient at an individual center and its neighbors. [Green–Tao, Theorem 1.1 and Proposition 4.2](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.538.pdf) · [Perelli, Corollary 1](https://doi.org/10.4171/RMI/205) · [Alsetri–Shao, Theorem 1.2](https://arxiv.org/html/2405.18576v2)

## Removing one endpoint per pair

Start with any set $\mathcal H$ of targets $h=2p^2$ with odd prime $p$ and $L(y)=|\mathcal H\cap[1,y]|\ll\log\log(3y)$. For each $h$ delete all $x\in\mathbb P$ with $x\ge h/2$ and $h-x\in\mathbb P$. Let $B$ be the primes surviving all deletions. Every unordered representation of $h$ loses its larger endpoint. Distinct representations of one fixed target are disjoint sets of endpoints. This deletes the minimum possible number for that single target. The diagonal $h/2=p^2$ is composite. For a sum cut off at $m$, only $h\le2m$ matter.

Here are the uniform sieve inputs used below. At ambient length $M=2m$ the coefficients of the forms $x,h-x,m-x$ all have modulus at most $M$. For a product of $k$ such forms with distinct roots over the rationals and admissible at every prime, let $\mathfrak S_F$ be the usual product of $(1-\nu_\ell/\ell)/(1-1/\ell)^k$, with $\nu_\ell$ the number of distinct roots modulo $\ell$. For every fixed $r>2$ the exponential sum of any subset of the simultaneous prime values, with coefficients of modulus at most one, has $L^r(\mathbb T)$ norm $\ll_{k,r}\mathfrak S_F M^{1-1/r}/(\log M)^k$ in our applications. Indeed, multiply the test coefficients in the proof of Theorem 1.1 by these bounded weights in (4.8). The exceptional sites having a prime form value at most $M^{1/20}$ contribute $O_k(M^{1/20})$, absorbed here since admissible unit-slope $k$-tuples have $\mathfrak S_F\gg_k1$. A uniform count $\ll_{k,r}\mathfrak S_F M/(\log M)^k$ follows by taking coefficients one and integrating over $|t|\le1/(10M)$, where every summand has real part at least $1/2$. This establishes uniformity also when the forms depend on $m$. [Green–Tao, Theorem 1.1, (4.8) and its application on pp. 159–160](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.538.pdf)

For the two forms $x,h-x$ the singular series is $2C_2(p-1)/(p-2)\ll1$. Hence the number of deletions below $m$ is $O(L(2m)m/\log^2 m)$. The prime number theorem, also in each fixed reduced class, proves the asserted density.

## Changes at every frequency

If $m\ne h$, any lost ordered representation of $m$ has at least one deleted endpoint $x$. Assigning it to one possible $h$ and allowing both orientations bounds the loss by $2\log^2(2m)$ times the sum over $h\le2m$ in $\mathcal H$ of the counts of positive prime triples $x,h-x,m-x$. For the three forms the determinant product has absolute value $\Delta=|hm(h-m)|>0$. For a prime $\ell\nmid\Delta$ the three roots are distinct, and the local factor is at most one. At $\ell\mid\Delta$ it is at most $(1-1/\ell)^{-2}$. Thus in the admissible case $\mathfrak S_F\le(\Delta/\varphi(\Delta))^2\ll(\log\log(3m))^2$, since $\Delta\ll m^3$. The last bound follows from Mertens' product up to $\log^2(3m)$, with a bounded contribution from the remaining prime divisors. In the inadmissible case a prime $\ell\le3$ divides one of the forms at every $x$, so a positive prime triple requires a form equal to $\ell$ and there are at most three choices of $x$. This gives
$$
 0\le R_{\mathbb P}(m)-R_B(m)\ll m L(2m)(\log\log(3m))^2/\log m
 \qquad(m\notin\mathcal H).
$$

Let $D_m=S_{\mathbb P,m}-S_{B,m}$. Partition the deleted primes up to $m$ by the least $h$ responsible for their deletion. Each part is supported on prime values of $x,h-x$. Apply the two-form restriction bound to each part with coefficients $\log x/\log(2m)$ and sum. The one-form bound applies to both original and retained primes, giving
$$
 \|D_m\|_r\ll_r L(2m)m^{1-1/r}/\log m,\qquad
 \|S_{\mathbb P,m}+S_{B,m}\|_r\ll_r m^{1-1/r}.
$$
The arc measure is $O(Q_m^2/m)=O(\log^4 m/m)$ by summing the lengths. Apply Hölder to the product $D_m(S_{\mathbb P,m}+S_{B,m})$ on this set. For every $m$, including $m\in\mathcal H$, the change of signed major coefficient is bounded by
$$
  O_r\!\left(m L(2m)(\log m)^{-1+4(1-2/r)}\right).
$$
Choose fixed $r>2$ sufficiently close to two, and absorb $L(2m)$ into the remaining logarithmic allowance. Subtract the major from the full coefficient to obtain the stated off-center minor estimate. Each application uses exactly the cutoff and mask of the target being estimated.

## Choosing centers with good neighbors

For true primes, at every $h=2p^2$ the previous comparison gives $J_{\mathbb P}(h)/h=2C_2+O(1/p+\log\log h/\log^2 h)$. On prime indices $P\le q\le2P$, the bound $|I_{\mathbb P}(2q^2)|/(2q^2)\le1/\log P$ fails at most $O_D(P/\log^D P)$ times for every fixed $D$. This follows from Perelli's Corollary 1 for $F(u)=2u^2$ and the major-arc comparison, using the full prime-log coefficient after removing proper prime powers. [Pointwise major comparison and polynomial transfer](https://github.com/LonelyQuantum/goldbach-proofs/blob/32636251f4b1dcbf339bcc9ee9cfecf17e72a363/research/diagnostics/PrimeSquareMinorArcExceptions.md) · [Perelli, pp. 477–478](https://content.ems.press/assets/public/full-texts/serials/rmi/12/2/5197/online/10.4171-rmi-205.pdf)

At stage $j$ put $b=\lceil(\log(2P))^j\rceil$ and take $D=j+4$. Discard the first and last $b$ primes of this block, and every center within $b$ prime ranks of a bad index. At most $2b+(2b+1)O_D(P/\log^D P)=o_j(P/\log P)$ centers are lost. Choose $P=P_j$ sufficiently large at each stage, with $P_{j+1}>4P_j^2$ and $P_1$ large. There is at least one remaining prime $p_j$. These blocks are disjoint and $L(y)\ll\log\log(3y)$ for the chosen targets. Every neighbor in the retained block, other than the center, lies outside $\mathcal H$. The off-center estimate with $\eta=1/2$ now makes its normalized minor integral $o(1)$ uniformly. Its normalized major integral tends to $2C_2$. At the center $R_B(h_j)=0$, so $I_B(h_j)=-J_B(h_j)=-(2C_2+o(1))h_j$.

One can also read off the cost of destroying the true center. There are $(C_2+o(1))h_j/\log^2 h_j$ unordered representations of $h_j$. To see this, use $R_{\mathbb P}(h_j)=(2C_2+o(1))h_j$ from the choice of centers. The ordered pairs with an endpoint below $h_j/\log^4 h_j$ have count $O(h_j/\log^4 h_j)$ and total weight $o(h_j)$. On the remainder both logarithms are $(1+o(1))\log h_j$. Divide by two to pass to unordered pairs. The minimum number of deletions is exactly the number of unordered pairs. In this construction all their larger endpoints lie in $[h_j/2,h_j]$, so the missing logarithmic weight there is at least $(C_2+o(1))h_j/\log h_j$. A prime number theorem with absolute error $O(h_j/\log^2 h_j)$ on that interval detects the deletion even though the relative prime density tends to one.

## What shared endpoints measure for the actual primes

With $w=w_{\mathbb P}$ define $T(h,m)=\sum_x w(x)w(h-x)w(m-x)$ and $\vartheta(t)=\sum_{\ell\le t,\ \ell\ {\rm prime}}\log\ell$. For every even $h>4$ and integer $H\ge1$, interchanging the two finite sums gives
$$
 \sum_{\substack{h<m\le h+H\\2\mid m}}T(h,m)
 =\sum_{x=1}^{h-1} w(x)w(h-x)\,[\vartheta(h-x+H)-\vartheta(h-x)].
$$
Both endpoints of a contributing representation of $h$ are odd. Since $m-x>h-x\ge3$, every eligible prime $m-x$ is odd and its corresponding $m$ is even. This accounts for the absence of a parity factor.

Uniformly for $h^{7/12+\varepsilon}\le H\le h$ and fixed $A,\varepsilon>0$, each bracket with nonzero weight is $H+O_{A,\varepsilon}(H/\log^A h)$. For $t=h-x\ge H$ use the short-interval theorem with modulus one and remove proper powers, of total weight $O(\sqrt{2h}\log^2(2h))$. For $t<H$ use the classical prime number theorem with logarithmic error at both endpoints, bounding the absolute error uniformly for arguments up to $2H$. Consequently the average obtained by dividing the left side by $H$ equals $R_{\mathbb P}(h)(1+O_{A,\varepsilon}(\log^{-A}h))$, also when $R_{\mathbb P}(h)=0$. A uniform lower bound for this averaged overlap of size $\gg h$ would already give a uniform lower bound of the same order for the original center. Abundant representations of the separate neighboring targets control a different sum. [Baier–Zhao, Lemma 6](https://arxiv.org/pdf/math/0701577v6#page=5)

## Exact finite check

For $h=2\cdot101^2=20402$ integer sieving removes 172 larger endpoints, one for each unordered representation. The table counts ordered pairs at $m=2q^2$.

| Prime index $q$ | All primes | After deletion |
|---:|---:|---:|
| 89 | 284 | 192 |
| 97 | 322 | 234 |
| 101 | 344 | 0 |
| 103 | 352 | 266 |
| 107 | 368 | 292 |

For all 257 even $m$ with $|m-h|\le256$, enumerating prime complements verified that the count lost equals twice the number with first endpoint deleted, minus the number with both endpoints deleted. An independent integer-weight check of the double-sum identity used $H=127$ and the weight $x$ at each prime $x$ in place of its logarithm, including in the corresponding prefix sum. Both sides were $3096075599699336$. These checks only concern finite combinatorial identities.

The set $B$ omits genuine primes. The construction tests whether density one, closeness of the major coefficients on the linear scale, and many good neighboring targets together force propagation. A proof for the full primes can still exploit arithmetic information that the deletion destroys.
