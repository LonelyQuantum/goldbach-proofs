# How much numerator cancellation suffices on the rational bands?

Let $p$ tend to infinity through odd primes, $n=2p^2$, $H=\lfloor p^{4/3}\rfloor$, $M=2H+1$ and $Q=\lfloor\log_2(n+2)\rfloor^2$. Put $e(t)=\exp(2\pi i t)$ and let $S(t)=\sum_{|\ell-p^2|\le H,\ \ell\ {\rm prime}}\log(\ell)e(\ell t)$. We estimate weighted integrals of $f=\operatorname{Re}(S^2e(-nt))$ over the bands $Q/(qn)<|\beta|\le Q/(qM)$ centered at reduced $a/q$ on the circle, $q\le Q$. Distinct bands are disjoint for large $p$. A weight in $[0,1]$ specifies how much of each point to retain.

**Result.** Retain the entire $q=1$ band. At a squarefree $q\ge3$, let $\ell$ be its largest odd prime divisor. Group the reduced numerators $a$ by their class modulo $q/\ell$, and at each fixed offset $\beta$ require weights within each group to differ by at most $\delta\in[0,1]$. The $q=2$ band and nonsquarefree denominators have arbitrary weights. All weights are measurable. Write $I_\delta(p)$ for the infimum over the allowed weighted integrals.

* If $\delta=0$, **every** such selection retains more than $M/5$ of signed mass for all sufficiently large $p$.
* There is a constant $1/5<K<1/4$ such that whenever $\delta\log Q\to\lambda<\infty$,
  $$
  I_\delta(p)/M\longrightarrow K-\lambda/\pi .
  $$
  The limiting sign changes at $\lambda=\pi K$. If $\delta\log Q\to\infty$, then $I_\delta(p)/M\to-\infty$.

This is a stability result for **these rational bands and this central window**. The extremizing weights are allowed to depend on $p$ and on the integrand. The region outside the bands still enters the Goldbach coefficient.

## Grouping by one prime divisor

On a band the real model for $f$ is
$$
 \frac{\mu(q)^2}{\varphi(q)^2}D_H(\beta)^2\cos(2\pi n a/q),\qquad
 D_H(\beta)=\sum_{|j|\le H}e(j\beta).
$$
The total integral of the absolute approximation error is $o(M)$ by the uniform short-progression estimate. This also bounds the error after any of our weight selections. Put $J_q=M^{-1}\int_{\rm offsets}D_H(\beta)^2\,d\beta$ if $q\le Q$, and zero otherwise. Orthogonality gives $0\le J_q\le1$, and $J_q\to1$ for each fixed $q$ by the central Dirichlet-kernel profile. The signed mass of all bands is $(2C_2+o(1))M$ for $C_2=\prod_{\ell>2,\ \ell\ {\rm prime}}(1-(\ell-1)^{-2})$. Also the negative part before any grouping integrates to $M(\pi^{-1}\log Q+O(1))$. These are the analytic inputs. [Arc profile](CentralWindowArcScale.md) · [Positive and negative mass](CentralWindowSignedMass.md) · [Baier and Zhao, Lemma 6](https://arxiv.org/pdf/math/0701577v6#page=5)

For a squarefree $q\ge3$, write $t=q/\ell$. The $\ell$ lifts of a unit $r\bmod t$ form a complete progression modulo $q$. Their phases $e(-na/q)$ sum to zero since $\ell\nmid n$ for $q\le Q<p$. Exactly one lift, say $\ell b$, is divisible by $\ell$. The sum over the reduced lifts is therefore **exactly** $-e(-nb/t)$. This is a complex number of modulus one. Its real part can have either sign. The same $\beta$ and weight in a group allow this summation before taking absolute values.

Write $q=d$ or $q=2d$ with $d$ odd squarefree, $d>1$, and set $s=d/\ell$. As $r$ varies, the residual phases range once over the negatives of the primitive $s$-th roots of unity. For odd $q$ this follows from invertibility of $\ell$ and $n$ modulo $s$. For even $q$, project the units modulo $2s$ to those modulo $s$ and use $n=2p^2$. For $s=1$ interpret the unique primitive root as $1$.

## Exact worst case with common weights

Define two absolutely convergent sums over odd squarefree $d>1$, taking $\ell$ and $s$ as above,
$$
 C=\sum_d\frac{\varphi(s)}{\varphi(d)^2},\qquad
 V=\sum_d\frac{1}{\varphi(d)^2}\sum_{b\bmod s}^{*}|\cos(2\pi b/s)|.
$$
In particular $V\le C$. Grouping by the largest prime gives
$$
 C=\sum_{\ell>2,\ \ell\ {\rm prime}}\frac{1}{(\ell-1)^2}
      \prod_{3\le r<\ell,\ r\ {\rm prime}}\frac{r}{r-1}.
$$
A convergent numerical majorant with an explicit tail appears below. Outside $q=1,2$, the normalized total variation after grouping tends to $2V$: each $d$ occurs with both denominators $d,2d$ and we apply dominated convergence to $J_q$. The normalized signed sum there tends to $2C_2-2$, since each omitted denominator contributes $1+o(1)$. The sum of the negative parts of the grouped model, divided by $M$, thus tends to $1+V-C_2$. The minimum integral retains the $q=1$ anchor, drops $q=2$ and retains the negative groups. Uniform $o(M)$ replacement transfers the same limiting minimum to the prime sum. Hence $K=C_2-V$.

To bound $K$, use $x^2\le|x|\le(1+x^2)/2$ for $|x|\le1$. The squared cosines sum to $(\varphi(s)+\mu(s))/2$ because $s$ is odd squarefree and the sum of primitive $s$-th roots is $\mu(s)$. Furthermore
$$
 \sum_d\frac{\mu(s)}{\varphi(d)^2}
 =\sum_\ell\frac{1}{(\ell-1)^2}
       \prod_{3\le r<\ell,\ r\ {\rm prime}}(1-(r-1)^{-2})=1-C_2
$$
by telescoping consecutive partial products. We obtain
$$
 \frac{5C_2-3C-1}{4}\le K\le \frac{3C_2-C-1}{2}. \tag{1}
$$

For a rational certificate, sum the series for $C$ through $1001$, obtaining $C_0$. Let $A$ and $B$ be the products of $r/(r-1)$ and $1-(r-1)^{-2}$, respectively, over the odd primes through the same cutoff. Then
$$
 C_0\le C\le C_0+A/1000,\qquad B(1-1/2000)\le C_2\le B .
$$
Indeed at $\ell=2h+1$ with $h>500$ the positive product beyond the cutoff is at most $\sqrt{(2h-1)/1001}$: square the factors for all intervening odd integers and use $(1+1/(2j))^2\le(2j+1)/(2j-1)$. Bound the tail by summing over all $h>500$ and use $\sum_{h>500}h^{-3/2}\le2/\sqrt{500}$. For $B$ use $\sum_{h>500}(4h^2)^{-1}\le1/2000$. Exact fractions in (1), rounded outwards, give $0.201969\le K\le0.244840$.

## Allowing variation within a group

For any finite real list $x_i$ and weights $0\le w_i\le1$ of spread at most $\delta$,
$$
 \min_w\sum_i w_i x_i=(1-\delta)\min(0,\sum_i x_i)+\delta\sum_i\min(0,x_i).
$$
For $0<\delta<1$ any feasible vector is a common weight with coefficient $1-\delta$ plus individual weights with coefficient $\delta$: choose the common contribution in $[\max(0,\max_i w_i-\delta),\,\min(1-\delta,\min_i w_i)]$. Equality is attained by the common indicator of a negative group sum and individual indicators of negative entries. The endpoints follow directly. These choices are measurable in $\beta$. Applying this identity to the **actual integrand** yields exactly $I_\delta=(1-\delta)I_0+\delta I_1$. The fixed anchor enters both sides identically. With unrestricted weights off the anchor, the previous negative-mass estimate gives $I_1/M=-\pi^{-1}\log Q+O(1)$; the model of the anchor is nonnegative and its mass is $M(1+o(1))$. This proves the transition claimed above. At the threshold the leading normalized term is zero and the formula gives no eventual sign.

The [standalone exact check](LargestPrimeFiberCheck.py) also tests the residue multisets for $p=1009,1013$ and $q\le350$ (1188 groups), and compares the finite minimization against exhaustive weight grids in 840 cases. The rational bounds use all 167 odd primes through 1001.
