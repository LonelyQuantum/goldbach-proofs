# A prime and a squarefree six-almost-prime in the original central window

Let $p$ be prime, $X=p^2$, $H=\lfloor X^\theta\rfloor$. Fix $d\ge1$. For $0\le b<d$ with $(b,d)=(2X-b,d)=1$, let $G_6$ count $1\le h\le H$ for which $X+h$ is prime in the class $b\bmod d$ and $X-h$ is squarefree with at most six prime factors. We obtain the following paper deduction from classical sieve results:

$$G_6(X,H;d,b)\gg_{d,\theta}\frac{H}{(\log X)^2}
\qquad\left(\frac{193}{290}<\theta\le\frac23\right).$$

The bound holds for every sufficiently large prime $p$, simultaneously in all admissible classes for the fixed $d$. At $\theta=2/3$ it improves the seven-factor conclusion in [the original window calculation](CentralPrimeAlmostPrime.md). The improvement comes from counting integers after extracting a large prime divisor. The distribution estimate for primes still has exponent $\delta=\theta-1/2$. This deduction does not assume GRH. The comparative claim is limited to our previous calculation.

## Small divisors of the reflected integer

Take $\mathcal A=\{2X-t:X<t\le X+H,\ t\ {\rm prime},\ t\equiv b\bmod d\}$, $Y=\int_X^{X+H}dt/(\varphi(d)\log t)$, and
$$D=X^\delta/(d\log^B X),\quad z=D^{1/4},\quad w=z^2,\quad y=R=z^5,\quad Q=D^{9/10}.$$
Let $S$ count members of $\mathcal A$ with all prime factors at least $z$ and $S_q$ count those divisible by the prime $q$. Define
$$V(z)=\prod_{\substack{2<\ell<z\\ \ell\nmid d}}\left(1-\frac1{\ell-1}\right),\qquad K=e^\gamma/2,$$
with products over primes throughout. For any fixed $A>4$, Cai–Lu's short-interval estimate at $\beta=0$ gives total absolute remainder $O_{A,d}(H/\log^A X)$ for squarefree moduli $k<D$, $(k,2d)=1$, taking $B$ sufficiently large. The CRT fixes one reduced class modulo $dk$ since $k<p$. The linear lower sieve then gives $S\ge YV(z)K(\log 3+o(1))$. For $z\le q<Q$, apply the linear upper sieve at level $D/q$ with prime cutoff $\min(z,\sqrt{D/q})$. Its parameter lies in $[2,3]$, where $F(s)=2e^\gamma/s$. The upper main term for $S_q$ is
$$\frac{YV(z)K}{q-1}\left(\frac{1}{1-\log q/\log D}+o(1)\right).$$
The error is uniform on this range. The auxiliary remainder moduli $qk<D$ have a unique prime divisor at least $z$, so the summed absolute remainders obey the same bound. These are the small-divisor estimates already derived for the seven-factor result. [Cai and Lu, *Chen's theorem in short intervals*, Lemmas 1–3, pp. 312–313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=2)

## An integer sieve for the remaining divisors

For each prime $Q\le q<y$ write $X-h=qm$. The interval of $m$ has length $H/q$, and $qm\equiv2X-b\bmod d$ fixes one residue. Uniformly for large $p$ we have $q>w$, $(q,d)=1$, and $p>w$. An upper bound for $S_q$ results from excluding multiples of primes below $z$ from $m$ and multiples of primes below $w$ from $2X-qm$. The actual prime $2X-qm>X$ passes the latter test.

Outside $d$, an odd prime $\ell<z$ forbids two distinct residues of $m$, namely $0$ and $2X/q\bmod\ell$. The prime 2 forbids a single residue. For $z\le\ell<w$ only $2X/q\bmod\ell$ is forbidden. Primes dividing $d$ impose no further restriction by admissibility. Write $\nu(\ell)$ for the respective forbidden counts. With $P$ the product of primes $\ell<w$ outside $d$, the joint survival density is exactly
$$V_*=\prod_{\ell\mid P}(1-\nu(\ell)/\ell)
     =V(z)\prod_{\ell\mid P}(1-1/\ell).$$
In particular the factor at 2 occurs exactly once if $d$ is odd. For $k\mid P$ extend $\nu$ multiplicatively and put $\rho(k)=\nu(k)/k$. By CRT the count with forbidden residues at all primes dividing $k$ is $H\rho(k)/(dq)+O(\nu(k))$.

Write $g(\ell)=\rho(\ell)/(1-\rho(\ell))$, extend multiplicatively to divisors of $P$, and put $G(R)=\sum_{k\mid P,\,k<R}g(k)$. The Selberg upper bound is
$$ S_q\le\frac{H}{dqG(R)}+O(R^2(1+\log R)^2). $$
For completeness, square a divisor sum with coefficients $\lambda_j$ on $j\mid P$, $j<R$, and $\lambda_1=1$. A survivor has square equal to 1. The quadratic main form $\sum_{i,j}\lambda_i\lambda_j\rho([i,j])$ equals $\sum_k g(k)^{-1}v_k^2$ with $v_k=\sum_{k\mid j}\rho(j)\lambda_j$. Indeed $\sum_{k\mid n}1/g(k)=1/\rho(n)$ for $n\mid P$. Taking $v_k=\mu(k)g(k)/G(R)$ for $k<R$ gives main form $1/G(R)$ and $\lambda_1=1$ by inversion. Also
$$ |\lambda_j|=\frac{\prod_{\ell\mid j}(1+g(\ell))}{G(R)}
      \sum_{\substack{n\mid P,\;(n,j)=1\\n<R/j}}g(n)\le1. $$
Every term in the expanded numerator occurs in $G(R)$. The rounding errors are bounded by $(\sum_{j<R,\,j\mid P}\nu(j))^2\le (R(1+\log R))^2$, since $\nu(j)\le\tau(j)$.

It remains to bound the truncated sum $G(R)$ from below. Give every divisor $k\mid P$ probability $V_*g(k)$. Its prime divisors occur independently with probabilities $\rho(\ell)$. For $L=\log z$, the mean and variance of $\log k$ are
$$ \mathbf E\log k=(3+o(1))L,\qquad
 {\rm Var}(\log k)=(5/2+o(1))L^2. $$
Indeed the contributions of $\rho$ are those of one copy of $1/\ell$ below $z$ and one below $w=z^2$, up to finitely many primes. Partial summation gives $\sum_{\ell<t}(\log\ell)^j/\ell\sim(\log t)^j/j$ for $j=1,2$; the $\rho^2$ contribution to the variance is bounded. Cantelli's one-sided variance inequality at $\log R=5L$ gives
$$ V_*G(R)=\Pr(\log k<5L)\ \ge\ \frac{(2+o(1))^2}{5/2+(2+o(1))^2+o(1)}=8/13+o(1). $$
The strict cutoff includes no boundary mass on the wrong side. By Mertens' product theorem, $\prod_{\ell\mid P}(1-1/\ell)\sim e^{-\gamma}d/(\varphi(d)\log w)$. Since $\log w\sim(\delta/2)\log X$, we have uniformly in $Q\le q<y$,
$$ S_q\le\frac{YV(z)K}{q}\left(\frac{13}{2\delta}e^{-2\gamma}+o(1)\right)
                 +O(R^2(1+\log R)^2). $$
The coefficient is strictly less than 13 throughout the claimed range: $\delta>24/145$ and $e^{2\gamma}>145/48$. The sum of all the displayed additive errors is $O(yR^2(1+\log R)^2)=X^{15\delta/4+o(1)}=o(H/\log^2 X)$, since $\delta\le1/6$ and $\theta=1/2+\delta$. This integer count uses no prime-distribution estimate at modulus $q$.

## Positive margin after combining both ranges

Use the weight $1-\lambda^{-1}\sum_{z\le q<y,\,q\mid a}(1-\log q/\log y)$ on each surviving $a$, with $\lambda=13/6$ and $u=\log D/\log y=4/5$. For squarefree $a$, the penalty is at least $\Omega(a)-\log a/\log y$. We have $\log a/\log y\le 4/(5\delta)+o(1)$ and $\lambda+4/(5\delta)<7$ exactly when $\delta>24/145$. Thus a squarefree $a$ with at least seven factors has nonpositive weight. Every weight is at most 1. Removing nonsquarefree survivors from the lower estimate costs at most $O(H/z+\sqrt X)=o(YV(z))$, by counting multiples of prime squares in the interval.

Summing the small- and large-divisor upper bounds with the nonnegative penalty and using partial summation over primes gives
$$G_6\ge\frac{YV(z)K}{\lambda}\bigl(\Delta+o(1)\bigr),$$
where
$$\begin{aligned}
\Delta&=\frac{13}{6}\log3
-\int_{1/4}^{9/10}\frac{1-4t/5}{t(1-t)}\,dt
-13\int_{9/10}^{5/4}\frac{1-4t/5}{t}\,dt\\
&=\frac{13}{6}\log3-\log(18/5)-\tfrac15\log(15/2)
-13\bigl(\log(25/18)-7/25\bigr)>3/50 .
\end{aligned}$$
Here $t=\log q/\log D$. Both prime ranges have bounded reciprocal mass; replacing $1/(q-1)$ by $1/q$ costs $o(1)$ in the normalized sum. Finally $YV(z)\asymp_{d,\theta} H/(\log X)^2$. The two computations of $\Delta$ agree at approximately $0.0658593$.

Both strict numerical inequalities can be checked entirely with rational arithmetic. For $x>1$, set $s=(x-1)/(x+1)$ and sum $2\sum_{j=0}^{n-1}s^{2j+1}/(2j+1)$ as a lower bound for $\log x$. Adding $2s^{2n+1}/((2n+1)(1-s^2))$ gives an upper bound. With $n=160$ these bounds certify $\Delta>3/50$ and $2(H_{32}-\log33)>\log(145/48)$, where $H_{32}=\sum_{j=1}^{32}1/j$ and $\gamma\ge H_{32}-\log33$.

## What would suffice for five factors in the original window?

At $\theta=2/3$, keep $D,z,S_q$ as above, but change the weight to $y=D^2$, $u=1/2$, $\lambda=299/100$. The sign budget becomes $\lambda+6u=5.99<6$. One sufficient unproved estimate is the following weighted sum for each sufficiently large prime-square center and fixed admissible class:
$$
\sum_{D^{7/9}\le q<D^2}\left(1-\frac{\log q}{2\log D}\right)S_q
\le YV(z)K\left[\frac92\left(\log(18/7)-11/18\right)+o(1)\right],
$$
where $q$ runs over primes. Individual bounds for every $q$ are unnecessary. Below $D^{7/9}$ the same linear sieve applies. The remaining normalized margin would be
$$\tfrac{299}{100}\log3-\log(28/9)-\tfrac12\log(27/8)
-\tfrac92\bigl(\log(18/7)-11/18\bigr)>1/25.$$
The six-factor proof supplies a larger coefficient and covers a shorter upper range. A five-factor result in this window remains open in this calculation.

The analytic deduction is a paper argument. The existing [Lean lemmas](RichertFactorBudget.lean) cover the finite weight inequalities. The [exact arithmetic check](CheckSixFactorSwitch.py) certifies both margins, the bound on Euler's constant, and finite tests of the local densities and the Selberg form. Run it with Python 3 from this directory. The estimate still counts composite smaller summands; a positive lower bound for two prime summands would require new control of their contribution.
