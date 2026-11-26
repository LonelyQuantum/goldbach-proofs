# Three prime divisors of the reflected endpoint at one Goldbach target

Use $N=2s$, $L=\log s$, $h\asymp s^{2/3}$, $z=\exp(L/(\log L)^3)$, $w=(2s)^{1/3}$, $R,Z,F_0,D_0,J$ and the unswitched expansion of [the fixed-target semiprime estimate](HybridSemiprimeFrontier.md). In particular $F_0=s^{1/6+o(1)}$. Write $b=rt$ for an ordered pair of distinct primes in the lower window $[s-H,s-2T)$, and $a=N-b$. Keep $(rt,N)=1$, $a$ squarefree and coprime to $P_z=\prod_{p\le z}p$.

First restrict $s^{17/50}<r\le s^{7/20}$; this fixes the smaller prime and leaves room below $dr=Z$ throughout the three-factor range below. Write $\sum_b^*$ for summation over these pairs with weight $\log r$, and put $U_s=\sum_b^*1$. All estimates hold for each sufficiently large integer $s$. Define
$$
 u=1/16,\quad v=3/40,\qquad
 \mathcal P=\{\ell\text{ prime}:s^u<\ell\le s^v,\ \ell\nmid N\},\qquad
 c_\ell=1/(\ell-1),\quad X_\ell(a)=1_{\ell\mid a}.
$$
For squarefree $k$ supported on this band put $c_k=1/\varphi(k)$. The count of actual band primes dividing $a$ is $Q(a)=\sum_{\ell\in\mathcal P}X_\ell(a)$.

## One and two prescribed divisors

Let $\mathcal K$ consist of the primes in this band or of the products of two distinct primes from it. For any coefficients $|\gamma_k|\le1$,
$$
 \sum_b^*\sum_{k\in\mathcal K}\gamma_k(1_{k\mid a}-c_k)
       =O_A(hL^{-A}) \qquad (A>0).
 \tag{1}
$$
In particular this holds uniformly for a subset of pairs chosen at the given center. The reference uses the actual mass $U_s$ on the rough reflected endpoints.

To prove (1), apply the arithmetic smoothing, squarefree removal and order-$J$ wheel from the preceding note to both terms, before character projection. Their total cost is $O_A(hL^{-A})$. In the arithmetic term the inner sum is bounded by a fixed divisor power since $k\mid a$; in the reference $\sum_{k\in\mathcal K}c_k=O(1)$ by the prime reciprocal sum on the band. Each modulus $kj$ determines $k$ and the small-prime part $j$. In the characters modulo $kj$, the part principal on $k$ gives exactly $c_k1_{j\mid a}$ after summing the characters on $j$. The identity holds since $N,rt$ are units modulo $kj$ (the primes in $k,j$ are smaller than both $r,t$). This cancels the wheel expansion in the reference.

Every remaining primitive conductor $f$ contains a prime $>s^u$ and satisfies $f\le s^{2v}z^J=s^{3/20+o(1)}$. Thus it lies strictly inside the range of [hybrid estimate (4)](HybridSemiprimeFrontier.md#joint-average-over-the-two-primes). Its proof only needs a bounded coefficient for each uniquely represented modulus and uses absolute values on lifting to primitive characters. It applies to $\gamma_k\mu(j)$ as well. The single $\log r$ is allowed in the prime polynomial. This proves (1). The same proof works with $wL^{K}\le r\le Z/R$, $t>w$ and $rt$ in the window, for $K$ chosen as in that estimate; $t\gg s^{10/21}$ there. Either prime weight may impose a further independent interval restriction. The ordinary multiplicative large sieve is the analytic input to the hybrid bound. [Kowalski–Vaughan, Lemma 2.1](https://personal.science.psu.edu/rcv4/personal/Publications/s00208-024-03069-3-1.pdf#page=4)

## The surviving three-prime correlation and its sign

Let $\mathcal D$ contain the products of three distinct primes from $\mathcal P$, counted once. Then $s^{3/16}<d\le s^{9/40}$, strictly above the earlier $s^{1/6}$ scale. For the chosen $r$-band, $dr\le s^{23/40}< Z$ eventually. On these moduli, take the contribution $H_3(s)$ from conductors $f>F_0$ in the previously specified smoothed character expansion, with unit prime weights and the original factor $\log d$. The high-conductor projection has a particularly simple arithmetic expression:
$$
 H_3(s)=\sum_b^*\sum_{d\in\mathcal D}\log d\prod_{\ell\mid d}(c_\ell-X_\ell(a))
                  +O_A(hL^{-A}).
 \tag{2}
$$
Indeed every conductor using at most two of the three band primes is $\le s^{2v}z^J<F_0$, while any using all three exceeds $s^{3u}>F_0$. For squarefree $dj$ all characters on $j$ are therefore summed without restriction and each prime of $d$ must carry a nonprincipal character. At $\ell$ this character sum is $(\ell-1)X_\ell(a)-1$. Multiplying by $\mu(dj)/\varphi(dj)$ gives precisely $\mu(j)1_{j\mid a}\prod_{\ell\mid d}(c_\ell-X_\ell(a))$. Sum over $j$ to restore roughness. Replacing the truncated wheel, restoring squarefreeness and undoing smoothing here is valid: after summing the absolute products over $d$ the weight is $\ll L(\sum_{\ell\in\mathcal P}(c_\ell+X_\ell))^3\ll L$, since $Q(a)\le16$. This verification uses the factorization specific to this projection.

Define $V_i=\sum_{d}\log d\,c_d$ over products of $i$ distinct band primes, for $i=2,3$. Applying (1) to the linear and quadratic terms of (2) gives
$$
 H_3(s)= U_s V_3-\sum_b^*\sum_{\substack{d\in\mathcal D\\d\mid a}}\log d
               +O_A(hL^{-A}).
 \tag{3}
$$
For example the coefficient of any specified pair in the quadratic part is $\sum_{\ell}\log(k\ell)c_\ell\ll L$; the linear coefficients are also $O(L)$. Normalize before using (1) and increase $A$. In the independent reference the constant, linear and quadratic terms have multiplicities $1,-3,+3$, leaving one copy of $V_3$. The sign is important: excess simultaneous divisibility contributes negatively. Restricting the raw divisor sum alone to these triples would retain only the negative count in (3).

There is an explicit one-sided target. For $Q(a)\ge2$ each actual pair $\ell_1,\ell_2\mid a$ has $Q(a)-2$ possible third primes. Weight it by $\log(\ell_1\ell_2)$. Let $M_s$ be the mean of $Q(a)-2$ under those pair weights and $\sum_b^*$; set $M_s=0$ when the denominator vanishes. The three pair logarithms in a triple sum to $2\log d$. The denominator is $U_s V_2+O_A(hL^{-A})$ by (1), and $0\le M_s\le14$. Therefore
$$
 H_3(s)=\tfrac12 U_s V_2\bigl(\lambda_s^*-M_s\bigr)+O_A(hL^{-A}),
 \qquad \lambda_s^*=2V_3/V_2=\log(6/5)+O_A(L^{-A}).
 \tag{4}
$$
For the last equality write $\lambda=\sum_\ell c_\ell$, $D=\sum_\ell c_\ell\log\ell$. Omitting repeated prime indices costs $O(L^{O(1)}s^{-u})$ in $V_2=D\lambda$ and $2V_3=D\lambda^2$, viewed as approximations. The prime number theorem with its classical zero-free-region error gives $\lambda=\log(v/u)+O_A(L^{-A})$ and $D=(v-u)L+O_A(L^{-A})$; omitting primes of $N$ in the band costs $O(Ls^{-u})$. In particular $V_2\asymp L$.

The endpoint sieve bound [equation (2)](LargeLeastPrimeSemiprimes.md#how-large-can-the-isolated-sum-be) gives $U_s\ll S_s/\log z$, $S_s=h\mathfrak S(N)$, by dividing out one log weight. Thus a uniform upper bound $M_s\le\lambda_s^*+o((\log L)^{-3})$ would give $H_3(s)\ge-o(S_s)$ on this block. The first two divisibility moments do not supply this upper bound. The complete triple block and the other partner classes remain open. This calculation uses no GRH.

## A part of the three-prime range can already be removed

For $0\le\Delta\le v-u$ select the triples with at least two prime exponents within $\Delta$, i.e. $|\log(\ell_1/\ell_2)|\le\Delta L$ for some pair. In the original **full** labeled prime range $w<r\le Z/R$, $t>w$, with the actual cutoff $dr\le Z$, their total absolute arithmetic weight satisfies
$$
 \sum_{\rm actual}\log r\sum_{\substack{d\mid a,\ dr\le Z\\d\ {\rm selected}}}\log d
 \ll S_s\left[\frac{(\log L)^c}{L}
          +\frac{L}{\log z}\left(\Delta+\frac1L\right)\right]+O_A(hL^{-A})
 \tag{5}
$$
for an absolute $c$ (implied constants may depend on $A$). In particular $\Delta=(\log L)^{-4}$ gives $o(S_s)$ at every center. This removes a shrinking region inside a fixed exponent range beyond $1/6$. It does not remove every divisor in that range.

For the bottom $w<r<wL^K$ use the earlier absolute proper-divisor strip bound with the labeled prime as the proper divisor of $b$. On the interior drop $dr\le Z$ for an upper bound. Each actual close pair extends to at most $16$ actual triples, and each triple weighs at most $3vL$. By (1) the weighted number of actual close pairs is bounded by the rough-endpoint mass times $\sum_{\rm close}c_{\ell_1}c_{\ell_2}$ plus $O_A(hL^{-A})$. For a fixed prime $\ell_1$, the allowed partners have reciprocal sum $O(\Delta+1/L)$, by partial summation of the Chebyshev upper bound on the exponent interval (including the endpoint term). Summing over $\ell_1$ costs $O(1)$. The rough-endpoint mass on the full labeled interval is $\ll S_s/\log z$ by the same endpoint sieve bound, counting at most two orientations. This proves (5).

Within the restricted $r$-band of (2), the **projected** contribution of the close triples is also $o(S_s)$ for this $\Delta$. Apply (3) to just the selected triples: the coefficient bounds used in (1) survive selection. The actual count is covered by (5); its reference is $O(LU_s(\Delta+1/L))$ by the same reciprocal-pair estimate. Thus on the full-width block of (4) one can focus on triples whose prime exponents are mutually separated by more than $(\log L)^{-4}$. [Exact finite checks](CheckThreePrimeDivisorMoment.py)

## Why the two earlier moments cannot give the third

There are two probability laws on subsets of $\mathcal P$, each supported on at most three elements, with exactly the reference inclusion probabilities for **every singleton and every pair**. They can even agree on every close triple in (5), yet have opposite signs for the remaining expression in (3).

Prescribe inclusion probabilities $m(\varnothing)=1$, $m(T)=\prod_{\ell\in T}c_\ell$ for $|T|=1,2$, and $m(T)=\kappa_T\prod_{\ell\in T}c_\ell$ for $|T|=3$, with higher moments zero. In both laws take $\kappa_T=1$ on close triples. Take $\kappa_T=0$ on all other triples in the first law and $2$ there in the second. For an exact subset $B$ of size at most three assign the mass
$$
 p(B)=\sum_{\substack{T\supseteq B\\ |T|\le3}}(-1)^{|T|-|B|}m(T).
 \tag{6}
$$
Boolean inclusion-exclusion recovers the prescribed inclusions and total mass one. For large $s$, $\lambda=\sum c_\ell<1/2$. Pair masses are at least $c_i c_j(1-2\lambda)$; singleton masses are at least $c_i(1-\lambda)$. The empty mass is at least $1-\lambda+e_2-2e_3>0$, where $e_k$ denotes the elementary symmetric sum of the $c_\ell$ and $3e_3\le\lambda e_2$. Triple masses are nonnegative by definition.

In the two laws the mean of the centered sum in (2), per unit endpoint weight, is respectively $+V_{3,\mathrm{sep}}$ and $-V_{3,\mathrm{sep}}$, where $V_{3,\mathrm{sep}}$ counts the mutually separated triples in $V_3$. At $\Delta=(\log L)^{-4}$, $V_{3,\mathrm{sep}}=V_3+o(L)\asymp L$. The two laws even satisfy the elementary upper bound $Q\le16$ for a real endpoint. These are models for divisibility data, with no assertion that the models come from reflected semiprimes. They show explicitly which information (1) and the removal of close triples still leave undetermined.

The finite checker also enumerates an actual integer window at $N=91782$ with a diagnostic prime band $\{11,13,17,19\}$, wheel prime $5$ and conductor cutoff $1800$. Among 45 semiprime records before the wheel there are four triple incidences after it. With additive integer replacements for logarithms, summing the primitive kernels gives exactly the arithmetic centered triple, and equals the reference minus the actual count **plus the measured lower-moment errors**. Those finite errors are nonzero. The finite check tests signs and the order of operations; the asymptotic error in (3) comes from (1).
