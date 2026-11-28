# Cold read 17 of the claim paper: report and disposition

- **Reader:** `openai/gpt-6.1-sol`, renavondata/opencode-runner #1448, on 28 November. It checked only the change from draft 28 to draft 29, which holds cold reads 15 and 16's edits.
- **Text read:** the diff between `7335140` (draft 28) and `00a0307` (draft 29).
- **Verdict:** **accept**. It checked all fourteen changed passages against the record, the cited sources and the recomputation, and found that every one is supported and introduces no error or inconsistency.
- **Disposition:** no change. Draft 29 is the final text.

## The report (verbatim)

# Referee report: draft 28 → draft 29

**The changes are supported and resolve the substantive points raised by referees 15 and 16. I found no newly introduced error or inconsistency requiring revision.** This assessment is confined to the changed passages. I compared the two drafts, inspected the cited record at `e580b64`, reran the ancillary recomputation, checked the relevant literature, and independently counted runner issue titles.

1. **Table 1: “with recorded departures.”**  
   Supported. SPEC §10 records three departures from the pre-stated counted-line cap, including the increase after C1b opened. The qualification brings the table into agreement with §4.3 rather than presenting an exceptionless prospectivity claim. Referee 15’s point is resolved.

2. **Proposition 1(b): unequal-length logs.**  
   Correct. Position-numbering from zero means unequal-length logs have different terminal `seq` values, hence different terminal lines. If both terminal lines hash to \(h\), they immediately furnish a collision. The equal-length backward argument remains valid. The shorter proof introduces no inconsistency and resolves the requested clarification.

3. **The cutoff filtration.**  
   Explicitly including earlier resolved-subset identities, outcomes, scores and stakes supplies the information needed by the subsequent resolved-subset statistic and predictable stake construction. The increasing-filtration statement is consistent with accumulated cutoff records and assumption (A). This makes the intended mathematical setup explicit without changing the theorem. Resolved.

4. **Interpretation of rejecting the value null.**  
   “Is evidence that,” with the level specified, correctly replaces the deductive-sounding “shows.” Rejecting the pointwise null supports an advantage somewhere, without establishing persistence or superiority to a finer baseline. This agrees with Choe–Ramdas’s strong/weak-null distinction and draft 29’s limitations. Resolved.

5. **The split Remark.**  
   This is a paragraph break only. The filtration argument, conditional-independence alternative and joint-versus-marginal distinction retain their previous content. No factual or mathematical change is introduced. The readability request is adequately addressed.

6. **Batched liveness as an unfinished operational definition.**  
   The new sentence accurately states the consequence of leaving the batch-versus-expiry unit unspecified: the proposed batching rule is not yet deployable. It does not undermine the generic conditional theorem. I also reproduced the accompanying implementation counts: **641 items**, with **190** sharing timestamps—**188 expiries and two batches**. The strengthened disclosure resolves referee 15’s point and is consistent with the paper’s design-and-audit scope.

7. **Repair typing and the `window_fixes` date.**  
   Supported, with an important historical distinction now correctly preserved. Following the file’s move from `tools/status.py` to `judge/status.py` confirms that the repair-predicate line entered in `879caf93` on **31 October**, during C1b, and remains unchanged. Commit `4c1f9c97` adds the window-fix exception and has **author date 11 November**; its committer date is 12 November UTC. Thus “added on 11 November” is supported as the authored-change date, without claiming deployment that day. The exception suppresses late reporting and clears qualifying taint at a subsequent push while leaving the repair predicate intact. Referee 16’s point is resolved.

8. **Whole-word proposal-title counting.**  
   Recounting gives **6,621** builder/reviewer entries, **5,919** forecasts/resolutions, **5,811** stream forecasts/resolutions, and **702** proposals. Of these proposals, **627** have the specified stream-title prefixes; among the remaining **75**, whole-word `read`/`review` matching, excluding seqs 654 and 657, gives **46**. The revised wording accurately excludes “reviewer.” Resolved.

9. **Table 3 and its introductory paragraph.**  
   The requested script reproduces:
   \[
   1.51983\times10^{60},\quad
   2.492\times10^{58},\quad
   1.739\times10^{10},\quad
   1.993\times10^4.
   \]
   Successive logarithmic reductions round to **1.8, 48.2 and 5.9 orders**, totaling approximately **56**. The event and scoring descriptions match the computation; the stated 5.9 events per sitting is supported. The explicit noncausal qualification appropriately covers simultaneous changes in samples, scoring and betting structure. Resolved.

10. **Falsifier summary and introduction of assize.**  
    CHARTER §§1 and 12 support both the four-item list and assize’s identity as the earlier repository supplying the baseline. The revised summary accurately distinguishes tested, untested and literally met clauses. Independently scanning complete half-open 14-day intervals reproduces the worst **63:5** ratio at genesis and the post-seq-31 maximum **872:1,755**. The rewrite introduces no inconsistency and resolves the explanatory/readability points.

11. **The three acts tables.**  
    Direct `class` counts reproduce **7→1**, **61→1** and **81→9** for `acts-20261101`, `acts-20261103` and `acts-20261103T2144`, respectively. Amendment 2 supports attribution by declaration. The named pairs now eliminate the ambiguity between the two 3 November tables. Resolved.

12. **Score decomposition and citation placement.**  
    Bröcker’s equation (13) explicitly decomposes expected score into uncertainty, resolution and reliability; Table 1 includes logarithmic “Ignorance.” The revised wording is accurate in this finite-outcome setting. Moving Choe–Ramdas’s citation to sequential comparator testing removes the erroneous implication that it supplies the resolution/calibration decomposition. Both referees’ points are resolved.

13. **Potential performativity.**  
    “Exposes the stream” correctly describes capacity for influence rather than evidence that influence occurred. The operator’s three forecasts are all `world.assize`. The change is consistent with Table 1 and resolves referee 15’s objection.

14. **Disclosure count.**  
    Using the stated observation endpoint, I counted **965** builder/reviewer issues; **853** name a model under a straightforward title parser, including **720** naming `gpt-5.4-mini`. Thus “720 of about 850” is supported, and the frozen endpoint and parsing qualification resolve the request.

RECOMMENDATION: accept
