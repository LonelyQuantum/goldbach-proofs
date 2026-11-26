# Which semiprime records can detect a prescribed Goldbach pair?

The [proposed W14 parity identity](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2588) separates prime and semiprime remainders of a fixed even target. Its admissible semiprimes are $rq$ with $r,q$ prime and $r^{10}\le q^9$. The counts are of prime summands, so the two orientations of a distinct prime pair count separately where both satisfy the cutoff. Li and Liu's preprint gives a lower bound for the combined count for sufficiently large even targets in the full summand range. In particular it does not give that lower bound for the prime branch alone or in a prescribed central window. [W14 single-file submission](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2591) · [Li and Liu v2, Theorem 1.1 and (4.4)](https://arxiv.org/pdf/2606.05224v2#page=2)

## What remains exactly the same after deleting prime pairs

For even $N=2Y\ge8$, form $E$ from the actual primes by deleting each prime $p\ge Y$ for which $N-p$ is prime. This hits every Goldbach pair of $N$, including a prime midpoint. It preserves, **tuple by tuple**, every record
$$
 N=p+r_1\cdots r_k,\qquad k\ge2,\qquad p,r_1,\ldots,r_k\text{ prime}.
$$
Indeed $p$ has composite complement, and every $r_i\le(N-p)/2<Y$. All entries survive in the same $E$, including repeated factors. Passing to a subset can add no records. All prime pairs at every even target $M\le Y$ also survive because their summands are $<Y$. This simultaneously preserves every semiprime record in W14 at $N$, with every cutoff on its complement, as well as the full prime-pair lists throughout the lower half-range.

Use membership in $E$ for **each** prime argument when comparing records. For W14 write $D=R+B$ and $J=B-R$, with $R$ the ordered prime branch and $B$ the semiprime branch. The comparison keeps $B$ exactly. The combined count $D$ can fall by $R$ and the signed count $J$ can increase by $R$. Their difference is the missing information. This is a statement about the data retained by a subset of actual primes. It neither preserves every analytic estimate about the full primes nor supplies a counterexample to W14 or Goldbach.

## Detecting the deletion at nearby centers using only the factor 3

For the remaining statements let $Y$ be sufficiently large, $L=\log Y$, $H=\lfloor Y^{2/3}\rfloor$, $T=\lfloor Y^{21/40}\rfloor$, $D_0=\lfloor Y^{16/25}\rfloor$. Use the symmetric set $I=\{a:2T<|a-Y|\le H\}$ of integer summands. Write $r_N$ for the number of **unordered** pairs in $I$. For $1\le s\le D_0$ record
$$
 A_s=\{(a,q):a\in I,\quad N+2s=a+3q,\quad a,q\text{ prime}\}.
$$
Here $q\asymp Y/3$, so $3^{10}\le q^9$ and all records qualify for the W14 semiprime branch with complement cutoff zero. For any odd $a\in I$, the possible prime factors $q$ lie in $((N-a)/3,(N-a+2D_0)/3]$. Every prime in that interval is odd and yields a unique integer label $s$. Let $w(a)$ denote their number, without requiring $a$ itself prime. Uniformly in $a$,
$$
 w(a)=\lambda+O_A(D_0/L^A),\qquad \lambda=\frac{2D_0}{3\log(Y/3)}. \tag{1}
$$
Take modulus one in the fixed-interval prime estimate (1.1) cited below. The interval length exceeds $Y^{3/5}$ by a power. On it $\log q=\log(Y/3)+O(H/Y)$, so replacing the prime logarithm in the weighted estimate costs a power saving. In particular no averaging over $Y$ or $a$ enters (1). [Koukoulopoulos, introduction, (1.1), stating Timofeev's estimate](https://arxiv.org/pdf/1405.6592v2#page=1)

For a subset $E'$ of primes use the same membership predicate for $a,3,q$ and denote the resulting lists by $A_s(E')$. Among all subsets destroying all the pairs in $I$, the exact minimum of the loss in the sum of the list sizes is
$$
 \min_{E'}\sum_{s=1}^{D_0} (|A_s|-|A_s(E')|)
 =\sum_{\{a,b\}\text{ prime pair in }I,\ a+b=N}\min(w(a),w(b))
 =(\lambda+O_A(D_0/L^A))r_N.                                    \tag{2}
$$
At least one endpoint of each disjoint pair must be deleted. Its $w(a)$ records carry that endpoint as their first coordinate. Conversely delete a cheapest endpoint of each pair and keep all other primes. All auxiliary primes, including 3, lie outside $I$, hence this attains the lower bound. One may also destroy pairs outside $I$ by deleting their larger endpoint, without changing the lists. Thus even scalar counts at neighboring centers can detect deletions if an **independent** control of their total loss is precise enough. For a single pair the average lost count per label is of order $1/\log Y$.

## Many smaller even targets carry compatible records

Take $(a,q)\in A_s$ and $(b,u)\in A_t$, with $a>Y>b$. There is an exact test
$$
 a+b=N\quad\Longleftrightarrow\quad 3(q+u)=N+2(s+t).            \tag{3}
$$
On a match, $M=q+u$ is even and lies in $((N+2)/3,(N+4D_0)/3]$, strictly below $Y$. The ordering on $a,b$ counts each original pair once. For a fixed original pair the number of labeled matches is exactly $w(a)w(b)$. Equations (1) and (3) give a total $(1+o(1))\lambda^2 r_N$.

There exist absolute $c_1,c_2>0$ such that for **each** original prime pair, at least $c_1D_0$ distinct smaller even targets $M$ each have at least $c_2D_0/L^2$ compatible labeled matches for that pair. One may require $q,u$ to be in the trimmed central window of $M$ as well. An unordered pair $\{q,u\}$ accounts for at most two of these matches at a fixed original pair and $M$.

To check the trim, $q-M/2=(b-a+2(s-t))/6$. Hence $|q-M/2|\le H/3+D_0/3<\lfloor(M/2)^{2/3}\rfloor$ for large $Y$ because $1/3<3^{-2/3}$. For each $s$, the inner exclusion $|q-M/2|\le 2\lfloor(M/2)^{21/40}\rfloor$ rules out $O(1+Y^{21/40})$ choices of $t$. Even before imposing primality the total loss is $O(D_0Y^{21/40})=o(D_0^2/L^2)$.

For the concentration estimate write $V_M$ for the surviving matches for the fixed original pair. Once $M$ and $q$ are specified, $u=M-q$ and both labels are determined. Put $F(M)=\prod_{\ell\mid M,\ \ell>2}(\ell-1)/(\ell-2)$ over primes. The two-root upper sieve on the interval for $q$ gives
$$
 V_M\ll D_0 F(M)/L^2.                                         \tag{4}
$$
Here the two forbidden residues are $0,M\bmod\ell$, coinciding precisely if $\ell\mid M$. For details one can use the Selberg square in the [preceding note](RoughOffsetSpacing.md#sifting-two-distinct-offsets-together) with interval length $m\asymp D_0$, radius $Z=m^{1/40}$ and sieving primes $7\le\ell<Z^{1/16}$. The crude rounding error $O(Z^8)$ is negligible. The generic local product is $\asymp L^{-2}$ and a coincident odd prime multiplies it by $(\ell-1)/(\ell-2)$. Both true primes exceed the sieve cutoff.

Throughout this interval of $M$, $\sum F(M)^2\ll D_0$. To see uniformity, expand $F(M)^2=\sum_{d\mid M}g(d)$ with $g$ supported on odd squarefree integers, $g(\ell)=((\ell-1)/(\ell-2))^2-1$. The multiple count is $O(D_0/d+1)$, $\sum g(d)/d=O(1)$, and $\sum_{d\le2Y}g(d)\ll(\log Y)^2$ by the Euler product. Equation (4) gives $\sum V_M^2\ll D_0^3/L^4$. Meanwhile $\sum V_M\gg D_0^2/L^2$ by (1) and the trim. The targets below $c_2D_0/L^2$ together carry at most half that lower bound for small enough $c_2$. Cauchy–Schwarz on the remaining targets proves the assertion. In particular discarding any $o(D_0)$ prescribed smaller targets preserves a constant proportion of the matches of **each** original pair. An exceptional set is allowed to depend on $N$.

The argument provides many descents from an existing pair. A proof by induction in the reverse direction would need at least one *compatible* pair of records. Even if $M=q+u$ is furnished and $k=(3M-N)/2$ is integral, setting $t=k-s$ makes the two required large entries $a=N+2s-3q$ and $b=3q-2s$. Their primality still concerns the same fixed sum $N$. The subset in the first section preserves all smaller prime-pair data. Equation (2) isolates a neighboring statistic on which that subset can fail.

For the untrimmed smaller pairs and the deletion measurement (2), the ordinary Riemann hypothesis gives a shorter usable label range, $D_0=\lfloor\sqrt Y\,L^3\rfloor$. The error $O(\sqrt Y\,L)$ in $\pi(x)-\operatorname{li}(x)$ is then $O(\lambda/L)$ in each interval, so the relative error in $w(a)$ is $O(1/L)$. The inner-trim argument above uses the larger unconditional range. No GRH premise is needed for (1)–(4) at $D_0=\lfloor Y^{16/25}\rfloor$. [Schoenfeld, Corollary 1](https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf)

## A positive reference term for the missing reverse implication

Here the auxiliary primes $q,u$ are tested before either large endpoint. Keep both orientations. Put $h=H-2T$, $w=L/(\log L)^2$ and $W=\prod_{\ell\le w}\ell$. Start from all $a\in I$, $b=N-a$, with $(ab,W)=1$. For each such $a$, keep the labels $s,t$ for which $q=(b+2s)/3$ and $u=(a+2t)/3$ are primes in the trimmed window of $M=q+u$. Call this list at $M$ the set $\mathcal L_M$, write $n_M=|\mathcal L_M|$, and let $S_M$ count records with $a$ prime. The involution $(a,b,s,t,q,u)\mapsto(b,a,t,s,u,q)$ preserves $\mathcal L_M$, so exactly $S_M$ records have $b$ prime. Set $\alpha_M=S_M/n_M$ on nonempty lists. Define
$$
 B_N=\sum_{n_M>0}\frac{S_M^2}{n_M},\qquad
 E_N=\sum_M\sum_{\mathcal L_M}
       (1_{\mathbb P}(a)-\alpha_M)(1_{\mathbb P}(b)-\alpha_M).
$$
The definitions give $B_N+E_N=(2+o(1))\lambda^2 r_N$ with uniform relative counting weights for each original pair, and exact zero when $r_N=0$. The following lower bound holds at **every** sufficiently large $N$:
$$
 B_N\ge (1-o(1))\,\lambda^2\frac{2h}{L^2}\,\mathfrak S(N),\qquad
 \mathfrak S(N)=2C_2F(N),\quad C_2=\prod_{\ell>2}(1-(\ell-1)^{-2}). \tag{5}
$$
In particular it would suffice to bound $E_N$ from below by $-(1-\eta)$ times the displayed reference scale for a fixed $\eta>0$. This would imply $r_N\gg_\eta h\mathfrak S(N)/L^2$. The covariance condition concerns actual compatible records over the smaller targets.

For the proof let $\nu_\ell=1$ if $\ell\mid N$ and $2$ otherwise, and put $V=\prod_{\ell\le w}(1-\nu_\ell/\ell)$ and $U_1=\prod_{\ell\le w}(1-\nu_\ell/\ell)/(1-1/\ell)$, with the quotient taken at each prime. The number of starting $a$ is $(1+o(1))2hV$ by CRT since $W=\exp(O(w))=Y^{o(1)}$. Of these, $(1+o(1))2hU_1/L$ are prime. Indeed, for prime $a$ inclusion-exclusion for $N-a$ requires one reduced class modulo each squarefree $d\mid W$ coprime to $N$. If $\ell\mid N$, an $a\in I$ equal to $\ell\le w$ is impossible. Timofeev's estimate over moduli up to $Y^{1/7}$ on the two intervals, each of length $h\asymp Y^{2/3}$, sums the errors with an arbitrary log-power saving. Replacing the prime log by $L$ on the final nonnegative count gives a uniform relative $1+o(1)$. The products satisfy $V\gg(\log w)^{-2}$ and $U_1\gg(\log w)^{-1}$. [Fixed-interval distribution range](https://arxiv.org/pdf/1405.6592v2#page=1)

By (1) and the inner-trim estimate, **every** starting $a$ has $(1+o(1))\lambda^2$ labeled records, uniformly, even when $a,b$ are composite. Therefore $\sum_M n_M\sim 2hV\lambda^2$ and $\sum_M S_M\sim 2hU_1\lambda^2/L$. Cauchy–Schwarz gives $B_N\ge(\sum S_M)^2/\sum n_M$. The local factor of $U_1^2/V$ is $(1-\nu_\ell/\ell)/(1-1/\ell)^2$. Their product for all primes is $\mathfrak S(N)$. In passing from $w$ to infinity the generic tail is $1+O(1/w)$, while $\sum_{w<\ell\le L}1/\ell=o(1)$ by Mertens and $\sum_{\ell\mid N,\,\ell>L}1/\ell=O(1/\log L)$. This proves (5), uniformly including highly composite $N$.

Pooling the smaller targets gives the baseline $(\sum S_M)^2/\sum n_M$. Keeping them separate increases this reference by the nonnegative quantity $\sum n_M(\alpha_M-\bar\alpha)^2$, with $\bar\alpha=\sum S_M/\sum n_M$. It decreases the centered covariance by the same amount. A gain on the signed sum requires arithmetic information about the two prime marks in compatible records. The individual small-target counts alone do not provide that gain.

## What a genuine exception would force in the full range

There is also a consequence for actual primes at the original target. Use $U=C(N)N/\log^2N$ with $C(N)=C_2F(N)$ in Li–Liu's normalization, $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$. Write $\alpha=4/53$, $\beta_0=9/19$ and $c=1/2500$. Use the quantitative analytic estimates from their preprint as input. Either $N$ has at least $cU/2$ ordered prime-pair representations in the full range, or the following holds. In $\gg\log N$ distinct dyadic blocks $[R,2R)$ of the range $N^\alpha\le r<N^{\beta_0}$ there are $\gg R/\log N$ distinct primes $r$ each with $\gg U/r$ different prime solutions $(p,q)$ to $N=p+rq$, $r^{10}\le q^9$. Absolute constants may depend on the fixed parameters of the paper. This concerns each sufficiently large even $N$; no central-window conclusion follows from this full-range input.

For the needed support refinement, read the inequality in the proof, not only the final statement. In (4.6) of Li and Liu the right side counts prime remainders and semiprime remainders whose smaller prime lies in $[N^\kappa,N^\tau)$, with $N-p>\varepsilon N$ and $\tau=9/19-\varepsilon$. This follows by splitting $\Omega(n)=1,2,\ge3$ directly in the four displayed sums. In (4.9) and (4.12), both such counts are bounded above by the count with the smaller of the two lower cutoffs. The two uses (4.19) and (4.20) have cutoff pairs $(\alpha,1/3)$ and $(4/33,3/11)$, all at least $\alpha$. Therefore the left side in their (5.51) may be restricted to prime remainders and this union of qualifying semiprimes. Their reported margin $0.00172$ on the scale $4U$ leaves the weaker bound $cU$ for this restricted count. We have checked this support implication and have not independently reproduced their analytic constants. [Original inequalities (4.6)–(4.14)](https://arxiv.org/pdf/2606.05224v2#page=12) · [Two applications of the inequality](https://arxiv.org/pdf/2606.05224v2#page=16) · [Parameters (5.1) and final bound (5.51)](https://arxiv.org/pdf/2606.05224v2#page=43)

If the first alternative fails, write $T_r$ for the number of these semiprime records with fixed smaller prime $r$. Uniqueness of the smaller factor gives $\sum_r T_r\ge cU/2$. Uniformly $T_r\le BU/r$ with an absolute $B$. If $r\mid N$, the summand $p$ equals $r$ and there is at most one choice of $q$. Otherwise sieve $q$ and $N-rq$ for $q\le N/r$. The two roots modulo $\ell\nmid r$ coincide exactly when $\ell\mid N$. At $\ell=r$ only one root is forbidden. Relative to the two-root product this last correction is bounded by $(r-1)/(r-2)\le2$ for odd $r$. The Selberg square used for (4), now at length $m=N/r\ge N^{1-\beta_0}$, gives the asserted bound. Solutions with $p$ or $q$ at most the sieve cutoff contribute $O(m^{1/640})$ since each linear form is injective. This proof requires no distribution theorem for primes in a single large residue class.

The reciprocal sum of all primes in the range is bounded by a fixed $B_0$ by Mertens' theorem. Discard those $r$ with $T_r<cU/(4B_0r)$. The rest carry at least $cU/4$, hence their reciprocal sum is at least $c/(4B)$. Each dyadic block contributes $O(1/\log N)$ to this reciprocal sum by the ordinary upper bound for the prime count and $R\gg N^\alpha$. There are $O(\log N)$ blocks in all. Consequently $\gg\log N$ blocks each contribute $\gg1/\log N$, which proves the stated abundance in each. In particular an arbitrary $o(\log N)$ selected blocks cannot carry all of the semiprime alternative.

In that alternative one may choose one witness for **every** retained $r$ so the chosen triples have no prime in common. Discard $p\le N^{\beta_0}$, costing at most $N^{\beta_0}/r+1=o(U/r)$ per $r$, and discard $p=q$, costing at most one. Each $q>\varepsilon N^{1-\beta_0}>N^{\beta_0}$. Upon processing an $r$, fewer than $2N^{\beta_0}$ already used large primes each rule out at most two possibilities because $q$ and $p=N-rq$ are both injective in $q$. The remaining choices before these exclusions are $\gg N^{1-\beta_0}/\log^2N\gg N^{\beta_0}$. This is a consequence of a lower bound for the *combined* branch together with a two-prime upper bound; it still permits the prime branch to vanish.

At $Y=1009^2$ there are 52 unordered prime pairs in $I$ and $D_0=6998$ labels. The integer minimum in (2) is 18,798 records. The pair at offset 10,110 has 133,947 labeled matches, of which 121,357 survive the smaller-window trim, on 4,563 distinct smaller even targets. These figures use the stated powers with exact integer floors. The checker also compares 8,143 composite tuples before and after deletion across 253 even targets, tests (3) in both directions, and verifies the covariance identity and pooling inequality in nine finite instances. [Independent finite enumerations](CheckSemiprimeRecords.py)
