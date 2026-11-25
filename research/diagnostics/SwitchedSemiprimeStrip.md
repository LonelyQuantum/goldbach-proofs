# Testing the semiprime replacement against lower small prime factors

Let $X=p^2$ for a large odd prime $p$, $L=\log X$, $H=\lfloor X^{2/3}\rfloor$, $T=\lfloor X^{21/40}\rfloor$, and $J=[X-H,X-2T)\cap\mathbb Z$. Write $a=2X-n$, $K=2C_2H/L^2$, $C_2=\prod_{\ell>2}(1-(\ell-1)^{-2})$. Let $P$ denote the prime indicator and $A(n)=1_{P^-(n)>\sqrt L}/(L V(\sqrt L))$, where $V(v)=\prod_{\ell\le v}(1-1/\ell)$. The [binary replacement construction](PrimeReflectionDivisorTests.md) used additions opposite semiprimes with both factors above a prescribed progression level. We bound how often those additions could survive even the small-prime exclusions obeyed by true lower primes.

Let $\mathcal S$ consist of upper sites $a=qt$ with $q,t$ prime and
\[
 X^{4/25}<q\le X^{1/6}.
\]
Here $t>q$ automatically. Write $N_f(\mathcal S)=\sum_{n\in J,\,a\in\mathcal S} f(n)$ and $P_\kappa(n)=1_{P^-(n)>X^\kappa}$ for $\kappa=1/18$. For every sufficiently large prime square,
\[
 N_{P_\kappa}(\mathcal S)<0.5855K,\qquad
 N_P(\mathcal S)-N_A(\mathcal S)<0.5367K. \tag{1}
\]
In particular, if the previous construction is used with progression exponent $4/25$, its $(1+o(1))K$ additions lie in this strip. More than $0.4145K$ of the added **lower** sites must have a prime factor at most $X^{1/18}$. The estimate counts all eligible rough lower integers, so it applies even to additions chosen after inspecting the factorizations.

On $\mathcal S$ the [previous large-factor log weight](BalancedPrimeCofactors.md) is $\log(a)/L=1+O(H/(XL))$. Let $C_{\rm out}(f)$ be the same total upper-composite log weight against $f$ with $\mathcal S$ omitted, and let $R$ count the actual central prime pairs in $J$. Then
\[
 R+C_{\rm out}(P)-C_{\rm out}(A)>0.1395K \tag{2}
\]
eventually. A missing pair would still require this much excess outside the entire strip. This is a statement about actual primes; the monotone-edit consequence below has additional hypotheses.

## The switched upper bound

First fix $4/25<b<1/6$. Take the prime cofactor interval $((2X)^{4/25},(2X)^b]$ and set
\[
 c_b=\int_{4/25}^b\frac{du}{u(1-u)}.
\]
Apply Cai–Lu Lemma 3 at base $2X$ to the short product interval $[X+2T+1,X+H+1)$, $\theta=2/3$, auxiliary function $1_{\mathbb P}$ and the difference of the two fixed auxiliary exponents. For each $q$ the prime $t$ has expected mass $(1+o(1))H/[q\log(X/q)]$ uniformly. The total mass is $(c_b+o(1))H/L$ by prime reciprocal summation. For odd sieve moduli $d$, the condition $d\mid n$ prescribes the reduced class $qt\equiv2X\bmod d$. The lemma controls the sum over $q$ **inside** the absolute discrepancy, summed over moduli to level $D=(2X)^{1/6}/\log^{B}(2X)$. In the sieve itself all prime factors of $d$ are at most $X^{1/18}$ and thus smaller than every $q$. No noncoprime auxiliary variable is omitted on that support.

Sift $n$ through $X^{1/18}$ on that product sequence; $n$ is already odd. The local density for an odd sieve prime $\ell$ is $1/(\ell-1)$. Its survival product is $(2C_2e^{-\gamma}+o(1))/\log(X^{1/18})$. The linear-sieve parameter tends to 3, so the upper function tends to $F(3)=2e^\gamma/3$. Multiplying by the initial mass and dividing by $K$ gives $12c_b+o(1)$. For the reference $A$, use inclusion–exclusion at primes through $\sqrt L$ in the same product sequence, with all moduli dividing the primorial of size $X^{o(1)}$. The resulting product $\prod_{2<\ell\le\sqrt L}(1-1/(\ell-1))/V(\sqrt L)$ tends to $2C_2$. Thus the normalized reference mass on the interior band tends to $c_b$. [Cai–Lu, Lemmas 1–3, in particular the auxiliary exponent and the value of the upper sieve function](https://bibliotekanauki.pl/articles/1216105.pdf#page=3)

## Uniform treatment of the endpoint

The auxiliary theorem assumes a strict exponent below $1/6$. The following elementary sieve closure is also useful for composite co-factors. Uniformly for primes $q$ between $X^{4/25}/2$ and $2X^{67/400}$, count *integer* $t$ with $2X-qt\in J$, $P^-(t)>X^{11/100}$ and $P^-(2X-qt)>X^{1/18}$. The count is at most
\[
 \left(\frac{800}{11}+o(1)\right)\frac Kq. \tag{3}
\]
The interval for $t$ has length $(H-2T)/q$ up to rounding. At each odd prime through both cutoffs the two forbidden residues are $0$ and $2X/q$ modulo that prime; these are distinct as neither $p$ nor $q$ is a sieve prime. At 2 they coincide. At primes above the smaller cutoff there is only one forbidden residue. The ideal two-form density is consequently $(2C_2+o(1))V(X^{11/100})V(X^{1/18})$.

For the upper sieve first impose both conditions up to $w=\exp(\sqrt L)$ by adjacent Bonferroni cutoffs at order $\asymp L^{1/4}$. For middle divisors $e,d$ of $t,n$ respectively, a common prime is impossible. Coprime $e,d$ give one progression and the pre-sieve main term with relative error smaller than every inverse power of $L$, plus $X^{o(1)}$ rounding. Indeed the omitted product tail is bounded by $(2\sum_{\ell\le w}1/\ell)^j/j!$ times the unsieved mass and there are at most $2^{O(j)}w^{O(j)}$ residues to round. Use dimension-one upper Rosser weights on the two remaining factors at levels $X^{33/100}$ and $X^{1/6}$ respectively. Their product majorizes the two indicators; the divisor coefficients separately have absolute value at most one. Summed rounding per $q$ is $X^{33/100+1/6+o(1)}=o(K/q)$ because $67/400+33/100+1/6<2/3$. In the main term restoring the omitted common middle primes costs $O((H/q)L^2\sum_{\ell>w}\ell^{-2})=o(K/q)$. The resulting one-dimensional products can be estimated separately at parameter 3; replacing independent two-prime survival factors above $w$ by the two-root factors changes the product by $1+O(1/w)$. Multiplying the two $F(3)$ bounds and the two Mertens factors gives $[2/(33/100)] [2/(1/6)]=800/11$ in units of $K/q$. The asymmetric cutoffs and the strict rounding margin are needed for (3). [Two-form CRT argument](MarkedPrimePartners.md#both-endpoints-rough-with-an-optional-marked-upper-prime) · [Iwaniec, linear sieve](https://doi.org/10.4064/aa-37-1-307-320)

This uniform bound costs $O(\log((1/6)/b))K+o(K)$ for the omitted primes $q$ above the fixed interior band, by Mertens' theorem. Shifting either fixed lower endpoint from $(2X)^u$ to $X^u$ costs $o(K)$ by the same bound. Take the limsup in $p$ before letting $b\uparrow1/6$. For the nonnegative reference only the interior lower estimate is needed. Since $c_b\to c=\log(21/20)$ this proves $\limsup N_{P_\kappa}/K\le12c$ and $\limsup(N_P-N_A)/K\le11c$. Equation (2) follows from the previously certified bound $R+C(P)-C(A)>0.6762K$ with a strict limiting margin and $11c<0.5367$. Multiplying the strip count by $\log(a)/L$ changes the difference by $o(K)$ even with the trivial bound of $H$ sites.

## Where a rough monotone replacement would have to go

Suppose that at the same square one deletes $(1+o(1))K$ lower sites opposite upper primes, adds the same number only opposite upper composites, and changes the summed maximum over reduced lower classes by $o(K)$ to level $D_0=X^{83/500}$. Assume additionally that all added lower sites have least prime factor greater than $X^{1/18}$. Then **more than $0.3457K$ additions** have upper partners with at most five prime factors, counted with multiplicity, all greater than $X^{67/400}$.

In fact the added lower sites are odd. For each odd prime $\ell\le D_0$ the class $n\equiv2X\bmod\ell$ contains no deletion, since $a$ is then a multiple of $\ell$ larger than $\ell$. The union bound from the [previous construction](PrimeReflectionDivisorTests.md#why-monotone-additions-must-avoid-small-upper-factors) disposes of $o(K)$ additions with $P^-(a)\le D_0$. If $D_0<q=P^-(a)\le X^{67/400}$, then $a=qt$ with $t>1$ and $P^-(t)\ge q>X^{11/100}$, also when $q^2\mid a$. Apply (3) and sum $1/q$ over the strip. The resulting upper coefficient is $(800/11)\log(335/332)<0.6543$. The remaining additions have $P^-(a)>X^{67/400}$. Six such factors would give $a>X^{402/400}>X+H$ eventually. This proves the assertion. Monotonicity is used to turn a discrepancy bound into an upper bound on actual additions; it need not hold for $P-A$. Neither (1) nor (2) decides the sign of the discrepancy outside the semiprime strip.

The [exact checker](CheckSwitchedSemiprimeStrip.py) encloses the logarithmic constants and checks the distinct and coincident sieve roots, finite semiprime switching, and the smallest-factor partition with repeated factors.
