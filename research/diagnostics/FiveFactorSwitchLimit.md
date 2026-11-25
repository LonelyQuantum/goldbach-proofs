# Why separate large-divisor upper bounds miss the five-factor target

Use the notation of [the six-factor deduction](CentralPrimeSixFactors.md). Fix $X=p^2$, $H=\lfloor X^{2/3}\rfloor$, the modulus $d$, $D=X^{1/6}/(d\log^B X)$, $z=D^{1/4}$ and $K=e^\gamma/2$. For a prime $q$ set $t=\log q/\log D$. The following obstruction concerns two particular estimates for the penalty term $S_q$, the sifted count with $q\mid X-h$. It makes no assertion about the true size of $S_q$.

* In the prime progression calculation use the existing linear upper sieve for $1/4\le t<1$, with normalized leading coefficient $1/(1-t)$.
* In the switched integer calculation use a single Selberg square for each $q$, excluding small factors of $m=(X-h)/q$ below $z$ and of $2X-qm$ up to a selectable cutoff. Charge the standard absolute rounding error separately on each dyadic $q$ interval, with sieve radius $R$ subject to $\log R\le\tfrac12\log(H/q)+o(\log X)$ uniformly. Normalize the leading upper bound by $YV(z)K/q$, as in the six-factor calculation.

Even choosing the better of the two bounds for each $q$, the resulting penalty estimate cannot give a positive five-factor margin for any fixed Richert parameter $u>0$ with the usual sign budget $\lambda+6u\le6$, $\lambda>0$. The statement prescribes the lower-sieve parameter $v=4$, the two leading terms, and the radius budget. It leaves open averaged rounding remainders, different weights, and different estimates for the actual arithmetic counts.

## An upper bound on the Selberg denominator

It suffices to work on $1/4\le t\le T=179/100$. Grant the integer sieve the largest radius allowed at the level of powers of $X$, with $\log R=\tfrac12\log(H/q)+o(\log X)$. Monotonicity of the positive denominator handles smaller choices. Here $\log R/\log z$ lies in a compact subinterval of $(1,\infty)$. For an optimistic upper bound on the denominator, fill in a forbidden class from the second form at every prime $\ell<R$ outside $d$. If $q$ itself is included, use the same idealized density as at an ordinary prime. This can only increase the denominator. Primes $\ell\ge R$ cannot occur in any divisor $k<R$. The model now has two forbidden classes for odd $\ell<z$ outside $d$, and one everywhere else below $R$ outside $d$; call its denominator $G_2(R)$. Indeed $q\ge z$, $p>R$ throughout the interval for large $X$, and a possible coincidence of forbidden classes can only reduce the actual denominator.

For comparison put $G_1(s)=\sum_{n<s,\,(n,d)=1}\mu^2(n)/\varphi(n)$. It equals $(\varphi(d)/d)\log s+O_d(1)$. One proof factors its Dirichlet series as $\zeta(1+s)H_d(s)$ (here $s$ denotes the complex argument). Each good Euler factor of $H_d$ is $1+(\ell^{-s}-\ell^{-2s})/(\ell(\ell-1))$ and each omitted factor is $1-\ell^{-1-s}$. The coefficients of $H_d$ are absolutely summable with a logarithmic weight and $H_d(0)=\varphi(d)/d$. Convolution with $1/n$ gives the formula.

Generate a random divisor $B_1$ by selecting each prime $\ell<R$ outside $d$ independently with probability $1/\ell$. From the omitted odd primes $\ell<z$ outside $d$, independently add each with probability $1/(\ell-1)$ and call the resulting product $B_2$. The inclusion probability in $B_2$ is exactly $2/\ell$ at the doubled primes. Write $V_1=\prod_{\ell<R,\;\ell\nmid d}(1-1/\ell)$ and $V(z)=\prod_{2<\ell<z,\;\ell\nmid d}(1-1/(\ell-1))$. From the two product laws,
$$\Pr(B_1<s)=V_1G_1(s)\quad (1<s\le R),\qquad
\Pr(B_2<R)=V_1V(z)G_2(R).$$

Given $R/\sqrt z\le B_1<R$, any added prime in $[\sqrt z,z)$ pushes the product to at least $R$. Only $O(1)$ primes of that interval are already in $B_1$ because their product is less than $R$. Uniformly in such a $B_1$, the conditional probability of adding none of the remaining primes of this interval is $1/2+o(1)$, by Mertens' product formula. Omitting a bounded number changes the product by $1+O(1/\sqrt z)$. Thus
$$
V(z)G_2(R)\le G_1(R)-(1/2+o(1))\bigl(G_1(R)-G_1(R/\sqrt z)\bigr)
=\frac{\varphi(d)}d\left(\log R-\tfrac14\log z+o(\log X)\right).
$$
This accounts for some of the divisor mass lost even in an optimally evaluated single Selberg square. Since its optimal main term is $H/(dqG(R))$, its normalized coefficient is at least
$$ \frac{24e^{-\gamma}}{31/8-t}+o(1). $$
The constant $31/8$ uses $\log R-\frac14\log z\le(31/8-t)(\log D)/2+o(\log X)$. All asymptotics above are uniform on the fixed integration interval.

## A certificate for every sign-budget parameter

Set $A=31/8$, $C=67/5<24e^{-\gamma}$ and $b=(C-A)/(C-1)$. The better of the two allowed upper-bound coefficients is still at least $k(t)+o(1)$, where $k(t)=1/(1-t)$ on $[1/4,b]$ and $k(t)=C/(A-t)$ on $[b,T]$. At the join the two expressions agree. Against the nonnegative weight $(1-ut)_+$ the optimistic penalty coefficient is therefore at least
$$
\int_{1/4}^T (1-ut)_+ k(t)\frac{dt}{t}
\ \ge\ J_0-uJ_1,\qquad J_0=\int_{1/4}^T k(t)\frac{dt}{t},\quad J_1=\int_{1/4}^T k(t)\,dt .
$$
Writing $L=\log((3/4)/(1-b))$ gives
$$
J_0=\log(4b)+L+\frac CA\log\frac{T(A-b)}{b(A-T)},\qquad
J_1=L+C\log\frac{A-b}{A-T}.
$$
Exact rational enclosures give $J_0>6.60>6\log3>6.59>J_1$. Thus $J_0-uJ_1>(6-6u)\log3\ge\lambda\log3$, already exceeding the whole available lower-sieve term. For the previously proposed $u=1/2$ the same coefficient on $[7/9,2]$ gives a floor of $1.63889\ldots$ on that explicit upper estimate alone; the sufficient target there was $1.50007\ldots$. The denominator argument covers this slightly longer interval as well.

The [rational checker](CheckSixFactorSwitch.py) verifies the comparisons, including $C<24e^{-\gamma}$ via $\gamma<H_{128}-\log128$. The unresolved quantity is the *actual weighted sum* of $S_q$; a proof using correlations or a saving over these separate upper estimates would evade this calculation.
