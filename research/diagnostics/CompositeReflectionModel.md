# A central-window model supported entirely on rough composites

Fix a sufficiently large odd prime $p$, put $m=p^2$, $n=2m$, $H=\lfloor m^{2/3}\rfloor$, $M=2H+1$, and $W=[m-H,m+H]\cap\mathbb Z$. Write $z=\exp(\sqrt{\log m})$. Call an integer rough if all its prime factors exceed $z$.

There exists a set $E=E_p$ of rough **composites** in $W$ with $E\cap(2m-E)=\varnothing$. Give every selected site $j$ its ordinary weight $\log j$. For every fixed $A,D>0$, uniformly over integer subintervals $I\subseteq W$ and reduced classes $a\bmod q$ with $q\le(\log m)^D$,
$$
 \sum_{\substack{j\in E\cap I\\j\equiv a\bmod q}}\log j
   =\frac{|I|}{\varphi(q)}+O_{A,D}\big(M/(\log m)^A\big).
 \tag{1}
$$
Here $|I|$ counts integers. The error is absolute on the window scale. Real primes satisfy (1) as well. The same sequence of sets works for all fixed exponents. This construction tests what can follow from these one-point distribution estimates, weights and small-prime exclusions.

## The available composite sites

Let $V=\prod_{r\le z}(1-1/r)$, over primes, and $\rho=V-1/\log m$. Mertens' product estimate gives $V^{-1}\asymp\log z=\sqrt{\log m}$, so $\rho\sim V$. Uniformly in the intervals and classes of (1), the number of rough integers is
$$
 \frac{|I|V}{\varphi(q)}+O_{A,D}(M/(\log m)^A).
$$
Indeed, eventually every prime factor of $q$ is at most $z$. Remove the sieve primes dividing $q$, which already miss the specified reduced class. For each product $d$ of the remaining distinct sieve primes, the Chinese remainder theorem counts multiples of $d$ in that class with error at most one from $|I|/(qd)$. Use the even and odd Bonferroni truncations at consecutive orders $k$ and $k+1$ with $k=\lfloor(\log\log m)^2\rfloor$. The sum of counting errors up to degree $k+1$ is bounded by $(k+2)z^{k+1}=m^{o(1)}$. For the main term these same truncations bracket $\prod_{r\le z,\ r\nmid q}(1-1/r)=Vq/\varphi(q)$. Their gap in density is at most $\lambda^b/b!$ with $b=k+1$, where $\lambda=\sum_{r\le z}1/r=O(\log\log m)$. This bound decays faster than every negative power of $\log m$ by $b!\ge(b/e)^b$. [Mertens' estimates and proof](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/)

Every prime in $W$ exceeds $z$. Its unweighted class count in $I$ is $|I|/(\varphi(q)\log m)+O_{A,D}(M/(\log m)^A)$. For $|I|\ge M/(\log m)^K$ apply Baier and Zhao's short-interval Siegel–Walfisz lemma, since this length eventually exceeds $(m+H)^{7/12+1/24}$. Removing proper prime powers costs $O(\sqrt m\log^2 m)$ in logarithmic weight. Replacing $\log j$ by $\log m$ costs $O(MH/m)$ in that weight over the window. Shorter intervals follow from $|I|\log(2m)$ by taking $K$ sufficiently large. Thus after subtracting primes and dropping the midpoint, the count of available composites in each class is $|I|\rho/\varphi(q)+O_{A,D}(M/(\log m)^A)$. [Baier–Zhao, *On Primes in Quadratic Progressions*, v6, Lemma 6](https://arxiv.org/pdf/math/0701577v6#page=5)

## Choosing one endpoint at most

For each available site set $\alpha_j=1/(\rho\log j)$, and set $\alpha_j=0$ elsewhere. For each positive offset $h\le H$, select $m-h$ with probability $\alpha_{m-h}$, select $m+h$ with probability $\alpha_{m+h}$, and select neither with the remaining probability. For all large $m$ the two probabilities sum to $O(1/\sqrt{\log m})<1$. Make distinct orbit choices independently. Every outcome has the required support and no reflected pair.

A selected site's expected logarithmic weight is exactly $1/\rho$ at every available site. Dividing the composite count by $\rho$ costs only $O(\sqrt{\log m})$, which is absorbed by taking a larger initial exponent. For a given interval and residue class the weighted sum is a sum of $H$ independent variables, one per orbit, each in $[0,\log(2m)]$. Hoeffding's inequality bounds its deviation from its mean by $C\sqrt M(\log m)^{3/2}$ outside an event of probability $O(m^{-10})$ for an absolute $C$ large enough. There are $O(M^2z^2)$ interval/class tests with $q\le z$. The union of the exceptional events has probability less than one. Fix any outcome good for this whole finite family. The concentration bound is $o(M/\log^A m)$ for every fixed $A$ and the family contains every $q\le(\log m)^D$ eventually. This proves (1). Multiplying the weights by $(\log j)^{s-1}$ and summing by parts also transfers every fixed positive integral power $s$ of the site weight to the same absolute logarithmic precision when compared with the true primes. [Hoeffding, Theorem 2](https://doi.org/10.1080/01621459.1963.10500830)

## Consequence at the original arc widths

Take $Q=\lfloor\log_2(n+2)\rfloor^2$ and the project radii $Q/(qn)$ for $q\le Q$. Write $S_E(t)=\sum_{j\in E}\log j\,e(jt)$ with $e(t)=\exp(2\pi it)$. Summing (1) over reduced residue classes and applying partial summation on $W$ gives the same major-arc approximation as for the actual prime sum, to pointwise error $O_A(M/\log^A m)$. Nonreduced classes contain no selected sites for these moduli. The losses are at most $q$ from classes and $1+O(M|\beta|)$ from a twist by $\beta$ around a reduced center.

With $B=M^2Q/n$, the signed major integral for this model is $(\kappa+o(1))B$, where $\kappa=3\prod_{r>2}(1-1/[r(r-1)^2])$ over odd primes. In the linked computation the integrated error divided by $B$ is $O_A(Q/\log^{A-1}m)$. Orthogonality and the excluded pairs give $\int_0^1 S_E(t)^2 e(-nt)\,dt=0$ **exactly**. Its minor integral therefore has real part $-(\kappa+o(1))B$. In particular a fixed improvement $\eta B$ for actual primes would use information beyond (1), roughness and the prescribed individual weights. The example is separately constructed for each $p$. It makes no assertion about the actual prime support or a single set working at all centers. [Major-arc calculation at a fixed revision](https://github.com/LonelyQuantum/goldbach-proofs/blob/fbf200ddd9444ad0eabc77ffa322ac687066d78b/research/diagnostics/CentralWindowArcScale.md)
