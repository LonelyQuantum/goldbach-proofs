# The capacity gap on split prime shells for three integer buckets

The [phase II protocol](https://github.com/CGandGameEngineLearner/goldbach-proofs/blob/0128594b96adbbe6743836588f918d2cbacc76e5/research/hash-phase-2.md) compares real and integer maxima of the ordered triple count $\sum k(k-1)(k-2)$, fixing the sample count, ordered pair count and bucket capacity. Here is an explicit infinite family with an active capacity constraint. It specializes classical Eisenstein-integer facts and a published angular theorem. Prior literature on the resulting discrete moment optimization has not been exhaustively compared.

Let $S\equiv1\bmod3$ be a rational prime. Take
$$m=\left\lceil2\sqrt{S/3}\right\rceil,\quad c=\lfloor\sqrt S\rfloor,\quad B=m+c.$$
The three bucket sizes sum to $3m$. Write them as $m+x,m+y,m+z$ with $x\le y\le z$ and $x+y+z=0$. Fix the pair count to $3m(m-1)+2S$, equivalently $x^2+xy+y^2=S$. Denote the real and integer maximal ordered triple counts by $R$ and $I$ under $0\le m+x$ and $m+z\le B$.

There is exactly one pair $1\le r<s$ with $r^2+rs+s^2=S$. Then
$$R-I=3\{rs(r+s)-c(S-c^2)\}.$$
In particular the normalized gaps have liminf zero and limsup $2/\sqrt3$ through split rational primes. More precisely their limiting distribution at $0\le t\le2/\sqrt3$ is
$$
\lim_{N\to\infty}
\frac{\#\{S\le N:S\text{ prime},\ S\equiv1\bmod3,\ (R-I)/S^{3/2}\le t\}}
{\#\{S\le N:S\text{ prime},\ S\equiv1\bmod3\}}
=\frac2\pi\arcsin(\sqrt3\,t/2).
$$
Thus this scale admits no uniform $o(S^{3/2})$ gap. A positive proportion of the shells have a loss of order $S^{3/2}$, although the same natural parameter scale admits arbitrarily small normalized gaps.

**Exact optimization.** Each split prime has twelve representations by the Eisenstein norm, from the six associates of each of two conjugate factors in the Euclidean ring $\mathbb Z[e^{i\pi/3}]$. Units and conjugation put exactly one in the open sector $(0,\pi/6)$; its form is $s+r e^{i\pi/3}$ with $0<r<s$. Boundary elements have square norm or three times a square. The twelve solutions as deviation triples are the six permutations of $(-(r+s),r,s)$ and their negatives; the two orbits are distinct and exhaustive. All are primitive because any common divisor squared would divide $S$. We have $s<\sqrt S<r+s$, so precisely the first sorted triple satisfies $z\le c$. All real and integer deviations have absolute value at most $2\sqrt{S/3}$, so nonnegativity holds for this $m$.

On the real shell, the largest coordinate ranges over $[\sqrt{S/3},2\sqrt{S/3}]$. Indeed the two other coordinates are $(-z\pm\sqrt{4S-3z^2})/2$, and the larger of these is at most $z$ precisely when $z\ge\sqrt{S/3}$. As $s\le c<r+s$, the point $z=c$ is feasible. Expanding the ordered triple count gives a constant depending only on $m,S$, plus $3xyz=3(z^3-Sz)$. This polynomial increases over the specified interval. The real maximum occurs at $z=c$ and the integer maximum at $z=s$, yielding the formula. The upper cap always removes the other integer orbit.

**Angular distribution.** Let $\phi=\arg(s+r e^{i\pi/3})$. Taking the imaginary part of the cube gives $\sin(3\phi)=3\sqrt3\,rs(r+s)/(2S^{3/2})$. Therefore the normalized gap differs from $(2/\sqrt3)\sin(3\phi)$ by at most $6/\sqrt S$, since $0\le c(S-c^2)<2S$. The prime ideals in the Eisenstein ring are equidistributed in argument modulo the units by Marmon's Theorem 35. The inert prime ideals with norm at most $N$ contribute $O(\sqrt N)$, and the one ramified prime is immaterial. Folding conjugate angles onto $[0,\pi/6]$ gives each split rational prime equal weight and a uniform limiting angle. The displayed distribution follows by taking the length of the corresponding interval; continuity includes both endpoints. [Marmon, *Hexagonal Lattice Points on Circles*, §5, Theorem 35](https://people.kth.se/~kurlberg/eprints/marmon.pdf#page=45)

**Finite check.** At $S=7,19,37,61$ the exact gaps are $0,54,234,288$. An independent enumeration up to $S=20\,000$ checked all 1,124 split primes: run $1\le z\le\lfloor\sqrt{4S/3}\rfloor$ and keep $4S-3z^2=k^2$ with $k+z$ even and $k\le3z$. Maximize the integer objective over the retained triples with $z\le c$. The comparison uses integer arithmetic only. The distribution statement uses the angular theorem, not a numerical fit.
