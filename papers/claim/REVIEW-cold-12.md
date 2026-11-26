# Cold read 12 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1387. The session ran from 10:40Z to 10:47Z on 26 November.
- **Text read:** draft 22, at `15087a5`.
- **Verdict:** minor revision. The reader found the eleventh referee's points resolved, and reproduced every figure, including the four window ratios, by its own count of the entries. Its main point is a real error: the claim that no row had been re-attributed.
- **Draft 23** corrects it. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What draft 23 does |
|---|---|
| "No row has been re-attributed" is wrong | Corrected from the CSVs. Under BRIEF-C1b's Amendment 2, attribution by declaration cut the repair rows from 7 to 1 (1 November) and from 81 to 9 (3 November). The falsifier, which concerns re-typing as decisions, is not met as worded, but this is now named as the nearest case. The nine remaining rows were not re-attributed. |
| A rule fixed before any window, against code that came later | Now: the charter fixed the rule before any window; the code entered on 31 October, during C1b's window, and its predicate line has not changed since (`git log -G`). The reader placed the code before C1b's opening, but the REPORT gives the opening as seq 188, which precedes the commit. |
| The 14-day scan's observation boundary | Stated: complete intervals, each ending by the record's last entry. |
| When an amendment's two effects begin | Now "two things change at a itself". |
| "Trusted rather than tested" | The abstract and §5.2 now say "held fixed and trusted as infrastructure". DGM's Appendix H itself exposed a detector failure by experiment. |
| Compress Table 1 and replay detail | Kept, as before. |

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

An institution governing a self-modifying agent should be built first, bind its builders first, and earn authority through valid sequential tests on its own record. That record should expose failures of the institution’s tests—including dependence-sensitive betting and weak baselines—rather than merely certify success.

The abstract states this message, and the body delivers a conditional design and reproducible retrospective audit. It also clearly acknowledges that the reference implementation has not implemented evidence-earned capability grants. Table 1’s genealogy, repeated build-order explanations, and some replay mechanics contribute less directly than §§4–6.

## 2. Correctness

**The six propositions are sound under their stated hypotheses. They do not certify the implementation as a whole.**

1. **Proposition 1:** Prefix-local evaluation proves (a). Position-numbering and predecessor links make the collision extraction in (b) correct. Different-length logs already have distinct terminal sequence numbers, so their equal terminal hashes immediately yield a collision. The guarantee concerns commitment relative to a retained head, not completeness or preservation under arbitrary interpreter replacement.

2. **Proposition 2:** Correct:
   \[
   g'(p)=\frac{\pi-p}{p(1-p)},\qquad
   g''(p)=-\frac{\pi}{p^2}-\frac{1-\pi}{(1-p)^2}<0.
   \]
   Monotonicity around \(\pi\) supplies the grid result, including boundaries and ties. Part (b) matches the registered-principal comparison in the kernel. The identity-assignment, collusion, performativity and nonlinear-reward qualifications are necessary and present.

3. **Proposition 3:** For \(r=|R_m|>0\), clipping puts both joint likelihoods between \(0.001^r\) and \(0.999^r\), establishing \(|\bar D_m|\le1\). Predictable nonnegative stakes below one give positive factors with conditional expectation at most one under the displayed null. The sufficient condition correctly conditions on the resolved subset, fixing the random denominator.

   Bayesian telescoping proves (b) when posterior updates use exactly the scored resolved blocks; including the baseline supplies the second inequality. The paper correctly distinguishes size-weighted log-score regret from unweighted betting wealth.

4. **Proposition 4:** Since \(0<\hat q_j<1\), \(0\le\lambda_j<1/p_0\). Factors are positive and their conditional expectations are at most one under the null. Continuing the unchanged process therefore gives lifetime control. Both restarting bounds and the exact-test qualification are correct. The simultaneous-item endpoint remains operationally unfinished, as disclosed.

5. **Proposition 5:** Correct intersection–union argument; independence is unnecessary. The per-layer limitation is explicit.

6. **Proposition 6:** Correct conditional finite-input agreement and historical evaluator dispatch. Part (a) essentially restates the admission condition; part (c) correctly denies extrapolation. The substantial gap between full specified replay and automated enforcement is disclosed.

**Remark:** Correct. Simultaneity itself is harmless; the issue is conditioning subsequent bets on information excluded from the null. Frozen correlated factors also need not have expected product at most one. Conditional independence plus eventwise nulls supports eventwise betting. The distinction between joint dependence modelling and marginal forecasting improvement is particularly important.

**Example and simulations:** I reproduced:

| Configuration | Per-event crossing | Block crossing |
|---|---:|---:|
| Default: 20 events, 4,000 runs | 0.1325 | 0 |
| 50 events, 2,000 runs | 0.5035 | 0 |
| Independent outcomes, default | 0 | Not computed |
| Roster mode, 2,000 runs | 0.2850 | 0 |

The isolated example’s drift is \(-0.1202\). Roster mode is correctly excluded as a true-null demonstration: its mixture can model the shared outcome, giving positive initial joint-score advantage despite no marginal skill.

## 3. The Lean files

I read the README and all seven files. I did not build them or independently verify the reported axiom audit. The supplied source contains no `sorry`.

- **`HashChain.lean`: `collision_of_ne` → Proposition 1(b).** Matches nonempty, linked, position-numbered logs represented backwards. Genesis’s zero parent is unnecessary to the lemma. Entries and hashes are abstract; JSON, SHA-256 security and efficient cryptographic reduction remain informal. The existential conclusion does not explicitly locate the collision witnesses in the logs.

- **`Propriety.lean`: `log_score_proper`, `log_score_strict` → Proposition 2(a).** Proves optimality and strictness for belief and report in \((0,1)\), not strict concavity or the grid clause. The manuscript accurately discloses these narrower statements.

- **`Mixture.lean`: `prod_Q`, `regret`, `regret_base` → Proposition 3(b).** Proves telescoping, per-member regret and baseline regret for positive block likelihoods with \(K>0\). Positivity is weaker than normalized clipped probability assumptions, making the algebra more general. Event products, resolved subsets, normalization and the finite maximum remain informal bridges.

- **`Ville.lean`: `ville_finite`.** Proves the finite-horizon maximal inequality for a pointwise nonnegative supermartingale under a finite measure, using optional stopping. Infinite-horizon passage is informal.

- **`Wealth.lean`: `wealth_supermartingale`, `wealth_level` → Propositions 3(a), 4(a).** Proves generic recursive betting under explicit adaptedness, predictability, deterministic boundedness and conditional-mean hypotheses. Substituting threshold \(1/\alpha\) yields the advertised level. `value_factor` and `liveness_factor` allow endpoint stakes and zero factors, establishing less than strict positivity but enough for validity. They do not verify the concrete stake formulas or empirical filtration.

- **`Restart.lean`: `restart_independent`, `restart_union` → Proposition 4(b).** The former proves real-number algebra without independent events or their union-probability identity; it even permits negative \(r_j\). The latter is a genuine measure bound. The scope descriptions are accurate.

- **`Conjunctive.lean`: `conjunctive_promotion` → Proposition 5.** Proves containment plus either component crossing bound implies the promotion bound. It assumes the component bounds rather than instantiating the wealth results.

These files substantiate a useful generic mathematical core, not verification of the implementation or measurement pipeline.

## 4. The recomputation

**The reported numbers reproduce.**

| Quantity | Reproduced result |
|---|---|
| Implementation-selected events | 2,820 |
| Implementation wealth | \(1.51983\times10^{60}\) |
| Completed / pending sittings | 476 / 4 |
| Member events in completed sittings | 2,803 |
| Expiries, including late resolutions | 170, including 168 |
| Resolved events lacking pre-cutoff forecasts | 19 |
| Completed sittings by class | 215, 195, 47, 15, 4 |
| Pooled-baseline final wealth | 19,930; 11,090; 3.009; 1.159; 1.022 |
| Class-two maximum | Approximately 11,900 |
| Thresholds | 40, 120, 240, 400, 600 |
| Per-dataset running maxima | 1 in every class |
| Successive ablations | \(2.492\times10^{58}\), \(1.739\times10^{10}\) |

The method supports Proposition 3(a)’s betting argument under the stipulated **normalized resolved-subset null and recorded-time interpretation**:

- Membership and deadlines derive from pre-cutoff forecasts.
- Late resolutions cannot revise expiries.
- Pending sittings participate in class allocation.
- Although retrospectively coded using completion times, assignment asks only whether an earlier sitting had completed before the new cutoff—information observable then.
- Stakes use earlier completed sittings in their class.
- Weights and baselines use pre-cutoff information.
- Deterministic summable thresholds handle adaptively created classes.

Cross-class and partial-sitting weight updates preserve predictability but forgo Proposition 3(b), as disclosed. The 1.8, 48.2 and 5.9 orders-of-magnitude differences reproduce and are correctly described as successive ablation differences.

This is retrospective protocol development, not a selection-adjusted 5% discovery claim covering all protocols considered during revision.

## 5. The revisions

The eleventh referee’s points are substantially resolved:

1. **Fixed prompt:** Resolved. The text now reports five revisions after initial recording; the six relevant commits support this.
2. **Stream entries and proposals:** Resolved. The 5,811/5,919 distinction and 627/702 title classification reproduce.
3. **Fourteenth-day statement and opening sequence:** Substantively resolved. The breach episode, genesis maximum and seq 31 boundary reproduce for complete half-open intervals. State the observation-boundary convention explicitly.
4. **Unnoticed kernel-family lapse:** Appropriately restricted to the record. I found no ruling addressing the particular C1 authorship lapse.
5. **Proposed versus actual powers:** Resolved prominently in the introduction and conclusion as well as §5.1.
6. **Ablation causality:** Resolved.
7. **Compression:** Optional presentation advice remains partly unadopted; this is not a correctness defect.

The acts-table attribution issue below was not resolved by those changes.

## 6. Backing

Line numbers refer to the supplied `draft.md`. Repository checks use `e580b64`, except the explicitly named historical commits. Source support is distinguished from independently rerunning historical experiments.

### Direct checks

| Lines | Claim checked against its source |
|---|---|
| 20 | **DGM 20%→50%:** supported by the cited paper’s abstract/results. |
| 20 | **Detector-marker removal despite instructions:** supported explicitly by DGM Appendix H, node 114. |
| 20 | **Hyperagents boundary and parent-selection exception:** supported by v2’s source, including the quoted safety rationale and future boundary expansion. |
| 20 | **114 studies, 90 self-described RSI, 22% audited reruns:** supported by arXiv:2610.27610. |
| 55 | **Wrong resolution stands:** `REPORT`, C1a §4, explicitly documents forecast 123’s incorrect resolution. |
| 99–109 | **Seven fields, state and refusal structure:** supported by `SPEC` and `kernel/check.py`. |
| 123 | **Activation above amendment position:** enforced by `kernel/check.py`. |
| 125 | **Builder, herald and operator powers:** supported by the named entries; the last-key guard is present. |
| 135 | **Principal-based self-resolution refusal:** directly present in `kernel/check.py`. |
| 145 | **Prompt history:** initial commit plus five subsequent changes reproduce. |
| 186 | **Per-resolution stake, weight and baseline updates:** directly present in `judge/value.py` and `judge/entries.py`. |
| 202, 333 | **Scrivens’ qualified finite-total-TPR result:** supported by v2’s power-law and overlap conditions. |
| 214–220 | **Installation boundary and evidence attestation:** supported by `SPEC` and `installing_push`; the latter does not implement full-table replay. |
| 220 | **Replay indices 300/400/593 and CI invocation:** supported by `pins/replay.py` and the workflow. |
| 235 | **RQGM selective erasure:** supported by v3’s description of discarding evaluator-dependent utility records. |
| 237 | **Kernel authorship:** trailers and historical NOTES support the stated family history. The Google C1 revision adds the last-key guard rather than replacing the OpenAI entry-type implementation. `REPORT` supplies C1a’s Claude attribution. |
| 243–244 | **Repair exclusions, taint and pending clearing:** supported by `item_process`, with the attribution qualification below. |
| 264 | **19 key entries, 14 before first promotion:** reproduced; all are signed by the operator. RUNBOOK supports opening-time grants. |
| 272 | **\(6/11\) versus \(5/11\):** explicitly distinguished in the brief’s “Null” paragraph. |
| 277 | **SEA gate-first precedent and conjectural composition:** supported by §4.4 and the source’s qualifications. |
| 277 | **Builder/reviewer activity:** reproduced: 6,621 entries; 5,919 forecasts/resolutions; 5,811 exactly typed stream entries; 702 proposals, 627 stream-titled, 75 others, 46 reads/reviews. |
| 283 | **450 kernel lines:** reproduced as \(138+172+140\). `REPORT` reports 100,000 logs and 658,885 prefixes; I did not rerun that experiment. |
| 292, 297 | **Nine residual repair rows:** CSV and brief support one operator act, five machinery acts and three closes of unestablished hand. |
| 305 | **Forecasting model:** reproduced: 2,887 freshness forecasts, 2,869 naming a model, all `openai/gpt-5.4-mini`. |
| 316–319 | **Falsifier quotations:** match CHARTER §12. The specified `git log -S` returns only `879caf93`. |
| 319 | **Four window ratios:** direct in-memory entry classification reproduces 127:32, 67:82, 1,131:3,449 and 320:1,296, using the specified window ends. I did not run `judge/status.py`. |
| 351–353 | **Fixed-table crossing and 9/28 criteria:** supported as reported retrospective constructions by the cited audit. |
| 363 | **No rule entry:** reproduced from all 7,810 entries. |
| 381 | **Runner model share:** independently queried issue titles: 720 of 853 model-named `builder:`/`reviewer:` issues from 30 October through observation name `gpt-5.4-mini`, **84.4%**. |
| 381, 411 | **Book provenance:** exactly one body citation, in Disclosure, plus its bibliography entry. |

### Remaining inadequate backing or specification

1. **Line 318: “no row has been re-attributed” is overbroad.**  
   The raw and attributed tables establish otherwise:
   - `acts-20261101-raw.csv` has seven repair rows; the attributed table has one repair and six `party-act` rows.
   - `acts-20261103T2144-raw.csv` has 81 repair rows; the attributed table has nine repairs and 72 `party-act` rows.

   `BRIEF-C1b-draft.md`, Amendment 2, explicitly prescribes attribution by declaration. This does not establish improper reclassification, and the nine residual C2a rows were not subsequently re-attributed. But the paper must distinguish **unchanged on-log typing**, **declaration-based attribution of platform acts**, and **retention of those nine residual rows**. The existing statement obscures a measurement step material to the falsifier.

2. **Line 243: “a rule fixed before any window” conflates design commitment and implemented predicate.**  
   The mechanical-typing commitment predates windows, but the cited predicate entered the code on 31 October, while C1a had already opened on 25 October. Say the charter committed the principle beforehand and the implemented liveness predicate preceded C1b’s opening.

3. **Line 319: the 14-day scan needs its observation boundary stated.**  
   I reproduce the worst complete interval as **63:5**, breach starts confined to the initial period through 17 October, and the post-seq-31 maximum as **872:1,755**. The latter requires \(t+14\text{ days}\le T_{\mathrm{obs}}\). Right-truncated intervals near the record’s end are not complete 14-day observations. Add that restriction explicitly.

4. **Line 123: amendment timing is ambiguous.**  
   “It takes effect at \(k\). Two things change at once” can place charter matching at activation. The cited code instead requires matching the newly promulgated digest immediately at \(a\), while prohibiting pushes during the intervening interval. State those two immediate effects at \(a\) directly.

5. **Lines 14 and 277: fixed evaluators versus untested evaluators.**  
   The sources establish protected, fixed evaluation boundaries. They do not establish absence of evaluator testing in every ordinary sense; DGM Appendix H itself experimentally exposes a detector failure. “Treated as trusted evaluation infrastructure” would express the supported architectural contrast more precisely. The census measures loop-evaluation practice, not evaluator-validation frequency.

The qualified novelty statements remain plausible priority judgments rather than exhaustively established literature results. I found no further definite contradiction among the checked claims.

## 7. Overclaiming and clarity

The paper now responsibly distinguishes predictive advantage from utility, recorded labels from verified outcomes, specification from enforcement, and design from implementation. Its strongest result is an auditable institutional construction accompanied by an unfavorable baseline audit—not demonstrated superior governance or adversarial robustness.

Retain those qualifications. Compress Table 1, repeated build-order summaries, and replay row mechanics. The liveness endpoint’s unresolved units deserve their present disclosure; they should not be presented as a completed operational correction.

## 8. Recommendation

**Minor revision.** The conditional mathematics is sound, the formalization’s scope is candid, and the central empirical conclusion reproduces. The principal remaining correction concerns the description of platform-act attribution.

The five changes that matter most, in order:

1. Replace the global no-reattribution claim with an accurate account of raw classification, declaration-based attribution and the nine retained C2a rows.
2. Distinguish the charter’s advance typing commitment from the later implemented liveness predicate.
3. Specify complete 14-day intervals within the observation period.
4. Clarify immediate amendment effects and describe fixed evaluators as trusted infrastructure without implying absence of all evaluator testing.
5. Compress genealogical and replay detail while preserving implementation departures and the retrospective qualification.

RECOMMENDATION: minor revision
exit=0
```

