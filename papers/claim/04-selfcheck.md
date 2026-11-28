# Self-check of draft 2 — every factual claim against its source

*Claim session, 25 November 2026. The sources were `renavondata/jack` at `origin/main` `e580b64` (log to seq 7809), gfrmin/agent-court at `007a007`, and the arXiv and Crossref records as fetched today. "✓" means checked against the source named. "Fixed" means the draft was wrong and has been corrected.*

## Claims about the implementation

| § | Claim | Source checked | Result |
|---|---|---|---|
| 4.1 | An entry has seven fields: `parent` is the SHA-256 of the previous line, `sig` is Ed25519 | SPEC §§3–6 | ✓ |
| 4.1 | The state holds keys, the charter in force, the trusted base and forecasts | SPEC §7 | ✓ |
| 4.1 | There are fourteen reasons for refusal; the first refusal is the verdict | SPEC §1, §9 | ✓ |
| 4.1 | An activation height must exceed the `amend` entry's own seq | SPEC §7 ("must exceed its own `seq`") | ✓ |
| 4.1 | The kernel never reads a clock; `ts` may not decrease | SPEC §4, §7 | ✓ |
| 4.1 | Builder keys hold proposal, spec_conflict, forecast and resolution | seq 34 | ✓ |
| 4.1 | The herald's key holds `merge` alone | seq 201 | ✓ |
| 4.1 | Only guy-master holds key, push, amend and decision | all 19 `key` entries and seqs 0, 1, 33 | ✓ |
| 4.1 | A `key` entry that would remove the last key power is refused | CHARTER A2.5; SPEC §7 | ✓ |
| 4.2 | Probabilities are per mille, 1–999 | SPEC §5 | ✓ |
| 4.2 | `self_judged` is judged by principal | SPEC §7; §8, step 8a | ✓ |
| 4.3 | A window ends at its stated end, at `promote`, or at a veto | CHARTER A5.1, A6.1 | ✓ |
| 4.3 | The judge refuses an unlawful `promote` after the installing push | SPEC §10, item 15; push at seq 7281 | Fixed: the draft now says "since seq 7281", because promotions 188 and 337 are not judged |
| 4.3 | The stake formula for value | CHARTER A4.4; `judge/value.py` `stake()`, `factor()`, `difference()` | ✓ The code computes Σx/(2+Σx²), capped at 1−1/(n+2) |
| 4.3 | The roster includes the base-rate forecaster; an abstainer is scored as the base rate | `judge/value.py` `roster_at()` (appends `"base"`), `value()` (`g["forecasts"].get(k,(None,b))`) | ✓ |
| 4.3 | The implementation bets per event in resolution order | `judge/value.py` `value()` | ✓ |
| 4.3 | Liveness stake and null | CHARTER A4.2, A4.3 | ✓ |
| 4.3 | A failed window continues the same wealth | CHARTER A4.1 | ✓ |
| 4.3 | A repair taints the writs open at its entry; a tainted item has Y = 0 | BRIEF-C2a-3 §The late-report rule | ✓ |
| 4.4 | Trusted-base rules: items 1, 11 and 12 | SPEC §10 | ✓ |
| 4.4 | The evaluator changes only by a replay table and marked lines | SPEC §10, "The promotion evaluator"; grant seq 6851 (it marks rows 593–705); push seq 7281 | ✓ |
| 4.4 | Two kernels, Python and Go; the second written from the SPEC by another family; CI fails on disagreement | CHARTER §5; README; REPORT §8.2 (kernel2 by Codex) | ✓ |
| 4.5 | Acts are typed as decision or repair by type and key, fixed in advance | CHARTER §7 | ✓ |
| 4.5 | A window fails on an off-log repair | BRIEF-C2a criterion 7 (REPORT, C2a §1 table) | ✓ |
| 5.1 | The ledger comes before the clerk | CHARTER A3.1 | ✓ |
| 5.2 | Quotation from A2.10 | CHARTER.md lines 298–300 | ✓ verbatim |
| 5.2 | Named attacks are simulated before any model touches a layer | CHARTER §6, "Simulator first" | ✓ |
| 5.2 | Builder, reviewer and counsel keys were declared on 19 October | seqs 6–8 (05:43–05:44Z) | ✓ |
| 5.2 | Builder and reviewer keys signed 6,621 of 7,810 entries | log count: builder 3,410 + reviewer 3,211 | ✓ |
| 5.3 | `merge` was granted to the herald at seq 51 | seq 51; book §11.10 for the reason | ✓ The reason given is the book's reading |
| 7 | The charter's SHA-256 is in genesis | `git show 95679e7:CHARTER.md \| sha256sum` = `383867d0…` = seq 0 `body.charter` | ✓ |
| 7 | The kernel is 450 lines | `tools/count_kernel.py --limit 500` | ✓ |
| 7 | 100,000 logs and 658,885 prefixes, with 0 disagreements | REPORT §8.1, criterion 2 | ✓ |
| 7 | Table 2 seqs and dates: 188, 337, 367, 5563, 5564, 7180, 7615 | log | ✓ |
| 7 | C1b: M = 214358881/8398080 over nine items, p₀ = 6/11 | REPORT, C1b §1 | ✓ |
| 7 | C2a failed on nine off-log repairs | REPORT, C2a §§1–2; `fix` seq 5563 | ✓ |
| 7 | C2a′ failed on criterion 3's walk of commits | BRIEF-C2a-3 §The precedent | ✓ |
| 7 | C2a-3 opens at the first push after 2026-11-30T00:00:00Z | BRIEF-C2a-3 §The window; grant seq 7615 | ✓ |
| 7 | The falsifiers | CHARTER §12 | ✓ |
| 7 | The ratio is 459 : 1,786 | `judge/status.py --subject C2a` at seq 7809 (A3.4 line) | ✓ |
| 8 | A fixed table crosses at event 53 | AUDIT-criteria-20261117.md, construction F | ✓ |
| 8 | The freshness stream comes from the operator's own marketplace | book App. A, A.22, Mechanism | ✓ |
| 8 | The guy-master key holds `forecast` | seq 33 | ✓ |
| 8 | The A2.8 monitor is unbuilt | LAW.md line 256 | ✓ |
| 8 | Cross-family reads are procedural, not code | CHARTER A6 order; BRIEF-C2a-3 line 83 (`jack push` checks no verdict) | ✓ |
| Table 1 | Waismann row: no code mechanism | book App. A, A.19: "None in code" | Fixed: now marked ◦ (forced, not built) |
| Table 1 | Hart row: the three rules are held by the core, not the kernel alone | CHARTER A1.1 | Fixed |
| Disclosure | "each act signed under a key" | keys from seq 6 on; earlier and off-log acts exist (REPORT C2a §2) | Fixed: now "since 19 October 2026 they have acted under keys declared on the record" |
| Disclosure | Three providers' families | REPORT, C1b §2 "Models" (gpt-6-astra builds and reads); gemini-4-argon reviews; Codex kernel2; Claude counsel | ✓ |

## Claims about the literature

| Claim | Checked against | Result |
|---|---|---|
| DGM went from 20% to 50%, and removed the hallucination markers despite instructions | arXiv 2505.22954 §4.4, App. H | ✓ Fixed: draft 1 said "doubled" |
| Hyperagents' quotation "to ensure safety, prevent evaluation gaming" | arXiv 2603.19461 App. A.5 | ✓ |
| The census covers 114 studies; product evaluated, process rarely | arXiv 2610.27610 abstract | ✓ |
| Kolt's quotation "actors that shape the very laws that govern them" | arXiv 2603.28669 PDF | ✓ verbatim |
| Kim et al.: more than 350 models; correlated across providers | arXiv 2506.07962 abstract | ✓ |
| Pato Nogueira et al.: fail together beyond independence | arXiv 2607.02808 abstract | ✓ |
| Ron et al.: 387.44 → 130.99 | arXiv 2606.20158 abstract | ✓ ("about two-thirds") |
| Zhao et al., Corollary 3 (integrity vs completeness) | arXiv 2610.07459 abstract; the research report | Partial: the abstract confirms the completeness condition; "Cor. 3" comes from the research report and still needs checking against the PDF |
| RQGM's selective erasure on replacement | arXiv 2606.26294 PDF | ✓ |
| REUSE controls false promotions over a run | arXiv 2609.33180 abstract | ✓ |
| TRUST controls the false-evolution rate | arXiv 2611.10787 abstract | ✓ |
| Cai et al.: the requirement diverges near the ceiling | arXiv 2609.08175 PDF ("The requirement diverges as Ẑk ↓ Ẑ∞") | ✓ Reworded |
| Scrivens: summable risk gives finite true-positive rate | arXiv 2603.28650 abstract | ✓ |
| Survey: "Utility does not authorize promotion" is a takeaway | arXiv 2610.00093 PDF | ✓ Reworded as a principle |
| Henzi & Ziegel: lag classes averaged for lag h | arXiv 2103.08402 PDF | ✓ |
| Kolluri et al.: autonomy as the fraction of actions taken without human approval | arXiv 2602.11416 abstract | ✓ |
| McCain et al. (Anthropic): interventions per session fell from 5.4 to 3.3 | anthropic.com page, 18 Feb 2026 | ✓ |
| Tracekit: Ed25519, witnessed Merkle log | arXiv 2609.35659 abstract | ✓ |
| AgentBound: owner-signed constitutions | arXiv 2606.30970 v2 listing | ✓ |
| SFA AutoLab components | repo docs (autolab-frozen-zone, -preregistration, -ratification, -controller) | ✓ |
| Bibliographic details of 40 classic references | Crossref (DOIs as given) and the arXiv API | ✓ All except Henry (1974) and Yudkowsky & Herreshoff (2013), which stay † |

## Closed after the first pass

- **Zhao et al. (2026), Corollary 3.** Checked verbatim against the arXiv PDF: "signatures, hash chains, and independent checkpoints of the entries the audited party submits cannot justify SUPPORTED".
- **Henry (1974).** The paper cited is now "Option values in the economics of irreplaceable assets", *Review of Economic Studies* 41, doi:10.2307/2296373 (Crossref). The AER paper of the same year is no longer cited. The end page, 104, is from knowledge.
- **Yudkowsky & Herreshoff (2013).** The MIRI technical report was confirmed through its public discussion pages.
- **Suber (1990)**, Peter Lang, Bern, with Nomic as Appendix 3, confirmed at Harvard DASH. **Goodman (2014)**, the Tezos white paper of 2 September 2014, confirmed at tezos.com.

## Round 3 (25 November, after the referee pass)

| § | Claim | Source | Result |
|---|---|---|---|
| 3.2 | Gödel's second incompleteness theorem, cited as Gödel (1931) | Crossref record for doi:10.1007/BF01700692: *Monatshefte für Mathematik und Physik* 38:173–198 | ✓ |
| 4.3 | Prop. 3(b) in block form: the product of Bayes-mixture joint forecasts telescopes to $K^{-1}\sum_k \prod p_k$ | Cesa-Bianchi & Lugosi (2006), ch. 9, log loss; checked by hand | ✓ |
| 4.3 | With marginals, the bound fails: two members at 0.999 and 0.001, a block of two events, outcome (1,1) gives regret $2\ln 2 - 0.002 > \ln 2$ | by hand | ✓ |
| 4.3 | Example figures: 13.25% (n=20, 4,000 runs of 300 sittings), 50.35% (n=50, 2,000 runs of 200), block 0%, independent 0% | `sim_filtration.py`, seeded; the four commands in its docstring | ✓ |
| 4.3 | Fourteen resolutions in one minute of 2 November, seqs 550–563 | `log.jsonl` at e580b64: resolutions with ts 2026-11-02T12:15, all `world.renavon` | ✓ |
| 7 | Kernel line count | `tools/count_kernel.py` (now cited inline) | ✓ (as round 1) |
| Refs | Henzi & Ziegel is *Biometrika* 109(3), 2022; now cited as 2022 | Crossref (round 1) | ✓ |

## Round 4 (25 November, after cold read 1)

| § | Claim | Source | Result |
|---|---|---|---|
| 2, 3 | Rice is restricted to arbitrary programs, and Löb to a successor in the same theory | standard statements; the cold reader's objection | ✓ reworded |
| 3.2 | Only one of the seven stops is an authority | book ch. 12 (cold reader: lines 42, 78, 126) | ✓ |
| 4.3 | Example 2: implementation form 28.5%, block form 0% (n=20, 2,000 runs of 300 sittings); n=1 gives 0% for both | `sim_filtration.py --roster 20 300 2000` and `--roster 1 300 2000`, seeded | ✓ |
| 4.3 | The implementation updates the stake and the weights per event | `judge/value.py` 113–135 at e580b64 (the cold reader confirmed) | ✓ |
| 4.3 | Its base rate counts same-batch resolutions | `judge/entries.py` `resolution_rates`: a Laplace estimate over every earlier resolution of the type, in seq order | ✓ |
| 6 | SEA calls ALG 4 "the governance layer to deploy first" (§4.4), and leaves the composition's guarantees as open conjectures | arXiv 2607.00871 text, lines 524–525 and 84–89 | ✓ |
| 6 | RQGM gates on an evaluator-independent anchor and discards dependent records (§3.2, App. F) | arXiv 2606.26294 text, lines 176 and 328–330 | ✓ |
| 7 | 2,820 events; 478 sittings; 6 lag classes (213, 194, 47, 15, 8, 1); per-event E ≈ 1.52e60; block-form final wealth 2.149e4 and 1.615e4; threshold 120 | `block_on_log.py`, run in the jack checkout at e580b64 (31 s) | ✓ |
| Refs | Kephart & Chess 2003; Garlan et al. 2004 | Crossref records for the two DOIs | ✓ |
| Refs | Ross, Gordon & Bagnell 2011, PMLR 15:627–635; Zhang & Cho 2017, AAAI 31(1), doi:10.1609/aaai.v31i1.10857 | proceedings.mlr.press; ojs.aaai.org | ✓ |

## Round 5 (26 November, after cold read 2)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.1 | Prop. 1(b) with $L^*$ starting at a genesis entry: a proper suffix is excluded | by hand; the reader's counterexample no longer applies | ✓ |
| 4.3 | 641 liveness items; 37 timestamps with more than one item, covering 190 items (the reader counted 191); `score_items` scores them in sequence | `judge/status.py` `item_process` at e580b64, run in a scratch clone | ✓ |
| 4.4 | The judge does not read `promotion-replay.json`; the CI spot-check replays rows 592, 593 and 705; the table has 706 rows; the full replay is `transcripts/sessions/c2a-3-replay.md` | `judge/judge.py` (no reference to the table), `tests/promotion_replay_spot.py` and the table at e580b64 | ✓ |
| 7 | 2,846 events forecast, 2,820 resolved, 26 never; 482 sittings; classes 214, 191, 46, 19, 10, 2 | `block_on_log.py --rev e580b64` | ✓ |
| 7 | Type-pooled base rate: classes end at 2.149e4 and 1.296e4 (peak 1.392e4); thresholds 40 and 120; both cross | same | ✓ |
| 7 | Per-dataset base rate: running maximum 1 in every class | same; the reader found the same independently | ✓ |
| 7 | Ablations: per event with nothing leaked 1.089e60; one block process 3.552e10; the implementation's figure 1.520e60 | same | ✓ |
| 7 | Forecasts in these events: reviewer 2,795, builder 12 | same | ✓ |
| 8 | Audit: 28 criteria, of which 11 sound, 8 narrow and 9 empty; liveness is empty (construction L), and so is the procedure/object ratio (R) | `transcripts/AUDIT-criteria-20261117.md` lines 5, 40, 62 | ✓ |
| Table 1 | The grant at seq 7615 defers two pins until C2a-3 ends | log line 7616 | ✓ |

## Round 6 (26 November, the abstract first and the Lean core)

| § | Claim | Source | Result |
|---|---|---|---|
| Abstract | Fixed first, following Peyton Jones (one idea, contributions first), Mensh & Kording (a single message; context, content, conclusion) and Whitesides (work from an outline) | `05-what-the-paper-is-about.md` | ✓ |
| 4 | Props. 1(b), 2(a), 3(b), 4(b) and 5, and 3(a) and 4(a) for every finite horizon, are checked in Lean 4 against Mathlib v4.37.0-rc1, with only `propext`, `Classical.choice` and `Quot.sound` as axioms | `lake build` succeeded; `#print axioms` for every theorem; `grep sorry` finds nothing | ✓ |
| 4 | Ville's inequality is derived from Mathlib's optional stopping theorem, not assumed | `Claimproofs/Ville.lean`, `ville_finite` | ✓ |
| Refs | The mathlib Community 2020, CPP 367–381; de Moura & Ullrich 2021, CADE-28, LNCS 12699:625–635 | Crossref records for both DOIs | ✓ |

## Round 7 (26 November, after cold read 3)

| § | Claim | Source | Result |
|---|---|---|---|
| 7 | Observed to 2026-11-25T11:05:35Z: 476 sittings done and 4 pending; 2,803 member events, of which 2 expired unresolved; 19 resolved events had no forecast before their cutoff | `block_on_log.py --rev e580b64` (revised) | ✓ |
| 7 | Classes 212, 190, 45, 17, 10, 2. Pooled base: final wealth 2.231e4 and 1.25e4 (peak 1.342e4), crossing 40 and 120. Per-dataset base: running maximum 1. Ablations: 1.087e60 and 3.873e10 | same | ✓ |
| 4.3 | Example 1's aggregate is a product forecast, so the joint null and the per-event nulls coincide | by construction | ✓ |

## Round 8 (26 November, after cold read 4)

| § | Claim | Source | Result |
|---|---|---|---|
| 6 | Re-run at `e580b64`: 476 sittings done, 4 pending; 2,803 member events in done sittings, of which 170 expired, 168 of them resolved only after the deadline; 19 resolved events with no forecast before their cutoff | `block_on_log.py --rev e580b64` | ✓ |
| 6 | Five lag classes. Pooled base: final wealth 1.993e4 and 1.109e4 (peak 1.19e4), crossing 40 and 120. Per-dataset base: running maximum 1 in every class | same | ✓ |
| 6 | Ablations: per event with nothing leaked 2.49e58; one block process 1.74e10; the implementation's own figure 1.52e60 | same | ✓ |
| 6 | Forecasts in these events: reviewer 2,795, builder 12 | same | ✓ |

## Round 9 (26 November, after cold read 5)

| § | Claim | Source | Result |
|---|---|---|---|
| 2 | Promotion evidence is checked for presence and hash, not truth; the operator attests it by signing | SPEC §10 item 15, at `e580b64` | ✓ |
| 4.5 | A `fix` decision is typed as a repair; the first qualifying `fix` naming a failed window is not reported late and its taint lifts at the next push | `judge/status.py`, `item_process` (repair predicate, `window_fixes` handling) and `window_fixes` | ✓ (draft 11 had this backwards; corrected in draft 12) |
| 5.3 | Seq 51 is a `key` entry granting `merge` to herald, before the first promotion (C1a, seq 188) | log at `e580b64` | ✓ |
| 6 | C2a′ was vetoed at seq 5879 (before A6, so not ending it) and again at seq 7180, which A6 makes the end | log; CHARTER Amendment A6 | ✓ |
| 4.3, 7 | Scrivens's Theorem 1 assumes power-law risk schedules and overlap conditions | arXiv:2603.28650v2, Thm. 1 | ✓ |
| 4.3 | Restarting three windows at α = 0.05: 1 − 0.95³ ≈ 14.3% if independent; 3α = 15% in general | arithmetic | ✓ |

## Round 10 (26 November, drafts 12 and 13: held to the abstract; cold read 6)

| § | Claim | Source | Result |
|---|---|---|---|
| Abstract, 4.3 | C0 needs safety alone; C1's value is the liveness rate; predictive value from C2 | CHARTER §6 | ✓ (abstract reworded to match) |
| 4.1 | The kernel's state includes `transmuted` | `kernel/check.py` line 16 and lines 98–99 | ✓ |
| 4.4 | Kernel2 by Codex at C0 from SPEC alone; Gemini's C1a changes from SPEC, `spec/` and `tests/vectors/` | REPORT line 238; `kernel2/NOTES.md` | ✓ |
| 4.4 | The judge refuses on `checker_drift`; CI runs 300 seeds through both kernels | SPEC §10 item 5; `.github/workflows/tests.yml` line 57 | ✓ |
| 4.4 | The move must also agree at every first-parent commit after T up to its parent | SPEC §10, "The promotion evaluator" | ✓ |
| 4.2 | Counsel's and the operator's forecasts are scored by `tools/entry.py` `score`; none is among §6's value events | `tools/entry.py` line 122; `block_on_log.py` (reviewer 2,795, builder 12) | ✓ |
| 5.2 | Builder and reviewer keys: 2,968 forecasts, 2,951 resolutions and 702 proposals (6,621); 622 proposals carry the streams by title | log at `e580b64` | ✓ |
| 6 | The C2a′ ratio is 320 to 1,296 at seq 7180 and 459 to 1,786 at seq 7809 | `judge/status.py --subject C2a` with and without `--as-of 2026-11-22T11:44:05Z` | ✓ |

## Round 11 (26 November, draft 14 after cold read 7)

| § | Claim | Source | Result |
|---|---|---|---|
| 2 | A resolution needs an integer outcome and a non-empty evidence string; nothing checks that the evidence implies the outcome | SPEC §5 (body schemas) | ✓ |
| 2 | The resolution of forecast 123 was wrong, and stands in the score | REPORT, C1a report §4, line 371 | ✓ |
| 4.1 | A public key belongs to its first identifier for the life of the log | `kernel/check.py` line 51 (`bad_key`) | ✓ |
| 4.1 | The state holds each charter with its activation height; `charter_at` derives the one in force | `kernel/check.py` lines 16–20, 92–95 | ✓ |
| 4.3 | Proposition 3's sufficient condition needs conditioning on which events resolve | the reader's counterexample, checked by hand (−0.1252; +0.0300) | ✓ corrected |
| 4.5 | Non-repairs: genesis, key, amend, push, proposal and non-`fix` decisions. The operator's resolution or merge is a failure; his other entries clear pending resolutions | `judge/status.py` `item_process`, lines 110–113 and 126–136 | ✓ |

## Round 12 (26 November, draft 15 after cold read 8, which accepted)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.1 | The kernel records `transmuted` and the charter digests but does not use them; the judge enforces them | SPEC §7 ("The kernel records them; the judge enforces them (§10.13)"); `judge/judge.py` `promulgated_charter` | ✓ |
| 4.1 | An `amend` changes at once the charter trunk must match, and freezes pushes until its height | SPEC §10 items 2 and 12 | ✓ |
| 4.4 | Kernel2 at C0 by `openai/gpt-6-astra`; later revisions at `8fcd821`, `432e385` and `7ae10a3` (the last by `google/gemini-4-argon`) | `git show a6f36b4:kernel2/NOTES.md`; `git log e580b64 -- kernel2` | ✓ |
| 6 | 2,795 and 12 count the forecasts in the implementation's 2,820 events | `block_on_log.py`, which counts over `v["rows"]` | ✓ (now labelled) |

## Round 13 (26 November, who wrote each kernel)

| Revision | Kernel 1 (Python) | Kernel 2 (Go) | Families differ? |
|---|---|---|---|
| C0, 13–14 Oct | `claude-fable-5-1`, with round-2 fixes by `claude-opus-5-5` (trailers of 0ca0380…2d7e9a9) | `openai/gpt-6-astra` via Codex (a6f36b4, 12fc4ee; NOTES.md) | yes |
| C1 entry types, 18 Oct | `openai/gpt-6.1-sol` (2b6b835) | `openai/gpt-6-astra` (8fcd821; NOTES.md), then revised by `google/gemini-4-argon` (432e385) | **no**, for the first version of both |
| Last-key guard, 18 Oct | `claude-opus-5-5` (8d1dda9) | `google/gemini-4-argon` (432e385) | yes |
| C1a, 25 Oct | builder-1, Claude in counsel's custody (eafb69c, bcb19f7; REPORT, C1a report) | `google/gemini-4-argon` (7ae10a3) | yes |

## Round 14 (26 November, draft 18: strongest backed claims, on Guy's instruction)

| § | Claim | Source | Result |
|---|---|---|---|
| 5.1 | 19 `key` entries by seq 7809, 13 before the first promotion (seq 188); every key is the operator's grant | log at `e580b64` (seqs 1–82 before 188) | ✓ |
| 5.2 | 702 builder/reviewer proposals; 622 titled as stream batches (`due `, `freshness`, `hkjc`); of the other 80, 48 are reads and reviews | log titles, rule stated | ✓ |
| 5.2 | C1b's p₀ = 6/11 is the Laplace rate on the record through seq 163, committed before the window | `transcripts/BRIEF-C1b-draft.md`, "Null" | ✓ |
| 6 | Of C2a's nine repair rows, one was the operator's own act; eight were the court's machinery under his login; none re-attributed; the remedy was a GitHub App (seqs 5562–5563) | `transcripts/BRIEF-C2a-prime-draft.md`, "The nine rows"; log | ✓ |
| 6 | Gap decomposition: log10(1.52e60/2.49e58) = 1.8; log10(2.49e58/1.74e10) = 48.2; log10(1.74e10/1.99e4) = 5.9; 5.9 events per sitting (2,803/476) | `block_on_log.py --rev e580b64`; arithmetic | ✓ |
| 4.3 | 190 of 641 liveness items share a timestamp: 188 expiries, 2 batches | `item_process` at seq 7809 (rounds 5; cold reads 6 and 8) | ✓ |
| Discl. | The charter was drafted by Claude (`claude-opus-5-5`); SPEC commits are proposed by Claude counsel sessions | CHARTER line 3; `git log -- SPEC.md` trailers | ✓ |

## Round 15 (26 November, the adviser's audit, `REVIEW-adviser-1.md`)

| § | Claim | Source | Result |
|---|---|---|---|
| 5.1 | Key entries before seq 188 | log: seqs 1, 6, 7, 8, 22, 23, 31, 32, 33, 34, 48, 49, 51, 82 | **Fixed**: 14, not 13 (draft 18 miscounted) |
| 4.4 | Which file CI uses to replay the table | `tests.yml` line 31 runs `unittest discover -s tests`, whose default pattern `test*.py` skips `tests/promotion_replay_spot.py`; line 44 runs `pins/run.py`, whose `replay_drift` pin (`pins/replay.py` line 49) replays rows 300, 400 and 593 | **Fixed**: the citation and the rows. Round 5 above and cold reads 5–8 had accepted the wrong file. |
| 6 | Of 2,887 `world.renavon` forecasts, 2,869 carry `args.model`, all `openai/gpt-5.4-mini` (2,857 reviewer, 12 builder); 18 carry none | log at `e580b64` | ✓ (added) |

## Round 16 (26 November, draft 20: cold read 9 and the adviser's answers)

| § | Claim | Source | Result |
|---|---|---|---|
| 1 | 114 studies; of 90 self-described RSI studies, 22% audit two or more reruns of the full loop | arXiv:2610.27610 abstract | ✓ |
| 4.3 | Value events are the freshness stream and HKJC races | `judge/value.py` lines 29 and 33 | ✓ |
| 6 | CHARTER §12 quotations | CHARTER lines 185–190 | ✓ verbatim |
| 6 | A3.4 per window: C1a 127:32, C1b 67:82, C2a 1,131:3,449, C2a′ 320:1,296 | `judge/status.py --subject … --as-of` each end, at `e580b64` | ✓ |
| 6 | The typing predicate is unchanged since it entered the code | `git log -S'body["kind"] != "fix"'`: one commit, 879caf9, 31 Oct | ✓ |
| 6 | The nine rows: 1 operator, 5 machinery, 3 closes of unestablished hand | `acts-20261103T2144.csv`; BRIEF-C2a-prime lines 58–64 | ✓ |
| 5.1 | Forecast and resolution powers at seqs 31–34, as C1a's window began; herald-2 moves the merge key | RUNBOOK, `jack key`; log | ✓ |
| 4.4 | No ruling on the C1 kernel-family lapse | `git grep -i -E 'different (model )?family|same family'` | ✓ |
| Discl. | About four in five runner sessions naming a model ran `gpt-5.4-mini` | issue titles (740/881 by my parse; 739/939 by the adviser's) | ✓ |
| 6 | Audit recipe: latest `resolves_by`; empty sittings skipped before the stake count | `block_on_log.py` lines 168, 177 | ✓ |

## Round 17 (26 November, draft 21 after cold read 10, which accepted)

| § | Claim | Source | Result |
|---|---|---|---|
| 6 | Over every full 14-day interval, one exceeds 5 : 1: from genesis, 63 : 5; from seq 32 on, the worst is 871 : 1,755 | log at `e580b64`, objects by `judge/status.py`'s `world` rule (line 181, 186) | ✓ computed; the lead sentence now says the fourth falsifier was met once, on a literal reading |
| 6 | No key held `forecast` before seq 31; first object entry seq 38 (26 Oct) | log | ✓ |
| 5.2 | p₀ = 6/11 is the more demanding of two attributions; the brief's own rule gives 5/11 | BRIEF-C1b-draft lines 123–130 | ✓ corrected |
| 5.2 | 627 of 702 proposals titled as batches of either stream (adding the five `M2 race` titles); of the other 75, 46 reads and reviews (excluding the two read-gate proposals, seqs 654 and 657) | log titles | ✓ corrected |
| 4.4 | Gemini's 432e385 added only the last-key guard (and a `hasPower` helper) to kernel2; 8fcd821's C1 code stands | `git diff 8fcd821 432e385 -- kernel2/checker.go` | ✓ corrected |

## Round 18 (26 November, draft 22 after cold read 11)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.2 | The stream's prompt was put on the record on 2 November (0a60c84) and revised five times, to 13 November | `git log e580b64 -- transcripts/sessions/stream-forecast.md` (six commits) | ✓ corrected; draft 21 said "fixed" |
| 5.2 | Of the builders' and reviewers' 5,919 forecasts and resolutions, 5,811 are of the two stream types (5,747 `world.renavon`, 64 `world.hkjc`); 108 other | log, each resolution typed by its forecast | ✓ corrected |
| 6 | 14-day intervals over 5 : 1 begin only between genesis and 2026-10-17T17:16:59Z; worst 63 : 5 at genesis; from seq 31 (A3 in force) the worst is 872 : 1,755 | log; half-open intervals at every start time where a count changes | ✓ corrected; draft 21 said "one interval" and seq 32 |
| 6 | A3 entered at seq 30, in force at seq 31; the first forecast key is seq 31 | log | ✓ |
| 4.4 | "First to record it": the record searched holds no ruling, waiver or finding on the C1 lapse | `git grep` (round 16) | ✓ restated as a claim about the record |

## Round 19 (26 November, draft 23 after cold read 12)

| § | Claim | Source | Result |
|---|---|---|---|
| 6 | Attribution by declaration cut repair rows 7 → 1 (acts of 1 Nov) and 81 → 9 (acts of 3 Nov) | `transcripts/evidence/acts-20261101-raw.csv` against `acts-20261101.csv`; likewise for `acts-20261103T2144`; BRIEF-C1b Amendment 2 | ✓ corrected; drafts 20–22 said "no row has been re-attributed" |
| 4.5 | The typing code entered on 31 Oct at 13:06Z, during C1b's window (opened at seq 188, 10:42Z), and the repair predicate line has not changed | `git log -G` on the predicate line (one commit, 879caf9); REPORT, C1b report ("The window opened at seq 188") | ✓ |
| 4.1 | An `amend` at seq a changes the charter trunk must match at a, and freezes pushes until k | SPEC §10 items 2 and 12 | ✓ reworded |
| 6 | The 14-day scan covers complete intervals ending by the record's last entry | the computation of round 18 | ✓ stated |
| Abstract, 5.2 | "held fixed and trusted as infrastructure", not "rather than tested" | DGM, Hyperagents (§1); DGM App. H shows a detector failure found by experiment | ✓ reworded |

## Round 20 (26 November, draft 26: the paragraph pass and adversarial read 1)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.3 | Our value null is the strong (pointwise) null in Choe & Ramdas's terms; their weak null concerns advantage on average | arXiv:2110.00115 abstract ("on average (rather than always)") | ✓ corrected; drafts to 25 said "weak" |
| 4.3 | Evidence valid in a coarser filtration need not be valid in a finer one | Choe & Ramdas, arXiv:2402.09698, abstract | ✓ added |
| 6 | The per-event ablation now dates each sitting by its whole completion; figure unchanged (2.492e58) | `block_on_log.py`, re-run at `e580b64` | ✓ fixed |
| 6 | Across protocol versions: class 1 final 1.993e4–2.231e4, class 2 1.109e4–1.615e4, all crossing; per-dataset maximum 1 wherever computed | rounds 4, 5, 7, 8 above | ✓ |
| 7 | SEA accumulates per-version evidence across rounds (§4.4); no carry-over of a rejected candidate's evidence is described | arXiv:2607.00871v1 §4.4 | ✓ qualified |
| 7 | Pitt, Schaumeier & Artikis 2012, ACM TAAS 7(4), doi:10.1145/2382570.2382575: six of Ostrom's eight principles axiomatised in the Event Calculus, with a testbed | Crossref record; abstract | ✓ |
| 7 | AgentCity (Ruan & Zhang 2026, arXiv:2604.07007): agents legislate operational rules as smart contracts, "the law itself"; human ownership chain; no sequential promotion | arXiv abstract | ✓ |
| 7 | Artikis, Sergot & Pitt 2009 (ACM TOCL 10(1):1–42) and Artikis 2012 (J. Logic Comput. 22(6):1301–1334) | reference lists of later papers by the same group | ✓ bibliographic details from those lists |
| 8 | The operator's three forecasts are all `world.assize`; none is on the freshness stream | log at `e580b64` | ✓ |

## Round 21 (26 November, draft 27 after adversarial read 2)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.3 | The counted-line cap was raised three times against the pre-statement (4,500 → 5,500 on 19 Oct; 6,200 on 25 Oct; 6,900 on 31 Oct at seq 197, after C1b's window opened at seq 188), each recorded as a finding | SPEC §10 (line 547); BRIEF-C1b criterion 3; seq 197 push at 13:04:49Z | ✓ added |
| 4.3 | Assumption (A) now also requires that none of B_m's own outcomes be realised when its forecasts close | the reader's point; the block statistic needs it | ✓ fixed |
| 4.3 | Simulation intervals: 530/4,000 = 13.3% (12.2–14.3%); 1,007/2,000 = 50.4% (48.2–52.5%); 0/4,000, upper bound 0.075% | normal approximation; rule of three | ✓ |
| 8 | Proper scores, including the logarithmic, decompose into reliability and resolution | Bröcker, arXiv:0806.0813 (doi:10.1002/qj.456) | ✓ corrected; drafts to 26 called a log-score analogue open |
| 7 | Schneier & Kelsey (1999), secure audit logs | ACM TISSEC 2(2) | ✓ added |


## Round 22 (28 November, draft 29 after cold reads 15 and 16)

| § | Claim | Source | Result |
|---|---|---|---|
| Abstract, 8 | The paper offers a design and an audit, not an evaluation; the experiment that would test the design has two steps, tie each grant to a passed test and then compare with simpler governance | Guy's choice of scope, 28 Nov; §5.1; adversarial reads 1 and 2 | ✓ stated (draft 28) |
| Table 1 | Layers promoted on criteria stated in advance, with recorded departures | SPEC §10, three raises of the line cap (round 21) | ✓ qualified |
| 4.1 | Prop. 1(b): logs of different length have last lines with different `seq`, so equal last hashes are a collision at once | entries numbered by position (SPEC §6; kernel) | ✓ shorter proof |
| 4.3 | Rejection at level α is evidence, not proof, of a conditional advantage at some block | standard | ✓ reworded |
| 4.3 | The common unit for batched liveness items is an open operational definition | the text's own statement | ✓ labelled |
| 6, Table 3 | Ablations: 1.52e60 → 2.49e58 → 1.74e10 → 1.99e4; differences 1.785, 48.156, 5.941 orders | `block_on_log.py --rev e580b64`; reproduced by read 15 | ✓ tabulated |
| 8 | The expected score of a strictly proper score, the logarithmic among them, decomposes into uncertainty, resolution and reliability | Bröcker 2009, eq. (13) and Table 1 ("Ignorance"), arXiv:0806.0813 | ✓ made precise |
| 8 | The freshness stream is exposed to performative influence; nothing shows that influence occurred | log at seq 7809 (the operator's three forecasts are `world.assize`) | ✓ reworded |
| Disclosure | 30 Oct to 25 Nov 11:05Z: 965 `builder:`/`reviewer:` issues; 849–855 name their model, by parse; 720 name `gpt-5.4-mini` (84–85%) | REST list of renavondata/opencode-runner issues, 28 Nov; read 15 counted 720 of 853 | ✓ endpoint and count fixed |
| 4.5 | The repair-typing line entered at 879caf9 (31 Oct) and is unchanged; the `window_fixes` exception was added later, in 4c1f9c97 (11 Nov; on main at 33ee227a, 12 Nov), before its first use at seq 5563 (17 Nov) | `git log -S window_fixes e580b64 -- judge/status.py`; first-parent ancestry; log seq 5563 | ✓ corrected after read 16; drafts to 28 implied both dated from 31 Oct |
| 6 | Re-attribution: 7 → 1 (acts-20261101), 61 → 1 (acts-20261103), 81 → 9 (acts-20261103T2144), each against its `-raw` twin | `class` column counts at `e580b64` | ✓ both 3 Nov tables now named |
| 6 | assize is the programme's earlier repository, whose record supplies the charter's baseline | CHARTER §1, "Evidence from assize" | ✓ introduced |
| 8 | Choe & Ramdas 2024a back the stronger incumbent and the bounded-difference bet, not a resolution check | arXiv:2110.00115 (read 16: "resolution" appears only for grid resolution) | ✓ citation moved |
| 5.2 | Reads and reviews: titles naming the word read or review (whole word; "reviewer" excluded) | log at seq 7809; reads 15 and 16 reproduce 46 | ✓ worded |

## Round 23 (28 November, draft 30 after counsel's note on windows and tests)

| § | Claim | Source | Result |
|---|---|---|---|
| 4.3, 5.1 | Promotion means a layer is "frozen, and the next begins"; a failed window is fixed by a change entry and starts again | CHARTER §6, promotion rule, at `e580b64` | ✓ quoted |
| 5.1 | Key grants are the operator's decisions, and the charter does not tie them to promotion | CHARTER §7 ("a capability grant (money, releases, keys)"); no mention of keys in §6's promotion rule | ✓ |
| 5.1 | C1b's window opened at C1a's promotion (seq 188); C2a's at seq 367, after C1b's (seq 337); C2b not begun | REPORT, C1a and C1b reports ("C1b opened at the same instant"; "the window opened at seq 188"); log | ✓ |
| 5.1 | One promotion rested on a sequential test (C1b, M ≈ 25.5); C1a's rested on exact criteria: pins, checker agreement, kernel size, counts of forecasts and resolutions | REPORT, C1a report §1 (criteria 1–6), C1b report §1 | ✓; drafts to 29 implied by omission that promotions were test-based |
| 5.1 | No key entry has followed a promotion; the rule that would tie keys to promotion is in neither the charter nor the code | log (key entries after 337: 2254–2255 only); CHARTER; adviser's answer 5 | ✓ |
| Abstract, 1, 8, 9 | The design's claim is now growth by test (freeze and begin the next), not "powers only by test", which the charter never said and which would be circular for the layer under test | counsel's note of 28 November; CHARTER §6 | ✓ restated |
