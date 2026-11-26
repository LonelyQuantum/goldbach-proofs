# How much of a fixed Goldbach deficit can one divisor scale carry?

Fix a sufficiently large integer $Y$, $N=2Y$, $L=\log Y$, $H=\lfloor Y^{2/3}\rfloor$, $T=\lfloor Y^{21/40}\rfloor$, $I=(Y+2T,Y+H]$ and $h=H-2T$. An ordered endpoint $a\in I$ is the larger summand; $b=N-a$. Write $\vartheta(n)=1_{\mathbb P}(n)\log n$ and $G_N=\sum_{a\in I}\vartheta(a)\vartheta(b)$. The even-target singular series is $\mathfrak S(N)=\prod_p(1-\nu_p/p)/(1-1/p)^2$, with $\nu_p=1+1_{p\nmid N}$. The question concerns the signed divisor expansion in [D01](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2589).

Take $R=Y^{1/7}$ and strengthen the sieve on the endpoints to
$$
 z=\exp\!\left(\frac{L}{(\log L)^3}\right),\qquad P=\prod_{p\le z}p.
$$
Call an integer rough if it is coprime to $P$. No actual high prime pair is lost. The values of individual signed divisor sums do change when the sieve changes.

**Fixed-target strip bound.** There is an absolute constant $C$ such that for every real $D\ge1$,
$$
 \sum_{\substack{a\in I\\(ab,P)=1}}
 \sum_{\substack{d\mid a,\ 1<d<a\\D<d\le2D}}
 \sum_{e\mid b} |\mu(d)\mu(e)|\log d\,\log e
 \ \ll\ h\mathfrak S(N)\frac{(\log L)^C}{L}.                         \tag{1}
$$
It also holds on interchanging $a,b$. Both the center and the strip are arbitrary. In particular the entire balanced box $d,e\asymp\sqrt Y$ is $o(h\mathfrak S(N))$ even in absolute value. Any $O(L^{1-\delta})$ chosen proper-divisor strips may be discarded for a fixed $\delta>0$. The whole divisor $d=a$ is excluded from (1). No claim sums this upper bound over all $O(L)$ strips with a saving.

## Recovering the main term after strengthening the sieve

Put $J=\lceil(\log L)^{3/2}\rceil$ and $Z_*=h\exp[-4L/(\log L)^{3/2}]$. With the same definitions of the short divisor sum and singular series as in the [preceding note](SignedDivisorsAtSmallerTargets.md), one has, for each $A>0$,
$$
 G_N=h\mathfrak S(N)+
 \sum_{\substack{a\in I\\(ab,P)=1}}\ 
 \sum_{\substack{d\mid a,\ e\mid b\\ d,e>R,\ [d,e]>Z_*}}
 \mu(d)\mu(e)\log d\log e+O_A(hL^{-A}).                             \tag{2}
$$
Here $[d,e]$ denotes the least common multiple. The earlier switched exclusions $x e^2\le Y^{1/3-\epsilon}$ and $y d^2\le Y^{1/3-\epsilon}$, for $x=a/d$, $y=b/e$, may still be made with $O_{A,\epsilon}(hL^{-A})$ error for fixed $\epsilon>0$. The cutoff $Z_*$ in (2) is smaller than the preceding note's cutoff for its weaker sieve.

These claims require controlling the **truncated** inclusion-exclusion for $P$. The full product $P$ exceeds the available distribution level. Here are the details.

1. For a subset of primes of $P$, truncate the inclusion-exclusion for divisibility of $n$ at order $J$. It equals the exact indicator unless $\omega(n)>J$, and its absolute value is at most $\tau(n)$. In either endpoint interval the count with $\omega(n)>J$ is $O(hL^{C_0}2^{-J})$, since $2^{\omega(n)}\le\tau(n)$. This still costs $O_A(hL^{-A})$ in any of the sums with a fixed product of powers of $\tau(a),\tau(b),L$, by Cauchy–Schwarz and the short-interval moment bounds $\sum_{n\in I}\tau(n)^k\ll_k hL^{C_k}$, also on the reflection of $I$. These follow from Shiu's theorem with modulus one; the short-divisor argument below also proves the bounds. Every modulus introduced by a truncated wheel is at most $z^{J+1}=Y^{o(1)}$. In the corresponding local densities the omitted tail is bounded by a constant times $(O(\log L))^J/J!$, smaller than $L^{-A}$ for every fixed $A$. Here $\sum_{p\le z}1/p$ and $\sum_{2<p\le z}1/(p-1)$ are $O(\log L)$.
2. Let $A_R(n)=-\sum_{d\mid n,\ d\le R}\mu(d)\log d$ and $B_R=\Lambda-A_R$. Use $\Lambda\Lambda=\Lambda A_R+A_R\Lambda-A_RA_R+B_RB_R$, with the two factors evaluated at $a,b$. Higher prime powers cost $Y^{1/2+o(1)}$. In a mixed term the actual prime passes the sieve and cannot divide $N$ in these intervals. Keep only rough $d$ coprime to $N$ at the opposite end, then apply step 1 there with primes not dividing $N$. Each modulus $dj$ has a unique decomposition into the rough part $d$ and the small-prime part $j$. The largest modulus is $Rz^{J+1}=Y^{1/7+o(1)}$, within Timofeev's fixed-interval prime estimate. The mixed main term is $hU_1(-\sum_{d\le R,(d,NP)=1}\mu(d)\log d/\varphi(d))$, where $U_1=\prod_{p\le z,\ p\nmid N}(1-1/(p-1))$. For $A_RA_R$, on each compatible progression of modulus $[d,e]$, the two-root sieve has density $V=\prod_{p\le z}(1-\nu_p/p)$. Bonferroni at orders $J,J+1$ gives an error $O_A(hL^{-A}/[d,e]+(1+2z)^{J+2})$ per compatible pair. This is summable for $d,e\le R$, increasing $A$ to pay for logarithms and reciprocal moduli. [Fixed-interval distribution, (1.1)](https://arxiv.org/pdf/1405.6592v2#page=1)
3. The two Euler corrections in the preceding note have the same local factors with $P$ in place of the former wheel. Use the absolute coefficient norm at $\sigma=1/\log z$. Primes $p\le z$ satisfy $p^{2\sigma}\le e^2$ and $\sum_{p\le z}1/p=O(\log L)$. For primes $p>z$ dividing any additional integer $m\le Y^{O(1)}$, the sum of $p^{-1+2\sigma}$ is $O(L/z)$; there are $O(L)$ of them. Generic local errors are $O(p^{-2+2\sigma})$. Thus the norms and $\prod_{p\mid mP}(1-p^{-1+\sigma})^{-1}$ are $L^{O(1)}$. A cutoff $Y^\alpha$ at any fixed $\alpha>0$ gives the tail factor $\exp(-\alpha(\log L)^3)$. The zero-free-region Möbius prefix estimates used in the preceding note now evaluate each of the two mixed terms and the short-short term as $h\mathfrak S(N)+O_A(hL^{-A})$ before the external signs. In particular the product of the short-short density and its Euler correction recovers the full singular series exactly at zero.
4. For $d,e>R$ and $[d,e]\le Z_*$ write $d=gu,e=gv$ with $g=(d,e)\mid N$. The number of compatible pairs is $\ll Z_*L\sum_{g\mid N}1/g$. Their reciprocal modulus sum is $\ll L^2\sum_{g\mid N}1/g$. Since $(1+2z)^{J+2}\le\exp(2L/(\log L)^{3/2})$ for large $Y$, the rounding and density errors in step 2 are admissible. In the main density $g>\sqrt R$ contributes $O(hL^{O(1)}\tau(N)/\sqrt R)$. Otherwise the $u$ sum lies in an interval above $\sqrt R$, with $(u,gvP)=1$. Convolve $\mu$ with integers supported on primes of $gvP$ to remove this coprimality restriction. The norm in step 3 bounds the large convolution indices; subtracting the two log-weighted Möbius prefixes cancels their constant. The $u$ sum with weight $\mu(u)\log(gu)/u$ is $O_A(L^{-A})$. Summation over $g,v$ proves (2).
5. For the switched exclusions, replace just the wheel on $b$ at primes not dividing $N$ by its order-$J$ expansion **before** switching. Step 1 pays for this replacement on the original divisors. In the proof of the [switched estimate (6)](SignedDivisorsAtSmallerTargets.md#a-switched-range-strictly-beyond-the-modulus-cutoff), removal of the large smooth convolution index $c$ can now cost an additional factor $\tau(b)$ from that expansion. Its exceptional-set bound still saves every log power by step 3, including primes of $r\mid N$. The subsequent progression modulus $q=e_1j$ still determines both factors and is at most $(Y^{1/3-\epsilon}/x)^{1/2}z^{J+1}$. This is the same power range in Timofeev's Möbius estimate. The preceding control of its coprime mean via the maximal progression norm applies without change. [Timofeev, Theorem 1](https://doi.org/10.1070/IM1988v030n02ABEH001013) · [Matomäki–Shao–Tao–Teräväinen, (1.4)–(1.5)](https://arxiv.org/pdf/2204.03754v4#page=3)

## Proof of the strip bound

On the rough endpoints, we may remove every $a$ for which $a$ or $b$ is nonsquarefree, or $(a,N)>1$, at a cost $O_A(hL^{-A})$ even in absolute divisor weight. In the first case some $p>z$ has $p^2\mid a$ or $b$. Counting multiples costs $O(h/z+\sqrt Y)$. In the second case some $p>z$ divides $a,N$; summing over these primes costs $O(L(h/z+1))$. On this sifted set $\tau(a)\tau(b)\le\exp(O((\log L)^3))$, since each factor exceeds $z$. These losses remain negligible. The resulting $a,b$ are coprime and squarefree.

For a proper divisor $d$ in $(D,2D]$ put $u=\min(d,a/d)$ and $v=a/u$. Then $1<u\le\sqrt{2Y}$, and $u$ belongs either to $(D,2D]$ or to $[Y/(2D),2Y/D]$. These are at most two intervals of bounded ratio; each $a,u$ gives at most two choices of $d$. The shifted lower endpoint $b$ is treated identically using $Y/2<b<2Y$, which only changes the fixed ratio. The two logarithms in (1) cost $O(L^2)$, and the sum over $e$ costs at most $\tau(b)$.

Here is an elementary short-divisor majorant to retain the sieve saving while paying for $\tau(b)$. Fix $\kappa=1/48$. For squarefree $b\le2Y$,
$$
 \tau(b)\le C_1\sum_{\substack{m\mid b\\m\le Y^\kappa}} C_1^{\omega(m)}.       \tag{3}
$$
There are a bounded number of prime factors above $Y^{\kappa/2}$. Partition the other factors into groups of product at most $Y^\kappa$, starting a new group when adding the next factor would exceed this threshold. Every completed group then has product $>Y^{\kappa/2}$, so there are at most $K=O(1/\kappa)$ groups. The largest divisor count of these group products raised to $K$ bounds the product of all their divisor counts. This proves (3) after absorbing the large primes. For nonsquarefree $n$ the same grouping of prime factors with repetition and submultiplicativity gives $\tau(n)^k\ll_k \sum_{m\mid n,\ m\le Y^\kappa}\tau(m)^{O_k(1)}$. Summing the latter over an interval of length $h$ gives the moment estimate used above, since $\sum_{m\le Y^\kappa}\tau(m)^t/m\ll_t L^{O_t(1)}$ and $Y^\kappa\ll h$.

In (3), every $m$ is rough and $(m,u)=1$ since $(a,b)=1$. The condition $m\mid N-uv$ puts $v$ into a single class modulo $m$. Within that class sieve $v$ and $N-uv$ at primes $p\le z$. Both $m,u$ are units modulo $p$. The forbidden roots in the variable $v$ are $0,N/u\bmod p$, coinciding precisely when $p\mid N$. The interval for $v$ has length $h/u$. As in the Bonferroni step above, the sifted count is
$$
 \ll \frac{h}{um}\big(V+O_A(L^{-A})\big)+(1+2z)^{J+2}.
$$
Counting unrestricted $v$ in this upper bound is legitimate after retaining $(m,u)=1$. Since $C_1^{\omega(m)}\ll_\eta m^\eta$ for every fixed $\eta>0$, the total rounding cost before logarithms is $Y^{1/2+\kappa+o(1)}$. Mertens' product formula gives
$$
 V\asymp\frac{\mathfrak S(N)}{(\log z)^2},\qquad
 \sum_{\substack{m\le Y^\kappa\\(m,P)=1}}
       \frac{\mu^2(m)C_1^{\omega(m)}}m
 \le \prod_{z<p\le 2Y}(1+C_1/p)\ll(\log L)^{O(1)} .
$$
The first comparison is uniform: the omitted singular factors have relative error $O(L/z)$ by the generic $1/p^2$ tail and the prime divisors of $N$.

Finally, on any interval $[U,cU]$ of fixed ratio up to $2Y$,
$$
 \sum_{\substack{U\le u\le cU\\u>1,\ (u,P)=1}}1/u
      \ll_c (\log L)^3/\log z.
$$
If nonempty, factor off one prime $p>z$. For a fixed rough cofactor $k$, Chebyshev's bound gives at most $O_c(U/(k\log z))$ choices of $p\le cU/k$. Summing $1/k$ costs at most $\prod_{z<p\le2Y}(1-1/p)^{-1}\ll L/\log z=(\log L)^3$. Combining the last three bounds gives $hL^2\mathfrak S(N)(\log L)^{O(1)}/(\log z)^3$, which proves (1). The proof bounds even $L^2$ times the number of ordered divisor incidences, since it used only the upper bound $O(L^2)$ on the original log weights.

## What the signs give, and what a failed center would force

For a squarefree $n$ put $\mathcal D_t(n)=\{d\mid n:|\log(d/\sqrt n)|\le t\}$ and $C_t(n)=\sum_{d\in\mathcal D_t(n)}\mu(d)\log d$. The exact relation $\mu(n/d)=\mu(n)\mu(d)$ and the involution $d\leftrightarrow n/d$ give
$$
 C_t(n)=
 \begin{cases}
 (\log n/2)\sum_{d\in\mathcal D_t(n)}\mu(d),&\mu(n)=1,\\
 \sum_{d\in\mathcal D_t(n)}\mu(d)\log(d/\sqrt n),&\mu(n)=-1.
 \end{cases}                                                        \tag{4}
$$
For fixed $t>0$ these are proper divisors for large $Y$ and occupy $O_t(1)$ strips. In the signed balanced packet $C_t(a)C_t(b)$, each specified endpoint with $\mu(n)=-1$ gains another factor $O_t(1/L)$ in the absolute bound for the **packet after grouping**. Indeed on the support each divisor logarithm is $\asymp L$, and in the second line its replacement has size at most $t$. Thus the sum of absolute grouped products with $j$ prescribed odd-parity endpoints, $j=0,1,2$, is $O_t(h\mathfrak S(N)(\log L)^C/L^{1+j})$ on the rough squarefree endpoints. Even parity alone gives no sign rule for $\sum\mu(d)$.

There is a quantitative alternative for a window with $G_N=0$. Remove the negligible exceptional endpoints above and call the remaining rough starts $\mathcal A$. Put
$$
 P_N=\sum_{a\in\mathcal A}\mu(a)\mu(b)\log a\log b.
$$
This is the term $d=a,e=b$ in (2). Partition every other remaining term disjointly: if $d<a$, assign its dyadic $d$ strip on the first side; otherwise assign its proper $e$ strip on the second side. Let $S=h\mathfrak S(N)$. Then either

* $P_N\le-S/2$, or
* for some absolute $c>0$ at least $cL/(\log L)^C$ different assigned strips have signed total $\le-cS/L$.

Indeed the second case has proper-divisor sum $\le-(1/2-o(1))S$ by (2). There are $O(L)$ strips; discard negative strips of size less than $cS/L$ for sufficiently small $c$, then use (1) on each remaining strip. The conclusion allows cancellations among other strips.

In the first alternative there is a specific parity bias. Let $n_-,n_+$ count starts in $\mathcal A$ with $\mu(a)\mu(b)=-1,+1$, respectively. The same two-root sieve gives $|\mathcal A|=(1+o(1))e^{-2\gamma} S/(\log z)^2$, where $\gamma$ is Euler's constant. Since $\log a\log b=L^2+O(LH/Y)$, that alternative requires
$$
 \frac{n_- - n_+}{|\mathcal A|}\ \ge\
 \frac{e^{2\gamma}/2-o(1)}{(\log L)^6}.                              \tag{5}
$$
The individual parities admit a separate test. For fixed $0<\epsilon<1/6$, fixed $k\ge0$, and every $A>0$,
$$
 \sum_{m\le Y^{1/6-\epsilon}}\tau(m)^k
   \max_{K\subset I}\left|\sum_{\substack{a\in K\cap\mathcal A\\m\mid b}}\mu(a)\right|
       \ll_{A,\epsilon,k} h L^{-A},                                  \tag{6}
$$
where $K$ runs over intervals. This also holds on reflection. In particular $n_{+-}-n_{-+}$ and $n_{++}-n_{--}$ are both $O_A(hL^{-A})$, with the subscripts recording the two endpoint signs in order. Thus (5) measures a joint parity bias even after the individual endpoint means are known to much higher accuracy.

For (6) first take $k=0$. Only $(m,NP)=1$ occurs on $\mathcal A$. Restore the other endpoint conditions to just $(ab,P)=1$ while retaining this restriction on $m$. Errors are uniform in $K$, since a bad endpoint is charged at most $\tau(b)$ times over all $m$. Expand the truncated $b$ wheel at $j$ coprime to $N$ and put $\mu(a)1_{(a,P)=1}=\sum_{c\mid a,\ p\mid c\Rightarrow p\le z}\mu(a/c)$. For $c>Y^\eta$, $\eta=\min(\epsilon,1/100)$, the smooth-divisor exceptional set and moment bounds from the proof of (2) handle all truncation errors, including $\tau(b)$ from summing $m$ and another $\tau(b)$ from the truncated wheel. For fixed smaller $c$ the class is $ct\equiv N\bmod mj$. Because $m$ is rough, the modulus uniquely specifies $m,j$. It is coprime to $N$, so the class is empty or reduced. With $X\asymp Y/c$, $y=h/c$, $Q=Y^{1/6-\epsilon}z^{J+1}$, one has $Q\sqrt X/y\ll Y^{-\epsilon+\eta/2+o(1)}$ and $y\gg X^{5/8+\delta}$ for a fixed $\delta>0$. Timofeev's maximal estimate for $\mu$ and the maximal arithmetic-progression bound for its coprime mean from the preceding note now give $O_A(yL^{-A})$ summed over $mj$, including the maximum over subintervals. The remaining sum over $c$ costs $\sum_{c\le Y^\eta}1/c\ll L$. For the weight $\tau(m)^k$, interpolate by Cauchy–Schwarz between the unweighted sum of the absolute errors and the bound $\sum_{m\le Q}\tau(m)^{2k}(h/m+1)\ll h L^{O_k(1)}$ using the original counts for the trivial estimate. The $m=1$ term on each orientation gives the two assertions about the parity table.

For squarefree $b$, $\mu(b)=\sum_{m\mid b}(-2)^{\omega(m)}$ by the binomial theorem. In $P_N$, all terms of this expansion with $m\le Y^{1/6-\epsilon}$ have signed total $O_{A,\epsilon}(hL^{-A})$ by (6) with $k=1$, freezing the logarithms at $L$ at power-saving cost. Here $\sum_{m\mid b}2^{\omega(m)}=3^{\omega(b)}\le \tau(b)^2$ suffices with the fixed short-interval moments. This expansion still includes $m=b$.

In fact (6) allows conditioning on the **entire list** of small prime factors of $b$. Let $z_1=\exp(L/(\log L)^2)$ and $t(b)=\prod_{p\mid b,\ p\le z_1}p$. Then
$$
 \sum_s \max_{K\subset I}\left|
     \sum_{\substack{a\in K\cap\mathcal A\\t(b)=s}}\mu(a)\right|
       \ll_A hL^{-A}.                                                \tag{7}
$$
Here $s$ ranges over all possible lists encoded by their squarefree products, including $s=1$. To prove it, write $1_{t=s}=\sum_{m\mid t,\ s\mid m}\mu(m/s)$ and truncate at $\omega(m)\le J$. This is exact unless $\omega(b)>J$. The absolute error summed over all $s$ at an exceptional endpoint is at most $1+\sum_{m\mid t}2^{\omega(m)}\le1+\tau(b)^2$, so step 1 applies. Each surviving $m$ has all its primes $\le z_1$, hence $m\mid t(b)$ is precisely $m\mid b$. Also $m\le z_1^J=Y^{o(1)}$ and its coefficient is counted at most $\tau(m)$ times over $s$. Apply (6) with $k=1$. Consequently any bounded function of the full small-prime list, including its parity or the least factor when it belongs to the list, has negligible signed correlation with $\mu(a)$. This estimate concerns the summed absolute errors; very rare individual lists need not have a small *relative* error.

### Distributing the whole-divisor term over proper prime factors

There is a way to remove the isolated term $P_N$ from the alternative above. On $\mathcal A$, $\mu(b)=-1+2\,1_{\mu(b)=1}$. Every $b>1$ with $\mu(b)=1$ is composite and has a least prime factor $p^-(b)\le\sqrt b$. Equation (6) at $m=1$ gives
$$
 P_N=2\sum_{\substack{a\in\mathcal A\\\mu(b)=1}}
             \mu(a)\log a\log b+O_A(hL^{-A}).                        \tag{8}
$$
The main sum in (8) is assigned to right-side dyadic bins by $p^-(b)$. This counts each contributing endpoint exactly once. Each bin obeys (1), since the proof bounds $L^2$ times the count of proper-divisor incidences. The parity condition on $b$ is retained.

Let $U_j$ be the earlier disjoint left and right proper-divisor sums, adding the assignments from (8) to their right bins. Then $G_N=S+\sum_j U_j+O_A(hL^{-A})$, with $O(L)$ bins and $|U_j|\ll S(\log L)^C/L$ uniformly. It follows **without a separate assumption on $P_N$** that any center with $G_N=0$ has at least $cL/(\log L)^C$ distinct side-and-scale bins with $U_j\le-cS/L$ for sufficiently large $Y$. This assertion is about the regrouped quantities $U_j$. For the original divisor boxes the two alternatives preceding (5) remain the conclusion. The many negative bins are compatible with the available upper bounds.

The remaining target is a lower bound for their **sum**, such as $\sum_j U_j\ge-(1-\delta)S$ with a fixed $\delta>0$. Equations (6)–(7) control small-divisor information on the partner. Equation (8) asks for the sign at the first endpoint with even parity and a specified least prime factor at the other. Replacing this joint mark by the unmarked small-divisor test would lose the unknown correlation.

For a finite illustration, $Y=1009^2$ with the explicitly chosen sieve cutoff 29 gives 232 rough, squarefree, coprime starts. The sign counts $(++,+-,-+,--)$ are $(54,56,53,69)$. With $t=\log 2$, 42 starts have a balanced proper divisor on at least one side and only two have one on both sides; the window contains 52 prime pairs. This finite sieve differs from the asymptotic choice of $z$ at this $Y$. [Exact finite checks](CheckProperDivisorScales.py)
