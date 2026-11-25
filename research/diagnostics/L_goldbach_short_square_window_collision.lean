import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace GoldbachSquareWindow

private theorem square_mod_two (x : ℤ) : x ^ 2 % 2 = x % 2 := by
  rw [pow_two, Int.mul_emod]
  have hx : x % 2 = 0 ∨ x % 2 = 1 := by omega
  rcases hx with hx | hx <;> simp [hx]

private theorem sum_mod_two (x y : ℤ) : (x ^ 2 + y ^ 2) % 2 = (x + y) % 2 := by
  rw [Int.add_emod (x ^ 2) (y ^ 2), square_mod_two, square_mod_two, ← Int.add_emod]

end GoldbachSquareWindow

theorem L_goldbach_short_square_window_collision :
    ∀ (P H a b c d : ℤ), 0 ≤ P → 0 ≤ H → H ^ 2 ≤ 8 * P + 4 * H + 4 →
      P ≤ a → a ≤ b → b ≤ P + H → P ≤ c → c ≤ d → d ≤ P + H →
      a ^ 2 + b ^ 2 = c ^ 2 + d ^ 2 → a + b ≤ c + d →
      (a = c ∧ b = d) ∨
        (H ^ 2 = 8 * P + 4 * H + 4 ∧ a = P ∧ b = P + H ∧
          c = d ∧ 2 * c = 2 * P + H + 2) := by
  intro P H a b c d hP hH hwidth ha hab hb hc hcd hd hs horder
  have hpar := congrArg (fun x : ℤ => x % 2) hs
  change (a ^ 2 + b ^ 2) % 2 = (c ^ 2 + d ^ 2) % 2 at hpar
  rw [GoldbachSquareWindow.sum_mod_two, GoldbachSquareWindow.sum_mod_two] at hpar
  by_cases heq : a + b = c + d
  · left
    have hsumsq := congrArg (fun x : ℤ => x ^ 2) heq
    change (a + b) ^ 2 = (c + d) ^ 2 at hsumsq
    have hprod : ((b-a) - (d-c)) * ((b-a) + (d-c)) = 0 := by
      nlinarith only [hs, hsumsq]
    rcases mul_eq_zero.mp hprod with h | h <;> omega
  · right
    have hgap : a + b + 2 ≤ c + d := by omega
    have hsep : 0 ≤ (c+d-(a+b+2)) * (c+d+(a+b+2)) :=
      mul_nonneg (by omega) (by omega)
    have hspan : 8*P + 4*(b-a) + 4 ≤ (b-a)^2 := by
      nlinarith only [hs, hsep, sq_nonneg (d-c), ha]
    have hlarge : 2 < b-a := by
      by_contra! h
      nlinarith only [hspan, hP, hab,
        mul_nonneg (show 0 ≤ 2-(b-a) by omega) (show 0 ≤ b-a by omega)]
    have hfull : b-a = H := by
      by_contra h
      have hstrict : 0 < (H-(b-a)) * (H+(b-a)-4) :=
        mul_pos (by omega) (by omega)
      nlinarith only [hstrict, hwidth, hspan]
    have hleft : a = P := by omega
    have hright : b = P + H := by omega
    have hbound : H ^ 2 = 8*P + 4*H + 4 := by
      rw [hfull] at hspan
      exact le_antisymm hwidth hspan
    have hdiag : (d-c)^2 = 0 := by
      nlinarith only [hs, hsep, hleft, hright, hbound, sq_nonneg (d-c),
        (show (b-a)^2 = H^2 by rw [hfull])]
    have hcd' : c = d := by
      have hz : (d-c)*(d-c) = 0 := by simpa [pow_two] using hdiag
      rcases mul_eq_zero.mp hz with h | h <;> omega
    have hsum : c+d = a+b+2 := by
      by_contra h
      have hpos : 0 < (c+d-(a+b+2)) * (c+d+(a+b+2)) :=
        mul_pos (by omega) (by omega)
      nlinarith only [hs, hpos, hleft, hright, hbound, sq_nonneg (d-c),
        (show (b-a)^2 = H^2 by rw [hfull])]
    exact ⟨hbound, hleft, hright, hcd', by omega⟩
