# Which upper factors can carry the signed prime-pair discrepancy?

Let $X=p^2$ for a sufficiently large odd prime $p$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $J=[X-H,X-2T)\cap\mathbb Z$, $h_0=H-2T$ and $a=2X-n$ for $n\in J$. Put $K=2C_2H/L^2$, where $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes. Write $P$ for the prime indicator and $R_G=\sum_{n\in J}G(n)P(a)$. All estimates below are at the prescribed center. These are paper deductions from published sieve inequalities.

For $z<y$, let
\[
 W_{z,y}(a)=\mathbf1_{\{a\ {\rm composite,\ squarefree},\ P^-(a)>z\}}
                 \sum_{\ell\mid a,\ \ell>y,\ \ell\ {\rm prime}}\frac{\log\ell}{L}.
\]
For a composite comparison set of lower sites with indicator $G$, put $\Delta W=\sum_{n\in J}(G(n)-P(n))W_{z,y}(a)$. The following table gives bounds for
\[
 \limsup_{p\to\infty}\frac{|R_P-R_G-\Delta W|}{K}. \tag{1}
\]

| Lower comparison set | Upper roughness $z$ | Marked upper prime factor $>y$ | Bound |
|---|---|---|---|
| The [original two-band semiprime set](SemiprimeDivisorTests.md) | $X^{1/360}$ | $X^{1/72}$ | $<0.0022$ |
| The two- or three-factor set defined below | $X^{1/30}$ | $X^{1/15}$ | $<0.15$ |
| The same two- or three-factor set | $X^{1/30}$ | $X^{1/12}$ | $<0.312$ |

The first row keeps the original $R_G$. The other rows use a different indicator, still supported entirely on squarefree composites of full [Richert weight](SwitchedWeightedCofactors.md). In the last two rows any contributing upper integer has at most 30 prime factors and must contain a prime above the marked cutoff. The weight in $\Delta W$ and its sign are essential. A pointwise lower bound $R_G+\Delta W\ge (b+\varepsilon)K$, with $b$ the applicable bound and fixed $\varepsilon>0$, would give genuine central pairs. The earlier $0.34K$ lower bound concerns a different count and does not supply this inequality.

## Localizing the signed remainder

Suppose both lower indicators separately have main term $h_0/(L\varphi(d))$ in reduced classes with sum of maximum absolute errors $O_A(HL^{-A})$ through $D=X^\delta$. All sites in both sets are odd. Write $z=X^\lambda$, $y=X^\eta$, $0<\lambda<\eta$, $\lambda+\eta<\delta$, $(\delta-\eta)/\lambda>2$, and $F=G-P$. On $a$ use Vaughan's identity with the $\mu$ and $\Lambda$ cutoffs both at $z$. The argument for [equation (3) in the preceding note](SemiprimeDivisorTests.md) absorbs the short terms, since $z^2<D$. In the last convolution write $jk=a$ with $k>z$ carrying $\Lambda(k)$. For $z<k\le y$, $j>1$ and $\sum_{e\mid j,e>z}\mu(e)=-\sum_{e\mid j,e\le z}\mu(e)$. Thus this whole range is a sum of tests $ke\mid a$ with $ke\le zy<D$ and coefficients of magnitude at most $\log(ke)$ after grouping. Its signed total is $O_A(HL^{-A})$. More generally this works for bounded additional weights depending on $k$. With the **exact original cutoffs** $z=X^{1/72}$ in the preceding (3), this already removes the columns $z<k\le X^{11/720-\epsilon}$ for every fixed $0<\epsilon<1/720$, by its original level $\delta<7/240$.

Let $V_{z,y}(a)=\sum_{jk=a,\ j>z,\ k>y}\Lambda(k)\sum_{e\mid j,e>z}\mu(e)$. Its signed total is $L(R_G-R_P)+O_A(HL^{-A})$. At primes it vanishes. At a squarefree $z$-rough composite its value is exactly $-LW_{z,y}(a)$: for each prime $k>y$ dividing $a$, $j>1$ is rough and its only divisor $\le z$ is 1. Rough nonsquarefree sites are negligible even with this convolution weight. Indeed some prime $\ell>z$ has $\ell^2\mid a$, giving $O(H/z+\sqrt X)$ sites, and the divisor bound gives $|V_{z,y}(a)|\le X^{o(1)}$. Replacing $\log a$ by $L$ costs a power-saving error. Consequently (1) is also an upper bound on the absolute **net** contribution of all $P^-(a)\le z$ to this high-column convolution, in units $LK$.

It remains to bound the error without an assumption about true upper primes. Write $S_z(a)=\mathbf1_{P^-(a)>z}$. On squarefree rough composites the logs of the prime factors sum to $\log a$. On upper primes the factor itself exceeds $y$. These facts give
\[
 R_P-R_G-\Delta W =
 -\sum_{n\in J}F(n)S_z(a)
 +\sum_{z<\ell\le y}\frac{\log\ell}{L}
       \sum_{n\in J,\ \ell\mid a} F(n) S_z(a)
 +O_A(H L^{-A}), \tag{2}
\]
where the outer sum is over primes. Apply the one-dimensional upper and lower linear sieves to each **nonnegative** lower set separately. At odd sieve primes the density is $1/(\ell-1)$, since $d\mid a$ prescribes the reduced residue $2X\bmod d$ for odd $d<D<p$. At 2 no removal is needed. The common sieve product is $(2C_2e^{-\gamma}+o(1))/\log z$. The largest possible absolute difference of two counts bracketed by the same bounds is one bracket width. [Cai–Lu, *Chen's theorem in short intervals*, Lemmas 1–2](https://bibliotekanauki.pl/articles/1216105.pdf#page=2)

Write $F_1,f_1$ for the linear sieve functions and $\rho$ for the Dickman function, with $\rho(v)=1$ on $[0,1]$ and $v\rho'(v)=-\rho(v-1)$ above 1. Subtracting the two delay equations gives $s(F_1(s)-f_1(s))=2e^\gamma\rho(s-1)$ for $s\ge2$, by the initial values and successive unit intervals. The first term of (2), divided by $K$, has limsup at most $(2/\delta)\rho(\delta/\lambda-1)$. For the marked term fix $\ell=X^u>z$. The common starting mass acquires $1/(\ell-1)$, and the remaining level is $D/\ell$. The small sieve primes are distinct from $\ell$. In all the summed remainder bounds the modulus $\ell d$ recovers its marked prime uniquely, since every prime of $d$ is at most $z$. This justifies summing absolute errors. The sieve asymptotics are uniform on the compact parameter range in use. Prime partial summation gives the additional width
\[
 \int_\lambda^\eta\frac{2}{\delta-u}\rho\!\left(\frac{\delta-u}{\lambda}-1\right)du
 =2\left[\rho\!\left(\frac{\delta-\eta}{\lambda}\right)
         -\rho\!\left(\frac{\delta-\lambda}{\lambda}\right)\right].
\]
For the first row take $\delta=1/36$. The total is $70\rho(9)+2\rho(5)<0.0022$. For the remaining rows let $\delta\uparrow1/6$ **after** taking the limsup at fixed $\delta$. The totals are $10\rho(4)+2\rho(3)$ and $10\rho(4)+2\rho(5/2)$. The [rational checks](CheckLocalizedVaughan.py) give $\rho(4)<0.005$, $\rho(3)<0.05$ and $\rho(5/2)<0.131$. The bound $v\rho(v)=\int_{v-1}^v\rho(t)dt\le\rho(v-1)$ gives $\rho(9)\le1/9!$ and $\rho(5)\le\rho(4)/5$.

## A composite set with distribution through every fixed level below $1/6$

Put $c=17/50$, $b=33/200$, and set
\[
 I=\int_c^{1/2}\frac{1+\log(6v-1)}{v(1-v)}\,dv,\qquad
 \frac{\alpha}{1-\alpha}=\frac{b}{1-b}\exp(I-1).
\]
Here $0.92<I<0.93$ and $3/20<\alpha<b<1/6$. Define $G(n)=1$ in the following two cases and zero elsewhere:

* $n=qt$ with $q,t$ prime and $X^\alpha\le q\le X^b$, $q<t$.
* $n=mt$, $X^c\le m\le\sqrt{X-H-1}$, $t$ prime, and $m$ either prime or a product of two distinct primes both exceeding $X^{1/6}$.

In the second case $t>m$ is the unique largest prime. The semiprime bands are disjoint and a three-prime product has only one eligible $m$. Every prime factor in either case exceeds $X^{3/20}$. The density of the small band relative to primes is $\log((b/(1-b))/(\alpha/(1-\alpha)))=1-I$. In the balanced range the relative density is $I$. The term 1 in its numerator counts prime $m$. For $m=q_1q_2$ at total exponent $v$, the unordered reciprocal prime measure has density
\[
 \tfrac12\int_{1/6}^{v-1/6}\frac{du}{u(v-u)}=\frac{\log(6v-1)}v.
\]
The prime $t$ supplies $1/(1-v)$. Each combined main term is accurate to arbitrary inverse powers of $L$ by the classical prime number theorem with logarithmic remainder and partial summation. For the prime-pair integral one can perform the inner prime sum first, uniformly for the moving endpoints within the fixed exponent ranges, then the outer sum on the finitely many smooth pieces. Repeated primes have reciprocal mass $O(X^{-1/6})$. The change from $\sqrt X$ at the top costs $O((1+H/\sqrt X)/\sqrt X)$ in reciprocal mass since the integers $m$ have multiplicity one. These calculations give the common total main term $h_0/L$.

The small band satisfies the required progression estimate by Cai–Lu Lemma 3 at $\theta=2/3$, with prime auxiliary coefficient supported below $X^b$. When a marked $q$ divides the modulus, the reduced class has no term from $q$. Restoring its reciprocal main term costs at most $O(H L^{O(1)}\sum_{q>X^\alpha}q^{-2})$ in total since $\sum_{d\le D,\ q\mid d}1/\varphi(d)\ll L/(q-1)$. The same lemma with auxiliary variable 1 supplies the estimate for $P$. [Cai–Lu, Lemma 3, p. 313](https://bibliotekanauki.pl/articles/1216105.pdf#page=3)

For clarity, the balanced part also reaches $D=X^\delta$ for **every fixed** $\delta<1/6$. For conductors $r\le L^C$ its sharp-interval reduced class counts have main term $h_0\sum_m[m\log(X/m)]^{-1}/\varphi(r)$ and error $O_B(HL^{-B})$ for arbitrary $B$. This uses the overlap estimate for *all* integers $m$ from the [previous derivation](SemiprimeDivisorTests.md), restricted to the indicated subset. For each $m$ the class of $t$ is determined by the inverse of $m$. Hence the nonprincipal character sums for this range are $O_B(\varphi(r)HL^{-B})$. The case $r=1$ supplies the principal mass. [Koukoulopoulos, Theorem 1.2](https://dms.umontreal.ca/~koukoulo/documents/publications/shortaps.pdf#page=3)

For larger conductors all prime factors of $mt$ on the balanced branch exceed $D$, so every induced character has the same value here as its primitive character. The levels lost to small prime factors in the first branch have already been accounted for separately. In character orthogonality the sum over the moduli inducing a given primitive character has coefficient $\sum_{d\le D,r\mid d}1/\varphi(d)\ll L/\varphi(r)$. Thus in a dyad $R<r\le2R$ the required weight is $O(L^2/R)$ per primitive character.

Here are details of the short interval and time cutoff. Replace its hard indicator by a smooth weight supported inside it, equal to 1 except in end strips of width $\Delta=H/L^B$, using rescaled smooth transitions. The aggregate cost **in residue counts before character expansion** is $O(\Delta\log(2D)+D)$ since $G\le1$. Its effect on the principal mass is $O(\Delta)$ and on all small-conductor contributions is $O(\Delta L^{O(C)})$. Take $B$ large after $C$. On writing the weight as a function of $\log(n/X)$, its Fourier transform is $O_j((H/X)(1+|\tau|\Delta/X)^{-j})$ by integration by parts. Frequencies above $V=X^{1/3+\kappa}$ then cost a power saving of arbitrary fixed order by choosing $j$ large. Here $0<\kappa<\min(c-1/3,1/6-\delta)$ is fixed; the polynomial saving absorbs all fixed powers coming from $\Delta$.

On $m\asymp M$, $t\asymp N$ with $MN\asymp X$, the separated sums have coefficients of modulus at most one. Dyadic rectangles with $MN\asymp X$ cover the support; the product cutoff is still imposed by its Fourier transform. The primitive hybrid large sieve bounds the character sum and time integral of the squared polynomial at scale $M$ by $O((M+R^2 V)M)$ and similarly at $N$. Cauchy–Schwarz, the transform bound $H/X$, and the conductor weight above give an error per dyad, divided by $H$, of at most
\[
 O\!\left(L^2\left[\frac1R+\sqrt{V/M}+\sqrt{V/N}+RV/\sqrt X\right]\right).
\]
The last three terms save a power because $M\gg X^c$, $N\gg X^{1/2}$ and $R\le D$. The $1/R$ term absorbs every required logarithm by taking $R\ge L^C$ with $C$ large enough. The number of dyadic rectangles and conductor shells costs only logarithms. This proves the asserted summed maximum discrepancy for the balanced branch and completes the input to (2). [Montgomery–Vaughan, Theorem 26.16, equation (26.22), with its proof](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)

The estimate concerns real upper primes through (1) and real factor bands through $W_{z,y}$. It does not give a lower bound for $R_G+\Delta W$ at an exceptional prescribed square.
