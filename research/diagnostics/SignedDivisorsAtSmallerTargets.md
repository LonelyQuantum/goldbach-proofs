# Signed divisor pairs at a prescribed Goldbach target

Fix a sufficiently large integer $Y$ and put $N=2Y$, $L=\log Y$, $H=\lfloor Y^{2/3}\rfloor$, $T=\lfloor Y^{21/40}\rfloor$, $I=(Y+2T,Y+H]$, and $h=H-2T$. Count the larger summand $a$ once and write $b=N-a$. Let $\vartheta(n)=1_{\mathbb P}(n)\log n$, $w=L/(\log L)^2$, $W=\prod_{p\le w}p$. Write
$$
 G_N=\sum_{a\in I}\vartheta(a)\vartheta(b),\qquad
 \mathfrak S(n)=\prod_p\frac{1-\nu_p(n)/p}{(1-1/p)^2},
 \qquad \nu_p(n)=1+1_{p\nmid n}
$$
for even $n$. All sums over $a$ are over integers. This note gives a fixed-target reduction of the [D01 divisor expansion](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2589) and examines the information retained by the [W14 smaller-target records](SemiprimeRecordsAtSmallerTargets.md). The inputs for the reductions below are unconditional. Neither reduction supplies the required positive lower bound for $G_N$.

## Which pairs of long divisors can be removed at every target?

Take $R=Y^{1/7}$ and $Z=h\exp[-3(\log L)^2]$. Define
$$
 \mathcal T_N=
 \sum_{\substack{a\in I\\(ab,W)=1}}
 \ \sum_{\substack{d\mid a,\ e\mid b\\d,e>R,\ [d,e]>Z}}
       \mu(d)\mu(e)\log d\log e ,
$$
where $[d,e]$ is the least common multiple. Then for each fixed $A>0$, uniformly in $N$,
$$
 G_N=h\mathfrak S(N)+\mathcal T_N+O_A(hL^{-A}).                 \tag{1}
$$
Moreover, inside $d,e>R,\ [d,e]\le Z$, the sum of the absolute values of the **signed totals** on disjoint dyadic $d,e$ boxes is $O_A(hL^{-A})$. The modulus cutoff satisfies $Z=Y^{2/3-o(1)}$. Common factors $(d,e)>Y^\eta$ can also be removed from $\mathcal T_N$ at cost $O_{A,\eta}(hL^{-A})$, for every fixed $\eta>0$.

### The three terms with a short divisor

Put $A_R(n)=-\sum_{d\mid n,\ d\le R}\mu(d)\log d$ and $B_R(n)=\Lambda(n)-A_R(n)$. The identity $\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d$ gives
$$
 \Lambda(a)\Lambda(b)=\Lambda(a)A_R(b)+A_R(a)\Lambda(b)
                         -A_R(a)A_R(b)+B_R(a)B_R(b).
$$
All four terms are summed on the wheel $(ab,W)=1$. In terms with a $\Lambda$, replacing it by $\vartheta$ costs $O(Y^{1/2+o(1)})$ in each sum. There are $O(\sqrt Y\log Y)$ higher prime powers up to $2Y$, and each divisor weight is bounded by $\tau(n)\log(2Y)=Y^{o(1)}$. Every actual central prime pair passes the wheel.

In the first mixed term the prime $a$ is coprime to $N$ since $N/a$ cannot be an integer in the stated trimmed range. The reflected interval for prime $b$ has the same property. Sum over $d\le R$ dividing the opposite endpoint, with $(d,NW)=1$. Enforce the wheel at that endpoint by inclusion-exclusion over $j\mid W$, $(j,N)=1$. The prime then lies in the reduced class $N\bmod dj$. The modulus $dj$ uniquely determines the parts $d$ and $j$. The coefficients are bounded by $\log R$, and $RW=Y^{1/7+o(1)}$ lies below the short-interval distribution level $Y^{1/6-\delta}$ for a fixed small $\delta>0$. Thus each mixed term equals the following expression up to $O_A(hL^{-A})$:
$$
 h U_1\left(-\sum_{\substack{d\le R\\(d,NW)=1}}
        \frac{\mu(d)\log d}{\varphi(d)}\right),\qquad
 U_1=\prod_{p\mid W,\ p\nmid N}(1-1/(p-1)).
$$
This uses Timofeev's fixed-short-interval estimate for primes. Its formulation and range are given in [Koukoulopoulos, (1.1) and the paragraph following it](https://arxiv.org/pdf/1405.6592v2#page=1). See also [Timofeev's paper](https://doi.org/10.1070/IM1988v030n02ABEH001013).

For $A_R(a)A_R(b)$ the Chinese remainder theorem gives density $V/[d,e]$ if $(de,W)=1$ and $(d,e)\mid N$, and zero otherwise, where $V=\prod_{p\mid W}(1-\nu_p(N)/p)$. The rounding error is at most $O(W)$ per divisor pair. The total $O(WR^2L^2)$ is admissible. Denote the unweighted Dirichlet series of the mixed divisor sum and the double divisor sum (apart from $U_1,V$ and the logarithms) by $C(s)/\zeta(1+s)$ and $B(s,t)/(\zeta(1+s)\zeta(1+t))$, respectively. With $x=p^{-s},y=p^{-t}$ their correction factors are

| | Numerator of local correction | Denominator |
|---|---|---|
| $C$ | $1$ if $p\mid NW$, otherwise $1-x/(p-1)$ | $1-x/p$ |
| $B$ | $1$ if $p\mid W$, otherwise $1-(x+y)/p+1_{p\mid N}xy/p$ | $(1-x/p)(1-y/p)$ |

Here the $xy/p$ term uses the least common multiple when both divisors contain $p$. At $s=t=0$ a local multiplication gives $U_1C(0)=VB(0,0)=\mathfrak S(N)$, including $p=2$.

For uniformity in the sharp cutoffs, take $\sigma=1/\log L$. The absolute coefficient norms of $C,B$, weighted by $k^\sigma$ or $(kl)^\sigma$, are $L^{O(1)}$. The local norm in excess of 1 is $O(p^{-2+2\sigma})$ outside $NW$ and $O(p^{-1+2\sigma})$ on its prime factors. Split the latter sum at $L$. Below $L$, $p^{2\sigma}\le e^2$. Above $L$ there are $O(L/\log L)$ prime factors and $p^{-1+2\sigma}\le e^2/L$. This argument also bounds $\prod_{p\mid m}(1-p^{-1+\sigma})^{-1}$ for $m\le Y^{O(1)}$.

The classical zero-free-region prime number theorem for $\mu$ and partial summation give $\sum_{n\le x}\mu(n)/n=O_J(\log^{-J}x)$ and $-\sum_{n\le x}\mu(n)\log n/n=1+O_J(\log^{-J}x)$, using the simple zero $1/\zeta(1+s)=s+O(s^2)$ at $s=0$. After convolution with a correction coefficient indexed by $k\le\sqrt R$, the inner sum with $-\log(kn)$ and $n\le R/k$ is $1+O_J(L^{-J})$, with $J$ arbitrary. Indices exceeding $\sqrt R$ cost $O_J(L^{-J})$ by the weighted norm, even with the trivial $O(L^2)$ for each inner sum. Apply this in both variables for $B$. This proves that each of the three short terms, before its external sign, is $h\mathfrak S(N)+O_A(hL^{-A})$.

### Signed cancellation up to a least common multiple close to the window length

For compatible squarefree divisors, put $g=(d,e)\mid N$, $d=gu$, $e=gv$. Then $(u,v)=1$, $(uv,g)=1$, $(guv,W)=1$ and $[d,e]=guv$. On the corresponding progression the wheel forbids precisely $\nu_p(N)$ residue classes modulo each $p\mid W$. Truncating inclusion-exclusion at the consecutive orders $j,j+1$, $j=\lceil\log L\rceil$, bounds the count from both sides by
$$
 hV/(guv)+O_J\big((h/(guv))L^{-J}+\exp(2(\log L)^2)\big).
$$
Indeed the difference from the local product is at most a constant times $(2\sum_{p\le w}1/p)^j/j!$ in density. At most $(1+2w)^{j+2}$ progression rounding errors occur. There are $\ll Z L\sum_{g\mid N}1/g$ such compatible pairs up to $[d,e]\le Z$, and their reciprocal least-common-multiple sum is $\ll L^2\sum_{g\mid N}1/g$. These follow by summing over $uv\le Z/g$. Since $\sum_{g\mid N}1/g\ll L$ and the two logarithms cost $O(L^2)$, the total rounding and truncation errors are $O_A(hL^{-A})$.

The remaining density sum has sign $\mu(u)\mu(v)$ and denominator $guv$. The part $g>\sqrt R$ costs $hL^{O(1)}\tau(N)/\sqrt R$, which is negligible. Otherwise, for fixed $g,v$, the allowed $u$ lie in an interval above $R/g\ge\sqrt R$, below $Z/(gv)$, with $(u,gvW)=1$. Rectangular dyadic cuts still give an interval. Uniformly for $Y^\delta\ll U_0\le U_1\le Y^{O(1)}$, $m\le Y^{O(1)}$, $1\le g\le 2Y$ and fixed $\delta>0$,
$$
 \sum_{\substack{U_0<u\le U_1\\(u,m)=1}}\frac{\mu(u)\log(gu)}u
       \ll_{J,\delta} L^{-J}.
$$
To see this, convolve $\mu$ with the indicator of integers $k$ supported on primes dividing $m$; their convolution is $\mu(n)1_{(n,m)=1}$. For $k\le Y^{\delta/2}$ subtract the two Möbius prefixes. The constant in the log-weighted prefix cancels, including when $U_1$ is close to $U_0$. For larger $k$ apply the preceding weighted Euler product bound and $k^{-\sigma}\le Y^{-\delta\sigma/2}$. The other logarithm and the sums of $1/v$ and $1/g$ cost only powers of $L$. Summing over $O(L^2)$ dyadic boxes preserves any fixed log saving. This establishes (1).

Finally, any actual term with $g>Y^\eta$ has $g\mid N,a$. There are at most $\tau(N)(h/Y^\eta+1)$ such $a$, each with total absolute divisor weight $Y^{o(1)}$. This proves the stated large-gcd removal even beyond $Z$.

### A switched range strictly beyond the modulus cutoff

There is additional cancellation inside $\mathcal T_N$ itself. For fixed $\epsilon>0$ the total on
$$
  x=a/d,\qquad e>R,\qquad xe^2\le Y^{1/3-\epsilon}                   \tag{6}
$$
is $O_{A,\epsilon}(hL^{-A})$, including $e$ with factors in common with $N$. The same holds with the roles of $(a,d)$ and $(b,e)$ interchanged. In particular this covers $x\le Y^{1/100}$ and $R<e\le Y^{3/20}$. In (6), $x\le Y^{1/21}$, so $d\gg Y^{20/21}$ and even the smallest possible $[d,e]$ already exceeds $Z$. The estimate also applies on each rectangular dyadic restriction on $x,d,e$ inside (6), with its absolute signed totals summable over those boxes.

**Proof.** Write $a=xd$, so $(x,W)=(e,W)=1$ and $e\mid N-xd$. At primes dividing $N$ the wheel condition on $b$ follows from $(xd,W)=1$. Thus it suffices to enforce the wheel on $d$ and to enforce on $b$ only the primes of $W$ coprime to $N$. For squarefree $e$, write $e=e_0e_1$ with $e_0=(e,N)$ and $(e_1,N)=1$. Put $\eta=\min(\epsilon/8,1/200)$. If $e_0>Y^\eta$, then $e_0\mid a,N$, so at most $\tau(N)(hY^{-\eta}+1)$ endpoints occur and their total absolute weight is $O_A(hL^{-A})$. For $e_0\le Y^\eta$, set $r=e_0/(e_0,x)$. The congruence modulo $e_0$ is exactly $r\mid d$. Both $r$ and $e_0$ are coprime to $W$.

Write $d=rd'$. Use the exact convolution
$$
 \mu(d)1_{(d,W)=1}=\mu(r)\mu(d')1_{(d',Wr)=1}
   =\mu(r)\sum_{\substack{c\mid d'\\p\mid c\ \Rightarrow\ p\mid Wr}}\mu(d'/c).
$$
Discard $c>Y^\eta$ **before** expanding the wheel on $b$. Its error, summed even in absolute value across the terms thereby discarded, is $O_{A,\epsilon}(hL^{-A})$. Indeed any affected $a$ has a divisor $m\in[Y^\eta,Y^{2\eta}]$ supported on primes dividing $WN$: multiply the prime factors of $c$ one at a time to cross the threshold, using $r,w\le Y^\eta$. The number of these $a$ is at most
$$
 hY^{-\eta\sigma}\prod_{p\mid WN}(1-p^{-1+\sigma})^{-1}
     +O(Y^{2\eta})\ll_{J,\epsilon} hL^{-J}.
$$
The total absolute weight at a given $a$ is $O(L^2\tau(a)^2\tau(b))$. Its squared sum over $I$ is $O(hL^{O(1)})$ by Cauchy–Schwarz and Shiu's theorem for the fixed powers $\tau^8,\tau^4$. Cauchy–Schwarz once more shows that these exceptional $a$ have the asserted negligible weight. This step avoids any factor equal to the number of divisors of $W$ in the error bound.

For $c\le Y^\eta$ set $d=rct$ and expand the $b$ wheel over $j\mid W$ with $(j,N)=1$. The remaining condition on $t$ becomes
$$
  xrc t\equiv N\pmod {e_1j}.
$$
For fixed $e_0$ the modulus $q=e_1j$ determines $e$ and $j$ separately. It is coprime to $N$, so if $(xrc,q)>1$ there are no solutions. Otherwise this is one reduced class. For fixed $x,e_0,c$ the height is comparable to $X=Y/(xrc)$, the interval length is $y=h/(xrc)$, and $q\le Q=W(Y^{1/3-\epsilon}/x)^{1/2}$. Uniformly, $Q\sqrt X/y\le Y^{-\epsilon/2+\eta+o(1)}$ and $y\gg X^{5/8+\delta}$ for an absolute $\delta>0$ since $xrc\le Y^{1/21+1/100}$. Timofeev's Theorem 1 for $\mu$ gives a sum over $q\le Q$ of the maximal deviations from the coprime mean, bounded by $O_J(yL^{-J})$. Its bound is $O(L^{64}Q\sqrt X+yL^{-J})$ here. Use a constant multiple of $X$ in the theorem to cover the interval starts. The theorem permits all shorter subintervals. [Timofeev, Theorem 1, pp. 317–318](https://www.mathnet.ru/links/20531535b2e6f2f785c1c6e5939f97d8/im1297_eng.pdf#page=3)

The coprime mean of $\mu$ must also be estimated. For every subinterval $J'$ in the padded interval of length $2y$,
$$
 \left|\sum_{t\in J',\ (t,q)=1}\mu(t)\right|
 \le \sum_{m\mid q}\left|\sum_{t\in J',\ m\mid t}\mu(t)\right|
 \ll_F \tau(q)yL^{-F}.
$$
The last bound uses the **maximal arithmetic-progression** norm in Matomäki–Shao–Tao–Teräväinen (1.4), (1.5), with constant test function. It is absolute relative to the padded interval length and holds for every progression inside it. After division by $\varphi(q)$, summing over $q$ loses only powers of $L$, since $\sum_{q\le Q}\tau(q)/\varphi(q)\ll L^{O(1)}$. The factor $\mu(e)\mu(j)\log e$ costs at most $O(L)$ in the summed errors. Partial summation with $\log(rct)$ costs another $O(L)$; dyadic restrictions on $d$ just shorten the interval. Finally $\sum_c1/c\ll L$, and
$$
 \sum_{x\le Y^{1/21}}\frac1x\sum_{e_0\mid N}\frac{(e_0,x)}{e_0}
 \le (1+L)\sum_{e_0\mid N}\frac{\tau(e_0)}{e_0}\ll L^{O(1)}.
$$
Expand $(e_0,x)=\sum_{v\mid(e_0,x)}\varphi(v)$ for the inequality. For the last bound one may even sum $\tau(n)/n$ over all $n\le N$. These reciprocal sums pay for every $y=h/(xrc)$ in the error. This proves (6). [Maximal norm and Theorem 1.1(i)](https://arxiv.org/pdf/2204.03754v4#page=3) · [Shiu's short-interval theorem](https://doi.org/10.1515/crll.1980.313.161)

## How much information does the smaller even target retain?

Let $D=\lfloor Y^{16/25}\rfloor$. For odd $a\in I$ and even $M$, put $k=(3M-N)/2$. Take only $2\le k\le2D$. Let $K_M(a)$ count $1\le s,t\le D$, $s+t=k$, for which $q=(b+2s)/3$ and $u=(a+2t)/3$ are primes and
$2\lfloor (M/2)^{21/40}\rfloor<|q-M/2|\le\lfloor (M/2)^{2/3}\rfloor$. Put
$$
 \ell_k=\min(D,k-1)-\max(1,k-D)+1,\qquad
 v_M=\frac{2\ell_k}{3\log^2(Y/3)}\mathfrak S(M).
$$
Then
$$
 \sup_{a\in I,\ a\ {\rm odd}}\sum_M|K_M(a)-v_M|\ll_A D^2L^{-A}.       \tag{2}
$$
For any fixed function $f$ on the odd $a$ in $I$, the triangle inequality therefore gives
$$
 \sum_M\left|\sum_a f(a)K_M(a)-v_M\sum_a f(a)\right|
       \ll_A D^2 L^{-A}\sum_a |f(a)| .                               \tag{3}
$$
All implied constants are independent of $f$. Equation (3) controls any final weighting of the smaller targets by coefficients of magnitude at most one. It supplies no uniform error of this size for an individual $M$, and does not estimate a weight chosen jointly in $a,M$.

**Proof.** For fixed $a,M$, $s$ runs through a contiguous integer interval of length $\ell_k$. Every odd prime $q$ in the corresponding ordinary interval for $q$ gives exactly one integer $s=(3q-b)/2$ and $t=k-s$, and $u=M-q$. In particular the ordinary interval length is $2\ell_k/3+O(1)$, with no further progression restriction on the primes. The parity density is already in $\mathfrak S(M)$. The outer trim is automatic since $|q-M/2|\le(H+D)/3<\lfloor(M/2)^{2/3}\rfloor$ for sufficiently large $Y$. The inner trim costs $O(Y^{21/40}+1)$ choices per $M$.

Fix the desired exponent $A$ and split $[1,D]$ into $\asymp L^B$ consecutive cells of comparable lengths, with $B>A+10$. For each $M$ retain the whole cells inside its $s$ interval. At most two partial cells are lost, costing $O(D/L^B+1)$ individually in the prime count. The corresponding loss in the proposed main term is $O((D/L^B+1)\mathfrak S(M)/\log^2(Y/3))$, where $\mathfrak S(M)\ll\log L$. A fixed whole cell maps to an ordinary $q$ interval $J$ of length $2|\mathrm{cell}|/3+O(1)$, independent of $M$. Take one ordinary interval $J'$ of length $\asymp D$ containing all $M-q$ under consideration for this $a$ and cell. Its endpoints, like those of $J$, are $Y/3+O(H)$.

On these intervals replace $\vartheta(n)$ by
$$
 P_z(n)=1_{(n,\prod_{p<z}p)=1}\prod_{p<z}(1-1/p)^{-1},
 \qquad z=\exp((\log(Y/3))^{1/10}).
$$
The Fourier supremum of the difference on either interval is $\ll_J D L^{-J}$ for every fixed exponent $J$ (here the subscript denotes the exponent). Both lengths exceed $Y^{5/8+\delta}$ for a fixed $\delta>0$. Apply the linear-phase case of Matomäki–Shao–Tao–Teräväinen, Theorem 1.1(ii), first with its own starting height in $z$. Changing that height to $Y/3$ changes $z$ by less than one, by differentiation. If a prime crosses the cutoff, its multiples and the change in normalization cost $O((D/z+1)L)$ in absolute sum. Higher prime powers cost $O(\sqrt Y L^2)$. [Published article](https://doi.org/10.1017/fmp.2023.28) · [Definitions (1.1), (1.4) and estimate (1.6)](https://arxiv.org/pdf/2204.03754v4#page=3)

Convolve the two restricted sequences additively. By Parseval, replacing the first and then the second factor costs $\ll_J D^{3/2}L^{-J}$ in $\ell^2$ over the integer targets: multiply the preceding Fourier supremum by the $\ell^2$ norm $O(\sqrt D L)$ of the companion sequence, increasing $J$ first. On $O(D)$ targets this costs $\ll_J D^2L^{-J}$ in $\ell^1$. Restricting the resulting absolute errors to targets containing the cell can only decrease this bound.

For the model convolution, $M-J\subset J'$ on these targets. Sieve $q\in J$ against $0,M\bmod p$ for all $p<z$. Bonferroni at the consecutive orders $j,j+1$ with $j=\lfloor L^{1/3}\rfloor$ gives $|J|\mathfrak S(M)+O_J(DL^{-J})$ after normalization, uniformly in $M$. The unsummed density tail is bounded by a constant times $(2\sum_{p<z}1/p)^j/j!$, and the rounding error by $(1+2z)^{j+2}=Y^{o(1)}$. The normalization is $O(L^2)$. The omitted Euler factors for $p\ge z$ have relative error $O(L/z)$, by summing $1/p^2$ generically and $1/p$ over prime factors of $M$. Returning from prime logarithms to counts uses $\log q,\log u=\log(Y/3)+O(H/Y)$. Choose the Fourier and sieve error exponents larger than $A+B+10$ before summing the cells. The inner trim, cell endpoints and partial cells now fit the stated error. This proves (2).

### Consequences and the missing sign

* In the interior $4D/5\le k\le6D/5$, $v_M\gg D/L^2$. With $f(a)=1_{\mathbb P}(a)1_{\mathbb P}(b)$, for every fixed $A,C>0$ all but $O_{A,C}(D/L^A)$ smaller targets have $(1+O(L^{-C}))v_M r_N$ compatible records, where $r_N$ counts original pairs in $I$. Apply (3) with an appropriately larger exponent. The assertion holds even for one original pair. With $r_N=0$ every record of this type vanishes identically.
* For one signed divisor box let $f$ be its contribution at $a$, including the wheel. Then $\sum_a|f(a)|\ll hL^5$. Indeed $|f(a)|\le L^2 O(\tau(a)\tau(b))$. Use Cauchy–Schwarz and the short-interval upper bound for $\sum\tau^2$ on each reflected interval, which is $O(hL^3)$ by Shiu's theorem ($q=1$, local prime value $4$). Hence each canceled box above contributes $O_{A,C}(hD/L^C)$ on all but $O_{A,C}(D/L^A)$ smaller targets. Any predetermined family of $O(L^2)$ such boxes can use a common exceptional set by increasing the exponents. The $\ell^1$ estimate (3) also accounts for the exceptional targets in bounded reweightings. [Shiu, Theorem 1](https://doi.org/10.1515/crll.1980.313.161)
* If the original central window fails, (1) forces $\mathcal T_N=-h\mathfrak S(N)+O_A(hL^{-A})$. The same holds after removing (6) and its disjoint reflection. At least one of the $O(L^2)$ dyadic $d,e$ boxes in that remainder then has signed total $\le-c h\mathfrak S(N)/L^2$ for an absolute $c>0$. The positive main term would survive if the remainder were $\ge-(1-\delta)h\mathfrak S(N)$ for a fixed $\delta>0$ at each target. None of these bounds supplies this inequality. Taking complementary factors $x=a/d$ and $y=b/e$ leaves the exact equation $xd+ye=N$. Even $x=y=1$ retains $\mu(a)\mu(N-a)$ on the wheel, outside both switched ranges.

### The size of the increase from keeping the smaller targets separate

Use both orientations as in the [earlier covariance estimate (5)](SemiprimeRecordsAtSmallerTargets.md#a-positive-reference-term-for-the-missing-reverse-implication). Let $n_0$ count oriented starting endpoints on the wheel and $s_0$ those with $a$ prime. At each $M$ let $n_M$ and $S_M$ be the corresponding labeled counts after imposing the two small primes and their trim. The symmetry $K_M(a)=K_M(N-a)$ extends (2) to both orientations. Set $F(s,n)=s^2/n$ for $0\le s\le n$, with $F(0,0)=0$. On this cone,
$$
 |F(s,n)-F(s',n')|\le 2|s-s'|+|n-n'|
$$
by the partial derivative bounds and continuity at the origin. Apply (3) to the wheel indicator and the single prime mark. By homogeneity and the last inequality, both $\sum_M F(S_M,n_M)$ and $F(\sum_M S_M,\sum_M n_M)$ differ from $F(s_0,n_0)\sum_M v_M$ by $O_A(hD^2L^{-A})$. Hence
$$
 0\le \sum_M\frac{S_M^2}{n_M}-
             \frac{(\sum_M S_M)^2}{\sum_M n_M}
       \ll_A hD^2L^{-A},                                             \tag{4}
$$
omitting empty bins. Nonnegativity is Cauchy–Schwarz. The previous lower bound for the positive reference term can also be made two-sided. With $\lambda=2D/(3\log(Y/3))$, one odd starting endpoint has total $\lambda^2+O_A(D^2L^{-A})$ records by the one-dimensional prime estimate and the inner trim, so (2) gives the same estimate for $\sum_M v_M$. Also $n_0=2hV+O(W)$ and $s_0=2hU_1/L+O_A(hL^{-A})$ by the wheel calculation above, freezing the prime logarithm at $L$. Since $V^{-1}\ll(\log w)^2$, we obtain
$$
 \sum_M\frac{S_M^2}{n_M}=\frac{2h\lambda^2}{L^2}\frac{U_1^2}{V}
                              +O_A(hD^2L^{-A}).                       \tag{5}
$$
The finite product $U_1^2/V$ is needed at this accuracy. Its ratio to $\mathfrak S(N)$ tends to one uniformly as in the earlier note. In particular (4) rules out gaining a fixed proportion of the reference in (5) just by keeping the $M$ bins separate.

At $Y=1009^2$, all 933 even targets with $4D/5\le k\le6D/5$ carry all 52 original central pairs. Across these $933\cdot52$ incidences, a given pair has between 4 and 101 compatible trimmed records at a given target. The companion [exact finite checker](CheckSignedDivisorTransfer.py) also tests the divisor partition, local factors and label map. The uniform estimates above use the cited analytic inputs.
