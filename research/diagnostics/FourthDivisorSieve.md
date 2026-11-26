# A pointwise fourth-divisor bound for the reflected semiprime sample

Fix an integer $s$, $N=2s$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $h=H-2T$ and $z=\exp(L/(\log L)^3)$. Take $b=rt\in[s-H,s-2T)$ with $r,t$ prime, $s^\alpha<r\le s^\beta$, $\alpha=17/50,\ \beta=7/20$. Retain $(b,N)=1$, squarefree $a=N-b$ and $(a,P_z)=1$, where $P_z=\prod_{p\le z}p$. Give each record weight $\log r$ and write $U_s$ for their total weight. Let $\mathcal P=\{p\text{ prime}:s^u<p\le s^v,\ p\nmid N\}$ with $u=1/16,\ v=3/40$. Denote the number of these primes dividing $a$ by $Q(a)$.

Select a record and an unordered pair of distinct band primes $p,q\mid a$ with joint probability proportional to $\log r\,\log(pq)$. Write $\mathbb P_s,\mathbb E_s$ for this law and set $Z=Q(a)-2$, $M_s=\mathbb E_s Z$. For **every sufficiently large $s$** the law exists and
$$
 M_s<1.475,\qquad \mathbb P_s(Q(a)\le3)>0.525.                         \tag{1}
$$
These bounds apply even at an exceptional center of the [short-packet estimate](ThirdDivisorPackets.md). The one-sided target for the signed three-prime contribution is $M_s\le\log(6/5)+o((\log L)^{-3})$, with $\log(6/5)\simeq0.18232$. Other parts of the Goldbach expansion have separate error terms. The arguments below are unconditional.

## The total weight at a prescribed center

Set $I=\log((1-\alpha)/(1-\beta))=\log(66/65)$ and $\delta_z=\prod_{\ell\le z,\ \ell\nmid N}(1-1/(\ell-1))$. Uniformly in $s$, for each fixed $A>0$,
$$
 U_s=h\delta_z\sum_{s^\alpha<r\le s^\beta,\ r\ {\rm prime},\ r\nmid N}
             \frac{\log r}{r\log(s/r)}+O_A(hL^{-A})
     =h\delta_z I+O_A(hL^{-A}).                                        \tag{2}
$$

Here is the transfer from intervals averaged in position to one specified $s$. Put $J=\lceil(\log L)^{3/2}\rceil$ and $Q_0=z^{J+1}$. For a dyadic block $R<r\le2R$ clipped to the prime range, put $X=s/R$, $B=X^{1/4}$, and $I_r=[(s-H)/r,(s-2T)/r)$. For $j\mid P_z$, $(j,N)=1$ and $\omega(j)\le J+1$, let $\theta(I_r;j,c)$ be the sum of $\log t$ over primes in the indicated class. Koukoulopoulos's Theorem 1.1 and its unconditional specialization at $c=12/5+\epsilon$ bound the integral of $\sum_{j\le Q_0}E(y,B;j)$ over each dyadic interval of size comparable to $X$ by $O_D(XB L^{-D})$. Here $E$ is the maximum over reduced residues of the absolute error against $B/\varphi(j)$. The exponent condition holds since $Q_0=s^{o(1)}$ and $B=X^{1/4}$. The larger interval $[X/3,2X]$ needs only a bounded number of such estimates. [Koukoulopoulos, *Primes in short arithmetic progressions*, Theorem 1.1 and the subsequent remark, arXiv v2, pp. 2–3](https://arxiv.org/pdf/1405.6592v2#page=2)

For $r\nmid N$ put $c_{r,j}=N\bar r\bmod j$. Approximate the sharp prime sum by the average of the sums on $(y,y+B]$ for $y\in I_r$, integrating with factor $1/B$. Only two collars of length $B+1$ differ, at a cost $O((B+1)L)$ per $(r,j)$. For each $y$ the multiplicity $\#\{r:y\in I_r\}$ is at most $1+h/y\ll h/X$ since $X\ll s^{1-\alpha}=o(h)$. Consequently, even with absolute values before summing over $r$ and $j$,
$$
 \sum_{r,j}\left|\theta(I_r;j,c_{r,j})-\frac{h}{r\varphi(j)}\right|
 \ll R Q_0(B+1)L+
      \frac{h}{XB}\int_{X/3}^{2X}\sum_{j\le Q_0}E(y,B;j)\,dy
 \ll_D hL^{-D}.
$$
Indeed $R Q_0(B+1)\ll s^{\beta+(1-\alpha)/4+o(1)}=o(hL^{-D-1})$. This uses the integral of absolute errors summed over moduli, including its maximum over residues. It needs no estimate at any particular $y$.

Apply consecutive Bonferroni truncations of orders $J,J+1$ to forbid $\ell\mid a$ for $\ell\le z,\ell\nmid N$ on prime $t$. In the main term the error is bounded by the tail of $\sum_{k\ge J}(C\log L)^k/k!\ll_D L^{-D}$. In converting the log-weight on $t$ use $\log t=\log(s/r)+O(H/s)$ on the original records before truncation. The factor $\log r/\log(s/r)$ is bounded. Removing products divisible by a prime of $N$ in the ranges of $r,t$ costs $O((h s^{-\alpha}+1)L^{O(1)})$ on the original support, since there are $O(1)$ such primes and each $b$ has at most one allowed representation. Among the remaining rough $a$, the nonsquarefree cases cost $O((h/z+\sqrt{s})L)$ by counting multiples of squares. These errors and all dyadic blocks are absorbed in (2). Partial summation with the classical prime number theorem evaluates the sum over $r$ as $\int_\alpha^\beta d\tau/(1-\tau)+O_A(L^{-A})$.

Write $W_z=\prod_{\ell\le z}(1-1/\ell)$ and $\nu_\ell=1+1_{\ell\nmid N}$. Then $V_z=\prod_{\ell\le z}(1-\nu_\ell/\ell)=W_z\delta_z$. The product $\delta_z/W_z$ is the truncated even Goldbach singular series, including the factor $2$ at $\ell=2$. The tail from $\ell>z$ differs from one by $o(1)$ uniformly since $\sum_{\ell>z,\ell\mid N}1/\ell\ll L/z$ and $\sum_{\ell>z}1/\ell^2\ll1/z$. Thus $\delta_z\sim e^{-\gamma}\mathfrak S(N)/\log z\gg1/\log z$. In particular (2) removes the denominator hypothesis in the previous packet result. In each packet of length $\lfloor X^{3/8}\rfloor$, $M_s=\log(6/5)+O_A((\log X)^{-A})$ outside $O_A((\log X)^{C(A)})$ centers. No claim about which centers are exceptional is needed for (1).

## Four distinct divisors at one center

Let $d$ be any product of four distinct members of $\mathcal P$. At fixed allowed $r$ put $Y=h/(rd)$. We have $Y\gg s^{1/60}$, since $\beta+4v=13/20$. The number of actual records with this $r$ and $d\mid a$ satisfies, uniformly,
$$
 \#\{t\}\ \le\ (2+o(1))\,\frac{h\delta_z}{r\varphi(d)\log Y}.           \tag{3}
$$

To prove it, impose $t\equiv N\bar r\bmod d$. Sieve both $t$ and $N-rt$ at primes $\le z$. On $t$, use a Selberg square with real coefficients $\xi_m$ on squarefree $m\le D=\sqrt{Y}\exp(-4g)$, $(m,P_zd)=1$, $g=L/(\log L)^{3/2}$ and $\xi_1=1$. Actual primes $t>D$ have square weight one. For $k=[m,n]$, the additional condition $k\mid t$ gives one progression of length $Y/k$ in counting measure before endpoint rounding. On that progression there are exactly $\nu_\ell$ forbidden classes modulo $\ell\le z$, by CRT. The count after the small sieve equals
$$
 (Y/k)V_z + O_C\big((Y/k)L^{-C}+(1+2z)^{J+2}\big).
$$
Indeed the two adjacent Bonferroni sums differ from the product by at most the exponential-series tail used in (2), now with $\sum_{\ell\le z}\nu_\ell/\ell=O(\log L)$. Rounding each intersection costs at most $\prod_{\ell\mid j}\nu_\ell$. The two-sided error here permits signed coefficients in the expanded square.

The minimum of $\sum_{m,n}\xi_m\xi_n/[m,n]$ is $1/G$ with $G=\sum_{m\le D,\ (m,P_z d)=1}\mu^2(m)/\varphi(m)$ and $|\xi_m|\le m/\varphi(m)\ll L$. This follows by diagonalizing with $\sum_{k\mid m}\varphi(k)=m$ and inverting on the divisor-closed support. Since $\sum_{m,n\le D}1/[m,n]\ll L^3$ by extracting their gcd and $D^2(1+2z)^{J+2}\le Y\exp[-(7-o(1))g]$, the count is at most $YV_z/G+O_A(YL^{-A})$. [Selberg weights and inversion](LargeLeastPrimeSemiprimes.md#how-large-can-the-isolated-sum-be)

For the leading constant, factor the Dirichlet series for $G$ as $\zeta(1+w)C(w)$ before truncation. At $p\mid P_zd$ the local correction is $1-p^{-1-w}$. Otherwise it is $(1+p^{-w}/(p-1))(1-p^{-1-w})$. Thus $C(0)=W_z\varphi(d)/d$. At $\Re w=-1/\log z$ the sum of the absolute Dirichlet coefficients with the shifted weights is $L^{O(1)}$: the small primes cost $\exp(O(\sum_{p\le z}1/p))$, the four primes of $d$ cost $O(1)$, and the remaining local errors are $O(p^{-2+2/\log z})$. The tail beyond $\sqrt D$ saves arbitrary log powers after returning to $w=0$, even with a logarithmic weight. Convolve the remaining coefficients with the harmonic sum up to $D/m$ to get
$$
 G=C(0)(\log D+\gamma)+C'(0)+O_A(L^{-A}).
$$
Logarithmic differentiation gives $|C'(0)/C(0)|\ll\log z+1$ (the excluded primes contribute $\sum_{p\mid P_zd}(\log p)/(p-1)$ and the generic terms are absolutely summable). Since $\log z=o(\log D)$ and $\log D\sim\tfrac12\log Y$ uniformly, (3) follows. This computation keeps the local factors for $p=2$, $p\mid N$ and $p\mid d$ separately.

## From incidences to the constant

Let $A_i$ be the sum of $\log r\,\log d$ over all records and all products of $i$ distinct band primes dividing $a$. Put $V_i=\sum_d\log d/\varphi(d)$ over the unrestricted products of $i$ distinct band primes. The earlier fixed-center two-divisor estimate gives $A_2=U_s V_2+O_A(hL^{-A})$, $V_2\sim(v-u)\lambda L$, $\lambda=\log(v/u)$. In a triple each logarithm occurs in two constituent pairs. In a quadruple it occurs in three constituent pairs, and the other two primes can be ordered in two ways. Hence
$$
 M_s=2A_3/A_2,\qquad \mathbb E_s[Z(Z-1)]=6A_4/A_2.                   \tag{4}
$$
In particular $A_2>0$ eventually by (2). [Fixed-center pair estimate and signed-block identity](ThreePrimeDivisorMoment.md)

Let $\tau$ be uniform on $[\alpha,\beta]$, $x_1$ uniform on $[u,v]$, and $x_2,x_3,x_4$ have density $1/(\lambda x)$ on $[u,v]$, all independent. Summing (3) with its positive weights and dividing by (2) and $V_2$ yields
$$
 \limsup_{s\to\infty}\tfrac12\mathbb E_s[Z(Z-1)]
 \le \frac{\beta-\alpha}{I}\lambda^2\,
       \mathbb E\!\left[\frac1{2/3-\tau-x_1-x_2-x_3-x_4}\right].       \tag{5}
$$
In detail the prime $r$ supplies $L\,d\tau$ via $\log r/r$ and the four prime divisors supply $\prod_i dx_i/x_i$ via $1/(p_i-1)$. The quotient $\log d/\log Y$ tends uniformly to $\sum_i x_i/(2/3-\tau-\sum_i x_i)$. Symmetry gives four choices of an $x_i$ to cancel, and unordered divisors contribute $1/4!$. In the half moment these multiply $3\cdot 2$ from (3)–(4), giving coefficient one. The prime number theorem gives these limits by partial summation on compact exponent ranges. Coincident prime indices and the band primes dividing $N$ have total reciprocal weight $O(L^{O(1)}s^{-u})$. The gap is at least $1/60$.

For a rational certificate in (5), Jensen's inequality gives $(\beta-\alpha)/I\le1-(\alpha+\beta)/2=131/200$. An upper bound for $\lambda$ is the nine-term alternating Taylor sum at $1/5$. Write the last three coordinates as $u(6/5)^y$ with $y$ uniform on $[0,1]$. The reciprocal gap is separately convex in each of the five normalized uniform coordinates, since the reciprocal is increasing and convex as a function of the sum and the exponential coordinates are convex. The 16-panel composite trapezoid rule in each coordinate therefore bounds the integral from above. The checker rounds each exponential node upward using integer powers and each reciprocal upward to a multiple of $10^{-7}$. It gives an upper bound $21.8007$ for the expectation in (5), and the product using the unrounded rational quadrature bound is strictly below $0.47467$. Since $Z$ is a nonnegative integer, $Z\le1+Z(Z-1)/2$ and $1_{Z\ge2}\le Z(Z-1)/2$. With strict slack this proves (1). The signed term in the preceding note consequently satisfies $H_3(s)/(U_sV_2)\ge-(1.475-\lambda)/2+o(1)$. The remaining loss is of order $U_sV_2\asymp h\mathfrak S(N)(\log L)^3$. [Rational certificate, finite incidence counts and CRT checks](CheckFourthDivisorSieve.py)

## Why a bound on rare high multiplicities leaves a gap

Set $c_p=1/(p-1)$, $\lambda_s=\sum_{p\in\mathcal P}c_p$. There is a law on subsets of the band with the exact reference single and pair inclusions, **zero** fourfold and higher inclusions, and pair-weighted $M=1+o(1)$. Prescribe triple inclusions $\prod_{p\in T}c_p/\lambda_s$ and invert on subsets as in the earlier inclusion model. Each exact pair mass is $c_i c_j(1-\sum_{k\ne i,j}c_k/\lambda_s)\ge0$. Singleton masses are at least $c_i(1-\lambda_s)$ and the empty mass is at least $1-\lambda_s+e_2-e_3/\lambda_s>0$, where $e_i$ are the elementary symmetric sums and $3e_3\le\lambda_s e_2$. Triples have nonnegative mass, and inversion gives total mass one. Its pair-weighted mean is $2V_3/(\lambda_s V_2)=1+o(1)$. One can also keep the independent inclusions on close triples by reducing just their multiplier to one. The same lower bounds on atoms apply, including nonnegativity for pairs, and the close reference weight is $o(V_3)$ at the earlier shrinking cutoff. This abstract law only describes divisibility statistics.

For actual records put $D_s=\mathbb P_s(Z=0)$ and $T_s=\mathbb E_s[(Z-1)_+]$. The exact identity $M_s=1-D_s+T_s$ singles out the remaining question. To reach the signed-block target, one needs $D_s-T_s\ge1-\log(6/5)-o((\log L)^{-3})$. In the model even perfect upper bounds on fourfold and higher incidences coexist with $D_s=o(1)$. A productive next estimate would distinguish reflections with exactly two band primes from those with exactly three at the prescribed center.
