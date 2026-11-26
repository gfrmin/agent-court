/-
Proposition 3(b): the Bayes mixture's regret, for the quantity the value test uses.

`P k m > 0` is member `k`'s joint probability of block `m`'s realised outcomes
(the product of its clipped per-event probabilities). With a uniform prior, the
posterior weight of `k` before block `m` is proportional to `∏_{j<m} P k j`, and the
mixture's joint probability of block `m` is `Q m = ∑_k w k m * P k m`.
Then `∏_{m<T} Q m = (1/K) ∑_k ∏_{m<T} P k m`, so the mixture's cumulative log loss is
within `log K` of every member's; if the base rate is a member, within `log K` of it.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Fin

open Finset Real

namespace Claim

variable {K : ℕ} (P : Fin K → ℕ → ℝ)

/-- Unnormalised posterior mass after `T` blocks. -/
noncomputable def S (T : ℕ) : ℝ := ∑ k, ∏ m ∈ range T, P k m

/-- The mixture's joint probability of block `T`'s outcomes, with Bayes weights. -/
noncomputable def Q (T : ℕ) : ℝ := (∑ k, (∏ m ∈ range T, P k m) * P k T) / S P T

lemma S_pos (hK : 0 < K) (hP : ∀ k m, 0 < P k m) (T : ℕ) : 0 < S P T := by
  unfold S
  have : Nonempty (Fin K) := ⟨⟨0, hK⟩⟩
  exact Finset.sum_pos (fun k _ => Finset.prod_pos (fun m _ => hP k m)) Finset.univ_nonempty

lemma Q_eq (T : ℕ) : Q P T = S P (T + 1) / S P T := by
  unfold Q S
  congr 1
  refine Finset.sum_congr rfl (fun k _ => ?_)
  rw [Finset.prod_range_succ]

/-- The telescoping identity. -/
theorem prod_Q (hK : 0 < K) (hP : ∀ k m, 0 < P k m) (T : ℕ) :
    ∏ m ∈ range T, Q P m = S P T / K := by
  induction T with
  | zero =>
    have hK' : (K : ℝ) ≠ 0 := by exact_mod_cast hK.ne'
    simp [S, hK']
  | succ T ih =>
    rw [Finset.prod_range_succ, ih, Q_eq]
    have h1 := S_pos P hK hP T
    have hK' : (0 : ℝ) < K := by exact_mod_cast hK
    field_simp

/-- Regret against each member: `∑ log Q ≥ ∑ log P_k - log K`. -/
theorem regret (hK : 0 < K) (hP : ∀ k m, 0 < P k m) (T : ℕ) (k : Fin K) :
    ∑ m ∈ range T, Real.log (P k m) - Real.log K ≤ ∑ m ∈ range T, Real.log (Q P m) := by
  have hK' : (0 : ℝ) < K := by exact_mod_cast hK
  have hQ : ∀ m, 0 < Q P m := fun m => by
    rw [Q_eq]; exact div_pos (S_pos P hK hP _) (S_pos P hK hP _)
  rw [← Real.log_prod (fun m _ => (hQ m).ne'), ← Real.log_prod (fun m _ => (hP k m).ne'),
    prod_Q P hK hP T, ← Real.log_div (Finset.prod_pos (fun m _ => hP k m)).ne' hK'.ne']
  apply Real.log_le_log (div_pos (Finset.prod_pos (fun m _ => hP k m)) hK')
  apply div_le_div_of_nonneg_right _ hK'.le
  unfold S
  exact Finset.single_le_sum (f := fun k => ∏ m ∈ range T, P k m)
    (fun j _ => (Finset.prod_pos (fun m _ => hP j m)).le) (Finset.mem_univ k)

/-- Against the base rate, when the base rate is a member (`P k₀ = B`):
the aggregate's cumulative log-likelihood ratio over the base is at least `-log K`. -/
theorem regret_base (hK : 0 < K) (hP : ∀ k m, 0 < P k m) (T : ℕ) (B : ℕ → ℝ) (k₀ : Fin K)
    (hbase : ∀ m, P k₀ m = B m) :
    -Real.log K ≤ ∑ m ∈ range T, (Real.log (Q P m) - Real.log (B m)) := by
  have h := regret P hK hP T k₀
  simp only [hbase] at h
  rw [Finset.sum_sub_distrib]
  linarith

end Claim
