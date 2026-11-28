# Cold read 20 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, renavondata/opencode-runner #1460, on 28 November. It checked the change from draft 31 to draft 32: one sentence.
- **Verdict:** **accept**.
  - It found every statement in the sentence supported.
  - It re-derived M = 214358881/8398080 ≈ 25.52.
  - It confirmed that p₀ = 6/11 was in brief v7 (`e414bb58`, 31 Oct 09:14:26Z) before C1b opened at 10:42:10Z.
- **One pinpoint citation, non-blocking:** C0's missing window is stated in REPORT §8.3, item 4, and §8.2 gives the patch history. The final text now cites §§8.2–8.3, and round 25 of the self-check is corrected. The sentence is otherwise unchanged.

## The report (verbatim)

## Referee report: draft 31 → draft 32

**The substantive correction resolves the nineteenth referee’s objection.** The in-memory comparison finds exactly one changed sentence, in §5.1. It removes “each under the charter’s rule” and explicitly records C0’s procedural departures.

### 1. Factual support

- **C0:** Supported. At `e580b64`, REPORT §8.1 records satisfaction of C0’s safety-oriented exit criteria and recommends promotion. REPORT §8.3, item 4, explicitly states: “No window was stated for C0, and the layer was patched in place throughout.” Section 8.2 documents the intervening patches. CHARTER §6 exempts C0 from liveness and value testing, but still requires a pre-stated window and forbids patching failed windows in place. The revised wording correctly distinguishes satisfaction of safety criteria from full procedural compliance.
- **C1:** Supported. CHARTER Amendment A3.2 explicitly makes C1a and C1b two windows of one layer, with promotion at C1b’s exit. The log records `promote C1b` at seq 337, **1 November 2026, 11:31:58Z**.
- **Liveness wealth and advance-fixed null:** REPORT’s C1b item table records nine successes. Independently applying A4’s predictable Laplace stakes gives
  \(M=214358881/8398080=25.524748633\ldots\),
  supporting “25.5.” The null \(p_0=6/11\) already appears in brief v7, commit `e414bb58`, dated **31 October, 09:14:26Z**, before C1b opened at seq 188, **10:42:10Z**.

### 2. Errors and consistency

There is **one citation-location error**: the sentence cites REPORT §8.2, whereas the explicit missing-window disclosure is in **§8.3, item 4** (`REPORT.md:271–272`). Section 8.2 supports the patch history. Citing “REPORT §§8.2–8.3” would cover both.

Otherwise, the change introduces no factual error or new inconsistency. It brings §5.1 into agreement with Table 2’s existing disclosure that C0 was not pre-registered. C1’s advance-fixed null remains compatible with the separately disclosed changes to its cap and attribution rule; the sentence does not assert that all criteria remained unchanged.

### 3. Disposition

The sentence now appropriately claims **less procedural compliance for C0**, without understating its recorded safety result or weakening the supported account of C1’s promotion. After forming this assessment, I read REVIEW-cold-19 and round 25; their substantive disposition agrees with the record, although both repeat the section-number mistake. That pinpoint-citation correction is nonblocking.

RECOMMENDATION: accept
