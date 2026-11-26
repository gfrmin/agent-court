# Cold read 13 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1388. The session ran from 10:49Z to 11:00Z on 26 November.
- **Text read:** draft 23, at `9e65919`.
- **Verdict:** **accept**. The reader found "no remaining definite factual contradiction". It reproduced every figure and confirmed that the twelfth referee's corrections were right, including the re-attribution counts.
- **Draft 24** makes three of its five suggested final edits:
  1. **Falsifier status.** Untested falsifier clauses are now distinguished from clauses that were tested and not triggered.
  2. **Retrospective protocol.** The paper now says the retrospective protocol is not covered by a guarantee adjusted for the choice among protocols.
  3. **Title classification.** The recipe for classing proposals by title is stated.

  The other two, compressing Table 1 and moving the replay rows into ancillary documentation, are presentation advice and are not taken. The replay rows stay because an audit found the paper had cited the wrong file for them.

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

An institution governing a self-modifying agent should be built first, bind its builders first, and earn additional authority through valid sequential tests on its own record. Its record should expose failures of the institution’s evidence—including invalid compounding and weak comparators—rather than merely certify success.

The abstract states this message, and the body delivers a conditional design, a mathematical account of its guarantees, and a reproducible retrospective audit. Table 1’s intellectual genealogy, repeated explanations of the construction order, and some replay mechanics serve it less directly. The manuscript appropriately distinguishes the proposed authority-allocation mechanism from what the implementation has actually operated.

## 2. Correctness

**The six propositions are sound under their stated hypotheses.**

1. **Proposition 1.** Prefix-local evaluation proves (a). Predecessor links and position-numbering establish (b): unequal terminal lines with equal hashes immediately supply a collision; equal terminal lines allow backward comparison. Different-length numbered logs necessarily have different terminal sequence numbers. This is commitment relative to a retained head, not proof of completeness or protection against arbitrary replacement of the interpreter.

2. **Proposition 2.** For \(p,\pi\in(0,1)\),
   \[
   g'(p)=\frac{\pi-p}{p(1-p)},\qquad
   g''(p)=-\frac{\pi}{p^2}-\frac{1-\pi}{(1-p)^2}<0.
   \]
   These establish the continuous optimum and the adjacent-grid-point result, including boundary cases and ties. Part (b) matches the kernel’s registered-principal comparison. The qualifications concerning collusion, identity assignment, performative outcomes and nonlinear rewards are necessary and present.

3. **Proposition 3.** For \(r=|R_m|>0\), clipping bounds both joint likelihoods between \(0.001^r\) and \(0.999^r\), yielding \(|\bar D_m|\le1\). Predictable nonnegative stakes below one give positive factors with conditional expectation at most one under the displayed null. The sufficient expected-score condition correctly conditions on the resolved subset, addressing the random denominator.

   Bayesian telescoping proves (b) when posterior updates use exactly the scored blocks. Including the baseline supplies the second inequality. The distinction between size-weighted log-score regret and unweighted betting wealth is correctly stated.

4. **Proposition 4.** Since \(0<\hat q_j<1\), the prescribed stake satisfies \(0\le\lambda_j<1/p_0\). Factors are positive and have conditional expectation at most one under the null. Continuing the unchanged product gives lifetime crossing control. The restarting bounds, exact-test qualification, and zero-stake case are correct. The simultaneous-item rule’s operational units remain unfinished, as explicitly disclosed.

5. **Proposition 5.** Correct intersection–union argument. No independence assumption is needed. The absence of a familywise guarantee across layers is explicit.

6. **Proposition 6.** Correct conditional finite-input agreement and historical-evaluator dispatch. Part (a) essentially restates the admission condition; part (c) properly denies extrapolation. The paper discloses that automated enforcement is substantially narrower than the specified full replay.

**Remark.** Correct. Simultaneous resolution is not itself the problem: conditioning subsequent bets on information excluded from the null is. Freezing stakes does not make a product of correlated factors valid. Conditional independence together with eventwise nulls supports eventwise betting. The distinction between joint dependence modelling and improved marginal forecasts is especially important.

**Examples and simulations.** I reproduced:

| Configuration | Per-event crossing | Block crossing |
|---|---:|---:|
| Default: 20 events, 4,000 runs | 0.1325 | 0 |
| 50 events, 2,000 runs | 0.5035 | 0 |
| Independent outcomes, default | 0 | Not computed |
| Full-roster mode, 2,000 runs | 0.2850 | 0 |

The isolated example’s drift is \(-0.1202\). Roster mode is correctly excluded as a true-null demonstration: its joint mixture can exploit shared outcomes despite its members lacking marginal skill.

## 3. The Lean files

I read the README and all seven files. **I did not build them or independently verify the reported axiom audit.** The supplied source contains no `sorry`.

| File and mapped results | Comparison with the paper |
|---|---|
| **HashChain:** `collision_of_ne` → 1(b) | Matches nonempty linked, position-numbered logs represented backwards. Genesis’s zero parent is unnecessary. Entries and hashes are abstract; canonical JSON, SHA-256 security and computational reduction remain informal. The existential conclusion does not explicitly require the collision witnesses to belong to the supplied logs. |
| **Propriety:** `log_score_proper`, `log_score_strict` → 2(a) | Proves optimality and strictness on \((0,1)\), not strict concavity or the grid clause. This narrowing is accurately disclosed. |
| **Mixture:** `prod_Q`, `regret`, `regret_base` → 3(b) | Proves telescoping, per-member regret and baseline regret for positive block likelihoods and \(K>0\). Positivity is weaker than normalized clipped-probability assumptions, making the algebra more general. Event products, resolved subsets and the finite maximum are informal bridges. |
| **Ville:** `ville_finite` | Establishes the finite-horizon maximal inequality for a pointwise nonnegative supermartingale under a finite measure, using optional stopping. Infinite-horizon passage is informal. |
| **Wealth:** `wealth_supermartingale`, `wealth_level` → 3(a), 4(a) | Proves generic recursive betting under explicit adaptedness, predictability, deterministic bounds and conditional-mean hypotheses. Substituting \(1/\alpha\) gives the claimed level. The factor lemmas permit endpoint stakes and zero factors—less than strict positivity, but sufficient for validity. Concrete stake formulas and the empirical filtration are not formalized. |
| **Restart:** `restart_independent`, `restart_union` → 4(b) | The first proves real-number algebra, without modelling independent events or their union probability; it even allows negative \(r_j\). The second is a genuine measure bound. The README accurately distinguishes these scopes. |
| **Conjunctive:** `conjunctive_promotion` → 5 | Proves containment plus either component crossing bound implies the promotion bound. Component bounds are hypotheses, not instantiated consequences of the wealth files. |

The formalization supports a useful generic mathematical core. It does not verify the reference implementation, its measurement pipeline, or the bridges connecting them to those theorems; the manuscript now says so.

## 4. The recomputation

**The numbers reproduce.**

| Quantity | Reproduced result |
|---|---|
| Implementation-selected events | 2,820 |
| Implementation wealth | \(1.51983\times10^{60}\) |
| Completed / pending sittings | 476 / 4 |
| Events in completed sittings | 2,803 |
| Expiries, including late resolutions | 170, including 168 late |
| Resolved events without pre-cutoff forecasts | 19 |
| Completed sittings by class | 215, 195, 47, 15, 4 |
| Pooled-baseline final wealth | 19,930; 11,090; 3.009; 1.159; 1.022 |
| Class-two maximum | Approximately 11,900 |
| Thresholds | 40, 120, 240, 400, 600 |
| Per-dataset running maxima | 1 in every class |
| Successive ablations | \(2.492\times10^{58}\), \(1.739\times10^{10}\) |

The method supports the betting argument under the stipulated **normalized resolved-subset null and recorded-time interpretation**:

- Membership and deadlines derive from pre-cutoff forecasts.
- Late resolutions cannot revise expiries.
- Pending sittings participate in class allocation.
- Although implemented retrospectively using completion timestamps, class assignment asks whether earlier sittings had completed before the new cutoff—information observable then.
- Class stakes use earlier completed sittings; weights and baselines use pre-cutoff information.
- Summable deterministic thresholds accommodate adaptively created classes.

I additionally checked that no scored event’s recorded resolution was already available at its own cutoff.

Cross-class and partial-sitting weight updates preserve predictability but forgo Proposition 3(b), as disclosed. The 1.8, 48.2 and 5.9 orders-of-magnitude differences reproduce and are correctly described as successive ablation differences.

“Valid” here means valid for the fixed protocol under its stated null. It does not provide a selection-adjusted 5% discovery guarantee covering all protocols considered during manuscript revision.

## 5. The revisions

The twelfth referee’s substantive points are resolved:

1. **Off-log re-attribution:** Corrected. The raw/attributed CSV pairs establish reductions from seven repair rows to one, and from 81 to nine. Line 318 now distinguishes attribution from re-typing and retains the nine residual rows.
2. **Advance typing commitment versus later code:** Corrected at line 243. The charter’s commitment is distinguished from the predicate’s introduction during C1b. The earlier referee’s suggested placement before C1b’s opening was itself inaccurate.
3. **Observation boundary:** Corrected. Line 319 specifies complete 14-day intervals ending within the observed record.
4. **Immediate amendment effects:** Corrected. Line 123 locates both immediate consequences at amendment entry \(a\).
5. **Fixed versus untested evaluators:** Corrected. “Held fixed and trusted as infrastructure” matches the architectural evidence without denying evaluator experiments.
6. **Compression:** Largely unadopted. This remains presentation advice, not a correctness defect.

## 6. Backing

Line numbers refer to the supplied draft. Repository checks use `e580b64`, except explicitly identified historical revisions. I distinguish source support from independently rerunning historical experiments.

### Direct checks

| Lines | Claim and result |
|---|---|
| 20 | **DGM 20%→50%:** supported by the cited paper’s abstract/results. |
| 20 | **Detector-marker removal despite instructions:** explicitly supported by DGM Appendix H’s node-114 account. |
| 20 | **Hyperagents’ fixed boundary, safety rationale and parent-selection exception:** supported by its v2 source, including the quoted wording and future-work discussion. |
| 20 | **114 studies, 90 self-described RSI, 22% audited reruns:** supported by arXiv:2610.27610. |
| 55 | **A wrong resolution stands:** `REPORT`, C1a §4, documents forecast 123’s incorrect resolution and inability to replace it. |
| 99–109 | **Entry format, state and fourteen refusal reasons:** supported by `SPEC` and `kernel/check.py`. |
| 123 | **Activation above amendment position and immediate effects:** supported by the kernel and SPEC §10. |
| 125, 135 | **Named capability grants, last-key guard and principal-based self-resolution refusal:** supported by the entries and kernel. |
| 145 | **Prompt revised five times after initial recording:** six relevant commits reproduce this history. |
| 186 | **Per-resolution updates of stakes, weights and baseline:** directly present in `judge/value.py` and `judge/entries.py`. |
| 186 | **Fourteen resolutions within one minute:** seqs 550–563 run from 12:15:08Z to 12:15:58Z. |
| 214–220 | **Installation boundary and partial replay enforcement:** supported by SPEC and `installing_push`; the judge does not enforce full-table replay. |
| 220 | **Replay rows 300/400/593 and CI invocation:** supported by `pins/replay.py` and the workflow. |
| 235 | **RQGM replacement anchors and selective erasure:** supported by its v3 account. |
| 237 | **Kernel authorship:** trailers, historical NOTES and the Go diff support the family history. The Google C1 revision adds the last-key guard rather than replacing the OpenAI entry-type implementation. |
| 237 | **No recorded ruling on that authorship lapse:** the specified repository search found no contrary ruling, waiver or finding. This supports the appropriately record-limited formulation. |
| 243–244 | **Repair exclusions, taint, pending clearing and failed-window exception:** supported by `item_process` and `window_fixes`. |
| 264 | **Nineteen key entries, fourteen before first promotion:** reproduced; all have proposer `guy`. RUNBOOK supports opening-time grants. |
| 272 | **\(6/11\) versus the brief’s \(5/11\):** explicitly distinguished in the brief’s “Null” paragraph. |
| 277 | **SEA’s gate-first precedent and conjectural composition:** supported by §4.4 and its qualifications. |
| 277 | **Activity census:** reproduced: 6,621 entries; 5,919 forecasts/resolutions; 5,811 exactly typed stream entries; 702 proposals. A stream-specific title filter reproduces 627 stream-labelled proposals. |
| 283 | **450 kernel lines:** reproduced as \(138+172+140\). `REPORT` supports the historical 100,000-log/658,885-prefix claim; I did not rerun it. |
| 292, 297 | **Nine residual repair rows:** CSV kinds and the brief support one operator act, five machinery acts and three closes of unestablished hand. |
| 305 | **Forecasting model:** reproduced: 2,887 freshness forecasts, 2,869 naming a model, all `openai/gpt-5.4-mini`. |
| 316–319 | **Four falsifier quotations:** match CHARTER §12. The specified `git log -S` returns only `879caf93`. |
| 318 | **Re-attribution:** raw/attributed tables reproduce 7→1 and 81→9. Amendment 2 states the declaration rule. |
| 319 | **Window ratios:** direct in-memory classification reproduces 127:32, 67:82, 1,131:3,449 and 320:1,296 using the evaluator’s boundaries. I did not run `status.py`. |
| 319 | **Fourteen-day scan:** reproduced the genesis maximum 63:5, breach starts confined to the initial period through 17 October, and post-seq-31 maximum 872:1,755. |
| 351–353 | **Fixed-table crossing and 9/28 criteria:** supported as reported retrospective constructions by the cited audit. |
| 363 | **No `rule` entry:** reproduced. |
| 381 | **Runner model share:** independently queried issue titles through the record’s observation time: 720 of 853 model-named builder/reviewer issues were `gpt-5.4-mini`, or 84.4%. “About four in five” is supported. |
| 381, 411 | **Book provenance:** exactly one body citation, in Disclosure, plus its bibliography entry. |

### Remaining incomplete backing or specification

I found **no remaining definite factual contradiction** in these checks. The residual evidentiary qualifications are:

- **Lines 315–317: falsifier status.** The second falsifier names assize’s baseline, but the reported C1b test used the builders’ baseline. The text discloses this, just as it discloses that Datalog was untested. Nevertheless, “not met” should not be read as “tested and survived”: evidence against the specifically named assize comparison is missing.
- **Lines 33–36, 248, 277, 333 and 339: priority and negative literature claims.** The citations establish relevant precedents, not exhaustive absence of another matching design. The “to our knowledge” and “in our reading” qualifiers are appropriate; the claims remain bounded literature judgments.
- **Line 273: transfer from builders to agent.** Sharing a broad model-policy class supports the design argument, but supplies no demonstrated transfer of reliability or resistance to adversarial self-modification. The subsequent qualification and limitations correctly prevent that stronger reading.

The missing controlled comparison, independent world operator, comprehensive act monitor and deployed agent are openly acknowledged limitations, not concealed evidentiary support.

## 7. Overclaiming and clarity

The manuscript now maintains its essential distinctions: mathematical validity versus implementation conformity; recorded outcomes versus verified truth; predictive advantage versus utility; and auditability versus demonstrated governance effectiveness.

Its strongest contribution is an auditable institutional design accompanied by an unfavorable audit of its own value evidence. It does not establish superior governance or adversarial robustness, and now does not need those results to deliver its abstract.

The remaining clarity risk is that readers may interpret “valid test” as validating the retrospective discovery procedure as a whole. One explicit sentence would prevent that. Likewise, “three falsifiers have not been met” could more clearly distinguish untested clauses from survived tests.

Compress Table 1, repeated build-order summaries, and replay mechanics. Preserve the trust-boundary and implementation-divergence disclosures: they are doing essential work.

## 8. Recommendation

**Accept.** The conditional mathematics is sound, the formalization’s scope is candid, the main empirical findings reproduce, and the twelfth referee’s substantive corrections are incorporated. This is a design-and-audit contribution, with appropriately limited empirical claims.

The five highest-value final edits, in order, are:

1. Distinguish **untested falsifier clauses** from clauses tested without triggering.
2. State explicitly that retrospective protocol development is not covered by a selection-adjusted 5% discovery guarantee.
3. Give the activity census’s title-classification recipe or inclusion list, making its exact counts readily reproducible.
4. Compress Table 1 and repeated construction-order explanations.
5. Move replay row mechanics into ancillary documentation while retaining the full-replay/automated-enforcement distinction in the paper.

RECOMMENDATION: accept
exit=0
```

