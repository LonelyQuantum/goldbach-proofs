# Terminal prime denominators of the third-band coefficient

Let \(N\) be a sufficiently large even integer, \(R=\lfloor N^{1/3}\rfloor\), \(V=\lfloor N^{2/3}\rfloor\), \(U=\lfloor N^{1/16}\rfloor\), and \(H=256R\lfloor\log_2(N+2)\rfloor^2\). Put \(e(t)=\exp(2\pi i t)\), \(\delta_q=H/(qN)\), and
\[
 T(\alpha)=\sum_{R<a\le V} C(a)\sum_{U<r\le N/a}\Lambda(r)e(ar\alpha),
 \qquad C(a)=\sum_{d\mid a,\ d>U}\mu(d).
\]
We permit either the full outer range or its restriction to \(3\mid a\) throughout. For \(R/3<q\le R\), let
\[
 I_q=\int_{-\delta_q}^{\delta_q}e(-N\beta)
       \sum_{c\bmod q}^{*} e(-Nc/q)\,T(c/q+\beta)^2\,d\beta .
\]
The reduced numerators for one denominator are summed with their phases before taking an absolute value. All constants below are uniform in the target \(N\). Powers \(N^{o(1)}\) can be replaced by \(O_\varepsilon(N^\varepsilon)\) for each \(\varepsilon>0\).

**Fixed-target bounds.** The following are paper deductions for the frozen third-band weight.
\[
 \sum_{\substack{R/3<q\le R\\q\ {\rm prime}}}|I_q|
       \ll_\varepsilon N^{47/48+\varepsilon}.                                      \tag{1}
\]
More generally, for \(D=N^{1/512}\),
\[
 \sum_{\substack{R/3<q\le R\\q=b p,\ b\le D,\ p\ {\rm prime}}}|I_q|
       \ll_\varepsilon N^{63/64+\varepsilon}.                                      \tag{2}
\]
Both bounds include primes dividing \(N\) and all prime powers in \(\Lambda\). Neither requires GRH. The full third-band lower bound continues to require the other terminal denominators, the rest of the wide arcs and comparison with the full-circle coefficient. [Upstream third-band formula, FW-8005](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2739)

## Making the hyperbolic cutoff rectangular

Fix \(\Delta=N^{-\kappa}\). Partition \(R<a\le V\) into intervals \((x,y]\) of ratio \(y/x\le1+\Delta\), for instance by successive geometric endpoints and truncation at \(V\). In a block use \(r\le N/y\). The omitted records have \(N/(1+\Delta)<ar\le N\). Each coefficient of the original sum, the rectangular sum \(T_*\), or their difference is \(N^{o(1)}\) in absolute value, by the divisor bound also applied to \(C(a)\). Parseval therefore gives
\[
 \|T-T_*\|_2\ll N^{o(1)}(\Delta N+1)^{1/2},\qquad
 \|T+T_*\|_2\ll N^{1/2+o(1)}.
\]
The arcs are disjoint for large \(N\) since \(2HR<N\). For any family of whole terminal denominators, summing the absolute error of their signed integrals costs \(N^{1+o(1)}\sqrt\Delta\) for the choices below. This is a single estimate on the original circle, before splitting into residue classes or characters. Further split \(r\) dyadically. There are \(N^{\kappa+o(1)}\) rectangles with scales \(A\asymp x\), \(M\) such that \(a\asymp A,\ r\asymp M,\ A\gg R,\ A,M\ll R^2,\ AM\ll N\).

## The two character estimates

For use in (2), allow restrictions \(a\equiv i,\ r\equiv j\bmod b\), where \(b\le D\). In (1) take \(b=1\). In either case take primes \(p\) with \(R/(3b)<p\le R/b\). In particular \(p>\max(b,U,3)\) for large \(N\). Nonprincipal characters modulo \(p\) are primitive. Extend all characters by zero at multiples of \(p\).

On any initial subinterval of an outer rectangle put \(F_\chi=\sum C(a)\chi(a)\), including its stated masks. Then
\[
 \sum_{\chi\ne1\bmod p}|F_\chi|^2
       \ll N^{o(1)}\min\{(A+p)A,\ U^2p^2\}.                                      \tag{3}
\]
For the first bound use character orthogonality on the unit residues and Cauchy–Schwarz within a residue class. For the second, \(a>1\) implies \(C(a)=-\sum_{d\mid a,\ d\le U}\mu(d)\). For each divisor label \(d\), its multiples satisfying the masks lie in an empty set or one arithmetic progression, with step dividing \({\rm lcm}(3,b,d)\) and prime to \(p\). Complete periods of the progression contribute zero to every nonprincipal character. The remaining segment contains at most \(p\) distinct residues, so its character vector has \(\ell^2\) norm at most \(p\) by orthogonality. Sum the norms over \(d\le U\). On the same subintervals we also have
\[
 \max_{\chi\ne1}|F_\chi|\ll U\sqrt p\log(2p).                                     \tag{4}
\]
For each progression, multiply the variable by the inverse of the step modulo \(p\) to obtain a shifted interval character sum up to a constant of modulus one. Completing that interval gives (4) by the \(\sqrt p\) Gauss sum and the \(O(p\log(2p))\) sum of absolute unnormalised interval Fourier coefficients.

For \(G_\chi=\sum\Lambda(r)\chi(r)\) on any initial subinterval of the inner rectangle, include the mask on \(r\). The multiplicative large sieve gives
\(\sum_p\sum_{\chi\ne1}|G_\chi|^2\ll (R^2+M) M N^{o(1)}\ll R^2M N^{o(1)}\).
At a single \(p\) orthogonality instead gives \(\sum_\chi|G_\chi|^2\ll(p+M)M N^{o(1)}\). Both estimates allow the sharp interval endpoints. [Bombieri–Davenport inequality and Gauss expansion, Theorem 18.2](https://kskedlaya.org/ant/chapter-18.html)

For the coefficients \(w_*(k)\) of the rectangular sum (with the chosen masks) set
\(X_\chi(\beta)=\sum_k w_*(k)\chi(k)e(k\beta)\) and \(L_p=\sum_{\chi\ne1}|X_\chi(\beta)|\).
Uniformly for \(|\beta|\le3H/(RN)\),
\[
 \sum_p L_p^2\ll N^{2\kappa+o(1)} R^3 U N .                                       \tag{5}
\]
Indeed on one unphased subrectangle apply Cauchy–Schwarz in \(\chi\) at fixed \(p\) to \(F_\chi G_\chi\) and sum in \(p\). By (3),
\(\min\{(A+p)A,U^2p^2\}\ll AUR\), using \(A\gg R\) and the geometric mean of the two bounds. Thus the squared norm is at most \(N^{o(1)}R^3 U AM\). To restore \(e(ar\beta)\), apply two-dimensional partial summation to the rectangle. Its corner, boundary derivatives and mixed derivative have total variation \(O(1+|\beta|AM+(|\beta|AM)^2)\ll\log^4(2N)\). Use the triangle inequality in \(\ell^2_p(\ell^1_\chi)\) under these common endpoint integrals. Finally sum the rectangle norms before squaring. This accounts for the factor \(N^{2\kappa+o(1)}\). For a single \(p\), (4) and the fixed-modulus inner bound give by the same argument
\[
 \sum_{\chi\ne1}|X_\chi(\beta)|^2\ll N^{2\kappa+o(1)} U^2 R^5 .                   \tag{6}
\]

## The signed sum over numerators

At prime modulus \(p\) and fixed \(\beta\), let \(Z=\sum_{p\mid k}w_*(k)e(k\beta)\), \(B=Z-X_1/(p-1)\), and \(S_c=\sum_k w_*(k)e(k\beta)e(ck/p)\). Thus \(|B|\ll N^{1+o(1)}/p\), also with the extra masks. Multiplicative Fourier inversion gives for each unit \(c\)
\[
 S_c=B+\frac{1}{p-1}\sum_{\chi\ne1}\tau(\bar\chi)\chi(c)X_\chi(\beta),
 \qquad \tau(\bar\chi)=\sum_{t\bmod p}^*\bar\chi(t)e(t/p).
\]
If \(p\nmid N\), the sum over \(c\) of a character against \(e(-Nc/p)\) has absolute value at most \(\sqrt p\), and is \(-1\) for the principal character. Expanding the square gives an upper bound \(O(|B|^2+|B|L_p+p^{-1/2}L_p^2)\), hence
\[
 \left|\sum_{c\bmod p}^*e(-Nc/p)S_c^2\right|
       \ll \sqrt p\,|B|^2+p^{-1/2}L_p^2.                                          \tag{7}
\]
For \(p\mid N\) orthogonality kills the linear term and pairs a character only with its inverse. The bound is instead \(O(p|B|^2+\sum_{\chi\ne1}|X_\chi|^2)\). Both statements apply to products for two different masks by expansion or polarization, with the sum of the two corresponding squared-norm bounds.

For (1), take \(b=1,\ \kappa=1/24\). The common integration length is \(N^{-1+o(1)}\). By (5) and (7) the quadratic error for \(p\nmid N\) is at most
\(N^{2\kappa+o(1)}R^{5/2}U=N^{47/48+o(1)}\).
The constant contribution in (7) is \(N^{5/6+o(1)}\) after summing all primes and integrating. Only \(O(1)\) terminal primes divide \(N\). From (6) their nonconstant contribution is \(N^{7/8+o(1)}\), and their constant contribution is \(N^{2/3+o(1)}\). The discarded shell costs \(N^{47/48+o(1)}\). This proves (1).

**Connection with the earlier unit-residue question.** For \(p\nmid N\) the same bound holds with both \(k,l\) restricted to units mod \(p\). In (7) set \(Z=0\). For the shell transfer on this modulus-dependent mask, the removed multiples of \(p\) have shell amplitude at most \(N^{o(1)}(\Delta N/p+1)\) on each of its arcs, and full amplitude \(O(N^{1+o(1)}/p)\). Their summed shell and full squared norms over the arcs are respectively \(O(\Delta^2 N^{1+o(1)})\) and \(O(N^{1+o(1)})\). Together with Parseval for the unmasked weights these imply the same \(N^{1+o(1)}\sqrt\Delta\) transfer for the unit-restricted square.

For the previously isolated discrepancy in the \(3\mid a\) packet, take \(3\nmid N\), use the prime-only inner weight from the outset and restrict both endpoints \(k,l\) to units, with \(p\nmid N\). There is no \(h=k+l-N=0\) term. For \(0<|h|\le N^{7/12}\) there are at most \(N\) endpoint pairs of total absolute multiplicity \(N^{o(1)}\) per pair. Sum \(|c_p(h)|\le(p,h)\) over \(p\le R\), using \(\sum_{q\le R}(q,h)\le R\tau(|h|)\), and multiply by \(2\max\delta_p\). This costs \(N^{11/12+o(1)}\). Replacing \(c_p(h)=p{\bf1}_{p\mid h}-1\) by \(c_p(h)+(p-1)^{-2}\) on the retained records costs \(N^{2/3+o(1)}\) by counting all pairs and using \(p\asymp R\). Thus the same \(o(N)\) bound reaches that specific centered congruence sum.

## Moduli with a small cofactor

Take \(q=bp\) in (2). Here \(p>b\) and the representation with \(b\le D\) is unique for large \(N\), since \(p>\sqrt R\). On summing reduced numerators, the original kernel is \(c_{bp}(k+l-N)=c_b(k+l-N)c_p(k+l-N)\) by the Chinese remainder theorem. The factor \(e((k+l-N)\beta)\) and the width \(\delta_{bp}\) stay unchanged. Split each of \(a,r,a',r'\) into its residue class modulo \(b\). There are at most \(b^4\) choices and the first Ramanujan factor is then constant, of absolute value at most \(b\). For each choice apply (5)–(7) to the two masks at prime \(p\). We apply the shell bound once to the original family of arcs before these splits.

Put \(\kappa=1/32\). For fixed \(b\) and fixed masks the integrated quadratic bound in the nonsingular case is \(b^{1/2}N^{23/24+o(1)}\), using \(p\asymp R/b\). The corresponding constant bound is \(b^{1/2}N^{5/6+o(1)}\). Among primes in this interval only \(O(1)\) divide \(N\), uniformly for \(b\le D\). Their integrated contributions per choice of masks are bounded by \(N^{19/24+2\kappa+o(1)}+bN^{2/3+o(1)}\) using (6). After the \(b^5\) cost and summation, all these bounds together are at most \(D^7 N^{23/24+o(1)}\). Since \(23/24+7/512<63/64\), the shell \(N^{63/64+o(1)}\) gives (2).

For the remaining terminal moduli \(q\) every prime divisor \(p\mid q\) satisfies \(q/p>N^{1/512}\). A subsequent estimate has to address this range, where rebuilding a full modulus by the above residue-class splits becomes too expensive. All statements here concern the written mathematical argument; the parent problem is still open.

## A further reduction for the remaining composite denominators

For each \(R/3<q\le R\) coprime to \(N\), let \(P_q\) be the orthogonal projection of functions of the unit numerator \(c\bmod q\) onto the span of the primitive multiplicative characters of conductor exactly \(q\). This projection acts separately at each fixed \(\beta\). Replace \(T(c/q+\beta)^2\) in \(I_q\) by \([P_q(T(\cdot/q+\beta))(c)]^2\), and call the result \(I_q^{\rm prim,prim}\). Then
\[
 \sum_{\substack{R/3<q\le R\\(q,N)=1}} |I_q^{\rm prim,prim}|
       \ll_\varepsilon N^{47/48+\varepsilon}.                                     \tag{8}
\]
Here the denominators may be arbitrary composites. Use the unmasked inner range and either original outer range. For a primitive character its numerator Fourier coefficient is \(\tau_q(\bar\chi)X_\chi/\varphi(q)\), also for nonunit input frequencies, since the primitive Gauss sum at a nonunit frequency vanishes. In (3), a progression consists of multiples of \(d\), or of \({\rm lcm}(3,d)\) with the outer mask. If its step shares a prime with \(q\), it contributes zero to every primitive character; otherwise a full period runs over all residues. Thus (3) still holds with \(q\) in place of \(p\), summed over just primitive characters. The large sieve on the inner factor sums precisely these characters over all moduli, so (5) holds with that choice as well.

For any product character modulo \(q\), its numerator Gauss sum at \(-N\) has magnitude at most \(\sqrt q\). Indeed, for a character induced from conductor \(f\mid q\), expand the coprimality conditions at primes of \(q\) outside \(f\) by Möbius inversion. For each divisor label \(d\) the resulting sum is over a multiple of \(f\) of length \(q/d\). Summing its periods of length \(f\) gives zero unless \(q/d=f\), since \((q,N)=1\). The surviving primitive Gauss sum has magnitude \(\sqrt f\); conductor 1 is included. Thus the signed numerator square is bounded by \(q^{3/2}L_q^2/\varphi(q)^2\ll q^{-1/2+o(1)}L_q^2\), using \(\varphi(q)\ge q/\tau(q)\). Bound (5) and \(\kappa=1/24\) give (8) for the rectangles. Orthogonal projection is a contraction in \(\ell^2_c\), so the same integrated shell estimate as before transfers (8) back to the sharp product cutoff.

In particular at the balanced semiprime moduli \(q=p_1p_2\) coprime to \(N\), the remaining terms involve at least one character induced from a proper divisor (including the principal character). One must also allow denominators sharing a factor with \(N\). Bound (8) is for a projected square; it does not bound its cross term with the complementary projection.
