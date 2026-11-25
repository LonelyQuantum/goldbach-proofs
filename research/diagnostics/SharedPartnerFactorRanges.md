# How composite partners can be distributed at a prime-square center

Fix $r\ge2$ and a sufficiently large prime $p$. Write $s=p^2$, $L=\log s$, $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$ and $U=H/L^{r+2}$. Fix the roughness parameter $B$ from the [five-factor estimate](CentralFiveAtTwoThirds.md) and set $z_0=s^{1/36}/L^{B/6}$. Use the $r$-element subsets $J$ of the complete consecutive shift blocks of width $\lceil100rL\rceil$ in $[1,T]$. A candidate is an upper prime $a=s+h$, $2T<h\le H$, with squarefree $b=s-h$ having at most five prime factors, all at least $z_0$, and all $b+2j$ prime for $j\in J$. Let $N_5(J)$ count these candidates. A prime $b$ gives a central Goldbach pair at $2p^2$.

We prove a uniform upper bound for candidates with a specified divisor of $b$. Together with the [previous positive-proportion bound](SharedPrimeCenters.md), it restricts the possible factorization patterns if the prescribed center has no prime pair. The positive lower counts below depend on the project's five-factor estimate, which awaits independent review. The divisor upper bound does not use that estimate.

## A uniform bound with a specified divisor

Put $k=r+2$, $F(n)=\prod_{\ell\mid n,\,\ell>2k}(1+2k/\ell)$ over primes, and
\[
 S(J)=F(s)\prod_{j\in J}F(j)F(s+j)\prod_{\substack{i,j\in J\\i<j}} F(j-i).
\]
For fixed $0<\kappa<2/3$, let $1\le d\le s^{2/3-\kappa}$ have no prime factor below $z_0$ (including $d=1$). Uniformly in $d,J$,
\[
 \#\{a\text{ counted by }N_5(J):d\mid b\}\ \ll_{r,\kappa,B}\ S(J)U/d. \tag{1}
\]

Write $b=dt$. The interval for $t$ has real length $(H-2T)/d\asymp Y=H/d\gg s^\kappa$. Sieve the forms $t,2s-dt,dt+2j$ for $j\in J$, up to $z=\min(z_0/2,R^{1/(4k)})$, $R=Y^{1/(20(k+2))}$. Each counted $t$ survives since $t\mid b$ and all the other values are primes of size $\asymp s$. We have $\log z\asymp_{r,\kappa,B}L$. For each prime $\ell<z$, multiplication by $d$ permutes the residues. The forbidden residues in the coordinate $dt$ are precisely $0,2s,-2j$ with repetitions removed. If they exhaust the residues, there are no survivors.

Otherwise let $\nu_\ell$ be the number of these residues and extend it multiplicatively to squarefree integers. In the [Selberg upper square](CentralPrimePairsNearOneCenter.md) the untruncated denominator is $\prod_{\ell<z}(1-\nu_\ell/\ell)^{-1}$. Under its normalized divisor law the expected log divisor is $\sum_{\ell<z}\nu_\ell\log(\ell)/\ell\le(1/4+o(1))\log R$. Thus truncating at $R$ retains at least half the denominator for large $s$. Each CRT residue class has counting error at most one on the actual $t$ interval. The total rounding error is $O_k(R^{4+2k})=O_k(Y^{1/10})$, using $|\lambda_e|\le e$ and $\nu([e,f])\le [e,f]^k$ for $e,f\le R$. This is $o(Y/L^k)$ uniformly. For $\ell>2k$ a root collision costs a ratio at most $1+2k/\ell$ against $1-k/\ell$ and requires $\ell$ to divide one of the arguments of $F$ above. Mertens' product bound and the finitely many small primes finish (1). No estimates for primes in a progression of modulus $d$ are used.

## Removing near-equal factorizations

The previous incidence estimate and the bounded fixed moments of $S$ give constants $c,K,\delta>0$ so that at least a fraction $\delta$ of these $J$ simultaneously have $N_5(J)\ge cU$ and $S(J)\le K$. Indeed choose $K$ large enough that the fraction with $S>K$ is less than half the previous rich fraction. All subsequent assertions refer to each of these $J$ separately.

For any collection of primes $\mathcal Q\subset[z_0,\sqrt s]$, the number of candidates with some $q\in\mathcal Q$ dividing $b$ is $\ll_{r,B}U\sum_{q\in\mathcal Q}1/q$, by (1) with $\kappa=1/6$. For $0<\eta\le 1/40$ take the union of $[s^{1/m-\eta},s^{1/m}]$ for $m=2,3,4,5$, intersected with that prime range. Its reciprocal sum is $O(\eta+1/L)$ uniformly: each interval meets $O(1+\eta L)$ dyadic intervals, all with lower endpoints $\gg s^{1/5-1/40}$, and $\pi(2Q)\ll Q/\log Q$ gives $O(1/L)$ per interval. In particular a width $\eta=L^{-1/2}$ costs $O_{r,B}(U/\sqrt L)$. Fix $\eta>0$ small enough in terms of $c,r,B$ that the total loss for large $s$ is at most $cU/4$.

At least $3cU/4$ candidates remain. Every surviving composite $b=q_1\cdots q_m$, $q_1<\cdots<q_m$, satisfies
\[
 q_1<s^{1/m-\eta},\qquad q_m\ge (1-H/s)^{1/(m-1)}s^{1/m+\eta/(m-1)}.
\]
Indeed $q_1\le b^{1/m}<s^{1/m}$, and $q_m^{m-1}\ge b/q_1$. All prime partners survive the removal.

## If the exact prime pairs are scarce

Suppose fewer than $cU/4$ candidates have $b$ prime for the given $J$. This holds, in particular, if $2p^2$ has no positive-offset central prime pair. Some single $m\in\{2,3,4,5\}$ then accounts for at least $cU/8$ surviving composites. Set $t_m=\lfloor 2m/3\rfloor$, respectively $1,2,2,3$. Sort the first $t_m$ primes of each of those partners into ordered dyadic boxes, with coordinate $q_i\in[Q_i,2Q_i)$, $Q_i$ a power of two. Then

* at least $\gg_{r,B} L^{t_m}$ different boxes each contain $\gg_{r,B}U/L^{t_m}$ candidates;
* in every such box these candidates realize $\gg_{r,B}(\prod_i Q_i)/L^{t_m}$ distinct ordered tuples of actual prime factors.

To see the margin for applying (1), put $d=q_1\cdots q_{t_m}$. By ordering, $d^m\le b^{t_m}$. For $m=2,4,5$ this gives $d\le s^{3/5}$ or better. For $m=3$ use $q_2^2\le b/q_1$ and the preceding exclusion to get $d^2\le bq_1<s^{4/3-\eta}$. Thus $\kappa=\min(1/15,\eta/2)>0$ works in all four cases. Its choice comes after the one-divisor estimate fixed $\eta$.

There are $O(L^{t_m})$ boxes. Each occupied coordinate has $Q_i>z_0/2$, so the sum of reciprocal primes in it is $O_B(1/L)$. By (1), summing only over realized tuples and then enlarging the reciprocal sums, every box contains $O_{r,B}(U/L^{t_m})$ candidates. Boxes with fewer than $\epsilon U/L^{t_m}$ candidates contribute at most $cU/16$ in total for a sufficiently small fixed $\epsilon>0$. The remaining mass and the per-box cap give the first assertion. One specified tuple can account for at most $O_{r,B}(U/\prod_i Q_i)$ candidates by (1), giving the second.

The bounds permit a dispersed population of composites of the stated size. In particular, the case $m=2$ can already occupy order $L$ distinct least-factor intervals. To deduce a prime pair from this count one still needs a joint bound on the composite contribution across those ranges that is strictly below the candidate lower bound. The [finite checker](CheckSharedPrimeCenters.py) exercises the change of variables, the product inequalities and the counting conventions.
