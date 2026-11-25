# A Selberg bound after fixing the smallest prime factors

Fix an odd prime $p$, $X=p^2,\ L=\log X,\ H=\lfloor X^{2/3}\rfloor,\ T=\lfloor X^{21/40}\rfloor$. Write $I=(X+2T,X+H]$, $n=2X-a$ for $a\in I$, and $K=2C_2H/L^2$, where $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$. All limits are along prime $p\to\infty$. The estimates below hold at each sufficiently large center. All constants in the ranges are fixed before taking that limit.

## A uniform two-form bound

Write $a=mt$, $v=\log m/L$. Suppose $v\le b<2/3$, $m$ is odd with a bounded number of prime factors, and all its prime factors exceed $X^{s_0}$ for fixed $s_0>0$. Count sites where $n,t$ both have no prime factor at most $Z$, where
$$
 Z=\min\{X^\eta,\sqrt{H/m}/L^{10}\},\qquad \eta>0.
$$
For $p\nmid m$, this count is at most
$$
 \left(\frac{2}{\min(\eta,(2/3-v)/2)^2}+o(1)\right)\frac K m. \tag{1}
$$
The error is uniform for the indicated $m$. For true prime $n,t$ one can omit the $X^\eta$ cap: both exceed $\sqrt{H/m}$. Multiples of $p$ in $I$ contribute $O(H/p+1)=o(K)$ to any count of sites, and none have a true lower prime for large $p$.

Indeed, $t$ ranges over an interval of length $Y=(H-2T)/m$. On a squarefree modulus $d$, the number of roots of $t(2X-mt)$ is multiplicative, with $\nu(2)=1$, $\nu(\ell)=1$ for odd $\ell\mid mp$, and $\nu(\ell)=2$ at other odd primes. The interval count is $Y\nu(d)/d+O(\nu(d))$. Set $h(\ell)=\nu(\ell)/(\ell-\nu(\ell))$ and $G(Z)=\sum_{d\le Z}\mu^2(d)\prod_{\ell\mid d}h(\ell)$. The Selberg upper square has main term $Y/G(Z)$. Its coefficients have absolute value at most one, so rounding costs
$$
 O\left(\sum_{d,e\le Z}2^{\omega([d,e])}\right)
 =O\big(Z^2\log^2(2Z)\big)=o(K/m).
$$
Here each summand is at most $\tau(d)\tau(e)$. The square majorizes both prime forms as soon as both avoid the primes through $Z$. [Selberg upper-square theorem and two-root interval error, Theorem 1.1 and §1.2](https://www.math.tau.ac.il/~rudnick/courses/sieves2015/selberg%20sieve%20twin%20primes.pdf)

For clarity, take first the basic roots $1$ at 2, $2$ elsewhere. The Dirichlet series for this $G$'s summand is $\zeta(1+w)^2 B(w)$. The Euler factors of $B$ are $(1+h(\ell)\ell^{-w})(1-\ell^{-1-w})^2$. Writing $B(w)=\sum b(d)d^{-w}$, we have $\sum |b(d)|d^{1/4}<\infty$: the coefficients of the first two powers of $\ell^{-w}$ are $O(\ell^{-2})$ and the cubic coefficient is $O(\ell^{-3})$. At zero $B(0)=1/(2C_2)$. Convolution with $\sum_{r\le y}\tau(r)/r=\tfrac12\log^2 y+O(\log(2y))$ yields $G_{\rm basic}(Z)=\log^2 Z/(4C_2)+O(\log(2Z))$. Reducing the roots at primes dividing $mp$ changes $G$ by at most $G_{\rm basic}(Z)\sum_{\ell\mid mp,\,\ell>2}2/(\ell-2)=o(G_{\rm basic}(Z))$ uniformly. Using $\log Z/L=\min(\eta,(2/3-v)/2)+o(1)$ gives (1).

## Keeping several prime factors in the sieved variable

Let $a=q_1\cdots q_j$ have exactly $j\ge2$ prime factors in increasing order, with repetitions allowed, and $q_1>X^s$, $0<s<1/j$. Fix $1\le k<j$ with $k/j<2/3$. Freeze $m=q_1\cdots q_k$ and leave **all** $j-k$ remaining primes in $t$. Their size guarantees $P^-(t)>X^s$. Let $N$ count these upper sites with $P^-(n)>X^\kappa$, or with $n$ prime (write $\kappa=+\infty$ in that case). Then
$$
 \limsup\frac{N}{K}\le
 \frac{2}{\min(s,\kappa,(2/3-k/j)/2)^2}
 \frac{(1-js)^k}{k!\,j(j-1)\cdots(j-k+1)\,s^k}. \tag{2}
$$
Indeed, ordering gives $m\le (X+H)^{k/j}$. Put $u_i=\log q_i/L$. Since each unfrozen factor is at least $q_k$,
$$
 s\le u_1\le\cdots\le u_k,\qquad
 u_1+\cdots+u_{k-1}+(j-k+1)u_k\le 1+o(1).
$$
The sum of $1/m$ over prefixes is bounded in the limit by the integral of $\prod du_i/u_i$ on this polytope with right endpoint 1. This follows by rectangle approximation from the prime harmonic sum $\sum_{X^c<q\le X^d}1/q\to\log(d/c)$ for fixed $0<c<d$; the boundary has zero volume. Repeated primes in the prefix contribute $o(1)$ by $\sum_{q>X^s}q^{-2}=o(1)$ and bounded remaining prime harmonic sums. Repetitions in $t$ are already covered by (1). In coordinates $u_1-s,u_2-u_1,\ldots,u_k-u_{k-1}$ the simplex has coefficients $j,j-1,\ldots,j-k+1$ and intercept $1-js$. Its volume times $s^{-k}$ bounds the integral. Apply (1) with $\eta=\min(s,\kappa)$. Counting all eligible $t$ for each prefix only enlarges the result.

For fixed $B>1$, if all $j$ factors lie between $X^{1/j}/B$ and $BX^{1/j}$, the stronger bound $O_{j,B,\kappa}(K/L^k)$ follows directly: each frozen prime contributes $O_{j,B}(1/L)$ to its harmonic sum, by the elementary prime counting upper bound. The other restrictions and the strictly positive sieve exponent are uniform in this range. One can choose $k=\lceil2j/3\rceil-1$. In particular balanced five-factor products with fixed factor ratios cost $O(K/L^3)$ even for lower sites sifted only through $X^{1/18}$.

## Applying the bound to the signed excess and the replacement model

Use the signed inequality (2) of the [preceding strip estimate](SwitchedSemiprimeStrip.md). There $R$ counts true central prime pairs, $P(n)$ is the prime indicator and $A(n)=1_{P^-(n)>\sqrt L}/(L\prod_{\ell\le\sqrt L}(1-1/\ell))$. The upper-composite weight $W(a)$ vanishes off squarefree $X^{1/30}$-rough composites and sums $\log\ell/L$ over prime factors $\ell>X^{1/10}$ on its support. The previous result supplies $R+C_{\rm out}(P)-C_{\rm out}(A)>0.1395K$ after removing semiprimes whose smaller factor is in $(X^{4/25},X^{1/6}]$.

Remove the following further upper sectors simultaneously. Each entry in the last column is rounded **up** from an upper bound for the limiting true lower prime count divided by $K$. Decimal exponents are exact.

| Number of upper prime factors | Further restriction on the ordered prime factors | Upper bound |
|---|---|---:|
| 2 | $X^{1/6}<q_1\le X^{0.1668}$ | 0.025614 |
| 3 | $q_1>X^{1/6},\ q_1q_2\le X^{0.336}$ | 0.004683 |
| 3 | $q_1>X^{0.3333}$ | 0.007201 |
| 4 | $q_1>X^{0.249}$ | 0.003097 |
| 5 | $q_1>X^{0.19}$ | 0.091122 |

For rows 1 and 2, write $a=mt$ with $r=1,2$ frozen factors and true primes $n,t$. For $u_i>h=1/6$, $v=\sum u_i\le b$, the ordered prefix volume is $(b-rh)^r/(r!)^2$ (one factorial for the simplex, one for ordering). By (1) the cap is $8((b-rh)/h)^r/((2/3-b)^2(r!)^2)$. Rows 3–5 use (2) with $(j,k)=(3,1),(4,2),(5,3)$. Since $A\ge0$ and $0\le W(a)\le\log(a)/L=1+o(1)$, their total positive signed contribution is at most their total true-prime cap plus $o(K)$. Thus, with all these sectors and the previous strip omitted,
$$
 R+C_{\rm remaining}(P)-C_{\rm remaining}(A)>0.00778K \tag{3}
$$
eventually. This still permits $R=0$ and a positive signed excess on the remaining upper composites.

For the [monotone replacement model](SwitchedSemiprimeStrip.md#where-a-rough-monotone-replacement-would-have-to-go), retain **all** the preceding hypotheses: deletions only opposite upper primes, disjoint insertions only opposite composites, $(1+o(1))K$ replacements, the required summed reduced-class discrepancy $o(K)$ through $X^{83/500}$, and all inserted lower sites $X^{1/18}$-rough. The preceding estimate forces more than $0.3457K$ insertions opposite upper composites having at most five factors and least factor $>X^{67/400}$. At $j=5,\ k=3,\ s=19/100$, the minimum sieve exponent in (2) is $1/30$, also for $\kappa=1/18$. Hence the five-factor class with $q_1>X^{19/100}$ accounts for at most $(625/6859+o(1))K$. More than $0.2545K$ insertions must therefore have either two to four such upper factors, or five with $X^{67/400}<q_1\le X^{19/100}$. This conclusion about inserted sites does not assume their lower endpoints are primes.

The five-factor estimate keeps two unknown primes in the sieved variable. Freezing four factors above $X^{67/400}$ would give $m>X^{67/100}>H$. There is also a numerical obstruction to sharpening (2) just by evaluating its three-variable integral exactly. Set $s=67/400$ and project the entire five-factor region to its first three ordered exponents as above. If every admissible prefix is charged the Selberg coefficient (1), the coefficient for $X^{1/18}$-rough lower sites is at least $648$. Throughout the projected simplex, $v\le3/5$, so $u_1u_2u_3\le(1/5)^3$ by AM–GM. Thus the **cost of this majorant**, in units of $K$, is at least
$$
648\cdot125\frac{(1-5s)^3}{360}=0.965478515625.
$$
Even with a true lower prime, the sieve exponent is at most $(2/3-3s)/2$, which gives a cost greater than $0.4422$ by the same argument. These are lower bounds on the integral of the chosen upper estimator; the actual number of sites could be far smaller. Resolving the full five-factor sector in this way would require using how often the unfrozen cofactor is a product of two primes, beyond knowing its least prime factor.

[Exact constants, finite Selberg squares and factorization checks](CheckOrderedPrimeFactors.py)
