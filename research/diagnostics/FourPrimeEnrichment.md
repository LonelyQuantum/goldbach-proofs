# True lower primes opposite four factors: local means and three prescribed squares

For an integer center $x$, put $L_x=\log x$, $H_x=\lfloor x^{2/3}\rfloor$, $T_x=\lfloor x^{21/40}\rfloor$ and $s=67/400$. Let $E_x$ consist of the integers $a$ in $(x+2T_x,x+H_x]$ with exactly four prime factors counted with multiplicity, all in $(x^s,x^{2/5}]$. Write $M_x=|E_x|$ and $P_x=\#\{a\in E_x:2x-a\ {\rm prime}\}$. Define

$$
B_x=L_x P_x/M_x,\quad
S(x)=\prod_{\substack{\ell\mid x\\\ell>2\ {\rm prime}}}\frac{\ell-1}{\ell-2},
\quad C_2=\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right),\quad
Z_x=\frac{B_x}{2 C_2 S(x)} .
$$

The product defining $C_2$ is over primes. $B_x$ uses **all** sites of $E_x$, so its denominator does not change at a lower sieve cutoff. The preceding [four-prime distribution estimate](FourPrimeDistribution.md) and the subtraction of the [sector with largest prime above $x^{2/5}$](FivePrimeDistribution.md) give $M_x\sim c'H_x/L_x$ and equidistribution of those sites in each fixed reduced class. Here $c'=c_4-c_4(2/5)>0$. These upper-site estimates hold at arbitrary integer centers: their proofs use the product window before imposing any condition on its reflection.

## Threshold for a missing pair at a prime square

At $x=p^2$ retain $D_{\rm else}$, $R$ and $K=2C_2 H_x/L_x^2$ from the preceding note. Thus $D_{\rm else}$ is the signed upper-composite excess after omitting the old semiprime strip and the complete four- and five-factor sectors with all primes above $x^s$. For every sufficiently large prime square, $R=0$ implies

$$
 D_{\rm else}>0.0150K\qquad\text{or}\qquad Z_x>1.225
 \quad\text{(hence in the second case }B_x>1.615\text{).} \tag{1}
$$

Indeed the previous signed inequality gives $R+D_{\rm else}+P_x-N_A(E_x)>0.0297K+o(K)$, where the lower reference has $N_A(E_x)/K\to c'$. If $R=0$ and $D_{\rm else}\le0.0150K$, then $P_x/K\ge c'+0.0147+o(1)$. To bound $c'$ sharpen the four-factor density cap on this sector. If the distinguished exponent $u_4>\beta=2/5$, its product with the other three is at most $\beta((1-\beta)/3)^3$ by AM–GM and the monotonicity of $t(1-t)^3$ for $t>1/4$. The distinguished density integral therefore gives
$$
c_4(\beta)\ge\frac{(1-\beta-3s)^3}{36\beta((1-\beta)/3)^3}.
$$
With $c_4<0.0731696$ this yields $1+0.0147/c'>1.225$. Finally $S(p^2)\to1$, $H_x\sim H_x-2T_x$, and $2C_2(1.225)>1.615$ (finite prime product to 1000 with its tail bounded in the checker). This proves (1).

## A short-block mean with genuine lower primes

Let $Y\to\infty$ through integers, $D=\lfloor Y^{3/5}\rfloor$. For **every fixed odd squarefree** $W$ (including 1) and residue $b\bmod W$,
$$
\underset{Y<x\le Y+D,\ x\equiv b\ (W)}{\operatorname{mean}} B_x
=2 C_2(W)S_W(b)+o_W(1),                                             \tag{2}
$$
where $C_2(W)=\prod_{\ell\mid W}(1-(\ell-1)^{-2})$ and $S_W(b)=\prod_{\ell\mid(W,b)}(\ell-1)/(\ell-2)$.

First freeze the upper set at $E_Y$. Moving either window endpoint costs $O(D)$ sites per center. Moving either exponent gate alters its boundary by $O(DY^{2/5-1})=O(1)$. Each of the $O(1)$ primes that can cross a gate divides at most $O(H_Y/Y^s+1)$ sites in the enlarged window. The total change is $o(H_Y/\log^A Y)$ for every fixed $A$, uniformly in $x$. The same estimate applies to the reflected prime count with the center $x$ held fixed while replacing its upper set. Thus $M_x$ may also be replaced by $M_Y$ in the mean, with $o(1)$ error after scaling.

For fixed $a\in E_Y$, as $x$ runs through the specified class, $2x-a$ runs through the class $2b-a\bmod 2W$ in $(2Y-a,2Y+2D-a]$. If that class is not reduced it has no primes there for large $Y$. Otherwise it contributes $(2+o_W(1))D/(\varphi(W)\log Y)$ primes, uniformly in $a$. This follows from the fixed-modulus short-interval prime number theorem at exponent $3/5>7/12$; proper prime powers cost $O(\sqrt Y\log^2 Y)=o(D)$ and unweighting is uniform. Use the $7/12+\epsilon$ range, with fixed $\epsilon<1/60$, rather than the separate endpoint theorem requiring logarithms at $3/5$. [Timofeev, *Distribution in the mean of arithmetic functions in short intervals in progressions*, theorem for $\Lambda$](https://www.mathnet.ru/links/20531535b2e6f2f785c1c6e5939f97d8/im1297_eng.pdf)

All upper sites are odd and coprime to $W$. Their reduced classes modulo $W$ have equal asymptotic mass. At $\ell\mid W$ the compatible fraction of the unit classes is $(\ell-2)/(\ell-1)$ if $\ell\nmid b$, and 1 otherwise. Multiply these fractions by $2W/\varphi(W)$ from dividing the preceding prime count by the number of centers, and (2) follows. For example the two limits at $W=3$ are $3/2$ for $b=1$ and $3$ for $b=0$. If $W=15015$ and $(b,W)=1$, the mean is $1.3441162109375$. Positivity and Markov's inequality then place more than $16.7\%$ of these centers below or at $B_x=1.615$ eventually.

There is a normalization which also handles unrestricted integer centers. In each of the same blocks, even after restricting to one fixed residue class of an odd squarefree $W_0$,
$$
 \operatorname{mean} Z_x=1+o_{W_0}(1),\qquad
 \liminf_{Y\to\infty}\operatorname{fraction}\{Z_x\le1.225\}\ \ge\ 9/49. \tag{3}
$$
To see this, first include $W_0$ and all odd primes through a fixed $w$ in a squarefree wheel $W$. Apply (2) on every compatible class modulo $W$ after dividing by $2C_2S_W(x)$. The result is $C_2(W)/C_2+o_W(1)$. The pointwise all-even upper sieve in the preceding note gives $B_x\ll S(x)$, using $P_x$ bounded by the rough count of the full four-factor sector and $M_x\sim c'H_x/L_x$. Thus the difference of the two normalized means is bounded by a constant times the mean of $S(x)/S_W(x)-1$. Expand this last product into nonnegative squarefree-divisor terms with weights $g(d)=\prod_{\ell\mid d}1/(\ell-2)$ and all primes above $w$. Over the unrestricted block its mean is at most
$$
 \sum_{d>1}\frac{g(d)}{d}+\frac1D\sum_{d\le2Y} g(d)
 \ll 1/w+(\log Y)^{O(1)}/D .
$$
The first estimate follows by the Euler product and $\sum_{k>w} k^{-2}\ll1/w$; the second follows from the product of $1+1/(\ell-2)$ up to $2Y$. Restricting to the fixed original class costs at most a factor $O(W_0)$. Let $Y\to\infty$ first and then $w\to\infty$. Nonnegativity gives the second claim by Markov, since $1-1/1.225=9/49$. An interval mean over integer centers, including those in a square-compatible congruence class, does not control a prescribed prime square. Also the counted upper sites here have four prime factors.

## Uniform finite sampling

The experiment draws sites of $E_x$ with replacement. For sorted primes $q\le r\le t\le u$ set $m=qrt$, and write the upper window as $(l,h]$. Draw from dyadic boxes of eligible primes in the first three slots. In a box with minima $q_0,r_0,t_0$ use $J=1+\lfloor(h-l)/(q_0r_0t_0)\rfloor$. Allocate exactly $(\#q)(\#r)(\#t)J$ tickets to the box. Each ticket selects one prime triple and an integer $0\le j<J$, giving $u=\lfloor l/m\rfloor+1+j$. Reject unless the order, product bounds, final prime gate and primality all hold. Boxes pruned in the driver cannot contain a sorted admissible tuple. Each valid site has precisely one ticket by sorted factorization, also with repeated primes. This proves exact uniformity conditional on acceptance for uniform independent ticket draws. Two toy intervals check every ticket against independent trial factorization.

Use 16,000 accepted sites at each of the following centers; $p$ is the first prime after $2^{25}$ or one of the two primes bracketing $3^{24}$. Exact integer root comparisons set every gate. Primality uses twelve strong probable-prime bases **within their deterministic range**; all tested integers are below $318665857834031151167461$. [Sorenson–Webster, *Strong pseudoprimes to twelve prime bases*](https://doi.org/10.1090/mcom/3134)

| $p$ | $\lfloor x^{1/48}\rfloor$ | lower rough sites | lower primes | observed rough-site prime share | finite $1.20/(L_x V(x^{1/48}))$ | observed $B_x$ estimator | upper bound for $B_x$ from sample |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 33554467 | 2 | 16000 | 605 | 3.7813% | 6.9249% | 1.31048 | 1.5061 |
| 282429536453 | 2 | 16000 | 406 | 2.5375% | 4.5512% | 1.33811 | 1.5861 |
| 282429536483 | 3 | 7957 | 365 | 4.5872% | 6.8268% | 1.20298 | 1.4392 |

The last column rounds upward. One-sided binomial KL–Chernoff bounds at tail probability $1/600$ per rate give simultaneous 99% coverage for the three unconditioned and three conditional rates in the ideal independent sampling model (conditioning on the number of rough sites for the latter). The program uses fixed pseudorandom seeds 2026112601–03 for reproduction. The third rough-site percentage exceeds the often quoted **limiting** 4.45%; its finite threshold is 6.8268%. Including 3 removes the class $a=2\bmod3$ from the denominator at this square. The last column tests the same cutoff-free scale at all three centers. These observations are numerical and do not give a uniform upper bound on $B_{p^2}$ or on $D_{\rm else}$.

[Reference implementation and exact checks](CheckFourPrimeEnrichment.py)
