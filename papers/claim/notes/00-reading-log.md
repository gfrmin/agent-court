# Claim note — reading log

*Claim session, 25 November 2026. This file records what was read for the note and how far, so that the self-check in step 3 can say which comparisons rest on a full reading.*

## jack, at `origin/main` `e580b64` (log to seq 7809, 2026-11-25T11:05:35Z)

| Source | How far it was read |
|---|---|
| `CHARTER.md` (§§0–13 and A1–A6) | In full. |
| `SPEC.md` §§1–9 and §10 items 1–15 | §§1–9 in full. §10 items 1–15 and the paragraph on the promotion evaluator were read. |
| `README.md`, `REPORT.md` (C0 exit, C1a, C1b, C2a part 1) | Read. The README's status section is dated 5 November and stale. |
| `transcripts/BRIEF-C2a-3-draft.md` | Read to line 311. |
| `transcripts/AUDIT-criteria-20261117.md` | The summary and the table rows were read. |
| `transcripts/RESEARCH-self-similarity-20261105.md`, BRIEF-C2b and BRIEF-C2c | Read in part. |
| `LAW.md` and `tools/enforcement.json` | Read in part. |

What was run against the log:
- `log.jsonl` was parsed: counts by type and by proposer, and every genesis, key, push, amend and decision entry.
- `python3 tools/count_kernel.py --limit 500` gave 450 lines.
- `python3 judge/status.py --subject C2a --as-of 2026-11-25T11:05:35Z --runs transcripts/evidence/runs-tests-20261117T1010-historical.json` gave:
  - value E ≈ 1.5 × 10⁶⁰ over 2,820 events;
  - continued liveness E ≈ 10¹⁰ over 641 items;
  - this is read to C2a-prime's stated end, because change 6 is not built.
- The genesis charter hash was checked: `git show 95679e7:CHARTER.md | sha256sum` gives `383867d0…`, which equals the `body.charter` of seq 0.

The founding post is `gfrmin/gfrminsite` `content/posts/the-science-was-done/index.md`, published at `6926b8c` (2026-11-01 12:22 +0800). It was read in full.

## Competitors

| Work | Date | How far it was read |
|---|---|---|
| Sengupta, SEA, arXiv 2607.00871 | v1 1 Jul 2026 | §§1–11 in full; appendix pseudocode skimmed |
| Zhang et al., DGM, arXiv 2505.22954 | v3 12 Mar 2026, ICLR 2026 | §§1–6 in full; Appendix H in full; other appendices not read |
| Zhang et al., Hyperagents, arXiv 2603.19461 | v2 1 Nov 2026 | §§1–4 and §§6–7 in full; A.5 and Appendix G read; §5 results skimmed |
| Huang & Huang, ASG-SI, arXiv 2512.23760 | v1 28 Dec 2025 | In full |
| Neal, SFA-Bench v2.0.0-alpha.2 and AutoLab, github.com/iotaverbum-core/sfa-bench, DOI 10.5281/zenodo.20766587 | released 13 Jul 2026; last commit 25 Jul 2026 | README read; concept, claims-and-limitations and AutoLab items 1–4 read; the July 2026 policy paper's opening read |
| Wu et al., SGM, arXiv 2510.10232 | v1 11 Oct 2025, v2 17 Sep 2026 | Abstract and introduction |
| PACE, arXiv 2606.08106 | 6 Jun 2026 | Abstract, introduction and related work |
| Nakajima, Regimes, arXiv 2606.10241 | 8 Jun 2026 | Abstract and introduction |
| Roesner & Kohno, Trusting Trust Revisited, arXiv 2609.17817 | 15 Sep 2026 | Abstract and introduction |
| Bracale Syrnikov et al., Institutional AI, arXiv 2601.11369 | v2 20 Jan 2026 | Abstract |
| Qin et al., Governable Individuals, arXiv 2607.05463 | v2 15 Jul 2026 | Abstract |

Every competitor predates jack's genesis (14 October 2026). The note's priority claims are therefore confined to what none of them has.

Searches also turned up the following, none of which has yet been read beyond the search snippet:
- AgentBound, arXiv 2606.30970;
- the IETF draft-sato-soos-cap, the "Constitutional AI Protocol";
- PunkGo's "Right to History";
- Forecast-Dojo, arXiv 2609.28876.

A second, unrelated "SFA-Bench" exists, on state-fabrication attacks, at github.com/ThisisOmar-here/sfa-bench. The brief's "Neal, 2026" fixes the one meant: the CITATION.cff of iotaverbum-core/sfa-bench names Matthew Neal.
