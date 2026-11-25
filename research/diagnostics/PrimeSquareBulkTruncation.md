# Removing small primes from the signed minor-arc integral at a prime square

Let $n=2p^2$ with $p$ prime, $Q=\lfloor\log_2(n+2)\rfloor^2$, and $e(t)=\exp(2\pi it)$. Use the task desk's major arcs $\mathfrak M$ and minor arcs $\mathfrak m$ on the unit circle. Put $S_X(t)=\sum_{\ell\le X,\ \ell\ {\rm prime}}(\log\ell)e(\ell t)$ and $I(F)=\int_{\mathfrak m} F(t)^2e(-nt)\,dt$. For every fixed $A>0$ and every integer $0\le L\le n/2$, I obtain
$$
 |I(S_n)-I(S_n-S_L)|\ll_A L+n/(\log n)^A .
$$
In particular, for any $L=L(n)=o(n)$ the original signed minor-arc lower bound and the high–high version are equivalent **on this family** at the $o(n)$ scale. The catalogue uses $L=\lfloor n^{1/3}\rfloor$ and asks for every sufficiently large even integer. The estimate below compares the two integrals and leaves their common lower bound open.

**The catalogue cutoff for general targets.** For every even $n$ and $L=\lfloor n^{1/3}\rfloor$ the same comparison already follows from elementary estimates. The whole-circle difference is at most $2L\log^2 n$ by orthogonality. On the major arcs, of measure at most $2Q^2/n$, the integrand difference is at most $3nL\log^2 n$, using $|S_X|\le X\log n$. This gives $O(n^{1/3}\log^6 n)=o(n)$ uniformly in even $n$. Thus the two catalogue lower bounds quantified over every fixed $\varepsilon>0$ imply each other, by applying either with $\varepsilon/2$. The prime-square estimate below extends the comparison to all cutoffs $L=o(n)$ on that family.

**Whole circle.** Fourier orthogonality identifies the difference with the sum of the nonnegative weights of ordered prime representations in which at least one prime is at most $L$. For $L<\sqrt n$ the trivial bound $2\sqrt n\log^2 n$ suffices. Otherwise sieve $k,n-k$ for $1\le k\le L$ through $v=L^{1/4}$. Since $v<p$, there is one prohibited residue at 2 and two at each odd sieve prime. The dimension-two Selberg upper sieve gives $O(L/\log^2 L)$ survivors uniformly in $p,L$. In equation (3.8) the interval remainder is $O(2^{\omega(d)})$ per squarefree modulus, hence its total is $O(v^2\log^5v)$. Add at most $v$ prime endpoints at or below the sieve level. Since $\log L\ge(\log n)/2$, the weighted difference is $O(L)$. This gives $O_A(L+n/\log^A n)$ uniformly in both ranges. [Heath-Brown, §3, (3.8)](https://arxiv.org/pdf/math/0209360#page=22)

**Major arcs.** At each reduced center $a/q$, with $|\beta|\le Q/(qn)$, write $D_X(\beta)=\sum_{1\le j\le X}e(j\beta)$. For any fixed $B>0$, uniformly for $X\le n$,
$$
 S_X(a/q+\beta)=\frac{\mu(q)}{\varphi(q)}D_X(\beta)+O_B(n/\log^B n).
$$
Indeed, for partial sums at $x\ge\sqrt n$ apply Siegel–Walfisz in reduced residue classes, choosing the exponent freely since $q\le Q\ll\log^2 n$; for smaller $x$ use $O(\sqrt n\log n)$ per class. Partial summation against $e(t\beta)$ costs $1+O(n|\beta|)$, and summing the classes costs at most $q$. The exceptional primes dividing $q$ contribute at most $\log q$. Replacing the continuous model integral by $D_X$ costs $O(1+X|\beta|)$ by summation on unit intervals. These polylogarithmic losses are absorbed in the choice of exponent. The major arcs have total length at most $2Q^2/n$. The trivial bound $|S_X|\le n\log n$ thus makes the integrated product-replacement error $O_A(n/\log^A n)$ by taking $B>A+6$. [Koukoulopoulos, chapter 12](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=126)

For large $n$ the reduced arcs are disjoint, and the two halves at denominator one join by periodicity. In the model for $2S_nS_L-S_L^2$, summing the phase $e(-na/q)$ gives $c_q(n)$ before taking absolute values. For squarefree $q\le Q<p$, $|c_q(2p^2)|=1$ by multiplicativity: the factor at 2 is 1, and every odd prime factor contributes $-1$. Hence the sum of the absolute denominator weights is bounded independently of $n$ by $\prod_{\ell\ {\rm prime}}(1+1/(\ell-1)^2)<\infty$.

For $X=n$ or $L$, each remaining signed kernel integral satisfies
$$
 \left|\int_{-\delta}^{\delta}D_X(\beta)D_L(\beta)e(-n\beta)\,d\beta\right|\ll L,
 \qquad \delta=Q/(qn).
$$
To see this, fix a frequency $1\le k\le L$ of $D_L$. Integrating the other factor gives a sum over consecutive integer frequencies $d=j+k-n$. The zero frequency contributes at most $2\delta$. For $d\ne0$ the summand is $\sin(2\pi d\delta)/(\pi d)$. Its sum over any consecutive range is bounded uniformly: split at $|d|=1/\delta$, use $|\sin x|\le |x|$ below this point, and partial summation with the geometric-series bound $O(1/\delta)$ above it. This proves the kernel bound after summation over $k$. The major-arc difference is therefore $O_A(L+n/\log^A n)$. Subtracting it from the whole-circle difference proves the claim.

The arithmetic gain is specific: the reduced-center phases give a summable denominator weight for $2p^2$. Taking their absolute values separately would lose this cancellation. This is a paper derivation using the cited analytic inputs.
