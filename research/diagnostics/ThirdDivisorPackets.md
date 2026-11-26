# The third reflected divisor at fixed and nearby Goldbach targets

Write $N=2s$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $h=H-2T$, $z=\exp(L/(\log L)^3)$ and $P_z=\prod_{p\le z}p$. Take primes $s^{17/50}<r\le s^{7/20}$ and $t$ with $b=rt\in[s-H,s-2T)$; then $r<t$. Put $a=2s-b$. The notation $\sum_b^*$ retains $(rt,N)=1$, squarefree $a$ and $(a,P_z)=1$, and includes weight $\log r$. In the band $\mathcal P_s=\{s^{1/16}<p\le s^{3/40}:p\ {\rm prime},\ p\nmid N\}$, set $X_p(a)=1_{p\mid a}$, $c_p=1/(p-1)$, $Q_s(a)=\sum_p X_p(a)$, and $U_s=\sum_b^*1$. Denote by $\mathcal D_s$ the unordered products of three distinct band primes. The previous [three-divisor calculation, (1)–(4)](ThreePrimeDivisorMoment.md) supplies the fixed-target first two moments and identifies the signed high-conductor block $H_3(s)$ with the centered triple sum to $O_A(hL^{-A})$.

## How many centers can have an excess?

Define the signed discrepancy and its version conditioned on a pair by
$$
 \begin{aligned}
 E(s)&=\sum_{d\in\mathcal D_s}\log d
       \left(\sum_b^*1_{d\mid a}-U_s/\varphi(d)\right),\\
 E_e(s)&=\log e\sum_b^*1_{e\mid a}
       \sum_{\ell\in\mathcal P_s,\,\ell\nmid e}(X_\ell(a)-c_\ell),
       \qquad e=pq,\ p<q,\ p,q\in\mathcal P_s .
 \end{aligned}
$$
Thus $H_3(s)=-E(s)+O_A(hL^{-A})$. For every fixed $A>0$, in **every** integer interval $X\le s<X+K$, $1\le K\le X^{1/2}$, the following bounds hold, with $H_X=\lfloor X^{2/3}\rfloor$, $L_X=\log X$.

| Quantity exceeding $H_X L_X^{-A}$ | Upper bound for the number of centers |
|---|---|
| $|E(s)|$ | $\ll_A L_X^{2A+8}(1+K X^{-3/8})$ |
| $\sum_e |E_e(s)|$ | $\ll_A L_X^{2A+8}(1+K X^{-1/4})$ |
| $\sum_{d\in\mathcal D_s}\log d\,|\sum_b^*1_{d\mid a}-U_s/\varphi(d)|$ | $\ll_A L_X^{2A+8}(1+K X^{-3/16})$ |

In particular the full block has at most a power of $\log X$ exceptional centers in a packet of length $X^{3/8}$. For pairs one can take absolute values **after conditioning on each pair**; the corresponding packet length is $X^{1/4}$. These are absolute discrepancies. At centers with $U_s\ge H_X L_X^{-B}$ for a fixed $B$, the first estimate and [the earlier ratio formula](ThreePrimeDivisorMoment.md#the-surviving-three-prime-correlation-and-its-sign) give $M_s=\log(6/5)+O_A(L_X^{-A})$ outside the corresponding exceptional set (increase the working error exponent by $B+A+2$ if necessary). No uniform lower bound for $U_s$ is needed to estimate $H_3(s)$.

**Reduction to a fixed trigonometric polynomial.** Multiply each centered triple by a coefficient bounded by $O(L_X)$, allowing either a label $e\mid d$ or a label $d$ when taking the outer absolute values. The coefficients within each label are fixed after freezing. A sign depending on the center may multiply the entire label output when its absolute value is taken. For the second row of the table use $X_pX_q(X_\ell-c_\ell)$ with $e=pq$. Write $X_p=(X_p-c_p)+c_p$ and likewise for $q$. After multiplying each pair by an arbitrary sign, the two-factor error terms have coefficients $O(L_X\sum c_p)=O(L_X)$, and the one-factor terms cost $O(L_X(\sum c_p)^2)=O(L_X)$. Both are $O_A(hL^{-A})$ by the previous fixed-target one- and two-divisor estimates, also for products of two centered indicators by expansion. This argument with arbitrary signs on triples gives the third row as well. The first row is its signed counterpart. Hence it suffices to analyze just the fully centered products; the sign convention for those products is immaterial here.

Freeze the product interval, $r$-band, prime divisor band and wheel at $X$. The target in $a=2s-b$ still varies. Omit $(rt,N)=1$ at cost $O_A(hL^{-A})$: any lost product is a multiple of one of the $O(1)$ primes $>s^{17/50}$ dividing $N$. Allow all primes in the frozen divisor band. For a prime $p$ of the band dividing $N$, $p\nmid rt$ and $X_p(a)=0$; the sum of its reference weights is $O(L_X X^{-1/16})$. The product window changes by $O(K+1)$ integers, the $r$ and divisor-band thresholds move by less than one for the stated $K$, and $z$ also moves by less than one. A crossing prime $p$ contributes $O(h/p+1)$ multiples in the relevant window, plus its reciprocal weight when it is used in a centered product. These estimates apply before averaging. Indeed $Q_s(a)=O(1)$, $\sum c_p=O(1)$, and $\sum_d\prod_{p\mid d}(c_p+X_p(a))=O(1)$, also with at most three pair labels per triple. There is at most one allowed smaller prime $r$ per semiprime $b$. All freezing errors, including log weights, are $O_A(hL^{-A})$ uniformly in the outer signs.

Replace each $c_p$ by $1/p$ in the centered products. Telescoping costs $O(L_X\sum_p 1/(p(p-1)))=O(L_X X^{-1/16})$ per integer before the outer $\log r$. Drop the squarefreeness restriction on rough $a$ at a cost bounded using $O(h/z+\sqrt X)$ positions. On these odd $a$ expand the roughness indicator over odd squarefree $j\mid P_z$, $\omega(j)\le J=\lceil(\log L_X)^{3/2}\rceil$, with weight $\mu(j)$. The truncated expansion agrees with the indicator unless $\omega(a)>J$, has size at most $\tau(a)$, and all its $j$ satisfy $j\le z^J=X^{o(1)}$. The short-interval divisor moments on the window of length comparable to $H_X$ and $2^{\omega(a)}\le\tau(a)$ give a total $O_A(hL^{-A})$ error by Cauchy–Schwarz. All sharp approximations here are on the original arithmetic side. [Divisor moments and wheel truncation, step 1](ProperDivisorScales.md#recovering-the-main-term-after-strengthening-the-sieve)

Write $e(x)=\exp(2\pi i x)$. The factor $1/p-1_{p\mid a}$ equals $-p^{-1}\sum_{1\le b<p} e(ba/p)$. Consequently each frequency of a given triple contains **all three** primes in its reduced denominator. After multiplying by $1_{j\mid a}$, the reduced denominator is $q=dk$, $k\mid j$, and both $d$ and $k$ are determined by $q$. At each reduced numerator the contribution from this $j$ has magnitude $1/(dj)$ by the Chinese remainder theorem. Including the logarithmic weight, its total coefficient is
$$
 |C_{a'/q}|\ll \frac{L_X}{d}\sum_{k\mid j,\ j\mid P_z}\frac1j
          \ll \frac{L_X^2}{q}.
 \tag{1}
$$
In this bound the last sum may be enlarged beyond the truncation; the actual frequencies use only truncated $j$. Here $\prod_{p\le z}(1+1/p)\ll\log z\ll L_X$. All $q$ are odd, so multiplication by two permutes reduced numerators and preserves reduced denominators.

Let $B(\alpha)=\sum_b w_b e(-b\alpha)$ for the frozen semiprime window, $w_b=\log r$ on its records and zero otherwise. For a fixed label the output is a sum of $C_{\alpha}B(\alpha)e(2s\alpha)$. The additive large sieve on a length-$M$ integer interval has squared norm $\ll M+\delta^{-1}$ for frequencies spaced by $\delta$ modulo one, in both the direct and dual forms. Apply it first to $B$. All denominators are at most $X^{9/40+o(1)}$, so their squared maximum is $o(H_X)$, and $\sum_\alpha|B(\alpha)|^2\ll H_X\sum_b|w_b|^2\ll H_X^2 L_X^2$. The sum here runs over the distinct actual reduced frequencies. No cancellation assumption on semiprimes is used in this step. [Montgomery–Vaughan, *The large sieve*, Theorem 1](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf)

For labels with $i=0,2,3$ band primes respectively (empty label, a pair, the whole triple), group the labels $e\asymp E$ and denominators $q\asymp Q$ dyadically. For $i=0$ take $e=E=1$. Within one fixed label every denominator is a multiple of $e$. Distinct doubled frequencies are separated modulo one by $\gg E/Q^2$, since the least common multiple of any two such denominators is $\ll Q^2/E$. Apply the dual sieve on $K$ consecutive centers, then Cauchy–Schwarz on at most $O(E)$ labels. Each frequency is counted at most $\binom{3}{i}$ times over the labels. By (1) the squared norm of the sum of absolute label outputs on this shell is
$$
 \ll L_X^4\frac{E(K+Q^2/E)}{Q^2}
              \sum_{\alpha\ {\rm on\ shell}}|B(\alpha)|^2 .
$$
As $q^2/e\ge X^{(6-i)/16}$, Cauchy–Schwarz over $O(L_X^2)$ shells costs $O(L_X^2)$ in the squared norm. Each frequency occurs in at most three shells, since it determines $d$ and the dyadic denominator range, and $d$ has at most three labels of the given size. The preceding energy bound therefore gives $O(H_X^2 L_X^8(1+K X^{-(6-i)/16}))$. This bound is for the frozen polynomials. Restore the uniform errors at a smaller threshold and apply Chebyshev's inequality to obtain the table. The argument counts exceptions; it does not rule out the prescribed first center of a packet.

## What cancels at every individual center

There is also a pointwise reduction that retains the original prime $r$. Write
$$
 G_s(a)=\sum_{d\in\mathcal D_s}\log d\prod_{p\mid d}(1/p-X_p(a)).
$$
Let $I_r=\{t:s-H\le rt<s-2T\}$. For $0<\epsilon<11/120$, let $Y=s^{11/120-\epsilon}$. If $|\alpha_v|\le \tau(v)^C L^C$ for $v\le Y$, then
$$
 \sum_{\substack{r\ {\rm in\ band}\\ r\ {\rm prime},\,r\nmid N}}
 \log r\sum_{v\le Y}\alpha_v\sum_{w:vw\in I_r}
       G_s(N-rvw)\,1_{(N-rvw,P_z)=1}\,g_{r,v}(w)
       \ll_{A,C,\epsilon} hL^{-A}.
 \tag{2}
$$
Here the supremum norm plus total variation of $g_{r,v}$ on the relevant interval is at most $L^C$. This includes the log and reciprocal-log weights below. The same bound holds for bounded masks on triples, or one signed choice per pair after summing its third primes, in the fully centered kernel. Formula (2) has integer cofactors and is an estimate for a part of a prime-detecting identity.

Use the truncated wheel, this time including 2 since integer $t=vw$ may be even. The truncation error remains $O_A(hL^{-A})$: each $b$ has at most two possible divisors $r>s^{17/50}$, and summing the absolute weights for $v\mid b/r$ costs a fixed power of $L\tau(b)$. Short-interval moments and Cauchy–Schwarz on the reflected windows handle these factors. For fixed $r,v,d,j$, some band prime $p\mid d$ does not divide $rv$, since $r$ exceeds every band prime and $d>s^{3/16}>Y$. Over a complete period of length $dj$ the $p$-factor has mean zero independently of all the other factors, including the wheel, by CRT. Expand the three centered factors into eight terms. Each resulting condition $ej\mid N-rvw$, $e\mid d$, specifies either no $w$ or one class modulo $ej/(ej,rv)$. Thus on **every** interval the unweighted remainder after subtracting the complete period mean is $O(8)$, including when $v$ shares factors with $dj$. Partial summation handles $g_{r,v}$. The cost of all rounding is at most
$$
 s^{7/20}Y\,s^{9/40+o(1)}=s^{2/3-\epsilon+o(1)},
$$
using the usual maximal order $\tau(v)=s^{o(1)}$ and $j\le z^J$. This proves (2).

For example fix any $0<\eta<11/240$ and put $V=s^\eta$, $b_V(m)=\sum_{k\mid m,\ k>V}\mu(k)$. The unresolved expression for $H_3(s)$ at a specified center is, to $O_A(hL^{-A})$,
$$
 \sum_{\substack{r\ {\rm in\ band}\\ r\ {\rm prime},\,r\nmid N}}\log r
 \sum_{\substack{m,n>V\\ mn\in I_r}}
   b_V(m)\frac{\Lambda(n)}{\log(mn)}
   1_{(N-rmn,P_z)=1}G_s(N-rmn).
 \tag{3}
$$
Indeed start with the previous arithmetic formula for $H_3(s)$, replace the centers $c_p$ by $1/p$ as above, and remove the squarefree restriction on rough $a$. Omitting $t\nmid N$ on the original primes costs only log-small error by counting multiples of the few large primes dividing $N$. Replace their indicator by $\Lambda(t)/\log t$. For each $r$, the number of higher powers in $I_r$ is $O(L((h/r)/\sqrt{s/r}+1))$ by counting each exponent separately; the sum over $r$ is $O(s^{7/20}L^{O(1)})$ here since $(h/r)/\sqrt{s/r}\ll1$. Their weights are bounded. With $*$ denoting Dirichlet convolution, the exact identity is
$$
 \Lambda=\mu_{\le V}*\log - \mu_{\le V}*\Lambda_{\le V}*1
             +\Lambda_{\le V}+b_V*\Lambda_{>V}.
$$
It follows from $\log=1*\Lambda$ and $\mu*1$ being the convolution identity. The singleton term vanishes at the present $t$. The first two sums have a coefficient variable at most $V^2$, hence satisfy (2) by choosing $0<\epsilon<11/120-2\eta$. The last term is (3). This reduction uses neither GRH nor a lower bound for $U_s$. A one-sided bound at each center still needs cancellation involving the two remaining factors in (3). Other sectors of the original Goldbach expansion also remain. [Exact finite checks](CheckThirdDivisorPackets.py)

The checker compares the integer and Fourier kernels at 17 successive centers on a frozen semiprime window, including four actual triple incidences after its diagnostic wheel. It also verifies spacing of doubled fractions, CRT counts with noninvertible slopes, and the four-term convolution identity with a completely additive integer substitute for the logarithm. These checks concern the finite transformations; the exceptional-set estimates use the large sieve.
