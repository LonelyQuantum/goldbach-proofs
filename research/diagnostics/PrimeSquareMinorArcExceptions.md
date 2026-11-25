# Signed minor arcs at twice a prime square

For the Goldbach desk let $e(t)=\exp(2\pi it)$, $S_n(t)=\sum_{\ell\le n,\ \ell\ {\rm prime}}\log\ell\,e(\ell t)$, and $Q=\lfloor\log_2(n+2)\rfloor^2$. On the unit circle take the union of the arcs about reduced $a/q$, $q\le Q$, with radius $Q/(qn)$. Write $J_Q(n)$ and $I_Q(n)$ for the integrals of $S_n(t)^2e(-nt)$ on this union and its complement. Reflection $t\mapsto -t$ makes both integrals real. Their sum $R_{\mathbb P}(n)$ counts ordered prime pairs with product logarithmic weights. The lengths here are those of the full-support desk problem. [Project arc convention](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/649) · [Fixed-mask exception proposal](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/453)

**Unconditional consequence.** Fix $A,\varepsilon>0$. For sufficiently large $P$, uniformly for $P^{1/3+\varepsilon}\le H\le P$, all but $O_{A,\varepsilon}(H/(\log P)^A)$ prime indices $p\in[P,P+H]$ satisfy, with $n=2p^2$,
$$
 |I_Q(n)|\ll n\,\frac{\log\log n}{(\log n)^2}.
$$
In particular the desk threshold $I_Q(n)\ge -n$ holds off this exceptional set. On dyadic intervals the exceptions have relative density zero among primes. The count applies throughout the stated short-interval range. Relative density in an individual interval also needs a lower bound for the number of primes there, available for example when $H\ge P^{7/12+\delta}$ for fixed $\delta>0$. These statements allow isolated exceptional prime indices. They concern the full range of summands. [Perelli (1996), Theorem 1 and Corollary 1, pp. 477–478](https://doi.org/10.4171/RMI/205) · [Baier–Zhao, Lemma 6 with modulus 1](https://arxiv.org/pdf/math/0701577v6#page=5)

## 1. The major integral at every prime-square target

For even $n$ write $\mathfrak S(n)=\sum_{q\ge1}a_q(n)$ with $a_q(n)=\mu(q)^2 c_q(n)/\varphi(q)^2$ and $c_q$ the Ramanujan sum. This series converges absolutely for each $n$. Its value at $n=2p^2$ for an odd prime $p$ is $2C_2(p-1)/(p-2)$, with $C_2=\prod_{\ell>2,\ \ell\ {\rm prime}}(1-1/(\ell-1)^2)$. [Montgomery–Vaughan, §18.2, equation (18.15)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)

The following estimate also applies if $Q$ is replaced by $T$ with $2\le T\le(\log n)^B$ for fixed $B$. Put $K_n(t)=\sum_{j=0}^n e(jt)$ and
$$
 F_q=\frac{1}{n+1}\int_{-T/(qn)}^{T/(qn)} |K_n(t)|^2\,dt \quad(q\le T),\qquad F_q=0 \quad(q>T).
$$
For $n$ sufficiently large the arcs are disjoint up to endpoints. By Siegel–Walfisz and partial summation, on each arc $S_n(a/q+t)=\mu(q)K_n(t)/\varphi(q)+O_{B,L}(n/(\log n)^L)$ for every fixed $L$. Starting with von Mangoldt weights costs $O(\sqrt n\log^2 n)$ to remove proper prime powers; adding the $j=0$ term to the model costs at most one. The total arc length is $O(T^2/n)$. Squaring, integrating and increasing $L$ absorbs all fixed powers of $\log n$. Summation over the numerators gives $c_q(-n)=c_q(n)$, and $K_n(t)^2 e(-nt)=|K_n(t)|^2$ exactly. Thus for every fixed $D>0$,
$$
 \frac{J_T(n)}{n+1}=\sum_{q\ge1} a_q(n)F_q+O_{B,D}((\log n)^{-D}).
$$
The classical uniform expansion (18.22) covers these radii. [Montgomery–Vaughan, §18.2, equation (18.22)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)

The full mass of $|K_n|^2$ is $n+1$ and $|K_n(t)|\le 1/(2|t|)$ for $0<|t|\le 1/2$. Integrating the two discarded tails gives $|1-F_q|\le\min(1,q/T)$, including $q>T$. For each squarefree $q$ write $q=gd$ with $g=(q,n)$, so $g\mid\operatorname{rad}(n)$ and $(d,n)=1$. Multiplicativity gives $|a_q|=1/(\varphi(g)\varphi(d)^2)$.

Here is an elementary estimate for the sum over $d$. Write $b(d)=(d/\varphi(d))^2$. Expanding the nonnegative divisor sum $b(d)=\prod_{\ell\mid d}(1+[(\ell/(\ell-1))^2-1])$ and counting multiples gives
$$
 \sum_{d\le y} b(d)\le y \prod_{\ell\ {\rm prime}}\left(1+\frac{(\ell/(\ell-1))^2-1}{\ell}\right)\ll y .
$$
Partial summation gives $\sum_{d\le y}b(d)/d\ll\log(2y)$ and $\sum_{d>y}b(d)/d^2\ll1/y$ for $y\ge1$. For $g\le T$ split at $y=T/g$; for $g>T$ bound the whole convergent sum. The result is
$$
 \left|\sum_q a_q F_q-\mathfrak S(n)\right|
 \ll \frac{\log(2T)}T\sum_{g\mid\operatorname{rad}(n)}\frac{g}{\varphi(g)} .
$$
At $2p^2$ this divisor factor is $(1+2)(1+p/(p-1))\le 15/2$ for odd $p$. Consequently
$$
 J_Q(2p^2)=n\,\mathfrak S(n)+O\!\left(n\,\frac{\log(2Q)}{Q}\right)
 \quad(n=2p^2)
$$
for **every** sufficiently large prime $p$. In particular widening the arc parameter from $Q$ to any $Q\le T\le(\log n)^B$ changes the signed integral by $O_B(n\log(2Q)/Q)$ at every such target. This also holds for families with a fixed bound on the number of distinct prime factors, with a constant depending on that bound.

## 2. Transfer of Perelli's polynomial mean square

Use $F(m)=2m^2$, degree $k=2$, and $N=P^2$ in Corollary 1 of Perelli. The paper's condition $H\ge N^{1/(3k)+\eta}$ becomes $H\ge P^{1/3+2\eta}$. Choose $\eta=\varepsilon/2$. For every prescribed $D$, the full von Mangoldt correlation at $n=F(m)$ is $n\mathfrak S(n)+O_{D,\varepsilon}(P^2/(\log P)^D)$ outside $O_{D,\varepsilon}(H/(\log P)^D)$ integer indices. Restrict the exceptional indices to primes. Each ordered pair lost in replacing $\Lambda$ by prime weights has a proper prime power at one of its two ends. There are $O(\sqrt n\log n)$ candidates for that end and at most one complement, so the total loss is $O(\sqrt n\log^3 n)$ pointwise. Subtract the estimate of §1 for $J_Q$ from this estimate for $R_{\mathbb P}$. Taking $D>\max(A,3)$ proves the claimed bound. This procedure uses one full-circle Fourier coefficient for each target and permits both the mask and the prime sum to change with $n$. [Perelli, original article, pp. 477–481](https://content.ems.press/assets/public/full-texts/serials/rmi/12/2/5197/online/10.4171-rmi-205.pdf)

## 3. A power bound for failures of the one-sided threshold, conditional on two analytic inputs

Assume precisely the smoothed fourth-moment estimate and the smoothed major-arc asymptotic stated as Theorems B and C in §2 of Althöfer–Chen–Perelli–Pintz (arXiv v1, 6 November 2026), for the same fixed weight $0\le w\le1$ and power-scale arcs. These analytic inputs and their external zero-free-region dependencies have not been independently verified here. For each fixed $\lambda>C_2/2$ and $\varepsilon>0$ they imply
$$
 \#\{P<p\le2P:\ p\ {\rm prime},\ I_Q(2p^2)\le-\lambda(2p^2)\}
 \ll_{\lambda,\varepsilon}P^{1/2+\varepsilon}.
$$
This includes $\lambda=1$. The preprint's stated exceptional set counts missing representations. We adapt its proof to the desk's signed deficit, which can occur even at a represented target. [Althöfer–Chen–Perelli–Pintz, §§1–4, Theorems B/C and Lemma G](https://arxiv.org/html/2611.09386v1)

Choose $0<\delta<1/2$ so that $C_2/[2(1-\delta)]<\lambda$. Cover $2P^2<n\le8P^2$ by $O_\delta(1)$ intervals $( (1-\delta)X,X]$, with $X\asymp P^2$. Within each interval use one fixed prime sum $S_w(t)=\sum_\ell w(\ell/X)\log\ell\,e(\ell t)$ and one fixed power-scale split from B/C. Write $R_w=J_w+I_w^{\rm min}$ for its full coefficient. The convolution of the weights $V_w(n)=\sum_j w(j/X)w((n-j)/X)$ is at least $n-X/4-1$, by counting integers from $X/8$ to $n-X/8$ where both weights equal one. Theorem C gives $J_w(n)=\mathfrak S(n)V_w(n)+O(X^{1-c})$ for fixed $c>0$.

If $I_Q(n)\le-\lambda n$, positivity of the weights gives $R_w(n)\le R_{\mathbb P}(n)=J_Q(n)+I_Q(n)$. By §1, $\mathfrak S(2p^2)=2C_2+o(1)$ uniformly here, hence
$$
 I_w^{\rm min}(n)\le\mathfrak S(n)(X/4+1)-\lambda n+o(n)
 \le-\left(\lambda-\frac{C_2}{2(1-\delta)}-o(1)\right)n .
$$
For all large $P$ this is negative by a fixed multiple of $X$. This inequality transfers the deficit before applying a moment inequality with one fixed mask.

If $Z$ prime indices in this interval have the deficit, put $K(t)=\sum_{p\ {\rm in\ that\ set}}e(-2p^2t)$. The fourth moment of $K$ counts equal differences of twice-squares. The zero difference contributes $Z^2$. For $u\ne0$ the factorization $2(x-y)(x+y)=u$ bounds its number of representations by $O_\eta(P^\eta)$, and there are at most $Z^2$ ordered pairs in total. Thus $\int|K|^4\ll_\eta P^\eta Z^2$. By Hölder with $(4,2,4)$, Theorem B, and $\int|S_w|^2\ll X\log X$,
$$
 ZX\ll_{\lambda,\delta}\int_{\rm minor}|S_w|^2|K|
 \ll_\eta \big(X^{5/2}\log^{100}X\big)^{1/4}
          (X\log X)^{1/2}(P^\eta Z^2)^{1/4}.
$$
Dividing and squaring gives $Z\ll_\varepsilon X^{1/4}P^{\varepsilon}\ll_\varepsilon P^{1/2+\varepsilon}$ after taking $\eta$ small and absorbing the logarithms. Sum over the finite cover. [Preprint, (2.1), (2.2), (3.7) and (4.3)–(4.7)](https://arxiv.org/html/2611.09386v1)

Both bounds on exceptional indices can accommodate a single offending prime in arbitrarily large blocks. At an individual $2p^2$, §1 removes the band of denominators between the desk scale and every fixed power of the logarithm from the list of possible sources of an order-$n$ deficit. Controlling the remaining signed integral at that individual target, or confining the two primes to a shrinking central window, requires further information.

## Finite arithmetic checks

In a standard-library Python check, for all 45 odd primes $p<200$ and $1\le q\le256$ we computed $c_q(2p^2)=\sum_{s\mid(q,2p^2)}s\mu(q/s)$ and compared the exact rational $a_q$ with its grouped formula (zero for non-squarefree $q$). All 11,520 identities agreed. For $P=10,20,40,80,160,320$, take the primes in $[P,2P]$ in increasing order, then separately take the full list, every second element starting at the first, every third starting at the second, and the last element alone. All 24 lists passed the equal-sums/equal-differences energy identity and the divisor bound for each nonzero difference. For every integer $16\le X\le256$ and $\lceil X/2\rceil\le n\le X$, direct counting verified the plateau lower bound in §3, in 16,569 cases. These are exact checks of the finite identities used above.
