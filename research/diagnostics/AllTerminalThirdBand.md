# All terminal denominators for the signed third-band integral

**Research note, 27 November 2026. Status: paper argument for independent review.**

Let $N$ be a sufficiently large even integer and set $R=\lfloor N^{1/3}\rfloor$, $V=\lfloor N^{2/3}\rfloor$, $U=\lfloor N^{1/16}\rfloor$, $H=256R\lfloor\log_2(N+2)\rfloor^2$. Write $e(x)=\exp(2\pi i x)$,
$$
 C(a)=\sum_{v\mid a,\,v>U}\mu(v),\qquad
 T(\alpha)=\sum_{R<a\le V}C(a)\sum_{U<r\le N/a}\Lambda(r)e(ar\alpha).
$$
The outer range may optionally be restricted to $3\mid a$. For $1\le q\le R$ define
$$
 I_q(N)=\int_{-H/(qN)}^{H/(qN)} e(-N\beta)
        \sum_{c\bmod q}^{*} e(-Nc/q)T(c/q+\beta)^2\,d\beta .
$$
The numerator sum is signed and complete, and the square is an ordinary square. These are the wide arcs in the upstream full-circle subtraction identity. The argument below treats imprimitive characters, nonunit product frequencies, repeated prime factors of $q$, and $q$ sharing factors with $N$. [Frozen FW-8005 statement](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/2739) · [Preceding prime-denominator estimate](PrimeDenominatorThirdBand.md)

**Claim.** Uniformly for each such $N$ and every $\varepsilon>0$,
$$
 \sum_{R/3<q\le R}|I_q(N)|\ll_\varepsilon N^{155/156+\varepsilon},
 \qquad
 \sum_{N^{5/16}\le q\le R}|I_q(N)|\ll_\varepsilon N^{239/240+\varepsilon}. \tag{1}
$$
In particular both bounds include the whole square at balanced semiprime denominators. More generally, fix $c_0>0$, $0\le s<1/36$. For $c_0 N^{1/3-s}\le q\le R$ one obtains exponent $1-\zeta(s)+\varepsilon$, where
$$
 \zeta(s)=\min\{1/156,\ 1/60-3s/5\}.
$$
Empty ranges give zero. The same proof allows any measurable subintervals of the stated $\beta$-ranges that depend only on $q$. In particular it can cover the wings left by translation in the $3\mid a$ restriction. Small-denominator wide arcs and the full-circle coefficient remain in FW-8005. Bound (1) does not establish the deep-arc parent inequality.

### 1. Product cutoff and total energy

Work in one dyadic band $Q/2<q\le Q$, truncating at the requested endpoints. Write $Q=N^{1/3-\sigma}$ up to a bounded factor, with $0\le\sigma\le s+O(1/\log N)$. Put $Z=N^\zeta,\ \kappa=\max(2\zeta,\sigma),\ \Delta=N^{-\kappa}$. Partition the outer variable into intervals $(x,y]$ with $y/x\le1+\Delta$; in each keep only $r\le N/y$ and then split $r$ dyadically. Call the resulting polynomial $T_*$. The omitted frequencies lie in $N/(1+\Delta)<ar\le N$. All coefficients, with absolute record multiplicity, are $N^{o(1)}$ by the divisor bound. The full family of wide arcs is disjoint on the circle eventually, because $2HR<N$. By Parseval and Cauchy–Schwarz the sum over this band of absolute errors in the signed integrals is at most $N^{1-\kappa/2+o(1)}$. Here and below $N^{o(1)}$ permits an arbitrarily small positive exponent, uniformly in all divisors.

For $S_q(c,\beta)=T_*(c/q+\beta)$ write $S_f$ for its component on the characters modulo $q$ of exact conductor $f\mid q$; the dependence on $q,\beta$ is implicit. The counting norm is $\|S_f\|_q^2=\sum_c^*|S_f(c,\beta)|^2$. Orthogonality and disjoint arcs give
$$
 \sum_{q\asymp Q}\int \sum_{f\mid q}\|S_f\|_q^2\,d\beta
 \le \int_0^1 |T_*(\alpha)|^2\,d\alpha \le N^{1+o(1)}. \tag{2}
$$

### 2. Energy of an induced component

For $q=fh$ and $f>1$, each character of exact conductor $f$ is induced from a primitive $\chi\bmod f$. For any integer $k$,
$$
 \sum_{c\bmod q}^*\bar\chi(c)e(ck/q)=
 \tau_f(\bar\chi)\!
 \sum_{\substack{b\mid h,\ (b,f)=1\\ t=h/b,\ t\mid k}}
 \mu(b)\bar\chi(b)\,t\,\chi(k/t). \tag{3}
$$
Characters are zero at nonunits. Expand the coprimality conditions at primes outside $f$, set $c=bw$, and split the sum on $w\bmod ft$ into lifts of residues mod $f$. This gives $t{\bf1}_{t\mid k}$ times the primitive Gauss sum at $k/t$. In particular $|\tau_f(\bar\chi)|=\sqrt f$. If $w_*(k)$ denotes the coefficients of $T_*$, put $X_{\chi,t}=\sum_{t\mid k}w_*(k)e(k\beta)\chi(k/t)$. Parseval in the finite character group, (3) and Cauchy–Schwarz in $b$ imply
$$
 \|S_f\|_q^2 \le \frac{N^{o(1)}}{h}
       \sum_{t\mid h} t^2\sum_{\chi\bmod f}^{\rm prim}|X_{\chi,t}|^2. \tag{4}
$$
This uses $f/\varphi(q)\le\tau(q)/h$.

For fixed $h,t\mid h$ (with $h\asymp J$, $f\asymp F=Q/J$ and $f>1$), the following uniform estimate is sufficient:
$$
 \sum_{f\asymp F}\sum_{\chi\bmod f}^{\rm prim}|X_{\chi,t}|^2
       \ll N^{2\kappa+o(1)} U^2 F R^4 . \tag{5}
$$
To see it, first take one unphased subrectangle at scales $a\asymp A,\ r\asymp M$, $A,M\ll R^2,\ AM\ll N$. Whenever $a=v n$ with $v$ fixed, $vn>1$ throughout the range and
$$
 C(vn)=-\sum_{u\le U}\mu(u)\,{\bf1}_{u/(u,v)\mid n}.
$$
The optional $3\mid vn$ condition adds only another divisibility condition. For every interval of $n$ so obtained the weighted character sum $\sum_n C(vn)\chi(n)$ is $O(U\sqrt f\log(2f))$, uniformly in $v$. For each of the at most $U$ labels the progression consists of multiples of a step; a step sharing a factor with $f$ gives zero. Otherwise use the interval Pólya–Vinogradov bound for a primitive character. It follows by completing the interval modulo $f$: the primitive Gauss transform has size at most $\sqrt f$, and the sum of absolute unnormalised interval Fourier coefficients at nonzero frequencies is $O(f\log(2f))$.

If $(r,t)=1$, the condition $t\mid ar$ is $t\mid a$. Set $a=tn$, use the preceding supremum bound on the outer character sum, and apply the multiplicative large sieve to the inner coefficients $\Lambda(r){\bf1}_{(r,t)=1}$. Its squared norm summed over $f,\chi$ is $O((F^2+M)M N^{o(1)})\le R^4 N^{o(1)}$. If $(r,t)>1$ and $\Lambda(r)\ne0$, then $r$ is a power of a prime dividing $t$, giving $N^{o(1)}$ possible values. For each such $r$, put $g=(r,t)$, $a=(t/g)n$; the remaining character is $\chi(n)\chi(r/g)$. The same outer estimate applies. There are $O(F^2)$ characters over the indicated moduli, giving squared norm $O(U^2F^3N^{o(1)})$ for this part. These bounds hold on all initial subrectangles. [Multiplicative large sieve and primitive Gauss formula, Theorem 18.2](https://kskedlaya.org/ant/chapter-18.html)

For the phase, factor $e(\beta ar)=e(\beta x r)e(\beta(a-x)r)$ on the outer interval $(x,y]$. Absorb the first factor into the inner coefficients, independent of the varying conductor. The rare prime-power case allows the same factor. Two-dimensional partial summation restores the second factor with variation $O(1+|\beta|\Delta AM+(|\beta|\Delta AM)^2)=N^{o(1)}$, since $|\beta|N\ll N^\sigma\log^2(2N)$ and $\kappa\ge\sigma$. Use the triangle inequality on common endpoint integrals in the norm over $f,\chi$. Summing the $N^{\kappa+o(1)}$ rectangle norms before squaring proves (5).

For any fixed $d\mid N$ and $B\ge1$, (4) and (5) now imply
$$
 \sum_{q\asymp Q}\int
   \sum_{\substack{q=fh,\ f>1\\d\mid h,\ h/d\le B}}\|S_f\|_q^2\,d\beta
 \ll N^{19/24+2\kappa+o(1)} B. \tag{6}
$$
Indeed, for $h\asymp J$ there are $O(J/d)$ eligible multiples of $d$ when this range is nonempty, and $h^{-1}\sum_{t\mid h}t^2\le J N^{o(1)}$. With $F\asymp Q/J$ this costs $N^{2\kappa+o(1)}U^2 Q R^4(J/d)$ before integration. Multiply by $O(H/(QN))$, use $U^2 R^5/N\ll N^{19/24}$, and sum dyadic intervals subject to $J/d\ll B$.

### 3. The target phase between two conductors

In the product $S_f S_j$ put $L={\rm lcm}(f,j)$, $m=q/L$, $d=(m,N)$. The product depends on $c\bmod L$. For every unit $u\bmod L$, the mean of $e(-Nc/q)$ over the unit lifts $c\equiv u\bmod L$ has absolute value at most $N^{o(1)}d/m$. For a direct proof insert the Möbius sum for coprimality at the primes outside $L$. Each divisor label $b\mid m$ prime to $L$ gives a progression of $m/b$ residues on which the phase sum vanishes unless $m/b\mid N$, in which case its magnitude is $m/b$. The absolute numerator is at most $\sum_{v\mid d}v$, and the number of lifts is $\varphi(q)/\varphi(L)\ge m/\tau(q)$. This argument also works when $L$ and $m$ are not coprime.

When $m/d>Z$, the signed numerator sum costs at most $N^{o(1)}Z^{-1}\|S_f\|_q\|S_j\|_q$. Sum over all such pairs using the divisor bound and (2), giving $N^{1+o(1)}/Z$.

When $m/d\le Z$, take $f=\max(f,j)$ after exchanging the two labels if necessary. If $f>1$, then
$$
 f^2\ge L=q/m\ge q/(d Z),\qquad
 d\mid q/f=h,\qquad h/d\le \sqrt{Q Z/d}.
$$
Thus one side is covered by (6) with this $d$ and $B$, while the other is covered by (2). For each $d$, Cauchy–Schwarz in the pairs, $q$, and $\beta$ bounds the product of their integrated energy norms. A given component is repeated at most $\tau(q)$ times on either side for each $q,d$; summing over $d\mid N$ costs $N^{o(1)}$. The resulting bound is
$$
 N^{43/48+\kappa+o(1)}(QZ)^{1/4}. \tag{7}
$$
The remaining $f=j=1$ term can be treated over the entire band. The constant numerator coefficient is
$B_q=\varphi(q)^{-1}\sum_k w_*(k)e(k\beta)c_q(k)$, where $c_q$ is the Ramanujan sum. Thus $|B_q|\le N^{1+o(1)}/q$ since $|c_q(k)|\le(q,k)$ and $\sum_{k\le N}(q,k)\le N\tau(q)$. Its signed square is $c_q(N)B_q^2$. Since $\sum_{q\le Q}|c_q(N)|\le Q\tau(N)$, its integrated cost is $N^{1+o(1)} R/Q^2$.

### 4. Choice of exponents

The shell and the first phase case cost $N^{1-\kappa/2+o(1)}$ and $N^{1-\zeta+o(1)}$. The constant pair costs $N^{2/3+2\sigma+o(1)}$. The exponent in (7) is $47/48-\sigma/4+\kappa+\zeta/4$. If $\kappa=2\zeta$ this is at most $1-\zeta$ for $\zeta\le1/156$. If $\kappa=\sigma$ the same comparison holds for $\zeta\le1/60-3\sigma/5$. These inequalities give the stated $\zeta(s)$; the number of dyadic bands and bounded endpoint factors are absorbed in $N^{o(1)}$. The two displayed cases of (1) use $s=0$ and $s=1/48$, respectively.

This controls only the stated wide-arc integrals. As $s$ approaches $1/36$ the saving obtained here tends to zero. At smaller denominator scales one must re-estimate the longer $\beta$-intervals or use different arithmetic information, and the signed full-circle term still requires its own lower bound.
