# Where the two prime summands of twice a prime square occur

Write $w(x)=\log x$ for positive primes $x$ and zero for all other integers. Fix an integer $P$ tending to infinity. For a prime $P\le p\le2P$ put $n=2p^2$. For an interval of integers $J\subseteq[1,n-1]$, define the ordered pair weight
$$
 R(n;J,b,d)=\sum_{\substack{x\in J\\x\equiv b\bmod d}}w(x)w(n-x).
$$
Let $\nu_d(n)$ count the classes $b\bmod d$ with $(b(n-b),d)=1$. These are called admissible. Put $\mathfrak S(2p^2)=2C_2(p-1)/(p-2)$ for odd primes $p$, where $C_2=\prod_{\ell>2,\ \ell\ {\rm prime}}(1-(\ell-1)^{-2})$.

**A simultaneous estimate for the true primes.** For any fixed $A,D,E>0$, outside $O_{A,D,E}(P/(\log P)^E)$ prime indices in $[P,2P]$, one has
$$
 R(n;J,b,d)=\frac{\mathfrak S(n)}{\nu_d(n)}\,|J|
             +O_{A,D,E}\!\left(\frac{n}{(\log n)^A}\right)
 \tag{1}
$$
for **every** integer interval $J\subseteq[1,n-1]$, **every** $1\le d\le(\log P)^D$, and **every** admissible $b\bmod d$. Here $|J|$ counts all integers in the interval. For inadmissible $b$, the same error bounds the entire weight. Taking $E>1$ yields relative density one among prime indices. The argument below is a paper deduction using classical exponential sum and progression estimates. It does not require a zero-free half-plane hypothesis.

In particular take $H=\lfloor p^2/(\log p)^K\rfloor$ for any fixed $K>0$ and $J=[p^2+1,p^2+H]$. For the good indices the number of prime pairs with the **larger** prime in $J$ and in a given admissible class is
$$
 (1+o(1))\frac{H\,\mathfrak S(2p^2)}{\nu_d(2p^2)\,\log^2(p^2)}
 \tag{2}
$$
uniformly over the indicated classes and moduli. Choose $A>K+D+1$ in (1), use $\nu_d(n)\le d$, and note that both endpoints have logarithm $(1+o(1))\log(p^2)$. Each counted pair has its other prime between $p^2-H$ and $p^2-1$. Formula (2) gives actual reflected pairs in all these classes at the same index.

Perelli's Corollary 1 concerns the full von Mangoldt coefficient at polynomial targets. Coppola and Laporta's Theorem 1 localizes the two summands to a power-length window for almost all **even integers**. An exceptional set counted among all even integers can contain all the prime-square targets in a dyadic block. We use a sum over the quadratic frequencies themselves and retain the interval and congruence in one prime factor. [Perelli (1996), pp. 477–479](https://doi.org/10.4171/RMI/205) · [Coppola–Laporta (1995), Theorem 1](https://www.giovannicoppola.name/files/articoli/8_giovanni_coppola_number_theory_seminar_politecnico_torino_245.pdf)

## A common minor-arc estimate for the prime-square targets

Set $Y=8P^2$, $L=\log Y$, $T=L^B$ for a fixed sufficiently large $B$. Use one set of major arcs on the circle, centered at reduced $a/q$ with $q\le T$ and radii $T/(qY)$. The arcs are disjoint for large $Y$. Write $e(t)=\exp(2\pi it)$ and
$$
 S(\alpha)=\sum_{x\le Y} w(x)e(x\alpha),\qquad
 S_{u,b,d}(\alpha)=\sum_{\substack{1\le x\le u\\x\equiv b\bmod d}}w(x)e(x\alpha)
 \quad(0\le u\le Y).
$$
Here and in $S$ the integer summation begins at 1. The full Fourier coefficient of $S S_{u,b,d}$ at $n$ equals the prefix version of $R$ by orthogonality. Dirichlet approximation of order $\lfloor Y/T\rfloor$ gives every minor point a reduced approximant $a/r$ with $T<r\le Y/T$ and error at most $r^{-2}$ (the nearer bound is $1/(r(\lfloor Y/T\rfloor+1))$). By the Vinogradov–Vaughan estimate, $\sup_{\rm minor}|S|\ll Y L^{5/2-B/2}$ for all sufficiently large $Y$ depending on $B$. The $Y^{4/5}$ term, and the cost $O(\sqrt{Y}L^2)$ of proper prime powers, fit this bound. [Montgomery–Vaughan, Theorem 17.1, equation (17.29)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77)

For any $|z_p|\le1$ put $K(\alpha)=\sum_{P\le p\le2P}z_p e(-2p^2\alpha)$, summing over primes. Orthogonality bounds $\|K\|_4^4$ by the number of equal differences of twice-squares. At difference zero the contribution is $O(P^2)$. For a nonzero difference $2t$, $(x-y)(x+y)=t$ gives at most $2\tau(|t|)$ representations. Consequently $\|K\|_4^4\ll P^2 L^3$. Indeed $\sum_{t\le V}\tau(t)^2\le V\sum_{a,b\le V}1/[a,b]\ll V\log^3(2V)$ by writing $a=g a',\ b=g b'$ with $g=(a,b)$.

For one fixed $(u,b,d)$ denote the minor coefficient by $E_p$. Choose $z_p$ to make $z_p E_p=|E_p|$. Parseval gives $\|S_{u,b,d}\|_2,\|S\|_2\le\sqrt Y L$. On the minor arcs, $\|\mathbf1_{\rm minor} S\|_4\le(\sup_{\rm minor}|S|)^{1/2}\|S\|_2^{1/2}$. Hölder with exponents $4,2,4$ therefore gives
$$
 \sum_{P\le p\le2P}|E_p|
 \le \|\mathbf1_{\rm minor}S\|_4\,\|S_{u,b,d}\|_2\,\|K\|_4
 \ll PY L^{4-B/4}.
 \tag{3}
$$
The scale follows from $Y^{3/4}Y^{1/2}P^{1/2}\asymp PY$. No bound for an individual minor coefficient or a prime exponential sum in a short interval is assumed.

## The main term with one summand in a residue class

Let $V_u(\beta)=\sum_{1\le j\le u}e(j\beta)$. At $a/q+\beta$ on a major arc, the two prime sums have models $\mu(q)V_Y(\beta)/\varphi(q)$ and $A_{b,d}(a,q)V_u(\beta)$, where
$$
 A_{b,d}(a,q)=\frac1{\varphi([d,q])}
   \sum_{\substack{v\bmod[d,q]\\(v,[d,q])=1\\v\equiv b\bmod d}} e(av/q).
$$
Siegel–Walfisz in classes modulo $[d,q]\le L^{B+D}$ and partial summation give pointwise errors $O_{B,D,F}(Y/L^F)$ for every fixed $F$. For prefix lengths below $\sqrt{Y}$ a trivial bound suffices. For larger lengths the logarithms are comparable, the sum over residue classes costs at most $L^{B+D}$, primes dividing the modulus cost $O(\log [d,q])$, and partial summation costs $O(1+Y|\beta|)$. The total arc measure is $O(T^2/Y)$. Thus after multiplying and integrating, the error remains $O(Y/L^F)$ for any prescribed fixed $F$ upon increasing the initial exponent. [Montgomery–Vaughan, §18.2, in particular the major-arc expansion (18.22)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)

For admissible $b$, the coefficient after summing over the numerators equals
$$
 c_{q;b,d}(n)=\frac{\mu(q)}{\varphi(q)\varphi([d,q])}
 \sum_{\substack{v\bmod[d,q]\\(v,[d,q])=1\\v\equiv b\bmod d}}c_q(v-n),
 \tag{4}
$$
where $c_q$ denotes a Ramanujan sum. Non-squarefree $q$ contribute zero. For squarefree $q=t s$, with $t=(q,d)$ and $(s,d)=1$, the Chinese remainder theorem gives
$$
 c_{q;b,d}(n)=\frac{a_s(n)}{\varphi(d)\varphi(t)},\qquad
 a_s(n)=\frac{\mu(s)^2 c_s(n)}{\varphi(s)^2}.
 \tag{5}
$$
To check (5), the unit classes in the sum above account for a fraction $1/\varphi(d)$ of all units modulo $[d,q]$. At $\ell\mid t$ the residue is fixed and $c_\ell(b-n)=-1$, giving $1/(\ell-1)$ after multiplying by $\mu(\ell)/\varphi(\ell)$. At $\ell\mid s$ the residue is uniform on the units. The average of $c_\ell(v-n)$ is $-1$ when $\ell\mid n$ and $1/(\ell-1)$ otherwise, giving $a_\ell(n)$ in both cases.

The sum of (5) over all $q$ converges absolutely. It equals $\mathfrak S(n)/\nu_d(n)$ by multiplying local factors. In detail, the admissible count at $\ell^j\parallel d$ is $\ell^{j-1}(\ell-1)$ if $\ell\mid n$ and $\ell^{j-1}(\ell-2)$ otherwise. Dividing the restricted Euler factor by $1+a_\ell(n)$, and including $1/\varphi(\ell^j)$, gives exactly the reciprocal of this count. For an inadmissible class any representation counted has a prime endpoint dividing $d$, so its total weight is $O((1+\log d)L^2)$.

The full-circle coefficient of $V_uV_Y$ at $1\le n\le Y$ is $M_u(n)=\min(u,n-1)$ for integer $u$. The difference between this coefficient and the integral on $|\beta|\le T/(qY)$ is $O(Y q/T)$ for $q\le T$, by $|V_j(\beta)|\le1/(2|\beta|)$ on $0<|\beta|\le1/2$. For $q>T$ the discarded coefficient is at most $Y$. The total truncation error is accordingly bounded by
$$
 Y\sum_q |c_{q;b,d}(n)|\min(1,q/T)\ll Y\,\log(2T)/T.
 \tag{6}
$$
For completeness, in the factor $s$ of (5) write $s=gk$, $g=(s,n)$, so $g\mid\operatorname{rad}(2p^2)$, $(k,n)=1$, and $|a_s|=1/(\varphi(g)\varphi(k)^2)$. For any $v\ge1$,
$$
 \sum_{k\ge1}\frac{\min(1,vk/T)}{\varphi(k)^2}
 \ll (v/T)\log(2T).
$$
For $v\le T$ split at $k=T/v$ and partially sum $\sum_{k\le y}(k/\varphi(k))^2\ll y$. This last bound follows by expanding the positive divisor product and bounding its mean by $\prod_\ell(1+((\ell/(\ell-1))^2-1)/\ell)<\infty$. For $v>T$ the full series is bounded. Use $v=tg$ and sum. The factor $\sum_{g\mid\operatorname{rad}(n)}g/\varphi(g)\le15/2$. The remaining factor is $\varphi(d)^{-1}\sum_{t\mid\operatorname{rad}(d)}t/\varphi(t)\le15/4$: at prime powers its factors are $(1+\ell/(\ell-1))/\varphi(\ell^j)$, at most $3$ at 2, $5/4$ at 3, and at most one thereafter. This proves (6), including shared primes of $d$ and $n$.

## Recovering all intervals at once

First take prefix endpoints at a grid of mesh $\lceil Y/L^{A+2}\rceil$, including 0 and $Y$. There are $O(L^{A+2+2D})$ tests after including all moduli and their classes. By (3) the number of primes with $|E_p|>Y/L^A$ for any test is $O(P L^{2A+2+2D+4-B/4})$. Take $B$ fixed and sufficiently large for this to be $O(P/L^E)$ and for (6) to be $O(Y/L^A)$. The prefix main term is $M_u(n)\mathfrak S(n)/\nu_d(n)$, with uniformly bounded slope because $n=2p^2$. The actual prefix is nondecreasing. Bracketing between neighboring grid endpoints therefore costs at most the slope times the mesh plus the additive error at those endpoints. Subtract two prefixes to prove (1), using $Y/4\le n\le Y$.

## How many blocks of length $p^{4/3}$ contain many pairs?

There is a consequence at the shorter length using a uniform upper sieve. Fix $K>0$, let $H$ be as in (2), put $U=\lfloor p^{4/3}\rfloor$, and partition the first $H'=U\lfloor H/U\rfloor$ positive offsets into successive blocks of length $U$. A hit at offset $j$ means that both $p^2-j$ and $p^2+j$ are prime. For the good prime indices in (1), **at least a fraction $1/35-o(1)$ of the complete blocks** have at least $(C_2/4)U/\log^2 p$ hits each. The reflected blocks refer to the same target $2p^2$. Their distances from the center can be as large as $H$.

Indeed, (1) for $d=1$, with $A>K+1$, gives $(C_2/2+o(1))H'/\log^2 p$ hits in total. Both prime logarithms are $(1+o(1))\,2\log p$ uniformly, and $H'\sim H$. For any one block the count is at most $(9C_2+o(1))U/\log^2 p$, uniformly in its location. To see this, sieve $(p^2-j)(p^2+j)$ up to $z=\sqrt U/(\log U)^5$. Every pair of primes counted survives since both primes exceed $z$. For large $p$, $z<p$; there is one forbidden class at 2 and two at every odd sieve prime. For squarefree $s$ the interval remainder is $O(2^{\omega(s)})$ by CRT, uniformly in the translate. Formula (3.8) of Heath-Brown's lectures gives a remainder $O(z^2\log^5 z)=o(U/\log^2 p)$ since $\mu^2(s)6^{\omega(s)}\le\tau_6(s)$, where $\tau_6$ counts ordered factorizations into six factors. The dimension-two multiplier is $(2+o(1))e^{2\gamma}$ and the local product is $(2C_2+o(1))e^{-2\gamma}/\log^2 z$. As $\log z\sim(2/3)\log p$, the asserted upper constant is $9C_2$. If a fraction $f$ of the blocks reaches the threshold, the mean number of hits in units of $C_2 U/\log^2 p$ is at most $(1-f)/4+(9+o(1))f$. Its limit $1/2$ yields the fraction stated above. This lower bound on the fraction leaves the first block, $1\le j\le U$, individually undecided. [Heath-Brown, *Lectures on sieves*, §3, (3.8) and the Goldbach example](https://arxiv.org/pdf/math/0209360#page=22)

## Consequence for the desk's original radii on a central window

Take fixed $K>2$, the half-width $H$ used in (2), $W=[p^2-H,p^2+H]$, $M=2H+1$ and $Q=\lfloor\log_2(n+2)\rfloor^2$. Use the prime sum restricted to $W$, square it, and integrate against $e(-n\alpha)$. Since $W=n-W$, (1) with $d=1$ gives full weight $(2C_2+o(1))M$ outside the exceptional set. On the desk's arcs of radius $Q/(qn)$ the windowed major coefficient is $o(M)$ at **every** sufficiently large prime $p$. Indeed the preceding Siegel–Walfisz approximation applied to the two endpoints of $W$ gives the model $\mu(q)V_W(\beta)/\varphi(q)$, with integrated error $O_F(n/\log^F n)=o(M)$ for large fixed $F$. After summing numerators, $|V_W|\le M$ bounds the absolute value of the modeled signed coefficient by
$$
 (2M^2 Q/n)\sum_{q\le Q}|a_q(n)|/q\ll M^2 Q/n=o(M).
$$
Here the absolute sum is bounded at $n=2p^2$ by the four possible $g$ and the convergent $k$-sum above. Thus the **windowed** minor coefficient on the desk's original radii is $(2C_2+o(1))M>0$ for almost all prime indices. The larger polylogarithmic arcs used in the proof of (1) are auxiliary. Full-support pointwise tasks and the narrower half-width $\lfloor p^{4/3}\rfloor$ require additional estimates. At that half-width the additive error in (1) exceeds the predicted signal for every fixed $A$. [Earlier window-scale calculation and discussion](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/449#issuecomment-7152589370)

## Exact finite checks

For $p=3,5,7,11,17,101$, $1\le d\le18$, $1\le q\le40$ and every admissible $b$, enumerate the units modulo $[d,q]$ in (4). Evaluate $c_q(v-n)=\sum_{k\mid(q,v-n)}k\mu(q/k)$ and compare rational values with (5), taking zero at non-squarefree $q$. All 20,000 comparisons agreed. For the 15 primes in $[80,160]$ the fourth moment with unit phases, computed independently by equal sums and by equal differences of twice-squares, was 463. For $p=101$, $H=809$, $d=15$, direct enumeration of $p^2<x\le p^2+H$ gives 4, 3 and 7 pairs with larger summand in residues 1, 4 and 13 respectively. These are the three admissible classes. This last finite count illustrates the endpoint convention; the theorem is asymptotic.

For $p=1009$, take the integer outer half-width $145000$ and the exact inner length $U=\lfloor p^{4/3}\rfloor=10120$ (check $U^3\le p^4<(U+1)^3$). In the 14 complete positive-offset blocks the hit counts in order were $64,67,83,63,70,74,80,70,74,76,82,60,64,62$. Their sum 989 agrees with direct sieving of the whole union. This tests the reflection and block endpoints.
