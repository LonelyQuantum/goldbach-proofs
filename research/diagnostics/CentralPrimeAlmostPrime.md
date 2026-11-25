# A prime and a squarefree almost-prime in a prime-square central window

Let $p$ tend to infinity through primes, $X=p^2$, $H=\lfloor X^\theta\rfloor$. Write $\Omega(a)$ for the number of prime factors of $a$, counted with multiplicity. Fix an integer $d\ge1$ and call $0\le b<d$ admissible when both $b$ and $2X-b$ are coprime to $d$. Define $G_r(X,H;d,b)$ to count $1\le h\le H$ such that $X+h$ is prime and congruent to $b\bmod d$, while $X-h$ is squarefree and has $\Omega(X-h)\le r$. The orientation counts each offset once.

For every sufficiently large prime $p$, simultaneously in every admissible class for the fixed $d$, the following paper deductions hold unconditionally:
$$
 G_7(X,\lfloor X^{2/3}\rfloor;d,b)\gg_d H/(\log X)^2,\qquad
 G_6(X,\lfloor X^{27/40}\rfloor;d,b)\gg_d H/(\log X)^2,
$$
where $H$ on the right is the corresponding window width. The proof also keeps every prime factor of the smaller summand at least $X^{(\theta-1/2)/4-o(1)}$. One can, for example, fix $d=27{,}720$ and retain the full joint residue class. These bounds specialize classical distribution and sieve results. No priority or optimality assertion is made. The published Cai–Lu theorem gives a prime and a $P_2$ in the wider window $N^{0.972}$ about $N/2$ for every sufficiently large even $N$. Here we use their three preliminary lemmas. [Cai and Lu, *Chen's theorem in short intervals*, pp. 311–313](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf)

## Starting with one genuine prime

For a finite comparison take $p=1009$, $H=10120$. Direct enumeration gives $G_7=564$ and $G_1=64$ without a residue restriction. In the admissible class $b=25\bmod99$, the nine offsets counted by $G_7$ are $1248,2436,2832,5208,6396,7980,8376,8772,8970$; all nine smaller partners are composite. These counts can be reproduced by factoring $1009^2-h$ for each $1\le h\le10120$ with $1009^2+h$ prime, keeping exponents all equal to one and applying the stated class and factor-count conditions. The example illustrates the distinction between $G_7$ and $G_1$ at one center.

Put $\delta=\theta-1/2$. Let $\mathcal A=\{2X-t:X<t\le X+H,\ t\text{ prime},\ t\equiv b\bmod d\}$ and $Y=\int_X^{X+H}dt/(\varphi(d)\log t)$. Fix an error-saving exponent $A>4$. Cai–Lu Lemma 3 with $\beta=0$ and the auxiliary weight supported at $1$ supplies level $D_{\rm AP}=X^\delta/(\log X)^{B(A)}$. Both exponents $\theta$ used here exceed $3/5$. Put $D=D_{\rm AP}/d$. For squarefree $k<D$ coprime to $2d$,
$$
 |\mathcal A_k|=Y/\varphi(k)+r_k,\qquad
 \sum_{\substack{k<D\\k\ {\rm squarefree}\\(k,2d)=1}}|r_k|\ll_{A,d}H/(\log X)^A,
 \quad \mathcal A_k=\{a\in\mathcal A:k\mid a\}.
$$
Indeed $k\mid 2X-t$ fixes $t\equiv2X\bmod k$, and $k<D<p$. This is a reduced class and combines with $b\bmod d$ into one reduced class modulo $dk$. These moduli are distinct and lie in the published range. Either convention for the interval endpoints costs at most two counts per modulus, negligible here. Primes dividing $2d$ already divide no member of $\mathcal A$. The only use of the prime-square shape in this distribution step is the reducedness of the residue $2X$ at every sieving modulus. [Cai–Lu, Lemma 3](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=3)

## A weighted lower bound

Fix $2<v\le4$, $1<u<v$, $z=D^{1/v}$ and $y=D^{1/u}$. All these exponents are fixed before $p$ grows. Sift $\mathcal A$ by primes less than $z$, omitting those dividing $2d$. On each survivor use the weight
$$
 W(a)=1-\lambda^{-1}\sum_{\substack{z\le q<y\\q\ {\rm prime},\ q\mid a}}
                (1-\log q/\log y),\qquad \lambda>0.
$$
If $a$ is squarefree, the penalty sum is at least $\Omega(a)-\log a/\log y$: deleting negative terms from the sum over all prime factors only increases it. Put $T=1/\delta$. For $\lambda<r+1-uT$ and all sufficiently large $p$, every squarefree survivor with $\Omega(a)\ge r+1$ has $W(a)\le0$, because $\log a/\log y\le uT+o(1)$. The number of nonsquarefree survivors is at most $\sum_{z\le q\le\sqrt X}(H/q^2+1)\ll H/z+\sqrt X=o(H/\log^2 X)$. Each weight is at most 1, so the total weight, less this square correction, is a lower bound for $G_r$. The finite factor-budget and weighted counting inequalities are [verified in Lean](RichertFactorBudget.lean).

Write $V(w)=\prod_{\ell<w,\,\ell\nmid 2d}(1-1/(\ell-1))$ over primes $\ell$; $V(w)\sim C_d/\log w$ with $C_d>0$ by Mertens' theorem. The linear lower sieve gives at least $YV(z)(f(v)+o(1))$ survivors after including the absolute remainder bound. Here $f(v)=(2e^\gamma/v)\log(v-1)$. For $z\le q<y$ bound survivors divisible by $q$ from above by sifting $\mathcal A_q$ only to $w_q=\min(z,\sqrt{D/q})$, at level $D/q$. Then $2\le s_q=\log(D/q)/\log w_q\le\max(2,v-1)\le3$, so $F(s_q)=2e^\gamma/s_q$. In particular this argument remains valid when $D/q<z$. Every $w_q$ grows as a fixed positive power of $D$ or faster and $q\ge w_q$; the dimension-one density and sieve constants are uniform in $q$ for fixed $d,u,v$. In the upper sieve the remainder at each auxiliary modulus $k$ is $r_{qk}$, with $qk<D$ and every prime divisor of $k$ less than $w_q\le z$. Thus $q$ is the unique prime factor at least $z$ in $qk$; summing the absolute remainders costs at most the displayed distribution bound once. The upper main term for this $q$, divided by $YV(z)$, is
$$
 \frac{1}{q-1}\left(\frac{2 e^\gamma}{v(1-\log q/\log D)}+o(1)\right).
$$
The $o(1)$ is uniform; $\sum_{z\le q<y}1/(q-1)=O_{u,v}(1)$. Partial summation over primes, with $t=\log q/\log D$, now gives
$$
 G_r\ \ge\ YV(z)\frac{2e^\gamma}{v}
 \left[\log(v-1)-\frac{J_v(u)}{\lambda}+o(1)\right],
$$
whenever the factor budget above holds. Here
$$
 J_v(u)=\int_{1/v}^{1/u}\frac{1-ut}{t(1-t)}\,dt
       =\log(v/u)+(u-1)\log\frac{1-1/u}{1-1/v}.
$$
All errors, including removal of the squares, are $o(YV(z))$ for fixed $d$. Thus a strictly positive bracket proves the claimed order of magnitude. [Cai–Lu, Lemmas 1–2](https://matwbn.icm.edu.pl/ksiazki/aa/aa91/aa9142.pdf#page=2)

## Exact threshold for this choice of sieve functions

A strictly positive lower bound is available from these estimates when a fixed $\lambda$ lies strictly between $J_v(u)/\log(v-1)$ and $r+1-uT$. To test this interval, minimize $uT+J_v(u)/\log(v-1)$ over $1<u<v$. The derivative of $J_v$ is $\log((1-1/u)/(1-1/v))$ and its second derivative is $1/(u(u-1))>0$. The minimum is attained at $u_*=[1-(1-1/v)(v-1)^{-T}]^{-1}$ and equals
$$
 M_v(T)=\log_{v-1}\!\left(v(v-1)^T-(v-1)\right).
$$

- At $\theta=2/3$, $T=6$. For $v=4$, $4\cdot3^6-3=2913<3^8$, so $r=7$ works with strict slack. A direct choice is $u=13/12$ and $\lambda=4/3$. Indeed $4/3<8-6u=3/2$ and $J_4(u)\le\log(48/13)<(4/3)\log3$.
- Throughout $2<v\le4$ one has $M_v(T)>T+1$ for $T>1$, since $(v-1)^T>v-1$. At $T=6$ this rules out a positive certified bracket for $r=6$ throughout this family, including after optimizing $u$. It leaves open stronger sieve weights and additional arithmetic input.
- For $v=4$, $r=6$ works as soon as $\delta>1/\log_3((3^7+3)/4)=0.17423459\ldots$. At $\theta=27/40$ one has $T=40/7$ and the strict inequality follows from $4^7 3^{40}<(3^7+3)^7$. Choose $u=u_*$ and $\lambda$ halfway between the strict endpoints. With the original window a distribution bound of the displayed type beyond this level is one sufficient input. The wider window supplies it through the published theorem.

No estimate above bounds the number of surviving composite partners below the total surviving weight for the purpose of proving $G_1>0$. Even the elementary sign requirement $\lambda<2-uT$ is impossible for $T=6$ and $u>1$. The constructive [residue-count obstruction](ReflectedResidualExterior.md) and this positive almost-prime result therefore identify different pieces of the problem: actual prime input and a distribution theorem give genuine two-end information, while a positive lower bound for two genuine primes still requires more.
