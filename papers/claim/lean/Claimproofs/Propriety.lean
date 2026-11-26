/-
Proposition 2(a): the logarithmic score is strictly proper on (0,1).
For belief π and report p in (0,1), the expected score
  g(p) = π log p + (1 - π) log (1 - p)
is at most g(π), with equality only at p = π.
(The statement about the per-mille grid follows from concavity and is not formalised.)
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic

open Real

namespace Claim

noncomputable def expScore (π p : ℝ) : ℝ := π * Real.log p + (1 - π) * Real.log (1 - p)

theorem log_score_proper {π p : ℝ} (hπ0 : 0 < π) (hπ1 : π < 1) (hp0 : 0 < p) (hp1 : p < 1) :
    expScore π p ≤ expScore π π := by
  unfold expScore
  have h1 : Real.log (p / π) ≤ p / π - 1 := Real.log_le_sub_one_of_pos (div_pos hp0 hπ0)
  have h2 : Real.log ((1 - p) / (1 - π)) ≤ (1 - p) / (1 - π) - 1 :=
    Real.log_le_sub_one_of_pos (div_pos (by linarith) (by linarith))
  rw [Real.log_div hp0.ne' hπ0.ne'] at h1
  rw [Real.log_div (by linarith) (by linarith)] at h2
  have e1 : π * (p / π - 1) = p - π := by field_simp
  have e2 : (1 - π) * ((1 - p) / (1 - π) - 1) = π - p := by
    have : (1 - π) ≠ 0 := by linarith
    field_simp; ring
  nlinarith [mul_le_mul_of_nonneg_left h1 hπ0.le, mul_le_mul_of_nonneg_left h2 (by linarith : (0:ℝ) ≤ 1 - π)]

theorem log_score_strict {π p : ℝ} (hπ0 : 0 < π) (hπ1 : π < 1) (hp0 : 0 < p) (hp1 : p < 1)
    (hne : p ≠ π) : expScore π p < expScore π π := by
  unfold expScore
  have hq : p / π ≠ 1 := by
    intro h; apply hne; field_simp at h; linarith
  have h1 : Real.log (p / π) < p / π - 1 := Real.log_lt_sub_one_of_pos (div_pos hp0 hπ0) hq
  have h2 : Real.log ((1 - p) / (1 - π)) ≤ (1 - p) / (1 - π) - 1 :=
    Real.log_le_sub_one_of_pos (div_pos (by linarith) (by linarith))
  rw [Real.log_div hp0.ne' hπ0.ne'] at h1
  rw [Real.log_div (by linarith) (by linarith)] at h2
  have e1 : π * (p / π - 1) = p - π := by field_simp
  have e2 : (1 - π) * ((1 - p) / (1 - π) - 1) = π - p := by
    have : (1 - π) ≠ 0 := by linarith
    field_simp; ring
  nlinarith [mul_lt_mul_of_pos_left h1 hπ0, mul_le_mul_of_nonneg_left h2 (by linarith : (0:ℝ) ≤ 1 - π)]

end Claim
