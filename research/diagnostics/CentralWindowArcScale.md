# How wide should the major arcs be for a central Goldbach window?

Fix an odd prime $p$ tending to infinity. Write $m=p^2$, $n=2m$, $H=\lfloor p^{4/3}\rfloor$, $M=2H+1$, $Q=\lfloor\log_2(n+2)\rfloor^2$, and $e(x)=\exp(2\pi i x)$. In the central window $W=[m-H,m+H]\cap\mathbb Z$ put
$$
 S(t)=\sum_{\ell\in W,\ \ell\ {\rm prime}}\log\ell\,e(\ell t).
$$
For $0<T\le Q$ take all reduced rationals $a/q$ on the unit circle with $q\le Q$, and let $\mathfrak M(T)$ be the union of their arcs of radius $T/(qM)$. Write $J(T)=\operatorname{Re}\int_{\mathfrak M(T)} S(t)^2 e(-nt)\,dt$ and $I(T)$ for the same integral over the complement. The task desk's original radii $Q/(qn)$ correspond to $T_0=MQ/n$. This note changes the support of the prime sum to $W$. The desk's bulk task retains a much longer support.

## Two main terms for the same prime sum

For the original radii and the radii scaled to the window, respectively, the paper calculation gives
$$
 J(T_0)=(\kappa+o(1))\,\frac{M^2Q}{n},\qquad
 J(Q)=(2C_2+o(1))M,
$$
where the products below run over odd primes:
$$
 \kappa=3\prod_{r>2}\left(1-\frac1{r(r-1)^2}\right),\qquad
 C_2=\prod_{r>2}\left(1-\frac1{(r-1)^2}\right).
$$
In particular the band $\mathfrak M(Q)\setminus\mathfrak M(T_0)$ carries $(2C_2+o(1))M$ of signed mass. All estimates are pointwise as $p$ tends to infinity through primes.

By orthogonality, $R=I(T)+J(T)$ is the sum of $\log\ell\log(n-\ell)$ over ordered prime representations with both endpoints in $W$. Hence $I(T_0)\ge-o(M)$ is automatic, including under the hypothesis $R=0$. The finer scale $B=M^2Q/n$ does discriminate. Under $R=0$ one has $I(T_0)/B\to-\kappa$ along any such sequence. A bound $I(T_0)\ge-(\kappa-\eta)B$ for some fixed $0<\eta<\kappa$ and every sufficiently large prime $p$ would imply $R\ge(\eta+o(1))B$. Each unordered pair contributes at most $2\log^2 n$, so this would give $\gg_\eta p^{2/3}$ unordered central pairs. The derivation below provides the major-arc term. This last minor-arc inequality remains a research target.

## A uniform formula for intermediate widths

Put $F(z)=\int_{-z}^z(\sin(\pi u)/(\pi u))^2\,du$, with the continuous value at zero, and define
$$
 P(T)=\sum_{\substack{d\ {\rm odd}\\d\ {\rm squarefree}}}
 \frac{\mu(d)}{\varphi(d)^2}\,[F(T/d)+F(T/(2d))].
$$
Uniformly for $0<T\le Q$ we obtain
$$
 J(T)/M=P(T)+o(\min(T,1)).
$$
Keeping the factor $T$ in the error is essential when using the original radii.

**Short progressions.** Fix $A>0$. At each reduced center, uniformly for $|\beta|\le Q/(qM)$,
$$
 S(a/q+\beta)=\frac{\mu(q)}{\varphi(q)}e(m\beta)D_H(\beta)
                 +O_A(M/\log^A n),\qquad
 D_H(\beta)=\sum_{|j|\le H}e(j\beta).
$$
To see the uniformity, let $x=m-H-1$ and take integer prefixes $(x,x+y]$ of $W$. For $y\ge M/\log^K n$ (fixed $K$), we have $y\ge x^{7/12+1/24}$ eventually since $M\asymp x^{2/3}$. Baier and Zhao's short-interval Siegel–Walfisz lemma applies to every reduced class for $q\le Q\le\log^3 x$, with an arbitrarily large power of logarithmic saving. Removing prime powers costs $O(\sqrt n\log^2 n)$ even over the full range up to $n$, which is $o(M/\log^D n)$ for each fixed $D$. The shorter prefixes cost $O((y+1)\log n)$ by direct summation. Every window prime exceeds $q$. Sum over reduced classes with the additive phase, using $c_q(a)=\mu(q)$, then apply partial summation against $e(k\beta)$. The losses of at most $q$ and $1+O(M|\beta|)$ are polylogarithmic. Choosing $K$ and the saving in the lemma sufficiently large proves the displayed estimate. [Baier and Zhao, *On Primes in Quadratic Progressions*, v6, Lemma 6, p. 5](https://arxiv.org/pdf/math/0701577v6#page=5)

**The signed integral.** For large $p$ the arcs are disjoint since $2Q^2<M$. The two half-arcs at $0$ and $1$ form one arc. Their union with the other arcs has measure at most $2TQ/M$. Using $|S|\le M\log n$, the integrated product-replacement error divided by $M$ is $O_A(TQ/\log^{A-1} n)=o(\min(T,1))$, with $A$ sufficiently large. Squaring the model cancels $e(2m\beta)$ against $e(-n\beta)$. Summing $e(-na/q)$ over the reduced centers gives $c_q(n)$. Only squarefree $q$ survive. For $q\le Q<p$, an odd prime factor contributes $-1$ and the factor at 2 contributes $+1$. Writing $q=d$ or $2d$ with $d$ odd gives the two terms and the common coefficient $\mu(d)/\varphi(d)^2$ in $P(T)$.

For the kernel, put $u=M\beta$. Then $|D_H(u/M)|^2/M^2$ equals $(\sin(\pi u)/(\pi u))^2$ times $(\pi u/M\,/\,\sin(\pi u/M))^2$. Across $|u|\le Q$ the second factor is $1+O((Q/M)^2)$. Hence the normalized integral on one centered arc is $F(T/q)(1+O((Q/M)^2))$. Parseval for the Fourier transform of the unit interval gives $F(\infty)=1$, and $0\le F(z)\le\min(2z,1)$. The absolute sum of denominator weights is finite since $\prod_{r>2}(1+(r-1)^{-2})$ converges. In extending the finite sum to $P(T)$, each neglected $q>Q$ contributes at most $2\min(T,1)$ times its absolute weight. The tail and the kernel error are therefore $o(\min(T,1))$ uniformly.

**Constants and sign.** As $T\to0$, $F(z)=2z+O(z^3)$ gives $P(T)=\kappa T+O(T^3)$ by the Euler product for odd squarefree $d$. As $T\to\infty$, dominated convergence gives $P(T)\to2C_2$. For intermediate widths the profile is positive as well. Let $P_+=\prod_{r>2}(1+(r-1)^{-2})\le\exp(\pi^2/24)<2$. Since $F$ is increasing, the absolute sum of terms with $d>1$ is at most $(P_+-1)[F(T)+F(T/2)]$. Consequently $P(T)\ge(2-P_+)[F(T)+F(T/2)]>0$ for $T>0$.

**Direct check on the shrinking scale.** On the original arcs $|\beta|\le Q/(qn)$, every $|j\beta|\le T_0/(2q)$. Pairing the terms at $j$ and $-j$ gives $D_H(\beta)=M[1+O(T_0^2/q^2)]$ directly from $1-\cos v\le v^2/2$. The model integral on each arc is therefore its length times $M^2[1+O(T_0^2/q^2)]$. After summing centers and dividing by $B=M^2Q/n$, its coefficient is $2\sum_{q\le Q}\mu(q)^2c_q(n)/(q\varphi(q)^2)+O(T_0^2)$, tending to $\kappa$. On the same scale the error from the prime sum is $O_A(Q/\log^{A-1}n)=o(1)$, by the total length $2Q^2/n$. This calculation uses fixed $A$ and works directly at $T_0$.

**Arithmetic check.** Using rational arithmetic, the 167 odd primes up to $Y=1000$ give $2.699153<\kappa<2.699155$. To reproduce the enclosure, multiply their rational Euler factors and then multiply by 3 for the upper bound. For the lower bound multiply that result by $1-Y^{-3}-(2Y^2)^{-1}$, using $\sum_{r>Y}1/[r(r-1)^2]\le\sum_{k\ge Y} k^{-3}$. As a separate sign check, at $p=1009$ the polynomial $\sum_{(a,q)=1}X^{(-2p^2a\bmod q)}$ over one reduced residue system was reduced modulo the cyclotomic polynomial for each of the 61 squarefree $q\le100$. All remainders were the predicted $\mu(d)$ with $d$ the odd part of $q$. These finite checks concern constants and normalizations. The pointwise asymptotic uses the analytic lemma above.
