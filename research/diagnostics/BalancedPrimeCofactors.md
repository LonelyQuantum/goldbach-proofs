# What a missing central prime pair would require of the composite factors

Fix an odd prime $p$, $X=p^2$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$ and $J=[X-H,X-2T)\cap\mathbb Z$. Write $a=2X-n$, $z=X^{1/30}$, $y=X^{1/10}$, $K=2C_2H/L^2$, with $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes. For a squarefree composite $a$ whose prime factors exceed $z$, let $W(a)=\sum_{r\mid a,\ r>y}(\log r)/L$ over primes. Set $W=0$ elsewhere. With $P$ the prime indicator, put
\[
 R=\sum_{n\in J}P(n)P(a),\qquad C=\sum_{n\in J}P(n)W(a).
\]
Split $C=U+B$ according as $m=a/P^+(a)$ is at most $y$ or exceeds $y$. Each eligible upper integer occurs in just one sector, even when several large prime divisors enter its weight.

At every sufficiently large prime square the following inequalities hold:
\[
  15.3980K<R+C<16.0612K,\qquad U<14.9501K,\qquad R+B>0.4480K. \tag{1}
\]
We also construct a reference weight on lower integers at the *same center*. Its counts $U_0,B_0,C_0$ use exactly the same upper conditions. They satisfy
\[
  U_0/K\longrightarrow u_*\in(1.2458,1.2459),\qquad
  13.4740<B_0/K<13.4761,\qquad 14.7199<C_0/K<14.7219. \tag{2}
\]
The limit in (2) is the exact integral $u_*$ below. If $R=0$ at a sufficiently large center, $C-C_0>0.6762K$. Moreover at least one of $U>1.0459\,U_0$, $B>1.0459\,B_0$ must hold there. These are tests for a missing pair. Bounds on the actual deviations needed to exclude this possibility remain open.

## Upper and lower estimates with a genuine lower prime

Use the rough count $S_P$ and the small-factor log sum $T_P$ in the [marked-prime calculation](MarkedPrimePartners.md#keeping-the-signs-of-the-single-sieve-errors). Then $R+C=S_P-T_P+o(K)$. Squareful rough sites contribute $O(H/z+\sqrt{2X})=o(K)$, and $\log a/L=1+O(H/(XL))$. Set $M=30e^{-\gamma}$, $J_b=\int_2^b \log(t-1)\,dt/t$ and $I=\int_2^3 \log(t-1)\log(4/(1+t))\,dt/t$. The previously derived lower coefficient is $12\log4+10I-2\log2$. For the upper coefficient use the upper sieve for $S_P$ and the lower sieve for $T_P$:
\[
 \limsup (R+C)/K
 \le MF(5)-M\int_{1/30}^{1/10} f(5-30t)\,dt
 =12(1+J_4)-2J_4=12+10J_4.
\]
For each small mark $\ell\mid a$, use the reduced class $2X\bmod\ell$ of the lower primes, then sieve $a/\ell$ to $z$ at level $D/\ell$, $D=X^{1/6}L^{-b_0}$ for sufficiently large $b_0$. Each remainder modulus contains a unique prime factor above $z$. Near the last endpoint the lower sieve is allowed to give zero. One can first stop at $1/10-\epsilon$, keep the remaining summands nonnegative, and let $\epsilon$ decrease to zero. The stated integral follows from the lower sieve formula on $[2,4]$ and prime partial summation. We use Lemmas 1–3 of Cai–Lu, including the maximum over the short-interval starting point. [Cai–Lu, *Chen's theorem in short intervals*, pp. 312–313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=3)

## The small-cofactor sector

For $1<m\le y$, write $a=mr$ with $r$ prime. Since $a>X$, $r>X/y>y$. Squarefree $z$-rough $m$ has one or two prime factors, and only $r$ contributes to $W(a)$. The weight equals $g(m)=1-\log m/L$ up to $O(H/(XL))$. Even counting all upper integers costs $o(K)$ in this replacement, since $m=a/r$ is unique. Set $g$ to zero outside the allowed cofactors.

Apply Cai–Lu Lemma 3 to $mr$ in $[X+2T+1,X+H+1)$ with auxiliary weight $g(m)$ and reduced residue $2X\bmod d$. Use base $x=X+2T+1$, $\theta=2/3$ and auxiliary exponent $1/10<1/6$. For each $m$, if $Y_m$ is the logarithmic-integral count of the primes $r$ in the divided interval, then uniformly
\[
  g(m)Y_m=(1+o(1))\,\frac{H}{mL}.
\]
The factor $1-\log m/L$ cancels the prime-density denominator. The lemma keeps the weighted sum over $m$ inside the absolute value before summing the errors over moduli. The moving bounded weight satisfies the hypotheses as in the [switched-cofactor argument](SwitchedWeightedCofactors.md#sifting-the-opposite-side-after-fixing-the-largest-prime). To apply the upper linear sieve to $n=2X-mr$, sieve at $\sqrt D$ and use the odd-prime density $1/(\ell-1)$. In the main terms, omitting $m$ not coprime to $d$ costs $o(K)$ in total, since each $m$ has at most two factors $\ell>z$ and $\sum_{\ell\mid d,\,d\le D}^{\rm squarefree}1/\varphi(d)\ll L/(\ell-1)$. All lower primes in $J$ survive. Mertens' product and $F(2)=e^\gamma$ give the coefficient $12$ in units of $K$.

Prime reciprocal summation gives $\sum_m 1/m\to u_*=\log3+J_3$. The prime cofactors contribute $\log3$. For a product of two distinct primes, in units of $\log z$ their exponents $s,t$ satisfy $s,t>1$, $s+t\le3$. The integral of $ds\,dt/(2st)$ over this triangle equals $J_3$ by grouping by $s+t$. The diagonal has reciprocal mass $O(1/z)$. Consequently $\limsup U/K\le12u_*$. Subtracting this upper coefficient from the lower coefficient for $R+C$ proves the last inequality in (1). This uses unrounded constants before subtraction. All weighted counts are nonnegative.

One may additionally discard the marks $y<r\le X^{11/100}$ from $B$. Their total over *all* rough upper sites with a genuine lower prime is at most $(2\log(20/17)+o(1))K$. To see this, fix $r$ and use the upper sieve at level $D/r$ with cutoff $\min(z,\sqrt{D/r})$, giving the integral $\int_{1/10}^{11/100}2\,dt/(1/6-t)$. Thus $R$ plus the remaining weight in $B$ exceeds $0.1230K$ eventually. Both the marked prime and its complementary factor are now large: $r>X^{0.11}$ and $a/r\ge a/P^+(a)>X^{0.1}$.

## Centering the two sectors on the same square

Let $w=\sqrt L$, $V_1(w)=\prod_{\ell\le w}(1-1/\ell)$ and $V_c(w)=\prod_{2<\ell\le w}(1-1/(\ell-1))$. Replace $P(n)$ by
\[
 A(n)=\frac{1_{P^-(n)>w}}{L V_1(w)}
\]
in $R,C,U,B$, writing $R_0,C_0,U_0,B_0$ for the results. The upper prime indicator and all upper composite weights retain their original definitions. This uses the same small-prime normalization as the [earlier reflection calculation](CentralPrimePairPacket.md), now with an explicit balance condition on the upper cofactor.

* For $R_0$, inclusion–exclusion over the odd primes up to $w$ among genuine upper primes gives the count $(H/L)V_c(w)(1+o(1))$ before the normalization in $A$. Every modulus of inclusion–exclusion divides the small primorial of size $X^{o(1)}$, and its discrepancy occurs only once in Cai–Lu Lemma 3 with auxiliary variable one. The lower endpoint is automatically odd. Since $V_c(w)/V_1(w)\to 2C_2$, $R_0/K\to1$.
* For $U_0$ apply the same inclusion–exclusion to the products $mr$ just used. All permitted $m$ are coprime to the small primorial. The main mass before the normalization is $V_c(w)\sum_m g(m)Y_m$, and the total absolute discrepancy is $O_A(H/L^A)$ with any fixed large exponent. Hence $U_0/K\to u_*$.
* For $C_0+R_0$ compute $S_A-T_A+o(K)$. First impose both roughness conditions up to $w$ by exact CRT. The density is $V_1(w)V_c(w)$, since just one residue is forbidden at 2 and two at each odd prime. At primes $w<\ell\le z$ only $a$ needs sifting. Use dimension-one upper and lower divisor weights of level $X^{1/2}$, so the parameter is 15. For either an additional $z<r\le y$ dividing $a$ or no mark, the CRT error per middle divisor and mark is $X^{o(1)}$ (the full small primorial suffices). Summed rounding is $O(X^{1/2+1/10+o(1)})=o(K)$. The middle local density is $1/\ell$. After including $A$ the ideal mass in $S_A$ is $(M+o(1))K$. The ideal mass in $T_A$ is $(M/15+o(1))K$ by $\sum_{z<r\le y}(\log r)/(rL)\to1/15$. Each relative deviation is bounded by $g_{15}+o(1)$, where $g_{15}=4/15!$. Indeed $f(15)\le1\le F(15)$ and $F(15)-f(15)=2e^\gamma\rho(14)/15$; the Dickman recursion gives $j\rho(j)\le\rho(j-1)$. Square exclusions cost $o(K)$ since $A(n)\ll1$. [Linear sieve](https://doi.org/10.4064/aa-37-1-307-320) · [Delay identity used here](LocalizedVaughanComparison.md)

In particular
\[
 \left|C_0/K-\bigl(14M/15-1\bigr)\right|
 \le (16M/15)g_{15}+o(1).
\]
Subtract the limit for $U_0$ to obtain (2). Combining (1) and (2) gives $R+(U-U_0)+(B-B_0)>0.6762K$ eventually. The [rational certificate](CheckBalancedPrimeCofactors.py) also bounds the ratio of the unrounded lower coefficient for $R+C$ to the upper coefficient for $C_0$ strictly above $1.0459$. The two-sector alternative follows by summing, without any independence assumption. These pointwise baseline counts use a prescribed sieve weight at the lower endpoint. An estimate comparing genuine lower primes with that weight on the two composite sectors would supply the additional arithmetic input.

In particular the centered large-cofactor sum has an exact bilinear form. Write $E(n)=P(n)-A(n)$. Then
\[
 B-B_0=\sum_{\substack{r>y\\r\ {\rm prime}}}\frac{\log r}{L}
 \sum_{\substack{m>y,\ \mu^2(m)=1,\ P^-(m)>z,\ (m,r)=1\\2X-mr\in J}}
 E(2X-mr).
\]
The formula with $1<m\le y$ gives $U-U_0$. Indeed if $a/P^+(a)\le y$, the only possible marked prime is $P^+(a)$; otherwise $a/r>y$ for every marked prime. Thus each marked factor is assigned to the right sector without imposing an ordering on the unknown factors of $m$. The no-pair hypothesis forces a relative excess on at least one of these two explicit sums.
