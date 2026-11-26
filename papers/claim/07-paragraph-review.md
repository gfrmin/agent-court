# Paragraph-by-paragraph review of draft 24 (claim session, 26 November)

Guy asked for every paragraph to be checked in sequence: is it correct, does it make sense, and is it written as well as it can be? Draft 25 makes the changes below. Paragraphs not listed were read and left as they were.

| § | Paragraph | Problem | Change |
|---|---|---|---|
| Abstract | Sentence 1 | "Although" joined two unrelated claims: the evaluator is trusted, and Rice, Löb and Goodhart limit what can be established about the agent. | Split. The limits come first, then "yet" the evaluator is held fixed and trusted. |
| Abstract | Sentence 2 | Two colons in one sentence. | Split in two; the tests are listed after one colon. |
| 1 | Main idea | "…on its own record, and the tests should themselves be valid": two "and" clauses. | "…only by valid sequential tests on its own record." |
| 1 | Contribution 2 | "(§4)" twice. | The second removed. |
| 1 | New thing 1 | Read as a claim about the implementation, which has not done it. | Prefixed "In the design". |
| 2 | Opening | "The object" was undefined. | "What is to be governed". |
| 2 | Score | The Goodhart clause hung off the sentence ("on outcomes the scored parties do not control"). | "provided the scored parties do not control the outcomes". |
| 2 | Threat model | Said "two exceptions", then listed three (times as well). | Three exceptions, each in one sentence. |
| 4 | Opening | "Hold by construction" is false for 1(b) and 2(a), which are a collision reduction and calculus. | "are elementary". |
| 4.1 | State | Run-on bullet. | Tightened. |
| 4.1 | Prop. 1(b) | "produces one with at most its advantage" was garbled. | "with probability no greater than its probability of finding a SHA-256 collision". |
| 4.2 | Procedure | "One model, in every forecast that names its model" was awkward. | "one named model (§6)". |
| 4.3 | Value | A 300-word paragraph covering three topics; "resolved events" contradicted the later handling of unresolved ones. | Split into blocks, lag classes and partial resolution; "events". |
| 4.3 | Remark | "The joint forecast matters too" was a vague transition. | "Nor can the joint forecast be replaced by the product of the marginals…". |
| 4.3 | Liveness batching | The design rule, the implementation and a caveat that seemed to contradict the rule were interleaved. | Rule, then the open question of units, then what the implementation does. |
| 4.3 | Prop. 4(b) | "could only be bounded by". | "is bounded only by". |
| 4.4 | Kernels | Two colons in one sentence. | Recast with a semicolon. |
| 4.5 | Priced by entry | "Repairs cannot be made to fall by revising it" sat beside §6's account of repairs falling by re-attribution. | Adds that §6 records how they fell by re-attribution instead. |
| 4.5 | Off the record | The window-failing rule omitted the attribution step. | "after attribution by declaration (§6)". |
| 5.1 | Authority | Repetitive, and the seq 51 example duplicated the key count. | Restructured as design, then implementation, then what the implementation has done. |
| 5.2 | Ground 3 | "Frontier model sessions" was false: the stream ran on `gpt-5.4-mini`. | "from frontier models to small ones". |
| 5.2 | Last paragraph | Precedents and implementation counts ran together. | Split in two. |
| 6 | Sittings | The rule for empty sittings came before the scoring rule it depends on. | Reordered. |
| 8 | Null | "Open" twice. | Merged. |
| 8 | Correlated checkers | Chen, Zhu & Zheng was cited for estimating shared error against references, which that source has not been checked to say. | Citation dropped; Kim et al. kept, as the example. |
| 8 | Who operates the world | Missing the mitigating fact and the precise risk. | None of the operator's three forecasts is on that stream (log). He could move these outcomes, and the record could not show it. |
| Disclosure | "Since 19 October … they" | "They" pointed at the wrong noun. | "the model sessions", moved before the runner figures. |
