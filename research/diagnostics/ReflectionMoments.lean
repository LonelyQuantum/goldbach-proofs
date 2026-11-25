module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Data.Finset.Card
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring

/-! Two local moments of normalized weights bound how many allowed endpoints are occupied.
The indices in the two finsets describe the positive and negative sides of the midpoint. -/
@[expose] public section

namespace FiniteGoldbach.ReflectionMoments

open Finset

variable {ι : Type*}

/-- The contribution of a weight divided by its reference value. -/
def score (x : ℝ) : ℝ := 2*x - x^2

private theorem score_le_one (x : ℝ) : score x ≤ 1 := by
  unfold score
  nlinarith only [sq_nonneg (x-1)]

/-- Replacing the weights on any omitted endpoints by zero limits the total score. -/
theorem score_le_support (s : Finset ι) (x : ι → ℝ) :
    ∑ i ∈ s, score (x i) ≤ ((s.filter (fun i => x i ≠ 0)).card : ℝ) := by
  classical
  calc
    _ ≤ ∑ i ∈ s, (if x i ≠ 0 then (1 : ℝ) else 0) := by
      apply sum_le_sum
      intro i _
      by_cases h : x i = 0
      · simp [h, score]
      · simpa [h] using score_le_one (x i)
    _ = ∑ i ∈ s.filter (fun i => x i ≠ 0), (1 : ℝ) := by rw [sum_filter]
    _ = _ := by simp

/-- A score strictly above one less than the number of allowed sites fills every site. -/
theorem full_support_of_score (s : Finset ι) (x : ι → ℝ)
    (h : (s.card : ℝ) - 1 < ∑ i ∈ s, score (x i)) :
    ∀ i ∈ s, x i ≠ 0 := by
  classical
  intro i hi hz
  let t := s.filter (fun j => x j ≠ 0)
  have hst : t ⊂ s := by
    refine Finset.ssubset_iff_subset_ne.mpr ⟨filter_subset _ _, ?_⟩
    intro heq
    have hit : i ∈ t := heq.symm ▸ hi
    exact (mem_filter.mp hit).2 hz
  have hc : t.card + 1 ≤ s.card := card_lt_card hst
  have hc' : (t.card : ℝ) + 1 ≤ (s.card : ℝ) := by exact_mod_cast hc
  have hs : ∑ j ∈ s, score (x j) ≤ (t.card : ℝ) := score_le_support s x
  linarith only [h, hs, hc']

/-- Exact maximum among reflected pairs with at most one endpoint occupied.
The midpoint is excluded. Both weights vanish outside their permitted sets. -/
theorem pair_free_max [DecidableEq ι] (p q : Finset ι) :
    let admissible := fun x y : ι → ℝ =>
      (∀ i, 0 ≤ x i ∧ 0 ≤ y i) ∧ (∀ i ∉ p, x i = 0) ∧
      (∀ i ∉ q, y i = 0) ∧ (∀ i, x i * y i = 0)
    let total := fun x y : ι → ℝ => ∑ i ∈ p ∪ q, (score (x i) + score (y i))
    (∀ x y, admissible x y → total x y ≤ ((p ∪ q).card : ℝ)) ∧
      ∃ x y, admissible x y ∧ total x y = ((p ∪ q).card : ℝ) := by
  classical
  dsimp only
  constructor
  · intro x y h
    calc
      _ ≤ ∑ i ∈ p ∪ q, (1 : ℝ) := by
        apply sum_le_sum
        intro i _
        rcases mul_eq_zero.mp (h.2.2.2 i) with hz | hz
        · simpa [hz, score] using score_le_one (y i)
        · simpa [hz, score] using score_le_one (x i)
      _ = _ := by simp
  · refine ⟨fun i => if i ∈ p then 1 else 0, fun i => if i ∈ q ∧ i ∉ p then 1 else 0, ?_, ?_⟩
    · exact ⟨fun i => by dsimp only; split_ifs <;> simp, fun i hi => by simp [hi],
        fun i hi => by simp [hi], fun i => by by_cases h : i ∈ p <;> simp [h]⟩
    · calc
        _ = ∑ i ∈ p ∪ q, (1 : ℝ) := by
          apply sum_congr rfl
          intro i hi
          by_cases h : i ∈ p
          · simp [h, score]
            ring
          · have hq := (mem_union.mp hi).resolve_left h
            simp [h, hq, score]
            ring
        _ = _ := by simp

private theorem score_add_defect (s : Finset ι) (x : ι → ℝ) :
    (∑ i ∈ s, score (x i)) + (∑ i ∈ s, (x i-1)^2) = (s.card : ℝ) := by
  rw [← sum_add_distrib]
  calc
    _ = ∑ i ∈ s, (1 : ℝ) := by
      apply sum_congr rfl
      intro i _
      unfold score
      ring
    _ = _ := by simp

/-- Off the midpoint, the amount by which the true score exceeds the pair-free
maximum is exactly the number of double-occupied indices minus the squared defect. -/
theorem score_margin [DecidableEq ι] (p q : Finset ι) (x y : ι → ℝ) :
    (∑ i ∈ p, score (x i)) + (∑ i ∈ q, score (y i)) - ((p ∪ q).card : ℝ) =
      ((p ∩ q).card : ℝ) - ((∑ i ∈ p, (x i-1)^2) + ∑ i ∈ q, (y i-1)^2) := by
  have card : ((p ∪ q).card : ℝ) + ((p ∩ q).card : ℝ) = (p.card : ℝ) + (q.card : ℝ) := by
    exact_mod_cast card_union_add_card_inter p q
  linarith only [card, score_add_defect p x, score_add_defect q y]

private theorem log_diff_le {a b l H : ℝ} (ha : 0 < a) (hl : 0 < l) (hb : l ≤ b)
    (hH : 0 ≤ H) (hab : a-b ≤ H) : Real.log a - Real.log b ≤ H/l := by
  have hb' := hl.trans_le hb
  calc
    _ = Real.log (a/b) := (Real.log_div ha.ne' hb'.ne').symm
    _ ≤ a/b-1 := Real.log_le_sub_one_of_pos (div_pos ha hb')
    _ = (a-b)/b := by rw [sub_div, div_self hb'.ne']
    _ ≤ H/b := div_le_div_of_nonneg_right hab hb'.le
    _ ≤ _ := div_le_div_of_nonneg_left hH hl hb

/-- Squared error of using one reference logarithm on the entire window. -/
theorem window_log_defect (s : Finset ι) (j : ι → ℝ) {m H : ℝ}
    (hm : 1 < m) (hH : 0 ≤ H) (hl : H < m)
    (hw : ∀ i ∈ s, m-H ≤ j i ∧ j i ≤ m+H) :
    ∑ i ∈ s, (Real.log (j i)/Real.log m-1)^2 ≤
      (s.card : ℝ) * (H/((m-H)*Real.log m))^2 := by
  have hm' : 0 < m := by linarith
  have hl' : 0 < m-H := sub_pos.mpr hl
  have hlog := Real.log_pos hm
  calc
    _ ≤ ∑ _i ∈ s, (H/((m-H)*Real.log m))^2 := by
      apply sum_le_sum
      intro i hi
      obtain ⟨hj₁, hj₂⟩ := hw i hi
      have hj := hl'.trans_le hj₁
      have upper := log_diff_le hj hl' (show m-H ≤ m by linarith) hH (show j i-m ≤ H by linarith)
      have lower := log_diff_le hm' hl' hj₁ hH (show m-j i ≤ H by linarith)
      have habs : |Real.log (j i) - Real.log m| ≤ H/(m-H) :=
        abs_le.mpr ⟨by linarith only [lower], upper⟩
      have heq : Real.log (j i)/Real.log m-1 = (Real.log (j i)-Real.log m)/Real.log m := by
        rw [sub_div, div_self hlog.ne']
      rw [heq, ← sq_abs, abs_div, abs_of_pos hlog, ← div_div]
      exact pow_le_pow_left₀ (by positivity) (div_le_div_of_nonneg_right habs hlog.le) 2
    _ = _ := by simp

/-- A concrete separation margin at integer window radii with H³ ≤ m².
An integer window of radius H ≥ 1 has at most 2H+1 ≤ 3H sites. -/
theorem cubic_window_defect (s : Finset ι) (j : ι → ℝ) {m H : ℝ}
    (hm : 256 ≤ m) (hH : 0 ≤ H) (hcube : H^3 ≤ m^2) (hc : (s.card : ℝ) ≤ 3*H)
    (hw : ∀ i ∈ s, m-H ≤ j i ∧ j i ≤ m+H) :
    ∑ i ∈ s, (Real.log (j i)/Real.log m-1)^2 ≤ 1/3 := by
  have hm' : 0 < m := by linarith
  have hfour : 4*H ≤ m := by
    by_contra! h
    have hcub := pow_lt_pow_left₀ h hm'.le (by decide : 3 ≠ 0)
    nlinarith only [hcub, hcube, mul_nonneg (sq_nonneg m) (show 0 ≤ m-64 by linarith)]
  have hlog : 4 ≤ Real.log m := by
    have htwo := Real.one_sub_inv_le_log_of_pos (by norm_num : (0:ℝ) < 2)
    have hp := Real.log_le_log (show (0:ℝ) < 2^8 by norm_num) (show (2:ℝ)^8 ≤ m by norm_num; exact hm)
    rw [Real.log_pow] at hp
    norm_num at hp htwo
    linarith
  have hd : 3*m ≤ (m-H)*Real.log m := by
    nlinarith only [hfour, mul_nonneg (show 0 ≤ m-H by linarith) (sub_nonneg.mpr hlog)]
  calc
    _ ≤ _ := window_log_defect s j (by linarith) hH (by linarith) hw
    _ ≤ 3*H * (H/(3*m))^2 := by
      apply mul_le_mul hc _ (sq_nonneg _) (by positivity)
      have hd' : 0 < (m-H)*Real.log m := lt_of_lt_of_le (by linarith : 0 < 3*m) hd
      exact pow_le_pow_left₀ (div_nonneg hH hd'.le) (div_le_div_of_nonneg_left hH (by linarith) hd) 2
    _ ≤ _ := by
      rw [div_pow, ← mul_div_assoc, div_le_iff₀ (by positivity : 0 < (3*m)^2)]
      nlinarith only [hcube]

end FiniteGoldbach.ReflectionMoments
