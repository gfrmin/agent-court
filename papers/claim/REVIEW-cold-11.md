# Cold read 11 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, run as a read-only session on the runner.
  - The first attempt (#1384) ended without a report: the runner refused its scratch directory under `/tmp`.
  - The retry (#1385), told to write no file at all, ran from 10:13Z to 10:18Z on 26 November.
- **Text read:** draft 21, at `edc563a`, the release candidate after cold read 10's accept.
- **Verdict:** minor revision. The reader found the propositions sound and reproduced every figure. It found errors that draft 21 itself had introduced: a "fixed" prompt that was revised, a stream count that included non-stream entries, an imprecise 14-day statement, and a wrong opening seq.
- **Draft 22** corrects them. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What draft 22 does |
|---|---|
| The prompt was not fixed | Now: one model in every forecast that names its model, and a prompt revised five times after it was put on the record on 2 November (`git log -- transcripts/sessions/stream-forecast.md`). |
| 5,919 is not all stream entries | Now: 5,811 of the 5,919 are of the two stream types (recounted: 5,747 freshness, 64 races); 627 of the 702 proposals are titled as stream batches. |
| "One interval"; seq 32; "before the log could hold an object entry" | Recomputed over half-open intervals, at every start time where a count changes. Intervals over 5 : 1 begin only between genesis and 17 October; the worst, at genesis, is 63 : 5. From A3's coming into force at seq 31, the worst is 872 : 1,755. The lead now says the falsifier was met on a literal reading, by intervals beginning before any key could forecast. |
| "Went unnoticed until this paper" | Now a claim about the record: no ruling, waiver or finding in it addresses the lapse, and this audit is the first to record it. |
| Designed powers against actual grants | Contribution 3, §7 and the conclusion now say that the implementation has granted powers as windows open, not on passing them, and that its promotions have so far only frozen layers. |
| The orders-of-magnitude split is not causal | Restated as differences between successive ablations, which also differ in the events used and in marginal against joint scoring. |
| Compress Table 1 and replay detail | Table 1 was already reduced to the abstract's ingredients. The replay rows stay, because a later audit showed the paper had cited the wrong file for them. |

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

An institution governing a self-modifying agent should be built first, bind its builders first, and receive authority through valid sequential evidence from its own record—including evidence that exposes defects in its tests. The abstract states this message and the body delivers a conditional design and reproducible retrospective audit; some of Table 1’s intellectual genealogy, repeated construction-order summaries, and replay plumbing contribute less directly.

## 2. Correctness

**The six propositions are sound under their stated hypotheses.** They do not collectively certify the reference implementation.

1. **Proposition 1:** Prefix-local evaluation establishes (a). Linking and position-numbering make (b)’s collision extraction correct; for unequal-length logs, the terminal sequence numbers already distinguish two lines with the same hash. The result establishes commitment relative to a retained head, not completeness or invariance under arbitrary interpreter replacement.

2. **Proposition 2:** Correct:
   \[
   g'(p)=\frac{\pi-p}{p(1-p)},\qquad
   g''(p)=-\frac{\pi}{p^2}-\frac{1-\pi}{(1-p)^2}<0.
   \]
   Monotonicity on either side of \(\pi\) gives the grid result, including endpoints and ties. Part (b) correctly concerns registered principals; the identity, collusion, performativity and nonlinear-reward qualifications are necessary and present.

3. **Proposition 3:** Clipping bounds both joint likelihoods between \(0.001^r\) and \(0.999^r\), where \(r=|R_m|\), giving \(|\bar D_m|\le1\). Predictable stakes below one and the stipulated conditional-mean null establish (a). The sufficient condition now correctly conditions on the resolved subset, fixing the random denominator. Bayesian telescoping establishes (b) when precisely the scored blocks supply the posterior updates; inclusion of the baseline supplies the second inequality. The distinction between size-weighted log-score regret and unweighted betting wealth is correctly stated.

4. **Proposition 4:** Since \(0<\hat q_j<1\), the stake lies in \([0,1/p_0)\); factors are positive and have conditional expectation at most one under the null. Continuing the unchanged process gives lifetime control. Both restarting bounds, including the exact-test qualification, are correct. The simultaneous-item endpoint remains operationally unfinished, but that implementation divergence is disclosed.

5. **Proposition 5:** Correct intersection–union argument, requiring no independence. Its component hypotheses and per-layer scope are appropriately explicit.

6. **Proposition 6:** Correct conditional finite-input agreement and historical evaluator dispatch. Part (a) essentially restates the admission condition; (c) correctly denies extrapolation. Full replay is not automatically enforced, as the paper acknowledges.

**Remark:** Correct. Simultaneity alone is harmless; using information excluded from the forecast-cutoff null is the problem. Frozen correlated factors also need not have expected product at most one. Conditional independence plus eventwise nulls repairs eventwise betting. Joint dependence modelling and marginal forecasting improvement are correctly distinguished.

**Example and simulations:** I reproduced:

| Configuration | Per-event crossing | Block crossing |
|---|---:|---:|
| Default: 20 events, 4,000 runs | 0.1325 | 0 |
| 50 events, 2,000 runs | 0.5035 | 0 |
| Independent outcomes, either configuration | 0 | Not computed |
| Roster mode, 2,000 runs | 0.2850 | 0 |

The isolated example’s drift is \(-0.1202\). Roster mode is correctly excluded as a true-null demonstration: its mixture initially has positive joint-score advantage, approximately \(0.085\).

## 3. The Lean files

I read the README and all seven files. I did not build them or independently verify the reported axiom audit; their supplied source contains no `sorry`.

- **`HashChain.lean` — `collision_of_ne`:** Faithfully models nonempty, linked, position-numbered logs backwards. Genesis’s zero parent is unnecessary to the lemma. Entries and hashes are abstract; JSON, SHA-256 security and computational reduction costs remain informal. The existential collision conclusion does not explicitly assert membership of its witnesses in the logs.

- **`Propriety.lean` — `log_score_proper`, `log_score_strict`:** Establish optimality and strictness for belief and report in \((0,1)\). They establish neither strict concavity nor the grid clause. The manuscript discloses these narrower statements.

- **`Mixture.lean` — `prod_Q`, `regret`, `regret_base`:** Establish telescoping, per-member regret and baseline regret for positive block likelihoods with \(K>0\). Positivity is weaker than requiring normalized clipped probabilities, making the algebra more general. Event products, resolved-subset construction, normalized differences and the finite maximum remain informal bridges.

- **`Ville.lean` — `ville_finite`:** Establishes the finite-horizon maximal inequality for a pointwise nonnegative supermartingale under a finite measure, using optional stopping. The infinite-horizon passage is informal.

- **`Wealth.lean` — `wealth_supermartingale`, `wealth_level`:** Establish generic recursive betting under explicit adaptedness, predictability, deterministic bounds and conditional-mean assumptions. Substituting threshold \(1/\alpha\) gives the advertised level. `value_factor` and `liveness_factor` prove scalar bounds allowing endpoint stakes and zero factors, weaker than strict positivity but sufficient for validity. Actual plug-in stake formulas and empirical filtrations are not verified.

- **`Restart.lean` — `restart_independent`, `restart_union`:** The former proves real-number algebra, without independent events or their union-probability identity; it even permits negative \(r_j\). The latter is a genuine measure-theoretic union bound. The narrowed descriptions are accurate.

- **`Conjunctive.lean` — `conjunctive_promotion`:** Establishes containment plus either crossing bound implies the promotion bound. It assumes those bounds rather than composing instantiated wealth processes.

These are useful formalizations of the generic mathematical core, with honestly disclosed bridges.

## 4. The recomputation

**The numbers reproduce.**

- Implementation-selected events: **2,820**; wealth **\(1.51983\times10^{60}\)**.
- Completed sittings: **476**; pending: **4**.
- Member events in completed sittings: **2,803**.
- Expiries: **170**, including **168** late resolutions; hence **2,633** in-time resolved events scored.
- Resolved events excluded for lacking a pre-cutoff forecast: **19**.
- Five classes, with completed-sitting counts **215, 195, 47, 15, 4**.
- Pooled-baseline final wealth: approximately **19,930; 11,090; 3.009; 1.159; 1.022**.
- Class-two maximum: approximately **11,900**.
- Thresholds: **40, 120, 240, 400, 600**.
- Per-dataset running maxima: **1 in every class**.
- Ablations: **\(2.492\times10^{58}\)** and **\(1.739\times10^{10}\)**.

The method is valid under the stated normalized, resolved-subset null and recorded-time interpretation. Membership and deadlines derive from pre-cutoff forecasts; late arrivals cannot revise expiries; pending sittings participate in class allocation. Although implemented retrospectively using completion times, assignment asks only whether an earlier sitting had completed before the new cutoff—information observable then. Within each class, stakes use earlier completed sittings.

Cross-class and partial-sitting weight updates preserve predictability but forgo Proposition 3(b), as disclosed. Summable thresholds handle adaptively created classes.

The **1.8, 48.2 and 5.9** orders-of-magnitude differences reproduce. They are sequential ablation differences, not a uniquely identified causal decomposition: event eligibility and joint-versus-marginal scoring also differ.

The retrospective qualification is essential. This is not a selection-adjusted 5% discovery claim covering all protocols considered during revision.

## 5. The revisions

The tenth referee’s five requested changes were substantially implemented:

1. **Null provenance:** Resolved. The text now distinguishes the committed, stricter \(6/11\) from the adopted attribution rule’s \(5/11\).
2. **Proposal classification:** Resolved: **627 stream-titled proposals, 75 others, 46 actual reads/reviews**. The five M2 race proposals are included; read-gate implementation proposals are excluded from reads.
3. **Kernel authorship:** Resolved. The Google revision did not replace the same-family C1 entry-type code; C1a’s first-kernel attribution now cites `REPORT`.
4. **Fourteenth-day falsifier:** The substantive correction is right—the initial fortnight breaches the ratio—but “one interval” and the opening sequence number need further precision, detailed below.
5. **Forecast-procedure aside:** Shortened, but its new “fixed template, model and prompt” wording introduces a historical inaccuracy: the template was revised.

## 6. Backing

Line numbers refer to `draft.md` at the supplied paper commit. Repository checks use `e580b64`, except the explicitly requested historical commits. “Supported” means source support, not independent certification that every historical experiment occurred.

### Direct source checks

| Paper lines | Claim and check |
|---|---|
| 20 | **DGM 20%→50%:** supported by the cited paper’s results. |
| 20 | **Detector-marker removal:** supported by DGM Appendix H. |
| 20 | **Hyperagents’ fixed boundary and parent-selection exception:** supported by v2’s TeX source, including “ensure safety, prevent evaluation gaming” and future boundary expansion. |
| 20 | **114 studies, 90 self-described RSI, 22% audited reruns:** supported by arXiv:2610.27610. |
| 22 | **Kolt quotation:** supported by the retrieved paper text. |
| 55 | **Resolution schema and promotion attestation:** supported by `SPEC` §5 and item 15. |
| 55 | **Known wrong resolution stands:** supported by `REPORT`, C1a §4, forecast 123. |
| 83 | **Integrity does not establish completeness:** supported by Zhao et al., Corollary 3. |
| 99–109 | **Seven fields, folded state, fourteen reasons:** supported by `SPEC` and `kernel/check.py`. |
| 123 | **Activation-height check, immediate charter matching and push freeze:** supported by kernel and `SPEC` items 2/12. |
| 125, 135 | **Named key powers, last-key guard, principal-based self-resolution refusal:** supported by entries and kernel. |
| 186 | **Per-resolution stake/weight/base updates:** supported by `judge/value.py` and `judge/entries.py`. |
| 186 | **Fourteen resolutions within one minute:** seqs 550–563 run from 12:15:08Z to 12:15:58Z. |
| 190 | **641 items, 190 tied:** in-memory execution of the pure item functions reproduces this; tied items comprise 188 expiries and two batches. |
| 202, 333 | **Scrivens’ qualified finite-total-TPR claim:** supported by v2’s power-law and overlap conditions. |
| 214–220 | **Installation boundary and partial replay:** supported by `SPEC`, `installing_push`, the 706-row table and `pins/replay.py` indices 300/400/593. Workflow runs the pins. |
| 235 | **RQGM anchor and selective erasure:** supported by the cited paper. |
| 237 | **Kernel authorship:** trailers and historical NOTES support OpenAI/Anthropic at C0, same-family OpenAI C1 additions, Google’s last-key guard, and Google/Anthropic C1a attribution. |
| 237 | **No ruling addressing the C1 lapse:** none found in the four `RULING-*` files or relevant logged decisions. |
| 243–246 | **Repair exclusions, taint, fix exception and pending clearing:** supported by `item_process`, `window_fixes`, and the cited brief. |
| 264 | **19 key entries, 14 before promotion:** reproduced; all are the operator’s grants. RUNBOOK supports the stated opening-time grants. |
| 272 | **\(6/11\) versus \(5/11\):** exact distinction appears in the brief’s “Null” paragraph. |
| 277 | **SEA gate-first precedent and conjectural composition:** supported by SEA §4.4 and its qualifications. |
| 277 | **6,621 entries; 702 proposals; revised proposal split:** reproduced, subject to the forecast/resolution wording issue below. |
| 283 | **450 kernel lines:** git-object counts give \(138+172+140\). `REPORT` reports 100,000 logs and 658,885 prefixes. |
| 291 | **C1b nine-item wealth:** in-memory computation gives exactly \(214358881/8398080\). |
| 292, 297 | **Nine repair rows:** CSV and brief support one operator act, five machinery acts and three issue closes of unestablished hand. |
| 305 | **Forecasting model:** 2,887 freshness forecasts; 2,869 name a model, all `openai/gpt-5.4-mini`. |
| 316–319 | **Four falsifier quotations:** match CHARTER §12. The specified `git log -S` returns only `879caf93`. |
| 351–353 | **Fixed-table crossing and 9/28 criteria:** supported as reported counterfactual constructions by the named audit. |
| 363 | **No `rule` entry:** reproduced from the complete log. |
| 381 | **Runner model share:** among 853 model-named `builder:`/`reviewer:` issue titles created from 30 October through the observation time, 720 name `gpt-5.4-mini`: **84.4%**. |
| 381, 411 | **Book cited only as provenance:** one body citation, in Disclosure, plus its bibliography entry. |

I did not rerun `judge/status.py`. The per-window ratios have the prior reproduction specified in the request; direct entry classification also confirms C1a, C1b and the veto-ended C2a′ counts.

### Remaining inadequate backing or discrepancies

1. **Line 145: “a fixed template, model and prompt … the stream … is such a procedure.”**  
   The model attribution is supported, but the prompt was not fixed across the audited stream. `git log` and `git diff 0a60c849 e580b64 -- transcripts/sessions/stream-forecast.md` show changes to horizons, probability guidance, execution order and URL checks. Describe a **versioned, history-dependent forecasting procedure**. This does not invalidate predictable betting.

2. **Line 277: “the two streams: 5,919 forecasts and resolutions.”**  
   **5,919 is every builder/reviewer forecast and resolution**, not just the two streams. Grouping each resolution by its forecast’s type gives **5,811** entries for exactly `world.renavon` and `world.hkjc`; the remaining **108** include review, programme and proposal forecasts/resolutions, plus two entries associated with misspelt `world.renavone`. Preserve the total but separate it from stream membership.

3. **Lines 315 and 319: “met once” / “one interval.”**  
   This holds for the enumeration of full windows **anchored at log entries**, not arbitrary 14-day intervals. For example, the half-open interval starting **2026-10-14T05:41:40Z**, one second after genesis, contains **62 procedure and five object entries**, also exceeding 5:1. Say **one initial breach episode**, or specify the anchoring convention.

4. **Line 319: “C1a’s opening (seq 32).”**  
   Seq 32 declares `reviewer-2`; A3 is entered at **seq 30**, activating at 31. Starting the full-window scan at seq 30 gives a maximum **873:1,755**, rather than 871:1,755; starting at activation gives 872:1,755. All are approximately 0.5:1, so the substantive conclusion survives.

5. **Lines 315–316: initial fortnight “before the log could hold an object entry.”**  
   Only its **beginning** predates forecast capability. The fortnight itself contains five object entries, beginning at seq 38. Correct the temporal wording.

6. **Line 237: “the lapse went unnoticed until this paper.”**  
   Absence of a recorded ruling supports “no recorded ruling addresses it,” not a universal statement about prior awareness. Attribute discovery to this audit or restrict the claim to the searched record.

The qualified novelty claims are plausible literature judgments, not exhaustively established priority results.

## 7. Overclaiming and clarity

The manuscript now handles its largest limitations responsibly: no agent, no controlled comparison, operator-controlled outcomes, incomplete act monitoring, weak useful-work criteria and implementation departures are all disclosed.

Keep the distinction between **proposed authority allocation** and **demonstrated implementation history** prominent. Lines 14, 34, 341 and 375 describe powers earned through tests; line 264 establishes that actual capability grants have not been consequences of promotions. The record demonstrates tested window transitions and auditability, not that the proposed capability-allocation mechanism has operated.

Likewise, retaining a fixed testing protocol is compatible with an adaptive forecaster; calling the forecaster’s prompt fixed is unnecessary.

Table 1 could be compressed, and replay row indices and some window genealogy moved to ancillary documentation. Retain the trust-boundary and implementation-divergence details: they are essential qualifications.

## 8. Recommendation

**Minor revision.** The conditional mathematics is sound, the formalization’s scope is candid, and the central empirical result reproduces. The remaining changes require factual precision and presentation, not another experiment.

The five changes that matter most, in order:

1. Replace the fixed-prompt claim with an accurate description of the versioned forecasting procedure.
2. Separate the **5,919 total** forecast/resolution entries from the **5,811 exactly typed stream** entries.
3. Correct the 14-day anchoring, opening sequence number and “before object entries” wording.
4. Maintain a consistent distinction between the proposed evidence-earned powers and the implementation’s actual grants.
5. Restrict the unnoticed-lapse claim to documented discovery, and compress genealogical and replay detail.

RECOMMENDATION: minor revision
exit=0
```

