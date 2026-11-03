# Counsel → author: dispositions and evidence notes

*Counsel (jack's counsel session); append-only, dated sections. Counsel writes only this file and `data/<layer>-exit.md` here. Findings arrive as issues labelled `finding` and are answered on the issue; this file carries the evidence calendar and anything longer than a comment. Moved here from the Project's `claude/book/data/counsel-notes.md` on 3 November.*

## 3 November 2026, 05:30Z (from the Project copy)

- **F1 (`LAW.md` maps the charter at C0)** — accepted. Counsel brings `LAW.md` to the current layer in the same pull request as the C2a report (due by 4 Nov 06:00Z, `transcripts/COUNSEL-DUE.jsonl` row `c2a-report`). Until then cite the code and `tools/enforcement.json`.
- **F2 (the C2a value statistic cannot be recomputed)** — accepted; discharged by counsel's exit-evidence pull request at C2a's crossing: `transcripts/evidence/runs-tests-<date>.json` with every `tests` run to that instant, including the first green `main` run holding `tests/test_value.py` (counsel's working attack instant is `--attack-green 2026-11-01T15:59:44Z`, which the committed file lets you verify rather than take). `data/C2a-exit.md` will name the file, the commit and the exact invocations.
- **F3 (no acts file for C2a)** — accepted; same pull request: `acts-<date>-raw.csv`, the attributed `acts-<date>.csv` and the classifier's SHA-256.
- **E1** — Guy's to decide; counsel has told him.
- **Timing**, as counsel's forecasts on the ledger state them: both C2a processes ≥ 20 before 2026-11-03T18:00Z p 0.5 (RM-7), before 2026-11-04T00:00Z p 0.85 (RM-8). At 03:25Z: value *E* 12.6 over 108 events, continued liveness *E* 1.15 over 39 items (not citable until F2's file lands).
- **For chapter 5:** BRIEF-C2b Amendment 1 (cap 9,000 → 9,800 before the opening) merged as jack PR #207 at 05:11Z; its read `transcripts/REVIEW-C2b-am1.md` is running. Counsel's X6 (exit count under 9,000 nonetheless, p 0.45) is on the ledger with it.

## 3 November 2026, 06:00Z

- **Amendment 1 read: ACCEPT WITH OBLIGATIONS** (`transcripts/REVIEW-C2b-am1.md`, merged to jack `main` as PR #212). The reviewer's own count is about 1,495 new counted lines against 2,016 of headroom under 9,800 (F26); its delivery forecast under the new cap is 0.70 by 30 November.
- **Counsel's error, for the record (F25):** counsel's Amendment 1, its PR body, the opening note and SPEC's cap-history clause quoted the sixth read's fit forecast as 0.40. It is **0.55** (seq 633); 0.40 was the fifth read's (seq 612). The signed entries are untouched; the opening note and the SPEC clause on `push-c2b-9000` are corrected (prose only; cap and workflow unchanged); the brief's Amendment 1 keeps its wording, since an edit would need a fresh read, and this note and the C2a report carry the correction. Chapter 5 should quote seq 633, not the amendment.
