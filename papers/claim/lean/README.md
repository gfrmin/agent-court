# Machine-checked core of "Law Before the Agent"

Lean 4 (`leanprover/lean4:v4.37.0-rc1`) with Mathlib at tag `v4.37.0-rc1`. To check:

    lake exe cache get   # Mathlib's prebuilt files, a few GB
    lake build

Every theorem depends only on Lean's standard axioms (`propext`, `Classical.choice`, `Quot.sound`). There is no `sorry`.

| Paper | Lean | File |
|---|---|---|
| Prop. 1(b): two different linked logs, each numbered by position from 0, ending in lines with the same hash, give a collision | `Claim.collision_of_ne` | `HashChain.lean` |
| Prop. 2(a): the log score is strictly proper on (0,1) | `Claim.log_score_proper`, `Claim.log_score_strict` | `Propriety.lean` |
| Prop. 3(b): the mixture of product forecasts telescopes; its regret is within `log K` of every member, including the base rate | `Claim.prod_Q`, `Claim.regret`, `Claim.regret_base` | `Mixture.lean` |
| Ville's inequality, finite horizon, for a non-negative supermartingale (derived from Mathlib's optional stopping) | `Claim.ville_finite` | `Ville.lean` |
| Props. 3(a) and 4(a): the wealth is a non-negative supermartingale under the null, and reaches `1/α` by any horizon with probability at most `α` | `Claim.wealth_supermartingale`, `Claim.wealth_level` | `Wealth.lean` |
| The value and liveness factors meet `wealth_level`'s hypotheses | `Claim.value_factor`, `Claim.liveness_factor` | `Wealth.lean` |
| Prop. 4(b): the cost of restarting each window. `restart_union` is a measure bound. `restart_independent` proves only the inequality $1-\prod_j(1-r_j) \le 1-(1-\alpha)^k$; that independent events have that union probability is not formalised | `Claim.restart_independent`, `Claim.restart_union` | `Restart.lean` |
| Prop. 5: the conjunctive rule (intersection–union). It takes each component's crossing bound as a hypothesis | `Claim.conjunctive_promotion` | `Conjunctive.lean` |

**Not formalised:**
- the bridges from the paper's definitions to these statements: the product construction, the clipping and the stake rules;
- the grid clause of 2(a);
- that the stake rules keep `0 ≤ λ < 1` and `λ < 1/p₀`, which are simple bounds;
- the unbounded horizon, which follows from the finite one by continuity of measure;
- Props. 1(a), 2(b) and 6, which hold by construction of the code.
