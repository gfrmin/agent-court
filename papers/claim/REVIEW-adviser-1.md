# Adviser's audit of the release text against the record

Reader: Guy's adviser session (claude-opus-5-5, no key), 2026-11-26.
Text read: `claude/claim/release/law-before-the-agent.md`, as of 2026-11-26T05:23Z.
Method: each fact about the implementation was re-run against `renavondata/jack` at `e580b64e`. The log was read by `git show e580b64:log.jsonl`. The evaluator was run in a worktree of that commit, with the 919 successful `tests.yml` push runs on `main` paged from the API. I did not read the Lean files, the simulation, or the literature.

## Two corrections

1. **§5.1: "19 `key` entries by seq 7809, 13 of them before the first promotion at seq 188."**
   - The count is **14**, not 13. The `key` entries below seq 188 are seqs 1, 6, 7, 8, 22, 23, 31, 32, 33, 34, 48, 49, 51 and 82.
   - If seq 1 (the operator's own key) is meant to be left out, the text should say so.
   - The total of 19 is right.
2. **§4.4: "CI replays three of the table's 706 rows [`tests/promotion_replay_spot.py`]."**
   - The figures are right, but the citation is wrong. `tests/promotion_replay_spot.py` is not run by CI. Its name does not begin `test_`, so `python3 -m unittest discover -s tests` (`.github/workflows/tests.yml` line 31) skips it, as `transcripts/REVIEW-move-promotion-judge.md` Finding 2 records.
   - CI replays three rows through the `replay_drift` pin, run by `python3 pins/run.py` in the `pins` job (`tests.yml` line 44). The rows are fixed at line 49 of `pins/replay.py`: indices 300, 400 and 593.
   - Suggested citation: `pins/replay.py`, `replay_drift`.

## Held, by re-running

- **§6, the recomputation.** Run as `python3 -I block_on_log.py --rev e580b64`, it prints every figure the text gives:
  - 2,820 events; 2,795 reviewer and 12 builder forecasts;
  - 476 sittings done and 4 pending; 170 expired, 168 of them late; 19 non-members; 5 classes;
  - pooled finals 1.993e4 and 1.109e4, with the second class's peak at 1.19e4; thresholds 40 and 120;
  - per-dataset running maxima all 1;
  - 1.52e60, 2.49e58 and 1.74e10.
  - The orders-of-magnitude split comes out as 1.78, 48.16 and 5.94, as stated.
- **Table 2 and §6, the evaluator's output.**
  - C1b at its promotion (`--subject C1b --as-of 2026-11-01T11:31:58Z`): `live E 214358881/8398080 … items 9`.
  - The procedure-to-object ratio at the veto (`--subject C2a --as-of 2026-11-22T11:44:05Z`): `procedure 320 : object 1296`.
- **§4.3, the liveness items.** There are 190 of 641 sharing a timestamp: 188 expiries and 2 batches. Check: `item_process` at `e580b64e`, items after the gate of 2026-10-31T13:32:21Z.
- **§4.3, seqs 550–563.** These are fourteen resolutions, all between 12:15:08Z and 12:15:58Z on 2 November.
- **The log facts.**
  - The genesis is at 2026-10-14T05:41:39Z, and the log holds 7,810 entries to seq 7809.
  - Seqs 6–8 are key entries of 19 October, and the powers at seqs 6, 34, 51 and 201 are as stated. Seq 33 holds `forecast`.
  - Seqs 188, 337, 367, 5563, 5564, 6851, 7180, 7281 and 7615 are of the types and dates given.
  - There are 0 `rule` entries.
  - Builder and reviewer entries number 6,621; their forecasts and resolutions 5,919; their proposals 702.
- **Code facts.**
  - The kernel is 450 lines (`tools/count_kernel.py`).
  - `judge/value.py` updates the stake and the weights per event inside lines 113–135.
  - `spec/vectors/promotion-replay.json` has 706 rows.

## Not checked

- The 622 stream proposals and the split of the other 80, which depend on how the titles are classed.
- The C2a first-window account (nine rows, eight the court's), which I take from the brief.
- The kernel2 authorship trailers.
- Everything outside the repository: the literature, the proofs and the simulation.
