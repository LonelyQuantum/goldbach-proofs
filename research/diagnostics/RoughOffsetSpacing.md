# Spacing of sifted offsets at a prescribed Goldbach target

Let $N=2Y$, $L=\log Y$, $H=\lfloor Y^{2/3}\rfloor$, $T=\lfloor Y^{21/40}\rfloor$, $I=(2T,H]\cap\mathbb Z$, and $h=|I|$. For a positive integer $t$ put
$$
 F(t)=\prod_{\substack{p\mid t\\p>2}}\frac{p-1}{p-2},\qquad
 \Delta=\frac{L^2}{F(N)},\qquad K=\frac{h}{\Delta}.
$$
All products indexed by $p$ are over primes. Fix $z=(2Y)^{1/40}$. Let $R$ consist of $x\in I$ for which neither $Y+x$ nor $Y-x$ is divisible by a prime at most $z$. Mark $x\in R$ with a plus when $Y+x$ is prime and with a minus when $Y-x$ is prime. A doubly marked site is exactly an unordered central Goldbach pair in the trimmed window. Write $r$ for their number.

The [preceding bin calculation](NeighborPairLags.md) counted two prime anchors at nearby offsets. Testing both reflected integers for small prime divisors yields a bin certificate with a uniform error estimate. At every sufficiently large center and every admissible spacing, one may prescribe any one of four endpoints to be prime and obtain lower and upper counts of the same order. A thinning of the actual primes preserves this order simultaneously at every admissible spacing while removing all central representations. The arguments use unconditional estimates.

## Bounds from three counts in each bin

Partition $I$ into consecutive bins of at most $b$ integers. In bin $Q$ let $s_Q$ count all sites of $R$, and let $u_Q,v_Q$ count plus and minus marks separately. None of these three definitions requires testing two numbers at the same site for simultaneous primality. The individual prime marks can also be read from the two unions of neighboring prime-pair lists in the [endpoint cover](ThreeSquareEndpointCover.md), since all sites of $R$ are eligible for that result.

For every sufficiently large integer $Y$ and every integer $1\le b\le h$,
$$
 B_-=\sum_Q(u_Q+v_Q-s_Q)_+\ \le r\le\
 B_+=\sum_Q\min(u_Q,v_Q),\qquad
 B_+-B_-\ll K\,\frac{b+(\log L)^3}{\Delta}.                    \tag{1}
$$
In particular $b=\lfloor\Delta/\log L\rfloor$ gives an interval of width $O(K/\log L)$. A bin containing more prime endpoints than sifted sites certifies a representation. If $r\ge aK$ for a fixed $a>0$, these two bounds determine $r$ to relative error $O_a(1/\log L)$. A lone representation can fall within the uncertainty of (1).

For the exact bookkeeping in one bin let $i,j,k,c$ be its counts of double marks, plus-only marks, minus-only marks and unmarked sifted sites. The lower bound misses precisely $\min(i,c)$ double marks. The upper exceeds $i$ by $\min(j,k)$. These two errors sum to at most $ic+jk$, using disjoint types of unordered pairs of distinct sites in the bin. Consequently the total width in (1) is at most $C(b)$, the number of $x<y$ in $R$ with $y-x\le b$. With the three counts alone the displayed binwise endpoints are both attainable by assignments of marks to $s_Q$ sites. This combinatorial observation does not impose primality on those assignments.

## Sifting two distinct offsets together

For $1\le d\le b$ the four roots at prime $p$ in the variable $x$ are $Y,-Y,Y-d,-Y-d$. Write $\nu_p$ for their number of distinct residues. There are six potential pairwise equalities, giving
$$
 4-\nu_p\ \le\
 e_p=2\,1_{p\mid N}+2\,1_{p\mid d}+1_{p\mid N-d}+1_{p\mid N+d}.
$$
If $p$ divides both $N$ and $d$ all four roots coincide. The deficit is three while the right side is six, which is sufficient for an upper bound. The restriction $0<d\le h=o(Y)$ excludes coincidences over the integers.

Here are details of the uniform sieve bound. Omit $p\le5$. Use a Selberg square of radius $Z=h^{1/40}$ on the interval for $x$, and sieve primes $7\le p<w=Z^{1/16}<z$. The full divisor sum in its denominator is $\prod_{7\le p<w}(1-\nu_p/p)^{-1}$. Under the corresponding normalized squarefree-divisor weights, the expectation of $\log d'$ is $\sum_{7\le p<w}(\nu_p/p)\log p\le(4+o(1))\log w$. Markov's inequality retains at least half the denominator on $d'\le Z$. Each CRT rounding error for the least common multiple $m$ of two sieve divisors is $O(4^{\omega(m)})$. The crude bounds $|\lambda_{d'}|\le d'$ on the Selberg coefficients and $4^{\omega(m)}\le m^2$ give total error $O(Z^8)$. Thus the upper count is $\ll h\prod_{7\le p<w}(1-\nu_p/p)+O(Z^8)$. [Selberg square used in this project](CentralPrimePairsNearOneCenter.md#removing-a-central-coefficient-while-preserving-short-interval-counts) · [Green and Tao on the Selberg sieve for prime tuples](https://doi.org/10.5802/jtnb.538)

The base product $\prod_{7\le p<w}(1-4/p)$ is $\asymp L^{-4}$ by Mertens' theorem. At each prime its correction is $1+(4-\nu_p)/(p-4)$. With $f_p=(p-1)/(p-2)$ this is at most $(1+20/p^2)f_p^{e_p}$ for $p\ge7$, by $f_p^{e_p}\ge1+(4-\nu_p)/(p-2)$ and $4-\nu_p\le3$. Restoring the finitely many omitted factors on the upper-bound side is harmless. We obtain
$$
 \#\{x:x,x+d\in R\}\ll \frac{h}{L^4}
            F(N)^2 F(d)^2 F(N-d)F(N+d).                        \tag{2}
$$
For the one-site bound, the same argument with the two roots $\pm Y$ gives $|R|\ll K$.

To sum (2), the sixth moment $\sum_{1\le d\le b}F(d)^6$ is $O(b)$. Expand in nonnegative odd squarefree divisor weights $g_j$ defined by $g_j(p)=f_p^j-1$. The number of multiples of a divisor $m$ in $[1,b]$ is at most $b/m$, and $\prod_{p>2}(1+g_6(p)/p)$ converges. For $t=N\pm d$ the part of $F(t)^3$ from $p>L$ is $O(1)$ uniformly, since at most $O(L/\log L)$ such primes divide $t$. The truncated expansion now counts at most $b/m+1$ multiples. Its rounding contribution is at most $\prod_{2<p\le L}(1+g_3(p))\ll(\log L)^3$, while $\sum_m g_3(m)/m=O(1)$. Hölder with exponents $3,3,3$ bounds the sum of the last three factors of (2) by $O(b^{1/3}(b+(\log L)^3)^{2/3})$. In particular
$$
 C(b)\ll K\,\frac{b+(\log L)^3}{\Delta}.                        \tag{3}
$$
Also $F(N)\ll\log L$ by the same small- and large-prime split, so $(\log L)^3=o(\Delta)$ uniformly. This proves (1).

## A positive count at each admissible spacing

Suppose $1\le d\le h/2$. For $x,x+d\in R$ list the endpoints in order as $Y+x,Y-x,Y+x+d,Y-x-d$. Fix an index $j$ before counting. Let $P_j(d)$ count the $x$ for which endpoint $j$ is prime and each of the other three is squarefree with at most 39 prime factors. The local admissibility conditions are $2\mid d$ and either $3\mid N$ or $3\mid d$. When they fail, $P_j(d)=0$. When they hold,
$$
 P_j(d)\asymp \frac{h}{L^4}\mathcal F(N,d),\qquad
 \mathcal F(N,d)=
 \frac{F(N)^2 F(d)^2 F(N-d) F(N+d)}{F(\gcd(N,d))^3}.             \tag{4}
$$
The constants are absolute for all sufficiently large $Y$, all these $d$, and each of the four choices of $j$. In particular $d=6$ works for every $Y$. If $3\mid Y$, even $d=2$ works. The four separate counts may have different witnesses.

To verify admissibility, at 2 the roots occupy both residues exactly when $d$ is odd. At 3, if $3\nmid N$, the roots $\pm Y$ occupy two residues and their translate by nonzero $-d$ adds the third. If $3\mid N$ there are at most two roots. At $p\ge5$ the four roots cannot cover the field. For odd primes the exact deficit is
$$
4-\nu_p=e_p-3\,1_{p\mid\gcd(N,d)} .
$$
Indeed there is one quadruple coincidence when $p\mid\gcd(N,d)$, two disjoint double coincidences when $p$ divides just one of $N,d$, and at most one double coincidence otherwise.

Use the chosen endpoint $t$ as the variable on an interval of $m=h-d\asymp h$ integers at height $Y+O(H)$. Its coefficient of $x$ is a unit at every prime. The root for $t$ is now zero, leaving exactly $\rho_p=\nu_p-1$ nonzero classes for the three companions. For instance, for $t=Y+x$ the classes come from $N,-d,N-d$ after removing duplicates and zero. Their density within primes is $g(p)=\rho_p/(p-1)$. Thus the product for the sieve on the log-weighted primes is
$$
 V_3(z)=\prod_{p\le z}(1-g(p))
       =\prod_{p\le z}\frac{1-\nu_p/p}{1-1/p}.
$$
Put $Q=Y^\delta$ with $\delta=1/6-1/4000$. For the single interval of prime arguments let $e_q$ be the largest absolute error over unit classes mod $q$ relative to $m/\varphi(q)$. Timofeev's short-interval theorem gives $\sum_{q\le Q}e_q\ll_A h/L^A$ for every fixed $A$. Its fixed-interval range includes $m\gg Y^{3/5}L^{2A+129}$ and $Q\ll m/(\sqrt{Y}L^{A+64})$. For squarefree $q$ the CRT uses at most $3^{\omega(q)}$ unit classes. For any fixed $c\ge1$, Cauchy–Schwarz gives the same arbitrary logarithmic saving for $\sum_{q\le Q}c^{\omega(q)} e_q$. Indeed $e_q\ll hL^2/q$ by counting integers and $\sum_{q\le Q} c^{2\omega(q)}/q\ll_c L^{O_c(1)}$ by an Euler product. This covers the fixed divisor weights in the sieve remainder. [Timofeev's theorem](https://doi.org/10.1070/IM1988v030n02ABEH001013) · [Log-weighted formulation and range in Koukoulopoulos, (1.1)](https://arxiv.org/pdf/1405.6592v2#page=1)

On admissible spacings $g(p)<1$. The dimension-three product condition holds uniformly: the inverse product of $1-g(p)$ on $w\le p<u$ is at most $(\log u/\log w)^3(1+O(1/\log w))$ by $\rho_p\le3$ and Mertens' theorem, treating $p\le5$ directly. The Diamond–Halberstam–Richert lower sieve has $f_3(s)>0$ for $s>\beta_3$, with $\beta_3<6.641$. Here $\log Q/\log z\longrightarrow 1997/300>6.65$. Hence the lower sieve gives $\gg mV_3(z)$ in prime logarithmic weight, and the upper sieve gives $\ll mV_3(z)$. Division by the prime logarithms costs a factor $\asymp L$. [Diamond and Halberstam, Theorem 9.1](https://doi.org/10.1017/CBO9780511542909) · [Liu and Sarnak, (6.17)](https://web.math.princeton.edu/sarnak/few-final.pdf#page=27)

For $p\ge7$, the local ratio $(1-\nu_p/p)/(1-4/p)$ equals $f_p^{4-\nu_p}(1+O(p^{-2}))$, uniformly in $\nu_p$. The product of the base factors $(1-4/p)/(1-1/p)$ is $\asymp L^{-3}$. The small admissible factors are bounded above and below, and only $O(1)$ primes larger than $z$ divide $Nd(N-d)(N+d)$. The exact deficit therefore gives $V_3(z)\asymp L^{-3}\mathcal F(N,d)$. In particular $\mathcal F(N,d)\ge F(N)^2$, since the deficit at each odd $p\mid N$ is at least two. Each surviving companion is $<2Y=z^{40}$ and all its prime factors exceed $z$, so it has at most 39 factors counted with multiplicity. Repeated prime factors in any of the three cost $O(\sum_{z<n\le\sqrt{2Y}}(h/n^2+1))=O(h/z+\sqrt Y)=o(h/L^4)$ sites per companion. This proves (4).

Summing (4) over multiples of six up to $\min(b,h/2)$ gives $C(b)\gg Kb/\Delta$ throughout $6\le b\le h$, even when the same one of four endpoint positions must carry a prime and the other three must be squarefree. The lower and upper bounds (3) have matching orders for $b\ge(\log L)^3$. At bounded $b$ the arithmetic factors in (4) retain information about the particular $N$.

## Which spacing conclusions hold for genuine primes?

The earlier [central five-factor deduction](CentralFiveAtTwoThirds.md) gives $\gg K$ offsets with a genuine upper prime and a squarefree lower partner having at most five prime factors, all at least $Y^{1/36-o(1)}>z$. Taking out the first $2T=o(K)$ offsets preserves the bound. This is a prior project deduction using, among other inputs, Cai–Lu's progression estimate. Their published short-interval Chen theorem has a different window. Thus $|R|\asymp K$ at every sufficiently large $Y$. [Cai and Lu, Acta Arithmetica 91 (1999)](https://doi.org/10.4064/aa-91-4-311-323)

For any subset $E\subset R$ of size $s\ge aK$ with fixed $a>0$, and any fixed $0<\epsilon<1$, there are constants $c_{a,\epsilon},C_{a,\epsilon}>0$ such that at least $(1-\epsilon)(s-1)$ **consecutive gaps** in the increasing ordering of $E$ lie in $[c_{a,\epsilon}\Delta,C_{a,\epsilon}\Delta]$. Small gaps are bounded by (3) at $b=\lceil c_{a,\epsilon}\Delta\rceil$. Gaps greater than $M\Delta$ number at most $h/(M\Delta)=K/M$ by telescoping. Choose $c_{a,\epsilon}$ small and $M$ large, then take $Y$ sufficiently large. Moreover, at $b=\lfloor\Delta/\log L\rfloor$ only $O(K/\log L)$ sites of the **whole** $R$ have a different sifted site within distance $b$, by twice (3).

This applies to the prime-plus-at-most-five-factor family at every large target. It applies to the genuine two-prime family at each target with $r\ge aK$. In particular, by [the local packet estimate (1) at modulus one](CentralPrimePairPacket.md), this holds for all but $O_{A,\eta}(X^\eta/\log^A X)$ centers in every packet $[X,X+X^\eta)$ with fixed $5/8<\eta<2/3$ and fixed $A>0$. Indeed the singular series is $2C_2F(2Y)$ with $C_2$ the twin-prime constant, both prime logarithms are $(1+o(1))L$, and the trim contributes $O(TL^2)$. The preceding conclusion concerns the bulk of the gaps in a central window. Akeno's preprint studies the **smallest** gap between Goldbach primes over a wider summand range for almost all even targets. [Akeno, arXiv:2508.02769v3, Theorem 1.2 and Lemma 4.3](https://arxiv.org/abs/2508.02769v3)

There is also a lower bound showing the scale of (3). Use blocks of length $b$ and one possible final shorter block, so their number $m\le2h/b$. With $s_Q=|E\cap Q|$, same-block pairs number at least $(s^2/m-s)/2$ by Cauchy–Schwarz. For $b\ge 4\Delta/a$ this is $\gg_a Kb/\Delta$. Thus simply bounding **all** close sifted pairs cannot give $o(K)$ throughout this range, already for the prime-plus-at-most-five-factor set. This lower bound counts two sites of the same set. It gives no positive lower bound for two different prime marks at the same site.

## A limit of off-zero observations after sifting

At $b=\lfloor\Delta/\log L\rfloor$, let $t$ be the number of genuine double marks isolated from every other point of $R$ at distance at most $b$. Then $r-t=O(K/\log L)$. On the two copies $Y+I$ and $Y-I$ one can choose two equally large subsets of the actual primes giving **identical** products of any two signed prime marks at any distinct sifted offsets of distance at most $b$. They have identical one-sided marked totals as well. Their central counts are $0$ and $\lfloor t/2\rfloor$.

Choose $2\lfloor t/2\rfloor$ isolated double sites. In the first subset, retain just the upper prime on half and just the lower prime on the others. In the second subset retain both primes on the first half and neither on the others. Treat every other site identically, keeping only one endpoint at remaining double sites and retaining all primes elsewhere. Each subset deletes exactly $r$ primes. Any changed mark is on an isolated sifted site, so its product with a mark at any other sifted site in range is identically zero in both subsets. This assertion uses the original small-divisor test and the two signed marks; it does not assert equality of all four-prime neighboring-list statistics or of the separate counts in every small bin. For rare representations the error bound on $r-t$ permits $t=0$.

Even the positive lower bounds (4) at **all** spacings are compatible, up to absolute constants, with zero central pairs in a subset of the primes. At every original double site independently erase one of its two prime marks, with equal probabilities. Keep all other marks, all small-divisor tests and all integer squarefreeness tests. For a fixed $(d,j)$, each of its $P_j(d)$ witnesses asks to retain just one prime. As $x$ varies these marks belong to distinct sites for that fixed $j$, so their survival indicators are independent and have expectations at least $1/2$. A Chernoff bound shows that the probability of retaining fewer than $P_j(d)/3$ witnesses is at most $\exp(-cP_j(d))$ for an absolute $c>0$. Equation (4) gives $P_j(d)\gg h/L^4$ uniformly. A union bound over at most $4h$ tests gives a single subset retaining at least one third of every admissible count for all sufficiently large $Y$. The sum of the two marks at each site is now at most one. The argument preserves the order of each single-prime count. It does not assert that this subset reproduces the distribution of primes in progressions.

For a prescribed target the remaining task is to force $u_Q+v_Q>s_Q$ in some bin or to prove a lower bound involving two opposite prime marks at the same offset. Two prime marks in the four displayed positions could otherwise witness a difference $d$ or a neighboring sum $2Y\pm d$.

At $Y=1009^2$ a finite check with the illustrative cutoff 29 finds 239 sifted offsets and 52 actual pairs in the trimmed window. Bins of width 16 give $49\le r\le54$. At spacing six the four anchor counts are $(5,9,12,5)$. A subset with no surviving central pairs gives $(3,8,11,3)$ on exactly the same sifted tuples. The program also enumerates 3,187 local residue tests and 204 finite families of bin marginals. The finite cutoff is independent of the asymptotic choice of $z$. [Reproducible finite checks](CheckRoughOffsetSpacing.py)
