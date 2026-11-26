# Exact-two weight at every center in the reflected semiprime sample

Fix $N=2s$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $h=H-2T$ and $z=\exp(L/(\log L)^3)$. The records have $b=rt\in[s-H,s-2T)$ with $r,t$ prime, $s^\alpha<r\le s^\beta$, $(b,N)=1$, and $a=N-b$ squarefree with no prime factor $\le z$. Here $(\alpha,\beta)=(17/50,7/20)$. The band consists of primes $s^u<p\le s^v$, $p\nmid N$, with $(u,v)=(1/16,3/40)$. Let $Q$ count those dividing $a$. Mark an actual unordered pair $p,q\mid a$ with mass $\log r\,\log(pq)$. Let $W_j$ be the marked mass on $Q=j$, $A_2=\sum_j W_j$, and use the normalized measure $\mathbb P_s$ with expectation $\mathbb E_s$. Write $Z=Q-2$ and $M_s=\mathbb E_s Z$.

For **every sufficiently large integer $s$**, the estimates derived below give
$$
 M_s<0.985,\qquad \frac{W_2}{A_2}>0.025,\qquad W_2>W_3/39.              \tag{1}
$$
The lower bound for exactly two uses the sizes of the marked primes. The estimates allow $W_3=0$. No target averaging or GRH enters. The previous estimate gave $M_s<1.475$. To control the signed Goldbach block to the desired accuracy one still needs $M_s\le\log(6/5)+o((\log L)^{-3})$. [Previous normalization and pointwise bounds](FourthDivisorSieve.md) · [Signed-block formula (4)](ThreePrimeDivisorMoment.md)

## A distribution estimate with an unrestricted integer factor

Write $e(x)=\exp(2\pi i x)$. Let $w(b)=f((b-s)/h)$, where $f$ is smooth, supported in a fixed compact interval, and $\|f^{(j)}\|_\infty\ll_j(\log s)^{C_j}$ for every fixed $j$. On dyadic ranges $v_0\asymp V,\ d\asymp D$, use any two separate coefficients $\beta_{v_0},a_d$ of magnitude $s^{o(1)}$. Assume $D,V\ge1$, $(d,N)=1$ on the support, and, for fixed $\epsilon>0$,
$$
 VD^2\le s^{1-\epsilon},\qquad V\le h s^{-\epsilon}.
$$
For some $c(\epsilon)>0$ we obtain
$$
 \sum_{\substack{v_0,d\\(v_0,d)=1}}\beta_{v_0}a_d
 \left(\sum_{v_0 n\equiv N\bmod d} w(v_0 n)
       -\frac{1}{v_0d}\int_{\mathbb R}w(b)\,db\right)
       \ll h s^{-c(\epsilon)} .                                        \tag{2}
$$
The inner variable $n$ is unrestricted. In particular arbitrary prime weights can be retained on a factor of $v_0$. We give details because the power saving in (2) is responsible for crossing one in (1).

Poisson summation in $n$ gives nonzero frequencies $m/d$ with multiplier
$$
 \frac{h}{v_0d}\widehat f\left(\frac{mh}{v_0d}\right)
 e\left(\frac{mN\overline{v_0}}{d}-\frac{ms}{v_0d}\right).
$$
An inverse modulo one represents the trivial phase. Choose $\kappa=\epsilon/100$ (shrinking $\epsilon$ first if necessary). The range $|m|>(VD/h)s^\kappa$ is negligible to any power of $s$ by repeated integration by parts, allowing constant dyadic factors. If the range retained is empty there is nothing to bound. Split it into sign and dyadic blocks $|m|\asymp M$, $M\ge1$. After extracting $h/(VD)$, the amplitudes and their scaled derivatives in $v_0/V$ are bounded by powers of $\log s$ of fixed orders, uniformly in $m,d$. Indeed $y^j\widehat f^{(j)}(y)$ has such bounds at all real $y$.

Partition the frequencies in one block into $B$ intervals of width $O(M/(DB))$, $1\le B\le D$. One interval contains $O(M(1+D/B))$ pairs $(d,m)$, by fixing $m$ and counting $d$. Over all intervals the sum of the squares of the multiplicities of **equal fractions** is $O(DM\log(2D))$. For a reduced denominator $q\le 2D$ there are $O(Mq/D)$ possible nonzero reduced numerators and each fraction has multiplicity $O(D/q)$. These bounds use all integers, so they survive restrictions on the support.

Apply Cauchy–Schwarz over the bins, and within each bin in $v_0$, removing $\beta_{v_0}$. Here $\sum|\beta_{v_0}|^2\le Vs^{o(1)}$; extend the unweighted squared norm using a nonnegative smooth majorant for the dyadic $v_0$ interval. In the expansion take two distinct frequencies from one bin and put
$$
 \Delta=m/d-m'/d'=A/q,\quad (A,q)=1,\quad
 F=s|\Delta|/V,\quad
 s/(4VD^2)\le F\ll sM/(VDB).
$$
The corresponding sum over $v_0$ is $\ll s^{o(1)}\sqrt{qF}$. To verify this, fix the two frequencies first. Then $q\mid[d,d']$ is fixed, $(N,q)=1$, and $(v_0,[d,d'])=1$ implies that the difference of the modular phases is $NA\overline{v_0}/q$ modulo one. Impose $(v_0,q)=1$ directly. For the primes of $[d,d']$ absent from $q$, impose coprimality by Möbius inversion, at a cost of $s^{o(1)}$ divisors. In each term $v_0=l x$ with $(l,q)=1$, hence the inverse phase in $x$ has the unit coefficient $NA\bar l\bmod q$.

For completeness put $X=V/l$. Poisson completion in $x$ modulo $q$ gives complete Kloosterman sums divided by $q$ times integrals on $x\asymp X$. Their phases, after $x=Xy$, have the form $\pm F/y-jXy/q$. The smooth amplitudes have the derivative bounds above. Weil's bound for the complete sum is $\tau(q)\sqrt q$ for every $j$, since its inverse coefficient is a unit. The $j=0$ integral is $O_A(X(\log s)^{O_A(1)}F^{-A})$ by integration by parts. Here $F\gg s^\epsilon$, including fractions with a common original divisor. For $j\ne0$ of size $\ll qF/X$ there are $O(qF/X)$ modes, and the second derivative test bounds each integral by $O(X(\log s)^{O(1)}F^{-1/2})$. This test follows by separating an interval with first derivative of magnitude at most $\sqrt F$ (length $O(1/\sqrt F)$ in $y$) and integrating by parts on either side. For $|j|>CqF/X$ with $C$ sufficiently large, integration by parts gives $O_A(X(\log s)^{O_A(1)}(|j|X/q)^{-A})$; their total is negligible on taking $A$ large because $F\gg s^\epsilon$. All lengths and moduli are polynomial in $s$. Combining the modes proves the claimed bound. [Iwaniec–Kowalski, *Analytic Number Theory*, Corollary 11.12, composite-modulus Weil bound](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf)

For equal frequencies use the trivial bound $Vs^{o(1)}$. The sum of squared bin sizes is $O((DM)^2/B)$ from the bin occupancy bound. Inserting the diagonal multiplicity bound and $q\ll D^2$, the squared error on this dyadic block, divided by $h^2$, is
$$
 \ll s^{o(1)}
 \left(\frac{BM}{D}+
       \frac{M^2D}{V}\sqrt{\frac{sM}{VDB}}\right).                      \tag{3}
$$
Take $B\asymp(D/M)s^{-\epsilon/10}$, rounding to an integer. This is admissible since $M\ll(VD/h)s^\kappa$ and $V\le h s^{-\epsilon}$. The first term saves $s^{-\epsilon/10}$. The second is $\ll s^{\epsilon/20+3\kappa}(VD^2/s)^{3/2}$, using $h\asymp s^{2/3}$. Logarithmically many frequency blocks preserve a power saving. This proves (2).

## Using the longer sieve in the three-prime count

Fix dyadic ranges $r\asymp R$, $d\asymp D$, where $d$ is a product of **three distinct** band primes. Restrict $r$ to the prescribed prime range and $(r,N)=1$. Allow any nonnegative logarithmic weights on $d$ bounded by $O(L)$, including a sum of weights on some oriented pairs inside $d$. Write $J=\lceil(\log L)^{3/2}\rceil$. Majorize the product window by a smooth weight $w$ of the form in (2), equal to one on the window, of integral $h(1+O(L^{-2}))$, with transition collars of length $h/L^2$. Set
$$
 K=\frac{s^{1-2\epsilon}}{(2R)(2D)^2}.
$$
Here and below $\epsilon>0$ can be arbitrarily small and fixed. Use a Selberg square on $t$ with support on squarefree $m\le\sqrt K$ coprime to $P_z=\prod_{p\le z}p$. Its coefficients $\xi_m$ depend on the dyadic block and $z$, independently of the individual $r,d$. The square is one on all actual primes $t$ in the window. Its expansion imposes $k=[m,n]\mid t$, $k\le K$. Also upper-sieve $t$ at primes $\le z$ and $a$ at primes $\le z$ not dividing $N$, using the product of two nonnegative even-order Bonferroni truncations of order $J$ or $J+1$. Dropping squarefreeness and $t\nmid N$ is permissible for this positive upper bound.

A term of the small sieves imposes $l\mid t$, $j\mid a$; both $j,l\le z^{J+1}=s^{o(1)}$. With $t=lk n'$ the congruence is $(rlk)n'\equiv N\bmod dj$, where $(dj,N)=1$ and $(d,j)=1$. Nonunit $rlk$ give no solutions. For each fixed $l,j$ put $v_0=rlk$ and apply (2) with modulus $dj$. The coefficient on $v_0$ sums $\log r\,\xi_m\xi_n$ over the representations with $k=[m,n]$. Its absolute value is $s^{o(1)}$ by the divisor bound and $|\xi_m|\le m/\varphi(m)$. The coefficient on $dj$ depends only on $d$. Thus no prime or Selberg weight remains inside the completion step. We have $V(Dj)^2\le s^{1-\epsilon}$ eventually up to dyadic constants. Also $V\ll s^{1-6u+o(1)}=s^{5/8+o(1)}$, so $V\le h s^{-\epsilon}$ for small $\epsilon$. Dyadic blocks and all small sieve terms together cost $s^{o(1)}$ times the power-saving error in (2). This argument estimates the **sum** over $r,d$.

In the zero frequency the small-prime density is
$$
 V_z=W_z\delta_z,\qquad W_z=\prod_{p\le z}(1-1/p),\qquad
 \delta_z=\prod_{p\le z,\ p\nmid N}(1-1/(p-1)).
$$
Indeed $(l,j)=1$ is required, $p\mid N$ removes only the zero residue of $t$, and at $p\nmid N$ two residues are removed. The two truncated main terms give this product with additive error $O_A(L^{-A})$ for any fixed $A$: extend both sums absolutely past their truncations with tail bounded by a power of $L$ times $\sum_{j\ge J}(C\log L)^j/j!$. The large-prime quadratic form in the main term has the restriction $([m,n],d)=1$. Removing this restriction changes it by $O(L^{O(1)}s^{-u})$ uniformly. For each of the three $p\mid d$ sum $1/[m,n]$ over $p\mid m$ or $p\mid n$ by writing $m=g a,\ n=g b,\ (a,b)=1$, and putting $p$ into $g,a$ or $b$ in the resulting three harmonic sums. The sum is $O(L^3/p)$ before the two bounded coefficient factors.

The minimizing square gives $1/G$ with $G=\sum_{m\le\sqrt K,\ (m,P_z)=1}\mu^2(m)/\varphi(m)=(1+o(1))W_z\log\sqrt K$ uniformly, by the Euler-product calculation in the previous note with no excluded large primes. Thus with nonnegative weights the surviving upper main term sums the densities $2h\delta_z/(rd\log K)$ with relative $o(1)$ and total additive error $O_A(hL^{-A})$ after summing the blocks. The harmonic sums and all log weights in the additive errors cost only log powers. The factor $2$ comes from the square root in the support. In exponent variables $\tau=\log r/L$, $x_i=\log p_i/L$ for $d=p_1p_2p_3$, the denominator $\log K/L$ is $1-\tau-2\sum x_i-2\epsilon+O(1/L)$. Its limiting minimum at $\epsilon=0$ is $1/5$. One may let $\epsilon\downarrow0$ **after** taking the upper limit in $s$. [Selberg weights, normalization and uniform evaluation of $G$](FourthDivisorSieve.md)

## Separating exactly two from exactly three

Orient a marked pair $(p,q)$ by giving this order weight $\log r\,\log p$; its two orders recover the original mass. Set $I=\log(66/65)$ and $\lambda=\log(v/u)=\log(6/5)$. The empirical law of $(\tau,x,y)=(\log r,\log p,\log q)/L$ for marked pairs converges on fixed rectangles to the product probability measure
$$
 d\nu=\frac{d\tau}{I(1-\tau)}\frac{dx}{v-u}\frac{dy}{\lambda y}.
$$
Indeed the fixed-center pair estimate allows arbitrary bounded pair masks and a fixed subinterval for $r$. The normalization on that subinterval is (2) of the previous note with the corresponding integral. Apply the prime number theorem on the two exponent intervals, omitting repeated primes and primes dividing $N$ at power-saving cost. In particular $A_2\sim h\delta_z I(v-u)\lambda L$. [Fixed-center two-prime estimate](ThreePrimeDivisorMoment.md) · [Mass of the real sample](FourthDivisorSieve.md)

On a fixed rectangle $E$ in these three variables the triple upper sieve, with the oriented pair selected in $E$, gives
$$
 \limsup_{s\to\infty}\mathbb E_s[1_E Z]\le \int_E C(\tau,x,y)\,d\nu,\qquad
 C(\tau,x,y)=2(1-\tau)\int_u^v\frac{dt}{t(1-\tau-2x-2y-2t)}.          \tag{4}
$$
To see the weights, each admissible ordered $(p,q)$ extends by every third prime dividing $a$. Its weight remains $\log r\log p$. In the sieve main term the $r$ sum supplies $L\,d\tau$, $p$ supplies $L\,dx$, and the other two primes supply $dy/y$ and $dt/t$. Dividing by $\log K$ and by $A_2/(h\delta_z)$ gives (4). A fixed interval restriction on $r$ goes into its separate coefficient; the remaining orientation and interval restrictions on each triple are a single weight on $d$. All prime sums have limits by partial summation on compact ranges away from zero.

On every record $1_{Z=0}\ge1-Z$. Apply this on each cell of a finite partition, using zero as the lower bound on cells where the bound would be negative. Pass to finer partitions by continuity. This yields two bounds with different content:
$$
 \limsup M_s\le\int C\,d\nu,\qquad
 \liminf \mathbb P_s(Q=2)\ge\int (1-C)_+\,d\nu.                        \tag{5}
$$
Keeping the positive part inside the second integral retains more exact-two weight than subtracting the global estimate for $M_s$ from one.

Both integrals admit directed rational bounds. For the first, after cancelling $1-\tau$, use independent uniform $\tau,x$ and two log-uniform band exponents $y,t$. The prefactor is $2(\beta-\alpha)\lambda/I$. Jensen gives $(\beta-\alpha)/I\le131/200$. With $y,t=u(6/5)^v$ for a uniform parameter $v\in[0,1]$, the reciprocal gap is separately convex in all four uniform coordinates, so 24-panel product trapezoids give an upper bound. For the second, partition $\tau,x,y$ into $80^3$ equal-width boxes in ordinary exponent coordinates. The function $C$ increases in all three coordinates. At the three upper endpoints bound its inner log-uniform integral from above by 16-panel trapezoids. For the cell density use $(\beta-\alpha)/I\ge1-\beta$, $1/(1-\tau)$ at its lower endpoint and $1/y$ at its upper endpoint. Throughout use the nine-term alternating series upper bound for $\lambda$, upward rounding of each geometric node by integer powers and of each reciprocal to units of $10^{-7}$. Round each cell's lower contribution down. These operations give $\int C\,d\nu<0.98461$ and $\int(1-C)_+\,d\nu>0.02513$. Strict slack proves (1), since $W_3\le A_2-W_2$. [Rational certificates, reduced-denominator checks and actual finite marked counts](CheckPairTripleDispersion.py)

The argument provides a lower bound for exactly two and an upper bound on the relative weight of exactly three. A positive lower bound for $W_3$ would need additional information. For example an abstract inclusion law can have pair masses $c_p c_q$, singleton masses $c_p(1-\sum_{q\ne p}c_q)$ and empty mass $1-\sum c_p+\sum_{p<q}c_pc_q$, with $c_p=1/(p-1)$. These are nonnegative for large $s$, realize the reference single and pair inclusions, and put zero mass on every triple. For a further decrease of $M_s$, the remaining analytic question is whether the true-prime count on these triple progressions can beat the upper-square constant or the level $K$ in aggregate. The other Goldbach sectors remain open.
