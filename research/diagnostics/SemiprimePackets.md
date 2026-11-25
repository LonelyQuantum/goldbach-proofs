# Rough semiprimes opposite an upper prime in the central Goldbach window

For an integer center $s$, set $H_s=\lfloor s^{2/3}\rfloor$, $T_s=\lfloor s^{21/40}\rfloor$, $L_s=\log s$, and $z_s=s^{1/36}/L_s^{B/6}$ for fixed $B>0$. In the range $2T_s<h\le H_s$ write $a=s+h$ and $b=s-h$. Let $R(s)$ count pairs with both endpoints prime, and $C(s)$ count pairs with $a$ prime and $b=qt$ for distinct primes $z_s\le q<t$. The orientation matters. These two counts impose no positive shifts. Write $c=\log 35$.

1. At **every** sufficiently large integer center, the number of possible lower partners $b=qt$ before testing $a$ for primality is $(c+o(1))H_s/L_s$.
2. For fixed $1-\sqrt7/6<\theta<2/3$, let $K=\lfloor X^\theta\rfloor$, $H=H_X$, $L=\log X$. Summing over all integers $X\le s<X+K$ gives
\[
 \sum_s R(s)=(2+o(1))KH/L^2,\qquad
 \sum_s C(s)=(2c+o(1))KH/L^2 .
\]
For each fixed $0<\lambda<c$, a positive proportion of these centers satisfy $C(s)-\lambda R(s)\gg_\lambda H/L^2$ (constants can also depend on fixed $B,\theta$).
3. At an individual center, deleting the upper prime from each true central prime pair leaves its entire semiprime count unchanged. This remains exact after imposing any subset of the previous positive-shift primality tests.

These are paper deductions from prime distribution estimates. They use no five-almost-prime lower bound. Part 2 averages over consecutive integer centers, which may start at a prime square; a pointwise comparison of $C(p^2)$ and $R(p^2)$ remains open.

## Counting the lower semiprimes

Work first in $[X-H,X)$ and put $z=z_X$. For primes $z\le q\le\sqrt X$ count primes $t$ in $I_q=[(X-H)/q,X/q)$. Imposing $q<t$ changes the sum by at most $O((1+H/\sqrt X)^2)$: if $t\le q$, both factors lie between $(X-H)/\sqrt X$ and $\sqrt X$. This removes squares and duplicate orderings. Trimming a further $2T_X+O(1)$ integers costs $o(H/L)$ once each product is counted once.

We show that the prime count summed over $q$ equals
\[
 \sum_{z\le q\le\sqrt X,\ q\ {\rm prime}}\frac{H}{q\log(X/q)}+o(H/L). \tag{1}
\]
For $q\le X^{1/6}$ the interval length $H/q$ is at least a constant times $(X/q)^{3/5}$, so the uniform short-interval prime number theorem gives a relative $o(1)$ error on each positive main term. The sum of these errors is $o(H/L)$ because $\sum_{z\le q\le\sqrt X}1/q=O(1)$ over primes. [Guth–Maynard, Corollary 1.3](https://arxiv.org/pdf/2405.20552#page=3)

For the rest group the primes in dyadic blocks $Q\le q<2Q$, splitting also at the range boundaries below. Put $Y=X/Q$ and $Z=H/Q$. For a fixed $0<\sigma<1$ use
\[
 M_\sigma(y)=y^{-\sigma}\sum_{y<t\le y+y^\sigma,\ t\ {\rm prime}}\log t .
\]
On $y\asymp Y$ the measure with $|M_\sigma(y)-1|>\xi$ is $O_{\xi,\sigma,\epsilon}(Y^{\mu(\sigma)+\epsilon})$ for each fixed $\xi,\epsilon>0$ for the exponents used below. The published definition uses $\Lambda$. Proper powers contribute at most $O((y^{\sigma-1/2}+1)\log^2 y)=o(y^\sigma)$, by counting each exponent separately. We use $\mu(1/4)<1$ (monotonicity and Lemma 1.1(i)) and $\mu(\sigma)\le3(1-\sigma)/2$ only for $1/2<\sigma\le11/21$. [Gafni–Tao, Definition 1.1 and Lemma 1.1, pp. 4–5](https://arxiv.org/pdf/2505.24017#page=4)

For each $I_q$ the integral of $M_\sigma$ differs from the prime log weight by
\[
 O\bigl((Y^\sigma+1)L+Z Y^{\sigma-1}L\bigr).
\]
In fact an interior prime $t$ receives weight $\int_v^t y^{-\sigma}\,dy=1+O(Y^{\sigma-1})$, where $v+v^\sigma=t$. At either endpoint only $O(Y^\sigma+1)$ integers have their weights clipped or extended, by at most $O(1)$ each. The $I_q$ cover any point $y$ at most $1+O(H/Y)$ times since $(X-H)/y\le q\le X/y$. This is an upper bound using *all integers* $q$.

Choose $\nu$ strictly between $\max(0,\mu(1/4))$ and 1, and then $\delta>0$ small enough that $\delta<1/12$ and $(2/3+\delta)\nu<2/3$.

* For $X^{1/6}\le Q\le X^{1/3-\delta}$ use a fixed $\sigma$ strictly between $1/2$ and $\min(11/21,(1/3+\delta)/(2/3+\delta))$. Then $Y^\sigma/Z$ saves a fixed power of $X$ throughout. The overlap is bounded, and the integrated contribution of exceptional starts is $O(LY^{3/4+\epsilon})$, at most $O(LX^{(5/6)(3/4+\epsilon)})$.
* For $X^{1/3-\delta}\le Q\le\sqrt X$ take $\sigma=1/4$. Again $Y^\sigma/Z$ saves a fixed power, even at $Q=\sqrt X$. The exceptional contribution is $O(L(Y^\nu+HY^{\nu-1}))$. Here $X^{1/2}\ll Y\ll X^{2/3+\delta}$, so both terms save a fixed power against $H$.

Blocks split at an endpoint can be taken with base comparable to that endpoint. We used $M_\sigma\ll L$ on the exceptional set. The power savings absorb the $O(L)$ blocks and allow division of each prime log weight by $\log(X/q)\asymp L$. Across $I_q$, the log of any prime differs from $\log(X/q)$ by $O(H/X)$. Off the exceptional set the integrated absolute error is at most $\xi\sum_{q\ {\rm prime}}|I_q|\ll\xi H$. The sum of smoothing errors is $o(H)$ by the same prime reciprocal sum and the uniform polynomial margin $Y^\sigma/Z$. Taking $X\to\infty$ and then $\xi\downarrow0$ proves (1).

By prime partial summation with $u=\log q/L$, the right side of (1), divided by $H/L$, tends to $\int_{1/36}^{1/2}du/(u(1-u))=\log35$. The logarithmic factor in $z$ moves the lower endpoint in $u$ by $O_B(\log L/L)$. Restricting the sum to a fixed exponent band $1/36\le u_0<u_1\le1/2$ gives the same integral on that band, since all the preceding absolute error estimates restrict to a subset of the primes.

## Transposing to consecutive centers

Freeze the lower endpoint interval at $[X-H,X)$ and the roughness cutoff at $z_X$. Per center the geometric change costs $O(K+T_X+1)$ integers. The cutoff changes by $O_B(z_X K/X)=o(1)$ over the packet, so at most one possible integer prime factor crosses it. Its multiples cost $O(H/z_X+1)$ per center. Both costs are $o(H/L^2)$. For each remaining odd lower endpoint $b$, its upper primes range over $[2X-b,2X-b+2K)$; each such prime gives exactly one center. If $\theta>17/30$, the number is uniformly $(2+o(1))K/L$.

For the advertised extension choose any fixed tolerance. The [integer-start exceptional-set estimate](CentralPrimePairsNearOneCenter.md#transposing-the-sum) applies to this same interval regardless of how the lower endpoints are selected. For $1-\sqrt7/6<\theta\le17/30$ the bound $\mu(\theta)<2/3$ follows from the branch $(36\theta^2-96\theta+55)/(39-36\theta)$ and monotonicity. The two halves of length $K$ have only $O(X^{2/3-\epsilon_\theta})$ exceptional integer starts in total. A bad integer start gives a full unit interval of bad real starts at half tolerance since all the starts here differ from $X$ by $O(H+K)$ and the variable interval length differs from $K$ by $O(1+KH/X)$. Even the trivial $O(K)$ prime count on every bad start costs $o(KH/L^2)$. On good starts apply the relative tolerance and then send it to zero. The number of lower prime endpoints is $(1+o(1))H/L$, and (1) gives the lower semiprime count. This yields both constants in part 2.

For the positive proportion, the two-form square upper sieve on $t,2s-qt$ gives $C(s)\ll F(s)H/L^2$, $F(s)=\prod_{\ell\mid s,\ell>4}(1+4/\ell)$ over primes. Indeed $q\ge z_s$, $q\le\sqrt s$, and the fixed-divisor proof sieves strictly below $q$ in an interval of length $\gg s^{1/6}$. Its only large collision primes divide $s$, even for composite centers. Sum $1/q$ over the permitted range. The expansion of $F(s)^2$ into nonnegative squarefree divisor coefficients $g(d)$ has $g(\ell)=O(1/\ell)$, $\sum g(d)/d<\infty$ and $\sum_{d\le2X}g(d)\ll L^{O(1)}$. It gives $\sum_s F(s)^2\ll K$. The mean of $C-\lambda R$ is $(2(c-\lambda)+o(1))H/L^2$. On the set where it exceeds $(c-\lambda)H/L^2$, its positive part has total $\gg_\lambda KH/L^2$ and is bounded above by $C$. Cauchy–Schwarz gives $\gg_\lambda K$ such centers. [Fixed-divisor square and CRT error](SharedPartnerFactorRanges.md)

## What remains at one center

Write $P$ for the prime indicator and $E_s$ for the indicator of rough squarefree semiprimes just defined. Over odd lower endpoints $b$ in the trimmed interval, part 1 gives $\sum_b(E_s(b)-cP(b))=o(H_s/L_s)$. Consequently
\[
 C(s)-cR(s)=\sum_b\big(P(2s-b)-2/L_s\big)\big(E_s(b)-cP(b)\big)+o(H_s/L_s^2).
\]
This exposes the signed reflection correlation left after the two marginal densities have been accounted for. For a positivity test with no asymptotic remainder, replace $c$ by $c_s=(\sum_b E_s(b))/(\sum_b P(b))$; then $c_s\to c$ and the identity is exact. If the signed sum with $c_s$ is strictly less than $C(s)$, then $R(s)>0$.

There is an exact limitation of the semiprime data. Delete from the primes only $s+h$ from each genuine pair $s\pm h$, $1\le h\le H_s$. At $s$ every surviving semiprime candidate uses an upper prime that could not have been deleted, because its reflection $qt$ is composite. Its factors are below $s$. For any $J\subset[1,T_s]$ all of the optional shifted partner sites $b+2j$ are also below $s$ since $h>2T_s$. Thus every semiprime count, even separately for every least factor and every $J$, is exactly preserved while the true central-prime count becomes zero. Here a semiprime made from the retained set means a product of two distinct retained primes. This subset test and the packet theorem leave open an estimate for the true prime indicator at a prescribed square. [Exact finite checks](CheckSemiprimePackets.py)
