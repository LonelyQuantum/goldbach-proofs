# Five prime factors in the reflected short interval

Let $p$ be an odd prime, $X=p^2$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $I=(X+2T,X+H]$, $h=H-2T$, $n=2X-a$, and $L=\log X$. Define $K=2C_2H/L^2$ with $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes. Fix $s=67/400$. Let $\mathcal F$ consist of upper integers $a\in I$ with exactly five prime factors, counted with multiplicity, all $>X^s$. For $1/3<\beta<1-3s$, let $\mathcal Q_\beta$ consist of those with exactly four such factors and largest factor $>X^\beta$. The latter factor is unique for large $X$ because $2\beta+2s>1$. All limits are along prime $p\to\infty$.

For a sector $E$ write $N_f(E)=\sum_{a\in E}f(2X-a)$, $P(n)=1_{n\ {\rm prime}}$ and $P_\kappa(n)=1_{P^-(n)>X^\kappa}$, $\kappa=1/18$. The reference is $A(n)=1_{P^-(n)>\sqrt L}/(L\prod_{\ell\le\sqrt L}(1-1/\ell))$. For $E=\mathcal F$ or $\mathcal Q_\beta$ the following bounds hold at the prescribed center:

$$
\frac{N_A(E)}{K}\longrightarrow c_E,\qquad
12\log(2)c_E\le\liminf\frac{N_{P_\kappa}(E)}{K}
\le\limsup\frac{N_{P_\kappa}(E)}{K}\le12c_E. \tag{1}
$$

In particular, $N_{P_\kappa}(\mathcal F)<0.01119K$ eventually throughout the full five-factor range. The upper bound applies also to true lower primes. The lower bound counts rough lower integers. We derive these estimates using the prime-polynomial bound of Pliego–Sun–Wang and a hybrid large sieve.

## Distribution in reduced residue classes

Write $c_5=c_{\mathcal F}$ and $c_4(\beta)=c_{\mathcal Q_\beta}$. With $u_5=1-\sum_{i=1}^4u_i$ and $u_4=1-\sum_{i=1}^3u_i$ in the respective integrals, these numbers are

$$
c_5=\frac1{5!}\int_{u_1,\ldots,u_5>s}\frac{du_1\cdots du_4}{u_1\cdots u_5},
\qquad
c_4(\beta)=\frac1{3!}\int_{u_1,u_2,u_3>s,\ u_4>\beta}
                \frac{du_1du_2du_3}{u_1u_2u_3u_4}. \tag{2}
$$

As a normalization check, $\sum_i u_i=1$ makes $1/\prod_i u_i$ the sum of the five reciprocals with one factor omitted. On the five-factor simplex these five terms have equal integrals by permutation symmetry (the coordinate-change Jacobian has absolute value one). Equivalently $c_5$ is $1/4!$ times the integral with the fifth denominator omitted.

For every fixed $0<\delta<1/6$ and every $A_0>0$, we obtain

$$
\sum_{d\le X^\delta}\max_{(b,d)=1}
\left|\#\{a\in E:a\equiv b\bmod d\}
       -\frac{h c_E}{L\varphi(d)}\right|\ll_{\delta,\beta,A_0} H L^{-A_0}. \tag{3}
$$

**Set-up.** Count labelled prime products divided by the factorial in (2), labelling the distinguished large factor last in the four-factor case. This gives weights at most one and agrees with the indicator on squarefree integers. For repetitions there is an $\ell>X^s$ with $\ell^2\mid a$. For a reduced class the square divisor either gives no sites or a single residue modulo $d\ell^2$. Their total discrepancy cost on passing to the indicator is $O(H X^{-s}\log(2X)+X^{\delta+1/2})$, by summing the upper bound $H/(d\ell^2)+1$. Both terms save a power. Every factor exceeds $D=X^\delta$, so characters induced on these products agree with their primitive characters.

Choose $0<\epsilon<\min(2s-1/3,1/6-\delta,\beta-1/3)$, omitting the last constraint for five factors. Set $V=X^{1/3+\epsilon}$. Replace the window indicator by a smooth weight equal to one except within its two end strips of width $\Delta=H/L^B$, supported inside $I$ and bounded by one. In (3) this changes counts by $O(\Delta\log(2D)+D)$, using the interval length in each residue class. The exponent $B$ may be arbitrarily large. The Fourier transform in $\log(a/X)$ is $\ll_j(H/X)(1+|t|\Delta/X)^{-j}$, so frequencies $|t|>V$ are negligible to any fixed power of $X$ after choosing $j$. Split each prime range into truncated dyadic intervals $(M_i,2M_i]$ with $M_i\gg X^s$, imposing the fixed lower cutoffs inside the boxes. Only $O(L^5)$ boxes with $\prod_i M_i\asymp X$ meet the window. There is no ordering restriction inside a box. The factorial and the unique distinguished factor give the stated multiplicities.

**Large conductors.** By orthogonality a primitive character of conductor $r$ carries weight at most $\sum_{d\le D:r\mid d}1/\varphi(d)\ll L/\varphi(r)$. For $R<r\le2R$ this is $O(L^2/R)$. In the five-factor case group the factors as two and three; for four group the distinguished factor against the other three. The two product lengths $M,N$ both exceed $V$ by a fixed power of $X$ and $MN\asymp X$. The coefficients of each grouped Dirichlet polynomial are bounded by a factorial, by unique factorization. The hybrid large sieve bounds its integrated square over primitive characters in this conductor shell and $|t|\le V$ by $O((M+R^2V)M)$, and likewise for $N$. Cauchy–Schwarz and the transform bound $H/X$ give a contribution per box and shell, divided by $H$, of at most

$$
\ll L^2\left(R^{-1}+\sqrt{V/M}+\sqrt{V/N}+RV/\sqrt X\right).
$$

The last three terms save a power uniformly to $R\le D$; in particular $\delta+\epsilon<1/6$. The first saves any required power of $L$ for $R\ge L^C$, by choosing $C$ after $A_0$ and the box and shell counts. [Montgomery–Vaughan, Corollary 26.4 and Theorem 26.16, equation (26.22)](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)

**Small conductors.** For five factors peel off one prime and group the other four as two pairs. For four peel off an undistinguished prime and group the remaining factors as the distinguished prime and the small pair. Both remaining lengths $M,N$ exceed $V$ by a power. For each character, the ordinary Dirichlet-polynomial mean-value theorem and Cauchy–Schwarz give
$$
\int_{-V}^V |F_M(t)F_N(t)|\,dt\ll MN.
$$
For the peeled prime polynomial of length $U$, on any subinterval of its dyadic range one has $\left|\sum_q\chi(q)q^{-it}\right|\ll_J U L^{-J}$ for every fixed $J$, uniformly for nonprincipal primitive conductors $r\le L^C$, $|t|\le V$. The same bound holds for the principal character at $L^{J+3}\le |t|\le V$. In Lemma 3.1 of Pliego–Sun–Wang choose $\theta=3/4$ and the fixed integer in the conductor range large enough that $100k\log k>C$. The lower prime cutoff exceeds $\exp(L^\theta)$. Partial summation removes the reciprocal prime from the lemma; the extra principal term is $O(UL/(1+|t|))$. Thus these integrals after Fourier inversion cost $\ll H L^{-J}$ per box and character. The total induction weights at these conductors cost only a fixed power of $L$. [Pliego–Sun–Wang, *Local divisor correlations in almost all short intervals*, arXiv:2503.02962v1, Lemma 3.1, pp. 5–7](https://arxiv.org/pdf/2503.02962v1#page=5)

Only the principal character at $|t|<L^{J+3}$ remains. Replace each prime sum by $\int y^{-it}dy/\log y$ on the same truncated interval. The prime number theorem with logarithmic remainder and partial summation give error $O(U_i L^{-J'})$ for arbitrary $J'$ here, by using enough logarithmic saving before partial summation. Multiplying out, integrating over this polylogarithmic range, and summing boxes costs $O(HL^{-A_0-3})$ with suitable choices. The analogous continuous transforms on dyadic intervals are $O(M_i/(1+|t|))$ by integration by parts; extending their product to all frequencies costs an arbitrarily small log-power error by taking $J$ large. Their full inverse transform is precisely the product integral with measure $\prod_i dy_i/\log y_i$. Removing the smoothing changes this integral by $O(\Delta)$: at each product value near $X$ its density is $O(1/L)$ as computed below. All choices may be made in the order $C,J,B$ sufficiently large compared with the desired saving, then sufficiently many integrations by parts for the Fourier tail.

In the product integral change variables to $a=\prod_i y_i$ and $u_i=\log y_i/L$ for all but the final factor. The inner integral multiplying $da/L$ is (2) with the sum constraint equal to $\log a/L$. It differs from $c_E$ by $O(H/(XL))$ uniformly: all denominators are bounded away from zero and the moving simplex face changes a region of volume $O(H/(XL))$. This proves (3) including its main term. The large-conductor and small-conductor inputs control the specified window directly; no averaging over centers is used.

## Sieve and constants

For each odd squarefree sieve divisor $d\le D$, $d\mid n$ corresponds to the reduced upper class $2X\bmod d$. All upper sites and their reflections are odd. The density at odd $\ell$ is $1/(\ell-1)$. Its survival product up to $z=X^{1/18}$ is $(2C_2 e^{-\gamma}+o(1))/\log z$. Apply the upper and lower dimension-one linear sieves with level $X^\delta$ for fixed $1/9<\delta<1/6$. With $v=18\delta\in(2,3)$ their functions are $2e^\gamma/v$ and $2e^\gamma\log(v-1)/v$. Equation (3) controls their remainders with arbitrary log saving. Taking the limit in $X$ first and then $\delta\uparrow1/6$ gives the rough-site bounds (1). For $A$, exact inclusion–exclusion up to $\sqrt L$ uses only divisors of a primorial of size $X^{o(1)}$. After division by its Mertens product the local factor tends to $2C_2$. This gives the first limit in (1). [Matomäki, §2, Rosser–Iwaniec sieve](https://users.utu.fi/ksmato/wp-content/uploads/sites/1432/2025/04/Goldbach_k2pl2p1.pdf#page=3)

Put $b=1-5s$. On the five-factor simplex, $s^4(1-4s)\le\prod u_i\le5^{-5}$: the lower bound follows by expanding $\prod(s+x_i)$ with $\sum x_i=b$, and the upper by AM–GM. Its volume in the four independent coordinates is $b^4/24$. Therefore
$$
0.00075660 < \frac{5^5 b^4}{5!\,4!}\le c_5
\le\frac{b^4}{5!\,4!\,s^4(1-4s)}<0.00093207.
$$
For four factors let $y=u_1+u_2+u_3-3s$. Their product is at least $s^2(s+y)$. The simplex slice measure in $dy$ is $y^2/2$, so
$$
c_4(\beta)\le\int_0^{1-3s-\beta}\frac{y^2\,dy}{12s^2(s+y)(1-3s-y)} .
$$
The integrand increases. Exact right-endpoint sums on 2,048 equal intervals with upward rational rounding give $c_4(2/5)<0.00904$ and $c_4(9/25)<0.02434$.

## Consequences for reflected partners

* Retain all assumptions of the [monotone replacement estimate](SwitchedSemiprimeStrip.md#where-a-rough-monotone-replacement-would-have-to-go). It places more than $0.3457K$ insertions opposite composites with at most five prime factors, all above $X^s$. After excluding the whole five-factor class using (1), more than $0.3345K$ insertions must be opposite products of **two to four** primes above $X^s$. After also excluding $\mathcal Q_{9/25}$, more than $0.0424K$ must have two or three factors, or four with largest at most $X^{9/25}$.
* For **actual primes**, start from the [signed estimate outside the original semiprime strip](SwitchedSemiprimeStrip.md). Its $R$ counts prime pairs with $a\in I$, and its composite term sums $W(a)(P(n)-A(n))$ with the weight defined there. On the squarefree part of either new sector $W(a)=\log(a)/L=1+O(H/(XL))$; repeated-factor sites cost $o(K)$. By (1), omitting either sector costs at most $(11c_E+o(1))K$ in the signed lower bound. After omitting both $\mathcal F$ and $\mathcal Q_{2/5}$ as well as the original strip, **$R$ plus the remaining signed excess exceeds $0.0297K$** eventually. If one instead keeps all four earlier semiprime/three-/four-factor rows of the [ordered-factor table](OrderedPrimeFactors.md) excluded and replaces its fifth row by all of $\mathcal F$, the margin exceeds $0.08865K$. These are two distinct remaining regions. Neither estimate gives $R>0$ by itself.

At four factors near $X^{1/4}$ the large-conductor $2+2$ grouping still works. After peeling one prime at small conductor, the remaining $1+2$ grouping has a singleton of length $X^{1/4+o(1)}$. The mean-value argument used above then loses a factor $X^{1/24+O(\epsilon)+o(1)}$. A stronger small-conductor estimate for this four-prime product would go beyond the present grouping argument.

[Rational bounds and finite convolution checks](CheckFivePrimeDistribution.py)
