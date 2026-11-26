/-
Ville's inequality, finite horizon, for a non-negative supermartingale:
  ε · μ {ω | ε ≤ max_{k ≤ n} W k ω} ≤ E[W 0].
This is the step that Propositions 3(a) and 4(a) apply once the wealth is shown to be a
non-negative supermartingale. The proof follows Mathlib's Doob maximal inequality
(`smul_le_stoppedValue_hittingBtwn`), with optional stopping applied to `-W`.
-/
import Mathlib.Probability.Martingale.OptionalStopping

open MeasureTheory Finset
open scoped NNReal ENNReal

namespace Claim

variable {Ω : Type*} {m0 : MeasurableSpace Ω} {μ : Measure Ω} {𝒢 : Filtration ℕ m0}
  {W : ℕ → Ω → ℝ}

theorem ville_finite [IsFiniteMeasure μ] (hsup : Supermartingale W 𝒢 μ) (hnn : 0 ≤ W)
    (ε : ℝ≥0) (n : ℕ) :
    ε • μ {ω | (ε : ℝ) ≤ (range (n + 1)).sup' nonempty_range_add_one fun k => W k ω} ≤
      ENNReal.ofReal (∫ ω, W 0 ω ∂μ) := by
  set A := {ω | (ε : ℝ) ≤ (range (n + 1)).sup' nonempty_range_add_one fun k => W k ω}
  set τ : Ω → WithTop ℕ := fun ω ↦ ((hittingBtwn W {y : ℝ | ε ≤ y} 0 n ω : ℕ) : WithTop ℕ)
  have hτ : IsStoppingTime 𝒢 τ :=
    hsup.stronglyAdapted.adapted.isStoppingTime_hittingBtwn measurableSet_Ici
  have hbdd : ∀ ω, τ ω ≤ n := fun ω => by simpa [τ] using (hittingBtwn_le ω : _ ≤ n)
  have hneg := hsup.neg
  have hint : Integrable (stoppedValue W τ) μ := by
    have := hneg.integrable_stoppedValue hτ hbdd
    have he : stoppedValue (-W) τ = -stoppedValue W τ := by
      funext ω; simp [stoppedValue]
    rw [he] at this
    simpa using this.neg
  -- on A the stopped value is at least ε
  have hA : ∀ ω ∈ A, (ε : ℝ) ≤ stoppedValue W τ ω := by
    intro x hx
    simp only [A, Set.mem_ofPred_eq] at hx
    simp_rw [le_sup'_iff, mem_range, Nat.lt_succ_iff] at hx
    refine stoppedValue_hittingBtwn_mem (s := {y : ℝ | ε ≤ y}) ?_
    obtain ⟨j, hj₁, hj₂⟩ := hx
    exact ⟨j, ⟨Nat.zero_le _, hj₁⟩, hj₂⟩
  have hAmeas : MeasurableSet A := measurableSet_le measurable_const
    (measurable_range_sup'' fun k _ => (hsup.stronglyMeasurable k).measurable.le (𝒢.le k))
  have h1 : (ε : ℝ) * μ.real A ≤ ∫ ω in A, stoppedValue W τ ω ∂μ := by
    have := setIntegral_ge_of_const_le_real hAmeas (measure_ne_top _ _) hA hint.integrableOn
    simpa [mul_comm] using this
  have hnnτ : 0 ≤ stoppedValue W τ := fun ω => by simp only [stoppedValue]; exact hnn _ ω
  have h2 : ∫ ω in A, stoppedValue W τ ω ∂μ ≤ ∫ ω, stoppedValue W τ ω ∂μ :=
    setIntegral_le_integral hint (Filter.Eventually.of_forall hnnτ)
  -- optional stopping for the submartingale -W between 0 and τ
  have h3 : ∫ ω, stoppedValue W τ ω ∂μ ≤ ∫ ω, W 0 ω ∂μ := by
    have := hneg.expected_stoppedValue_mono (isStoppingTime_const 𝒢 0) hτ
      (fun ω => by simp) hbdd
    simp only [stoppedValue_const] at this
    have he : stoppedValue (-W) τ = -stoppedValue W τ := by funext ω; simp [stoppedValue]
    rw [he] at this
    simp only [Pi.neg_apply, integral_neg] at this
    linarith
  rw [ENNReal.le_ofReal_iff_toReal_le, ENNReal.toReal_smul]
  · simp only [smul_eq_mul, NNReal.smul_def] at *
    calc (ε : ℝ) * (μ A).toReal = (ε : ℝ) * μ.real A := rfl
      _ ≤ _ := h1
      _ ≤ _ := h2
      _ ≤ _ := h3
  · exact ENNReal.mul_ne_top (by simp) (measure_ne_top _ _)
  · exact integral_nonneg (fun ω => hnn 0 ω)

end Claim
