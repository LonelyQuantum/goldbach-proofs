# The four-factor penalty at the original central width

Fix a positive modulus $d$, a center class $c\bmod d$, and a prime class $b\bmod d$ with $(b,d)=(2c-b,d)=1$. The target is $N=2x$, with $x\equiv c\bmod d$. Write $H=\lfloor x^{2/3}\rfloor$, $D=x^{1/6}/(d\log^B x)$, $z=D^{1/6}$, $u=11/20$, $y=D^{1/u}$, and $K=e^\gamma/3$. Use the sufficiently large fixed $B$ from the [five-factor calculation](CentralFiveAtTwoThirds.md). Below, $p,\ell,q$ denote primes. All averages over centers use ordinary counting measure in the specified class.

**Result.** Fix $3/5<\eta<2/3$. In every interval $[X,X+X^\eta)$ for sufficiently large $X$, at least one sixth of these centers satisfy the actual four-factor penalty criterion of the preceding calculation. For each such center there are
$$
\gg_d \mathfrak S_d(2x)H/(\log x)^2
$$
positive $h\le H$ for which $p=x+h\equiv b\bmod d$ is prime and $a=x-h$ is squarefree with at most four prime factors, all at least $z$. Here $\mathfrak S_d(2x)=\prod_{\ell\mid 2x,\ \ell>2,\ \ell\nmid d}(\ell-1)/(\ell-2)$. The fraction is asserted for each fixed choice of $d,c,b$. The good centers may depend on $b$. This is a paper deduction; the estimate for **every** individual center remains open.

## What remains at an individual center

Write $Y=(\operatorname{Li}(x+H)-\operatorname{Li}(x))/\varphi(d)$, $V=\prod_{2<\ell<z,\ \ell\nmid d}(1-1/(\ell-1))$, and $Z=YVK$. Let $M_x$ be the product defining $\mathfrak S_d(2x)$ restricted to $\ell<z$. For each genuine pair with $a$ rough (all prime factors at least $z$), the average probability of passing the extra residue markers of the five-factor calculation is exactly $1/M_x$. Indeed at $\ell\mid x$ the prime endpoint is a unit, and the forbidden unit is uniform. There is no loss at the other primes. Use this identity to define the dimensionless **true** penalty on a range $I$ of $q$ by
$$
P_x(I)=\frac{1}{M_x Z}
\sum_{\substack{x-H\le a<x,\ a\ {\rm rough}\\p=2x-a\ {\rm prime},\ p\equiv b\bmod d}}
\ \sum_{\substack{q\in I,\ q\mid a}} (1-u\log q/\log D).
$$
Put $P_{\rm small}=P_x([z,D^{2/3}))$, $P_{\rm tail}=P_x([D^{2/3},y))$. The earlier Richert argument applies once their sum is at most $2.83+o(1)$, with a strict margin since $(169/100)L(6)>2.84$. All its bounds before averaging over markers are uniform. Keeping this slack gives the same lower-bound constant at every successful center.

For all sufficiently large centers,
$$
1.67<P_{\rm small}<2.06.
$$
In the notation $t=\log q/\log D$, the small-prime sieve at level $D/q$ has $s=6(1-t)\in[2,5]$ throughout. Its normalized upper and lower leading bounds are the integrals of $(1/t-u)/(1-t)$ times $U(s)$ and $L(s)$, respectively, for $1/6\le t\le2/3$. The remainder moduli each have a unique prime factor $\ge z$, as in the preceding calculation. Omitting $q\mid 2xd$ has cost $o(1)$ even in the lower integral, since at most $O(1)$ such primes exceed $z$. For the lower certificate use $L(s)\ge\log(s-1)$, from $U\ge1$. The outward-rounded enclosures give a lower bound $1.673326250241$ and an upper bound $2.058080482926$ for the respective integrals. Thus $P_{\rm tail}\le0.77$ suffices.

There is a pointwise comparison which isolates the prime input. For one tuple of markers let $R_q$ count integers $a$ in the same interval, with $2x-a\equiv b\bmod d$, $q\mid a$, both endpoints rough, and the indicated markers satisfied. Define $B_x$ by summing $R_q$ on the tail with the same weights, averaging over the tuples, and multiplying by $c_z/Z$, where
$$c_z=\bigg(\log x\prod_{\ell<z}(1-1/\ell)\bigg)^{-1}.$$
This replaces the prime indicator, on the same marked rough support, by a constant. Ignore $q\mid 2xd$ in the comparison (they give no prime pairs). We have
$$
B_x\le (21/20)(5/8)+o(1).
$$
Consequently either $P_{\rm tail}-B_x\le 0.11+o(1)$ or $P_{\rm tail}\le (7/6)B_x+o(1)$ is sufficient for four factors. In the latter test the allowed weighted prime fraction among the comparison endpoints is $(7/6)c_z$ (up to an additive error in the normalized counts). Both are open pointwise estimates.

To prove the comparison bound, on $a$ use the Selberg upper square with radius $R^2=H/(q\log^{12}x)$ and primes below $z$ outside $d$. The single forbidden class at 2 enforces oddness if needed. At every other active prime there are two distinct classes: $2x\bmod\ell$ and $2x-c_\ell\bmod\ell$, where $c_\ell$ is the marked forbidden unit for the upper endpoint. If $\ell\nmid 2x$ the latter class is zero. If $\ell\mid 2x$ the first class is zero. These exclusions enforce roughness of both endpoints, including at exceptional primes. The full survival product is $V\prod_{\ell<z,\ \ell\nmid d}(1-1/\ell)$.

For clarity, if $\nu_\ell$ classes are forbidden and $g(\ell)=\nu_\ell/(\ell-\nu_\ell)$, the full survival product times $G(R)=\sum_{j<R}g(j)$ is $\Pr(J<R)$. Here the summation is on squarefree products of sieve primes with multiplicative $g$, and $J$ includes each prime independently with probability $\nu_\ell/\ell$. This probability gives the fraction of the full denominator retained in the Selberg bound. Uniformly on the tail,
$$\frac{\log R}{\log z}\ge \frac{72}{11}+o(1).$$
Prime Mertens sums and partial summation give mean $(k+o(1))\log z$ and variance $(k/2+o(1))\log^2 z$ for $\log J$ when $\nu_\ell=k$ outside finitely many primes. Cantelli's inequality therefore bounds $1/\Pr(J<R)$ by $1+(k/2)/(72/11-k)^2+o(1)$. For $k=2$ this is below $21/20$; for $k=1$ it is below $51/50$. In both uses of the square, the total absolute rounding errors are $O(H/\log^6 x)$: the grouped coefficient times the number of classes is bounded by $\tau_6(n)$ on squarefree $n<R^2$, and $\sum_{n<R^2}\tau_6(n)\ll R^2(1+\log R)^5$. All $q$ here exceed the sieve primes. [Derivation of the square and coefficient bounds](CentralPrimeSixFactors.md#an-integer-sieve-for-the-remaining-divisors)

Since $d$ is fixed, multiplying the integer main term by $c_z$ cancels the extra one-root product and changes $H/d$ to $Y(1+o(1))$. Prime partial summation leaves the tail integral
$$
J_0=\frac{1}{K}\int_{2/3}^{1/u}(1/t-u)\,dt
=3e^{-\gamma}\bigl(\log(30/11)-1+11/30\bigr)<5/8 .
$$
Together with the two-root bound this proves the stated pointwise comparison.

## A short-interval mean for the true tail

We prove $\limsup_{X\to\infty}\operatorname{avg}_{X\le x<X+X^\eta,\ x\equiv c\bmod d}P_{\rm tail}\le(51/50)J_0<0.64$. Here it is the actual prime indicator that enters the sum. Write $T=X^\eta$. Subscripts $X$ below mean that the sieve parameters and $H$ are evaluated at the left endpoint.

1. Fix $L>2$ independently of $X$. Let $W$ be the product of the odd primes $\le L$ outside $d$, $m=dW$, and $m_0=\operatorname{lcm}(2,m)$. Split the centers into classes $c'\bmod m$ above $c$. In a given class, $M_x\ge M_*=\prod_{\ell\mid(W,c')}(\ell-1)/(\ell-2)$. An admissible $a$ is odd, is congruent to $2c'-b\bmod d$, and both $a,2c'-a$ are units modulo $W$. There are $A=\prod_{\ell\mid W}\rho_\ell$ such classes modulo $m_0$, with $\rho_\ell=\ell-1$ for $\ell\mid c'$ and $\ell-2$ otherwise. At 2 and the primes of $d$ there is a unique class modulo $\operatorname{lcm}(2,d)$.
2. Extend the ranges to a common interval of $a$ of length $H_X+O(T)$, use the weaker cutoff $z_X$, and extend $q$ to $[D_X^{2/3},D_{X+T}^{1/u})$ with weight $1-u\log q/\log D_{X+T}$. These are upper bounds term by term since $D_x$ is increasing for large $X$. The endpoint and weight changes leave the limiting reciprocal-prime integral unchanged by Mertens' theorem. Also $Z_x/Z_X=1+o(1)$ uniformly and $T=o(H_X)$.
3. Fix $a$ in one of the $A$ classes. As $x$ traverses this center progression, $2x-a$ lies in a single unit class modulo $2m$ in a real interval of length $2T+O(1)$. The number of primes there is at most $(1+o(1))2T/(\varphi(2m)\log X)$ uniformly in $a$. Apply Cai–Lu's Lemma 3 with $\beta=0$ at exponent $\eta>3/5$, reference point $3X/2$, and the fixed modulus $2m$. Splitting the interval into a bounded number of pieces of length at most $(3X/2)^\eta$ meets the length condition; all starting points are within the lemma's range for large $X$. Dividing by the number $(1+o(1))T/m$ of centers gives the factor $2m/(\varphi(2m)\log X)$. [Cai and Lu, Lemma 3, p. 313](https://bibliotekanauki.pl/articles/1216105.pdf#page=3)
4. For each $q$ and each $a$ class modulo $m_0$, count rough integers $a$ divisible by $q$ in the enlarged interval. Apply the preceding square at $R^2=H_X/(q\log^{12}X)$ with **one** forbidden class, zero, at each prime below $z_X$ outside $m_0$. The per-prime upper main term is $(51/50+o(1))H_X/(qm_0)$ times $\prod_{\ell<z_X,\ \ell\nmid 2m}(1-1/\ell)$. This use of the square is on integers, after the uniform short-interval prime bound. It makes no independence assumption on primes and reflected divisors at a single center.
5. The wheel constants cancel exactly. Indeed $2m\varphi(d)/(\varphi(2m)m_0)=1/\varphi(W)$ for either parity of $d$, and $A/M_*=\prod_{\ell\mid W}(\ell-2)$. After division by $Y_XV(z_X)K$, the extra factor beyond $(51/50+o(1))J_0$ is at most
$$
\prod_{\substack{L<\ell<z_X\\\ell\nmid 2d}}
\frac{1-1/\ell}{1-1/(\ell-1)}
\le \exp\biggl(\sum_{n>L}\frac1{n(n-2)}\biggr).
$$
This tends to 1 as $L\to\infty$. First let $X\to\infty$ with the finite wheel fixed, then let $L\to\infty$. The asserted mean follows after averaging the finitely many classes for each wheel.

Because the true tail is nonnegative, the fraction of centers with $P_{\rm tail}\le0.77$ has lower limit at least $1-0.64/0.77=13/77>1/6$. The small-range estimate and the original sign budget now give the claimed lower bound on those centers. The average does not control the largest value in an interval.

The [Python certificate](CheckFourFactorTail.py) uses directed rational arithmetic and enumerates 2,745 small congruence cases for the wheel identity. It checks the constants and finite identities. The short-interval distribution and the sieves are analytic inputs to the paper proof. The contribution concerns this particular true penalty and a sufficient pointwise comparison; no priority claim for the existence of almost-prime representations on average is made.
