/-
Proposition 5 (conjunctive promotion): the intersection–union principle.
If promotion requires both processes to cross, then under any law in which
either null holds, the probability of promotion is at most the level that
null's process guarantees.
-/
import Mathlib.MeasureTheory.Measure.Basic

open MeasureTheory

namespace Claim

variable {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)

/-- The promotion event lies inside both crossing events, so its probability is
bounded by whichever crossing probability the true null controls. -/
theorem conjunctive_promotion {Promote CrossW CrossM : Set Ω} {α : ENNReal}
    (hW : Promote ⊆ CrossW) (hM : Promote ⊆ CrossM)
    (hnull : μ CrossW ≤ α ∨ μ CrossM ≤ α) : μ Promote ≤ α := by
  rcases hnull with h | h
  · exact (measure_mono hW).trans h
  · exact (measure_mono hM).trans h

end Claim
