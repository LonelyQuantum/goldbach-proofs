# Three partner primes in the mixed-sieve product strip

Fix $\rho=1/100$. Use the genuine extended records, orientations, small wheels and block-dependent Selberg roots of [CompositePartnerWeight.md](CompositePartnerWeight.md). Brackets sum the actual weights $\log r\,\log p$ of these records and divide by the genuine marked-pair mass $A_2$. Here $p$ is the marked reflected prime. The brackets give mass relative to $A_2$, which need not be a probability on the extended sample. The center is $N=2s$, $L=\log s$, $\eta=(\log L)^{-3}$, $z=s^\eta$. Write $k=\#\{z<q\le B_+:q\mid t\}$ and $F_\pm=F_{B_\pm}(t)$. The set $E$ consists of records with $k=3$ and $B_-^2\le P\le B_+^2$, where $P$ is the product of these three distinct partner primes. At a record put $X=\log q_{\min}/\log B_+$.

In the [fixed-center dispersion framework](PairTripleDispersion.md#a-distribution-estimate-with-an-unrestricted-integer-factor) we obtain
$$
\begin{aligned}
 \limsup_{s\to\infty}\langle1_{k=3}(F_-F_+)_-\rangle_s &<0.023287,\\
 \limsup_{s\to\infty}\langle1_E1_{X\ge1/4}\rangle_s &<0.862723,\\
 \limsup_{s\to\infty}\frac{\langle1_E\rangle_s}{\log(1/\eta)}
 &<0.340225.                                                        \tag{1}
\end{aligned}
$$
Here $u_-=\max(0,-u)$. The last two lines count hits with the original record weights and no mixed-root multiplier. The last line is one-sided and does not determine the growth rate. The small-prime logarithm arises in the upper count when the smallest prime can approach the wheel. The first line bounds the *entire* three-factor debit, including negligible finite-sieve approximation errors outside $E$.

## Two tags at each actual record

In a dyadic block put $\gamma=\log K_*/L$, $b=\log B_+/L=(\gamma+.01)/2$ and $\delta=.02/b$. The two radii have exponents $b(1-\delta)$ and $b$. In the limit $.20\le\gamma\le .285$ and $.105\le b\le .1475$. Use the smallest of the three primes as the first tag, and take either of the other two as the second tag. Write $X,Y$ for their exponents in units of $b$ and $Z$ for the missing exponent in the same units. Thus $X\le Y,Z\le1$, with no order imposed between $Y$ and $Z$. There are exactly two choices of second tag, including when their exponents fall in the same mesh cell.

The product strip gives $2-2\delta\le X+Y+Z\le2$. In particular
$$
 (X,Y)\in D_\delta=\{0<X\le Y\le1,\quad X+Y\ge1-2\delta,\quad 2X+Y\le2\}.
$$
Write $c=(\gamma-b(X+Y))/2=b\,e_\delta(X,Y)$, with $e_\delta=1-\delta/4-(X+Y)/2$. In the limiting domain $e_\delta\ge1/4-\delta/4>1/5$. The cofactor of the two tagged primes has no prime of exponent below $bZ$ on our squarefree sample. Moreover $bZ\ge(\gamma-.03-b)/2\ge .0325+O(1/L)$ since $X\le Z$ and $Y\le1$. From $b(X+Y+Z)\ge\gamma-.03$ it follows that $2c\le bZ+.03\le2bZ$ for all sufficiently large $s$. This leaves the full auxiliary Selberg radius $s^{c-\epsilon}$ available on that cofactor. Rough nonsquarefree partners have negligible total mass even with the roots, by the divisor-moment estimate in the previous mixed-weight note.

For a nonnegative majorant $\Psi_\delta(X,Y)$ valid for **each** of the two choices, the resulting upper integral on any compact region away from $X=0$ is
$$
 \frac{q}{2}\,\mathbf E_0\left[
 \frac1b\int_{D_\delta}
 \frac{\Psi_\delta(X,Y)}{e_\delta(X,Y)}\,\frac{dX\,dY}{XY}\right],
 \qquad q=\frac{(.35-.34)\log(6/5)}{\log(66/65)}.                    \tag{2}
$$
Region restrictions are included in the integrand. This bounds an arithmetic upper limit for each center sequence. The factor $1/2$ accounts for the two choices just counted. Under $\mathbf E_0$ the exponent $\tau$ of $r$ is uniform on $[.34,.35]$, one reflected exponent is uniform on $[1/16,3/40]$, and the other two are log-uniform there, independently. Their sum $d_0$ gives $\gamma=1-\tau-2d_0$ up to the vanishing dyadic endpoint shift.

For the transfer, majorize each genuine marked record by its cofactor square, which equals one on that record, and then allow unrestricted cofactors. Bin $b,X,Y$ and freeze a lower auxiliary radius, leaving fixed power slack. Writing $t=q_1q_2 n$, the modulus cost on the partner side is at most $q_1q_2s^{2(c-\epsilon)}\le K_*s^{-2\epsilon}$ before bin rounding. The divisor conditions of the square act on $n$ even when its divisors share a tag. Within an original $R,D$ block, tags and all square coefficients enter the same divisor-side coefficient, with divisor-bounded multiplicity. The reflected triple weight stays separate. These are the hypotheses of the previous dispersion transfer. In the zero mode one obtains the factor $1/(q_1q_2)$ for the tags and $1/G(s^{c-\epsilon})$ for the square. Coincidences of a tag with a reflected prime give no records and may be omitted in the positive upper count. Deleting reflected primes in the square costs a power saving as in the preceding proof. The small wheels have their usual two-end density since the tags are units there. Partial summation of reciprocal prime weights on exponent intervals, $G(s^c)\sim W_z cL$ and the earlier $A_2$ evaluation give (2). Take the center limit first, then refine the bins and let $\epsilon$ decrease. This calculation does not apply the dispersion estimate to the product of all three tagged primes and a full-size square.

## The missing prime and the sign

For fixed $k=3$ the two roots have uniform limiting profiles $f_w=\sum_{U}(-1)^{|U|}(1-\sum_{i\in U}X_i/w)_+$ at $w=1-\delta,1$. The error is $O((\log L)^{-3/2})$ on these records. The previous fixed-factor upper count bounds their total normalized mass by $O((1+\log(1/\eta))^3)$, so the integrated error tends to zero. By complementary subsets, a nonzero three-prime profile has the sign of $X+Y+Z-2w$, so a negative product can only occur on $E$. [Profile and three-prime sign](CompositePartnerWeight.md#a-mixed-product-below-the-old-reference-constant)

Put $h=1-Z$, $C=(X+Y-1)_+$ and $A=\min(X,(X+Y-1+\delta)_+)$. On the strip $X\le2/3<1-\delta$ and $Y+Z\ge2(X+Y+Z)/3>1$. The two-factor difference at $v$ is the tent $T(v)=\max(0,\min(v,X,X+Y-v))$, so $w f_w=T(w)-T(w-Z)$. At the two radii this gives precisely
$$
 -f_1=\min(X,h)-C,\qquad
 (1-\delta) f_{1-\delta}=A-\min(X,(h-\delta)_+).
$$
When $h>X$ the first expression is constant and the second is nonincreasing. Positive parts therefore bound the debit by the following function of the two observed tags.
$$
 U_\delta(X,Y)=\frac1{1-\delta}
  \max_{0\le h\le R}\big(A-(h-\delta)_+\big)_+(h-C)_+,\qquad
  R=\min(X,1-X).                                                       \tag{3}
$$
For $h\le\delta$ the product increases. Above $\delta$ its positive part is a concave quadratic on its positive interval. An optimizer is $h=\min(R,\max(\delta,(A+\delta+C)/2))$, also giving zero when the positive interval misses $[0,R]$. The estimate is valid for both tag choices. The bound $U_\delta\le X^2/(1-\delta)$ removes the small-prime logarithm in (2). To justify the endpoint on the arithmetic side, group $X\le\epsilon_0$ in one cell and use its weight $X^2$, keeping the two-tag reciprocal sum. On the strip $Y>1/2$ for small $\epsilon_0$, and $\sum_{p\le s^{b\epsilon_0}}(\log p/(bL))^2/p=O(\epsilon_0^2)+o(1)$ by partial summation, uniformly on the compact $b$ range. A fixed auxiliary radius bounded below is available. One can now let $\epsilon_0$ decrease to zero.

For the second line of (1) use $\Psi=1_{X\ge1/4}$. For the last line separate $X\ge\epsilon_0$, whose mass is bounded, and the complementary region. In this latter region summing the first tag costs at most $\log(1/\eta)+O_{\epsilon_0}(1)$, since its lower endpoint is $z=s^\eta$. Bin $Y$ and $b$ as above, using the level at the upper edge for $X$. After dividing by $\log(1/\eta)$ and decreasing $\epsilon_0$, the upper integral becomes
$$
 \frac q2\,\mathbf E_0\left[\frac1b
 \int_{1-2\delta}^1\frac{dY}{Y(1-\delta/4-Y/2)}\right].                \tag{4}
$$
The factor $1/2$ also applies here. Counting only the smaller of the two nonminimal tags would lose this multiplicity when the minimum approaches the wheel.

## Directed constants and a genuine finite hit

The [checker](CheckThreeFactorStrip.py) evaluates (2)–(4) using integer upper sums. It uses 768 panels per normalized tag coordinate and 64 outer panels per reflected or $r$ exponent. The three upper integrals increase with $\delta$ and $1/b$. Each log-uniform reflected coordinate is dominated by an ordinary uniform coordinate since its geometric quantile is below the chord between its endpoints. Right endpoints for these uniform coordinates give lower $b$ and hence upper values. On each tag cell use upper $A,R,\delta$ and lower $C,e_\delta$, and integrate $dX/X$ and $dY/Y$ by left endpoint upper sums. For $X<1/768$ the debit integral before $q/(2b)$ is at most $4/768^2$ using (3), $e_\delta>1/5$ and $Y>1/2$. All rounding and the outer logarithm bounds are rational. The integer-cell maxima can be achieved at a half-grid position and the checker retains it.

There is also a record with actual primes and actual finite sieve roots. At $s=106389289462078729450840$ take
$$
 a=29\cdot37\cdot43\,(2^{61}-1),\qquad
 2s-a=87958907\cdot(3\cdot31\cdot409)\cdot31798879949 .
$$
Here $2<z<3$, $\lfloor B_-\rfloor=193$, $\lfloor B_+\rfloor=560$, and $P=38037$ lies in the strip. The roots satisfy $0.03675<F_-<0.03676$ and $-0.26382<F_+<-0.26381$. The checker verifies primality, the sharp window, both radius comparisons and both exact rational root sums. This supplies an example of nonzero negative mass at one center. The uniform bounds in (1) come from the sieve transfer.

The three-factor debit uses at most $71.82\%$ of the previous $0.032427 A_2$ allowance in the upper-limit sense. After reserving $0.023287 A_2$ for it, the remaining sufficient budget is $0.009140 A_2$ on $4\le k\le4095$ outside the four-factor band already charged. The [previous many-factor bounds](MixedMultiplicityTail.md) and this estimate leave $M_s<0.980$ open.
