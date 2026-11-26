# Cold read 5 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1368, filed under Guy's standing yes. The session ran from 03:50Z to 03:55Z on 26 November.
- **Text read:** draft 10, at `ea71d37`.
- **Verdict:** minor revision.
- **Draft 11** answers it. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What draft 11 does |
|---|---|
| Rice, Löb and Goodhart as necessities (abstract, §2, Table 1, conclusion) | §3 is now "What the results motivate", and the Table 1 columns are "Motivates" and "Response". Rows are called design arguments, some of them analogies. The abstract says "limit what … can establish". The conclusion says "we have argued". |
| Proper scores are not unique | "Under expected-score incentives, a proper score can be held fixed …" |
| Skalse's scope; Bahadur–Savage tails | Both qualified in Table 1. |
| Conant–Ashby, the regress, Wheeler, option value | The regress is stopped "by engineering choice". The Wheeler row says diversity of authors, not diverse double-compiling. "Only the irreversible" becomes "Irreversible acts merit a hard gate". |
| Evidence is attested, not recomputed | Stated in the threat model [SPEC §10, item 15]. |
| "Judged once" | Now "assessed with one historical evaluator"; the current judge drives it. |
| Typing and taint exceptions | The `window_fixes` exceptions are stated. |
| The nine repairs are classifier rows | Now "nine rows that its classifier labels as repairs under the operator's login; one suffices". |
| Authority earned by record | Qualified: some powers came before any statistical promotion (C0; seq 51). The builders' record is "the nearest record that does". |
| $R_m$ throughout; empty blocks; the cutoff-time null | Stated. |
| The information sets in the recomputation; the gap wording | The exact eligible sets are given. "Compounding, not leakage, accounts for most of the gap, though the ablations do not use exactly the same events." |
| Scrivens overstated | Restricted to power-law risk schedules and overlap conditions [Thm. 1], in §4.3 and §7. |
| The ratio's window | It counts to seq 7809, past the veto at seq 7180. Stated. |
| Murphy; recency | Murphy is for the Brier score, and a log-score gate is open. A split-α process keeps validity and trades power. |
| The roster mode in the script | Its docstring now says it is not a true null for the joint score. |

## The report (verbatim)

## 1. The one idea

The governing institution for a self-modifying agent should be built and tested before receiving authority, with its builders subject to its rules and promotion conditional on sequential evidence from its own record. That record must also expose failures of the institution’s tests, including dependence-sensitive betting and misleading baselines.

The abstract states this message, and the body delivers a coherent design, conditional guarantees and a reproducible retrospective audit. The seven-regress taxonomy, several rows of Table 1 and repeated architectural-necessity claims contribute less than the concrete construction and audit.

## 2. Correctness

Line numbers below refer to `draft.md` at the supplied commit.

**Proposition 1.** Both parts are correct for a fixed prefix-local validity predicate. Position-numbering excludes the suffix counterexample to earlier versions of part (b); equal terminal hashes of different-length numbered logs already give a collision between their terminal lines. This establishes commitment to a linked history relative to a retained head, not completeness or independent witnessing.

**Proposition 2.** Correct. The derivative and strict-concavity argument establish the continuous optimum; monotonicity on either side gives the grid statement, including endpoints and ties. Part (b) matches the principal-string comparison in `kernel/check.py:82–83`. The qualifications concerning nonlinear rewards, collusion and identity assignment are appropriate.

**Proposition 3.** Correct for complete blocks. Clipping puts both joint likelihoods between \(0.001^{|B_m|}\) and \(0.999^{|B_m|}\), establishing the stated bound on \(\bar D_m\). Predictability and the conditional-mean null establish the supermartingale; Bayesian telescoping establishes both regret inequalities.

The partial-resolution extension needs one explicit convention: replace \(B_m\) by \(R_m\) **throughout**, including posterior updates and the size multiplier in part (b), and take a unit factor when \(R_m=\varnothing\). Line 180 explicitly mentions replacing the sets in \(Q_m\) and \(\bar D_m\), but leaves the displayed posterior and regret formulas requiring interpretation.

**Remark.** Substantively correct. Dependence alone is not the problem; the null, filtration and update rule must match. Frozen correlated factors need not have expected product at most one. Conditional independence plus eventwise nulls supports eventwise betting. Joint-mixture scoring can reward dependence modelling without marginal improvement; products of mixture marginals lack the stated regret guarantee.

**Example.** Correct as an isolated counterexample to eventwise betting, rather than an instance of the baseline-containing mixture construction. I reproduced:

| Configuration | Per-event crossings | Block crossings |
|---|---:|---:|
| Default: 20 events, 4,000 runs | 0.1325 | 0 |
| 50 events, 2,000 runs | 0.5035 | 0 |
| Default, independent outcomes | 0 | Not computed |

The conditional drift is approximately \(-0.1202\).

The requested `--roster 20 300 2000` run produces **0.2850 versus 0**. This remains **not a true-null experiment for the joint-score test**: initially its normalized expected joint advantage is approximately \(+0.08498\). Its removal from the manuscript as a false-positive example was correct; the ancillary script’s introductory “under a true null” framing should explicitly exclude this mode.

**Proposition 4.** Correct under its stipulated item-level—or explicitly substituted block-mean—null. The stake is nonnegative and below \(1/p_0\); factors are positive and have conditional expectation at most one. Continuing the same process preserves the bound across administrative windows. Both restarting bounds are correct, including the exact-test qualification. The implementation’s asymmetric success/failure units remain an unresolved endpoint-design issue, now disclosed.

**Proposition 5.** Correct intersection–union argument, without independence. The per-layer limitation is correctly stated.

**Proposition 6.** Part (a) follows from its admission condition; part (c) correctly limits extrapolation. Part (b) should say **“assessed using one historical evaluator version”**, not “judged once”: `promotion_checks` re-executes historical assessments on subsequent judge runs.

## 3. The Lean files

I read the README and all seven files. I did not build them or independently verify the reported axiom audit; their source contains no `sorry`.

- **`HashChain`: `collision_of_ne`.** Matches numbered, linked, nonempty logs represented backwards. Hashes and entries are abstract; serialization, SHA-256 security and an efficient adversarial reduction are outside the statement.
- **`Propriety`: `log_score_proper`, `log_score_strict`.** Establish expected-score optimality and strictness on \((0,1)\), not strict concavity or the grid result. The manuscript now discloses this accurately.
- **`Mixture`: `prod_Q`, `regret`, `regret_base`.** Correctly establish telescoping and regret for arbitrary positive block likelihoods and an actual baseline member. Positivity is weaker than requiring normalized, clipped product probabilities, making the algebra more general. Identification with the paper’s event products, normalized statistic and finite maximum remains informal.
- **`Ville`: `ville_finite`.** Establishes the advertised finite-horizon maximal inequality for a nonnegative supermartingale under a finite measure, using optional stopping.
- **`Wealth`: `wealth_supermartingale`, `wealth_level`.** Establish the generic betting result with explicit measurability, deterministic boundedness and conditional-mean assumptions. These are sufficient hypotheses for the intended bounded construction. `wealth_level` gives threshold times crossing probability at most one; substituting \(1/\alpha\) gives the claimed level.
- **`value_factor`, `liveness_factor`.** Prove scalar bounds allowing endpoint stakes and zero factors. This is weaker than strict positivity but sufficient for validity. They do not verify the actual stake formulas, clipping bridge or empirical filtration.
- **`Restart`: `restart_independent`, `restart_union`.** The former is algebra only: it contains neither independent events nor their union-probability identity. The latter is a genuine measure-theoretic union bound. The README is explicit; line 118’s “inequality, not … attain” description could additionally mention the missing independent-event bridge.
- **`Conjunctive`: `conjunctive_promotion`.** Correctly proves containment plus either crossing bound implies the promotion bound. It assumes those bounds rather than composing the wealth theorems. This limitation is disclosed.

Overall, this is a useful formalized mathematical core, not verification of the reference implementation.

## 4. The recomputation

The numerical results reproduce:

- **2,820** implementation-selected resolved events; implementation wealth \(1.51983\times10^{60}\).
- **476 completed sittings**, four pending; 2,803 member events in completed sittings.
- **170 expiries**, including 168 resolutions arriving after deadline.
- Five classes, with completed-sitting counts **215, 195, 47, 15, 4**.
- Pooled-baseline final wealth: **19,930; 11,090; 3.009; 1.159; 1.022**, approximately.
- Class-two maximum: approximately **11,900**.
- Thresholds: **40, 120, 240, 400, 600**.
- Dataset-baseline maxima: **1 in every class**.
- Ablations: **\(2.492\times10^{58}\)** and **\(1.739\times10^{10}\)**.

The fourth referee’s two adaptation bugs are fixed: late arrivals cannot change expired outcomes, and pending sittings participate in class allocation. At three intermediate observation times, including the earlier counterexample times, I found no changes to already-completed sittings or their class assignments when compared with the terminal run.

The method supports the stipulated **resolved-subset, cutoff-information null**, conditional on the protocol being fixed. Predictable cross-class and partial-sitting weight updates preserve the betting argument but lose the telescoping regret guarantee, as disclosed.

Two qualifications remain:

1. This is retrospective protocol development, not a demonstrated level-0.05 discovery procedure accounting for all analyses considered.
2. “Time of forecasting” must mean **aggregate cutoff**, not original issuance: the template issues forecasts for several future cutoffs together, while aggregation uses information arriving subsequently.

The recomputation is in **§6**, despite the review request’s §7 locator.

## 5. The revisions

Against the fourth report’s disposition:

1. **Deadline and pending-class bugs:** resolved; updated figures reproduce.
2. **Liveness units:** accurately disclosed, but a symmetric operational batch endpoint remains unspecified. “Incumbent’s series” is correct. The historical \(6/11\) provenance is actually available in Freeman, §6.2.
3. **Lean scope:** substantially resolved; add the independent-event bridge qualification noted above.
4. **Resolved subsets/global regret:** substantially resolved; make the all-formulas substitution and empty-subset convention explicit.
5. **Implementation facts:** key powers, kernel state, installation boundary and brief path are corrected. “Judged once” remains inaccurate.
6. **Builder activity:** routine-stream dominance is now clear; approximate proposal classifications need a reproducible counting rule.
7. **Procedure/object count:** improved, but still labels a post-veto continuation as the window’s count.
8. **Presentation:** abstract wording, source classification and final-versus-peak distinction are corrected. Retaining Table 1 is defensible, but its unsupported implications need narrowing.

## 6. Backing

### Independent source checks

These checks use implementation objects at `e580b64`, Freeman at `007a007`, and the named external versions. “Supported” means source support, not independent certification that every historical experiment occurred.

| Paper line(s) | Claim checked | Source and result |
|---|---|---|
| 21 | DGM improves 20%→50% | Zhang 2025 v3 abstract: supported. |
| 21 | DGM removes detector markers | Same, Appendix H narrative and patch: supported. |
| 21 | Census includes 114 studies; process evidence weaker | Chen–Zhu–Zheng v1: supported. |
| 126 | Seven fields, canonical encoding, signatures | `SPEC` §§1–6: supported. |
| 136 | Fourteen refusal reasons | `SPEC:295–297`: supported. |
| 150 | Activation exceeds amendment position | `kernel/check.py:71–72`: supported. |
| 152 | Builder powers at seqs 6 and 34 | Both entries: supported. |
| 152 | Herald-2 holds merge alone | Seq 201: supported. |
| 152 | Operator powers added at seq 1 | Seqs 0–1: supported. |
| 152 | Last key authority cannot be lost | `check.py:84–87`: supported. |
| 162 | Principal-based self-resolution refusal | `check.py:81–83`: supported. |
| 172 | Counsel 100 forecasts; operator three | Independent log count: supported. |
| 213 | Stakes and weights update per resolution | `judge/value.py:113–135`: supported. |
| 213 | Baseline includes preceding same-type resolutions | `judge/entries.py:resolution_rates`: supported. |
| 213 | Fourteen resolutions within one minute | Seqs 550–563: supported. |
| 247 | Three replay rows checked | `promotion_replay_spot.py`, indices 592/593/705: supported. |
| 262 | RQGM selectively discards evaluator-dependent utilities | Iacob v3: supported. |
| 302 | 6,621 builder/reviewer entries; 5,919 forecasts/resolutions | Independent log count: supported. |
| 302 | SEA recommends gate first | Sengupta v1 §4.4: supported; conjectural scope also supported. |
| 316 | Kernel totals 450 lines | Git-object counts \(138+172+140\): supported. |
| 316 | 100,000 logs, 658,885 prefixes | `REPORT:223` reports exactly these figures. |
| 324 | Nine-item C1b wealth and \(p_0\) | `REPORT:420` and §2 table: supported. |
| 380–382 | Fixed-table crossing; nine of 28 criteria | Named audit: supported as reported retrospective constructions. |
| 392 | No `rule` entry | Independent complete-log type count: supported. |

### Statements whose backing or scope remains inadequate

1. **Lines 15, 25, 52, 76–77, 404 — architectural necessity.** Rice does not require judging arbitrary changes *only by running*; Löb does not generally prohibit trusting a same-theory successor. It obstructs particular uniform reflection/proof strategies under particular formal assumptions. Neither result derives an external-key institution or its construction order. Replace these implications with scoped motivations.

2. **Lines 53, 79–80 — uniqueness and protection of proper scores.** Propriety is relevant to eliciting probabilities under expected-score incentives. It does not establish that proper scoring is the only trustworthy measurement mechanism or necessary for every useful target. The manuscript’s nonlinear-reward qualification itself prevents the broader inference.

3. **Line 80 — Skalse’s scope.** The cited paper distinguishes unrestricted stochastic policies from deterministic or finite policy sets, for which nontrivial unhackable pairs can exist. “No non-trivial proxy is unhackable” omits essential policy-space and equivalence qualifications.

4. **Line 82 — unbounded means.** Bahadur–Savage concerns sufficiently unrestricted distribution classes, not every unbounded variable. Known tail or parametric assumptions permit inference about unbounded means. State “without distributional/tail restrictions.”

5. **Lines 84, 102 — control and regress.** A state fold is not thereby a demonstrated model satisfying Conant–Ashby’s regulatory conditions; multiple model families do not establish requisite variety. Nor does readability plus agreement terminate correctness justification. These are engineering choices, not discharged necessities.

6. **Lines 89–91 — security/economic implications.** Diverse implementations do not implement Wheeler’s diverse double-compiling assurance. Option-value results do not establish that *only* irreversible actions merit hard gates; that conclusion needs utilities, information and waiting costs. Label these analogies/design commitments.

7. **Line 57 — distrust of unrecomputable evidence strings.** `SPEC:467–469` explicitly says promotion evidence is checked for presence and hash, **not truth**, with the operator attesting its contents. `evidence_ok` likewise establishes byte integrity, not correctness of an outcome interpretation. Distinguish recomputation from trusted acquisition and attestation.

8. **Lines 118, 253, 259 — “judged once.”** `promotion_checks` replays historical promotions on every relevant run. What is fixed is the selected historical evaluator, not the number of executions. The driver also comes from the current judge; the trust boundary should say so.

9. **Lines 229, 362 — Scrivens is materially overstated.** I checked **arXiv:2603.28650v2, Theorem 1 and §3.1**. Its finite-total-TPR result assumes a power-law risk schedule and distribution-overlap/Rényi conditions. It explicitly excludes a blanket summability inference for slowly decaying summable schedules such as \(1/(n\log^2 n)\). “Gates with summable risk schedules admit only a finite total true-positive rate” is not supported.

10. **Lines 270–271 — immutable typing and universal taint.** The implementation has `window_fixes`, evidentiary attribution and special handling that removes qualifying fix taints at a later push (`status.py:120–123,371–402`). State these exceptions. Fixed code does not establish that arbitrary acts cannot be represented using a different type.

11. **Lines 273, 325, 330 — nine operator repairs.** The record supports **nine classifier-labelled repair rows under the operator’s login**. Freeman §6.4 explicitly identifies shared-login attribution problems and establishes only one as the operator’s own hand. Calling all nine actual human repairs overstates measurement, although one suffices for the recorded failure.

12. **Lines 297, 306–310 — record-earned authority.** Proposition 4 requires a precommitted \(p_0\), not that the builders’ record is its only possible source. Seq 51 grants merger authority before C1b’s statistical promotion; C0 predates statistical windows. Qualify “a power exists only because it was earned … by scored record.”

13. **Lines 336, 346 — audit information and ablation.** Mixture updates actually exclude late-resolved events (`done_events`), whereas baseline estimation includes resolutions more broadly. Replace “all outcomes” with the exact eligible set. Moreover, the implementation and deadline-filtered ablation use different event sets; compounding clearly dominates the gap, but “the gap comes from” is not a perfectly controlled single-factor decomposition.

14. **Line 348 — window extent.** The 459:1,786 count extends through seq 7809, although A6 ended C2a′ at seq 7180. This is the old evaluator’s continuation, not the legally ended window. Give both intervals or label the obsolete projection.

15. **Lines 380, 384 — remedies.** Murphy’s Brier-score decomposition does not itself define a valid log-score promotion gate preventing “calibration without resolution.” A fresh split-\(\alpha\) process also need not “trade validity” for recency: it trades allocation/power while preserving validity. Specify the proposed method.

The novelty statements at lines 35–38, 275 and 302 remain plausible, explicitly qualified priority claims, rather than established exhaustive literature results.

## 7. Overclaiming and clarity

The strongest supported contribution is an auditable institutional protocol plus a revealing negative-baseline audit. It does not establish superior governance, adversarial robustness or reduced meaningful oversight burden; the manuscript generally acknowledges this well.

Cut or compress the regress catalogue, the unbuilt Waismann row and repeated universal “must” formulations. Retain the distinction between mathematical validity, implementation conformity, measurement truth and substantive utility.

## 8. Recommendation

**Minor revision.** The mathematical core is sound, the principal recomputation defects are repaired, and the empirical conclusion reproduces. Remaining changes principally concern precise claims and provenance.

The five priorities are:

1. Correct the Scrivens attribution and scope the Rice/Löb/Goodhart, control and option-value implications.
2. State the evidence-attestation boundary and describe the nine repairs as classified rows.
3. Correct “judged once,” fix-taint exceptions, and authority-earned-by-score universals.
4. Make resolved-subset updates, empty blocks and cutoff-time conditioning explicit; qualify the roster simulation.
5. Correct the post-veto counting interval and audit eligibility description; distinguish retrospective evidence from prospective error control.

RECOMMENDATION: minor revision
