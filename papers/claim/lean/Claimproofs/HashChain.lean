/-
Proposition 1(b): two different linked logs, numbered from 0 and ending in lines
with the same hash, yield a collision of the hash function.

A log is read from its last line backwards, so we state the result for the reversed
list `R = [e_n, e_{n-1}, …, e_0]`: each line's `parent` is the hash of the line after it
in `R`, and each line's `seq` equals the number of lines after it in `R` (the kernel
numbers entries by position, from the genesis entry at 0).
-/

import Mathlib.Data.List.Basic

namespace Claim

variable {α β : Type*} (hash parent : α → β) (seq : α → ℕ)

/-- Read backwards: each line's `parent` is the hash of the line before it in the log. -/
def RevLinked : List α → Prop
  | x :: y :: rest => parent x = hash y ∧ RevLinked (y :: rest)
  | _ => True

/-- Read backwards: each line's `seq` is its position in the log. -/
def RevNumbered : List α → Prop
  | [] => True
  | x :: rest => seq x = rest.length ∧ RevNumbered rest

theorem collision_of_ne :
    ∀ (xs : List α) (x x' : α) (xs' : List α),
      RevLinked hash parent (x :: xs) → RevLinked hash parent (x' :: xs') →
      RevNumbered seq (x :: xs) → RevNumbered seq (x' :: xs') →
      hash x = hash x' → x :: xs ≠ x' :: xs' → ∃ a b, a ≠ b ∧ hash a = hash b := by
  intro xs
  induction xs with
  | nil =>
    intro x x' xs' _ _ hn hn' hh hne
    by_cases hxy : x = x'
    · subst hxy
      obtain ⟨hs, -⟩ := hn
      obtain ⟨hs', -⟩ := hn'
      cases xs' with
      | nil => exact absurd rfl hne
      | cons _ _ => simp at hs hs'; omega
    · exact ⟨x, x', hxy, hh⟩
  | cons z zs ih =>
    intro x x' xs' hl hl' hn hn' hh hne
    by_cases hxy : x = x'
    · subst hxy
      obtain ⟨hs, hn⟩ := hn
      obtain ⟨hs', hn'⟩ := hn'
      cases xs' with
      | nil => simp at hs hs'; omega
      | cons z' zs' =>
        obtain ⟨hp, hl⟩ := hl
        obtain ⟨hp', hl'⟩ := hl'
        have hz : hash z = hash z' := by rw [← hp, ← hp']
        have htail : (z :: zs) ≠ (z' :: zs') := by
          intro h; exact hne (by rw [h])
        exact ih z z' zs' hl hl' hn hn' hz htail
    · exact ⟨x, x', hxy, hh⟩

end Claim
