# Cold read 19 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, renavondata/opencode-runner #1459, on 28 November. It checked the change from draft 30 to draft 31 only.
- **Verdict:** **minor revision**. Every change was backed by the record. Its checks:
  - Amendment 2 is commit `5829399d`, 1 November 10:33:43Z, before C1b closed at 11:31:58Z.
  - A5 entered at seq 137 on 30 October, during C1a's window.
  - C2b grants no key.
  - The C2b branches were pre-built.
  - Minsky & Ungureanu 2000 is confirmed by Crossref.
  - M = 214358881/8398080 ≈ 25.52 was recomputed.
- **The one remaining point:** one sentence overclaims. It said both layers were promoted "under the charter's rule", but C0 had no pre-stated window and was patched in place (REPORT §8.2). Draft 32 takes the reader's own wording for that sentence. No other change was needed.

## The report (verbatim)

## Referee report: draft 30 → draft 31

The revision substantially resolves the two referees’ checkable objections. I found one remaining overstatement in the rewritten §5.1 that merits a small correction. This recommendation concerns the change alone, not the hostile referee’s broader publication objections.

I compared the drafts in memory, examined the implementation at `e580b64`, checked amendment dates using `git log`, queried Crossref, and reran the supplied record computation. I formed my initial assessment before reading the reviews and round-24 self-check.

### 1. Abstract, Contributions 1 and 3, §7’s self-amendment paragraph, §8’s comparison, and §9

**Backed and improved.** CHARTER §6 distinguishes promotion from capability grants, which §7 reserves separately to the operator. Replacing the contrast between keys granted “as windows open” and keys earned “on passing” removes a misleading implication: trial powers must already be available during their test.

“Each layer after the record” correctly excludes C0’s safety-only case. CHARTER A3.2 explicitly makes C1a and C1b **two windows of C1**, with the layer promoted at C1b’s exit. C1a’s exact exit criteria therefore do not contradict the statistical condition on C1’s eventual promotion.

The revised §8 correctly removes test-gated key grants as a prerequisite for evaluating the actual design. The abstract, contribution summary and conclusion now consistently describe the absence of a key/promotion rule. These changes resolve the cold referee’s substantive tension without inventing an implementation achievement.

### 2. Machine-checked-core paragraph: Proposition 6

**Correct correction.** Proposition 6(a) is conditional on the specification’s admission requirement, not a fully implemented code guarantee. `pins/replay.py:49` selects only rows 300, 400 and 593; `judge/judge.py` checks the qualifying grant/specification relationship rather than performing the entire quantified replay.

The replacement agrees with §4.4’s explicit partial-enforcement account and resolves the hostile referee’s objection. It appropriately claims less than draft 30.

### 3. §4.3 and Table 2: changing criteria during windows

**The added history checks out.**

- SPEC §10 records the three cap increases against prior statements: 4,500→5,500→6,200→6,900. BRIEF-C1b Amendment 1 records the last increase at seq 197.
- C1b opened at seq 188, **31 October 10:42:10Z**. Seq 197 occurred at **13:04:49Z** that day.
- Amendment 2’s attribution-by-declaration rule appears in commit `5829399d`, dated **1 November 10:33:43Z**, before C1b closed at seq 337, **11:31:58Z**. It was therefore adopted during the window, before exit evaluation.
- C1a began from A3’s 25 October entry/activation and originally ended **8 November 16:44:10Z**. A5 entered at seq 137 on **30 October 09:59:31Z**, activating at 138. C1a closed on **31 October** under that newly available early-ending rule.

The revised paragraph and table now disclose these departures rather than presenting entirely frozen measurement. “Every pre-stated criterion met” in C1a’s row is defensible alongside the explicit A5 qualification: the substantive criteria held, but the permissible closing time changed.

### 4. §5.1: promotion history and numerical evidence

**The layer/window correction and computation are sound.** My item-fold recomputation produced nine successful C1b items, at distinct timestamps, and
\[
M=214358881/8398080=25.524748633\ldots .
\]
The null \(p_0=6/11\) was committed before opening. The record also confirms 19 `key` entries through seq 7809, 14 before seq 188, and the stated opening/promotion order.

**One sentence overclaims:** “Two layers have been promoted, each under the charter’s rule: C0 … on safety alone …”.

C0 fits the charter’s **safety-only statistical exemption**, but did not fully follow its promotion procedure. `REPORT.md:271–272` expressly says no C0 window was stated and the layer was patched in place. Table 2 acknowledges the missing preregistration, so the new blanket wording creates an avoidable tension.

Replace it with, for example:

> Two layers have been promoted: C0 on safety criteria, without a pre-stated window, and C1 at C1b’s exit on a sequential liveness test.

This preserves the valid answer to the C1a objection without implying clean procedural compliance by C0.

### 5. §5.1: prebuilding and C2b keys

**Both factual corrections pass.** BRIEF-C2b:689–696 explicitly describes pre-built code and five branches awaiting the opening push. Restricting the claim to window opening resolves the false assertion that nothing was built beforehand.

Amendment 10 clause 3 strikes the proposed `herald-2` forecast-power grant; RUNBOOK:277–278 confirms that the election is tested, not run, with no such power. Removing “C2b’s keys would be its first case” is necessary and sufficient. The proposed predecessor-promotion gate is clearly hypothetical, not an implemented rule.

### 6. Independence remark and §6’s interpretation

**Supported.** Freezing forecasts as well as stakes supplies the missing qualification for the conditional-independence alternative.

The revised conditional-advantage sentence matches the strong null actually tested. My replay reproduced pooled-base crossings and no dataset-base wealth above 1. The numerical gaps are **55.88** and **48.16** orders of magnitude. “Accounts for 48,” read with the adjacent non-causal disclaimer, is acceptable descriptive wording; it does not establish isolated causal attribution.

### 7. Minsky–Ungureanu citation

**Verified.** Crossref confirms authors, July 2000, title and subtitle, *ACM TOSEM* **9(3):273–305**, and DOI **10.1145/352591.352592**. Its abstract supports the added description of explicit policies enforced through a generic mechanism over heterogeneous agents. The citation introduces no unsupported statistical novelty claim.

RECOMMENDATION: minor revision
