# A fixed-target divisor range for reflected products of two primes

Take a sufficiently large integer $s$, and write $N=2s$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $h=H-2T$, $I=[s-H,s-2T)$. Use
$$
 w=(2s)^{1/3},\quad R=s^{1/7},\quad z=\exp(L/(\log L)^3),\quad
 J=\lceil(\log L)^{3/2}\rceil,\quad Z=h\exp(-4L/(\log L)^{3/2}).
$$
Set $P_z=\prod_{\ell\le z,\ \ell\ {\rm prime}}\ell$, and $S_s=h\mathfrak S(N)$ with the usual even-target singular series. In [the unswitched divisor expansion, (1) and (1a)](LargeLeastPrimeSemiprimes.md), a semiprime $b=pq$ with $w<p<q$ can supply two logarithms. Label the prime supplying the logarithm by $r$ and the other by $t$. For any two prime weights $|\alpha_r|,|\beta_t|\le1$ and any divisor interval $\mathcal D\subset(R,Z/w]$, consider the actual signed sum
$$
 C(\mathcal D)=
 \sum_{\substack{r,t>w\ {\rm prime},\ r\ne t,\ rt\in I\\
                    (rt,N)=1,\ a=N-rt\ {\rm squarefree},\ (a,P_z)=1}}
     \alpha_r\beta_t\log r
     \sum_{\substack{d\mid a,\ d\in\mathcal D\\ dr\le Z}}\mu(d)\log d .
 \tag{1}
$$
In particular, unit prime weights give the semiprime contribution in that expansion. The weights may select either prime in a prescribed interval. All estimates below are uniform in the integer $s$ and in these bounded weights. They concern the joint sum over the primes at this one center.

**Fixed-target estimates.** Given $A>0$, there are constants $B,K>0$ such that, writing
$$
 F_0=(h/\sqrt{s})L^{-B},\qquad D_0=F_0/z^J,\qquad
 r_0=\sqrt{s}\exp[-2L/(\log L)^{3/2}],
$$
the following bounds hold.

1. If $\sup\mathcal D\le D_0$ and $\alpha_r$ vanishes for $r<wL^K$, then $C(\mathcal D)\ll_A hL^{-A}$. Without that restriction, $C(\mathcal D)\ll_A S_s(\log L)^{c}/L+hL^{-A}$ for an absolute $c$. Thus every fixed range $s^{1/7}<d\le s^{1/6-\epsilon}$, $0<\epsilon<1/42$, has total signed contribution $o(S_s)$.
2. For $\alpha_r$ supported on $r\ge r_0$, the full divisor interval satisfies $C((R,Z/w])\ll_A hL^{-A}$. Consequently both orientations of pairs with $p,q\ge r_0$ may be removed together. For $p<r_0$ the orientation $r=q$ may also be removed, by imposing $t<r_0,\ r\ge r_0$. The surviving logarithm is the one on the smaller prime.
3. After the arithmetic removals the sector equals, to $O_A(S_s(\log L)^c/L+hL^{-A})$, a **smoothed** character sum with
$$
 wL^K\le r<r_0,\qquad D_0<d\le Z/r,\qquad
 f\mid dj,\quad f>F_0.
 \tag{2}
$$
Here $f$ is a primitive character conductor and $j$ is the small-prime divisor in the expansion below. Other partner classes in the Goldbach expansion still require estimates.

There is also an absolute mean over the labeled prime. Fix $\beta$ and write (1) as $\sum_r\alpha_r C_r(\mathcal D;\beta)$, with $\log r$ included in $C_r$. Choose $\alpha_r=\overline{C_r}/|C_r|$ on the desired range wherever $C_r\ne0$. The bounds in assertions 1 and 2 then hold for $\sum_r |C_r|$ on those ranges. Thus the saving can be placed inside the sum over $r$, after summing the divisors and the other prime. No assertion of absolute cancellation before those inner sums is needed.

## Removing arithmetic restrictions and smoothing the window

Since $r,t>w$ and $(rt,N)=1$, the two reflected endpoints are coprime. A surviving $d$ is coprime to $NP_z$, and $d\le Z/w<w$ for large $s$. Keep these explicit restrictions when expanding. On rough $a$ the count spoiled by a repeated prime factor is $O(h/z+\sqrt{s})$ by summing multiples of squares. There are at most two labeled factorizations for each $rt$. By Cauchy–Schwarz, the fixed short-interval divisor moments give $O_A(hL^{-A})$ even with the logarithms and divisor multiplicities. The same estimate allows $r=t$, since $I$ contains $O(1+h/\sqrt{s})$ squares. The moments $\sum_{n\in I'}\tau(n)^k\ll_k |I'|L^{c_k}$ hold on these windows and collars of length $h/L^C$ for any fixed $C$, by Shiu's bound at modulus one. [Divisor moments and the stronger sieve](ProperDivisorScales.md)

The part $w<r<wL^K$ has absolute mass $O_K(S_s(\log L)^c/L)$, by the interchanged proper-divisor strip bound (1) in that same note. Indeed $r$ is a proper divisor of $b$ and there are $O_K(1+\log L)$ dyadic strips. This bound applies on the original arithmetic side. For all other terms $r\le Z/R<s^{11/21}$, so $t\gg s^{10/21}$ on the window and the collars below.

Convolve the interval indicator in $\log(rt/s)$ with a smooth nonnegative unit-mass kernel supported on $[-v,v]$, where $v=h/(sL^{C_0})$ and $C_0$ is large in terms of $A$. Call the resulting weight $W$. The difference is supported on two collars of $O(hL^{-C_0})$ integers each. By the divisor moments and the two-label bound its cost is $O_A(hL^{-A})$. Write $T_*=1/v$. For each fixed $k$ its Fourier transform satisfies
$$
 |\widehat W(\tau)|\ll_k (h/s)(1+|\tau|/T_*)^{-k}.
$$
Use the order-$J$ expansion for rough $a$ over $j\mid P_z$, $(j,N)=1$, $\omega(j)\le J$. Primes dividing $N$ cannot divide $a$ on the chosen support. The error is supported on $\omega(a)>J$ and bounded by a fixed divisor power times log weights. Its total is $O_A(hL^{-A})$ by $2^{\omega(a)}\le\tau(a)$, Cauchy–Schwarz and the same moments. We now have $rt\equiv N\bmod m$ where $m=dj$, and coefficient $\mu(d)\log d\,\mu(j)$. The modulus determines both $d$ and $j$, as $d$ is rough and $j$ is smooth. All prime factors of $m$ are smaller than $r,t$ even on the unrestricted prime rectangles used below (enforce $r,t>w$ there). Thus ordinary character orthogonality introduces primitive characters $\psi\bmod f$, $f\mid m$, with weight $\psi(r)\psi(t)\overline{\psi(N)}/\varphi(m)$. Formula (2) uses this expansion after smoothing the arithmetic sum.

## Small primitive conductors

For fixed $E$ and sufficiently large $s$, **$L^E<z$**. Thus if $f\le L^E$ divides $dj$ its prime factors all divide $j$, and $f\mid j$. There is no restriction from $f$ on the rough variable $d$. For each $r,t,j,\psi$ the only signed $d$ sum is over $\mathcal D\cap(R,Z/r]$ with weight $\mu(d)\log d/\varphi(d)$ and $(d,NP_z)=1$. It is $O_M(L^{-M})$ uniformly for every $M$. In particular there is no comparison of Euler factors for different integers $N$.

For details, write the Dirichlet series for $\mu(d)1_{(d,NP_z)=1}/\varphi(d)$ as $\zeta(1+u)^{-1}C_N(u)$. At prime $\ell$ the correction is $1/(1-\ell^{-1-u})$ for $\ell\mid NP_z$ and $(1-\ell^{-u}/(\ell-1))/(1-\ell^{-1-u})$ otherwise. At $\Re u=-1/\log z$ the absolute coefficient norm of $C_N$ is $L^{O(1)}$. Indeed the primes $\ell\le z$ cost $\exp(O(\sum_{\ell\le z}1/\ell))$, the larger primes dividing $N$ have reciprocal shifted sum $O(L/z)$, and the generic local errors are summable. The coefficient tail above $\sqrt R$ saves arbitrary log powers after shifting back. On the remaining indices the two sharp prefixes of $\mu(n)/n$ are log-small by the zero-free-region prime number theorem, and the two prefixes with the extra $\log n$ have the same constant. Subtract at the endpoints for this same $C_N$ to get the asserted bound, retaining the $\log$ of the convolution index. [Euler correction and uniform tail, steps 2–3](ProperDivisorScales.md)

The absolute $j$ sum of $1/\varphi(j)$ over multiples of $f$ is $\ll L^{O(1)}/\varphi(f)$ by the prime Euler product. The smoothed interval has $O(h)$ ordered prime pairs. Summing the log weights and the $O(L^{2E})$ characters with a larger $M$ bounds this whole part by $O_A(hL^{-A})$. This keeps the moving endpoint $Z/r$.

## Joint average over the two primes

On dyadic rectangles $r\asymp P,\ t\asymp Q$ intersecting the support we have $PQ\asymp s$. For $F<f\le2F$, the absolute weight lifting each primitive character to all allowed $m$ is
$$
 \ll L\sum_{\substack{m\ll s,\ f\mid m}}\frac1{\varphi(m)}
 \ll L^{c_1}/F .
$$
This uses uniqueness of $(d,j)$, $\varphi(fk)\ge\varphi(f)\varphi(k)$, and $\sum_{k\le s}1/\varphi(k)\ll L$. For $dr\le Z$ retain a supremum of prefixes of the $r$ polynomial *inside* the character and frequency norm.

For coefficients on $n\asymp P$, the hybrid inequality used here is
$$
 \sum_{f\le2F}\sum_{\psi\bmod f}^{*}
 \int_{-U}^U \left|\sum_n a_n\psi(n)n^{i\tau}\right|^2 d\tau
 \ll (F^2U+P)\sum_n|a_n|^2,\qquad U\ge1.
 \tag{3}
$$
For a direct deduction, integrate the squared character sums on $u<\log n\le u+1/U$ over real $u$. The squared Fourier multiplier of this interval is $\gg U^{-2}$ on $|\tau|\le U$. At fixed $u$, apply the multiplicative large sieve to an integer interval of length $O(1+P/U)$; integrating counts each $n$ for length $1/U$. Plancherel gives (3). For a supremum over prefix endpoints its right side acquires $O(L^2)$: use a binary interval tree on the indices. Each prefix uses at most one node per depth, disjoint nodes at a depth share the original total squared coefficient mass, and the triangle inequality in the joint norm sums the depths. [Kowalski–Vaughan, Lemma 2.1, ordinary multiplicative large sieve](https://personal.science.psu.edu/rcv4/personal/Publications/s00208-024-03069-3-1.pdf#page=4)

Fourier-invert $W$, use Cauchy–Schwarz for the two polynomials, and apply (3) with $U=T_*,2T_*,4T_*,\ldots$. Rapid Fourier decay sums this series. Bounding the squared coefficient masses by $PL^2$ and $Q$, the absolute bound for a block, divided by $h$, is at most
$$
 L^{c_2}\frac{\sqrt{(F^2T_*+P)(F^2T_*+Q)}}{F\sqrt{s}}
 \ll L^{c_2}\left(\frac1F+\sqrt{\frac{T_*}{P}}+
            \sqrt{\frac{T_*}{Q}}+\frac{FT_*}{\sqrt{s}}\right).
 \tag{4}
$$
We may include the logarithmically many choices of $P,Q,F$ in $c_2$, independently of $C_0,E,B,K$. Choose $C_0$ first for the collars, then $E>A+c_2+2$, $K>C_0+2(A+c_2+2)$ and $B>C_0+A+c_2+2$. On $L^E\le f\le F_0$ all four terms save the required log powers since $P\gg wL^K$, $Q\gg s^{10/21}$ and $T_*=(s/h)L^{C_0}$. Dyadic end blocks can be truncated. Together with the small-conductor argument, this bounds the full projection through $F_0$ by $O_A(hL^{-A})$ on the interior.

For $d\le D_0$, every possible $f$ satisfies $f\le dj\le D_0 z^J=F_0$. This proves assertion 1. For $r\ge r_0$, every $d$ is small enough because
$$
 (Z/r_0)z^J=(h/\sqrt{s})\exp[-(1+o(1))L/(\log L)^{3/2}]<F_0.
$$
Such $r$ are in the interior. Also $r_0^2<s-H$ eventually, so every pair with one prime $<r_0$ has its partner $>r_0$. This proves assertion 2 with separate prime weights for the stated restrictions. Finally apply the interior projection with $\mathcal D=(D_0,Z/w]$ and $r<r_0$ to obtain (2). The possible boundary error was estimated before the projection.

## An arithmetic expression for the outstanding conductors

The last term in (4) reaches order one, before log factors, at $F\asymp h/\sqrt{s}$. For the high conductors in (2), the signs and the phase can instead be combined exactly. For each squarefree $m=dj$ on the support, each unit product $b=rt$ and $a=N-b$, one has
$$
 \frac{\mu(m)}{\varphi(m)}
 \sum_{\substack{f\mid m\\ f>F_0}}\sum_{\psi\bmod f}^{*}
       \psi(b)\overline{\psi(N)}
 =\frac1{\varphi(m)}\sum_{e\mid(m,a)}\mu(e)\varphi(e)
      \sum_{\substack{v\mid m/e\\v<m/F_0}}\mu(v).
 \tag{5}
$$
The factor $\log d$ and the original prime and window weights remain outside this identity. Invert ordinary character orthogonality to obtain the primitive kernel $\sum_{e\mid(f,a)}\mu(f/e)\varphi(e)$. Write $f=eu$ and $m=euv$. Squarefreeness gives $\mu(m)\mu(u)=\mu(e)\mu(v)$; the strict bound on $v$ is equivalent to $f>F_0$. This proves (5), including equality at the cutoff. In particular the right side also vanishes for $m\le F_0$.

Here the complementary divisor $v$ is short even relative to $D_0$. Uniformly in the remaining range,
$$
 r v < Zz^J/F_0
 =\sqrt{s}\,L^B\exp[-(3+o(1))L/(\log L)^{3/2}]<r_0,\qquad
 v < (Z/w)z^J/F_0 < D_0.
 \tag{6}
$$
For the second comparison, divide by $D_0$ and use $Z z^{2J}/(wF_0^2)\ll L^{2B}\exp[-(2+o(1))L/(\log L)^{3/2}]$. This gives a precise next test: keep $e\mid N-rt$ and sum the signed complementary divisors $v\mid dj/e$. Applying assertion 1 directly to $v$ would require $v\mid N-rt$, which (5) does not impose. No one-sided estimate for (5) follows yet. Other partner classes must also be controlled to give a lower bound for the Goldbach count. [Exact finite character and divisor checks](CheckHybridSemiprimeFrontier.py)
