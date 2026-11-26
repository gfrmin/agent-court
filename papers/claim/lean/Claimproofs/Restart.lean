/-
Proposition 4(b): what restarting each window costs.
With k windows each crossing falsely with probability r_j ≤ α:
independence gives 1 - ∏(1 - r_j) ≤ 1 - (1 - α)^k, and in general the
union bound gives at most ∑ r_j ≤ k α.
-/
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.MeasureTheory.Measure.Basic

open Finset MeasureTheory

namespace Claim

theorem restart_independent {k : ℕ} (r : Fin k → ℝ) {α : ℝ}
    (hα : ∀ j, r j ≤ α) (hα1 : α ≤ 1) :
    1 - ∏ j, (1 - r j) ≤ 1 - (1 - α) ^ k := by
  have hle : (1 - α) ^ k ≤ ∏ j, (1 - r j) := by
    have : (1 - α) ^ k = ∏ _j : Fin k, (1 - α) := by simp
    rw [this]
    exact Finset.prod_le_prod₀ (fun j _ => by linarith [hα j]) (fun j _ => by linarith [hα j])
  linarith

theorem restart_union {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω) {k : ℕ}
    (A : Fin k → Set Ω) {α : ENNReal} (hα : ∀ j, μ (A j) ≤ α) :
    μ (⋃ j, A j) ≤ k * α := by
  calc μ (⋃ j, A j) ≤ ∑ j, μ (A j) := measure_iUnion_fintype_le μ A
    _ ≤ ∑ _j : Fin k, α := Finset.sum_le_sum (fun j _ => hα j)
    _ = k * α := by simp

end Claim
