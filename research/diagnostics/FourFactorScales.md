# Four partner primes at different scales

Keep the fixed-center arithmetic records, positive bracket normalized by $A_2$, and mixed Selberg roots $F_-,F_+$ of [the three-prime calculation](ThreeFactorStrip.md). The center is $N=2s$. Fix $\rho=1/100$. For $k=4$ order the four distinct partner primes $p_1<p_2<p_3<p_4$ between the small wheel and the long radius. Let $E$ be the previously charged event in which all four belong to $[s^{.030},s^{.045}]$. Put $D_s(H)=\langle1_{k=4}1_{E^c}1_H(F_-F_+)_-\rangle_s$, with $u_-=\max(0,-u)$. The weights include the genuine reflected prime triple and its marked-pair orientations.

The fixed-center dispersion argument gives the following upper limits through all integer centers.

| Event $H$ | Upper bound for $\limsup_s D_s(H)$ |
|---|---:|
| $p_{i+1}\ge p_i^2$ for $i=1,2,3$ | $0.0000874$ |
| Four distinct dyadic exponent bands $(2^{-j-1},2^{-j}]$, $j\ge0$ | $0.0011475$ |
| $p_4^2\ge p_2^5$ | $0.003752$ |
| All of $E^c$ at $k=4$ | $0.032372$ |

The first three bounds use at most $0.96\%$, $12.56\%$ and $41.06\%$ of the outstanding $0.009140 A_2$ budget, respectively. They concern overlapping events and should not be added. The last bound alone allows about $354.2\%$. A positive comparison measure satisfies **every** tagged rough-cofactor upper bound (3) below, yet its debit on $E^c$ exceeds $0.0111546$ in the same units. This identifies an obstruction to deriving the full budget solely from those inequalities. Its mass describes an exponent-space comparison and gives no lower bound on the debit of any integer center.

## Exact location of the two sign changes

In each block let $b=\log B_+/\log s$, $\delta=.02/b$, $a=1-\delta$, and $T=2-\delta/2$. In the limiting exponent boxes $.105\le b\le .1475$, $\log B_-/\log B_+=a$ and $\log K_*/\log B_+=T$. Write $x\le y\le v\le z$ for the four exponents in units of $\log B_+$, $S=x+y+v+z$, and
$$
 G(w)=\sum_{U\subseteq\{1,2,3,4\}}(-1)^{|U|}(w-\sum_{i\in U}x_i)_+,\qquad
 R=\min\{x+y,(x+y+v)/2,S/3\}.
$$
The limiting debit is $W=(-G(a)G(1))_+/a$. Replacing the two finite roots by their fixed-four-factor profiles costs $o(1)$ after summation by the uniform profile error and the fixed-factor mass estimate. [Harmonic approximation and arithmetic transfer](CompositePartnerWeight.md#a-mixed-product-below-the-old-reference-constant)

For all real $w$,
$$
 G(w)>0\quad\Longleftrightarrow\quad 0<w<R\ \text{ or }\ S-R<w<S.        \tag{1}
$$
Indeed $G(S-w)=G(w)$ by complementing subsets and annihilating the affine difference of the two ramps. Define $J(u)=\max(0,\min(u,x,x+y-u))$. Then $G(w)=J(w)-J(w-v)-J(w-z)+J(w-v-z)$. On $[x+y,v+z]$ both positive tents vanish. Below $x+y$ no pair can enter the original ramp sum. There $G(w)=w-\sum_i(w-x_i)_+$ for $w\ge0$, which is the minimum of $w,x,x+y-w,x+y+v-2w,S-3w$. Reflection covers $w>v+z$. The endpoints of the two open positive intervals have value zero. There can be additional zero intervals in the middle.

Consequently only two cases can contribute.

* **Low total.** $G(1)>0>G(a)$ implies $1<S<3/2$ and $a<S-R<1$. Non-strict crossing at the endpoints adds zero. The normalized all-four-tag level leaves an auxiliary radius exponent $(T-S)/2>1/5$.
* **High total.** $G(a)>0>G(1)$ implies $a<R<1$ up to a zero endpoint, $x+y>a$, and $3a<S<3$. For the last upper bound, no triple sum reaches below one since $S>3a>2$ and $z\le1$. Thus $G(1)=S-3+\sum_{i<j}(1-x_i-x_j)_+$.

For example $p_4^2\ge p_2^5$ forces $y\le 2z/5\le .4$ and $x+y\le .8<a$. This rules out the high-total case through (1), including for every sufficiently large block before taking the profile limit. Successive doubling of the log exponents implies this separation.

The two sign cases can also be distinguished arithmetically. On the low case, $x+y\le S/2<3/4<a$. On the high case $x+y>a$. Thus the part with $p_1p_2\le B_-$ has normalized upper limit below $0.008455$ (the outward low bound $0.0084545$ plus the tiny allowance $0.0000003$), or at most $92.51\%$ of the budget. This includes all three separated classes in the table. Four occupied dyadic bands force $x\le1/8$ and $y\le1/4$, hence $x+y<a$. Any remaining high-total debit requires $p_1p_2>B_-$.

## From factor tags to arithmetic upper bounds

Write $q=(.35-.34)\log(6/5)/\log(66/65)$ and use the reflected exponent average $\mathbf E_0$ from the preceding note. At a fixed limiting block, factor out $q/b$ from the measure. For disjoint exponent bins $I_i=[l_i,u_i]$ away from zero, let $h_i$ be the occupation counts in a four-factor cell and $j_i$ the numbers of unordered tags taken in each bin. Put $\ell_i=\log(u_i/l_i)$. If the untagged factors in that cell are all at least $c$ in normalized exponent, the arithmetic upper constraint on the normalized cell masses $m_h$, after factoring out $q/b$, is
$$
 \sum_{h\ {\rm eligible}}\left(\prod_i\binom{h_i}{j_i}\right)m_h
        \le \frac1c\prod_i\frac{\ell_i^{j_i}}{j_i!},
 \qquad \sum_i j_i u_i+2c\le T.                                        \tag{3}
$$
One can apply this directly to masked sums and upper limits without assuming an arithmetic limiting distribution. Remove the tags from the squarefree partner, use the auxiliary square of radius $s^{b(c-\epsilon)}$ on the remaining cofactor, then drop its factor restrictions. This square equals one on every counted occurrence. Its independent main term gives $1/c$ after the usual normalization, while the reciprocal prime sums give the bin measures. The divisor-side coefficients include the tags, independently of the reflected triple inside the original dyadic block. Positive power slack holds with $\epsilon>0$ fixed. Refine any exterior boxes and let $\epsilon$ tend to zero after the center limit. Wheel, collision and nonsquarefree errors are as in the previous [two-tag transfer](ThreeFactorStrip.md#two-tags-at-each-actual-record). Equality surfaces have zero exponent volume in the prime sums. All arithmetic estimates below use finitely many such bounds or their positive integral over the four observed tags.

For a cutoff $e=2^{-15}$, the part with $x\le e$ costs less than $0.0000003$ across both sign cases. The positive root numerator in (1) is at most $x$ and the negative magnitude is at most $2x$ by the two negative tents. Moreover $S>1$ on either case, so at most three factors lie at or below $1/4$. Tag all of those, and sieve their cofactor at normalized radius $1/4$. The total level cost is at most $3/4+2/4<T$. Sorting the least tag and summing the others bounds the debit by
$$
 \frac{2q}{(.105-.02)(1/4)}
 \sum_{j=1}^3\int_0^e t\,\frac{\log^{j-1}((1/4)/t)}{(j-1)!}\,dt .
$$
This remains valid down to the moving wheel. For fixed positive lower endpoint the reciprocal-prime sums have the displayed limits. The remaining part tending to zero follows by dyadic intervals and Mertens' reciprocal-prime upper bound from $s^\eta$ up to $B_+^{1/4}$, or by partial summation with the factor $t^2$. Here $\eta=(\log\log s)^{-3}$. Using $\log((1/4)/e)=13\log2<9.1$ gives the stated ceiling.

For $x\ge e$ the **low-total** debit is below $0.008455$. Use all four tags in (3), taking $c$ up to $(T-S)/2$. The integral is $q\mathbf E_0[b^{-1}\int W\,2/(T-S)\prod_i dx_i/x_i]$ on the ordered low region outside $E$. For integration, its positive numerator is
$$
 G(1)=\min(S-1,x,1-v-z,2-S-z,3-2S)
$$
on its strict support, by reflection. Since $x+y\le S/2<.75<a$, the negative numerator there is $(J(a-v)+J(a-z)-J(a-v-z))_+$. These formulas allow outward cell bounds with only positive-part and endpoint comparisons. Three additional sums restrict the cells to $2z\ge5y$, successive doubling, or four distinct dyadic exponent bands. For the last restriction, each coordinate box gives a consecutive range of possible band indices. Starting with the lowest admissible index, take at each coordinate the lowest allowed index strictly above its predecessor. If that index exceeds the range, no four distinct ordered bands are possible in that box. Adding the tiny tail to each sum gives the first three lines of the table.

For $x\ge e$ the **high-total** debit is below $0.023918$. On its support $G(a)$ is given by the initial ramp formula in the proof of (1), and $-G(1)$ by the pair sum above. Equivalently,
$$
 -G(1)=\sum_{j=2}^4\min(x,1-x_j)-x
                -\sum_{2\le i<j\le4}(1-x_i-x_j)_+ .
$$
Use both expressions to enclose $W$ on each cell. The additional cap $9\delta^2/(4a)$ follows from the [three-Lipschitz bound](MixedMultiplicityTail.md#a-numerical-debit-for-four-factors-in-a-band). For each exterior range the verifier finds nonnegative multipliers for (3) with zero to three tags, retaining the full cofactor square for two or three tags as described below. It checks in integers that the weighted sum covers the upper value of $W$ on every high cell. Summing the multiplied upper capacities and rounding up gives $0.0239171$ for the high part. Using only roughness gates had given $0.025479$. The tiny, low and high allowances together give less than $0.032372 A_2$ before normalization for all sufficiently large centers.

There is also a constraint on the actual unmarked integer beyond these projections. On squarefree records set $m=t/(p_1p_2p_3p_4)$, $\tau=\log r/\log s$. All prime factors of $m$ exceed $B_+$, and the window $rt=s+O(s^{2/3})$ gives
$$
 \frac{\log m}{\log B_+}=\frac{1-\tau}{b}-S+o(1).
$$
On the high-total support the expression on the right before the $o(1)$ lies between $.65/.1475-3=83/59$ and $.66/.105-3(17/21)=27/7$ in the limiting ranges. Both endpoints have fixed slack from $1$ and $4$. Hence $m$ has one, two or three prime factors, counted with multiplicity, for all sufficiently large centers on that support. Wherever $(1-\tau)/b-S\le2-\varepsilon$ for fixed $\varepsilon>0$, $m$ must be prime. For example $b\ge.14$ and $S\ge2.75$ give this conclusion. This size restriction offers a separate way to test the high-total debit.

## A continuous comparison for the scope of (3)

The comparison certificate checks all tag locations, counts and allowed radii of (3), including ones finer than the grid used for the arithmetic upper bounds. Divide $(0,1]$ into 32 equal bins, give the first bin zero mass, and distribute the stored nonnegative mass $n_h/10^{10}$ of each occupied four-factor box independently and uniformly **in log coordinates** within its bins, symmetrizing equal-bin labels. The resulting measure is the same in scaled coordinates at every exterior parameter. Multiply by $q/b$ and average under $\mathbf E_0$ to recover the original normalization. [Integer box masses](FourFactorGateWitness.json)

For a fixed tag-bin pattern the conditional incidence density in any subrectangle of the tag coordinates is constant relative to their product log measure. Its full-bin mass multiplier before imposing the roughness condition is $\prod_i\binom{h_i}{j_i}$. To upper-bound the conditional surviving mass, retain the whole box whenever every unmarked bin has upper endpoint at least $c$. This enlarged sum is a decreasing step function. It suffices to check the upper endpoints of its constant intervals and the largest permissible gate
$$
 c_{\max}=\min\{1,(2-(8/59)/2-\sum_i j_i l_i)/2\}.
$$
This uses the largest level over all exterior parameters and the smallest tag exponents in their bins. A nonpositive $c_{\max}$ imposes no test. The capacity decreases between consecutive gates. Consequently exact checks at those finitely many points suffice even for arbitrarily fine tags, tag-dependent radii and nonnegative tag masks. The checker rounds the log measures and all capacities down before checking the integer masses. This also covers tagging all four whenever the level permits.

A separate lower sum evaluates the actual limiting four-factor profile of this comparison measure on $E^c$. It subdivides each occupied coordinate into three subintervals, discards any subbox that could be in $E$ when necessary, and rounds subinterval probabilities, exterior weights and profile lower bounds down. The certified debit exceeds $0.0111546$. The witness has 2,622 nonzero boxes. Replaying it checks 59,814 gate inequalities and computes the lower objective using integer arithmetic. Thus even the complete family of positive tag-and-roughness upper bounds does not imply the target $0.009140$. The example is not a sequence of arithmetic centers. Inputs that it has not been required to satisfy include signed mixed moments, lower sieve information, and correlations with the reflected prime triple.

## An arithmetic test that separates the comparison measure

The same dispersion estimate transfers the full auxiliary square even when an unmarked prime lies below its radius. For two unmarked exponents $u,v$ the limiting cofactor root at radius $c$ is $\max(0,\min(c,u,v,u+v-c))/c$. For one unmarked exponent $u$ it is $\min(1,u/c)$. On the old rough-cofactor event these squares equal one. Elsewhere they can still give a strictly positive contribution to the left side of an upper constraint with exactly the same right side. The fixed-factor profile approximation is uniform on the marked sample, with the fixed-factor mass bound absorbing its error. We also use these stronger coefficients in the high-total calculation: for each remaining bin substitute its lower endpoint, round the square contribution down in units of $1/1024$ and verify the resulting covering inequalities.

For a concrete test mark two primes in $I=[25/32,26/32]$ and put $c=1/8$. The level cost is at most $2(26/32)+2/8=1.875<40/21\le T$ in the limiting blocks. In the units of (3), the genuine arithmetic upper bound for this square is $4\log^2(26/25)<0.0061531$. On the stored comparison measure the same integral is **at least** $1011061313/160000000000>0.0063190$, just by substituting the two unmarked lower bin endpoints in the tent. A pair is counted with its actual binomial multiplicity. This gives an explicit arithmetic distinction between the model and the real problem. The comparison argument concerns (3) alone. It leaves open how far the stronger square tests can be taken.

A further test has an explicit price. For two radii $0<c<d$ with $\sum_i j_i u_i+2d<T$, use the square $(F_c-\lambda F_d)^2$ on the cofactor, where the subscripts here denote normalized radius exponents. For fixed real $\lambda$ its right side in the units of (3) is
$$
 \left(\frac1c+\frac{\lambda^2-2\lambda}{d}\right)
 \prod_i\frac{\ell_i^{j_i}}{j_i!}.
$$
Indeed the nested Selberg roots have cross moment $1/G(B_+^d)$ in the independent zero mode, and the square transfers with the indicated level slack. This gives a test on the two remaining primes which uses their joint profile at two radii. The numerical upper bounds above use only single-radius squares. [Nested-root moment](CompositePartnerWeight.md#a-mixed-product-below-the-old-reference-constant)

## Reproduction

Run `python -B CheckFourFactorScales.py` in this directory with NumPy, SciPy and Numba installed. The run used Python 3.9.16, NumPy 1.23.5, SciPy 1.10.0 and Numba 0.56.4. The option `--witness-only` checks the sign formula and the stored comparison measure without solving a linear program. The high-total calculation uses the HiGHS interior-point solver only for candidate multipliers. It rounds those up, repairs any deficits and verifies all covering inequalities and prices independently. Use `--rebuild-witness` to regenerate the comparison file.

The low integral uses a relative mesh near zero and maximum width $1/320$ elsewhere, or $1/170$ for the separated sums. Equal-bin factorials account for ordering. All sign and level endpoints are integers on a $2^{21}$ grid. Each positive box price in the low integral uses at most 20 normal binary64 arithmetic operations, is enlarged by $1+2^{-40}$ and rounded up to an integer in units of $2^{-58}$ before summation. The high calculation uses 44 linear panels plus finer bins near zero. The true exterior measure is bracketed on 16 equal-probability panels per coordinate with outward rational endpoints for the two geometric quantiles. The verifier also checks (1) at 59,895 finite profile points including the candidate zeros. [Reproducible checker](CheckFourFactorScales.py)
