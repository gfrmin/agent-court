From the claim session, 25 November 2026. This session was asked to write the arXiv note on jack's theory; it holds no key on jack. It is filed here at Guy's instruction of the same day. The note's draft is in Guy's Project (`claude/claim/02-draft.md`) and is not public. Everything below is for the author to judge. Nothing is due.

The issue sits beside #34–#37 and tries not to repeat them. Sources are cited by arXiv id; the 2026 ones were checked against their arXiv records on 25 November.

## 1. Chapter 12 §12.7: the conjunction of the wealth processes is already a valid test

The chapter says: "Strictly, the court runs several wealth processes, and they make a single test only if they are combined, for instance by averaging, which the court does not yet do."

That holds for the *intersection* null, "neither value nor liveness holds". For promotion the null that matters is the *union*: "value is lacking, or liveness is lacking". A rule that promotes only when every process is at least 1/α is a valid level-α test of the union, because the event of promotion lies inside {sup W ≥ 1/α} and also inside {sup M ≥ 1/α}. Whichever null is true, Ville's inequality applies to it (Ville 1939). This is the intersection–union principle (Berger, R. L. 1982, "Multiparameter hypothesis testing and acceptance sampling", *Technometrics* 24(4):295–300; details to verify). The note states it as its Proposition 5. The chapter could say that no combination is needed for the promotion rule.

## 2. Rows A.14 and A.21: diversity is not independence, and the 2026 evidence on LLMs

Knight & Leveson (1986) is the classic counter to N-version independence. Three recent studies repeat it for language models:
- Kim, Garg, Peng & Garg (2025), "Correlated Errors in Large Language Models", ICML 2025, arXiv:2506.07962. Across more than 350 models, "models agree 60% of the time when both models err". Larger, more accurate models have highly correlated errors "even with distinct architectures and providers".
- Pato Nogueira, Pattabiraman, Vieira & Campos (2026), arXiv:2607.02808. Twelve models, 224 problems, five languages. Implementations still fail together far more often than independence predicts.
- Ron, Baudry & Monperrus (2026), "N-Version Programming with Coding Agents", arXiv:2606.20158. They re-run Knight–Leveson with 48 agent-written implementations and find substantial common-mode failure. Majority-vote triples still cut the mean failure count from 387.44 to 130.99.

**Suggested restatement:** a second kernel written by another model family detects the faults on which the two kernels differ, and lowers the risk. It does not make failures independent. The same applies to cold reads by other families as evidence. A.21 already says diversity must mean "different failure causes"; these papers show that a different family is not enough to guarantee that.

## 3. Row A.13: integrity is not completeness

Zhao et al. (2026), "Auditable Claims about AI Agents", arXiv:2610.07459, 5 Oct 2026, Cor. 3: signatures and hash chains over the entries a party submits cannot by themselves establish completeness, because an omitted action leaves the signed record valid.

**Suggested distinction:**
- *Completeness of law* holds by construction: an act that is not an entry has no legal effect.
- *Completeness of the record of acts in the world* does not. It needs an independent record.

Criterion 7's acts table — the platform's own event history of the owner's acts — is exactly such an independent record. Its finding of nine off-log repairs is what failed C2a's first window. A.13, or chapter 13, could say so.

## 4. Chapters 6 and 12: carried wealth buys validity at the cost of recency

A4.1 makes the probability of *ever* crossing under the null at most α, across all windows. That is the gain. The cost is that wealth earned earlier can carry a later window whose own items are few. `transcripts/AUDIT-criteria-20261117.md` on jack's main notes this for C2a-prime's criteria 5 and 6. A failure does bite: it multiplies wealth by (1 − q̂)/(1 − p₀), which is small when q̂ is high. Still, what is controlled is "ever", not "now". Tests that weight the present — a fresh process per window at a split α, or a change-detecting e-process — trade validity for recency. The book may want to name the trade where it praises A4.1.

## 5. Prior art for #37, found on 25 November

| Work | Note |
|---|---|
| Iacob et al., "The Red Queen Gödel Machine", arXiv:2606.26294 (v3, 8 Oct 2026) | The closest design to the promotion evaluator's replay rule, and its opposite. Its evaluator is replaced at epoch boundaries, followed by "selective erasure" of the utility records that depended on it. jack's new evaluator must reproduce the old one's verdicts except lines marked in advance (SPEC §10, item 15; grant seq 6851). |
| Sun, Zeng, She & Wang, "Which Self-Improvements Should We Trust?" (REUSE), arXiv:2609.33180 (27 Sep 2026) | Run-level control of false promotions when benchmarks are reused. |
| Gao, Qi & Cui, "Trustworthy Recursive Self-Improvement with Statistical Guarantees" (TRUST), arXiv:2611.10787 (7 Nov 2026) | False-evolution-rate control. |
| Cai et al., "A Theory of Reliable Self-Evolution for Agent Harnesses", arXiv:2609.08175 | |
| Scrivens, "Information-Theoretic Limits of Safety Verification for Self-Improving Systems", arXiv:2603.28650 | Shows that gates with summable risk admit only finite true-positive rate. |
| Chen, Zhu & Zheng, "Auditing the Product, Not the Recursion", arXiv:2610.27610 (20 Oct 2026) | A census of 114 studies of recursive self-improvement. Its reporting standard asks for "human repairs to the harness" and for who authorised changes to the evaluator. |
| Sengupta, "Self-Evolving Agents with Anytime-Valid Certificates", arXiv:2607.00871 | |
| PACE, arXiv:2606.08106 | |
| Wu et al., SGM, arXiv:2510.10232 | |
| Neal, SFA-Bench v2.0.0-alpha.2 and AutoLab, github.com/iotaverbum-core/sfa-bench, doi:10.5281/zenodo.20766587 (July 2026) | A hash-attested frozen zone, a pre-registration sealed before each patch, a hash-chained meta-ledger and human ratification by token. The closest precedent for pre-registration with a human gate. |
| Ghosh, Tracekit, arXiv:2609.35659 | Ed25519-signed, witnessed agent logs. |
| Kaul, Lan & Gupta, AgentBound, arXiv:2606.30970 | |
| Nakajima, Regimes, arXiv:2606.10241 | |
| Kolt, "Superintelligence and Law", arXiv:2603.28669 | Says that legal alignment "will need to contend with the prospect of actors that shape the very laws that govern them". |

**Verdict:**
- No work before 14 October 2026 is known to anticipate any of these three:
  - law built before the agent and imposed first on its builders;
  - promotion of the institution by a continued e-process that tests liveness, the owner's repairs, as well as value;
  - an evaluator that changes only by replaying its own past.
- Each of the following is anticipated, so the book should not claim it as new:
  - signed logs;
  - frozen evaluators;
  - human ratification;
  - pre-registration;
  - per-edit anytime-valid gates.

## 6. `papers/design-note/design-note.md`, Non-goals: "one drafting model"

The design note says: "The sessions run on one model family under several keys".

The record disagrees:
- jack's REPORT.md, C1b §2, "Models", says "gpt-6-astra for builds, reads and race resolution".
- kernel2 was written by Codex (REPORT.md §8.2).
- Reviews were also done by gemini-4-argon and gpt-6.1-sol (transcripts).

The sentence may mean the drafting of the law. If so, it needs narrowing.

---
*Filed by the claim session (Claude, `claude-opus-5-5`), which holds no key on jack, at Guy's instruction.*

🤖 Generated with [Claude Code](https://claude.com/claude-code)
