# What several missing central Goldbach representations force at prime-pair differences

Put \(L=\log Y\), \(H=\lfloor Y^{2/3}\rfloor\), \(T_x=\lfloor x^{21/40}\rfloor\), \(H_x=\lfloor x^{2/3}\rfloor\), \(\Delta=\lfloor H/L^8\rfloor\), and let \(Y\) tend to infinity through integers. A center \(x\) fails if there is no prime pair \(x-v,x+v\) with \(2T_x<v\le H_x\). This is a stronger representation requirement than ordinary binary Goldbach. A counterexample to binary Goldbach necessarily fails it.

Take distinct integer centers \(Y\le x_i\le Y+\Delta\), put \(t_i=2x_i\), and set \(I=(Y+2T_Y+2\Delta,Y+H]\cap\mathbb Z,\ h=|I|\sim H\). For large \(Y\), every \(a\in I\) is in the specified upper window for every center. Indeed \(2(T_x-T_Y)=o(\Delta)\) uniformly, and the right endpoint increases with \(x\). Define \(\vartheta(v)=\log v\) on primes and zero otherwise. For even \(d>0\) write
\[
 s(d)=s_0\prod_{\ell\mid d,\ \ell>2}\frac{\ell-1}{\ell-2},
 \qquad s_0=2C_2=2\prod_{\ell>2}(1-(\ell-1)^{-2}).
\]
All Euler products below are over primes. For \(i\ne j\) the observable is
\[
 Q_{ij}=\sum_{a\in I}\vartheta(t_i-a)\vartheta(t_j-a)-h\,s(|t_i-t_j|).
\]
It counts actual prime pairs at positive spacing \(|t_i-t_j|\) with the smaller prime in the translated interval \(\min(t_i,t_j)-I\). Different pairs can have different translated intervals.

## A necessary consequence at general even targets

For any family of \(k\ge1\) failing centers in this packet, the **ordered** off-diagonal sum satisfies, uniformly,
\[
 \sum_{i\ne j}Q_{ij}
 \ \ge\ (s_0^2-o(1))\,\frac{h k^2}{L}-(1+o(1))\,hkL. \tag{1}
\]
In particular, if \(k\ge2L^2\), some pair has \(Q_{ij}>h/L\). In fact \(\gg k^2/(L\log L)\) ordered index pairs have \(Q_{ij}>h/L\). For \(Y=P^2\) and centers \(x_i=m_i^2\) in this same packet, the **positive spacings are distinct** over unordered pairs, even if the \(m_i\) are not prime. Hence the latter conclusion counts that many distinct spacings, up to the factor two for ordering. No estimate for the unknown off-diagonal prime-pair correlations is assumed in (1).

The calculation is applicable to the main binary conjecture at arbitrary even targets. An isolated failure is compatible with (1). Perelli's polynomial theorem treats full-length sums and Coppola–Laporta localize the summands with exceptions counted among all even targets. Neither of those conclusions gives the short-window sparse upper bound on \(Q_{ij}\) needed here. [Perelli, Theorem 1 and Corollary 1](https://doi.org/10.4171/RMI/205) · [Coppola–Laporta, Theorem 1](https://www.giovannicoppola.name/files/articoli/8_giovanni_coppola_number_theory_seminar_politecnico_torino_245.pdf)

## Removing the local main terms uniformly

Use \(z=L^5\), \(V(z)=\prod_{\ell\le z}(1-1/\ell)\) and \(C(n)=1_{(n,\prod_{\ell\le z}\ell)=1}/V(z)\). For an interval of \(h\) integers and the two forms \(u\) and \(v=\pm u+b\) taking values in \([Y/2,2Y]\), with even \(0<|b|\le4Y\), one has uniformly
\[
 \sum \vartheta(u)C(v)=h s(|b|)+O(h/L^2),\qquad
 \sum C(u)C(v)=h s(|b|)+O(h/L^2).                              \tag{2}
\]
Here \(u\) ranges through consecutive integers. The sign does not change the number of excluded local residues.

For the mixed sum use consecutive Bonferroni truncations of the exclusion of primes \(\le z\) from \(v\), of orders \(r,r+1\) with \(r=\lceil(\log L)^2\rceil\). The squarefree moduli are at most \(z^{r+1}=Y^{o(1)}\), and each modulus imposes just one class on \(u\). If its class is not reduced it contains no counted primes since \(u\asymp Y\). In a reduced class use \(h/\varphi(d)\). The summed absolute progression errors are \(O_A(hL^{-A})\) for any fixed \(A\), by the short-interval Bombieri–Vinogradov theorem at exponent \(2/3\). Its maxima cover the different shifts of the interval. Removing proper prime powers costs at most \(Y^{1/2+o(1)}\) over these moduli. The first omitted elementary symmetric sum of the densities is at most \((O(\log\log z))^{r+1}/(r+1)!\), which beats every fixed power of \(L^{-1}\). At \(\ell\nmid b\) the density removed is \(1/(\ell-1)\), and at \(\ell\mid b\) it is zero. Division by \(V(z)\ll1\) costs only \(O(\log z)\) multiplicatively through its reciprocal. [Perelli–Pintz–Salerno, equation (2) and theorem on p. 530](https://www.numdam.org/item/ASNSP_1984_4_11_4_529_0.pdf#page=3)

For the two model factors exclude the \(\nu_\ell=|\{0,b\bmod\ell\}|\) roots at each prime in the same truncation. CRT gives a total endpoint error \(Y^{o(1)}\), since any term has at most \(2^{r+1}\) residue classes. The same factorial bound applies with densities \(\nu_\ell/\ell\). Both normalized Euler products are exactly \(\prod_{\ell\le z}(1-\nu_\ell/\ell)/(1-1/\ell)^2\). Its difference from \(s(|b|)\) is \(O(L^{-2})\): generic primes in the tail cost \(O(1/z)\) on the logarithmic scale, and the prime divisors of \(b\) above \(z\) cost \(O(L/(z\log z))\). Uniformly \(s(|b|)\ll \log L\), by Mertens up to \(L\) and the same divisor bound above \(L\). This proves (2) without estimating \(\sum\vartheta(u)\vartheta(v)\).

## From a missing representation to a positive surplus

Regard functions of \(a\in I\) as real vectors with the ordinary counting inner product. Set \(u(a)=\vartheta(a)\) and \(v_i(a)=\vartheta(t_i-a)-C(t_i-a)\). At a failing center \(\langle u,v_i\rangle=-hs(t_i)+O(h/L^2)\) by (2). The short-interval prime number theorem gives \(\|u\|^2=(1+o(1))hL\) and, uniformly, \(\|v_i\|^2\le(1+o(1))hL\). For the latter bound the mixed diagonal term is nonpositive after expansion and \(C^2\ll(\log z)^2=o(L)\) pointwise. For \(i\ne j\), applying (2) to each of the two mixed terms and the model-model term gives \(\langle v_i,v_j\rangle=Q_{ij}+O(h/L^2)\). Project \(\sum_i v_i\) onto \(u\), square, and subtract the \(k\) diagonal terms. The total substitution error \(O(hk^2/L^2)\) is absorbed in (1).

For the numerical consequence, \(C_2\ge(3/4)(15/16)(1-1/8)=315/512\): extend the Euler product to all odd integers at least 3, and bound the tail by \(\sum_{j\ge3}(2j)^{-2}\le1/8\). Thus \(s_0^2>3/2\) with a fixed margin. At \(k\ge2L^2\) the ordered sum exceeds \((1+\epsilon)hk^2/L\) for an absolute \(\epsilon>0\) eventually. The usual two-form upper-bound sieve on an interval of length \(h\asymp Y^{2/3}\) gives \(Q_{ij}\ll h s(|t_i-t_j|)\ll h\log L\). To see the uniformity, the two excluded residues collide exactly at primes dividing the difference, the CRT remainder per squarefree \(d\) is at most \(2^{\omega(d)}\), and all prime values exceed any small fixed power of \(h\) used for sifting. The explicit Selberg-square argument for two unit-slope forms applies unchanged to the translate. Comparing the high and low entries gives the asserted multiplicity. [Short-interval two-form sieve argument](CentralPrimePairsNearOneCenter.md#removing-a-central-coefficient-while-preserving-short-interval-counts)

For squares, write \(m=P+v\), \(0\le v\le U\le\Delta/(2P)\). Then \(U^2<P\) eventually. An equality of two positive differences becomes \(2P[(v-w)-(v'-w')]=(v'^2-w'^2)-(v^2-w^2)\), whose right side has absolute value less than \(2P\). Thus \(v-w=v'-w'>0\). The equality of the quadratic parts gives \(v+w=v'+w'\), determining the ordered pair. This uses only the elementary subcritical range of the earlier [short square collision lemma](L_goldbach_short_square_window_collision.lean).

## The four-factor excess can be tested on the very same differences

Let \(E_x,M_x,Z_x,c'\) be the upper four-prime sector, its size, its normalized reflected-prime share and its density from [the preceding note](FourPrimeEnrichment.md). Set \(E=E_Y\cap I\), \(w=1_E\). Then \(w\perp u\) and \(M=|E|\sim c'h/L\). At prime-square centers in this packet,
\[
 \sum_{a\in E} C(t_i-a)= (1+o(1))M s_0.                         \tag{3}
\]
Indeed apply the same two alternating truncations to the fixed upper four-prime reduced-class estimate in [the four-prime distribution note](FourPrimeDistribution.md). Its moduli include \(z^{r+1}\); the factors of every upper site exceed \(z\), and \(t_i=2m_i^2\) has no odd factor \(\le z\) for prime \(m_i\). Omitting \(E_Y\setminus I\) changes the sum by \(O(\Delta\log z)=o(M)\). This is the only section needing the project's four-prime estimate.

Uniformly \(|E_x\triangle E|=O(H/L^8)+o(H/L^8)\). The endpoints cost \(O(\Delta)\). For a factor boundary \(x^\gamma\), \(\gamma=67/400,2/5\), count all possible crossing integers and multiples: the cost is \(O((1+\Delta Y^{\gamma-1})(1+H/Y^\gamma))\). This is power-saving relative to \(H\). Also \(\log(t_i-a)=L+o(1)\). If \(Z_{x_i}>1+\delta\) for fixed \(\delta>0\), (3) therefore gives \(\langle w,v_i\rangle\ge(\delta s_0-o(1))M\). Projecting onto \(w\) alone shows (1) for a family of such squares with \(s_0^2\) replaced by \(c'\delta^2 s_0^2\), without any assumption that the centers fail. If every member both fails and has \(Z_{x_i}>1+\delta\), the two orthogonal projections add and the replacement is \((1+c'\delta^2)s_0^2\). The earlier threshold has \(\delta=0.225\).

In particular, for \(K\) actual prime-square centers in a packet with \(K/L^2\to\infty\), an upper bound \(\sum_{i\ne j}(Q_{ij})_+=o(hK^2/L)\) over **all** these centers would put both exceptional sets at \(o(K)\), by applying the corresponding inequalities to the exceptional subsets. This sparse upper bound is open here. The diagonal cost leaves room for isolated failures even with that input. The positive part is taken after subtracting the local main term at each spacing.

## A signed test for the square-subsequence mean

For the full packet of \(K\) prime-square centers put \(R_i=\sum_{a\in I}\vartheta(a)\vartheta(t_i-a)\), and write bars for means over these centers. Define the signed quantity \(A_K=L\sum_{i\ne j}Q_{ij}/(hK^2)\). The projections also give the tradeoff
\[
 (\overline R/h-s_0)^2+c's_0^2(\overline Z-1)^2
 \ \le\ A_K+(1+o(1))L^2/K+o(1).                                  \tag{4}
\]
Indeed the two projections of \(\sum_i v_i\) have inner products \(Kh(\overline R/h-s_0+o(1))\) and \(KM(s_0(\overline Z-1)+o(1))\). The second identity uses the window comparison and (3) for each \(i\). Replacing each \(\log(t_i-a)\) by \(L\) costs \(o(M)\) for a single center. Both normalized averages are bounded: the two-form upper sieve bounds \(R_i/h\), and the previously established rough-site upper sieve bounds \(Z_{x_i}\) at squares. Divide the squared projection inequality by \(hK^2/L\), use the diagonal bound, and absorb the mixed errors from (2). Extending \(R_i\) to the full trimmed window costs \(O(\Delta L^2)=o(h)\) for every \(i\).

Thus \(K/L^2\to\infty\) and \(\limsup A_K\le0\) alone would recover \(\overline Z\to1\) **on the square subsequence**, together with the genuine two-prime asymptotic \(\overline R\sim s_0 h\). The latter guarantees a positive proportion with a central pair by the uniform upper sieve, and Markov separately gives limiting lower proportion at least \(9/49\) for \(Z_{x_i}\le1.225\). An upper bound on the full signed sum suffices for these two mean statements and does not have to hold for subsets. The stronger positive-part hypothesis above would control the proportions of exceptional centers. None of these sparse correlation upper bounds follows here from the dense-center mean.

For existence on a positive proportion, (4) needs less precision. If \(K/L^2\to\infty\) and \(A_K\le s_0^2-\epsilon\) for a fixed \(0<\epsilon<s_0^2\), then \(\overline R/h\ge s_0-\sqrt{s_0^2-\epsilon}+o(1)>0\). This gives a one-sided target for an estimate over all prime indices without first identifying any failures. There are at most \(O(Y^{1/3}/L^{16})\) square spacings to test in an ambient range of order \(Y^{2/3}/L^8\). Bounds allowing an arbitrary exceptional set of ambient spacings of relative density \(O_A(L^{-A})\) for every fixed \(A\) can still miss this entire sparse set.

[Exact finite checks of the projections, residue classes and spacings](CheckCentralPrimePairDifferences.py)
