# Positive and negative mass on rational arcs for a central Goldbach window

For an odd prime $p$, put $m=p^2$, $n=2m$, $H=\lfloor p^{4/3}\rfloor$, $M=2H+1$, $Q=\lfloor\log_2(n+2)\rfloor^2$ and $e(t)=\exp(2\pi i t)$. Use the logarithmically weighted prime sum $S(t)=\sum_{|\ell-m|\le H,\ \ell\ {\rm prime}}\log(\ell)e(\ell t)$. Write $f(t)=\operatorname{Re}(S(t)^2e(-nt))$ and $f_\pm=\max(\pm f,0)$. Let $\mathcal B$ consist of the bands $Q/(qn)<|t-a/q|\le Q/(qM)$ about all reduced centers modulo one with $q\le Q$. Distances are on the circle. The bands are disjoint for large $p$ and lie in the original desk minor arcs, up to endpoints.

For each of the two signs and every sufficiently large prime $p$,
$$
\int_{\mathcal B} f_\pm(t)\,dt=M\left(\frac{\log Q}{\pi}+O(1)\right).
$$
Here $\log Q$ is natural. On the same bands the signed integral is $(2C_2+o(1))M$, where $C_2$ is the twin-prime constant, by the [central-window arc calculation](CentralWindowArcScale.md). In particular, the individual negative mass on even this subset of the minor arcs exceeds any fixed multiple of $M$ for large enough $p$. A lower bound for the signed integral can still use cancellation. The sum $S$ here has central-window support.

**Replacing the prime sum.** On an outer arc at $a/q+\beta$ the short-progression estimate gives
$$
 S(a/q+\beta)=\frac{\mu(q)}{\varphi(q)}e(m\beta)D_H(\beta)+O_A(M/\log^A n),\qquad
 D_H(\beta)=\sum_{|j|\le H}e(j\beta)\in\mathbb R .
$$
The preceding note derives this uniformly, using prefixes of length at least $M/\log^K n$ in Baier and Zhao's Lemma 6 and trivial estimates for shorter prefixes. Symmetry and $n=2m$ leave the real model $\mu(q)^2D_H(\beta)^2\cos(2\pi na/q)/\varphi(q)^2$. Squaring costs $O_A(M^2/\log^A n)$ and taking either positive part is 1-Lipschitz. The total length of the outer arcs is $O(Q^2/M)$, so the integrated error is $o(M)$. [Baier and Zhao, Lemma 6](https://arxiv.org/pdf/math/0701577v6#page=5)

**Numerator average.** Write $g_\pm(x)=\max(\pm\cos(2\pi x),0)$. Each function has one-period integral $1/\pi$ and bounded variation. Uniformly in squarefree $q\le Q<p$,
$$
 \sum_{a\bmod q}^{*} g_\pm(na/q)=\frac{\varphi(q)}{\pi}+O(\tau(q)).
$$
For odd $q$, multiplication by $n$ permutes the units. When $q=2d$ with $d$ odd, reduction of the units to $d$ is bijective, and $na/q=p^2a/d$. For either reduced modulus, Möbius inversion over the units uses complete grids on which the sum of $g_\pm$ differs from the grid size times its mean by at most its variation. Summing the numerator errors with weights $\mu(q)^2/\varphi(q)^2$ costs $O(1)$, by the convergent Euler product with local factors $1+2/(\ell-1)^2$.

**Arc integration and the coefficient.** Let $T_0=MQ/n=o(1)$ and $F(z)=\int_{-z}^z(\sin(\pi u)/(\pi u))^2\,du$. Upon dividing by $M$, the squared Dirichlet kernel integrates on a band to $F(Q/q)-F(T_0/q)$ times $1+O(Q^2/M^2)$, by the change of variable $u=M\beta$. The normalization also follows from orthogonality, $\int_0^1|D_H(\beta)|^2\,d\beta=M$, since only the $M$ identical-frequency pairs survive. The phase $e(2m\beta)e(-n\beta)$ is identically one. We have $1-F(Q/q)\ll q/Q$ and $F(T_0/q)\ll T_0/q$.

Set $w(q)=\mu(q)^2/\varphi(q)$. Then $\sum_{q\le Q}w(q)=\log Q+O(1)$. To see the coefficient, write $w$ as the Dirichlet convolution of $q\mapsto 1/q$ with a multiplicative function $b$. At a prime $\ell$ the local generating polynomial of $b$ is $1+t/(\ell(\ell-1))-t^2/(\ell(\ell-1))$. Thus $\sum b(d)=1$ and $\sum |b(d)|\log(2d)<\infty$. Convolution with the harmonic sum proves the estimate, including its bounded error. Partial summation gives $\sum_{q\le Q}q w(q)\ll Q$, and $\sum w(q)/q$ converges. The outer kernel tail and the inner cutoff therefore change the normalized main term by $O(1)$. This gives the displayed formula for both signs.

As a finite arithmetic check at $p=1009$, the convolution coefficients were compared exactly for all $1\le q\le400$. For the 243 squarefree denominators in that range, the reduced phase residues were enumerated and agreed as multisets with the units modulo $q/\gcd(q,2)$. The asymptotic formula uses the analytic argument above.
