# Two surviving composite endpoints near a prime square

Fix a large odd prime $p$. Let $H=\lfloor p^{4/3}\rfloor$, $L=\lfloor\sqrt p\rfloor$, and $z=p-L$. Call a positive integer rough if all its prime factors exceed $z$. For $1\le h\le H$, examine $n_+=p^2+h$ and $n_-=p^2-h$. Because $z^3>p^2+H$ for large $p$, each rough composite in this window factors as two odd primes exceeding $z$, with multiplicity allowed.

**Claim.** If both $n_+$ and $n_-$ are rough composites then for some integers $1\le k\le H/p$ and $u,v\ge0$ their factorizations have the form
$$
 n_+=(p+k-u)(p+k+u),\qquad n_-=(p-k-v)(p-k+v),\qquad
 u^2+v^2=2k^2.
$$
In particular $|h-2pk|\le k^2$. The number of such positive offsets is $O((H/p)\log(2+H/p))=O(p^{1/3}\log p)$, uniformly over the prime $p$. This controls the case with two composite endpoints. A surviving pair with one prime and one composite requires a different estimate, given below.

## Why the factor midpoints add to $2p$

The integer lemma admits a more general margin $b\ge0$ with $b^2<p-b$. Suppose each factor is at least $p-b$ and the factors of each product have the same parity. Order the factors and write their midpoints as $p+k,p+l$ and their nonnegative half-differences as $u,v$. Thus $u\le b+k$ and $v\le b+l$. Adding the two factorizations gives
$$
 2p(k+l)+k^2+l^2=u^2+v^2 .
$$
Bounding the right-hand side by $(b+k)^2+(b+l)^2$ gives $(p-b)(k+l)\le b^2<p-b$, hence $k+l\le0$. If $k+l\le-1$, both $k$ and $l$ belong to $[-b,b]$. The left-hand side is then at most $-2p+2b^2<0$. This proves $l=-k$ and the square identity. At the stated cutoff choose $b=L-1$; every surviving factor is at least $p-b$, and $(L-1)^2<p-(L-1)$.

The upper endpoint gives $h=2pk+k^2-u^2$. Since $p+k\ge p-b>0$ and $(p+k)^2\ge p^2+h$, one has $k>0$. Also $k\le b<p$ from $v\le b-k$. The square identity yields $h\ge k(2p-k)\ge pk$ and $|h-2pk|\le k^2$. The Lean file proves these integer assertions starting directly from four ordered factors, including the parities of their sums. [Standalone Lean proof](./L_goldbach_reflected_factor_centers.lean)

## Counting the offsets

The two half-differences have the same parity since their squares sum to $2k^2$. Set $A=(u+v)/2$ and $B=(u-v)/2$. Then $A^2+B^2=k^2$. If $B=0$, one has $u=v=k$ and $h=2pk$, giving at most one offset per $k$. If $B\ne0$, the triple $(A,|B|,k)$ is a positive integer Pythagorean triple. A primitive triple of hypotenuse at most $X$ arises from $s^2+t^2\le X$ for two positive integers $s,t$, so there are $O(X)$ choices. Allowing all common factors gives $O(\sum_{j\le X}X/j)=O(X\log(2+X))$. Signs and the order of the legs contribute a bounded factor, and $h$ is determined by $k,u$. Taking $X=H/p$ proves the claim. The Lean file covers the integer reduction; this counting argument uses the classical parametrization. [Mathlib's classification of primitive Pythagorean triples](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/PythagoreanTriples.html) · [Keith Conrad, Theorem 1.2](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pythagtriple.pdf)

There is a further necessary local condition for $z\ge3$. If $3\nmid k$, reduction of the square identity modulo 3 forces both $u,v$ to be nonzero modulo 3. To keep both $p+k\pm u$ indivisible by 3 would then require $p+k=0\bmod 3$. The other endpoint would require $p-k=0\bmod 3$. These two congruences contradict $3\nmid k$. Hence $3\mid k$, and reduction of the same identity then gives $3\mid u,v$.

## One rough prime paired with a rough composite

Let $T_z$ count offsets with two rough endpoints, and $r$ those where both endpoints are prime. Write $M_z$ and $D_z$ for the numbers with respectively one and two composite endpoints among the offsets counted by $T_z$. Exactly $T_z=r+M_z+D_z$.

For each composite endpoint, its smaller prime factor $q$ lies between $p-L$ and $\sqrt{p^2+H}$. The interval has length $O(\sqrt p)$, so the one-dimensional upper sieve on a translated interval gives $O(\sqrt p/\log p)$ possible prime $q$. For each $q$ the other factor $s$ ranges over an interval of length $U=2H/q\asymp p^{1/3}$. In a surviving pair neither $s$ nor $2p^2-qs$ has a prime divisor at most $U^{1/4}$. This cutoff is eventually smaller than $q,p,z$. The two forms have one forbidden residue modulo 2 and two distinct forbidden residues modulo every other sieve prime. The Selberg upper bound is $O(U/\log^2 U)$, uniform in $q$ and the translate. In either use of the sieve the remainder per squarefree modulus is at most the number of forbidden classes; at cutoff $U^{1/4}$ the summed remainders in dimension two are $O(U^{1/2}\log^5 U)$. In the dimension-one application take the fourth root of an enclosing interval length comparable to $\sqrt p$. Thus
$$
 0\le T_z-r=M_z+D_z \ll p^{5/6}/\log^3 p,\qquad D_z\ll p^{1/3}\log p .
$$
The first estimate counts at least one orientation of every surviving offset with a composite endpoint. Its log saving comes from using the primality of $q$ and the two sieve conditions on $s$. The bound for $D_z$ isolates the remaining mixed case. A uniform lower bound for $T_z$ exceeding the first error would yield a central prime pair; that lower bound remains open. [Heath-Brown, §3, equation (3.8)](https://arxiv.org/pdf/math/0209360#page=22)

## An exact test for one rough endpoint

For all sufficiently large $p$, a rough endpoint $n$ is composite exactly when $\lceil\sqrt n\rceil^2-n$ is a square (including zero). Indeed, for $n=qs$ as above with $q\le s$, the integer factor midpoint satisfies
$
 0\le (q+s)/2-\sqrt n=\frac{(\sqrt n-q)^2}{2q}
 \le\frac{(L+H/(2p))^2}{2(p-L)}=\tfrac12+O(p^{-1/6})<1.
$
It must therefore equal $\lceil\sqrt n\rceil$, and the gap is $((s-q)/2)^2$. Conversely a square gap $d^2$ gives $n=(\lceil\sqrt n\rceil-d)(\lceil\sqrt n\rceil+d)$ with both factors greater than one for large $n$, since $d^2<2\lceil\sqrt n\rceil$ and the smaller factor tends to infinity. This is the first trial in Fermat's factorization method. Here the roughness and window size guarantee that one trial suffices.

## Finite checks

For $p=101,1009,10007$ the counts $(r,M_z,D_z,T_z)$ are respectively $(8,1,0,9)$, $(64,2,0,66)$, and $(825,6,0,831)$. These use exact integer cube roots of $p^4$ for the radius and integer square roots for the cutoff. Mark multiples of primes up to $z$ in the window, then independently mark through $\lfloor\sqrt{p^2+H}\rfloor$ to distinguish prime endpoints. Pair the two lists at each positive offset.

A nondegenerate example is $p=550531$, $h=42940338$. The upper endpoint factors as $550519\cdot550621$ and the lower endpoint as $550471\cdot550513$. All four factors are prime, exceed $p-741$, and $h^3\le p^4$. They give $k=39$, $u=51$, $v=21$, and the triple $(36,15,39)$. Trial division through the integer square root verifies primality of the center base and all four factors. This example shows why the two-composite term must be retained.
