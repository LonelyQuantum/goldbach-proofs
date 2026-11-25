import Mathlib.Algebra.Order.BigOperators.Group.Finset

namespace GoldbachReflection

variable {α β : Type*} [DecidableEq α]

/-- Ordered pairs lost after changing a binary support are charged to deleted endpoints. -/
theorem orderedHits_le_after_edits (R : α ≃ α) (A B : Finset α) :
    (A.filter fun x => R x ∈ A).card ≤
      (B.filter fun x => R x ∈ B).card + 2 * (A \ B).card := by
  let hits (U : Finset α) := U.filter fun x => R x ∈ U
  let D := A \ B
  have cover : hits A ⊆ (hits B ∪ D) ∪ D.image R.symm := by
    intro x hx
    obtain ⟨xa, ra⟩ := Finset.mem_filter.mp hx
    by_cases xb : x ∈ B
    · by_cases rb : R x ∈ B
      · exact Finset.mem_union_left _ (Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨xb, rb⟩))
      · apply Finset.mem_union_right
        exact Finset.mem_image.mpr ⟨R x, Finset.mem_sdiff.mpr ⟨ra, rb⟩, R.symm_apply_apply x⟩
    · exact Finset.mem_union_left _ (Finset.mem_union_right _ (Finset.mem_sdiff.mpr ⟨xa, xb⟩))
  have imageCard : (D.image R.symm).card ≤ D.card := Finset.card_image_le
  have first := Finset.card_union_le (hits B) D
  have second := Finset.card_union_le (hits B ∪ D) (D.image R.symm)
  have bound := Finset.card_le_card cover
  change (hits A).card ≤ (hits B).card + 2 * D.card
  omega

/-- Fiber counts force a lower bound on intersection, with truncated natural subtraction. -/
theorem floor_le_overlap [Fintype α] [Fintype β] [DecidableEq β]
    (c : α → β) (A B : Finset α) :
    (∑ b, ((A.filter fun x => c x = b).card + (B.filter fun x => c x = b).card -
      (Finset.univ.filter fun x => c x = b).card)) ≤ (A ∩ B).card := by
  let part (s : Finset α) (b : β) := s.filter fun x => c x = b
  calc
    _ ≤ ∑ b, (part (A ∩ B) b).card := by
      apply Finset.sum_le_sum
      intro b _
      have cap : part A b ∪ part B b ⊆ part Finset.univ b := by
        intro x hx
        rcases Finset.mem_union.mp hx with h | h <;>
          exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, (Finset.mem_filter.mp h).2⟩
      have inter : part A b ∩ part B b = part (A ∩ B) b := by
        ext x
        simp [part, and_assoc, and_left_comm, and_comm]
      have size := Finset.card_union_add_card_inter (part A b) (part B b)
      rw [inter] at size
      have upper := Finset.card_le_card cap
      change (part A b).card + (part B b).card - (part Finset.univ b).card ≤ _
      omega
    _ = _ := (Finset.card_eq_sum_card_fiberwise (f := c)
      (s := A ∩ B) (t := Finset.univ) (fun _ _ => Finset.mem_univ _)).symm

end GoldbachReflection
