import Mathlib.Tactic.Linarith

namespace GoldbachSquareWindow

/-- A repeated mixed square sum forces the two block origins close to a rational slope.
    The inequality is cleared of denominators, so it also applies on the integer grid. -/
theorem mixed_window_origin_bounds
    (X H U V a b c d : ℤ) (hX : 0 < X) (hU : X ≤ U) (hV : X ≤ V)
    (hUc : U ≤ c) (hca : c < a) (haU : a < U + H) (haX : a ≤ 2 * X)
    (hVb : V ≤ b) (hbd : b < d) (hdV : d < V + H) (hdX : d ≤ 2 * X)
    (hs : a ^ 2 + b ^ 2 = c ^ 2 + d ^ 2) :
    let h := a - c
    let k := d - b
    0 < h ∧ h < H ∧ 0 < k ∧ k < H ∧ h ≤ 2 * k ∧ k ≤ 2 * h ∧
      -(H - 1) * k ≤ k * V - h * U ∧ k * V - h * U ≤ 2 * (H - 1) * k := by
  dsimp only
  have hh : 0 < a - c := by omega
  have hk : 0 < d - b := by omega
  have cross : (a - c) * (a + c) = (d - b) * (b + d) := by nlinarith only [hs]
  have ratio (h k s t : ℤ) (hp : 0 < h) (kp : 0 < k) (hx : 2 * X ≤ s)
      (tx : t ≤ 4 * X) (eqn : h * s = k * t) : h ≤ 2 * k := by
    by_contra! large
    nlinarith only [eqn, mul_nonneg hp.le (sub_nonneg.mpr hx),
      mul_nonneg kp.le (sub_nonneg.mpr tx), mul_pos hX (sub_pos.mpr large)]
  have ratio₁ := ratio _ _ _ _ hh hk (show 2 * X ≤ a + c by omega)
    (show b + d ≤ 4 * X by omega) cross
  have ratio₂ := ratio _ _ _ _ hk hh (show 2 * X ≤ b + d by omega)
    (show a + c ≤ 4 * X by omega) cross.symm
  refine ⟨hh, by omega, hk, by omega, ratio₁, ratio₂, ?_, ?_⟩
  · nlinarith only [cross, mul_nonneg hh.le (show 0 ≤ a + c - 2 * U by omega),
      mul_nonneg hk.le (show 0 ≤ 2 * (V + H - 1) - (b + d) by omega)]
  · nlinarith only [cross, mul_nonneg hk.le (show 0 ≤ b + d - 2 * V by omega),
      mul_nonneg hh.le (show 0 ≤ 2 * (U + H - 1) - (a + c) by omega),
      mul_nonneg (sub_nonneg.mpr ratio₁) (show 0 ≤ H - 1 by omega)]

end GoldbachSquareWindow
