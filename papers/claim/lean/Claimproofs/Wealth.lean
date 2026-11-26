/-
Propositions 3(a) and 4(a): the betting wealth is a non-negative supermartingale under the
null, so by Ville's inequality the chance that it ever reaches 1/α (up to any horizon) is at
most α.

`D (n+1)` is the bounded difference scored at step `n+1`, realised by `𝒢 (n+1)`; `L (n+1)` is the
stake, fixed by `𝒢 n` (predictable). The null is `E[D (n+1) | 𝒢 n] ≤ 0`. The hypotheses ask only
that `|D| ≤ B`, `0 ≤ L ≤ M` and that every factor `1 + L * D` lies in `[0, C]`. Both tests fit:
* value (Proposition 3): `D` is the block's mean log-ratio over `log 999`, `|D| ≤ 1`, `0 ≤ L < 1`,
  so `B = M = 1`, `C = 2`;
* liveness (Proposition 4): `D = Y - p₀` with `Y ∈ [0,1]`, `0 ≤ L < 1/p₀`, so `B = 1`,
  `M = 1/p₀`, and `1 + L * D ∈ (0, 1/p₀]`.
-/
import Claimproofs.Ville

open MeasureTheory Finset
open scoped NNReal ENNReal

namespace Claim

variable {Ω : Type*} {m0 : MeasurableSpace Ω} {μ : Measure Ω} {𝒢 : Filtration ℕ m0}

/-- Wealth: `W 0 = 1`, `W (n+1) = W n * (1 + L (n+1) * D (n+1))`. -/
def wealth (L D : ℕ → Ω → ℝ) : ℕ → Ω → ℝ
  | 0 => fun _ => 1
  | n + 1 => fun ω => wealth L D n ω * (1 + L (n + 1) ω * D (n + 1) ω)

variable {L D : ℕ → Ω → ℝ}

variable {B M C : ℝ}

lemma wealth_bounds (hC : 0 ≤ C) (hfac : ∀ n ω, 0 ≤ 1 + L n ω * D n ω ∧ 1 + L n ω * D n ω ≤ C) :
    ∀ n ω, 0 ≤ wealth L D n ω ∧ wealth L D n ω ≤ C ^ n := by
  intro n
  induction n with
  | zero => intro ω; simp [wealth]
  | succ n ih =>
    intro ω
    obtain ⟨a, b⟩ := ih ω
    obtain ⟨c, d⟩ := hfac (n + 1) ω
    simp only [wealth, pow_succ]
    exact ⟨mul_nonneg a c, mul_le_mul b d c (pow_nonneg hC n)⟩

lemma wealth_measurable (hDm : ∀ n, StronglyMeasurable[𝒢 n] (D n))
    (hLm : ∀ n, StronglyMeasurable[𝒢 n] (L (n + 1))) :
    ∀ n, StronglyMeasurable[𝒢 n] (wealth L D n) := by
  intro n
  induction n with
  | zero => exact stronglyMeasurable_const
  | succ n ih =>
    have h1 : StronglyMeasurable[𝒢 (n + 1)] (wealth L D n) := ih.mono (𝒢.mono (Nat.le_succ n))
    have h2 : StronglyMeasurable[𝒢 (n + 1)] (L (n + 1)) := (hLm n).mono (𝒢.mono (Nat.le_succ n))
    exact h1.mul (stronglyMeasurable_const.add (h2.mul (hDm (n + 1))))

theorem wealth_supermartingale [IsFiniteMeasure μ] (hC : 0 ≤ C)
    (hL : ∀ n ω, 0 ≤ L n ω ∧ L n ω ≤ M) (hD : ∀ n ω, |D n ω| ≤ B)
    (hfac : ∀ n ω, 0 ≤ 1 + L n ω * D n ω ∧ 1 + L n ω * D n ω ≤ C)
    (hDm : ∀ n, StronglyMeasurable[𝒢 n] (D n)) (hLm : ∀ n, StronglyMeasurable[𝒢 n] (L (n + 1)))
    (hnull : ∀ n, μ[D (n + 1) | 𝒢 n] ≤ᵐ[μ] 0) :
    Supermartingale (wealth L D) 𝒢 μ := by
  have hWm := wealth_measurable (𝒢 := 𝒢) hDm hLm
  have hWb := wealth_bounds hC hfac
  have hint : ∀ n, Integrable (wealth L D n) μ := fun n =>
    Integrable.of_bound ((hWm n).mono (𝒢.le n)).aestronglyMeasurable (C ^ n)
      (Filter.Eventually.of_forall fun ω => by
        rw [Real.norm_eq_abs, abs_of_nonneg (hWb n ω).1]; exact (hWb n ω).2)
  have hDint : ∀ n, Integrable (D n) μ := fun n =>
    Integrable.of_bound ((hDm n).mono (𝒢.le n)).aestronglyMeasurable B
      (Filter.Eventually.of_forall fun ω => by rw [Real.norm_eq_abs]; exact hD n ω)
  refine supermartingale_nat (fun n => hWm n) hint fun n => ?_
  -- W (n+1) = W n + (W n * L (n+1)) * D (n+1)
  set c : Ω → ℝ := fun ω => wealth L D n ω * L (n + 1) ω
  have hc : StronglyMeasurable[𝒢 n] c := (hWm n).mul (hLm n)
  have hcb : ∀ ω, 0 ≤ c ω ∧ c ω ≤ C ^ n * M := fun ω => by
    obtain ⟨a, b⟩ := hWb n ω
    obtain ⟨h0, h1⟩ := hL (n + 1) ω
    exact ⟨mul_nonneg a h0, mul_le_mul b h1 h0 (pow_nonneg hC n)⟩
  have hsplit : wealth L D (n + 1) = wealth L D n + c * D (n + 1) := by
    funext ω; simp only [wealth, c, Pi.add_apply, Pi.mul_apply]; ring
  have hcD : Integrable (c * D (n + 1)) μ := by
    have := (hDint (n + 1)).bdd_mul (c := C ^ n * M) ((hc.mono (𝒢.le n)).aestronglyMeasurable)
      (Filter.Eventually.of_forall fun ω => by
        rw [Real.norm_eq_abs, abs_of_nonneg (hcb ω).1]; exact (hcb ω).2)
    exact this
  rw [hsplit]
  have hadd := condExp_add (m := 𝒢 n) (hint n) hcD
  have hW : μ[wealth L D n | 𝒢 n] = wealth L D n := condExp_of_stronglyMeasurable (𝒢.le n) (hWm n) (hint n)
  have hpull := condExp_mul_of_stronglyMeasurable_left (μ := μ) (m := 𝒢 n) hc hcD (hDint (n + 1))
  filter_upwards [hadd, hpull, hnull n] with ω h1 h2 h3
  rw [h1, hW, Pi.add_apply, h2, Pi.mul_apply]
  have : c ω * μ[D (n + 1) | 𝒢 n] ω ≤ 0 := mul_nonpos_of_nonneg_of_nonpos (hcb ω).1 h3
  linarith

/-- Propositions 3(a) and 4(a), up to any horizon: under the null, the chance that the wealth
reaches `1/α` by step `n` is at most `α`. -/
theorem wealth_level [IsProbabilityMeasure μ] (hC : 0 ≤ C)
    (hL : ∀ n ω, 0 ≤ L n ω ∧ L n ω ≤ M) (hD : ∀ n ω, |D n ω| ≤ B)
    (hfac : ∀ n ω, 0 ≤ 1 + L n ω * D n ω ∧ 1 + L n ω * D n ω ≤ C)
    (hDm : ∀ n, StronglyMeasurable[𝒢 n] (D n)) (hLm : ∀ n, StronglyMeasurable[𝒢 n] (L (n + 1)))
    (hnull : ∀ n, μ[D (n + 1) | 𝒢 n] ≤ᵐ[μ] 0) (ε : ℝ≥0) (n : ℕ) :
    ε • μ {ω | (ε : ℝ) ≤ (range (n + 1)).sup' nonempty_range_add_one
      fun k => wealth L D k ω} ≤ 1 := by
  have h := ville_finite (μ := μ) (wealth_supermartingale hC hL hD hfac hDm hLm hnull)
    (fun n ω => (wealth_bounds hC hfac n ω).1) ε n
  simpa [wealth] using h

/-- The value test's factors: `|D| ≤ 1` and `0 ≤ L ≤ 1` give `1 + L * D ∈ [0, 2]`. -/
lemma value_factor {l d : ℝ} (hl : 0 ≤ l ∧ l ≤ 1) (hd : |d| ≤ 1) : 0 ≤ 1 + l * d ∧ 1 + l * d ≤ 2 := by
  have := abs_le.mp hd
  constructor <;> nlinarith [this.1, this.2, hl.1, hl.2]

/-- The liveness test's factors: with `p₀ ∈ (0,1)`, `Y ∈ [0,1]` and `0 ≤ L ≤ 1/p₀`,
`1 + L * (Y - p₀) ∈ [0, 1/p₀]`. -/
lemma liveness_factor {l y p₀ : ℝ} (hp : 0 < p₀ ∧ p₀ < 1) (hy : 0 ≤ y ∧ y ≤ 1)
    (hl : 0 ≤ l ∧ l ≤ 1 / p₀) : 0 ≤ 1 + l * (y - p₀) ∧ 1 + l * (y - p₀) ≤ 1 / p₀ := by
  have hlp : l * p₀ ≤ 1 := by
    have := mul_le_mul_of_nonneg_right hl.2 hp.1.le
    rwa [one_div, inv_mul_cancel₀ hp.1.ne'] at this
  constructor
  · nlinarith [hy.1, hl.1]
  · have h1 : l * (y - p₀) ≤ l * (1 - p₀) := mul_le_mul_of_nonneg_left (by linarith) hl.1
    have h2 : 1 + l * (1 - p₀) ≤ 1 / p₀ := by
      rw [le_div_iff₀ hp.1]; nlinarith [hlp, hl.1, hp.2]
    linarith

end Claim
