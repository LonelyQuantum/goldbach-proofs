import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace GoldbachRichert

/-- The Richert penalty, with each prime counted with multiplicity. -/
noncomputable def penalty (a : ℕ) (y : ℝ) : ℝ :=
  a.factorization.sum fun q e => (e : ℝ) * max (1 - Real.log q / Real.log y) 0

theorem factor_budget (a : ℕ) (y : ℝ) :
    (ArithmeticFunction.cardFactors a : ℝ) - Real.log a / Real.log y ≤ penalty a y := by
  rw [ArithmeticFunction.cardFactors_eq_sum_factorization, Real.log_nat_eq_sum_factorization]
  simp only [penalty, Finsupp.sum, Nat.cast_sum, div_eq_mul_inv, Finset.sum_mul,
    ← Finset.sum_sub_distrib]
  apply Finset.sum_le_sum
  intro q _
  calc
    _ = (a.factorization q : ℝ) * (1 - Real.log q / Real.log y) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (le_max_left _ _) (Nat.cast_nonneg _)

/-- A positive total weight certifies elements with at most r prime factors. -/
theorem weighted_count_le (A : Finset ℕ) (r : ℕ) (y b lam : ℝ) (hlam : 0 < lam)
    (hsize : ∀ a ∈ A, Real.log a / Real.log y ≤ b)
    (hbudget : b + lam ≤ (r : ℝ) + 1) :
    (∑ a ∈ A, (1 - penalty a y / lam)) ≤
      ((A.filter fun a => ArithmeticFunction.cardFactors a ≤ r).card : ℝ) := by
  calc
    _ ≤ ∑ a ∈ A, (if ArithmeticFunction.cardFactors a ≤ r then (1 : ℝ) else 0) := by
      apply Finset.sum_le_sum
      intro a ha
      by_cases good : ArithmeticFunction.cardFactors a ≤ r
      · simp only [good, ↓reduceIte]
        have hn : 0 ≤ penalty a y := by
          unfold penalty Finsupp.sum
          apply Finset.sum_nonneg
          intro q _
          exact mul_nonneg (Nat.cast_nonneg _) (le_max_right _ _)
        linarith [div_nonneg hn hlam.le]
      · simp only [good, ↓reduceIte]
        have hc : r + 1 ≤ ArithmeticFunction.cardFactors a := Nat.lt_iff_add_one_le.mp (Nat.lt_of_not_ge good)
        have hcr : (r : ℝ) + 1 ≤ (ArithmeticFunction.cardFactors a : ℝ) := by exact_mod_cast hc
        have hp : lam ≤ penalty a y := by linarith [factor_budget a y, hsize a ha]
        linarith [(one_le_div hlam).mpr hp]
    _ = _ := by simp [Finset.sum_boole]

end GoldbachRichert
