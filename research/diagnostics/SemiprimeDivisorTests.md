# A set of semiprimes matching the small-divisor statistics of primes at each square

Fix a sufficiently large odd prime $p$. Write $X=p^2$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $J=[X-H,X-2T)\cap\mathbb Z$ and $h_0=H-2T$. Each lower site $n\in J$ has upper partner $a=2X-n$. Write $P(n)=1_{\mathbb P}(n)$. Let $B(n)$ equal one if $n=qt$ for **distinct primes** $q<t$ with $\log_X q$ in
\[
 [\alpha,\beta]\ \cup\ [1/3,1/2],\qquad
 \beta=7/36,\quad \alpha=14/(29e+14)=0.150813\ldots ,
\]
and zero otherwise. This is a set of actual integers disjoint from the primes. Its indicator takes only the values zero and one. Both prime factors exceed $X^{3/20}$, so all members satisfy the previous lower-site factor restrictions and have [Richert weight](SwitchedWeightedCofactors.md) exactly one.

**Fixed-center estimate.** For any fixed $0<\delta<7/240$, $D=X^\delta$ and every $A>0$, the following deduction from published distribution theorems gives
\[
 \sum_{d\le D}\max_{(r,d)=1}
 \left|\sum_{\substack{n\in J\\n\equiv r\bmod d}}(B(n)-P(n))\right|
 \ll_{A,\delta} H L^{-A}. \tag{1}
\]
The constants are independent of $p$. In particular this holds for the tests $d\mid a$ at the prescribed target. For odd $d$ the residue $2X\bmod d$ is a unit. For even $d$ both counts for $d\mid a$ are zero. Any linear combination of these tests with coefficients bounded by a fixed power of $L$ also has error $O_{A,\delta}(HL^{-A})$, by increasing $A$. No average over centers or hypothesis on zeros enters (1). In fact the progression comparison itself works for general large $X$ with the same interval convention.

## Transferring the interval average to one center

For $y>0$, let $E(y,z;d)$ be the maximum over reduced residues of the absolute difference between the sum of $\log t$ over primes $y<t\le y+z$ in that residue and $z/\varphi(d)$. Koukoulopoulos's Theorem 1.2 bounds $\int_{Y_0}^{2Y_0}\sum_{d\le D}E(y,z;d)\,dy$ by $O_A(Y_0 z/\log^A Y_0)$ in particular when $Y_0^{1/6+2\epsilon}\le z\le Y_0^{1/2}$ and $D^2\le z/Y_0^{1/6+\epsilon}$, with fixed $\epsilon>0$. We use the theorem for its stated prime weight. [Koukoulopoulos, *Primes in short arithmetic progressions*, Int. J. Number Theory 11 (2015), Theorem 1.2 and definition of $E$](https://dms.umontreal.ca/~koukoulo/documents/publications/shortaps.pdf#page=3)

Partition $[X^{1/3},\sqrt X]$ into dyads starting at $X^{1/3}$, truncating the last. In one such dyad $M\le m<2M$ put $Y=X/M$ and $z=(H/M)X^{-\eta}$, with $\eta>0$ small and fixed. To keep integer endpoints exact let $I_m=((X-H-1)/m,(X-2T-1)/m]$. For every real $y$ in the union of the $I_m$, the condition $y\in I_m$ puts $m$ in an interval of length $h_0/y$. Hence the overlap is at most $1+h_0/y\ll H/Y$, using $y\asymp Y$ and $Y\le X^{2/3}$. This bound includes every integer $m$ and permits any subset.

For any $0<\delta'<1/24$ we can use $D'=X^{\delta'}$ throughout these dyads. In fact if $M=X^v$, $1/3\le v\le1/2$, then
\[
 \log_X\!\left((H/M)/Y^{1/6}\right)=1/2-5v/6+o(1)\ge1/12+o(1).
\]
Before extracting $X^{-\eta}$, $\log_Y(H/M)$ ranges from $1/3+o(1)$ to $1/2+o(1)$. Choosing $\eta,\epsilon$ sufficiently small gives the asserted hypotheses with power margins on the finitely many intervals $[Y_0,2Y_0]$ covering $[Y/3,2Y]$. In particular the upper endpoint $1/2$ presents no problem after shortening the interval.

For a reduced class $b\bmod d$, integrate its short-interval weighted prime sum over $y\in I_m$ and divide by $z$. Relative to the weighted prime sum on $I_m$ itself, only two intervals of length $z$ at the boundaries can contribute an error. Each has at most $1+z/d$ integers in the class, of weight $O(L)$. The main term integrates to $|I_m|/\varphi(d)$. Taking absolute values **before** summation over $m$, the overlap bound and the published integral estimate give
\[
 \sum_{M\le m<2M}^{*}\sum_{d\le D'}
 \max_{(b,d)=1}\left|
 \sum_{\substack{t\in I_m\cap\mathbb P\\t\equiv b\bmod d}}\log t
 -\frac{h_0}{m\varphi(d)}\right|
 \ll_A H L^{-A}+ ML(z\log(2D')+D').
\]
Here the star restricts $m$ to the stated range. The boundary term has a power saving since $Mz=HX^{-\eta}$ and $MD'\le X^{1/2+\delta'}$. There are $O(L)$ dyads. For $t\in I_m$, $\log t=\log(X/m)+O(H/X)$. Dividing by $\log(X/m)$ gives the ordinary count with main term $h_0/[m\varphi(d)\log(X/m)]$. In this replacement even the all-integer count summed over $m,d$ is $O(HL^2+\sqrt X D')$, using $1+h_0/(md)$ for each class. Thus the unweighting preserves arbitrary log savings.

Apply this to prime $m=q$ in the large band. As $q>D'$, a reduced class $n\equiv r\bmod d$ prescribes the single reduced class $t\equiv r q^{-1}\bmod d$. The unrestricted switched sum permits $t\le q$ only when both factors lie within $O(1+H/\sqrt X)$ of $\sqrt X$. Removing all such ordered pairs, including squares, costs $O(D'(1+H/\sqrt X)^2)$ even after summing the moduli, which has a power saving. The remaining pairs are unique.

## Completing the density with a second band

For $q=X^v$, $\alpha\le v\le\beta$, use Timofeev's fixed-location estimate on $I_q$. At scale $y=X/q$ and length $\ell=h_0/q$, its sufficient conditions are $\ell\ge y^{7/12+\epsilon}$ and $D\le \ell/y^{11/20+\epsilon}$. The two exponent differences before the $\epsilon$ loss are decreasing in $v$:
\[
 (2/3-v)-(7/12)(1-v)\ge1/432,\qquad
 (2/3-v)-(11/20)(1-v)\ge7/240 .
\]
The trim changes $\log_X\ell$ by $o(1)$. These strict margins give the claimed level for every $q$ in the band. The fixed-location error is $O_A(\ell/L^A)$ summed over moduli for each $q$. Summing over $q$ costs at most a logarithm since $\ell=h_0/q$. Timofeev states the result for $\Lambda$. Removing proper prime powers per $q$, even with every modulus charged for every power, costs $O(D\sqrt{X/q}\,L^2)$, which is $O(\ell X^{-c})$ for a fixed $c>0$ since $\delta+\beta/2<1/6$. Unweight as above. Here $t>q$ throughout and $q>D$. The same fixed-location result at $q=1$ gives the true prime progression count with main term $h_0/(\varphi(d)L)$ and summed error $O_A(HL^{-A})$. [Timofeev, *Distribution in the mean of arithmetic functions in short intervals in progressions*, Math. USSR-Izv. 30 (1988), §1, estimate (1)](https://doi.org/10.1070/IM1988v030n02ABEH001013)

For either fixed band $[u,v]$ the mass multiplier relative to the prime main term is
\[
 \sum_{X^u\le q\le X^v,\ q\ {\rm prime}}\frac{L}{q\log(X/q)}
 =\int_u^v\frac{ds}{s(1-s)}+O_A(L^{-A}).
\]
This follows by partial summation from the classical prime number theorem with error $O_A(x/\log^A x)$, uniformly on these fixed positive exponent ranges. For $[1/3,1/2]$ the integral is $\log 2$. For $[\alpha,\beta]$ the ratio of upper and lower odds $[v/(1-v)]/[u/(1-u)]$ is $e/2$, giving $1-\log 2$. The sets are disjoint by unique factorization. The two main terms therefore sum to exactly the prime main term up to arbitrary log savings, including after summing $1/\varphi(d)\ll 1$ on average in the form $\sum_{d\le D}1/\varphi(d)\ll\log(2D)$. This proves (1).

## What survives sieving and what still depends on primality

Set $w=\exp(\sqrt L)$. Count lower sites with $a$ having no prime divisor at most $w$. For either $P$ or $B$ the count is
\[
 \frac{h_0}{L}\prod_{2<\ell\le w,\ \ell\ {\rm prime}}
      \left(1-\frac1{\ell-1}\right)+O_{A,\delta}(H L^{-A}). \tag{2}
\]
For just the large band the main term is multiplied by $\log 2$. To see this, apply the even and odd Bonferroni truncations separately to the nonnegative counts. Use two consecutive cutoffs near $\tfrac12\delta\sqrt L$, so all squarefree products involved are $\le D$. Each product is used at most once in either truncation. The tails in the main term are bounded by $\sum_{j\ge k} s^j/j!$ with $s=\sum_{2<\ell\le w}1/(\ell-1)=O(\log L)$ and $k\asymp\sqrt L$. They beat every fixed power of $1/L$. The product is asymptotic to $2e^{-\gamma}C_2/\log w$, where $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes, by Mertens' theorem. Thus even this nonlinear small-prime screen gives asymptotically equal, positive counts in the two disjoint sets at **each** square center.

For a test of *true* upper primality the missing term can be written exactly up to arbitrary log savings. Put $F=B-P$, $D=X^{1/36}$, $U=X^{1/72}$, and let $R_B,R_P$ count the corresponding lower sites with $a$ prime. Then
\[
 L(R_B-R_P)=
 \sum_{n\in J}F(n)
 \sum_{\substack{jk=2X-n\\j>U,\ k>U}}
       \Lambda(k)\sum_{\substack{e\mid j\\e>U}}\mu(e)
 +O_A(HL^{-A}). \tag{3}
\]
Indeed Vaughan's identity on $a$ gives the two short terms $\mu_{\le U}*\log$ and $-\mu_{\le U}*\Lambda_{\le U}*\mathbf 1$. In the first term replace $\log(a/d)$ by $L-\log d$. The cost is $O((H/X)(H\log(2U)+U))$ by elementary divisor counting. The grouped coefficients in the second term are at most $\log d$ in absolute value and $d\le U^2=D$. Estimate (1) absorbs both terms. The term $\Lambda_{\le U}(a)$ vanishes. The remaining convolution is exactly the displayed one. Replacing $\Lambda(a)$ with $LP(a)$ costs $O(\sqrt X L^2+H^2/X)$ as $|F|\le1$. This establishes (3) without a sign estimate.

The previous $0.34$ lower bound counts genuine upper primes paired with a larger set of possible lower partners. Equations (1) and (2) do not identify the share of $B$ in that count. Equation (3) leaves a concrete target: a lower bound for $L R_B$ together with an upper bound for the displayed signed sum that leaves a positive margin larger than the error. Neither input at that precision is established here. The restriction in (1) concerns bounded linear divisor tests up to the given level; it places no impossibility claim on general sieve arguments or stronger bilinear information.

[Exact finite checks of the exponent margins, factorizations, smoothing boundaries and convolution](CheckSemiprimeDivisorTests.py)
