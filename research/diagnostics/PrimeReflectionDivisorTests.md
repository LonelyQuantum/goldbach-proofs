# Which cofactor excess can reduced progression counts detect?

Let $p$ be a large prime, $X=p^2$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $J=[X-H,X-2T)\cap\mathbb Z$ and $a=2X-n$. Write $P$ for the genuine prime indicator, $K=2C_2H/L^2$ with $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$, $z=X^{1/30}$ and $y=X^{1/10}$. For a lower weight $f(n)$, $R(f)=\sum_J f(n)P(a)$. On squarefree $z$-rough composite upper integers put $W(a)=\sum_{r\mid a,\ r>y}\log(r)/L$ over primes; elsewhere put $W=0$. Write $U(f)$ and $B(f)$ for $\sum_J f(n)W(a)$ with $a/P^+(a)\le y$ and $>y$, respectively. The [previous 4.59% alternative](BalancedPrimeCofactors.md) concerns these two sums at one fixed square.

## A divisor identity for the true primes

For every integer $a$ define
\[
 F(a)=\sum_{\substack{z<q\le y\\q\mid a}}(1-\log(q)/L)
       -\sum_{\substack{z<q<t,\ qt\le y\\qt\mid a}}1 ,
\]
with prime $q,t$. Let $\mathcal U$ be the upper integers in the small-cofactor sector. For $a\in\mathcal U$ put $m=a/P^+(a)$. All the primes of $m$ lie in $(z,y]$, and $m$ has one or two distinct factors since $y=z^3$. The largest prime exceeds $y$. Thus $F(a)=1-\log(m)/L$ exactly, including the two-factor case, whereas $W(a)=F(a)+\log(a/X)/L$. On upper primes and on upper integers with every prime factor above $y$, $F=0$.

Use the previous lower reference $A(n)=1_{P^-(n)>\sqrt L}/(L V(\sqrt L))$, where $V(v)=\prod_{\ell\le v}(1-1/\ell)$. At each square,
\[
 U(P)-U(A)
 =-\sum_{\substack{n\in J\\2X-n\notin\mathcal U}}(P(n)-A(n))F(2X-n)+o(K). \tag{1}
\]
Indeed, divisors tested by $F$ are primes $q$ or products $qt\le y$. In each case $d\mid a$ specifies the reduced class $n\equiv2X\bmod d$. Cai–Lu Lemma 3 at auxiliary variable one gives total prime discrepancy $O_M(H/L^M)$ relative to $|J|/(L\varphi(d))$ for any fixed $M$, also after freezing the logarithm. Each tested modulus occurs once. For $A$, exact CRT with the primorial up to $\sqrt L$ gives $|J|/(Ld)$ with summed rounding $X^{1/10+o(1)}$. The relative main-term difference is $O(1/z)$ since $d$ has at most two prime factors and both exceed $z$. Hence $\sum_J(P-A)F=o(K)$. The log replacement on $\mathcal U$ costs $O(H^2/(XL))=o(K)$. Identity (1) transfers a small-cofactor excess to other upper integers containing a prime in $(z,y]$. Its right side is signed. [Cai–Lu, Lemma 3, p. 313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=3)

## A pair of binary lower sets at each prescribed center

Fix $1/10<\delta<1/6$, and $D=X^\delta$. For each sufficiently large $p$ there are two equally large sets $E_0,E_1\subset J$ of squarefree integers with least prime factor greater than $w=\exp((\log L)^2)$. For $i=0,1$ and every fixed $M>0$,
\[
 \sum_{d\le D}\ \max_{(b,d)=1}\ \max_{I\subset J}
 \left|\sum_{\substack{n\in I\\n\equiv b\bmod d}}(1_{E_i}(n)-P(n))\right|
 \ll_{\delta,M} H/L^M , \tag{2}
\]
where $I$ ranges over integer intervals. The same choice of sets works for all $M$ at the fixed $\delta$. Keep the actual upper primes and factorization fixed. The two sets agree **site by site** opposite every member of $\mathcal U$, yet
\[
 R(1_{E_0})=(1+o(1))K,\qquad R(1_{E_1})=0,\qquad
 B(1_{E_1})-B(1_{E_0})=(1+o(1))K . \tag{3}
\]
All added sites have an upper partner which is a product of two genuine primes both exceeding $D$. The construction changes the lower prime indicator to test the information in (2). It gives no counterexample for the actual lower primes.

The baseline can also be chosen with $U(1_{E_0})/K\to u_*\in(1.2458,1.2459)$ and $13.4740<B(1_{E_0})/K<13.4761$, in the normalization of the previous calculation. Thus the balanced sum in the zero-pair set exceeds its baseline by more than 7.4%, with exactly zero change in the small-cofactor sum.

**The supply of upper semiprimes.** Choose fixed $\delta<u<v<1/6$, put $\mathcal Q=\{q\ {\rm prime}:(2X)^u<q\le(2X)^v\}$, and let $G(a)$ indicate $a=qt$ with $q\in\mathcal Q$ and $t$ prime. Throughout the upper window $t>(2X)^v$, so this representation is unique. Set
\[
 c_X=\sum_{q\in\mathcal Q}\frac{L}{q\log(X/q)}
 \longrightarrow \log\frac{v(1-u)}{u(1-v)}>0.
\]
For any fixed $\delta<\delta'<u$, the discrepancy of $G/c_X-P$ summed over moduli through $X^{\delta'}$, with the maximum over **all** classes and upper subintervals, is $O_M(H/L^M)$. For reduced classes apply Cai–Lu Lemma 3 at base $2X$, $\theta=2/3$, with arithmetic function $1_{\mathbb P}$ and take the difference between its two fixed auxiliary exponents $u$ and $v$. Both are admissible. Any upper subinterval starts in $[X,2X]$ and has length at most $H$. All permitted $q$ are coprime to each tested modulus. For an interval of length $h$, the main term from each $q$ is its divided logarithmic integral over that interval, equal to $h/(q\log(X/q))$ with relative error $O(H/(XL))$. Freezing the logarithm for upper primes incurs the same type of error. Sum these errors using $\sum_{d\le X^{\delta'}}1/\varphi(d)\ll L$. Nonreduced classes contain neither an upper prime nor one of these products because their factors exceed $X^{\delta'}$. Prime reciprocal summation gives the displayed limit for $c_X$; the exact $c_X$ is used in the discrepancy. [Cai–Lu, *Chen's theorem in short intervals*, Lemma 3](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=3)

**Lower reference and the transfer of progression bounds.** Put $A_*(n)=1_{P^-(n)>w}/(L V(w))$ and $S(n)=\mu^2(n)A_*(n)$. Both are $o(1)$ uniformly by Mertens' product theorem. To verify (2) in expectation first for $S$ alone, bracket the lower roughness indicator by adjacent Bonferroni sums of orders $j,j+1$, $j=\lceil\log L\rceil$. For a reduced class mod $d$, only small-prime divisors $k$ coprime to $d$ contribute. Summed over $d$, the errors from integer rounding are $O(D w^{j+1})=X^{\delta+o(1)}$. The total gap in the main terms is at most $O(H\log(2D))(\sum_{\ell\le w}1/\ell)^{j+1}/(j+1)!$, smaller than $H/L^M$ for every fixed $M$. This gives the normalized main term
\[
 \frac{|I|}{Ld}\prod_{\ell\mid d,\ \ell\le w}(1-1/\ell)^{-1}.
\]
Extending the product over all $\ell\mid d$ changes it by relative $O(L/w)$, negligible at arbitrary logarithmic precision. This is the prime main term by Cai–Lu with base $X$. Deleting squares on the surviving rough sites, uniformly in reduced classes and intervals, costs in the summed test $O(H\log(2D)/w+D\sqrt{2X})$. Indeed for $\ell>w$, $(\ell,d)=1$ there are at most $H/(d\ell^2)+1$ multiples of $\ell^2$ in the class; if $\ell\mid d$ there are none. Here $\delta+1/2<2/3$. The same deletion estimate applies with any uniformly bounded multiplier.

Next put $F_0(a)=G(a)/c_X-P(a)$. The lower sequence $S(n)F_0(2X-n)$ has summed discrepancy $O_M(H/L^M)$ against zero in (2). To see this, first omit the squarefree condition at the cost just proved. Expand the lower roughness indicator to order $j$. The error for this signed multiplier is bounded by its uniform norm times the integer $(j+1)$-hit count estimated above. Each compatible term $k$ now selects one upper residue class modulo $d k\le D w^j<X^{\delta'}$. A nonunit upper class contributes zero. Let $e_l$ be the maximum upper discrepancy of $F_0$ at modulus $l$ including the interval maximum. The number of occurrences of $l=dk$ is at most $\tau(l)$, and
\[
 \sum_{l\le X^{\delta'}}\tau(l)e_l
 \le\Big(\sum_l e_l\Big)^{1/2}\Big(\sum_l\tau(l)^2e_l\Big)^{1/2}
 \ll_M H/L^M .
\]
Indeed $e_l\ll H/l+1$ since both sequences are bounded, and the second sum is $O(H L^{O(1)})$ by $\tau^2\le d_4$ and elementary divisor summation. Use any required logarithmic saving in the first sum. This treats collisions among the moduli without charging the entire small primorial.

**Matching the number removed and added.** Write $s_P=\sum_J S(n)P(a)$ and $s_G=\sum_J S(n)G(a)$. Then $s_P/K\to1$. To verify this, expand the roughness indicator among genuine upper primes by the same Bonferroni bracket. Odd primes $\ell\le w$ exclude one reduced class with local density $1/(\ell-1)$ and the prime 2 incurs no loss. Use Lemma 3 at auxiliary variable one for the moduli $k\le w^{j+1}$, each occurring once. The product main term before lower normalization is $(|J|/L)\prod_{2<\ell\le w}(1-1/(\ell-1))$, with arbitrarily small logarithmic errors by the factorial bound. The ratio of this product to $V(w)$ tends to $2C_2$. The square deletion is negligible. From the transfer at $d=1$ we have $s_G/c_X-s_P=O_M(H/L^M)$. Thus
\[
 t_X=s_P/s_G=1/c_X+O_M(L^{-M}),\qquad
 Z(n)=S(n)\bigl(1-P(a)+t_XG(a)\bigr)
\]
is well defined for large $p$. Replacing $1/c_X$ by $t_X$ costs $O_M(H/L^M)$ in the summed test, using the elementary bound $\sum_{d\le D}(H/d+1)$. Consequently $Z$ and $S$ both pass (2) as weights and have exactly equal total mass. On upper primes $Z=0$, on the tagged semiprimes $Z=(1+t_X)S$, and elsewhere $Z=S$. As $t_X$ stays bounded and $\sup S=o(1)$, both weights lie in $[0,1]$ eventually.

**Passing to sets.** At each $n$ independently draw a uniform number on $[0,1)$ and use that same number for the two thresholds $S(n),Z(n)$, accepting below the threshold. For each set and each interval/class test Hoeffding's inequality bounds the rounding error by $O(\sqrt{(H/d+1)L})$ simultaneously with positive probability: the number of tests is $O(H^2D^2)$, so a sufficiently large absolute constant suffices in the union bound. Impose also $O(\sqrt{HL})$ errors on the counts of removed sites and added sites, each a sum of independent Bernoulli variables of mean $s_P$. On this outcome the total rounding loss in (2) is $O(\sqrt{HDL}+D\sqrt L)$. Trim the larger of the two edit lists to equalize their sizes, discarding the surplus sites from the set that alone contained them. This costs at most $O(D\sqrt{HL})=o(H/L^M)$ in (2). The sets now have equal cardinality. The reference-only sites are precisely its partners of upper primes, the other-only sites lie opposite the tagged semiprimes, and there are $(1+o(1))K$ of each. On the latter $W(a)=\log(a)/L=1+o(1)$. On every site opposite $\mathcal U$ the thresholds and the final memberships agree. This proves (3). [Hoeffding's inequality, Theorem 2](https://doi.org/10.1080/01621459.1963.10500830)

For the last two baseline bounds use the [two sector calculations](BalancedPrimeCofactors.md#centering-the-two-sectors-on-the-same-square) for $A_*$ and then $S$. In the small-cofactor sum, each $m\le y$ is coprime to the primes up to $w$ and Cai–Lu gives the same product of odd local factors as for $s_P$, with initial mass $\sum_m (1-\log(m)/L)Y_m$ in the notation of that calculation. Replace its small-primorial expansion by the bracket above; the gap on integers times the bounded upper weight is $O_M(H/L^M)$. For $B$ the simultaneous pre-sieve on $n,a$ uses at most two forbidden residues per small prime. After fixing a middle divisor $e$ and optional mark $r$, the gap before rounding is bounded by $O(H/(er))(\sum_{\ell\le w}2/\ell)^{j+1}/(j+1)!$, and rounding costs $X^{o(1)}$ per progression (even counting $2^{j+1}$ residues per divisor). Here all prime factors of $er$ exceed $w$. As before $e\le X^{1/2}$ and $r\le X^{1/10}$ for the small-factor log sum, so the summed rounding is $o(K)$. The dimension-one sieve on the remaining upper primes has the same parameter 15 and the same limiting product bounds. Omitting lower squares costs $o(K)$ at $d=1$. Include the two bounded-weight sector counts for the first set in the Hoeffding union bound; both rounding and the final trimming change them by $O(\sqrt{HL})$. These steps preserve the strict numerical bounds certified in the earlier calculation.

## Why monotone additions must avoid small upper factors

There is a converse that needs no sieve theorem. Suppose two lower sets of odd integers differ by deletions only opposite actual upper primes, with all other edits additions, and their summed class discrepancies relative to one another are $o(K)$ up to $D<p$. For an odd prime $\ell\le D$, the lower class $n\equiv2X\bmod\ell$ is reduced. Every upper partner in that class is a multiple of $\ell$ larger than $\ell$. Hence deletions contribute zero in the class. The number of additions with an upper partner divisible by *some* such $\ell$ is bounded above by
\[
 \sum_{2<\ell\le D,\ \ell\ {\rm prime}}
 \left|\#E_1(2X\bmod\ell)-\#E_0(2X\bmod\ell)\right|=o(K).
\]
The union bound permits repeated counting. Every small-cofactor upper site has a prime divisor at most $y$. Thus for $D\ge y$ a monotone replacement cannot put a positive proportion of $K$ additions in that sector. The semiprimes in (3) realize the other possibility while preserving all the reduced progression tests (2). For the genuine primes the signed difference $P-A$ is not a monotone edit of this kind; (1) applies to that difference. The construction does not test general two-variable estimates for the true primes.

The [finite checker](CheckPrimeReflectionDivisorTests.py) uses $X=1009^2$, the integer upper window $[X+3000,X+10000]$, and toy cutoffs $z=7,y=160$. It checks (1)'s sitewise polynomial on all 502 eligible upper sites via exact log coefficients, including the four two-prime cofactors. It also checks exact cardinality after thinning, opposite-prime deletion, untouched small-sector sites and the union bound with overlapping classes. The asymptotic discrepancy estimates in (2) are proved above.
