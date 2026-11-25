# A composite comparison with a proved supply of genuine prime partners

Fix a large odd prime $p$, $X=p^2$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, $h_0=H-2T$, and let $n$ run over $J=[X-H,X-2T)\cap\mathbb Z$. Write $a=2X-n$, $P=1_{\mathbb P}$ and $K=2C_2H/L^2$ with $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$ over primes. Put $\lambda=1/30$, $z=X^\lambda$, $u=921/10000$, $v=923/10000$ and define a lower weight
\[
 G(n)=c\,1_{\{n\ {\rm squarefree},\,P^-(n)>z\}}
       \sum_{\substack{X^u<q\le X^v\\q\mid n,\ q\ {\rm prime}}}1,\qquad
 c=\frac{e^\gamma}{30\log(v/u)}.
\]
Every selected site is composite. It has no prime factor at most $z$, and $n/P^+(n)>X^u$: either the marked prime survives removing the largest prime or the cofactor is at least $(X-H)/X^v$. The weight is bounded by $10c$ and counts each possible mark. There is no eight-factor restriction. This changes the comparison set from the [previous fixed-square reduction](LocalizedVaughanComparison.md).

Write $R_G=\sum_n G(n)P(a)$ and $R_P=\sum_n P(n)P(a)$. The first result is
\[
 \liminf_{p\to\infty}R_G/K\ \ge f(2.231)>0.331 .
 \tag{1}
\]
Consequently over $0.0012K$ **distinct** upper primes have such a squarefree composite lower partner at every sufficiently large prime square. The normalized weight in (1) is essential for the larger constant.

For $\eta>\lambda$, put
\[
 W_\eta(a)=1_{\{a\ {\rm squarefree,\ composite},\ P^-(a)>z\}}
       \sum_{\ell\mid a,\ \ell>X^\eta,\ \ell\ {\rm prime}}\frac{\log\ell}{L},
 \qquad \Delta_\eta=\sum_n (G(n)-P(n))W_\eta(a).
\]
The second result gives a **one-sided** bound with no unknown $R_G$ on the right:

| Upper marking exponent $\eta$ | Strict lower bound on $\liminf_{p\to\infty}(R_P-\Delta_\eta)/K$ |
|---|---|
| $1/15$ | $0.25$ |
| $1/12$ | $0.17$ |
| $1/10$ | $0.004$ |

For example, absence of a central pair along an infinite sequence forces $\Delta_{1/15}<-0.25K$ eventually on it. Conversely, $\Delta_{1/15}\ge-0.25K$ at every sufficiently large prime square would imply central pairs there. At the highest cutoff every marked upper prime factor exceeds every lower tag. These are necessary signed deficits for failure; an estimate excluding one for the actual primes is open.

## Lower bound with the upper endpoint prime

Let $S(b)=1_{P^-(b)>z}$. In all counts one may omit the squarefree test on a $z$-rough site at cost $o(K)$, since the number of multiples of squares of primes exceeding $z$ in the window is $O(H/z+\sqrt X)$. The weights here are bounded, including sums of marked logs divided by $L$.

Fix a mark $q$. Among primes $a\equiv 2X\bmod q$ sift $n/q$ through $z$ at level $D/q$, where $D=X^{1/6}L^{-B}$ with sufficiently large $B$. The initial mass is $h_0/[L(q-1)]$, and each odd sieve prime $\ell\le z$ has local density $1/(\ell-1)$. The prime 2 is already avoided. Summing the remainders after sieving uses each squarefree modulus $qd$ at most once since $q>z$ and all primes of $d$ are at most $z$. Cai–Lu Lemma 3 at auxiliary variable 1 applies to the full window and to these reduced classes. Replacing its logarithmic integral by $h_0/L$ is harmless since both endpoints are $X+O(H)$. [Cai–Lu, *Chen's theorem in short intervals*, Lemmas 1–3, pp. 312–313](https://doi.org/10.4064/aa-91-4-311-323)

Let $V_1(z)=\prod_{\ell\le z}(1-1/\ell)$ and $V_c(z)=\prod_{2<\ell\le z}(1-1/(\ell-1))$. Then $V_c(z)\sim 2C_2 e^{-\gamma}/\log z$. The lower sieve parameter differs by $o(1)$ uniformly from $30(1/6-\log_X q)$, which is at least $2.231$. The lower sieve function $f(s)=2e^\gamma\log(s-1)/s$ is increasing throughout this small range. Also $\sum_q1/(q-1)=\log(v/u)+o(1)$. Multiplication by $c$ proves (1). The same choice gives $c\sum_q q^{-1}V_1(z)\sim1/L$, which normalizes the comparison below.

## Both endpoints rough, with an optional marked upper prime

For $r=1$ or prime $z<r\le X^{1/10}$, consider $q\mid n$, $r\mid a$, $S(n)S(a)=1$. If $r=q$ the count is zero; the total discarded ideal weight is negligible since $\sum_q 1/q^2=o(1)$. Otherwise put $h_r=h_0/(qr)$. The arithmetic is a single progression modulo $qr$. Write $V_2(z)=V_1(z)V_c(z)$. The double-rough count has ideal mass $h_rV_2(z)$. Summed over marks, its relative error is bounded by
\[
 E=2g(1+g),\qquad g=1/10500, \tag{2}
\]
up to $o(1)$ in the normalized total, both with the unmarked upper side and with the nonnegative upper weights $\log r/L$. Here are the details ensuring uniformity.

First sieve both endpoints at primes $\ell\le w=\exp(\sqrt L)$. There are two distinct forbidden residues at every odd prime and one at 2, since $p>z$. Additional middle divisors $d\mid n$, $e\mid a$ have all their primes in $(w,z]$. For $(d,e)=1$, the initial progression has modulus $qrde$ and the pre-sieved count is
\[
 \frac{h_r}{de} V_2(w)+O_A\!\left(\frac{h_r}{de}L^{-A}+X^{o(1)}\right).
\]
Indeed two adjacent Bonferroni truncations of order $\asymp L^{1/4}$ have main-term gap at most $(O(\log L))^j/j!$ relative to $h_r/(de)$. Rounding costs $X^{o(1)}$, since all products used are $w^{O(L^{1/4})}$ and have at most $2^j$ forbidden CRT classes. If $(d,e)>1$ the count vanishes.

For each of the two remaining sieves take upper and lower Rosser divisor sums $U_i,L_i$ supported on $d$ or $e\le X^{7/30}$, with absolute coefficients at most one, and sandwich the middle-prime indicator $s_i$ between them. Pointwise,
\[
 U_1U_2-(U_1-L_1)U_2-U_1(U_2-L_2)
       \ \le s_1s_2\le U_1U_2 .
\]
This uses $U_i\ge s_i\ge0$ and $L_i\le s_i$. For instance the slack in the lower inequality is $(U_1-s_1)(U_2-s_2)+(s_1-L_1)U_2+(s_2-L_2)U_1$. Total rounding over all $q,r,d,e$ is $O(X^{v+1/10+14/30+o(1)})=o(K)$. To factor the CRT main term, putting back terms with a common prime in $d,e$ costs at most $O(L^2\sum_{\ell>w}\ell^{-2})$ times $h_r$. The same bound works for all three products of divisor sums. Summing the $L^{-A}$ errors costs at most logarithms times $H$.

In the factored main term the middle-prime divisor density on each side is $1/d$. The dimension-one product hypothesis is uniform on $(w,z]$ by Mertens' theorem (restricting the primes only decreases the product in the upper hypothesis). With $V_m=\prod_{w<\ell\le z}(1-1/\ell)$ the upper main sum divided by $V_m$ lies between 1 and $F(7)+o(1)$, and the lower between $f(7)-o(1)$ and 1. The inner endpoints 1 follow by averaging the pointwise inequalities in the independent divisibility model. The Rosser main-term bounds are the dimension-one linear sieve. [Iwaniec, *A new form of the error term in the linear sieve*](https://doi.org/10.4064/aa-37-1-307-320) · [Matomäki, sieving lemmata and Rosser–Iwaniec bounds](https://users.utu.fi/ksmato/wp-content/uploads/sites/1432/2025/04/Goldbach_k2pl2p1.pdf)

The width is $F(7)-f(7)=2e^\gamma\rho(6)/7<g$, by the Dickman delay identity in the previous note, $\rho(4)<0.005$, $j\rho(j)\le\rho(j-1)$ and $e^\gamma<2$. Hence the scaled upper product is at most $(1+g)^2+o(1)$ and the scaled lower expression is at least $1-2g(1+g)-o(1)$. Finally $V_2(w)V_m^2=V_2(z)(1+O(1/w))$ from the primewise factors. This proves (2).

## Keeping the signs of the single-sieve errors

For a lower weight $A$ write $S_A=\sum_n A(n)S(a)$ and $T_A=\sum_n A(n)S(a)\sum_{z<r\le X^\eta,\ r\mid a}(\log r)/L$ over prime $r$. On squarefree rough composites the logs of all prime factors sum to $\log a=L+O(H/X)$. It follows exactly up to $o(K)$ that
\[
 R_P-\Delta_\eta=R_G+S_P-S_G+T_G-T_P+o(K). \tag{3}
\]
Put $M=30e^{-\gamma}$. The comparison (2) gives $\limsup S_G/K\le M(1+E)$ and $\liminf T_G/K\ge M(\eta-\lambda)(1-E)$, since $\sum_{z<r\le X^\eta}(\log r)/(rL)\to\eta-\lambda$.

For the lower primes the upper roughness count satisfies $\liminf S_P/K\ge M f(5)$. To bound $T_P$ above, fix $r$, use the upper linear sieve at remaining level $D/r$, then sum. Each remainder modulus has only one prime above $z$. The density for $r$ is $1/(r-1)$, and the sieve functions are continuous on the compact ranges used. Thus
\[
 \limsup T_P/K\le M\int_\lambda^\eta F(5-30t)\,dt.
\]
Combining in (3) uses the lower bound on $S_P$ and the upper bound on $T_P$. For the three $\eta$ in the table, $s_*=5-30\eta\in[2,3]$. Near the last endpoint, if the logarithmic loss in $D$ puts the upper-sieve parameter just below 2, sift through $\min(z,\sqrt{D/r})$ for this upper bound; its product changes by a relative $o(1)$. Put $I_0=\int_2^3\log(t-1)\log(4/(t+1))\,dt/t$. Integrating the linear-sieve functions in their initial ranges gives $Mf(5)=12(\log4+I_0)$ and $M\int_\lambda^\eta F(5-30t)\,dt=2\log(4/s_*)+2I_0$. The resulting lower coefficient is
\[
 f(2.231)+12\log4+10I_0-2\log(4/s_*)
    -M\left[1-(\eta-\lambda)+E(1+\eta-\lambda)\right].
\]
The [rational enclosure and finite checks](CheckMarkedPrimePartners.py) certify all three margins. For the last row the remaining observable has the explicit factor sum
\[
 -\Delta_{1/10}=
 \sum_{\substack{X^{1/10}<r\le (X+H)/z\\r\ {\rm prime}}}
 \frac{\log r}{L}
 \sum_{\substack{t>1,\ P^-(t)>z,\ \mu^2(t)=1\\(r,t)=1,\ 2X-rt\in J}}
          (P(2X-rt)-G(2X-rt)).
\]
Each eligible $r$ contributes once for its upper site. The different marks on a site are part of its specified log weight. A uniform upper bound of $0.004K$ for this excess would suffice; the earlier $0.34K$ candidate count does not bound it.

## Counting distinct partners and testing one lower prime at a time

Let $\mathcal Q$ denote the lower tag primes above, $b=\log(v/u)$ and $M=30e^{-\gamma}$. For $q\in\mathcal Q$ let $A_q$ be the set of upper primes $a$ for which $q\mid n=2X-a$, $n\in J$, $n$ is squarefree and $P^-(n)>z$. At every sufficiently large prime square,
\[
 \left|\bigcup_q A_q\right|>0.0114K,\qquad
 \#\{a:a\text{ belongs to exactly one }A_q\}>0.0107K. \tag{4}
\]
There is also a statement for individual tags. Fix any $A>0$. In every dyadic interval $(Q,2Q]$ all but $O_A(Q/L^A)$ tag primes have more than $4.95K/q$ upper partners belonging exclusively to their own $A_q$. In a dyad contained in the tag band the exceptional proportion tends to zero for $A>1$. The exceptional set may depend on the center.

To see the individual lower bound, write $r_m$ for the discrepancy in the upper-prime progression of reduced residue $2X\bmod m$, with logarithmic-integral main term. Take the base point in Cai–Lu Lemma 3 to be $X+2T+1$ and its interval length $h_0$. For each $q$, the absolute sieve error is at most $e_q=\sum_{d\mid\prod_{2<\ell\le z}\ell,\,qd\le D}|r_{qd}|$. Unique recovery of $q$ as the only prime exceeding $z$ gives $\sum_q e_q\ll_{B'} H/L^{B'}$ for any prescribed $B'$ upon choosing the logarithmic loss in $D$ accordingly (the implied constant may depend on $B'$). Discard $q$ with $e_q>K/(qL)$. There are $O_A(Q/L^A)$ in a dyad, by taking $B'>A+3$. In this display the sum defining $e_q$ can include $d=1$. The fixed-$q$ linear sieve then gives
\[
 |A_q|\ge (M f(2.231)-o(1))K/q.
\]
The lower bound is uniform on the retained tags. In deleting squares at either rough endpoint for a fixed $q$, the primes $\ell>z$, $\ell\ne q$, cost $O(H/(qz)+\sqrt{2X})$ by CRT. The square $q^2\mid n$ costs $O(H/q^2+1)$, and $q\nmid a$. Multiplying the errors by $q$ gives $o(K)$ uniformly, since $v+1/2<2/3$.

For distinct $q,q'$ in the band, an intersection is bounded by counting multiples of $qq'$ with both endpoints $z$-rough. In the upper vector-sieve argument for (2), start on that single progression. The two tag primes exceed every sieve prime. The uniform bound is
\[
 |A_q\cap A_{q'}|\le(1+E+o(1))\frac{M^2K}{qq'}.
\]
Indeed the CRT rounding error per progression is $X^{14/30+o(1)}=o(K/(qq'))$ since $2v+14/30<2/3$. The other relative errors in (2) are uniform on these progressions. Here $H V_2(z)\sim M^2K$. Summing over $q'\ne q$ costs at most $((1+E)M^2 b+o(1))K/q$. Subtraction proves the individual assertion. For (4), the total incidence is at least $(M f(2.231)b-o(1))K$ by (1), while the sum over unordered intersections is at most $((1+E)M^2 b^2/2+o(1))K$. At a site with $k$ tags, $1_{k\ge1}\ge k-\binom{k}{2}$ and $1_{k=1}\ge k-2\binom{k}{2}$. Applying the two inequalities gives (4).

There is a limitation to varying $q$ in the signed test. Set $G_q=(q/M)1_{q\mid n}1_{\{n\ {\rm squarefree},\,P^-(n)>z\}}$, $R_q=\sum G_q(n)P(a)$ and $\Delta_{\eta,q}=\sum(G_q(n)-P(n))W_\eta(a)$. Write $d_\eta=\eta-\lambda$. Uniformly for **every** $q$ in the band, for each of the three cutoffs,
\[
 \left|\frac{R_q+\sum G_q(n)W_\eta(a)}{K}-M(1-d_\eta)\right|
 \le M E(1+d_\eta)+o(1). \tag{5}
\]
Indeed $R_q+\sum G_q W_\eta=S_{G_q}-T_{G_q}+o(K)$ by the log decomposition in (3). For $S_{G_q}$ and $T_{G_q}$, (2) now starts at the fixed tag. After multiplying by $q/M$ and summing over $r$, rounding costs $X^{v+1/10+14/30+o(1)}=o(K)$. Omitting $r=q$ removes $O(1/q)$ of the normalized ideal mass. Replacing $\log a$ by $L$ costs $o(K)$ even using the trivial bound $\sum G_q=O(H)$, and the square exclusions above apply with the bounded combined log weight. The two ideal masses are $MK$ and $M d_\eta K$.

For each retained $q$, $R_q/K\ge f(2.231)-o(1)$, so using (3) with $G_q$ gives the same three strict margins $0.25,0.17,0.004$ for $(R_P-\Delta_{\eta,q})/K$ at sufficiently large $p$. Thus absence of a central pair forces the corresponding deficits for almost all tags in each full dyad, simultaneously for the three cutoffs. Yet for any two tags, subtracting (5) cancels the shared lower-prime sum $\sum P(n)W_\eta(a)$ and gives
\[
 \big|(R_q+\Delta_{\eta,q})-(R_{q'}+\Delta_{\eta,q'})\big|<0.0069K
\]
at all sufficiently large centers. An increase in genuine upper partners can therefore occur alongside a nearly equal decrease in the signed residual. Counting more lower tags supplies no independent bound on the common sum over actual lower primes. None of (4) or (5) establishes $R_P>0$.

The common quantity also gives a sufficient test without any lower tag. Put $C_\eta=\sum_n P(n)W_\eta(2X-n)$. On lower primes the same log decomposition gives $R_P+C_\eta=S_P-T_P+o(K)$. The bounds for $S_P$ and $T_P$ above give
\[
 \liminf_{p\to\infty}\frac{R_P+C_\eta}{K}
 \ge 12\log 4+10I_0-2\log(4/s_*).
\]
The right-hand sides exceed $16.2090,15.8443,15.3980$ at the three cutoffs, respectively. In particular, an upper bound $C_{1/10}\le 15.3980K$ at every sufficiently large prime square would already force a central prime pair there. This is an outstanding upper bound on a nonnegative sum with an actual prime lower endpoint. The supplied estimates on tagged composite lower endpoints do not give it.
