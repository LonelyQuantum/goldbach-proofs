# The loss from counting rough offsets near a prime square

Let $p$ tend to infinity through odd primes, $m=p^2$, and $H=\lfloor p^{4/3}\rfloor$. Work in the closed integer window $W=[m-H,m+H]$. Write $P$ for the number of primes in $W$, and $r$ for the number of $1\le h\le H$ with both $m-h,m+h$ prime. Each representation counted by $r$ is unordered. Write $C_2=\prod_{\ell>2,\ \ell\ {\rm prime}}(1-1/(\ell-1)^2)$, and use natural logarithms.

An integer is $z$-rough if all its prime factors exceed $z$. Let $K_z$ count positive offsets with at least one rough endpoint, $T_z$ those with two rough endpoints, and $E_z$ the rough composite integers in $W\setminus\{m\}$. All cutoffs below are smaller than $m-H$ for large $p$.

## Result

For each fixed $0<c<1$, with $L=H/\log^2p$, the following estimates hold along **all** sufficiently large prime centers of the form $m=p^2$:
$$
 E_{cp}=(2\log(1/c)+o_c(1))L,\qquad
 K_{cp}=P-r+(2\log(1/c)+o_c(1))L.
$$
In particular, for each fixed $c<\exp(-9C_2/2)$, one eventually has $K_z>P$ for every $z\le cp$. This includes $z=p/20$ and every $z=p^{1-\varepsilon}$ for fixed $0<\varepsilon<1$. The endpoint of this sufficient range is about $0.05127$. Its optimal value is open. The asymptotic estimates above use $c$ fixed before $p$ tends to infinity.

### Counting convention

Off the midpoint, the rough endpoints number both $P+E_z$ and $K_z+T_z$. Thus
$$
 P-K_z=T_z-E_z,\qquad r-(P-K_z)=E_z-(T_z-r).
$$
The midpoint $p^2$ would itself be a rough composite at $z=cp$; it is excluded from all three counts. The exact condition $T_z>E_z$ certifies a representation by pigeonholing the prime endpoints. A genuine pair can exist when this condition fails.

### The rough composites

For fixed $c$, three factors exceeding $cp$ already have product greater than $p^2+H$ for large $p$. Each rough composite therefore has a unique factorization $qs$ with primes $cp<q\le s$. Up to $O_c((1+H/p)^2)$ terms we may sum over $cp<q\le p$, counting every prime $s$ with
$$
 (p^2-H)/q < s \le (p^2+H)/q .
$$
Indeed, $q>\sqrt{p^2+H}$ cannot be the smaller factor. All discrepancies from the order $q\le s$ and the boundary $q=p$ involve $q=p+O(H/p+1)$, with $O_c(H/p+1)$ possible partners each. If $s\le cp$ with $q>cp$, it belongs to that same ordering discrepancy. An integer at the open lower endpoint and removal of the midpoint affect the count by $O(1)$ after enforcing order, or $O(p)$ even if counted once per $q$; both are $o(L)$.

For clarity, the required almost-all prime estimate is applied to the **cofactor start**, at each fixed $p$. Put $x_q=\lfloor(p^2-H)/q\rfloor$. The real starting points for successive integers $q\le p$ differ by at least $(p^2-H)/(p(p+1))>1/2$ for large $p$, so an integer start has bounded multiplicity. All starts lie in a fixed number (depending on $c$) of dyadic intervals at scale $p$.

Fix a finite partition of $[c,1]$ into intervals $[a,b]$ with $b/a\le1+\eta$; assign shared endpoints to just one bin. For $ap<q\le bp$, sandwich the cofactor interval from $x_q$ between integer lengths $2H/(bp)-O(1)$ and $2H/(ap)+O(1)$, rounded outwards. Both lengths are $\asymp_c p^{1/3}$. Corollary 1.4 of Guth and Maynard applies for each fixed length on each dyadic interval $[X,2X]$ since $X\asymp_c p$ and $2/15<1/3<0.99$. It gives $y/\log x_q+o(y/\log p)$ primes for all but $O_c(p\exp(-k_c(\log p)^{1/4}))$ integer starts. Bounded multiplicity and the trivial $O_c(H/p)$ count per exceptional start make their entire contribution $o_{c,\eta}(L)$, even if all bad starts occur at prime $q$. No exception in the choice of $p$ remains. On the good starts $\log x_q=\log p+O_c(1)$; squeezing the two lengths costs a relative $O(\eta)$. Ordinary PNT and partial summation give $\sum_{cp<q\le p}1/q=(\log(1/c)+o_c(1))/\log p$. First let $p$ grow for the finite partition and then send $\eta$ to zero. Summing $2H/(q\log p)$ gives the stated $E_{cp}$. [Guth and Maynard, Corollary 1.4 and §13.2](https://arxiv.org/html/2405.20552v2)

### Two rough endpoints of which at least one is composite

Choose the composite endpoint $qs$ by its smaller prime factor $q\in(cp,\sqrt{p^2+H}]$. For each $q$, sieve the integer interval for $s$, of length $U=2H/q\asymp_c p^{1/3}$, by the two forms $s$ and $2p^2-qs$. If this endpoint and its reflection both survive at $cp$, neither form has a prime factor at most $v=U^{1/4}$. For large $p$, $v<\min(q,p,cp)$. There is one forbidden residue modulo 2 and exactly two modulo every odd prime up to $v$: they are $0$ and $2p^2/q\bmod\ell$. For a squarefree $d$ made of these primes, the interval remainder is $O(2^{\omega(d)})$ by the Chinese remainder theorem. Here $\omega(d)$ counts distinct prime divisors.

The dimension-two Selberg upper sieve gives $O(U/\log^2 U)$ surviving integers uniformly in the translate and in $q$. In (3.8) of Heath-Brown's notes the summed remainder is $O(v^2\log^5 v)=o(U/\log^2 U)$, using $\mu^2(d)6^{\omega(d)}\le\tau_6(d)$. There are $O(p/\log p)$ possible prime $q$. Every offset in $T_{cp}-r$ has at least one such endpoint, and counting both endpoints only enlarges the upper bound. Thus
$$
 0\le T_{cp}-r\ll_c H/\log^3 p.
$$
Together with the exact identities this proves the second asymptotic. [Heath-Brown, §3, equation (3.8) and its Goldbach example](https://arxiv.org/pdf/math/0209360#page=22)

### An unconditional range in which the certificate fails

Apply the same upper sieve directly to $(p^2-h)(p^2+h)$, now for $1\le h\le H$, with $v=\sqrt H/\log^5H$. For large $p$, $v<cp<p$. The roots are $\pm p^2\bmod\ell$, again one at 2 and two at odd sieve primes. The full sum of remainders is $O(v^2\log^5v)=o(L)$. The local density product is $(2C_2e^{-2\gamma}+o(1))/\log^2v$ by Mertens' product formula. In (3.8) the dimension-two multiplier is $e^{2\gamma}\Gamma(3)=2e^{2\gamma}$. Since $\log v\sim\tfrac12\log H\sim\tfrac23\log p$, this gives
$$
 T_{cp}\le(9C_2+o(1))L .
$$
If $2\log(1/c)>9C_2$, the main term of $E_{cp}$ exceeds this upper bound. Therefore $P<K_{cp}$, and decreasing $z$ only increases $K_z$. For the concrete fraction $1/20$, the product through prime 47 bounds $C_2$ above by $3041106216468949733/4588393964104581120<0.663$. The positive series $\log x=2\sum_{k\ge0}t^{2k+1}/(2k+1)$, $t=(x-1)/(x+1)$, applied to $\log20=4\log2+\log(5/4)$ through $k=2$ already gives $2\log20>5.98>9(0.663)$. [Selberg upper bound with its dimension factor](https://arxiv.org/pdf/math/0209360#page=22)

### A shrinking distance below $p$

For $z=p-\lfloor\sqrt p\rfloor$, counting possible factors directly gives $E_z=O(p^{5/6})$. Indeed the smaller factor has at most $\lfloor\sqrt p\rfloor+H/(2p)+2$ choices and then at most $2H/z+1$ choices for the other. Consequently a uniform lower bound on $T_z$ larger than this explicit product would suffice. The fixed-$c$ asymptotic above supplies no uniform estimate as $c\to1$. Establishing the lower bound on $T_z$ for every large prime $p$ remains open.

### Finite checks

The table uses $z=\lfloor 4p/5\rfloor$. The displayed counts include both sides of the window for $P,E_z$, and positive offsets only for $r,T_z,K_z$.

| $p$ | $H$ | $z$ | $P$ | $r$ | $E_z$ | $T_z$ | $K_z$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 101 | 470 | 80 | 103 | 8 | 8 | 9 | 102 |
| 1009 | 10120 | 807 | 1479 | 64 | 98 | 74 | 1503 |
| 10007 | 215644 | 8005 | 23459 | 825 | 1126 | 919 | 23666 |

To reproduce, find $H$ by integer cube root of $p^4$. Mark multiples of primes through $z$ on $W$ for the rough indicator, and separately through $\lfloor\sqrt{m+H}\rfloor$ for the prime indicator. Count their sums, pairwise products, and pairwise unions at offsets $1,\ldots,H$. All window elements exceed the sieving primes in these examples. The middle row was also checked using a separate prime-range enumeration and gcd with the product of sieve primes. The analytical estimates in this note are a paper derivation using the cited theorems.
