# Cold read 18 of the claim paper: report and disposition

- **Reader:** `google/gemini-4-argon`, renavondata/opencode-runner #1457, on 28 November. It checked the change from draft 29 to draft 30 only.
- **Verdict:** **minor revision**. It found that the restatement "restores the charter's own definition from genesis… rather than fitting the design post hoc to the record". It found one factual error and two tensions. **Draft 31** fixes all three.

## Disposition

| Point | Verified? | What draft 31 does |
|---|---|---|
| "C2b's keys would be its first case" is wrong: C2b grants no key | Yes: BRIEF-C2b Amendment 10 clause 3; RUNBOOK line 277 | Removed. |
| "Keys granted as windows open rather than on passing" conflicts with §4.3: a layer must hold its powers while tested, so a key rule can only require the earlier layer's promotion | Yes | Abstract, §1, §5.1, §8 and §9 now say "no rule yet ties its keys to promotion", and §5.1 states the coherent form of such a rule. |
| Contribution 1, §7 and §9 state "each layer" without C0's safety-only exception, and C1a used exact criteria | Yes for C0. C1a is a window (CHARTER A3.2) | "Each layer after the record"; §5.1 and Table 2 explain the windows. |
| "Nothing is built on" an unpassed layer: C2b and C2c were pre-built on branches | Yes | Now about the next layer's window. |
## The report (verbatim)

### Overall Assessment of the Change (Draft 29 → Draft 30)

Replacing "granted powers only by sequential tests" with growth by promotion ("a layer is frozen, and the next begun") restores the charter's own definition from genesis (`95679e7` and `e580b64`, `CHARTER.md` §6: *"A layer is promoted (frozen, and the next begins)"*) rather than fitting the design post hoc to the record. Draft 29 had read key grants into §6's promotion rule, which `CHARTER.md` §7 instead classifies separately among the operator's reserved decisions (*"a capability grant (money, releases, keys); a veto or promotion at a layer boundary"*). However, Draft 30 introduces one factual error against the repository at `e580b64` regarding C2b's keys (§5.1) and leaves an internal tension between §§4.3/5.1 and the framing in the Abstract, §1, §8 and §9 over when keys should be granted.

---

### Passage-by-Passage Check

#### 1. Abstract (l. 14)
- **(1) Factual backing:** Backed by `CHARTER.md` §6 (promotion freezes a layer and begins the next; liveness and, from C2, predictive value), `REPORT.md` (C1b report §1: one sequential-test promotion at `seq 337`, $E = 214358881/8398080 \approx 25.52$), and `log.jsonl` (19 `key` entries; powers granted as windows opened, e.g., `seqs 31–34` after C1a opened at `seq 30/31`).
- **(2) Errors / inconsistencies:** Saying *"its keys are still granted as windows open rather than on passing"* conflicts with §4.3 (l. 149) and §5.1 (l. 270), which point out that a layer under test *must* hold its powers when its window opens (*"before the test, not after it"*). Even under the key-gating rule §5.1 proposes, a layer's keys are granted when its window opens (after the *earlier* layer passes), not when that layer itself passes.
- **(3) Design vs. record:** The design sentence matches `CHARTER.md` §6 (including *"once there are forecasts to aggregate"*, save that C0 needs safety alone). The implementation sentence accurately reports one sequential-test promotion instead of Draft 29's blanket disclaimer.

#### 2. §1 Introduction — "The main idea" and "Contributions" 1 & 3, Scope, Novelty bullets (ll. 24, 27, 29, 31, 34–35)
- **(1) Factual backing:** Promotion gating layer order once on a sequential test (C1b) and keys being granted by the operator are backed by `CHARTER.md` §§6–8, `REPORT.md`, and `log.jsonl`.
- **(2) Errors / inconsistencies:**
  - In Contribution 1 (l. 27) and Novelty bullet 1 (l. 34), *"each layer is frozen, and the next begun, only when sequential tests pass, of liveness ... and of predictive value"* omits the qualification (present in the Abstract and §4.3) that C0 uses safety alone (`CHARTER.md` §6), C1a used exact criteria only (`REPORT.md`, C1a §1), and C1b tested liveness alone before C2's value test.
  - Contribution 3 (l. 29) repeats the contrast between promotion and keys *"which the operator makes as each window opens"*, without noting that opening a window already presupposes the prior layer's promotion.
- **(3) Design vs. record:** Restates the charter's §6 promotion rule and §8 build order, and no longer underclaims the record (Draft 29 claimed the design was unimplemented even for layer progression; Draft 30 credits the one sequential-test promotion at C1b).

#### 3. §4.3 Promotion by betting (ll. 149, 151) and §4.5 The principal, priced (l. 254)
- **(1) Factual backing:** Fully backed by `CHARTER.md` §6 (*"A layer is promoted (frozen, and the next begins)"*; *"A layer that fails its window is not patched in place: the failure is a precedent, the fix is a change entry, and the window starts again"*), §8 (*"Each is a simple system that works before the next is added"*), and A3.2.
- **(2) Errors / inconsistencies:** None within §4.3 or §4.5. The added explanation in §4.3 (why parties must hold a layer's powers before its test) is clear and sound.
- **(3) Design vs. record:** Directly quotes and paraphrases `CHARTER.md` §§6 and 8 from genesis (`95679e7`). It neither overclaims nor underclaims.

#### 4. §5.1 The order follows from the dependencies (l. 270)
- **(1) Factual backing:**
  - *Backed:* `CHARTER.md` §7 lists capability grants (`keys`) as operator decisions without tying them to promotion. `log.jsonl` has 19 `key` entries by `seq 7809`, 14 before `seq 188` (`seqs 1, 6–8, 22–23, 31–34, 48–49, 51, 82`). Forecast/resolution powers entered at `seqs 31–34` (`2026-10-25T16:50:21Z–16:51:56Z`) right after A3 opened C1a at `seq 30` (`activate_at: 31`; `RUNBOOK.md` l. 80). `herald-2` (`seq 201`) moved `merge` off counsel's session (`RUNBOOK.md` ll. 83–86); `seqs 216–217` revoked `builder-3` and `herald-1`; `seqs 2254–2255` rotated `counsel-2` to `counsel-3`. C1b opened at C1a's promotion (`seq 188`, `2026-10-31T10:42:10Z`), C2a opened at `seq 367` after C1b's promotion (`seq 337`, `2026-11-01T11:31:58Z`), and after C2a's two failed windows C2b's window has not opened (`REPORT.md`). C1b's promotion used a sequential liveness test ($M = 214358881/8398080 \approx 25.5$, $p_0 = 6/11$). C1a's rested on exact criteria (`REPORT.md`, C1a §1, criteria 1–6: the four named in §5.1 plus `scope.json` unchanged, `jack score` vector output, and no veto). Neither `CHARTER.md` nor `kernel/check.py` / `judge/judge.py` gates `key` entries on `promote`.
  - *Not backed (factual error):* **"C2b's keys would be its first case."** In `transcripts/BRIEF-C2b-draft.md` at `e580b64`, C2b adds no kernel entry types (ll. 29–33), and **Amendment 10, Clause 3** (l. 687, 10 Nov; approved by the operator's `decision grant` at `seq 4643`, 14 Nov) explicitly struck the `key herald-2 --powers merge,forecast` re-declaration from C2b's opening (*"`herald-2` keeps `merge` alone (seq 201), and the `forecast` power is given by the window that first has it draw"*). `RUNBOOK.md` l. 277 confirms: *"`herald-2` is not given the `forecast` power"*. Thus C2b has no key grant (and `forecast` is a C1a power, not a new C2b power).
  - *Nuance on "nothing is built on a layer that has not passed":* While C2b's *window* has not opened on `main`, C2b's prerequisite read gate was merged to `main` during C2a (`seqs 655, 658`), and C2b and C2c-1 code and pins were pre-built on branches before C2a passed (`seqs 4634, 4643`; `BRIEF-C2b-draft.md` l. 509; `BRIEF-C2c-1-draft.md` l. 120).
- **(2) Errors / inconsistencies:** The claim about *"C2b's keys"* contradicts `BRIEF-C2b-draft.md` Amendment 10 and `RUNBOOK.md` l. 277 at `e580b64`.
- **(3) Design vs. record:** Distinguishing layer-order promotion (in `CHARTER.md` §§6, 8) from key grants (in `CHARTER.md` §7) is faithful to the charter.

#### 5. §7 Related work (ll. 358, 360), §8 Limitations (ll. 372, 388), and §9 Conclusion (l. 396)
- **(1) Factual backing:** Backed by the record as above.
- **(2) Errors / inconsistencies:** §7 (l. 360) and §9 (l. 396) state without qualification that *each* layer grows/freezes by sequential test (whereas C0 and C1a used exact criteria). In §8 (l. 388) and §9 (l. 396), contrasting keys granted *"as each window opens"* with tying key grants to a passed test remains in tension with §4.3's argument that a layer under test needs its powers when its window opens (so a key gate can only require that the *preceding* layer's test has passed before the new window's keys are granted).
- **(3) Design vs. record:** Aligns §§7–9 with `CHARTER.md` §6 and the single sequential-test promotion in the record.

RECOMMENDATION: minor revision
