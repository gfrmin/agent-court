# Cold read 15 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, renavondata/opencode-runner #1446, 04:06Z to 04:15Z on 28 November. It read the whole paper, formed its view, and only then read the earlier reports.
- **Text read:** draft 28, the release candidate, at `7335140`. Guy chose on 28 November to publish it as a design and an audit.
- **Verdict:** **minor revision**.
  - "So scoped, this is a sound and useful arXiv preprint."
  - The six propositions are sound; the simulations, the recomputation, the ablations and the forking-paths ranges all reproduce.
  - About 35 claims were checked against their sources, and the reader found no factual contradiction.
  - On the adversarial reports, it found their rejection cases compelling against institutional validation at a demanding venue, but said they "do not compel rejection of the current, expressly narrower arXiv design-and-audit paper".
- **Draft 29** takes every verified point except the presentation choices noted below.
- **The request's own error:** our prompt gave arXiv:2111.04986 for Choe & Ramdas 2024a, which is the wrong locator. The correct one is 2110.00115. The paper cites the DOI and was not affected.

## Disposition

| Point | Verified? | What draft 29 does |
|---|---|---|
| Table 1 says "each promoted on criteria stated in advance" without the cap exception of §4.3 | Yes (SPEC §10) | Adds "with recorded departures (§4.3, §6)". |
| §4.3: "Rejecting … shows" a conditional advantage | Yes | Now "is evidence that"; "is not evidence of a persistent advantage". |
| §8: "That is the performative case" asserts influence that is only possible | Yes | Now "That exposes the stream to the performative case". |
| Prop. 1(b): logs of unequal length give a collision at once | Yes | Proof shortened: their last lines differ in `seq` and both hash to $h$. |
| Define the cutoff filtration explicitly, including which earlier events resolved | Yes | $\mathcal G_{m-1}$ now lists outcomes, resolved subsets, scores and stakes of earlier blocks, and is increasing. |
| Split the Remark | Fair | Split: the Remark gives the filtration argument, and a following paragraph gives the alternative and the joint-scoring cost. |
| Label the batched-liveness unit an open operational definition | Yes | Done, with "until it is fixed the batching rule is not a deployable protocol". |
| Ablation table | Fair (also asked by adversarial read 2) | Table 3 added. |
| The falsifiers' opening sentence is hard to parse | Fair | Rewritten as one sentence per falsifier. A table was not added, since the bullets carry the evidence. |
| Bröcker: uncertainty, resolution and reliability | Yes: eq. (13), Table 1 ("Ignorance") | Made precise, for strictly proper scores. |
| Freeze the Disclosure's endpoint and title rule | Yes | 30 October to 25 November: "720 of about 850" model-named sessions; the parse dependence is stated (849–855). |
| "Joint predictive value" in the abstract | — | Not taken: §2 defines value, and the Remark explains the joint score. |
| Shorten Table 1; move replay indices and commit genealogy to ancillary files | — | Not taken: the bracketed checks are the paper's convention for claims about the implementation. |

## The report (verbatim)

# Referee report

Line numbers refer to `draft.md` at `7335140ce5940889ecd0151daa2773346c59314a`. Implementation checks use `e580b64`. I formed the assessments in parts 1–6 before reading the earlier reports. The working tree remains clean.

## 1. The one idea

An institution governing a self-modifying agent should be built first, bind its builders first, and earn additional authority through valid sequential evidence from its own record. That record should expose failures of the institution’s evidence—including invalid betting protocols and weak comparators—rather than merely certify success.

The abstract states this message, and the body delivers a design, conditional guarantees and a reproducible retrospective audit. It accurately distinguishes the proposed authority-allocation mechanism from the implementation’s actual grants. Table 1’s intellectual genealogy, the repeated construction-order summaries and some replay mechanics serve the message less directly than §§4–6.

## 2. Scope

**The stated scope is accurate and sufficiently prominent.** The abstract, introduction at line 31, §5.1, limitations and conclusion disclose that:

- no self-modifying agent has been built under the design;
- capability grants have not depended on passing the proposed tests;
- the record does not validate the institution;
- the audit is retrospective;
- passing the statistical criteria has not been connected experimentally to welfare, safety or competent use of additional authority.

So scoped, this is a sound and useful arXiv preprint. Its strongest contribution is a precise governance proposal accompanied by an unusually inspectable, unfavorable audit of its own implementation.

A peer-reviewed systems or empirical AI venue would additionally need actual test-conditioned capability transitions, a completed operational liveness endpoint, repeated prospective comparisons against simpler governance, deliberate attacks, independently assessed outcomes, and measurements of useful work and human burden. Those requirements distinguish evaluation of the institution from the present design-and-audit contribution.

## 3. Correctness

**The six propositions are sound under their stated hypotheses.**

1. **Proposition 1, lines 113–121.** Prefix-local evaluation proves (a). Linking and position-numbering establish (b)’s collision extraction. Indeed, unequal-length logs already have distinct terminal sequence numbers, so equal terminal hashes immediately supply a collision. The result establishes commitment relative to an authenticated head, not completeness or immunity to arbitrary checker replacement. Line 123 now appropriately calls it one computational ingredient of prospectivity.

2. **Proposition 2, lines 131–137.** Correct:
   \[
   g'(p)=\frac{\pi-p}{p(1-p)},\qquad
   g''(p)=-\frac{\pi}{p^2}-\frac{1-\pi}{(1-p)^2}<0.
   \]
   Monotonicity around \(\pi\) gives the adjacent-grid-point result, endpoints and possible ties. Part (b) matches the kernel’s registered-principal comparison. Identity assignment, collusion, outcome manipulation and nonlinear rewards are properly qualified.

3. **Proposition 3, lines 153–184.** For \(r=|R_m|>0\), clipping puts both joint likelihoods between \(0.001^r\) and \(0.999^r\), yielding \(|\bar D_m|\le1\). Predictable stakes in \([0,1)\) give positive factors with conditional expectation at most one under the displayed null. Conditioning the sufficient expected-score condition on \(R_m\) correctly handles the random divisor. Bayesian telescoping proves (b) when updates use exactly the scored blocks; inclusion of the baseline supplies its second inequality. The distinction between size-weighted score regret and unweighted betting wealth is explicit.

   Assumption (A) now supplies the required current-block blindness and earlier-block information ordering. Dynamically created classes require the cutoff-information null for the adaptively selected class observations; the summable threshold schedule then controls their union.

4. **Proposition 4, lines 192–208.** Since \(0<\hat q_j<1\), \(0\le\lambda_j<1/p_0\). Factors are positive and have conditional expectation at most one under the stipulated null. Continuing the unchanged product gives lifetime crossing control. Both restart bounds and the exact-test qualification are correct.

   The simultaneous-item correction remains an **unfinished operational definition**: the common unit for successful batches and expiries is left open. This does not invalidate the generic theorem, but it prevents treating the paragraph as a completed deployable liveness protocol.

5. **Proposition 5, lines 210–214.** Correct intersection–union reasoning; independence is unnecessary. Component validity and per-layer scope are appropriately explicit.

6. **Proposition 6, lines 220–239.** Correct conditional finite-input agreement and historical-evaluator dispatch. Part (a) essentially restates the admission condition; (c) correctly denies extrapolation. The substantial difference between specified replay and automated enforcement is disclosed before the proposition.

**Remark, line 186.** Correct: filtration mismatch is the defect, while simultaneous resolution is its manifestation here. Freezing correlated factors does not suffice. Conditional independence together with eventwise nulls supports eventwise betting. Joint dependence modelling and improved marginal forecasts are correctly distinguished.

**Example, line 188.** The isolated randomized-product counterexample is sound. I reproduced:

| Configuration | Per-event crossings | Block crossings |
|---|---:|---:|
| \(n=20\), 4,000 runs | 530/4,000 = 13.25% | 0 |
| \(n=50\), 2,000 runs | 1,007/2,000 = 50.35% | 0 |
| Independent outcomes, either configuration | 0 | Not computed |
| Requested roster mode, 2,000 runs | 28.50% | 0 |

The stated intervals reproduce to their displayed precision; Wilson intervals are approximately 12.23–14.34% and 48.16–52.54%. The one-sided exact 95% upper bound for 0/4,000 is 0.07487%, agreeing with the rule-of-three figure. The drift is \(-0.1202\).

Roster mode is correctly excluded as a true-null demonstration: its mixture can exploit shared outcomes despite the members’ lack of marginal skill.

## 4. The Lean files

I read the README and all seven files. **I did not build them or independently verify the reported axiom audit.** The supplied proof sources contain no `sorry`.

| Mapped theorem(s) | Comparison with the paper |
|---|---|
| **HashChain:** `collision_of_ne` → 1(b) | Faithfully models nonempty linked, position-numbered logs backwards. Genesis’s zero parent is unnecessary. Entries and hashes are abstract; JSON, SHA-256 security and computational reduction costs remain informal. The existential conclusion does not explicitly locate its collision witnesses in the logs, although the proof constructs them there. |
| **Propriety:** `log_score_proper`, `log_score_strict` → 2(a) | Proves optimality and strictness on \((0,1)\), not strict concavity or the grid clause. Accurately disclosed. |
| **Mixture:** `prod_Q`, `regret`, `regret_base` → 3(b) | Proves telescoping, per-member regret and baseline regret for positive block likelihoods and \(K>0\). Positivity is weaker than normalized clipped-probability assumptions, making the algebra more general. Event products, resolved subsets, normalization and the finite maximum remain informal bridges. |
| **Ville:** `ville_finite` | Proves the finite-horizon maximal inequality for a pointwise nonnegative supermartingale under a finite measure, using optional stopping. Infinite-horizon passage remains informal. |
| **Wealth:** `wealth_supermartingale`, `wealth_level` → 3(a), 4(a) | Proves generic recursive betting under adaptedness, predictability, deterministic bounds and the conditional-mean null. Substituting \(1/\alpha\) yields the advertised level. The stronger explicit measurability/boundedness hypotheses are sufficient for the intended construction. |
| **Wealth:** `value_factor`, `liveness_factor` | Proves scalar factor bounds allowing endpoint stakes and zero factors—less than strict positivity, but enough for validity. These lemmas do not verify the concrete stake formulas or empirical filtration. |
| **Restart:** `restart_independent`, `restart_union` → 4(b) | The former is real-number algebra, without independent events or their union-probability identity; it permits negative \(r_j\). The latter is a genuine measure bound. The narrower scope is accurately described. |
| **Conjunctive:** `conjunctive_promotion` → 5 | Proves containment plus either component crossing bound implies the promotion bound. Component bounds are hypotheses rather than instantiated consequences of the wealth theorems. |

The formalization supports the advertised mathematical core, rather than end-to-end correctness of the implementation or measurement pipeline. Lines 91–95 communicate that distinction responsibly.

## 5. The recomputation

**The numerical results reproduce.**

| Quantity | Reproduced result |
|---|---:|
| Implementation-selected events | 2,820 |
| Implementation wealth | \(1.51983\times10^{60}\) |
| Completed / pending sittings | 476 / 4 |
| Member events in completed sittings | 2,803 |
| Expiries, including late resolutions | 170, including 168 |
| Resolved events without pre-cutoff forecasts | 19 |
| Completed sittings by class | 215, 195, 47, 15, 4 |
| Pooled final wealth | \(1.993\times10^4,\ 1.109\times10^4,\ 3.009,\ 1.159,\ 1.022\) |
| Class-two maximum | \(1.190\times10^4\) |
| Thresholds | 40, 120, 240, 400, 600 |
| Per-dataset running maxima | 1 in every class |
| Successive ablations | \(2.492\times10^{58},\ 1.739\times10^{10}\) |

The method supports the bounded-betting argument under the stipulated **normalized resolved-subset null and recorded-time interpretation**:

- membership and deadlines derive from pre-cutoff forecasts;
- late resolutions cannot revise expiries;
- pending sittings participate in class allocation;
- class assignment asks whether preceding sittings have completed before the new cutoff, an observable condition;
- stakes use earlier completed sittings in their class;
- weights and baselines use pre-cutoff information;
- deterministic summable thresholds handle adaptive class creation.

Cross-class and partial-sitting weight updates preserve predictability while forfeiting Proposition 3(b), as disclosed.

The per-event ablation now dates contributions by **whole-sitting completion**, including members that expire. It therefore fixes the availability defect identified by adversarial read 1. The successive logarithmic differences are 1.785, 48.156 and 5.941 orders of magnitude, matching 1.8, 48.2 and 5.9.

I also reran the historical scripts corresponding to the reported protocol revisions. They reproduce the final-wealth ranges: class 1, \(1.993\times10^4\)–\(2.231\times10^4\); class 2, \(1.109\times10^4\)–\(1.615\times10^4\). The per-dataset maximum remains 1 wherever computed.

These are reproducible retrospective sensitivity results, not a selection-adjusted 5% discovery procedure. Line 305 says this correctly.

## 6. Backing

### Direct source checks

The following checks are independent of the earlier reports. Historical experiment counts are identified as reported evidence where I did not rerun the experiment.

| Line(s) | Claim checked and source |
|---|---|
| 20 | DGM 20%→50%: supported by the cited paper’s abstract/results. |
| 20 | Detector-marker removal despite instructions: supported by DGM Appendix H. |
| 20 | Hyperagents’ boundary, safety quotation and parent-selection exception: supported by Appendix A.5. |
| 20 | 114 studies, 90 self-described RSI, 22% repeated-loop auditing: supported by the census text. |
| 55 | Promotion evidence checked for presence/hash, with operator attestation: explicit in SPEC §10.15. |
| 55 | Resolution truth not checked: SPEC §5 requires an outcome and nonempty evidence string. |
| 55 | Known incorrect resolution stands: REPORT, C1a §4, explicitly documents forecast 123. |
| 99–109 | Seven fields, state structure and fourteen refusal reasons: supported by SPEC and `kernel/check.py`. |
| 123 | Activation above amendment position and immediate promulgation/push effects: supported by kernel and SPEC. |
| 125, 135 | Builder/herald powers, operator powers, last-key guard and principal-based self-resolution refusal: supported by entries and kernel. |
| 145 | Initial prompt recording plus five revisions: six relevant history commits reproduce this. |
| 149 | Three cap raises against pre-statement: explicit in SPEC §10; seq 197 follows C1b’s opening at 188. |
| 184 | “Strong, pointwise null”: supported by Choe–Ramdas §4.4. |
| 186 | Filtration mismatch: supported by *Combining Evidence Across Filtrations*, including forecaster applications. |
| 190 | Per-event stake/weight updates and same-type resolution-order baseline: directly present in `value.py` and `entries.py`. |
| 190 | Fourteen resolutions within one minute: reproduced from seqs 550–563. |
| 194 | 641 liveness items, 190 timestamp-sharing: reproduced; 188 expiries and two batches. |
| 224 | Three replay rows out of 706: `pins/replay.py` uses 300, 400, 593; workflow invokes the pins. |
| 241 | Same-family C1 additions: historical trailers/NOTES support this; the Google diff adds the last-key guard rather than replacing that code. |
| 247 | Typing predicate unchanged since introduction: the specified history search returns `879caf93`. |
| 268 | Nineteen key entries, fourteen before first promotion: reproduced; all are operator grants. |
| 276 | \(6/11\) versus \(5/11\): explicitly distinguished in the brief’s “Null” paragraph. |
| 277, 391 | Titles identify mini and larger model sessions: supported; they do not establish reliability transfer. |
| 283 | 6,621 entries; 5,919 forecasts/resolutions; 5,811 stream entries; 702 proposals; 627 stream-titled: reproduced. |
| 289 | Kernel size: 450 physical lines. REPORT supports 100,000 logs and 658,885 prefixes; I did not rerun that historical experiment. |
| 324 | Raw/attributed repairs: CSV pairs reproduce 7→1 and 81→9; Amendment 2 states the declaration rule. |
| 325 | Complete half-open 14-day scan: reproduced 63:5 at genesis; breaching starts end on 17 October; post-seq-31 maximum 872:1,755. |
| 347 | Artikis 2009 executable normative specifications: supported by the author-hosted paper. |
| 347 | Artikis 2012 agent-driven runtime rule changes: explicit in the paper. |
| 347 | Six Ostrom principles, Event Calculus and testbed: explicit in Pitt–Schaumeier–Artikis’s abstract. |
| 347 | AgentCity’s smart contracts as law and ownership chain: explicit in its text. |
| 345 | Schneier–Kelsey audit-log precedent: supported by the original authors’ publication page and abstract. |
| 359 | Proper-score decomposition including log score: Bröcker’s Table 1 includes “Ignorance”; equation (13) gives the decomposition. |
| 369 | Operator’s three forecasts all `world.assize`: reproduced; none is `world.renavon`. |
| 391 | Runner share: 720/853 model-named `builder:`/`reviewer:` issues from 30 October through observation are mini-model sessions, 84.4%. “About four in five” holds. |

**Locator correction:** the checking request names arXiv:2111.04986 for Choe–Ramdas. That identifier is an unrelated federated-learning paper. *Comparing Sequential Forecasters* is **2110.00115**, matching the draft’s DOI. This is an error in the request’s locator, not the manuscript’s bibliography.

### Residual backing or scope defects

1. **Line 79: advance criteria.** The table’s unqualified “each promoted on criteria stated in advance” gives a cleaner prospectivity account than line 149 and SPEC support. Add “with recorded departures from pre-statement (§4.3).”

2. **Line 184: rejection “shows” conditional advantage.** A level-\(\alpha\) rejection is evidence against the null, not a deductive demonstration of its falsity. Replace “shows” with “provides level-controlled evidence.”

3. **Line 369: “That is the performative case.”** Source ownership establishes the capacity to influence outcomes; it does not establish that predictions actually changed their distribution. Say “This creates exposure to performative manipulation.”

The qualified priority claims remain literature judgments, not exhaustive absence results. I found no further definite factual contradiction among the checked claims.

## 7. Writing

The following paragraphs or table passages merit changes; unlisted paragraphs are satisfactory for their stated purpose.

| Line(s) | Specific fix |
|---|---|
| 14 | “Predictive value” is joint-score value here. Consider “joint predictive value” to expose the distinction developed in the Remark. |
| 24 | The argued thesis is acceptable, but “trusted” is broader than the operational guarantees. Keep it explicitly an argument, as presently written. |
| 53, 63–81 | The motivation/consequence distinction is now clear. Table 1 could still be shortened without weakening the construction. |
| 79 | Add the pre-statement exception identified above. |
| 121 | Shorten the unequal-length case: terminal sequence numbers already differ, immediately yielding a collision. |
| 153–157 | Define the increasing cutoff filtration in one explicit sentence, including previous resolved-subset identities. The intended construction is recoverable but unnecessarily implicit. |
| 184 | Replace “shows” with “provides level-controlled evidence.” |
| 186 | Split this long paragraph into filtration validity, independence-based alternative, and joint-versus-marginal scoring. |
| 194 | Label the unresolved common liveness unit an “open operational definition.” This is more informative than merely “leave that unit open.” |
| 224, 241 | Move replay indices and some commit genealogy to ancillary documentation; retain the enforcement and diversity limitations. |
| 305–319 | An ablation table would make the sample/scoring changes and noncausal interpretation easier to inspect. |
| 321 | The opening count of tested versus untested clauses is difficult to parse. A four-row status table would be clearer. |
| 359 | Say expected score decomposes into **uncertainty, resolution and reliability**; uncertainty is constant for a fixed outcome distribution. Bröcker supports this more precise wording. |
| 369 | Replace actual-performativity language with outcome-influence risk. |
| 391 | Freeze the disclosure’s issue-count endpoint and title-selection rule. The estimate is supported, but its denominator currently drifts. |

## 8. The earlier reports

I agree with the substantive dispositions: position-numbering, missingness, random normalization, deadline treatment, pending-class assignment, baseline interpretation, replay enforcement, attribution, prompt history and falsifier accounting have been corrected.

The decision not to average differently filtered class processes is reasonable; the summable allocation suffices. Removing roster mode as a true-null example was necessary. Correcting the auxiliary ablation by whole-sitting completion was also necessary despite unchanged rounded output.

Two corrections deserve stronger propagation:

- The cap-exception correction should reach Table 1, not only §4.3.
- The unfinished liveness unit should remain explicitly an open design component.

The adversarial reports’ rejection cases are compelling objections to **institutional validation at a demanding peer-reviewed venue**. They do not compel rejection of the current, expressly narrower arXiv design-and-audit paper. No dismissed mathematical correction remains necessary in the propositions.

## 9. Recommendation

**Minor revision.** The central mathematics is sound, the formalization’s limits are candid, and the principal empirical findings reproduce.

The changes that matter most are:

1. Preserve the design/implementation/evaluation distinction, and explicitly label the unfinished liveness endpoint.
2. Propagate the pre-statement exception into Table 1.
3. Use evidential language for rejection and risk language for potential performativity.
4. Make the filtration definition and score-decomposition wording precise.
5. Freeze the disclosure’s counting endpoint and simplify the densest audit paragraphs.

RECOMMENDATION: minor revision
