# Reflected prime residuals and the exterior of the central-window arcs

Let $p$ tend to infinity through odd primes. Put $m=p^2,\ n=2m,\ H=\lfloor p^{4/3}\rfloor,\ M=2H+1$ and $W=\{m-H,\ldots,m+H\}$. Use ordered pairs and the weight $a_x=\log x$ on primes in $W$, zero elsewhere in $W$. Reflection sends $x$ to $n-x$, and $Rf(x)=f(n-x)$. Write $\langle f,g\rangle=\sum_{x\in W} f(x)g(x)$, $T=\langle a,Ra\rangle$. Thus $T>0$ precisely when the window contains a pair of primes with sum $n$.

## A signed increment for each new odd prime

For $q\ge1$ let $h_b$ count window integers congruent to $b\bmod q$, and put $A_b=\sum_{x\equiv b} a_x$ within the window. Let $P_q a$ be the function equal to $A_b/h_b$ on each nonempty class. Reflection pairs classes of equal size. Put
$$
 C_q=\langle P_qa,RP_qa\rangle
     =\sum_{b:\,h_b>0}\frac{A_b A_{n-b}}{h_b},
 \qquad D_q=\langle a-P_qa,R(a-P_qa)\rangle .
$$
The residual sums to zero on each class. Both mixed terms therefore vanish, giving the exact identity $T=C_q+D_q$. If $q\mid q'$, apply the same argument to $P_{q'}a$ and the partition modulo $q$. Its coarse projection is $P_q a$, so for $u=P_{q'}a-P_q a$,
$$
 \langle u,Ru\rangle=C_{q'}-C_q=D_q-D_{q'}.
$$
The sign of this quantity depends on the arithmetic weights.

Fix $A,B>0$. Uniformly for even squarefree $q\le(\log n)^A$, put
$$
 S_q=2\prod_{2<\ell\mid q}\left(1-\frac1{(\ell-1)^2}\right).
$$
Here and below products indexed by $\ell$ are over primes. Then $C_q/M=S_q+O_{A,B}((\log n)^{-B})$. Indeed, Lemma 6 of Baier and Zhao, with left endpoint $m-H-1$ and length $M\asymp m^{2/3}$, gives $A_b=M/\varphi(q)+O_K(M/\log^K n)$ on every reduced class, for arbitrary fixed $K$ (enlarge the modulus exponent by one to switch between $\log n$ and the lemma's logarithm). The total possible prime-power correction is $O(\sqrt n\log^2 n)$. On nonreduced classes $A_b=0$ since every window prime exceeds $q$. Also $h_b=M/q+O(1)$. Inserting these estimates incurs an error after division by $M$ of $O(q^2/\log^K n+q^3/M)$, enough on taking $K>B+2A+1$. The main coefficient is $q\,\#\{b:(b,q)=(n-b,q)=1\}/\varphi(q)^2$. Modulo 2 one residue survives. Modulo each odd $\ell\mid q$ the two excluded residues $0,n$ differ because $p>q$ eventually. The Chinese remainder theorem now gives $S_q$. [Baier–Zhao, *On primes in quadratic progressions*, Lemma 6](https://arxiv.org/pdf/math/0701577v6#page=5)

Consequently, if $\ell\nmid q$ is odd and $q\ell\le(\log n)^A$, then
$$
 D_{q\ell}-D_q
 = \frac{M S_q}{(\ell-1)^2}
   + O_{A,B}\!\left(\frac M{(\log n)^B}\right)>0
$$
uniformly for all sufficiently large $p$. Take $B>2A$ and use $S_q\ge2C_2>0$, where $C_2=\prod_{\ell>2}(1-1/(\ell-1)^2)$. Thus the new component $u$ has strictly negative reflected correlation even though the residual left behind increases. This proves the sign at each permitted refinement without making a prime-pair assumption.

## Comparison with the arc exterior

Let $Q=\lfloor\log_2(n+2)\rfloor^2$. On the circle let $\mathfrak M(Q)$ be the union of the arcs of radius $Q/(dM)$ at all reduced fractions of denominator $d\le Q$, counting the center zero once. Write $S(t)=\sum_{x\in W}a_x e^{2\pi ixt}$, $f(t)=\operatorname{Re}(S(t)^2e^{-2\pi int})$, $J(Q)=\int_{\mathfrak M(Q)}f$, and $E_{\rm ext}=\int_{\mathfrak M(Q)^c}f$. Fourier orthogonality gives $E_{\rm ext}-D_q=C_q-J(Q)$ exactly.

Here the width matters. The enlarged arcs give the quantitative estimate
$$
 J(Q)/M=2C_2+O(\log(2Q)/Q).
$$
For details, the short-progression and partial-summation argument in the linked calculation approximates each prime sum by its Dirichlet-kernel model with error $O_K(M/\log^K n)$ for any fixed $K$. After integration and division by $M$, the error is $O_K(Q^2/\log^{K-1} n)$. The normalized kernel on an arc of denominator $d$ has integral $F(Q/d)(1+O(Q^2/M^2))$, with $F(v)=\int_{-v}^v(\sin(\pi u)/(\pi u))^2du$ and $0\le1-F(v)\ll 1/v$. The coefficients at denominators $d$ and $2d$, for odd squarefree $d$, are both $\mu(d)/\varphi(d)^2$. Their full sum is $2C_2$. Removing $d>Q/2$ costs $O(1/Q)$ in absolute value, allowing also for the singly included terms. Replacing the remaining kernels by 1 costs $O(Q^{-1}\sum_{d\le Q}d/\varphi(d)^2)=O(\log(2Q)/Q)$. For both bounds use $\sum_{d\le v}(d/\varphi(d))^2\ll v$ and partial summation. Indeed $(d/\varphi(d))^2=\sum_{k\mid d}g(k)$ for multiplicative $g$ supported on squarefree integers with $g(\ell)=(1-1/\ell)^{-2}-1$. The product for $\sum_k g(k)/k$ converges. [Central-window arc calculation](CentralWindowArcScale.md)

Now fix $c>0$, put $z=c\log\log n$ and $q=\prod_{\ell\le z}\ell$. The prime number theorem gives $\log q\sim z$, so $q\le(\log n)^{c+1}$ eventually. Partial summation using $\pi(v)\sim v/\log v$ yields $\sum_{\ell>z}(\ell-1)^{-2}\sim1/(z\log z)$. Taking logarithms of the tail product shows $S_q=2C_2(1+(1+o(1))/(z\log z))$. The preceding arc error is smaller than $1/(z\log z)$. Thus, for each sufficiently large prime along this family,
$$
 E_{\rm ext}=D_q+(2C_2+o(1))\,\frac M{z\log z}.
$$
The offset is positive. Its scale compares two ways of measuring the same missing pair correlation.

## What the refinement leaves open

For this primorial, $\|a-P_q a\|_2^2=(1+o(1))M\log m$. Indeed $\sum a_x^2=(\log m+o(1))\sum a_x\sim M\log m$. Applying the same class estimates without reflection gives $\|P_q a\|_2^2=Mq/\varphi(q)+O_B(M/\log^B n)$, while $q/\varphi(q)\le\prod_{j=2}^{\lfloor z\rfloor} j/(j-1)\le z$. Cauchy–Schwarz alone therefore leaves a lower bound of order $-M\log m$. Nonnegativity of the pair count already gives $D_q\ge-C_q$. With no central pair one has $D_q=-C_q$ **for every $q$**, consistent with every positive increment above. Even telescoping all such increments cannot test this hypothesis. A uniform bound $D_q\ge-C_q+\eta M$ for some fixed $\eta>0$ would give $T\ge\eta M$; a strict inequality $D_q>-C_q$ already suffices for existence. Both require information about simultaneous primality inside the classes.

The arithmetic sifted-set inequality supplies a stronger absolute bound. Let $Z=\lfloor M^{1/3}\rfloor$. For every large $p$, $Z<p$ and both members of every central prime pair exceed $Z$. Their first coordinates avoid $0,n\bmod\ell$ for all primes $\ell\le Z$. There is one prohibited class at 2 and two at every odd $\ell\le Z$. Write these numbers as $\omega(\ell)$. Montgomery–Vaughan's Corollary 1 bounds the number of first coordinates by
$$
 \frac{M+O(Z^2)}{G(Z)},\qquad
 G(Z)=\sum_{d\le Z}\mu(d)^2\prod_{\ell\mid d}\frac{\omega(\ell)}{\ell-\omega(\ell)}.
$$
For an explicit lower bound on the denominator, take $y=Z^{1/10}$, expand the product of $1+\omega(\ell)/(\ell-\omega(\ell))$ over $\ell\le y$, and normalize its weights to a probability distribution on squarefree $d$. Under this distribution each prime is selected independently with probability $\omega(\ell)/\ell$. Thus $\mathbb E\log d=\sum_{\ell\le y}\omega(\ell)\log\ell/\ell=(2+o(1))\log y$ by the prime number theorem and partial summation. Markov's inequality leaves at least half the mass at $d\le Z$ eventually. The full product is $\gg(\log y)^2$ by Mertens' product formula, or by comparison with $\prod_{\ell\le y}(1-1/\ell)^{-2}$ since the ratio converges to a positive constant. Consequently $G(Z)\gg(\log M)^2$, and multiplying the count by at most $(\log n)^2$ gives $0\le T\ll M$. In particular $|D_q|\ll M$ uniformly over the polylogarithmic moduli above, and $|E_{\rm ext}|\ll M$. This classical upper sieve controls the scale of the uncertainty. It allows $T=0$ and therefore gives no strict improvement on $D_q\ge-C_q$. [Montgomery–Vaughan, *The large sieve*, Corollary 1](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=2)

As a finite check of the identities, take every binary weight vector of lengths 1 through 8, place it at each of the two integer origins 0 and 7, and use $q=1,2,3,5$ with refinement $q'=2q$. Form the means as rational numbers and reverse the vector for reflection. All 8,160 decompositions and 4,080 nested identities agree exactly, including partitions with empty classes. These tests use arbitrary weights and concern only the finite identities.

## A sharp finite obstruction for exact residue counts

Write $k_b$ for the number of selected sites in class $b\bmod L$, for any integer $L\ge1$. Keep these counts fixed while varying the binary support $A\subseteq W$. The exact minimum of the **ordered** overlap is
$$
 \min_A |A\cap R(A)|=\sum_{b\bmod L}\max\{0,k_b+k_{n-b}-h_b\}.
$$
For two distinct partner classes, pull both supports back to the same $h_b$ positions by reflection. Sets of sizes $k_b,k_{n-b}$ can have intersection as small as their excess over $h_b$, truncated at zero. Each intersection point contributes once from each class. In a self-reflected class of size $h$ there are $\lfloor h/2\rfloor$ transpositions and $h\bmod 2$ fixed sites, since the entire interval has just one fixed site. Select one endpoint from each transposition first, then the fixed site if present, and finally the other endpoints. At occupancy $k$ this gives $\max(0,2k-h)$ reflected hits, which is also the inclusion-exclusion lower bound. The choices on different class orbits are independent.

Now take the **actual** prime counts in this formula, and let $L=\operatorname{lcm}(1,\ldots,\lfloor c\log\log n\rfloor)$ with fixed $c>0$. The prime number theorem gives $\log L\sim c\log\log n$. Lemma 6 applies to this modulus, including its prime-power factors. Uniformly on nonempty classes, the prime occupancy is $o(h_b)$: on reduced classes it is at most $A_b/\log(m-H)$, with $h_b\sim M/L$; on all others it vanishes. In the resulting bound use $L/\varphi(L)\le\prod_{j=2}^{\lfloor c\log\log n\rfloor} j/(j-1)\ll_c\log\log n$, and take a fixed saving larger than $c+2$ in Lemma 6. Thus **there exists a pair-free binary support with precisely the actual prime counts in every class for every modulus $d\le c\log\log n$, simultaneously**. Indeed, all those classes are unions of classes modulo $L$. One can even move the list of positive weights by a permutation within each class, if arbitrary weights are allowed. Such weights need not equal the logarithms of their new sites. The obstruction concerns arguments using these marginals alone. The earlier [rough-composite model](CompositeReflectionModel.md) instead kept the logarithm attached to each site and approximated local masses on subintervals.

An exhaustive rational/integer check grouped every binary support of lengths 1 through 11 by its exact class counts, for origins 0 and 7 and each modulus from 1 through 8. Direct minimization over the 65,504 configurations agreed with the formula for all 15,812 count profiles (counted separately for each interval and modulus).
