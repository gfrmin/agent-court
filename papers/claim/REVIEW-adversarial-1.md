# Adversarial read 1 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, briefed as the most demanding referee a top venue could assign and told to make the strongest fair case for rejection. It was barred from the earlier reports. The issue is renavondata/opencode-runner #1394, run from 13:32Z to 13:45Z on 26 November.
- **Text read:** draft 24, at `3e46dbf`.
- **Verdict:** **reject**. The reader found no fault in the mathematics, and the numbers reproduce. Its case concerns what the evidence shows, and how the paper is positioned.
- **Draft 26** answers what can be answered in a paper. It also carries the claim session's own paragraph-by-paragraph pass (`07-paragraph-review.md`). The disposition comes first; the report follows verbatim.

## Disposition

| Objection | Verified? | What draft 26 does |
|---|---|---|
| 1. The central mechanism, powers by test, is not demonstrated ("fatal to the present validation claim") | Yes: the implementation grants powers as windows open (§5.1) | The paper takes the reader's second remedy and narrows its claims. §1 now says it does not validate the institution: the record shows the ingredients running and one test exposing the institution's own weak evidence, not that granting powers by test works or predicts useful autonomy. The abstract now says the implementation has not yet tied its powers to these tests. The first remedy, building test-conditioned grants and running a controlled comparison, is work for the implementation, not this paper (§8, "No controlled comparison"). |
| 2. Passing certifies less than institutional fitness | Yes | New §8 paragraph, "What passing certifies". The link from passing to the principal's welfare or safety is the design's hypothesis, still untested. |
| 3. Novelty under-positioned; missing electronic institutions, AgentCity, and filtrations | Yes: each source checked | New §7 paragraph on electronic institutions: Artikis, Sergot & Pitt 2009; Artikis 2012; Pitt, Schaumeier & Artikis 2012; Ruan & Zhang 2026 (AgentCity). Choe & Ramdas 2024b, on combining evidence across filtrations, now frames the Remark and appears under "Testing by betting". Contribution 2 says "none mathematically new". |
| The value null is the *strong* null in Choe & Ramdas's terms, not the weak one | Yes: their abstract defines the weak null as advantage "on average (rather than always)" | Corrected, with what rejecting it does and does not say. |
| The per-event ablation dated evidence by the timely-resolved subset | Yes | `block_on_log.py` now dates each sitting by its whole completion. The figure is unchanged at the precision shown (2.492e58), as the reader also found. |
| SEA accumulates evidence across rounds | Yes: SEA §4.4, per-version | §7 is qualified: SEA accumulates each version's evidence across rounds. What is particular here is that one institutional test's wealth continues across failed windows. |
| The Remark should foreground the filtration mismatch, not simultaneity | Yes | Reworded; Choe & Ramdas 2024b cited. |
| Prop. 1 overinterpreted as Fuller's prospectivity | Fair | Now "one computational ingredient of Fuller's prospectivity". The kernel does not interpret substantive law, and checker changes lie outside the proposition. |
| Forking paths in the retrospective protocol: give the inventory | Yes | §6 lists the four rule changes made during revision. In every version both pooled classes crossed (class 1: 1.99e4–2.23e4; class 2: 1.11e4–1.62e4), and the per-dataset wealth never exceeded 1 wherever it was computed. `04-selfcheck.md` is now an ancillary file. |
| p₀ is a fixed threshold, not a bound on the incumbent's rate | Yes | Said in §5.2. |
| Shared policy class is weak evidence of transfer | Yes | §5.2 now says reliability transfer is not established either. |
| Integrity needs an authenticated anchor | Yes | §3: "relative to an authenticated head (Proposition 1)". |
| "Cannot merge"; "the design runs"; "either … is lacking"; per-edit gates answer a different question | Yes | Each reworded. |
| Non-rejection gives no bound | Yes | Added. |
| Line-by-line suggestions that would weaken backed claims (e.g. "we investigate … as one approach") | — | Not taken. The paper keeps its argued thesis ("We argue …"), marked as argument rather than finding, per Guy's instruction to state the strongest backed claim. |

## The report (verbatim)

**Recommendation: reject.** The numerical audit is reproducible and useful. The paper nevertheless provides substantially better evidence for a forecasting-baseline failure than for its proposed institution.

Line references below refer to `draft.md` at the specified commit; implementation references refer to `e580b64`. I inspected all seven Lean source files and their README, but did not build them under the no-write constraint.

## 1. The case for rejection

### 1. The central mechanism has not been demonstrated — **fatal to the present validation claim**

The advertised contribution is an institution whose powers are granted only after tests on its own performance (lines 14, 27, 34). The implementation does the reverse: powers arrive when windows open, and promotion freezes a layer and opens another window (264). Neither historical promotion was subject to the subsequently installed promotion evaluator (214). No governed self-modifying agent exists (31, 295).

Consequently, the case does not exercise the proposed authority-granting mechanism, its resistance to strategic applicants, or its effect on self-modification. Thousands of forecasting entries cannot substitute for that missing experiment.

**What would answer this:** implement promotion-dependent capability grants and compare repeated, adversarially exercised runs against simpler governance, measuring useful work, human effort, failures, and overhead. Alternatively, narrow the paper to a retrospective audit and remove institutional validation from its contribution claims.

### 2. The statistical guarantees certify much less than institutional fitness — **major**

The value null requires nonpositive conditional advantage at **every** block (169). Rejecting it establishes neither positive average advantage nor continuing competence. Liveness measures timely, repair-free completion, including completion of worthless work (353). Old wealth can authorize a later window (204), and the conjunctive guarantee is per layer, without lifetime familywise control across layers (210).

These qualifications are mostly disclosed. Their cumulative consequence is not confronted: an institution can satisfy the mathematical promotion conditions without establishing that granting it additional powers improves the principal’s welfare or safety. Formalizing standard probability lemmas does not supply that missing connection.

**What would answer this:** specify the operational promotion claim, choose estimands that bear on it, and demonstrate that passing predicts subsequent useful autonomous performance. Distinguish historical evidence, current competence, and authority-specific risk.

### 3. The incremental contribution is insufficiently established — **major**

The mathematical ingredients are explicitly standard (89). Executable institutional rules, institutional self-amendment, event-sourced agent histories, and statistical deployment gates all have substantial precedents. Important related work is missing, and the paper misidentifies its null relative to its closest statistical reference (180).

The remaining novelty may be the particular combination of repair accounting, sequential evidence, and institution-first development. That is a plausible design contribution, but the paper supplies neither a compelling comparative argument nor evidence that the combination earns its considerable procedural complexity.

**What would answer this:** a precise comparison with electronic-institution and adaptive-governance research, corrected statistical positioning, and an experiment isolating what the proposed combination buys.

## 2. Soundness

### Proposition 1: prospectivity and hash binding

**The stated fixed-checker results are correct.** Part (a) is prefix causality, essentially definitional. Part (b)’s backward collision argument correctly handles unequal lengths through position numbering; `HashChain.lean` captures this abstraction.

The interpretation is stronger than the theorem. Calling this “Fuller’s prospectivity” (123) conflates invariant prefix evaluation under a fixed predicate with prospective legal change. The kernel records charter digests but does not interpret the charter’s substantive law (107). Changes to checker code are outside this proof. Hash binding also requires an authenticated reference head; it supplies neither external completeness nor non-equivocation without checkpointing.

**Verdict:** sound, elementary, institutionally overinterpreted.

### Proposition 2: propriety and self-judgment

Part (a), including the adjacent-grid maximizer statement, is correct. Lean proves strict propriety, not strict concavity or the grid result, as accurately disclosed at 91–95.

Part (b) correctly describes `kernel/check.py`: the stored forecast proposer is compared with the resolution proposer after signature verification. It prevents equal principal identifiers from resolving their forecasts, not one real actor using distinct principals. The paper acknowledges this at 139.

The relevant incentive limitation is substantial: expected-score propriety does not establish truthful reporting when rewards are promotion, mixture weight, or authority (141). Thus propriety does not justify the broader institutional incentive story.

**Verdict:** sound; the useful guarantee is narrower than “no self-judgement” suggests.

### Proposition 3: value

Part (a) is the standard predictable bounded-betting argument. Part (b) is the standard mixture telescoping identity; including the baseline establishes its second inequality. I find no algebraic gap.

Four scope restrictions matter:

1. The null is **strong**, not the “weak” null attributed to Choe–Ramdas at 180. Their paper explicitly distinguishes pointwise conditional dominance from average dominance.
2. Joint product-mixture advantage can reward dependence modeling without better eventwise marginal predictions; the Remark correctly acknowledges this.
3. Outcome-dependent resolution changes the target population. The conditional-on-resolution formulation at 153–169 preserves a narrowly stated theorem, not inference about all issued forecasts.
4. The empirical posterior updates differ from the telescoping construction, so the empirical process lacks part (b)’s regret guarantee, as 303 concedes.

`Mixture.lean` proves algebra for positive block likelihoods; `Wealth.lean` proves a generic wealth theorem under supplied bounds, measurability, predictability, and null assumptions. Neither establishes that the empirical protocol satisfies those assumptions.

**Verdict:** mathematically sound; mislabeled null and limited operational meaning.

### Remark

The central warning is correct: multiplying correlated factors need not preserve validity merely because each has nonpositive conditional mean at the forecast cutoff. The conditional-independence qualification is also appropriate.

“Simultaneous resolution” is an imprecise shorthand: the problem is mismatched information sets, not timestamp equality. Conversely, sequentially recorded outcomes can have the same defect when earlier records reveal information excluded from the forecast-time null.

**Verdict:** correct, but should foreground the filtration mismatch rather than simultaneity.

### Example

I reproduced:

- \(n=20\): 530/4,000 per-event crossings, versus zero block crossings;
- \(n=50\): 1,007/2,000 per-event crossings, versus zero block crossings;
- both independent-outcome controls: zero per-event crossings.

The conditional drift is approximately \(-0.1202\), as stated. The script properly distinguishes this randomized forecaster from Proposition 3’s full mixture.

This establishes a counterexample to the per-event betting protocol, not the frequency of false promotion in the deployed institution. The paper mostly respects that distinction.

**Verdict:** correct and useful.

### Proposition 4: liveness and continuation

The stake bound and supermartingale proof are correct for the stipulated adapted observations. Restart bounds are correct worst-case bounds; generally they can be written \(\min(1,k\alpha)\).

The simultaneous-item repair remains underspecified: line 190 proposes averaging but immediately says an appropriate unit must first be determined. Thus the paper has a generic theorem before it has a complete deployable liveness protocol.

Committing \(p_0\) beforehand makes it a legitimate fixed threshold; it does **not** establish superiority to an incumbent’s unknown true rate. The nine-item historical estimate supplies no such comparative uncertainty guarantee.

**Verdict:** sound conditional theorem; incomplete measurement specification.

### Proposition 5: conjunctive promotion

Correct intersection–union reasoning. Dependence between components requires no correction. `Conjunctive.lean` proves the stated set-inclusion consequence from assumed component bounds.

But “either value or liveness is lacking” (210) must mean the precisely defined pointwise nulls, not ordinary institutional inadequacy. Exact extra gates cannot repair an invalid component process.

**Verdict:** sound and nearly immediate.

### Proposition 6: replay-bound change

Part (a) restates its admission condition; part (c) states finite testing’s limitation. Part (b) describes historical evaluator dispatch rather than deriving an invariant under arbitrary future judge changes.

The paper accurately discloses that CI replays only three rows and that the current judge drives historical assessment. The proposition is therefore a specification-level conditional guarantee, not a demonstrated comprehensive code-enforced replay guarantee.

**Verdict:** correct as qualified, but mostly definitional.

Overall, I found no fatal mathematical proof gap. The weakness is the distance between the correct conditional lemmas and the institutional conclusions.

## 3. The evidence

### The principal numerical result survives recomputation

The ancillary script reproduces all headline quantities:

| Quantity | Recomputed |
|---|---:|
| Implementation events | 2,820 |
| Completed/pending sittings | 476 / 4 |
| Lag classes | 5 |
| Pooled-baseline final wealth, classes 1–2 | \(1.993\times10^4,\ 1.109\times10^4\) |
| Corresponding thresholds | 40, 120 |
| Per-dataset running maxima | All 1 |

This supports the descriptive conclusion that the impressive original evidence depended on an inadequate pooled comparator.

### It is not a retrospectively selection-adjusted discovery

Line 299 appropriately acknowledges post-record protocol selection. The paper should provide the actual search history: considered cutoffs, deadlines, block definitions, baseline variants, scoring rules, exclusions, and stopping dates. Fixed-protocol anytime validity does not cover choosing that protocol after examining its results.

The large pooled crossings remain informative descriptively. Their magnitude does not supply an unspecified selection correction.

### An auxiliary “nothing leaked” claim is incorrect

In `block_on_log.py`, `run()` dates prior per-event contributions using:

`max(e["done"] for e in block)`

Here `block` contains only the **ultimately timely-resolved subset**, not the whole sitting. Whether that subset is complete can depend on future resolutions.

Concrete witness: the 8 November 02:00 sitting has five timely resolutions completed by 03:13:53 and one event expiring at 07:00. The ablation uses those five contributions at the 04:00 cutoff, although a future timely resolution would change that historical inclusion decision.

Waiting for whole-sitting completion gives \(2.4921561\times10^{58}\), unchanged at the paper’s displayed precision. This does not overturn the main lag-class results, but line 313’s cutoff-only claim and ablation accounting need correction.

### Other evidential limitations

- **Baseline:** pooled dataset frequencies discard readily available dataset identity; defeating them is a low bar. The negative per-dataset test supplies no equivalence conclusion or quantitative bound on remaining skill.
- **Forecaster:** almost all evidence concerns one mini-model procedure. Predictable prompt adaptation is statistically permissible, but defeats an interpretation as evidence for diverse aggregation or a stable, independently specified model.
- **Outcome source:** the author operates the dominant data source. This is a concrete conflict in the proposed separation between forecaster and world, not evidence of manipulation. Independent outcome acquisition is needed.
- **Burden:** repair accounting omits off-platform assistance, exempts substantial categories of operator action, and depends on attribution rules modified during the historical evaluation.
- **Single case:** no controlled comparison establishes reduced oversight, useful construction work, or improved safety. Routine stream traffic dominates the supposedly self-governing construction record.

The defensible finding is a reproducible failure analysis of one record—not validation of the institution.

## 4. Novelty and related work

Three missing comparisons are particularly important:

1. **Executable self-governing institutions.** Pitt et al., [*Algorithmic Self-Governance and the Design of Socio-Technical Systems*](https://ceur-ws.org/Vol-1283/paper_33.pdf), §3.2, already distinguish operational, collective-choice, and constitutional-choice rules and computational institutional adaptation. Their cited Pitt–Schaumeier–Artikis work predates this paper by over a decade. Nomic and Tezos alone are insufficient institutional background.

2. **Agent legislation as executable law.** Ruan and Zhang’s [AgentCity, arXiv:2604.07007](https://arxiv.org/abs/2604.07007), §§3–3.3, explicitly makes agent-produced smart contracts the law governing agents and separates foundational, procedural, and operational rules. It does not establish this paper’s sequential promotion mechanism, but it materially narrows the claimed architectural distinction.

3. **Filtration-sensitive e-processes.** Choe and Ramdas, [*Combining Evidence Across Filtrations*, arXiv:2402.09698](https://arxiv.org/abs/2402.09698), addresses precisely why evidence valid under a coarser filtration need not remain valid under a finer one, including multi-step forecaster comparison. It should frame the block discussion.

For the three novelty claims:

- **Layerwise institutional authority (34):** the exact sequential-testing combination may be new; neither its implementation nor its advantage is demonstrated.
- **Sequential repair testing with continued wealth (35):** plausibly the narrowest distinctive contribution. Its measurement validity and usefulness need evidence; the underlying betting and continuation principles are standard.
- **Builders governed before the agent (36):** potentially a distinctive development discipline, but presently closer to a methodological proposal than an established safety result. Shared model class does not establish transfer to persistent, strategically adversarial agents.

The audit-log discussion already credits substantial predecessors. Regimes genuinely supplies event-sourced improvement history; this is not a neglected discovery attributable to the present paper.

One further qualification: SEA §4.4 explicitly says that **per-version normal-mixture sequences accumulate value evidence across rounds**. Line 333’s blanket exclusion of evidence continuation needs to distinguish that mechanism from this paper’s unchanged institutional-window process.

I did not establish an exact predecessor to the three narrowly combined claims. Missing antecedents justify narrower positioning, not an accusation that the entire design was previously published.

## 5. Paragraph-by-paragraph corrections

The following are the paragraphs requiring revision, in reading order; omitted paragraphs are acceptable. Each entry gives the problem and a one-sentence replacement.

| Lines | Problem → better version |
|---|---|
| 14 | Overloaded abstract obscures the unimplemented mechanism → “We propose sequentially tested institutional governance and retrospectively audit a partial implementation.” |
| 20 | Benchmark and survey scope are compressed → “DGM improves a specified SWE-bench evaluation, while a frozen arXiv search frame finds limited repeated-loop auditing.” |
| 24 | “Only” asserts unsupported necessity → “We investigate an external institution as one approach to governing self-modification.” |
| 27 | Design and implementation are insufficiently separated → “The proposed authority-granting design extends beyond the mechanisms currently deployed.” |
| 28 | The contribution sounds mathematically stronger than §4 admits → “We assemble six standard or construction-level guarantees and formalize selected abstractions.” |
| 29 | The empirical contribution should name its scope → “A retrospective audit exposes baseline sensitivity and departures from the design.” |
| 33–36 | Priority claims lack operational comparisons → “Our proposed contribution is this particular combination, compared explicitly with its nearest antecedents.” |
| 43 | “After it stops being watched” is an unevaluated assumption → “The intended agent operates persistently, including between operator inspections.” |
| 49 | Classical obstacles do not select this architecture → “Rice and Löb limit particular verification ambitions but leave multiple external-assurance designs available.” |
| 53 | Good-regulator theory does not justify event sourcing → “We choose event sourcing for deterministic reconstruction and auditability.” |
| 63 | The catalogue mixes motivation with assurance → “These sources motivate design choices without establishing their necessity or sufficiency.” |
| 69–81 | Several table arrows overstate what citations entail → “Present each response as an engineering choice, with its assumptions and alternatives.” |
| 83 | Integrity needs an authenticated anchor → “Relative to an authenticated head, the chain binds recorded history but does not establish completeness.” |
| 111 | The Regimes contrast is too categorical → “Our proposed extension makes prospective authorization state explicit alongside event-sourced agent state.” |
| 123 | Prefix causality is equated with legal prospectivity → “Proposition 1 establishes fixed-predicate prefix invariance, one computational ingredient of prospectivity.” |
| 125 | “Cannot merge” exceeds log authorization → “The kernel refuses merge entries lacking an appropriately empowered signing key.” |
| 143 | The regret fact is standard and already repeated → “Uniform-prior Bayesian aggregation supplies the standard \(\ln K\) log-loss regret bound.” |
| 145 | One named model does not identify one stable procedure → “The record principally evaluates a mini-model with an adaptively revised prompt.” |
| 153 | Too many protocol choices inhabit one paragraph → “Define membership, information, missingness, and lag assignment separately before stating the null.” |
| 180 | The null is mislabeled → “This is pointwise conditional dominance, called the strong null by Choe–Ramdas.” |
| 182 | Timestamp language obscures the actual defect → “Validity depends on the information conditioned on between factors, not simultaneous recording itself.” |
| 190 | Liveness batching remains unfinished → “Specify the complete simultaneous-item unit and update rule before claiming an executable protocol.” |
| 202 | Continuation versus edit-gating compares different targets → “Continuation controls one unchanged null; changed adoption questions require their own error accounting.” |
| 210 | Ordinary “lacking” is stronger than the formal null → “The guarantee concerns the union of the two stated pointwise nulls.” |
| 235 | The court/optimizer contrast substitutes metaphor for analysis → “Replay preserves specified historical outputs but supplies no general assurance on future evaluator behavior.” |
| 243 | Fixed typing is mistaken for a stable burden measure → “Exemptions, attribution, and taint removal must be reported alongside the unchanged typing predicate.” |
| 248 | Priority is insufficiently substantiated → “We propose using repair-free completion as a sequential authority criterion.” |
| 262 | Historical analogies repeat the dependency argument → “The ordering follows the dependencies of this particular architecture.” |
| 264 | The decisive implementation discrepancy is buried → “No capability grant has yet been made conditional on passing the proposed tests.” |
| 272 | Prior commitment is confused with incumbent comparison → “The historical estimate supplies a precommitted threshold, not a confidence bound on incumbent performance.” |
| 273 | Shared policy class is weak transfer evidence → “Builder use exercises usability and accidental-failure handling, not adversarial-agent robustness.” |
| 277 | Priority and traffic accounting obscure the main limitation → “Construction-specific governed work is a small minority of the recorded activity.” |
| 283 | “The design runs” is inaccurate shorthand → “A partial implementation runs publicly with a 450-line Python kernel.” |
| 299 | Acknowledgment lacks a protocol-search inventory → “Enumerate all explored analysis choices and reserve confirmatory interpretation for new data.” |
| 311 | Non-rejection risks sounding like absence of skill → “This test detects no incremental advantage and supplies no equivalence bound.” |
| 313 | Cutoff-only ablation claim is incorrect → “Correct prior-score availability and report these as descriptive, noncausal ablations.” |
| 315 | Falsifier accounting is too favorable to altered tests → “Two original falsifiers remain untested as written, and one has been literally triggered.” |
| 331 | Institutional adaptation literature is too narrow → “Compare adaptive managers with research that also adapts institutional and constitutional rules.” |
| 333 | Evidence-continuation exclusion is overbroad → “Distinguish SEA’s across-round evidence accumulation from continuation of an unchanged institutional test.” |
| 351 | The open problem lacks a precise target → “Specify whether the desired gate tests average score advantage, calibration, resolution, or future utility.” |
| 359 | Source ownership is not proof of causal performativity → “Operator control creates an outcome-influence risk that requires independent measurement.” |
| 375 | Conclusion again outruns the evidence → “The case validates a reproducible audit, while the proposed authority mechanism awaits implementation and evaluation.” |

## 6. Backing

### Claims found wrong or unsupported

- **180:** “weak” null attribution is wrong; [Choe–Ramdas, arXiv:2110.00115](https://arxiv.org/abs/2110.00115), §§2 and 4.4, explicitly distinguishes the paper’s strong null from average-dominance weak nulls.
- **313:** the auxiliary cutoff-only stake claim is unsupported by its implementation; the resolved-subset availability counterexample is given above.
- **333:** the exclusion of across-attempt evidence continuation needs qualification; SEA §4.4 explicitly accumulates per-version evidence across rounds.
- **14, 27, 283:** treating the deployed system as an instance of test-conditioned authority granting is contradicted by log grant timing and the admission at 264.
- **123:** full legal prospectivity is not established by fixed-\(V\) prefix invariance; the kernel does not interpret substantive charter amendments.
- **248, 277:** the precise priority claims remain unestablished; the related-work comparison omits directly relevant institutional research.
- **359:** causal performativity is not established merely by source ownership; Perdomo et al. define predictions influencing the target distribution.

### Additional factual checks

Most concrete implementation claims were accurate. These **24 checks** provide a positive audit trail rather than manufacturing discrepancies:

| Paper line | Claim checked | Evidence/result |
|---|---|---|
| 20 | DGM 20%→50%; marker removal | DGM full text confirms both; benchmark scope needs clarification. |
| 20 | Hyperagents’ fixed boundary | Appendix A.5 confirms evaluator/data restrictions and parent-selection exception. |
| 20 | 114 studies, 90 RSI, 22% reruns | Census full text confirms the counts within its search frame. |
| 55 | Evidence truth is not checked | SPEC §10.15 and `promotion_checks` confirm hash/presence attestation. |
| 99 | Seven canonical entry fields | SPEC §4 and kernel shape checking agree. |
| 107 | Charter digests are not admission law | `check_entry` records them without interpreting their text. |
| 109 | Fourteen refusal reasons | SPEC §9 confirms the closed list. |
| 125 | Last-key guard | `check_entry` rejects loss of all `key` powers. |
| 129 | Forecast grid | SPEC §5 requires integer probabilities 1–999. |
| 135 | Principal-based self-resolution refusal | `check_entry` compares forecast and resolution proposers. |
| 145 | Five prompt revisions after introduction | Six file-history commits, including initial introduction. |
| 186 | Eventwise weights/stakes | `judge/value.py` updates both inside the resolution loop. |
| 186 | Same-batch baseline updates | `resolution_rates` updates counts after every resolution. |
| 190 | 641 items; 190 timestamp-sharing | Recomputed; 188 expiries and two batches. |
| 220 | 706 replay rows; three CI samples | Replay JSON and `pins/replay.py` confirm both. |
| 237 | Shared-family C1 kernel provenance | Commit trailers support the disclosed limitation; Codex attribution is incomplete. |
| 264 | 19 key entries; 14 before promotion | Counted directly from the log. |
| 277 | 6,621 builder/reviewer entries | Recounted; also 5,919 forecasts/resolutions and 702 proposals. |
| 283 | 450-line Python kernel | 138 + 172 + 140 physical lines. |
| 291 | Nine-item C1b wealth | Recomputed exactly as \(214358881/8398080\). |
| 302 | Sittings and exclusions | Reproduced 476 completed, four pending, 170 expired, 19 nonmembers. |
| 305 | Dominant party/model counts | Reproduced 2,795 reviewer, 12 builder; 2,869 named mini-model forecasts. |
| 308–309 | Baseline-dependent wealth | Reproduced all class totals and maxima. |
| 318 | Repairs reduced 81→9 by attribution | Raw and attributed CSV class counts confirm the reduction. |

## 7. Recommendation

**Reject**, with the following priorities:

1. Implement and evaluate actual test-conditioned authority grants.
2. Replace institutional-fitness rhetoric with precisely justified promotion claims.
3. Correct the null attribution and auxiliary ablation’s information timing.
4. Run a preregistered, independently measured comparison against simpler governance.
5. Add electronic-institution and filtration-combination antecedents; narrow priority claims.
6. Move implementation history and repeated philosophical motivation to appendices.

The strongest publishable core is presently the reproducible audit of baseline weakness and filtration errors. It does not yet establish that the proposed institution deserves additional authority.

RECOMMENDATION: reject
exit=0
```

