# Composite partners in the triple-divisor Selberg majorant

Use the real records and marked-pair mass $A_2$ of [the fixed-center dispersion estimate](PairTripleDispersion.md). Thus $N=2s$, $h=\lfloor s^{2/3}\rfloor-2\lfloor s^{21/40}\rfloor$, $L=\log s$, $z=\exp(L/(\log L)^3)$. The smaller prime $r$ has exponent $\tau\in(\alpha,\beta]=(17/50,7/20]$. Three distinct primes of the reflection $a=N-rt$ have exponents in $(u,v]=(1/16,3/40]$. Extend the partner $t$ from primes to integers with $(t,P_z)=1$, retaining the sharp product window, $(rt,N)=1$, and squarefree $a$ coprime to $P_z$. Here $P_z=\prod_{p\le z}p$. In a triple $d\mid a$ orient the marked pair $(p,q)$ and distinguish its third prime. Give this choice mass $\log r\log p$. Write $\langle f\rangle_s$ for its sum with test $f$, divided by $A_2$. This positive measure is not normalized to have mass one. Its restriction to prime $t$ has total mass **exactly** $M_s$.

We obtain a pointwise lower bound on actual composite weight at a specified sieve length. At a loss of $1/40$ in the exponent of the sieve level, partners with a prime divisor in $(s^{1/200},s^{1/100}]$ alone contribute more than $0.0234 A_2$ of unnormalized square weight at every sufficiently large $s$. Comparison with the limiting sieve gives more than $0.1134 A_2$ from all composites at this shorter length. The bounds do not yield a fixed saving from the limiting upper integral $C_0$. A separate mixed-product identity locates the obstruction to such a saving.

## Total and composite square weights

On each of the previous dyadic blocks $r\in(R,2R]$, $d\in(D,2D]$ set $K_* =s/((2R)(2D)^2)$ and $B_\sigma=(K_*s^{-\sigma})^{1/2}$. All $B$ below are radii for divisor weights, not counts. For squarefree $j$ coprime to $P_z$ define
$$
 h_j(t)=\prod_{p\mid j}(p\,1_{p\mid t}-1),\quad
 G(B)=\sum_{j\le B}^{*}\frac1{\varphi(j)},\qquad
 F_B(t)=\frac1{G(B)}\sum_{j\le B}^{*}\frac{\mu(j)}{\varphi(j)}h_j(t).
$$
The star denotes this same support throughout. This is the minimizing Selberg root: expanding $h_j$ in divisibility indicators gives the usual coefficients $\xi_m$, with $\xi_1=1$. At primes $t>B$ the value is one. In the model where the indicators $1_{p\mid t}$ are independent of means $1/p$, the $h_j$ are orthogonal with squared norms $\varphi(j)$. Consequently the model means satisfy $\mathbf E F_B^2=1/G(B)$ and $\mathbf E F_B F_{B'}=1/G(B')$ for $B\le B'$.

Write $\gamma=1-\tau-2(x+y+w)$, where $x,y,w$ are the exponents of the three indicated primes. Let $\mathbf E_0$ make $\tau,x$ uniform on their respective exponent intervals and $y,w$ independently log-uniform on $(u,v]$. Set $\lambda=\log(6/5)$, $I=\log(66/65)$, and
$$
 J_k(\sigma)=\frac{2(\beta-\alpha)\lambda}{I}\,
             \mathbf E_0[(\gamma-\sigma)^{-k}],\qquad C_\sigma=J_1(\sigma).
$$
For fixed small $\sigma>0$, at every sufficiently large center in the asymptotic sense,
$$
 \langle F_{B_\sigma}^2\rangle_s=C_\sigma+o(1),\qquad
 \langle 1_{t\ {\rm composite}}F_{B_\sigma}^2\rangle_s
                         = C_\sigma-M_s+o(1).                            \tag{1}
$$
Although the model evaluates the main term, the left sides count the actual integers. The error tends to zero with $\sigma$ fixed.

Here are the transfer details for (1) and its variants below. For a pair of roots, expansion gives divisor conditions $[m,n]\mid t$. With extra distinct prescribed marks of product $P\mid t$ the condition is $[m,n,P]\mid t$, avoiding any assumption that the marks are coprime to $mn$. Summing over marks can be included in the coefficient of the resulting integer since the multiplicity is bounded by a fixed divisor power. The fixed-center estimate (2) of the preceding note applies provided $BB' P\le K_*s^{-c}$ for a fixed $c>0$. The $r$ and divisor coefficients remain separate from the triple coefficient. The $s^{o(1)}$ small sieve factors fit inside this slack. The zero mode gives the two-end small-prime density $W_z\delta_z(N)$ of that note, times the independent divisor model on primes $>z$. The excluded primes of $d$ cause a total error of arbitrary negative log power: in the reciprocal lcm sum the cost of divisibility of $[m,n]$ by such a prime $p$ is $O(L^{O(1)}/p)$ as in the previous proof. The tag band used below is disjoint from the prime factors of $d$; coincident marks with $m,n$ are retained. One can bound absolute tagged zero-mode errors by summing over divisors of $[m,n]$ for shared tag primes and reciprocal weights for the other tags. This costs only log powers after the harmonic lcm sum, by fixed divisor moments (or the prime Euler product for the sum with weight $1/[m,n]$). A specified $p\mid d$ in those sums still saves $1/p$ up to log powers.

For signed products, truncate both small wheels on the arithmetic side. The error is supported where $b=rt$ or $a=N-b$ has more than $\lceil(\log L)^{3/2}\rceil$ prime divisors. All absolute weights here, including the truncated wheels, are bounded by fixed powers of $L,\tau(a),\tau(b)$, where $\tau(n)$ here denotes the divisor function. In particular $|\xi_m|\le m/\varphi(m)$, and each $b$ has $O(1)$ candidate $r$ in the fixed band. Short-interval divisor moments, $2^{\omega(n)}\le\tau(n)$ and Cauchy–Schwarz give error $O_A(h L^{-A})$. They also allow product collars of width $h/L^{C(A)}$. On small-sifted records, nonsquarefree $a$ or $t$ cost the same error since there are $O(h/z+\sqrt{2s})$ candidate integers $a$ or $b$ divisible by a square $p^2$, $p>z$. Thus we may remove repeated factors from composite $t$ when convenient. Common prime divisors $p>z$ of $b,N$ cost $O(hL/z+L)$ positions before the divisor-moment bound. Small common divisors are excluded on the support. This proves the transfer for the sharp genuine sample, including signed products. The previous Euler calculation gives $G(B)\sim W_z\log B$ uniformly for the polynomial radii here. The same prime exponent sums and pair normalization as before give $C_\sigma$. [Short-interval moment application](ProperDivisorScales.md) · [Shiu's multiplicative-function theorem](https://doi.org/10.1515/crll.1980.313.161)

In particular $\limsup M_s\le C_0$ by first using a fixed positive $\sigma$ and then letting it decrease. Directed integration gives $0.984570<C_0<0.984577$ and $1.098096<C_{1/40}<1.098104$. The first enclosure refines the numerical evaluation of the preceding integral. Equation (1) gives the $0.1134$ lower bound stated above. It compares sieve lengths and does not identify the responsible factors. In each packet of $\lfloor X^{3/8}\rfloor$ centers, outside at most a power of $\log X$ exceptions, the earlier result gives $M_s=\lambda+o(1)$. There the composite share of the square is $1-\lambda/C_\sigma+o(1)$, over $81.4\%$ even as $\sigma\downarrow0$ after the center limit. This last assertion permits exceptional centers. [Packet estimates](ThirdDivisorPackets.md) · [Uniform denominator](FourthDivisorSieve.md)

## Which composites can be counted directly?

Take $\sigma=1/40$, $\eta=1/200$, and tag factors $s^\eta<p\le s^{2\eta}$. The double-tag cost $s^{4\eta}$ leaves $s^{-1/200}$ of power slack in the level. Set $Y(t)$ equal to the number of distinct tags dividing $t$. Every hit forces $t$ composite.

For fixed squarefree $P$ made of tags, conditioning on $P\mid t$ in the divisor model collapses the coefficient of $\mu(j)h_j/\varphi(j)$ in $G(B)F_B$ to
$$
 T_P(j)=\sum_{\substack{k\mid P\\kj\le B}}\mu(k),\qquad (j,P)=1 .
$$
The conditional second moment, including the probability of the condition, is $\sum_{(j,P)=1}^{*}T_P(j)^2/\varphi(j)$ divided by $P\,G(B)^2$. For $P=p$ only the shell $B/p<j\le B$ survives. For $P=pq$ with $p<q$ and $pq<B$, the two surviving shells are $(B/p,B]$ with sign $+1$ and $(B/(pq),B/q]$ with sign $-1$. Endpoints follow from $kj\le B$. All the shell endpoints here are fixed positive powers of $s$. Relative to the original square weight their main terms are respectively $\log p/(p\log B)$ and $2\log p/(pq\log B)$, with relative $o(1)$ uniform over the tags. This uses $G(X)\sim W_z\log X$ at each endpoint. Deleting at most two primes $>s^\eta$ changes the harmonic sums negligibly.

Put $\theta=(\gamma-\sigma)/2$. Partial summation on tag primes gives the conditional multipliers $\eta/\theta$ for $Y$ and $2\eta(1-\log 2)/\theta$ for $\binom Y2$. For the latter, integrate $2\min(x,y)/(xy)$ over $\eta<x<y<2\eta$. Since $1_{Y>0}\ge [4Y-Y(Y-1)]/6$ for nonnegative integers, the tagged composite weight satisfies
$$
 \liminf_s\langle 1_{Y>0}F_{B_{1/40}}^2\rangle_s
 \ \ge\ 2\eta\,\frac{2\log 2}{3}J_2(1/40)>0.0234.                    \tag{2}
$$
The inequality vanishes at $Y=0$ and attains one at $Y=2,3$. Thus (2) charges a composite at most once even when it has several tagged factors. The identified saving is smaller than the $C_{1/40}-C_0$ cost of making room for the marks. No fixed main-order saving below $C_0$ follows from this calculation.

## A mixed product below the old reference constant

Fix $0<\rho\le1/100$, and in the same dyadic block take $B_-=B_{3\rho}$, $B_+=B_{-\rho}$. Their product is $K_*s^{-\rho}$, inside the dispersion range even though the square of $B_+$ is beyond it. The orthogonal cross moment is $1/G(B_+)$. If $P_s^-,P_s^+$ denote respectively the normalized negative and positive parts of $F_{B_-}F_{B_+}$ on **composite** partners (the minus part is positive in magnitude), then
$$
 M_s=C_{-\rho}+P_s^- -P_s^++o_\rho(1).                                 \tag{3}
$$
For $\rho=1/100$ the mixed constant is $<0.945494$. In particular $\limsup_s P_s^-\le0.034$ would suffice for $M_s<0.980$ eventually. This is a sufficient test; (3) allows cancellation with $P_s^+$. Merely multiplying the two roots is not an upper sieve. The finite checker gives opposite signs at the same atom of an exact finite divisor model.

There is a uniform reduction of the negative part. For each fixed integer $j\ge1$, write $k(t)=\#\{z<p\le B_+:p\mid t\}$ on its own dyadic block. Then
$$
 \limsup_{s\to\infty}\langle 1_{k(t)\le j}(F_{B_-}F_{B_+})_-\rangle_s
       \ll_j \rho^2(1+|\log\rho|)^j=o_j(\rho)\quad(\rho\downarrow0).     \tag{4}
$$
The order of limits matters. The gap $C_0-C_{-\rho}$ is of order $\rho$. Thus no fixed bound on the number of relevant prime factors can account for an obstruction of this order in the small-$\rho$ limit.

Here are details. For $S=\{p:z<p\le B_+,\,p\mid t\}$, $|S|\le j$, put $x_p=\log p/L$. At either radius $B=s^w$ the root differs by $O_j((\log L)^{-3/2})$ from
$$
 f_w(S)=\sum_{U\subset S}(-1)^{|U|}\left(1-\sum_{p\in U}x_p/w\right)_+ .
$$
Indeed summing the orthogonal formula first over divisors of $\prod_{p\in S}p$ gives the same alternating combination of harmonic prefixes $G^{(S)}(B/\prod_{p\in U}p)/G(B)$, where the primes of $S$ are removed. The removal costs $O_j(1/z)$ in the normalized prefixes. Uniformly above $X_0=\exp(L/(\log L)^{3/2})$, the previous harmonic convolution gives $G(X)=W_z(\log X+O(\log z+1))+O_A(L^{-A})$ for $X_0\le X\le B_+$. The shifted coefficient tail still gains $\exp[-c(\log L)^{3/2}]$ there. Below $X_0$ use positivity and $G(X_0)$, and use an empty prefix below one. This proves the asserted uniform approximation. [Harmonic convolution proof](FourthDivisorSieve.md#four-distinct-divisors-at-one-center)

The normalized radii have exponents bounded away from zero. For fixed $j$ the profile is Lipschitz in $w$, so its change between the radii is $O_j(\rho)$. If $S$ is nonempty, pairing each subset with its translate by the least member gives $|f_w(S)|\ll_j\min x_p$. At opposite signs the absolute product is at most one quarter the square of the difference. The empty configuration contributes no negative part. Consequently the negative integrand is bounded by $O_j(\min(\rho,\min x_p)^2+(\log L)^{-3})$ on the remaining configurations.

To sum this bound with the necessary prime-scale gain, fix $b>0$ small in terms of $j$, with $(j+2)b<1/10$ and $s^b<B_-$ eventually. On squarefree $t$ let $m$ be the product of all its primes in $(z,s^b]$. In (4), $m$ has at most $j$ distinct factors and $t/m$ has no prime factor $\le s^b$. Discard the negligible nonsquarefree cases as above. For an upper bound use a Selberg square of radius $s^b$ on $t/m$, supported on primes $>z$, with coefficients independent of $m$. Each counted cofactor has square weight one. The additional divisor level including $m$ is at most $s^{(j+2)b}$, strictly within the previous triple range even at $\gamma=1/5$. In the zero mode $t=m n$ and $n$ is unrestricted apart from the two small wheels and the square. Since $m$ is a unit at the small wheel and is smaller prime-by-prime than every factor of $d$ (choose $b<u$), the usual density and square calculation gives the following upper bound for a nonnegative weight $g(m)\le1$:
$$
 \langle 1_{k(t)\le j}g(m)\rangle_s
 \ll_j \sum_{\substack{m\ {\rm squarefree},\ \omega(m)\le j\\p\mid m\Rightarrow z<p\le s^b}}
                 g(m)/m+o_j(1).
$$
The diagonal factor is $1/m$, even if the auxiliary square divisors divide $m$, because the sieve square acts on the cofactor $n$. The uniform $1/\log(s^b)$ gain absorbs the prime normalization. The same dispersion bound allows arbitrary bounded coefficients on these $m$. For the constant error term the reciprocal sum is $O_j((1+\log\log L)^j)$. For the other term use $\min(\rho,\min_{p\mid m}x_p)^2$, with empty minimum interpreted as infinity. Its layer integral is at most $\int_0^\rho 2y\,O_j((1+\log_+(b/y))^j)\,dy$ by the prime reciprocal sum on $(\max(z,s^y),s^b]$. This proves (4).

For one or two relevant primes the limiting profile is nonnegative for all $w$. For three, $w f_w$ has the sign of $\sum_{p\in S} x_p-2w$ whenever it is nonzero. Indeed for $w$ below the largest exponent one has the nonnegative two-prime profile until half the total; between the largest exponent and half the total only the singleton subtractions enter, giving $\sum x_p-2w$. Reflection in half the total reverses the profile by pairing complementary subsets. Thus the negative part at $k=3$ is negligible away from $B_-^2\le\prod_{p\in S}p\le B_+^2$, by the same count for the approximation error. At $k\le2$ it is $o(1)$ after normalization for fixed $\rho$ (one root can be slightly negative by the approximation error, and the other is bounded). The open estimate is uniform control as the multiplicity grows, or control of the signed difference in (3). None of these reductions proves the central prime-pair assertion.

The rational verifier uses midpoint lower and trapezoid upper bounds for the separately convex reciprocal-gap integrands, geometric nodes rounded outwards, and rational series bounds for the logarithms. It checks the marked and mixed moments on every atom of a finite divisor model and verifies the finite-difference signs. [Reproducible checker](CheckCompositePartnerWeight.py)
