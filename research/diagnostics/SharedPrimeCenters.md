# Nearby Goldbach centers with many common prime summands

Fix an integer $r\ge2$. For every sufficiently large integer $s$ put $H=\lfloor s^{2/3}\rfloor$, $T=\lfloor s^{21/40}\rfloor$, $L=\log s$ and $I=[s-H+T,s)\cap\mathbb Z$. For a set $J\subset\{1,\ldots,T\}$ define
$$
N(J)=\#\{a\in I:\ a\text{ and all }2(s+j)-a,\ j\in J,\text{ are prime}\}.
$$
Every counted $a$ gives a positive-offset central representation at **each** $s+j$. In fact $1\le s+j-a\le H\le H_{s+j}$. The centers can share many of the same lower primes. The following are deductions from published prime-distribution estimates.

* Divide $[1,T]\cap\mathbb Z$ into consecutive blocks of $W=\lceil100rL\rceil$ shifts, dropping the last incomplete block. Of all $r$-element subsets of individual blocks, a proportion $\gg_r1$ satisfy $N(J)\gg_r H/L^{r+1}$.
* There are constants $D_r,k_r$ and an $r$-set $J\subset[1,T]$ of diameter at most $D_r$ such that $N(J)\gg_r H/L^{k_r+1}$. Both constants are independent of $s$. The distance from $s$ to this cluster can be as large as $T$.

These statements allow $s=p^2$ for any sufficiently large prime $p$. At that exact center one can also keep a rough, squarefree five-almost-prime as a partner of the same prime shared by the nearby centers. This last deduction uses the earlier paper-stage five-factor estimate. Whether the particular center $s$ has a central representation by two primes remains open.

## Clusters on a logarithmic scale

Write $b=2s-a$ for a lower prime $a\in I$. Every prime in $(b,b+2T]$ has the form $b+2j$ for a unique $1\le j\le T$. The quantitative Baker–Harman–Pintz bound gives at least $T/(20L)$ such shifts, uniformly in $a$: the interval contains $(b,b+b^{21/40}]$, with $b/s\to1$ uniformly. The short-interval PNT gives $\#(I\cap\mathbb P)\sim H/L$ since $H=s^{2/3}+O(1)$ and deleting the end strip costs at most $T=o(H/L)$. [Baker–Harman–Pintz, p. 562](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/BakerHarmanPintz.pdf#page=31) · [Short-interval PNT and ranges](https://arxiv.org/pdf/2505.24017)

For each $a$, discard the final strip of at most $W$ shifts and blocks containing fewer than $r$ eligible shifts. These cost at most $W+(r-1)T/W$, leaving $\gg T/L$ eligible shifts. A block with $d\ge r$ eligible shifts contributes $\binom dr\ge d/r$ tuples. Summing this count first over blocks and then over lower primes gives $\sum_J N(J)\gg_r HT/L^2$. The number of tuples under consideration is $M=\lfloor T/W\rfloor\binom Wr\asymp_r TW^{r-1}$. Hence the mean of $N(J)$ is $\gg_r H/L^{r+1}$.

To obtain a positive proportion, put $k=r+1$. The $k$ forms in $a$ have roots $0$ and $2(s+j)$, $j\in J$. The interval upper sieve gives
$$
 N(J)\ll_r \frac{H}{L^k}\prod_{j\in J}F(s+j)
                 \prod_{i<j,\ i,j\in J}F(j-i),\qquad
 F(n)=\prod_{\substack{\ell\mid n\\\ell>2k}}(1+2k/\ell),
$$
where $\ell$ runs over primes. Here is one uniform choice in the Selberg-square proof of the [preceding note](CentralPrimePairsNearOneCenter.md). Take $R=H^{1/(20(k+2))}$, $z=R^{1/(4k)}$ and write $\nu_\ell$ for the number of distinct roots. The independent divisor law has mean log divisor at most $(1/4+o(1))\log R$, so its mass up to $R$ is bounded below. For admissible forms the minimizing coefficients satisfy $|\lambda_d|\le d$. The CRT rounding error is at most $O(R^{4+2k})$ using $\nu([d,e])\le [d,e]^k$ for $d,e\le R$. All prime values counted here exceed $z$. A local obstruction gives no solutions. For $\ell>2k$ a collision can increase the generic product factor $1-k/\ell$ by a ratio at most $1+2k/\ell$. Such a prime must divide $s+j$ or $j-i$. The remaining product contributes $O_k(L^{-k})$ by Mertens.

Every fixed moment of each displayed $F$ factor is bounded on average over the $M$ tuples. For $F(s+j)$, fixing the value of an ordered coordinate of the sorted tuple leaves $O_r(W^{r-1})$ choices. For $F(j-i)$, fixing a positive difference $d<W$ leaves $O_r(TW^{r-2})$ choices. To check the resulting one-variable averages, expand $F(n)^v=\sum_{m\mid n}g_v(m)$ with nonnegative squarefree-supported coefficients $g_v(\ell)=O_{k,v}(1/\ell)$. For $1\le n\le W$ the average is at most $\sum_m g_v(m)/m<\infty$. On $s<n\le s+T$ the additional rounding cost is $O_{k,v}((\log s)^{O_{k,v}(1)}/T)=o(1)$. Hölder with as many factors as appear in the product therefore gives $M^{-1}\sum_J N(J)^2\ll_r H^2/L^{2k}$. Cauchy–Schwarz above half the lower mean proves the proportion claim.

## Clusters of fixed diameter

Apply Alweiss–Luo, Theorem 1.1, with $\delta=21/40$ and a fixed admissible tuple $n+iP$, $0\le i<k$, where $P$ is the product of the primes up to $k$. For primes at most $k$ the roots coincide, and for larger primes there are fewer roots than residues. Choose $k=k_r$ large enough for their lower bound $c_\delta\log k$ to be at least $r$. Set $D=(k-1)P$. For any lower prime $a\in I$ apply their theorem on the integer interval $[b+2,b+2T-D]$, $b=2s-a$. Its length is $(2+o(1))T$, greater than the $\delta$-th power of its right endpoint for all sufficiently large $s$. There are $\gg_r T/L^k$ values of $n$ which supply at least $r$ primes in $[n,n+D]$. [Alweiss–Luo, Theorem 1.1, pp. 3–4](https://arxiv.org/pdf/1707.05437#page=4) · [Published article](https://link.springer.com/article/10.1007/s40993-018-0109-y)

Select the least $r$ prime values in each qualifying tuple and convert them to shifts via $j=(q-b)/2$. Their diameter is at most $D/2$. For fixed $a,J$, the smallest selected $q$ can play at most $k$ roles $q=n+iP$, so at most $k$ choices of $n$ give this incidence. Summing over $a$ gives $\gg_r HT/L^{k+1}$ distinct incidences $(a,J)$. There are only $O_r(T)$ possible $r$-sets of bounded diameter. Averaging proves the second claim. The minorant in Alweiss–Luo does not prescribe which $r$ of the forms are prime.

## Including the prime-square center with a rough partner

Now set $s=p^2$ with $p$ prime. Keep an upper prime $a=s+h$, $2T<h\le H$, whose partner $b=2s-a$ is squarefree, has at most five prime factors, and has no prime factor below $z_0=s^{1/36}/L^{B/6}$ for a fixed sufficiently large $B$. The [$d=1$ five-factor estimate, first row](CentralFiveAtTwoThirds.md) gives $\gg H/L^2$ such $a$ after discarding at most $2T=o(H/L^2)$ sites. It is an input from this project awaiting independent review. Let $N_5(J)$ count these $a$ for which $b+2j$ is prime for every $j\in J$. Now $a$ stays the upper summand at every $s+j$ because $h-j\ge1$, and $h-j\le H\le H_{s+j}$.

The block-incidence lower bound with this set of $a$ gives $\sum_J N_5(J)\gg_r HT/L^3$. A positive proportion of the same $M$ tuples satisfy
$$
N_5(J)\gg_r H/L^{r+2}.
$$
For the second moment, include the form $2s-a$ among the sieve constraints. Its lack of prime factors below $z_0$ allows all $r+2$ forms to be sieved up to $\min(z_0,R^{1/(4(r+2))})$, whose logarithm is still comparable to $L$ for fixed $r$. Use the preceding square with $k=r+2$. The extra root $2s$ gives factors $F(s)$ and $\prod_{j\in J}F(j)$. At $s=p^2$ the first is uniformly bounded. The marginal for $j$ uses $1\le j\le T$ with $O_r(W^{r-1})$ tuples per coordinate, so the same divisor expansion bounds all its fixed moments. This proves the claimed proportion. The bounded-diameter incidence argument also applies to this set of upper primes and gives one tuple with $N_5(J)\gg_r H/L^{k_r+2}$. In all these incidences the **same** $a$ has an exact rough partner at $s$ and genuine prime partners at each of the other centers.

There is an explicit forbidden continuation for a prime square. If both original endpoints at $s=p^2$ are primes greater than 3 with $p>3$, their residues must both be 1 modulo 3. The same holds for the prime and its rough partner above once $z_0>3$. Replacing either partner $b$ by $b+2j$ can never give a prime for $j\equiv1\bmod3$. For a single nonzero shift these are precisely the local obstructions to the three forms $a,2s-a,2s+2j-a$: modulo 2 there is one root, modulo 3 the roots cover the field exactly in the indicated case, and no prime at least 5 has only three residue classes. The sieve calculation accommodates these empty tuples.

## Requiring two primes at the prescribed center

Let $R(s)$ count **all** positive-offset central prime pairs at $s$, including those lost by trimming to $I$. For each such pair $s-h,s+h$, choose the following single endpoint to share with future centers. If $h\le T$, keep $s-h$ and put $v=s+h$. If $h>T$, keep $s+h$ and put $v=s-h$. A prime $v+2j$, $1\le j\le T$, is its partner at $s+j$. In the first case the offset there is $h+j\le2T\le H$ for large $s$. In the second it is $h-j\in[1,H]$. This accounts even for the last possible pair at the boundary $h=H$.

Write $d_s(h)=\#\{1\le j\le T:v+2j\text{ is prime}\}$. The same Baker–Harman–Pintz lower bound and the elementary upper sieve on an interval of length $2T$ give $d_s(h)\asymp T/L$ uniformly. The total number of incidences of an original pair and $r$ distinct such continuations consequently satisfies
$$
A_r(s)=\sum_{h:\,s\pm h\ {\rm prime},\,1\le h\le H}\binom{d_s(h)}r
       \asymp_r R(s)(T/L)^r.
$$
There is no additive error, even if $R(s)=0$ or $1$. Thus one genuine central pair would give many such incidences, and proving $A_r(s)>0$ at the specified center is equivalent to proving $R(s)>0$. The lower bounds in the first two sections count incidences with only positive shifts.

## What the positive shifts can distinguish

First consider ordinary indicators. Delete just the upper prime of every central prime pair at $s$, and let $N_B(J)$ use the surviving primes. For fixed $|J|=r$, uniformly in all positive shifts,
$$
0\le N(J)-N_B(J)\ll_r H(\log\log s)^{C_r}/L^{r+2}.
$$
Indeed the lower prime $a<s$ survives. Losing $2s-a+2j$ requires $a-2j$ to be prime too. Its root $2j$ is distinct from $0$ and every $2(s+i)$. The upper sieve thus gains a full power of $L$; the product of nonzero root differences is $O_r(s^{O_r(1)})$, whose distinct prime divisors contribute at most $(\log\log s)^{C_r}$ by Mertens as in the preceding note. Sum over the $r$ possible lost sites. In particular all the logarithmic-block lower bounds for rich tuples survive, to smaller-order error, using a subset of the true primes.

There is an exact difference for the restricted count $N_5$. Keep its squarefree, rough integer condition on $b=2s-a$, and restrict the sites required to be primes to the surviving set. Since all $b+2j<s$, the loss is **exactly** the number of $a$ in $N_5(J)$ for which $b$ itself is prime. Controlling this difference from below for even one $J$ at a prescribed $s$ would produce a true central pair there.

There is a sharper test for the attempted inference. Write $P(n)=\mathbf1_{\mathbb P}(n)$. At this fixed $s$, independently for every actual central prime pair choose one of the assignments $(0,2)$ or $(2,0)$ with equal probabilities for its two prime indicators. Keep $P(n)$ elsewhere. Some resulting nonnegative weight $w$, supported entirely on genuine primes, gives zero at every central product $w(s-h)w(s+h)$, yet for every $J\subset[1,T]$ of size at most $r$, every integer subinterval $K\subset I$ of length $m\ge1$, and every real $\alpha$,
$$
\left|\sum_{a\in K} e^{2\pi i\alpha a}
\left[w(a)\prod_{j\in J}w(2s-a+2j)-P(a)\prod_{j\in J}P(2s-a+2j)\right]\right|
\ll_r\sqrt{m\log s}.
$$
One can simultaneously use log weights at all sites in both products at an extra cost $O_r(L^{|J|+1})$. This is a test of a specified family of multilinear statistics. The modified weight takes the value 2; the true prime indicator also satisfies the additional identity $P(n)^2=P(n)$.

For a fixed $a$ the sites in each product are distinct. The positive shifts put the upper sites strictly above $s$, and none equals the reflection $2s-a$ of the low site. Hence all nonconstant factors use different coins and their product has exactly the original expectation. At most $(r+1)m$ coins enter a sum over $K$. Flipping one coin affects at most $2(r+1)$ summands, each changing by $O_r(1)$. Apply bounded differences to the real and imaginary parts on a frequency grid of mesh at most $s^{-3}$. There are polynomially many choices of $K,J$ and grid point for fixed $r$, so a sufficiently large constant in the stated bound makes the probability of any failure less than one. Removing the phase at the left endpoint of $K$, the derivative of the centered sum has size $O_r(m^2)$; interpolation costs $O_r(m^2s^{-3})$. Deterministic logarithms multiply the coordinate differences and derivative by at most $O_r(L^{|J|+1})$. The exact-center statistic uses the same coin twice at opposite ends and is zero identically. For any genuinely present pair, a nonnegative random replacement with both site means equal to one and zero product almost surely needs a cap of at least two, since the sum of the two replacements has mean two. [McDiarmid, bounded differences](https://www.cambridge.org/core/books/abs/surveys-in-combinatorics-1989/on-the-method-of-bounded-differences/AABA597B562BDA7D89C6077E302694FB)

The same choice of coins can satisfy this error bound for the upper-endpoint counts $N_5(J)$ as well. In their sums over $s+2T<a\le s+H$, retain the deterministic integer test for roughness, squarefreeness and factor count at $2s-a$, and apply $w$ to the sites required to be primes. All the shifted sites $2s-a+2j$ now lie strictly below $s$, and none reflects to $a$. The identical expectation and bounded-differences argument works, with the two families included in one union bound. Thus even a roughness test at the exact partner, combined with fixed-order data at every collection of positive shifts, still allows the zero exact coefficient in this weighted model.

For a finite example take $s=101^2=10201$, $H=470$, $T=127$ and $J=\{83,84\}$. The upper prime $10639$ has prime partners $9929,9931$ at the two shifted centers. Its exact partner is $9763=13\cdot751$. For the same two centers the upper prime $10501$ has partners $10067,10069$, and its exact partner $9901$ is prime. The [finite checker](CheckSharedPrimeCenters.py) verifies incidence counts, both boundary cases and the expectation identity by exact enumeration. The distributional and sieve estimates above are paper arguments.
