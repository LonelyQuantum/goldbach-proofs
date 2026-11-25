# Central prime plus almost-prime bounds at every even target

Write $N=2X$, where $X$ is an integer. Fix $d\ge1$, $193/290<\theta\le2/3$, and $H=\lfloor X^\theta\rfloor$. For $0\le b<d$ with $(b,d)=(N-b,d)=1$, count positive offsets $h\le H$ for which $t=X+h$ is prime, $t\equiv b\bmod d$, and $a=X-h$ is squarefree with at most $r$ prime factors. Denote this count by $G_r$. The unconditional paper deduction in the first part is
$$
G_6\gg_{d,\theta} \mathfrak S_d(N)\,\frac{H}{(\log X)^2},
\qquad
\mathfrak S_d(N)=\prod_{\substack{\ell\mid N,\ \ell>2\\ \ell\nmid d}}
\frac{\ell-1}{\ell-2}
$$
for every sufficiently large even $N$, uniformly in the admissible class. At the slightly wider exponent $\theta=17/25$ we also obtain, unconditionally,
$$G_5\gg_d\mathfrak S_d(N)\,\frac{H}{(\log X)^2}.$$
One may additionally require every prime factor of $a$ to be at least $z$ for the respective window. The signed estimate sufficient for five factors at the original $\theta=2/3$ remains unproved. The wider-window proof is given at the end.

## Removing the prime-square hypothesis

Use the parameters and notation of [the six-factor calculation](CentralPrimeSixFactors.md): $\delta=\theta-1/2$, $D=X^\delta/(d\log^B X)$ with $B$ sufficiently large, $z=D^{1/4}$, $Y=(\operatorname{Li}(X+H)-\operatorname{Li}(X))/\varphi(d)$, $K=e^\gamma/2$, and $V(z)=\prod_{2<\ell<z,\,\ell\nmid d}(1-1/(\ell-1))$. Products indexed by $\ell$ here are over primes. For each odd $\ell<z$ outside $d$, forbid one residue $t=c_\ell\bmod\ell$. If $\ell\nmid N$, take $c_\ell=N\bmod\ell$. If $\ell\mid N$, choose *any nonzero* $c_\ell$. Every forbidden residue is a unit.

For each squarefree $k<D$ supported on these primes, the condition of hitting all forbidden residues fixes one reduced class modulo $dk$. Hence its density among the primes in the starting progression is $1/\varphi(k)$. The sum of absolute discrepancies is $\ll_{A,d} H/\log^A X$ for arbitrarily large fixed $A$, independently of the tuple of choices, by the maximum over reduced classes in Cai–Lu's short-interval estimate at $\beta=0$. The ordinary one-dimensional sieve applies to these residue conditions (equivalently translate all $t$ by one common CRT representative). The marked survivors with prime $t$ are genuinely rough at the reflected endpoint: if $\ell\mid N$ and $\ell\mid a$, then $\ell\mid t$, which is impossible for a prime $t>X$ dividing $N=2X$ once $X>1$. At $2$ both endpoints are odd. At primes dividing $d$, admissibility already gives both units. [Cai and Lu, Lemmas 1–3, pp. 312–313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=2)

For the penalty at $q\ge z$, omit $q\mid Nd$; no surviving endpoint $a$ has such a divisor. For every other $q$, the restriction $q\mid a$ fixes the reduced class $t\equiv N\bmod q$. The small-$q$ upper sieve has the same main term as before. Each remainder modulus $qk<D$ has exactly one prime factor at least $z$, so its absolute error is charged once. Dropping primes from the positive upper main-term sum can only improve the final lower bound.

For $D^{9/10}\le q<D^{5/4}$ put $a=qm$. Sift $t=N-qm$ against zero below $w=z^2$ and against $c_\ell$ at the odd active primes below $z$. As $q>w$, the forbidden classes of $m$ at an odd active prime below $z$ are $N/q$ and $(N-c_\ell)/q$; they are distinct even when $\ell\mid N$. There is one forbidden class at each remaining active prime, including 2 if $d$ is odd. Thus the two-root product, Selberg denominator and rounding bounds in the six-factor calculation are uniform in $N$ and all markers. The weighted factor-count inequality and the cost $O(H/z+\sqrt X)$ of removing squares also apply. We obtain $\gg_{d,\theta} H/\log^2 X$ marked, squarefree, six-factor offsets for *each* tuple, with a common constant and threshold.

Now take the exceptional markers at $\ell\mid N$ independently and uniformly among units. Every genuine qualifying rough offset survives with probability $\prod_{\ell\mid N,\,2<\ell<z,\,\ell\nmid d}(\ell-2)/(\ell-1)$. Averaging the count, then dividing by this exact probability, recovers the reciprocal product. The remaining prime divisors $\ell\ge z$ number at most $\log(2X)/\log z=O_\theta(1)$, so their product of correction factors is $1+O_\theta(1/z)$. This proves the stated result. The threshold for $X$ may depend on $d,\theta$; no uniformity in growing $d$ is asserted.

For a finite illustration, with $X=210$, $d=1$, $z=8$, the exceptional primes are $3,5,7$. Every qualifying offset survives exactly $1\cdot3\cdot5=15$ of the $2\cdot4\cdot6=48$ marker tuples. This example checks the local factor $16/5$ and uses an illustrative finite cutoff.

This sharpens the scope of the prime-square calculation. Classical work obtains fewer factors in wider windows: for example Cai–Lu's main theorem gives $P_2$ at width $N^{0.972}$. The contribution here is a specialization and extension of sieve inputs at the stated width, without a claim of priority. [Cai–Lu, main theorem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/91/4/110811/chen-s-theorem-in-short-intervals)

## One signed arithmetic estimate sufficient for five factors

Fix $\theta=2/3$. Use the preceding marked set, with $u=1/2$, $y=D^2$, $\lambda=299/100$ in the Richert weight. The small-divisor range ends at $D^{7/9}$. Write $W_q=1-\log q/(2\log D)$ and sum over primes $q\nmid Nd$ in $[D^{7/9},D^2)$. Split this interval into dyadic blocks $J=[Q,2Q)$ intersected with the interval (one may start the doubling at $D^{7/9}$). Choose one radius per block
$$ R_J^2=H X^{1/10}/Q . $$
On $a\in[X-H,X)$ in the class $N-b\bmod d$, set the bad residues $\Omega_\ell$ to $N\bmod\ell$ for primes $\ell<R_J$ outside $d$, adding $N-c_\ell\bmod\ell$ at odd active $\ell<z$. For squarefree products $n$ of these primes let $\Omega_n$ be the CRT product and $\nu(n)=|\Omega_n|$. For $n=1$ take the unique residue. Let $\lambda_i$ be the normalized optimal Selberg square coefficients at radius $R_J$ for those densities, with $\lambda_1=1$, as in the [explicit formula](CentralPrimeSixFactors.md#an-integer-sieve-for-the-remaining-divisors). Put $C_J(n)=\sum_{[i,j]=n}\lambda_i\lambda_j$ where $i,j<R_J$ are in the sieve support. In particular $|C_J(n)|\le3^{\omega(n)}$.

For $(n,q)=1$ define the exact discrepancy
$$
e_{n,q}=
\#\{a\in[X-H,X)\cap\mathbb Z:a\equiv N-b\bmod d,\ q\mid a,\ a\bmod n\in\Omega_n\}
-\frac{H\nu(n)}{dqn}.
$$
Each $n$ is coprime to $d$. If $q\mid n$, the observed count vanishes, since $q\ge z$ and its only bad residue is $N\not\equiv0\bmod q$. Omit these pairs from both the count and its main term. The signed sum of rounding errors is
$$
\mathcal E=\sum_J\sum_{n<R_J^2} C_J(n)\sum_{\substack{q\in J,\ q\nmid Nd\\(q,n)=1}} W_q e_{n,q}
$$
with zero coefficient off the sieve support. Expanding the square on multiples of $q$ in the interval gives an upper bound on the true total penalty. Its error is exactly $\mathcal E$.

**The main term fits.** For this square write $G_2(R)=\sum_{i<R}\prod_{\ell\mid i}\nu(\ell)/(\ell-\nu(\ell))$ over squarefree supported $i$ (with $R=R_J$). The unrestricted quadratic expectation is $1/G_2(R)$. On multiples of $q$ the model expectation of the nonnegative square is at most $q/((q-1)G_2(R))$: if $q<R$ condition on avoiding its single bad class, and if $q\ge R$ no change is needed. Independence of the other prime indicators follows from CRT.

Here one can lower-bound the denominator without a variance approximation. For a doubled prime set $g_1(\ell)=1/(\ell-1)$, $g_2(\ell)=2/(\ell-2)$, and expand $g_2=g_1+h$ with $h(\ell)=\ell/((\ell-1)(\ell-2))$. Let $G_{1,d}(s)=\sum_{i<s,\,(i,d)=1}\mu^2(i)/\varphi(i)=(\varphi(d)/d)\log s+O_d(1)$ for $s\ge1$; see [the one-root sum](FiveFactorSwitchLimit.md#an-upper-bound-on-the-selberg-denominator). For $s\le1$ put it equal to zero. For squarefree $(j,d)=1$,
$G_{1,dj}(s)\ge(\varphi(j)/j)G_{1,d}(s)$ by splitting off all factors of $j$ and relaxing the cutoff. Expanding $G_2(R)$ according to those primes assigned to $h$ therefore gives
$$ V(z)G_2(R)\ge \mathbf E\,G_{1,d}(R/L)
\ge \frac{\varphi(d)}d\bigl(\log R-\log z\bigr)-O_d(1). $$
Here $L$ is the product of independently chosen odd primes $\ell<z$ outside $d$ with inclusion probabilities $1/(\ell-1)$: the unnormalized weights are $h(\ell)(1-1/\ell)=1/(\ell-2)$. The prime Mertens estimate gives $\mathbf E\log L=\log z+O_d(1)$. Even when $L\ge R$, the logarithmic lower bound is valid because its right-hand side is then nonpositive up to the fixed error.

With $t=\log q/\log D$ this bounds the leading penalty coefficient, relative to $YV(z)K/q$, by $24e^{-\gamma}/(41/10-t)+o(1)$, uniformly over all blocks. Indeed $\log R-\log z=(41/10-t)(\log D)/2+o(\log X)$; replacing $q$ by the block endpoint costs $O(1)$ here. Use $24e^{-\gamma}<27/2$, $A=41/10$, $a_0=7/9$. The aggregated leading coefficient is at most
$$
I=\frac{27}{2A}\left[\log(2/a_0)+(A/2-1)\log\frac{A-2}{A-a_0}\right]
=1.523953\ldots .
$$
This is the integral of $(27/2)(1-t/2)/(t(A-t))$ over $[a_0,2]$. After the ordinary small-prime penalty the available coefficient is $\lambda\log3-\log(28/9)-\tfrac12\log(27/8)$. The difference from $I$ is strictly greater than $1/60$ by [rational arithmetic](CheckEvenTargetSieve.py). The sign budget $\lambda+6u=5.99<6$ excludes squarefree partners with six or more factors from positive weight.

**Only a band of moduli remains.** The contribution of all $n\le H/(Q\log^{12}X)$ in $\mathcal E$ is $o(YV(z))$ in absolute value. CRT gives $|e_{n,q}|\le\nu(n)$, and $\sum_{n\le T}3^{\omega(n)}\nu(n)\ll T(1+\log T)^5$ on squarefree support by the sixfold divisor function. There are $O(Q)$ possible $q$ per block and $O(\log X)$ blocks. Thus the following is a sufficient open input:
$$
\mathcal E_{\rm band}\le (1/60+o(1))\,YV(z)K,\qquad
\frac{H}{Q\log^{12}X}<n<R_J^2=\frac{H X^{1/10}}{Q}.
$$
It already suffices to establish this one-sided bound *on average over the exceptional markers at each fixed center and fixed admissible class*, since all the other bounds are uniform and marked counts can be averaged. It would give $G_5\gg_d\mathfrak S_d(N)H/\log^2X$ for those centers and classes where it holds asymptotically. This is a target for cancellation between signed terms with $H/\log^{12}X<qn<2HX^{1/10}$. We have evaluated the main term and disposed of the smaller products. No saving in the unresolved band, or positive lower bound for two genuine primes, follows from these calculations.

The average has an explicit deterministic form. The coefficients $C_J(n)$ depend only on the numbers of bad residues. In the observed count defining $e_{n,q}$ write the indicator of $\Omega_n$ as the product of its local indicators. At each odd $\ell\mid(n,N)$ below $z$, replace the local indicator by $\mathbf1_{\ell\mid a}+\mathbf1_{\ell\nmid a}/(\ell-1)$. Indeed the first bad residue is zero, and the second is uniform among units. Keep all other local indicators. Independence gives exactly the averaged discrepancy, with the same main term $H\nu(n)/(dqn)$. Thus attempting the remaining estimate requires no search over auxiliary choices.

## Unconditional five-factor bound at $\theta=17/25$

Set $\delta=9/50$, $D=X^\delta/(d\log^B X)$, $z=D^{1/4}$, $u=5/8$, $\lambda=63/25$, and $y=D^{8/5}$. Split at $D^{4/5}$. The sign budget has strict slack:
$$6-\lambda-u/\delta=7/900.$$
For a squarefree survivor with six or more prime factors the weight is therefore nonpositive for all sufficiently large $X$. The starting lower main term remains $YV(z)K\log3$; the small-$q$ upper coefficient before division by $\lambda$ is
$$J_{\rm small}=\log(16/5)+\tfrac38\log(15/4).$$
These formulas use Cai–Lu at $\theta=17/25>3/5$ and the same marked residues as above.

In each dyadic block of large divisors take $R_J^2=H/(Q\log^{12}X)$. Now **all** the grouped rounding errors are in the range already bounded in absolute value. This radius satisfies $R_J>z$ by a fixed power throughout the range. The two-root denominator estimate and the conditioning bound hold unchanged. Writing $A=\theta/\delta-1/2=59/18$, the normalized coefficient per prime is at most $4e^{-\gamma}/(\delta(A-t))+o(1)$ since $\log R_J-\log z=\frac12(A-t)\log D+o(\log X)$. We have $4e^{-\gamma}/\delta<25/2$. Integration for $4/5\le t<8/5$ gives an upper coefficient
$$
I_{\rm large}=\frac{25}{2A}\left[\log 2+(5A/8-1)\log\frac{A-8/5}{A-4/5}\right].
$$
The [rational checker](CheckEvenTargetSieve.py) verifies $\lambda\log3-J_{\rm small}-I_{\rm large}>1/40$ (approximately $0.02549$). The square deletion still costs $O(H/z+\sqrt X)=o(YV(z))$. This proves the marked five-factor bound for every tuple. Averaging over exceptional markers gives the displayed $\mathfrak S_d(N)$ uniformly for every sufficiently large even target. No averaged-error hypothesis from the $2/3$ window is used in this wider-window argument.
