# A sharp uniform asymptotic floor for the Goldbach desk's major arcs

For the full prime-logarithmic sum and exactly the arcs proposed in [PR #649](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/649), the modeled contribution exceeds $n$ for every even $n\ge6$. Its normalized lower limit along the even integers is $2C_2$, where $C_2=\prod_{r>2,\ r\ {\rm prime}}(1-1/(r-1)^2)$. The same lower limit holds for the actual signed major integral by the sublinear comparison in the accepted source of [PR #316](https://github.com/CGandGameEngineLearner/goldbach-proofs/pull/316). The sharpened constants and limit below are paper deductions.

## Finite bound

Set $Q=\lfloor\log_2(n+2)\rfloor^2$, $e(t)=\exp(2\pi i t)$, $K_n(t)=\sum_{k=0}^n e(kt)$, and
$$
 I_q=\int_{-Q/(qn)}^{Q/(qn)} |K_n(t)|^2\,dt,\qquad
 a_q=\frac{\mu(q)^2c_q(n)}{\varphi(q)^2}.
$$
Here $c_q(n)$ is the Ramanujan sum. It is real, $c_q(1)=\mu(q)$, and the model in the proposal is $M(n)=\sum_{q\le Q}a_q I_q$. The masses $I_q$ are nonnegative and decreasing in $q$. The base source already proves $M(n)\ge n/72$ for every positive even $n$. Its multiplicativity, prime coefficients and higher-power identities give precisely the coefficients above. [Local coefficient lemmas](https://github.com/DFQDZZ/goldbach-proofs/blob/e4ab24712555ae8c2c926adf19d368a9fb392c35/lean/PEqualNP/Outside/L_goldbach_arc_major_floor.lean#L4902-L4926) · [Existing modeled floor](https://github.com/DFQDZZ/goldbach-proofs/blob/e4ab24712555ae8c2c926adf19d368a9fb392c35/lean/PEqualNP/Outside/L_goldbach_arc_major_floor.lean#L5514-L5533)

Let $P$ be the total of positive terms and $D$ the absolute total of negative terms. For each $a_q<0$, choose the least prime $r\mid q$ that does not divide $n$. Such a prime exists, is odd since $n$ is even, and occurs once since $q$ is squarefree. With $s=q/r$, multiplicativity and $c_r(n)=-1$ give $a_s>0$ and $|a_q|=a_s/(r-1)^2$. Since $I_q\le I_s$ and $(s,r)$ determines $q$ uniquely,
$$
 D\le P\sum_{r>2,\ r\ {\rm prime}}\frac1{(r-1)^2}
 \le \frac P4\left(1+\frac14+\int_2^\infty t^{-2}\,dt\right)
 =\frac7{16}P.
$$
The integral bounds the terms $k\ge3$ after writing $r-1=2k$. In particular $M(n)\ge9P/16$ and $P\ge I_1+I_2$, because $a_1=a_2=1$. The same argument works within any group of squarefree denominators having the same $\gcd(q,n)$, since removing $r$ preserves that gcd.

Parseval on $[-1/2,1/2]$ gives kernel mass $n+1$. At $0<|t|\le1/2$ the geometric series gives $|K_n(t)|\le1/|\sin(\pi t)|\le1/(2|t|)$. For $b=Q/(qn)<1/2$ the two discarded tails contribute at most
$$
 2\int_b^{1/2}\frac{dt}{4t^2}=\frac{1}{2b}-1.
$$
For $b\ge1/2$ the full period is already inside the arc. Thus $I_q\ge n+1-qn/(2Q)$ in both cases. As $Q\ge9$ for $n\ge6$,
$$
 M(n)\ge\frac9{16}\left(2(n+1)-\frac{3n}{2Q}\right)
       \ge\frac{33}{32}n+\frac98>n .
$$
These $I_q$ are precisely the symmetric model integrals, so this finite calculation needs no disjointness of rational arcs.

## The limiting constant and a sequence attaining it

For large $n$ all symmetric intervals have width radius below $1/2$. Extend $I_q$ by zero for $q>Q$ and set $F_q=I_q/(n+1)$. For $q\le Q$ the tail estimate gives $0\le1-F_q\le q/(2Q)$. For all $q\ge1$, including the omitted ones, $|1-F_q|\le\sqrt{q/Q}$.

Group contributing denominators by $g=\gcd(q,n)$, so $q=gd$ with $g$ a squarefree divisor of $n$, $d$ squarefree and coprime to $n$. Their coefficients are $\mu(d)/(\varphi(g)\varphi(d)^2)$. Each group has nonnegative total by the preceding charging inequality. Keep just $g=1$ and $g=2$, both with $\varphi(g)=1$. For each of these,
$$
 \sum_{\substack{d\ {\rm squarefree}\\(d,n)=1}}
     \frac{\mu(d)}{\varphi(d)^2} F_{gd}
 =\prod_{\substack{r\ {\rm prime}\\r\nmid n}}\left(1-\frac1{(r-1)^2}\right)
   + O(Q^{-1/2}).
$$
The error is uniform because the absolute error is bounded by $\sqrt{g/Q}\prod_{r>2}(1+\sqrt r/(r-1)^2)$, a convergent product over primes. The product on the right in the displayed equation is at least $C_2$. This yields $M(n)/(n+1)\ge2C_2-O(Q^{-1/2})$ for every sufficiently large even $n$. For $n=2^k$ only the two retained groups occur and the product equals $C_2$, so $M(2^k)/(2^k+1)=2C_2+O(Q^{-1/2})$. The two bounds prove the claimed lower limit.

## Consequence for the binary target

Let $J(n)$ denote the actual major integral for the prime-log sum on the project's arcs in $[0,1]$. The source accepted for #316 proves $|J(n)-M(n)|\le E(n)$ once $2Q^2<n$, and $E(n)/n\to0$. This condition holds eventually. Hence $\liminf_{2\mid n,\ n\to\infty}\operatorname{Re}J(n)/n=2C_2$. For some fixed $\eta>0$, an eventual lower bound $-(2C_2-\eta)n$ for the signed minor integral at every even $n$ would imply a positive prime-pair correlation at every sufficiently large even $n$. Establishing such a pointwise minor estimate remains open. [Sublinear error](https://github.com/DFQDZZ/goldbach-proofs/blob/e4ab24712555ae8c2c926adf19d368a9fb392c35/lean/PEqualNP/Outside/L_goldbach_arc_major_floor.lean#L4627) · [Comparison with the actual integral](https://github.com/DFQDZZ/goldbach-proofs/blob/e4ab24712555ae8c2c926adf19d368a9fb392c35/lean/PEqualNP/Outside/L_goldbach_arc_major_floor.lean#L5474-L5488)

**Independent finite check.** For each even $2\le n\le1024$ and prefix $1\le L\le96$, compute $c_q(n)=\sum_{d\mid(q,n)}d\,\mu(q/d)$ and form the $q\le L$ positive and negative sums with unit mass, using rational arithmetic. All 49,152 prefix inequalities $16D\le7P$ and all 21,132 individual negative-parent coefficient identities held. This checks the arithmetic signs independently of integration. The bounds for all $n$ follow from the argument above.
