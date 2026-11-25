# Mixed fourth moments of short blocks of prime-square frequencies

Fix integers $X\ge3$ and $1\le H\le X$. Partition the integers in $[X,2X]$ into consecutive blocks of $H$ entries, truncating the last. Write $I_U$ for the block starting at $U=X+iH$, $D=H-1$, $M=\lfloor D/2\rfloor$, and $e(t)=\exp(2\pi i t)$. For any subset $S$ of the odd integers in this interval and $|z_p|\le1$, put
$$
K_U(\alpha)=\sum_{p\in S\cap I_U}z_p e(2p^2\alpha),\qquad
m_U=\sum_{p\in S\cap I_U}|z_p|^2.
$$
All integrals use probability Lebesgue measure on $[0,1]$. The elementary estimates below apply in particular to primes.

## A uniform bound for each fixed block

Let $T_{UV}$ count ordered solutions of $a^2+b^2=c^2+d^2$ with $a,c\in S\cap I_U$, $b,d\in S\cap I_V$ and $a\ne c$. This convention includes $U=V$ and includes swapped pairs there. Let $\mathcal H_M=\sum_{j=1}^M1/j$, taking $\mathcal H_0=0$. Then
$$
\begin{split}
\#\{V\ne U:T_{UV}>0\}&\le 3M^2,\\
\sum_V T_{UV}&\le 4D^2\mathcal H_M+2DM. \tag{1}
\end{split}
$$
These bounds hold for **every** $U$. In particular if $H^3=o(X)$, the fraction of partner blocks with a nonzero count tends to zero uniformly in the chosen block. Outside this set of partners, orthogonality gives $\int |K_U|^2|K_V|^2=m_Um_V$ exactly.

**Proof.** Order the collision as $a>c$, which implies $d>b$. The opposite ordering contributes a factor of two. Write $h=(a-c)/2$ and $k=(d-b)/2$, which are positive integers because all labels are odd. The equality $h(a+c)=k(b+d)$ shows that $1/2\le h/k\le2$. Write this ratio as $r/s$ in lowest terms and put $j=\max(r,s)\le M$. For the midpoints $A=(a+c)/2$, $B=(b+d)/2$ we have $rA=sB$, hence
$$
 V-\frac rs U=\frac rs(A-U)-(B-V)\ \in[-D,2D].
$$
For a fixed $r/s$ this interval for $V$ has length $3D<3H$, so it contains at most three grid origins. There are at most $M^2$ possible slopes. This proves the first inequality, including the single-entry case.

Since $r,s$ are coprime, $A=su$, $B=ru$ and $h=rv$, $k=sv$ for unique positive integers $u,v$. Thus the four labels are
$$
a=su+rv,\quad c=su-rv,\quad d=ru+sv,\quad b=ru-sv.
$$
Fix $U,r,s$. The within-block gaps imply $v\le D/(2j)$. The midpoint $su$ lies in $[U,U+D]$, so the number of $u$ values is at most $D/s+1\le2D/j+1$. Once $u,v$ are fixed, the other labels determine at most one partner block because the partition is disjoint. This counts **all partners together**, including $V=U$. There are at most $2j$ pairs $(r,s)$ with maximum $j$. Summing $2j\cdot 2\cdot(D/(2j))\cdot(2D/j+1)$ proves (1). The bound uses a closed interval of length $D$ even for the truncated block.

## Mean-square consequence for the block energies

Each off-diagonal ordered quadruple contributes a complex number of modulus at most one. In particular
$$
\left|\int |K_U|^2|K_V|^2-m_Um_V\right|\le T_{UV}.
$$
For $Q(\alpha)=\sum_U |K_U(\alpha)|^2$ the mean is $m=\sum_U m_U$. Summing (1), including its same-block terms, bounds the variance by
$$
\int |Q-m|^2\le \bigl(\lfloor X/H\rfloor+1\bigr)
       (4D^2\mathcal H_M+2DM)\ll XH\log(2H). \tag{2}
$$
For all primes in the dyadic interval with $|z_p|=1$, $m\sim X/\log X$. In particular $Q/m\to1$ in mean square whenever $H=o(X/\log^3 X)$, uniformly over those phases. A signed test function $f\in L^2$ can be inserted with error $|\int f(Q-m)|\le\|f\|_2\sqrt{\int |Q-m|^2}$. The sum of block energies lacks the products $K_U\overline{K_V}$ for $U\ne V$ that occur in $|\sum K_U|^2$.

## The full fourth moment and its effect on the earlier minor-arc estimate

For $K=\sum_U K_U$ supported on primes, unrestricted orthogonality also gives
$$
\left|\int|K|^4-\left(2m^2-\sum_p|z_p|^4\right)\right|
\ll X^2/(\log X)^3. \tag{3}
$$
Indeed the two ordered permutations of each pair give the displayed diagonal, with double-counting removed for a repeated prime. Every remaining quadruple is a member of $D_2(4X^2)$ as defined by square *coordinates* at most $\sqrt{4X^2}$ in §1 of Sabuncu. Take absolute values termwise before enlarging the count. Rieger's unconditional estimate for $D_2$ there includes distinct unordered pairs even when one pair has a repeated entry. Formula (3) has an absolute error uniform in the coefficients. For unit coefficients the diagonal is of order $X^2/\log^2 X$. This argument imports the literature bound. [Sabuncu, *On the Moments of the Number of Representations as Sums of Two Prime Squares*, §1, definition of $D_k$ and the bound following it](https://arxiv.org/pdf/2307.11547#page=2) · [Rieger's original paper, 1968, pp. 89–100](https://doi.org/10.1515/crll.1968.231.89)

In the [earlier prime-pair distribution calculation, equation (3)](https://github.com/LonelyQuantum/goldbach-proofs/blob/f4ff8da91616a1d5ad072805a19d79beab43d5b8/research/diagnostics/PrimeSquarePairDistribution.md), take $Y=8X^2$, $L=\log Y$, and denominator cutoff $L^B$ for fixed sufficiently large $B$. For each test $(u,b,d)$ let $E_p$ be its minor-arc coefficient there. Choose a phase for each $p$ so the weighted sum gives $\sum_p|E_p|$. Formula (3) gives $\|K\|_4\ll X^{1/2}L^{-1/2}$. For both prime sums in that argument, Parseval and $\sum_{p\le Y}\log^2p\ll YL$ give $\|S\|_2,\|S_{u,b,d}\|_2\ll(YL)^{1/2}$. On the minor arcs $\mathfrak m$ the earlier Vaughan estimate gives $\sup_{\mathfrak m}|S|\ll Y L^{5/2-B/2}$. Interpolation and Hölder yield
$$
\begin{split}
\|\mathbf1_{\mathfrak m}S\|_4&\ll Y^{3/4} L^{3/2-B/4},\\
\sum_p|E_p|&\ll XY L^{3/2-B/4}. \tag{4}
\end{split}
$$
The last two norm factors contribute opposite log powers, and $Y^{5/4}X^{1/2}\asymp XY$. Equation (4) gives a logarithmic improvement for the same auxiliary arcs. It remains an aggregate estimate. Even taking $K$ supported at one prime, the corresponding norm argument gives $O(Y^{5/4}L^{2-B/4})$, which exceeds the signal scale $Y$ asymptotically for fixed $B$.

## Verification

[Lean source](PrimeSquareMixedWindow.lean) verifies the cleared-denominator midpoint restriction on integer labels, with the upstream Lean 4.36.0 and the research environment's Lean 4.35.0. Both axiom audits listed only `propext`, `Classical.choice` and `Quot.sound`. Equations (1)–(4) use the paper arguments above.

Run `python PrimeSquareMixedWindowsCheck.py` next to the [standalone check](PrimeSquareMixedWindowsCheck.py). It compares Cartesian square sums, within-block differences, and primitive-slope parametrization on six finite partitions for both all odd integers and the primes. For $X=1000$, $H=26$ the 39 blocks have 7 unordered distinct prime-block pairs with a collision among 741 possible pairs. The maximum full row count is 32, and the variance for unit prime coefficients is 428. For example $1021^2+1213^2=1009^2+1223^2$. Over the whole prime interval $[1000,2000]$, the unit energy is 40,747, of which 4,432 ordered quadruples have distinct unordered pairs. These last two counts use different restrictions.
