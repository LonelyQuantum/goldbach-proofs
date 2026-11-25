import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace GoldbachReflectedFactors

private theorem centers {p b h k l u v : ℤ}
    (hb : 0 ≤ b) (hp : b^2 < p-b) (hh : 0 < h)
    (hu : 0 ≤ u) (hv : 0 ≤ v) (huk : u ≤ b+k) (hvl : v ≤ b+l)
    (h₁ : (p+k)^2-u^2 = p^2+h) (h₂ : (p+l)^2-v^2 = p^2-h) :
    l = -k ∧ 0 < k ∧ p*k ≤ h ∧ u^2+v^2 = 2*k^2 ∧ |h-2*p*k| ≤ k^2 := by
  have hp' : 0 < p-b := lt_of_le_of_lt (sq_nonneg b) hp
  have hu' := mul_nonneg (sub_nonneg.mpr huk) (show 0 ≤ b+k+u by omega)
  have hv' := mul_nonneg (sub_nonneg.mpr hvl) (show 0 ≤ b+l+v by omega)
  have hs : k+l ≤ 0 := by
    by_contra! h
    have H := mul_nonneg hp'.le (show 0 ≤ k+l-1 by omega)
    nlinarith only [H, h₁, h₂, hu', hv', hp]
  have hk : k ≤ b := by omega
  have hl : l ≤ b := by omega
  have Hk := mul_nonneg (sub_nonneg.mpr hk) (show 0 ≤ b+k by omega)
  have Hl := mul_nonneg (sub_nonneg.mpr hl) (show 0 ≤ b+l by omega)
  have heq : l = -k := by
    by_contra h
    have H := mul_nonneg (show 0 ≤ p by omega) (show 0 ≤ -(k+l)-1 by omega)
    nlinarith only [H, h₁, h₂, Hk, Hl, sq_nonneg u, sq_nonneg v, hb, hp]
  subst l
  have circle : u^2+v^2 = 2*k^2 := by linarith only [h₁, h₂]
  have hkpos : 0 < k := by
    by_contra! h
    have H := mul_nonneg (neg_nonneg.mpr h) (show 0 ≤ 2*p+k by omega)
    nlinarith only [H, h₁, sq_nonneg u, hh]
  have H := mul_nonneg hkpos.le (show 0 ≤ p-k by omega)
  refine ⟨rfl, hkpos, ?_, circle, abs_le.mpr ⟨?_, ?_⟩⟩
  · nlinarith only [h₁, circle, sq_nonneg v, H]
  · nlinarith only [h₁, circle, sq_nonneg v]
  · nlinarith only [h₁, sq_nonneg u]

end GoldbachReflectedFactors

/-- Reflected products whose factors are close to the same integer have opposite
midpoint displacements and half-differences on a common integer circle. -/
theorem PEqualNP.Outside.L_goldbach_reflected_factor_centers :
    ∀ (p b h a₁ a₂ c₁ c₂ : ℤ), 0 ≤ b → b^2 < p-b → 0 < h → p-b ≤ a₁ → a₁ ≤ a₂ → p-b ≤ c₁ → c₁ ≤ c₂ → Even (a₁+a₂) → Even (c₁+c₂) → a₁*a₂ = p^2+h → c₁*c₂ = p^2-h → ∃ k u v : ℤ, 0 < k ∧ p*k ≤ h ∧ 0 ≤ u ∧ 0 ≤ v ∧ a₁ = p+k-u ∧ a₂ = p+k+u ∧ c₁ = p-k-v ∧ c₂ = p-k+v ∧ u^2+v^2 = 2*k^2 ∧ |h-2*p*k| ≤ k^2 := by
  intro p b h a₁ a₂ c₁ c₂ hb hp hh ha ha' hc hc' ea ec A C
  obtain ⟨m, hm⟩ := ea
  obtain ⟨n, hn⟩ := ec
  let k := m-p
  let l := n-p
  let u := m-a₁
  let v := n-c₁
  have ha₁ : a₁ = p+k-u := by dsimp [k,u]; omega
  have ha₂ : a₂ = p+k+u := by dsimp [k,u]; omega
  have hc₁ : c₁ = p+l-v := by dsimp [l,v]; omega
  have hc₂ : c₂ = p+l+v := by dsimp [l,v]; omega
  have hu : 0 ≤ u := by dsimp [u]; omega
  have hv : 0 ≤ v := by dsimp [v]; omega
  have A' : (p+k)^2-u^2 = p^2+h := by
    rw [ha₁, ha₂] at A
    linarith only [A]
  have C' : (p+l)^2-v^2 = p^2-h := by
    rw [hc₁, hc₂] at C
    linarith only [C]
  obtain ⟨e, hk, hpk, circle, dist⟩ := GoldbachReflectedFactors.centers hb hp hh hu hv
    (show u ≤ b+k by omega) (show v ≤ b+l by omega) A' C'
  refine ⟨k,u,v,hk,hpk,hu,hv,ha₁,ha₂,?_,?_,circle,dist⟩
  · omega
  · omega
