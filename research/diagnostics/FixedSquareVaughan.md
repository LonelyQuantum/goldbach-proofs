# A signed divisor decomposition at one Goldbach target

Let $X=p^2$ for an odd prime $p$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$. In every sum $a=X+h$, $n=X-h$, $2T<h\le H$, and the upper endpoint $a$ is a genuine prime. Let $G$ be the sum of $\log a\log n$ over the terms with $n$ prime. Set $U=X^{1/30}$, $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes and $M=2C_2 H$. All limits below are pointwise as $p\to\infty$, with no averaging over centers and no hypothesis on zeros. This note uses the unshifted window.

**A part of the semiprime contribution can be subtracted at every target.** Let $S$ count the terms whose lower endpoint has all prime factors greater than $U$. Discard its nonsquarefree endpoints and all $n=qt$ with $q<t$ prime and $q\le X^{251/3000}$. The remaining number is at least
\[
 (0.08+o(1))\, M/L^2. \tag{1}
\]
They can have $n$ prime, $n=qt$ with $q>X^{251/3000}$, or at least three distinct prime factors. The size restriction in (1) applies to the smaller prime in a semiprime. No five-factor or shifted-site condition is imposed. The previous [all-center packet ratio](SemiprimePackets.md) concerns a different count and roughness cutoff.

**A signed bound at the same target.** Put $A_U(n)=\sum_{d\mid n,\,d\le U}\mu(d)$ and $B_U(n)=\sum_{\ell\mid n,\,\ell>U}\log\ell$ over primes. Let $N_{\rm rough}$ be the weight $\sum\log a\log n$ of the composite terms in $S$, and
\[
 J=-\sum_{\substack{n\ {\rm composite}\\ P^-(n)\le U}} \log a\, A_U(n)B_U(n).
\]
Then
\[
 G=M+J-N_{\rm rough}+o(H),\qquad
 15.81+o(1)\ \le J/M\le\ 15.88+o(1). \tag{2}
\]
These bounds evaluate the *net* contribution from lower composites with a small factor. If $G=0$ along a sequence, $N_{\rm rough}/M$ must lie between $16.814+o(1)$ and $16.874+o(1)$ on it. The size of the known signed term alone does not imply $G>0$. The square shape enters because $2p^2$ is coprime to every odd modulus below $p$; no additional cancellation special to individual prime squares has been proved here.

## The positive main term in Vaughan's identity

For arithmetic functions use Dirichlet convolution, $\mathbf1(n)=1$, and truncate $\mu,\Lambda$ at $U$ with subscripts $\le,>$. From $\Lambda=\mu*\log$ and $\log=\mathbf1*\Lambda$ one gets
\[
 \Lambda=\Lambda_{\le}+\mu_{\le}*\log-\mu_{\le}*\Lambda_{\le}*\mathbf1
                      +\mu_{>}*\mathbf1*\Lambda_{>}.
\]
The standalone $\Lambda_{\le}$ vanishes on our interval. In the next two terms average over the upper primes with weight $\log a$. A divisor $d\mid n$ prescribes $a\equiv2X\bmod d$. Even $d$ cannot occur, and every odd $d\le U^2$ is coprime to $2X$. Cai–Lu, Lemma 3 with the auxiliary weight supported at 1, gives a sum of absolute progression errors $O_A(H/L^A)$ up to level $D=X^{1/6}L^{-B(A)}$, including the maximum over interval prefixes. Partial summation against $\log a$ converts the integral with density $1/\log a$ to length. It also permits the additional factor $\log((2X-a)/d)$ in the first convolution. The coefficients of the second convolution grouped by modulus are bounded by $\sum_{v\mid d}\Lambda(v)=\log d$. Endpoint rounding costs $O(D L^{O(1)})$. The logarithm of $2X-a$ differs from $L$ by $O(H/X)$, and $\sum_{d\le U}1/\varphi(d)\ll L$. Thus, with $H'=H-2T$, the two main terms divided by $H'$ are, up to $o(1)$,
\[
 L A(U)-\sum_{d\le U,\ d\ {\rm odd}}\frac{\mu(d)\log d}{\varphi(d)}
 \quad\hbox{and}\quad
 -\sum_{\substack{m,v\le U\\mv\ {\rm odd}}}\frac{\mu(m)\Lambda(v)}{\varphi(mv)},
 \qquad A(x)=\sum_{d\le x,\ d\ {\rm odd}}\frac{\mu(d)}{\varphi(d)}.
\]
[Cai–Lu, Lemma 3, p. 313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=3)

The series $F(s)=\sum_{d\ {\rm odd}}\mu(d)/(\varphi(d)d^s)$ factors as $G_0(s)/\zeta(1+s)$. At each odd prime the factor of $G_0$ is $(1-\ell^{-s}/(\ell-1))/(1-\ell^{-1-s})$; at 2 it is $(1-2^{-1-s})^{-1}$. The coefficients of $G_0$ are absolutely summable even with the weight $d^{1/4}$ by the geometric expansions, and $G_0(0)=2C_2$. The classical zero-free-region estimate $\sum_{j\le y}\mu(j)/j\ll_A(\log(2y))^{-A}$ and convolution (split the $G_0$ divisor at $\sqrt x$) give $A(x)\ll_A(\log(2x))^{-A}$. Partial summation now justifies the derivative series at zero. Hence the first expression tends to $F'(0)=2C_2$.

For $v=\ell^j$ with odd $\ell$, the inverse totient of $mv$ is $(1-\mathbf1_{\ell\mid m}/\ell)/(\varphi(m)\varphi(v))$. The independent part is $O(L\,|A(U)|)$ since $\sum_{v\le U}\Lambda(v)/\varphi(v)\ll L$. Writing $A_\ell$ for the same sum excluding multiples of $\ell$ gives $A_\ell(x)=A(x)+A_\ell(x/\ell)/(\ell-1)$. Iteration bounds $A_\ell$ uniformly, and it tends to zero for each fixed $\ell$. Consequently $\sum_{\ell\mid m,\,m\le U,\,m\ {\rm odd}}\mu(m)/\varphi(m)\to0$ for each fixed $\ell$. The remaining coefficients are dominated by $\ell^{-1}\sum_{j\ge1}\log\ell/\varphi(\ell^j)\ll\log\ell/\ell^2$. Dominated convergence gives $o(1)$ for the full second expression. This proves the positive main term $M+o(H)$.

## Which factorizations enter the remainder

In the last convolution, discard terms with $\Lambda_{>}$ supported on proper powers. The number of lower sites divisible by any prime power $\ell^j>U$, $j\ge2$, costs $O((H/\sqrt U+\sqrt X)L^{O(1)})$: sum $H/\ell^j+1$, using $O(\sqrt y\log y)$ proper powers up to $y$ and partial summation. Even after divisor multiplicities $X^{o(1)}$ and log weights this is $o(H)$. The original $\Lambda(n)$ can likewise be restricted to primes at cost $o(H)$.

For a remaining divisor $\ell>U$ prime of a composite $n$, its cofactor $k=n/\ell$ exceeds one. The sum of $\mu$ over all divisors of $k$ vanishes. Its divisors at most $U$ are exactly the small divisors of $n$, since $\ell>U$. Thus the sum over large Möbius divisors is $-A_U(n)$. For prime $n$ the last convolution is zero. On a rough composite $A_U(n)=1$ and $B_U(n)=\log n$ except for squares of large factors, already negligible. This gives the identity in (2).

For example, a semiprime contributes zero here when its smaller prime is at most $U$, and contributes $-\log a\log n$ when both primes exceed $U$ and are distinct. With one distinct small prime the mixed term is zero. With exactly two distinct small primes $r,s$, it is nonnegative and equals $+\log a\,B_U(n)$ precisely when $rs>U$ (otherwise zero). With three distinct small primes its coefficient is negative precisely when their product exceeds $U$ but each pair product is at most $U$, provided $B_U(n)>0$. Repetitions of small primes do not alter $A_U$. More generally, for $r=P^-(n)\le U$, pairing $e,re$ gives
\[
 A_U(n)=\sum_{\substack{e\mid n,\ (e,r)=1\\ U/r<e\le U}}\mu(e).
\]
Any negative mixed contribution therefore needs at least three distinct small primes, including $r\le\sqrt U$.

## Quantifying the rough count and the semiprime subtraction

Apply the one-dimensional lower and upper linear sieves to the sequence of lower integers $n=2X-a$ with $a$ prime. At every odd prime $\ell\le U$ there is one forbidden reduced class out of $\ell-1$. The site at 2 is already avoided and $p>U$. The sieve product is
\[
 V(w)=\prod_{2<\ell\le w}(1-1/(\ell-1))
      \sim 2C_2 e^{-\gamma}/\log w .
\]
This follows by extracting $\prod_{\ell\le w}(1-1/\ell)$. The dimension-one prime sum follows from Mertens' theorem. Use level $D$ as above and $\log D/\log U\to5$. With normalization $M/L^2$ the lower and upper leading bounds for $S$ are $30e^{-\gamma} f(5)$ and $30e^{-\gamma}F(5)$. The use of a non-strict cutoff can equivalently be made with $\lfloor U\rfloor+1$. All endpoint weights $\log a\log n=(1+o(1))L^2$ uniformly. Since $G+N_{\rm rough}$ counts all of $S$ with these weights, (2) follows by subtraction. [Cai–Lu, Lemmas 1–2 and the bounds including the remainder sum, pp. 312–313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=2)

For $U<q\le X^\eta$, $\eta=251/3000$, fix $q\mid n$. An actual semiprime $n=qt$ has $t>q$ prime, hence $t>\sqrt{D/q}$. For an upper bound, sift $t$ below $w_q=\sqrt{D/q}$ at level $D/q$. Ignore 2 and $q$ in this sieve. The initial density is $1/\varphi(q)$ relative to upper primes, and a squarefree sieve divisor $d$ imposes the single reduced class $2X\bmod qd$ with $(d,q)=1$. Hence the additional local densities are exactly $1/(\ell-1)$. Omitting $q$ costs at most the factor $(q-1)/(q-2)=1+o(1)$ uniformly. Every error modulus $qd<D$ has only boundedly many possible marked primes $q>X^{1/30}$ and each fixes $d$. Lemma 3 therefore absorbs the accumulated absolute errors. Sieve dimension constants are uniform when one such prime is omitted.

Since $F(2)=e^\gamma$ and $\log w_q=(\log D-\log q)/2$, prime partial summation bounds the size of this semiprime layer, in units $M/L^2$, by
\[
 2\int_{1/30}^\eta\frac{du}{u(1/6-u)}+o(1)
 =12\log\!\left(\frac{4\eta}{1/6-\eta}\right)+o(1).
\]
Prime squares and all remaining nonsquarefree rough sites cost $O(H/U+\sqrt X)=o(H/L^2)$ by summing over prime squares. For clarity the constants below are certified by a rational interval calculation:
\[
 \begin{aligned}
 30e^{-\gamma} f(5)
 &=12\left[\log4+\int_2^3\frac{\log(t-1)}{t}\log\frac4{t+1}\,dt\right]\in(16.814,16.815),\\
 30e^{-\gamma} F(5)
 &=12\left[1+\int_2^4\frac{\log(t-1)}{t}\,dt\right]\in(16.872,16.874),\\
 12\log(4\eta/(1/6-\eta))&\in(16.731,16.732).
 \end{aligned}
\]
These expressions follow by integrating the linear-sieve delay equations once from their initial ranges. At $\eta=1/12$ the semiprime upper constant is exactly $12\log4$. The positive integral in $f(5)$ permits the stated excess in $\eta$. Subtraction gives (1). [Exact certificate and finite identity checks](CheckFixedSquareVaughan.py)

## A positive mixed subfamily

There is also a directly countable family contributing on the positive side of $J$. Take two distinct primes $X^{1/60}<r<s\le X^{1/36}$, put $m=rs>U$, and require $m\mid n$ while excluding all other odd prime divisors at most $U$. For each $m$ use sieve level $X^{1/10}$, giving parameter 3. Joint moduli are at most $X^{1/18+1/10}=X^{7/45}<D$; each such modulus determines at most a bounded number of admissible pairs $(r,s)$ by the lower size bound. Local density is $1/\varphi(m)$ times the preceding product with $r,s$ omitted. Uniformity of the sieve follows as above. Each survivor has exactly those two distinct small prime factors, hence is counted just once. Delete squares of primes $\ge X^{1/60}$ at cost $O(H/X^{1/60}+\sqrt X)=o(H/L^2)$ globally. The remaining $B_U(n)=\log(n/m)\ge(17/18+o(1))L$. Since the reciprocal totients of the unordered pairs sum to $(\tfrac12+o(1))\log^2(5/3)$, their positive contribution alone is at least
\[
 \left(\frac{85}{9}\log2\,\log^2(5/3)+o(1)\right)M>(1.70+o(1))M.
\]
This is a subfamily of the mixed term already included in (2); it cannot be added to (2) a second time. The unresolved pointwise estimate is an upper bound on the surviving composite contribution that leaves at least one genuine prime partner.
