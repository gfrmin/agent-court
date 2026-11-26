# Adversarial read 2 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, with the same hostile brief as read 1 and no access to earlier reports. The issue is renavondata/opencode-runner #1400, run from 15:58Z to 16:08Z on 26 November.
  - The first attempt, on Gemini (#1396), ended in a server error after an hour, without a report.
- **Text read:** draft 26, at `322aebb`.
- **Verdict:** **reject**. The reader found the narrowed claims candid and the numbers "unusually reproducible". Its case is the same as read 1's: the proposed mechanism, powers granted by test, has been neither implemented nor evaluated. A paper of this scope therefore cannot pass a top venue as a validation of the institution.
- **Draft 27** fixes every verified error the reader found. The question of scope is put to Guy, because only he can settle it.

## Disposition

| Point | Verified? | What draft 27 does |
|---|---|---|
| The principal contribution is not implemented or evaluated (fatal "to acceptance in its present form") | Yes | Not fixable in the text. Since draft 26 the paper has said it does not validate the institution. The remedy is an implementation and a prospective comparison. Left to Guy. |
| The criteria are not shown to predict competent use of the powers | Yes | "What passing certifies" (§8) now says exactly what passing is evidence against: two pointwise lifetime nulls. It says it guarantees no current performance and certifies no welfare or safety. |
| A log-score decomposition is not open | Yes: Bröcker, arXiv:0806.0813 | Corrected (§8). |
| Criteria were not all committed before their windows | Yes: SPEC §10 records three raises of the line cap, the third after C1b's window opened (seq 197) | Stated in §4.3. |
| Assumption (A) did not imply that a block's own outcomes are unrealised at its cutoff | Yes | (A) now says so. |
| "Valid test" in the abstract and conclusion hides retrospective selection | Fair | Now "the block-form test", and "run retrospectively" in the conclusion. |
| Simulation uncertainty | Yes | 95% intervals added (12.2–14.3%; 48.2–52.5%; block upper bound 0.075%). |
| "Source of law" undefined; audit-log precedents | Yes | Defined operationally in §7: admissibility as a function of the law folded from earlier entries. Schneier & Kelsey 1999 added. |
| The implementation does not require a merit forecast per proposal | Yes | Stated in §4.2. |
| The freshness stream violates the independent-outcome response in Table 1; the kernel is inside a larger trusted base | Yes | Both stated in Table 1. |
| "We argue … can be trusted only as far as …" asserts necessity | — | Kept. It is the paper's thesis, marked as argument, and the paper nowhere claims to establish it. |
| Shorten the legal analogies; restructure the contributions; put the ablations in a table | — | Not taken in this draft: presentation choices. |

## The report (verbatim)

# Referee report

Line references are to `draft.md` at `322aebb5b312ccf269398a0c1c28e283d6aa5372`; implementation checks use `e580b64`. I reproduced the recomputation and all four principal simulations and inspected all seven Lean source files. I did not rebuild Lean.

## 1. The case for rejection

### 1. The principal contribution has not been implemented or evaluated — **fatal to acceptance in its present form**

The distinguishing proposal is that an institution earns additional authority through tests of its own performance (L24–36). Yet no implementation key grant has followed from promotion; powers arrived when windows opened (L268). No self-modifying agent exists, no experiment compares governance designs, and no deliberate adversarial evaluation establishes the claimed institutional benefit (L279, L377–379).

Consequently, the paper evaluates neither evidence-conditioned authority nor governance of self-modification. It evaluates a logging infrastructure and retrospectively audits mostly routine forecasts. The candour about this is commendable, but does not supply the missing contribution.

**What would answer it:** implement an actual evidence-dependent capability transition and compare it prospectively with simpler governance under repeated, matched workloads and attacks.

### 2. The promotion criteria have no demonstrated connection to deserving the promoted powers — **major**

Predicting dataset freshness and completing forecast resolutions promptly need not indicate that an institution can safely administer greater authority. A system can perform these activities while remaining incapable of detecting malicious code changes. L361 acknowledges the missing welfare/safety link, but still says passing “certifies” timely, repair-free completion—more than the liveness theorem establishes.

The value statistic also credits joint dependence modelling, not necessarily better individual predictions (L186). Thus even the operational meaning of “predictive value” changes between the motivating claims and the tested quantity.

**What would answer it:** specify what each new capability requires, connect its evaluation tasks to that requirement, and measure whether passing predicts successful use of that capability.

### 3. The mathematical contribution is standard; the empirical novelty is predominantly a self-audit — **major**

The propositions are elementary constructions or direct applications of established results, as L89 concedes. Forecaster comparison, lagged outcomes, filtration mismatch, executable institutions, prospective protocol amendment and signed audit trails all have substantial precedents. The three novelty claims survive, at best, as a narrowly specified combination. No ablation establishes why that combination matters.

There is also a concrete literature error: L359 treats a log-score analogue of Murphy’s decomposition as open, although it already exists.

**What would answer it:** correct the literature, delimit the genuinely distinctive mechanism, and demonstrate an advantage attributable to that mechanism.

## 2. Soundness

### Proposition 1: correct, elementary, and narrower than “prospectivity”

**(a)** Prefix invariance follows immediately from a fixed deterministic predicate. It does not establish prospective substantive law: a later rule can impose consequences based on old acts without changing their original admission verdicts. Changing the checker is explicitly outside the result (L123).

**(b)** The backward collision argument is sound for the stated nonempty, position-numbered linked logs and an authenticated terminal hash. `HashChain.lean` genuinely proves the corresponding abstract collision implication. It proves neither cryptographic collision resistance nor authentication of the head.

The paper mostly states these qualifications correctly. The proposition supports immutable admission history, not the full legal analogy.

### Proposition 2: correct, with limited incentive and identity content

**(a)** The derivative proof and adjacent-grid-point claim are correct. `Propriety.lean` proves strict propriety on the open interval, not strict concavity or the grid result; L91–95 accurately discloses this.

**(b)** `kernel/check.py:82–83` implements comparison of declared principal strings. This prevents self-resolution by the same declared principal, not by the same real actor. Collusion, aliases and operator-controlled outcomes remain possible, as L139 acknowledges.

Most importantly, strict propriety does not imply truthful reporting under promotion rewards or mixture weights; L141 correctly withdraws that stronger claim.

### Proposition 3: sound under its stipulated null; not the full empirical procedure

The bounded-factor supermartingale argument is correct. The mixture telescoping identity and regret inequality are also correct for the specified posterior updates and fixed roster, including the base forecaster.

Three limitations are decisive:

1. **The filtration needs a more explicit definition.** L153 says “By (A)” the cutoff information contains none of the current block’s outcomes. Assumption (A), as written, orders *previous* blocks’ outcomes relative to current forecasts; it does not itself establish current-block blindness. State that requirement separately and define the increasing filtration, including resolution-membership information.
2. **Outcome selection changes the estimand.** With random resolved subsets, the null is about selected, timely recorded outcomes—not all issued forecasts. L157 and L173 correctly recognise this, but it substantially weakens institutional interpretation.
3. **The application drops the regret guarantee.** The recomputation updates weights across classes and from partly resolved sittings (L309). It therefore is not the posterior construction of Proposition 3(b), either within classes or globally. Predictable weights can still support part (a), but the empirical test does not inherit the advertised package of guarantees.

There is no apparent algebraic proof gap once those distinctions are respected.

### Remark: correct; it exposes an important change of target

Correlated factors cannot generally be multiplied merely because each is a valid cutoff-time bet. Freezing stakes is insufficient. The conditional-independence qualification is appropriate.

However, the block mixture can beat the baseline solely by assigning probability to dependence. With equally weighted constant forecasts \(0.95\) and \(0.05\), each marginal is \(0.5\), yet their mixture assigns much more probability than an independent \(0.5\) baseline to concordant outcomes. That is legitimate joint forecasting, but not evidence of improved individual-event forecasts. L186 acknowledges this; the abstract should make it visible.

### Example: reproduced, but deliberately outside the full construction

I obtained:

| Setting | Per-event crossings | Block crossings |
|---|---:|---:|
| Shared outcomes, \(n=20\), 4,000 runs | 13.25% | 0 |
| Shared outcomes, \(n=50\), 2,000 runs | 50.35% | 0 |
| Independent outcomes, both settings | 0 | Not computed |

The drift is approximately \(-0.1202\), as claimed. The example successfully refutes a general validity assertion for per-event betting. It does not estimate the reference implementation’s actual false-positive rate, and does not instantiate Proposition 3’s roster. Both distinctions should accompany any headline use of it.

### Proposition 4: correct theorem; incomplete operational liveness construction

The stake bound and conditional-expectation argument are correct. The restart inequalities are standard and correct; independent windows are an illustrative special case, not an assumption justified for this institution.

The unresolved issue is L194: simultaneous items require batching, but the paper leaves the comparable unit for expiries and batches open. This is part of the proposed mechanism, not merely an implementation detail. Moreover, the implementation scores simultaneous items sequentially. My check confirms 190 of 641 items share timestamps: 188 expiries and two batches.

Sequential scoring can be valid under the stronger, resolution-order conditional null. Timestamp ties alone do not prove invalidity. But the paper has not supplied a completed block construction connecting its preferred liveness interpretation to deployment.

Finally, rejecting “never better than \(p_0\)” does not certify reliable performance in the current window or future use of authority.

### Proposition 5: correct but nearly tautological

The intersection–union argument is valid, without independence. It controls erroneous promotion when an entire component null holds; it does not establish current competence, effect size or safety.

`Conjunctive.lean` proves the set-inclusion argument conditional on supplied crossing bounds. It does not verify either component process, the promotion code, or the exact-check conditions.

### Proposition 6: conditional specification, not an implemented replay guarantee

**(a)** Restates the admission condition.  
**(b)** Describes historical dispatch under a trusted current judge.  
**(c)** Correctly denies extrapolation beyond the finite replay inputs.

The material implementation gap is explicit: CI exercises three of 706 replay rows; the full condition depends on a reviewer session (L224). Consequently, this is not a mechanically enforced guarantee for the deployed evaluator-change path.

Overall, the Lean sources support the narrower claims listed in L91–95. They do not establish end-to-end correctness of the institutional mechanism. The strongest soundness concern is the gap between correct conditional mathematics and the unfinished, differently implemented operational protocol.

## 3. The evidence

**The numerical headline reproduces; its inferential strength does not become prospective through recomputation.** I obtained:

- 2,820 implementation-selected events;
- 476 completed sittings, four pending, five classes;
- pooled final wealth approximately \(19{,}930,\ 11{,}090,\ 3.009,\ 1.159,\ 1.022\);
- thresholds \(40,\ 120,\ 240,\ 400,\ 600\);
- no per-dataset running maximum above 1;
- implementation wealth \(1.51983\times10^{60}\);
- cutoff-restricted per-event ablation \(2.492\times10^{58}\);
- unsplit block ablation \(1.739\times10^{10}\).

The defensible conclusion is therefore the stated descriptive contrast between comparators.

**Forking paths remain consequential.** Four protocol rules changed during revision (L305). Stability across those reported alternatives is useful sensitivity evidence, not a selection-adjusted error guarantee. The overall claim cannot inherit a nominal 5% level from a procedure chosen after observing its record. L305 says this correctly; “the valid test” in the abstract and conclusion obscures it.

**Prospectivity also changed inside the implementation.** C1b opened at seq 188, but its cap was subsequently raised at seq 197 from 6,200 to 6,900. `SPEC.md` records this as a finding against pre-statement; the C1b brief amends criterion 3 accordingly. This qualifies the general presentation of windows as criteria committed before opening (L149). It does not invalidate the fixed-\(p_0\) calculation, but it matters to the governance claim.

**The baseline contrast is not an institutional success measure.** Dataset identity explains enough structure to eliminate the observed wealth growth. That exposes a weak comparator; it does not show that this institution detects weak evidence better than an ordinary statistical audit would.

**Selection and source control are substantial.** The statistic excludes 170 expired member events, including 168 resolved late, plus 19 resolved events without timely forecasts. Its guarantee concerns the selected statistic. Report outcome-sensitive missingness analyses and results by dataset and stream. The author also operates the freshness source (L369): signed entries authenticate reports, not independent outcomes.

**This is barely an ensemble experiment.** The selected events contain 2,795 reviewer forecasts and 12 builder forecasts; the reviewer stream overwhelmingly identifies one small model. Five prompt revisions make this an adaptive forecasting procedure. That can be statistically admissible with predictable forecasts, but prevents attribution to a stable model, aggregation, or institutional design.

**Liveness evidence is thin.** C1b’s crossing is nine successful items against a threshold derived from nine historical items using a different attribution rule. The paper correctly says \(6/11\) is a committed threshold, not a confidence bound. It consequently supports neither a statistically established improvement over incumbent performance nor a general estimate of reduced human burden.

The negative audit finding survives. The broader claim that this constitutes a successful test of the proposed institution does not.

## 4. Novelty and related work

### The three “new” claims

1. **Institutional powers granted by sequential tests:** potentially distinctive as a precise combination, but not demonstrated in the implementation. Self-amending rules, staged authority and statistical gates are separately established. The contribution needs an operational comparison, not merely their conjunction.
2. **Sequentially testing principal repairs with continuing wealth:** the intervention endpoint may be a useful application. Wealth continuation is ordinary optional-stopping discipline, however, and the endpoint’s relevance to authority remains unvalidated. I found no verified exact predecessor that would justify declaring this claim false.
3. **Governing builders before the governed agent exists:** this is principally a development methodology. SEA explicitly recommends deploying its governance gate first; Regimes §3.5 installs binding gates before widening the action space. Neither conclusively anticipates the exact claim, but both narrow its significance.

### Specific literature findings

- **A definite omission/error:** [Bröcker, *Reliability, Sufficiency, and the Decomposition of Proper Scores*](https://arxiv.org/abs/0806.0813), §2, Table 1 and equation (13), explicitly includes the logarithmic “Ignorance” score. Thus L359’s general claim that a log-score analogue is open is wrong. Sequential estimation of its components may remain open *for this protocol*.
- **Statistical comparison:** [Choe–Ramdas](https://arxiv.org/html/2110.00115), §4.4 and Appendix E, already develops weak-null comparisons and lagged forecasts. [Their filtration paper](https://arxiv.org/html/2402.09698v2), §4.2, addresses lagged forecast comparison directly. These are accurately cited, but deserve greater prominence than the elementary propositions.
- **Institutional precedents:** Pitt–Schaumeier–Artikis’s abstract confirms executable Event Calculus axioms for six Ostrom principles and an experimental testbed. AgentCity explicitly describes smart contracts as law and separates foundational, procedural and operational rules. These substantially anticipate the legal architecture.
- **Audit precedents:** add Schneier–Kelsey, [*Secure Audit Logs to Support Computer Forensics*](https://www.schneier.com/academic/archives/1999/05/secure_audit_logs_to.html), alongside recent agent papers. AgentBound already binds signed receipts to the governing policy and supports replay/provenance; the contrast at L345 needs an explicit operational definition of “source of law.”
- **Accurate major citations:** DGM reports the 20%→50% result and marker-based gaming example; Hyperagents’ source confirms the frozen boundary quotation; SEA confirms governance-first deployment and its conjectural composition guarantees; Red Queen confirms selective erasure of evaluator-dependent records.

No checked source establishes that the exact three-way combination is old. Equally, the paper has not established that combining these precedents yields a scientifically significant improvement.

## 5. Paragraph by paragraph

In order, the following paragraphs or table passages need changes; unlisted paragraphs are satisfactory for their stated purpose. Each entry gives the problem and a one-sentence replacement.

- **L14:** “Valid test” hides retrospective selection; replace with: “An exploratory blockwise audit reproduces pooled-baseline growth but finds none against dataset-specific frequencies.”
- **L24:** “Can be trusted only” asserts unsupported necessity; replace with: “We propose external, evidence-conditioned governance as one approach to self-modification.”
- **L26–36:** Two contribution lists repeat the thesis; replace with one list distinguishing the proposed mechanism, standard guarantees and retrospective audit.
- **L53:** The regulator theorem does not select an event fold; replace with: “We use event sourcing because it permits deterministic reconstruction and audit.”
- **L63:** Existing falsifiers do not test sufficiency; replace with: “The record exercises selected failure conditions but does not establish sufficiency.”
- **L71:** The 450-line figure risks standing for the monitor; replace with: “The Python validity kernel is 450 lines, within a substantially larger trusted enforcement system.”
- **L77:** Outcome independence is contradicted by the freshness application; replace with: “The design requires independent outcome production, a requirement the freshness stream does not satisfy.”
- **L79:** Pre-statement omits mid-window criterion revision; replace with: “The implementation uses staged criteria, with recorded exceptions including C1b’s cap increase.”
- **L111:** The Regimes contrast needs a narrower criterion; replace with: “Here the folded state includes authorisations determining admission of subsequent entries.”
- **L123:** Legal terminology exceeds prefix invariance; replace with: “The result preserves historical admission verdicts under a fixed checker.”
- **L129:** Forecast standing lacks a proposal-to-outcome mechanism; replace with: “The design scores submitted forecasts, but does not yet require a testable merit forecast for each proposed change.”
- **L149:** The unconditional precommitment description omits exceptions; replace with: “Windows are intended to precommit criteria, although C1b’s cap changed after opening.”
- **L153:** Assumption (A) does not imply current-block blindness; replace with: “Additionally require every current-block outcome to remain unrealised when its forecasts close.”
- **L184:** “Shows” should retain statistical uncertainty; replace with: “Crossing provides level-controlled evidence against the stipulated pointwise null.”
- **L188:** Simulation uncertainty is absent; replace with: “The seeded crossing estimates are 13.25% and 50.35%, with binomial uncertainty, versus zero observed block crossings.”
- **L194:** The liveness mechanism remains unspecified; replace with a complete definition of simultaneous-item grouping and comparable expiry units.
- **L206:** Numerical restart illustrations distract from the actual invalid process; replace with: “Continuing wealth avoids retry multiplicity only for an unchanged valid process and null.”
- **L224:** The enforcement gap belongs before the proposition; replace with: “The following replay property is specified, while deployment mechanically checks only three historical rows.”
- **L239:** “Removes” overstates deployment enforcement; replace with: “Complete compliance would prevent unmarked changes on the specified replay inputs.”
- **L252:** Priority language exceeds demonstrated importance; replace with: “We apply sequential testing to repair-free timeliness as a proposed authority criterion.”
- **L260–266:** Gall and Madison add analogy rather than evidence; replace with: “The proposed implementation order follows these explicit dependency constraints.”
- **L268:** The central implementation discrepancy appears too late; move its content into the contribution summary as: “Promotions have frozen layers but have not granted capabilities.”
- **L275:** Unrefused rules are not necessarily uninformed guesses; replace with: “Builder cases can supply useful rule-development evidence, supplemented by specifications and adversarial tests.”
- **L277:** Shared model class supplies little transfer evidence; replace with: “Builder trials exercise LLM-based workflows without establishing transfer to autonomous adversarial agents.”
- **L281:** The exact priority claim needs a defined comparison class; replace with: “We have not identified an earlier system combining builder subjection with the specified institutional promotion rule.”
- **L289:** Kernel size is not system auditability; replace with: “The validity kernel is small, while evaluator, workflows and evidence handling enlarge the trusted base.”
- **L303:** Every failure “illustrates” the design without discriminating evidence; replace with: “These incidents demonstrate recorded failure handling, not superiority over ordinary CI and review.”
- **L305:** Protocol robustness should not imply calibrated discovery; replace with: “Reported variants preserve the descriptive contrast, without accounting for protocol selection.”
- **L308:** Attrition is reported without substantive sensitivity; replace with: “We additionally report how outcome-dependent expiry could alter the comparison.”
- **L309:** The dropped guarantee deserves immediate emphasis; replace with: “This empirical process uses predictable weights but does not instantiate Proposition 3(b).”
- **L311:** Model counts need an attribution boundary; replace with: “The experiment primarily evaluates one changing small-model procedure, not diverse aggregation.”
- **L317:** The conclusion should remain exploratory; replace with: “The selected audit exhibits pooled-baseline advantage and no detected dataset-specific advantage.”
- **L319:** The dense ablation narrative belongs in a table; replace with: “Table X reports successive, non-causal ablations with their differing samples and scores.”
- **L321–325:** Literal falsifier accounting does not establish constructive validation; replace with: “Several founding tests were unexercised, altered in operational target, or triggered before forecasting became possible.”
- **L335:** Routine forecasting is not evaluation of the improvement process; replace with: “We test selected operational statistics rather than improvement of the governing process itself.”
- **L345:** “Source of law” is insufficiently operationalised; replace with: “Our distinction is that logged authorisation updates determine later entry admissibility.”
- **L359:** The claimed open decomposition already exists; replace with: “Log-score decompositions are established; their sequential use here remains to be specified.”
- **L361:** “Certifies” overstates both tests; replace with: “Passing provides evidence against lifetime pointwise nulls, not a guarantee of current repair-free operation.”
- **L375:** A market is unnecessary merely to expand a roster; replace with: “Roster expansion requires a specified prior or expert-entry mechanism and an updated guarantee.”
- **L385:** The conclusion promotes an exploratory audit into validation; replace with: “The contribution is a governance proposal and reproducible negative audit; its authority mechanism remains untested.”

## 6. Backing

### Wrong or unsupported claims established by checks

- **L149, L79:** Uniform pre-opening criteria are not an accurate implementation summary: `SPEC.md` §10 records C1b’s cap increase; its brief, criterion 3, identifies the post-opening push at seq 197.
- **L153:** The asserted current-block information exclusion does not follow from the stated (A); this is a specification omission, not a refutation of the conditional theorem.
- **L359:** A general log-score decomposition is not open: Bröcker’s Table 1 and equation (13) provide it.
- **L361:** Passing does not certify current timely, repair-free completion: Proposition 4 controls a lifetime null, and L208 explicitly allows inherited wealth.
- **L14, L385:** “Valid test” is unsupported if read as a calibrated claim for the complete retrospective research procedure; L305 expressly excludes protocol-choice multiplicity.
- **L24:** The necessity claim about trust is not established by Rice, Löb, the propositions, or the case history.

### Additional factual checks that passed

These are distinct checks, not twenty invented errors:

| # | Paper line | Evidence checked |
|---:|---:|---|
| 1 | 99 | Seven entry fields: `SPEC` §4. |
| 2 | 109 | Fourteen refusal codes: `SPEC` §9. |
| 3 | 125 | Builder powers: log seq 6. |
| 4 | 125 | Expanded builder powers: seq 34. |
| 5 | 125 | Herald merge-only key: seq 201. |
| 6 | 125 | Last-key guard: `kernel/check.py:84–87`. |
| 7 | 135 | Principal-based refusal: `check.py:82–83`. |
| 8 | 145 | Five subsequent prompt-file revisions: cited path history. |
| 9 | 190 | Eventwise weight/stake updates: `judge/value.py`. |
| 10 | 190 | Same-type resolution-order base: `judge/entries.py`. |
| 11 | 190 | Fourteen resolutions within one minute: seqs 550–563. |
| 12 | 194 | 641 items; 190 timestamp-sharing items: recomputed fold. |
| 13 | 218 | Historical evaluator dispatch: `SPEC` §10.15. |
| 14 | 224 | Replay table contains 706 rows. |
| 15 | 224 | CI replay indices 300, 400, 593: `pins/replay.py`. |
| 16 | 241 | C1 kernel-family limitation: commit trailers and revisions. |
| 17 | 247 | Repair predicate matches introduction at `879caf9`. |
| 18 | 268 | Nineteen key entries; fourteen before seq 188. |
| 19 | 283 | Builder/reviewer entries: 6,621. |
| 20 | 283 | Their forecasts/resolutions: 5,919, including 5,811 stream entries. |
| 21 | 283 | Their proposals: 702, including 627 titled stream batches. |
| 22 | 289 | Python kernel: 138 + 172 + 140 = 450 lines. |
| 23 | 297 | Nine successful items; exact wealth \(214358881/8398080\). |
| 24 | 303 | Cited attributed acts CSV contains nine repair rows. |
| 25 | 311 | 2,887 freshness forecasts; 2,869 name the stated model. |
| 26 | 369 | Operator’s three forecasts concern `world.assize`, not freshness. |

The principal empirical numbers are unusually reproducible. The objection is their scope and relevance, not fabricated arithmetic.

## 7. Recommendation

**Reject.** The changes that matter most are:

1. Implement and prospectively evaluate evidence-conditioned capability grants.
2. Establish whether the criteria predict competent, safe use of the granted powers.
3. Complete the liveness batching protocol and distinguish all three statistical procedures: theorem, deployment and retrospective audit.
4. Register a fresh comparison using stronger baselines, independent outcomes and explicit missingness treatment.
5. Correct the decomposition claim, narrow novelty language, expose mid-window exceptions, and shorten the legal analogies.

The reproducible negative audit is valuable. It is not yet sufficient evidence for the paper’s proposed governance mechanism.

RECOMMENDATION: reject
exit=0
```

