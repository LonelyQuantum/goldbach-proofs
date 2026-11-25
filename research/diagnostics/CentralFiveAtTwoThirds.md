# A central prime and a squarefree five-almost-prime at half-width $X^{2/3}$

Let $N=2X$ run over the even integers. Fix $d\ge1$. Write $G_r$ for the number of $1\le h\le H=\lfloor X^\theta\rfloor$ such that $X+h$ is prime in the class $b\bmod d$, and $a=X-h$ is squarefree with at most $r$ prime factors. For each of the two rows below, the paper deduction gives, for every sufficiently large $X$ and every $b$ with $(b,d)=(N-b,d)=1$,

$$
G_r\gg_d \mathfrak S_d(N)\frac{H}{(\log X)^2},
\qquad \mathfrak S_d(N)=
\prod_{\substack{\ell\mid N,\ \ell>2\\\ell\ \mathrm{prime},\ \ell\nmid d}}
\frac{\ell-1}{\ell-2}.
$$

| $\theta$ | $r$ | $\delta=\theta-1/2$ | $u$ | $\lambda$ | $r+1-\lambda-u/\delta$ | certified normalized margin |
|---|---|---|---|---|---|---|
| $2/3$ | 5 | $1/6$ | $11/20$ | $269/100$ | $1/100$ | $>3/100$ |
| $11/15$ | 4 | $7/30$ | $2/3$ | $427/200$ | $11/1400$ | $>1/50$ |

Both bounds are unconditional. The estimates allow the additional requirement that every prime factor of $a$ be at least $z=D^{1/6}$, with $D=X^\delta/(d\log^B X)$ and fixed sufficiently large $B$. The first row changes the roughness threshold from the previous $D^{1/4}$ to $D^{1/6}$. The signed error for the stronger old roughness requirement remains open. The positive lower bound here permits a composite summand. We make no priority claim.

## The two divisor ranges

Use the linear sieve $f,F$, and put $L(s)=sf(s)/(2e^\gamma)$, $U(s)=sF(s)/(2e^\gamma)$, $K=2e^\gamma/6$, $Y=(\operatorname{Li}(X+H)-\operatorname{Li}(X))/\varphi(d)$. Let $V(z)=\prod_{2<\ell<z,\ \ell\nmid d}(1-1/(\ell-1))$, with primes in this and subsequent products. At odd $\ell<z$ outside $d$ forbid the prime endpoint $X+h$ to lie in $c_\ell\bmod\ell$, taking $c_\ell=N\bmod\ell$ when $\ell\nmid N$, and any unit when $\ell\mid N$. Each tuple defines a marked set of prime endpoints, counted by $S$. Their reflected partners have no prime factor below $z$. Indeed a prime endpoint $>X$ is coprime to $N=2X$ for large $X$, both summands are odd, and admissibility handles the primes in $d$.

For each squarefree product of active primes $k<D$, CRT prescribes one unit class modulo $dk$. In Cai–Lu's Lemma 3 take $\beta=0$, $x=X$, interval start $X$, length $H$, and use the maximum over reduced classes. Interchanging endpoint inclusion costs at most two per modulus, absorbed by $O(D)$. Thus the sum of absolute errors is $O_{A,d}(H/\log^A X)$ for any fixed $A$ after choosing $B$. The density at $\ell$ is $1/(\ell-1)$, independent of the markers, and satisfies the dimension-one prime sum by Mertens' theorem. The lower linear sieve gives $S\ge YV(z)K(L(6)+o(1))$. [Cai and Lu, Lemmas 1–3, pp. 312–313](https://bibliotekanauki.pl/articles/1216105.pdf#page=2)

Let $S_q$ count marked endpoints with $q\mid a$. In the Richert penalty, $q$ runs over primes $z\le q<y=D^{1/u}$ with weight $1-ut$, where $t=\log q/\log D$. Only $q\nmid Nd$ need be included. Split at $D^{6/7}$.

* For $1/6\le t<6/7$, use the prime progression modulo $dq$ and the upper sieve at level $D/q$ with cutoff $z'=\min(z,\sqrt{D/q})$. Measured in units $YV(z)K/q$, the main-term coefficient is $U(6(1-t))/(1-t)+o(1)$, uniformly. For $6(1-t)\ge2$ this follows directly from $F$. Below 2, $V(z')/V(z)=(1+o(1))\log z/\log z'$ and $F(2)=e^\gamma$ give the same formula with $U=1$. Replacing $q-1$ by $q$ in this normalization costs $o(1)$. Each remainder modulus $qk<D$ has just one prime divisor at least $z$, since the primes of $k$ are $<z'\le z$; the absolute errors sum within the preceding budget.
* For $6/7\le t<1/u$, split into dyadic intervals $Q\le q<2Q$, truncated at the ends. Use $R^2=H/(Q\log^{12}X)$. On the integer $a$ forbid $N\bmod\ell$ for primes $\ell<R$ outside $d$, and also $N-c_\ell\bmod\ell$ at odd active $\ell<z$. Each true marked pair survives this test. There are two forbidden classes at those odd primes, one at the remaining sieve primes. Write $G(R)$ for the corresponding Selberg denominator. The one-root expansion in the [preceding calculation](EvenTargetsAndFiveFactorRemainder.md#one-signed-arithmetic-estimate-sufficient-for-five-factors) gives $V(z)G(R)\ge(\varphi(d)/d)(\log R-\log z)-O_d(1)$. It uses only the local counts and $R>z$. In both rows $A_\theta=\theta/\delta-1/3>1/u$, so $\log R-\log z=(A_\theta-t)\log D/2+o(\log X)$ is uniformly positive by a fixed multiple of $\log X$.

For $q<R$, divisibility by $q$ forces avoidance of its single forbidden class $N\bmod q$. The other local indicators have their original joint product law in the main term. Conditioning a nonnegative Selberg square on this avoidance multiplies its expectation by at most $q/(q-1)$. For $q\ge R$ it costs nothing. The per-prime main term is therefore at most $H/(d(q-1)G(R))$. Dividing by $YV(z)K/q$ gives the switched coefficient

$$
\frac{6e^{-\gamma}}{\delta(A_\theta-t)}+o(1).
$$

For completeness, the signed coefficients $C(n)$ from expanding this square satisfy $|C(n)|\le3^{\omega(n)}$ on squarefree $n<R^2$, since the normalized divisor weights have magnitude at most 1. Terms with $q\mid n$ have zero observed and conditional model count. Otherwise the CRT rounding error for a product $n$ is at most its number of bad classes, at most $2^{\omega(n)}$. The sum of the errors over a block is $O(QR^2(1+\log R)^5)$ by using $6^{\omega(n)}=\tau_6(n)$ on squarefree $n$ and $\sum_{n<T}\tau_6(n)\ll T(1+\log T)^5$. Over $O(\log X)$ blocks this is $O(H/\log^6 X)=o(YV(z))$, for each fixed $d$. No signed cancellation is used.

## The positive margin

The weight on a marked endpoint is $1-\lambda^{-1}\sum_{z\le q<y,\ q\mid a}(1-ut)$. On squarefree $a$, the penalty sum is at least $\Omega(a)-\log a/\log y$, by including the nonpositive terms for $q\ge y$. Since $\log a/\log y\le u/\delta+o(1)$, the strict sign slack in the table makes the weight nonpositive whenever $\Omega(a)\ge r+1$. Every weight is at most 1. Deleting nonsquarefree rough $a$ from a lower bound costs at most $O(H/z+\sqrt X)=o(YV(z))$ by summing the counts of multiples of $\ell^2$ for $z\le\ell\le\sqrt X$.

Partial summation over the primes, extending the nonnegative upper main terms to primes dividing $Nd$, gives a marked lower bound $YV(z)K(\Delta+o(1))/\lambda$, where

$$
\Delta=\lambda L(6)
-\int_{1/6}^{6/7}\left(\frac1t-u\right)\frac{U(6(1-t))}{1-t}\,dt
-\int_{6/7}^{1/u}\left(\frac1t-u\right)
 \frac{6e^{-\gamma}}{\delta(A_\theta-t)}\,dt .
$$

Here is a reproducible enclosure. $L=0$ up to 2 and $U=1$ up to 3. Thereafter their derivatives are respectively $U(s-1)/(s-1)$ and $L(s-1)/(s-1)$. Both functions are nondecreasing. On each cell of width $1/2400$ bound the delayed numerator at both endpoints and the reciprocal denominator at the opposite endpoints. Round lower and upper increments outwards to multiples of $10^{-12}$. In the two outer integrals, use 2400 equal cells each, bounding each nonnegative factor by its maximum endpoint value, with $U$ rounded to the next grid point. The inequality $\gamma\ge H_{512}-\log513>\log(16/9)$, where $H_{512}$ is a harmonic number, gives a rational upper bound $6e^{-\gamma}<27/8$. This yields certified lower bounds $0.03440604497977$ and $0.031304860479455$ for $\Delta$, respectively. The Python checks use only integers and rational arithmetic. [Exact checker](CheckCentralFive.py)

Finally average over independent uniform unit choices for each $c_\ell$ at $\ell\mid N$. Each genuine qualifying rough pair survives with the same probability $\prod_{2<\ell<z,\ \ell\mid N,\ \ell\nmid d}(\ell-2)/(\ell-1)$. The omitted factors of $\mathfrak S_d(N)$ for $\ell\ge z$ contribute $1+O(1/z)$, since their number is bounded in both rows. Dividing by the survival probability and using $YV(z)\asymp_d H/(\log X)^2$ gives the stated counts.

## Four factors at the original width

One sufficient arithmetic estimate can be stated with the same marked $S_q$. At $\theta=2/3$ keep $v=6,\ u=11/20$, and use $\lambda=169/100$. The sign slack for excluding five or more factors is again $1/100$. It would suffice, for each large center and admissible class, to show that the marker average of the **whole** weighted penalty is at most $(283/100+o(1))YV(z)K$. Indeed $(169/100)L(6)>2.84$ by the same certificate. The independent upper estimates used here give a sum of upper bounds about $4.50$ in these units. The new sufficient bound is open. Even the four-factor result in the wider window allows composite partners; a positive count of pairs with both summands prime requires further information about the composite contributions.
