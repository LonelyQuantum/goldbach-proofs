# Removing small cofactors and many-factor partners at the same square

Let $X=p^2$ for an odd prime $p$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $L=\log X$. Count upper primes $a=X+h$, $2T<h\le H$, and put $n=X-h$. Define
\[
 \alpha=1/30,\quad \delta=1/6,\quad b=3/20,\quad \lambda=7/3,\quad \eta=9/100,\quad
 U=X^\alpha,\quad K=\frac{2C_2H}{L^2},\quad C_2=\prod_{\ell>2}\left(1-\frac{1}{(\ell-1)^2}\right)
\]
with a prime product. The following is a pointwise paper deduction using the sequence estimates in Cai–Lu. For every sufficiently large prime $p$, at least $(0.34+o(1))K$ different upper primes have a lower partner satisfying **all** the following requirements:

* $n$ is squarefree, every prime divisor exceeds $U$, and $\Omega(n)\le8$;
* either $n$ is prime, or its cofactor after removing the largest prime satisfies $n/P^+(n)>X^{9/100}$.

For semiprimes the cofactor is the smaller prime. For three-factor partners it is the product of the two smaller primes. For four through eight factors the proof below gives the stronger cofactor thresholds $X^{1/10},X^{1/4},X^{2/5},X^{11/20},X^{7/10}$, respectively. The [previous fixed-center subtraction](FixedSquareVaughan.md) removed semiprimes with smaller factor up to $X^{251/3000}$ and gave a lower constant of 0.08, with no explicit eight-factor restriction. The earlier [five-factor estimate](CentralFiveAtTwoThirds.md) has a different cutoff and different restrictions. No intersection of separately large sets is assumed here.

## One weight for the counts

On the $U$-rough candidates set
\[
 W(n)=1-\lambda^{-1}\sum_{q\mid n,\ q\ {\rm prime}}\left(1-\frac{\log q}{bL}\right)_+ .
\]
Write $S$ for their count before weighting. For squarefree $n$, setting $j=\Omega(n)$ and using $\log n<L$ gives $\sum(1-\log q/(bL))_+\ge j-\log n/(bL)>j-1/b$. Thus $W(n)>0$ requires $j\le8$. The same inequality on all primes except the largest gives $\log_X(n/P^+(n))>b(j-1-\lambda)=(3j-10)/20$. These are algebraic constraints on the *same* positive-weight candidates. Squareful rough sites cost at most $O(H/U+\sqrt X)=o(K)$ in count. As $W\le1$, deleting them can lower the weighted sum by at most this amount.

Use $D=X^\delta/L^{B_0}$, with $B_0$ sufficiently large as in Cai–Lu Lemma 3. The previous lower sieve gives $S/K\ge16.814+o(1)$. To bound the subtracted part of $W$, for each $U<q<X^b$ fix $q\mid n$. Start with the upper primes in the reduced class $2X\bmod q$, and sieve the lower cofactor by primes up to $\min(U,\sqrt{D/q})$ at level $D/q$. In the main term each odd sieve prime $\ell\ne q$ has density $1/(\ell-1)$, and $p>D$. Membership of the residue is counted with Lemma 3 at auxiliary exponent zero. Each remainder modulus is $qd\le D$ with only boundedly many choices of its marked prime $q>U$. The smallest residual level is $D/X^b$, a fixed positive power up to log factors, giving uniform sieve errors. The trim at the center can be taken by subtracting two prefixes, with negligible endpoint rounding.

For $s\le3$ put $\mathcal F(s)=1$, and for $3\le s\le4$ put $\mathcal F(s)=1+\int_2^{s-1}\log(t-1)\,dt/t$. The upper-sieve function on this range is $2e^\gamma\mathcal F(s)/s$ for $s\ge2$. Below parameter 2 the smaller cutoff just chosen uses parameter 2 and gives the same coefficient. Mertens' product and prime partial summation bound the penalty, in units of $K$, by
\[
 P=\lambda^{-1}\int_\alpha^b \left(1-\frac{u}{b}\right)
       \frac{2\mathcal F((\delta-u)/\alpha)}{u(\delta-u)}\,du<6.769
\]
up to $o(1)$. Here $u=\log_X q$. The expression for $\mathcal F$ up to 4 suffices since $(\delta-\alpha)/\alpha=4$. [Cai–Lu, Lemmas 1–3, pp. 312–313](https://bibliotekanauki.pl/articles/1216105.pdf#page=2)

## Sifting the opposite side after fixing the largest prime

Suppose $n=mt$ with $t=P^+(n)$ prime and $1<m\le X^\eta$. Since $n\ge X-H$, $t>X^\eta$ and $t>X^b$ for large $X$. Conversely every product in this window with $m$ squarefree and $U$-rough in this range, and $t$ prime, has $m$ as this unique cofactor. There can be only $i=1$ or $2$ primes in $m$ because $3\alpha>\eta$. They all lie below $X^b$. For $v=\log_X m$ the precise weight of the unwanted product is therefore
\[
 w_i(v)=1-(i-v/b)/\lambda .
\]
Both functions are positive on their ranges. Subtracting the *weighted* counts avoids charging these products twice for the Richert penalty.

For each $i$ let $g(m)=w_i(\log_Xm)$ on the indicated $m$ and zero elsewhere. Apply the upper linear sieve to the integers $a=2X-mt$ with the nonnegative weights $g(m)$, using level $D$ and prime cutoff $\sqrt D$. All true upper primes survive. For odd squarefree $d\le D$ the condition $d\mid a$ fixes $mt\equiv2X\bmod d$, a reduced class. Terms with $(m,d)>1$ vanish in the actual count. Cai–Lu Lemma 3 permits the **sum over $m$ inside the absolute value**, since $\eta<(5(2/3)-3)/2=1/6$, $0\le g\le1$, and $\sum_{m\le X}g(m)^2/m\ll L$. The starting point $X-H$ of the product interval is in $[X/2,X]$. The predicted count for this modulus is consequently $\varphi(d)^{-1}\sum_{(m,d)=1}g(m)Y_m$, where
\[
 Y_m=\int_{X-H}^{X-2T}\frac{dx}{m\log(x/m)}
      =(1+o(1))\frac{H}{mL(1-\log_Xm)}
\]
uniformly in this range. The endpoint convention is $[X-H,X-2T)$, with $H,T$ integers. The lemma bounds the sum of absolute errors by $O_A(H/L^A)$. The use of the weighted prime-product sum here is the extra input beyond the auxiliary-exponent-zero estimate. [Cai–Lu, Lemma 3 and its switched application in §4](https://bibliotekanauki.pl/articles/1216105.pdf#page=3) · [Wu, original short-interval distribution theorem](https://doi.org/10.1093/qmath/44.1.109)

Uniformity for these moving supports can also be obtained from the fixed-function formulation. If the normalized remainder seminorms in Lemma 3 were unbounded along a sequence of $X$ for the bounded weights above, choose a subsequence with pairwise separated bands $[X^\alpha,X^\eta]$. On each new band extend one global arithmetic function by either $g$ or $-g$. The triangle inequality for the lemma's seminorm ensures one choice gives a value at least as large as that of the new band alone. Future bands start past the current truncation $X^\eta$ and cannot affect it. The resulting single function has absolute value at most one and violates Lemma 3. This argument concerns the distribution error; the actual sieve weights $g$ used for counting are nonnegative.

To use a common main term for the sieve we still have to account for the removed noncoprime $m$. For each prime $\ell\mid m$, $\ell>U$ and
\[
 \sum_{\substack{d\le D,\ d\ {\rm squarefree}\\\ell\mid d}}\frac1{\varphi(d)}
 \le \frac{1}{\ell-1}\sum_{k\le D}\frac1{\varphi(k)}
 \ll \frac{L}{\ell-1}.
\]
The last sum is $O(L)$, for example by expanding $k/\varphi(k)$ as a nonnegative divisor sum. There are at most two such primes per $m$, so the total change is $\ll (L/U)\sum_m g(m)Y_m=o(K)$, even using $\sum_{m\le X^\eta}1/m\ll L$. We may now use density $1/\varphi(d)$ with main mass $\sum_m g(m)Y_m$. At 2 the actual upper endpoints are odd and no sieving is needed. The odd prime sieve product is $(2C_2e^{-\gamma}+o(1))/\log\sqrt D$ and $F(2)=e^\gamma$. This gives coefficient $2/\delta=12$ after normalization by $K$.

For $m$ prime and for $m$ a product of two distinct primes, respectively, the upper bounds in these units are
\[
 B_1=12\int_\alpha^\eta\frac{w_1(v)}{v(1-v)}\,dv<9.297,\qquad
 B_2=12\int_{2\alpha}^\eta\frac{w_2(v)\log((v-\alpha)/\alpha)}{v(1-v)}\,dv<0.407.
\]
Indeed the prime reciprocal measure tends to $du/u$ on compact positive exponent intervals. For two primes, the ordered measure at fixed sum $v$ has density $\int_\alpha^{v-\alpha}du/[u(v-u)]$. Divide by two for unordered pairs; repeated primes have reciprocal weight $O(1/U)$. The displayed single log results. Prime partial summation or step-function approximation on the compact exponent triangle justifies these limits.

## What this leaves to prove

Remove nonpositive weights after subtracting the unwanted products. The sum of the remaining positive weights is at least $(16.814-6.769-9.297-0.407+o(1))K>(0.34+o(1))K$. Each remaining weight is at most one. All genuine prime partners carry weight one. This proves the simultaneous count.

Keeping the same weight, the exact constant budget at cutoff $e$ is $30e^{-\gamma}f(5)-P-B_1(e)-B_2(e)$ for $2\alpha<e<3\alpha$. The two upper integrals are strictly increasing on this interval. At $e=0.092$ the margin still exceeds 0.03, yielding the stronger cofactor cutoff with that smaller lower-count constant. At $e=0.093$ the budget is below $-0.10$. Thus its unique zero is between those exponents. A negative value here limits this fixed combination of estimates, not the actual counts.

There is a single bilinear sum describing what can still go wrong. Put $Z=X^\eta$. For a surviving composite $n$, its least divisor $d>Z$ satisfies $d\le\sqrt n$. To see this, every prime in $n/P^+(n)$ is at most $\sqrt n$. If one exceeds $Z$, use it. Otherwise multiply those primes until the product first exceeds $Z$; the result is at most $Z^2<\sqrt n$. Conversely any divisor $Z<d\le\sqrt n$ forces $n/P^+(n)\ge d$. If the largest prime exceeds $\sqrt n$, it cannot divide $d$; otherwise $n/P^+(n)\ge\sqrt n$. The choice of the least divisor makes the sum over $n=dt$ unique, even when several divisors lie in range.

Thus if there is no central prime pair at this $X$, the sum of $W(n)_+$ over the remaining squarefree rough composites with $a=2X-dt$ prime, $X^\eta<d\le\sqrt n\le t$, and $d$ selected as above, is at least $(0.34+o(1))K$. These large-factor products still allow complete cancellation. In fact averaging over **all consecutive integer centers** supplies a check on attempts to bound them in absolute value: in the [packet calculation](SemiprimePackets.md), retain only semiprimes with smaller prime in $[X^{1/5},X^{1/3}]$. The density integral on this band is $\log 2$. Both factors exceed the Richert cutoff, so these terms have weight one and pass all the new restrictions. For packets of length $X^{3/5}$ the mean of this single subfamily alone is $(2\log2+o(1))H/L^2$, already above $0.34K$. The pointwise result here concerns prime-square centers; the packet statement does not establish that lower bound at any given prime square.

The [finite checker](CheckSwitchedWeightedCofactors.py) uses rational upper and lower intervals for the four constants. It also compares direct and switched finite product counts, tests the noncoprime moduli and checks the cofactor and sign identities. The analytic estimates and quantifiers in $p$ are paper arguments.
