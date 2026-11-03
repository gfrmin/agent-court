# Author's recomputation, 3 November 2026

Clone of `renavondata/jack`, `main` at `6b800e14fc80eaf22137de6aa739a483c5a7f552` (2026-11-03T04:26:46Z), history fetched to 1,190 commits (`git fetch --depth=2000 origin main`; a shallow clone makes `tools/status.py` fail with "historical tree unverified"). Python 3.13. Nothing was signed, entered, fetched from GitHub's API or pushed.

## Structure of the log

```
python3 -I -c 'fold over log.jsonl'
entries 807
by type: genesis 1, key 17, push 7, decision 7, amend 4, proposal 128, merge 123, forecast 311, resolution 209
by proposer: guy 48, builder 219, counsel 138, reviewer 266, herald 136
first seq by type: genesis 0, key 1, push 2, decision 3, amend 4, proposal 10, merge 11, forecast 37, resolution 52
```

Genesis [seq 0]: `ts` 2026-10-14T05:41:39Z, proposer `guy`, charter `383867d0…`, checker `d3ac5ef5…`, one key `guy-master` with powers `genesis key proposal merge`.

The sovereign's entries (type `key`, `push`, `decision`, `amend`), by seq:

| seq | ts | type | body |
|---|---|---|---|
| 1 | 2026-10-18T14:40:56Z | key | guy-master → genesis key proposal merge amend push decision |
| 2 | 14:42:38Z | push | digest f77c28e5… |
| 3 | 2026-10-19T04:33:05Z | decision | transmute A2 |
| 4 | 04:33:38Z | amend | A2, activate_at 5 |
| 5 | 04:36:23Z | push | 1db66ff0… |
| 6–8 | 05:43–05:44Z | key | builder-1 (proposal, spec_conflict); reviewer-1 (proposal); counsel-1 (proposal) |
| 9, 12 | 19 Oct 06:00Z; 20 Oct 02:06Z | push | bf9a798d…; ba8f9a77… |
| 22, 23 | 24 Oct | key | counsel-2; reviewer-2 (proposal) |
| 28 | 2026-10-24T20:53:36Z | decision | transmute A3 |
| 29 | 2026-10-25T16:16:20Z | push | 606e6562… (C1a's installing push) |
| 30 | 16:44:10Z | amend | A3, activate_at 31 |
| 31–34 | 16:50–16:51Z | key | counsel-2 +forecast; reviewer-2 +forecast +resolution; guy-master +forecast +resolution; builder-2 |
| 48, 49 | 26 Oct 07:09Z | key | counsel-2 +resolution; builder-3 |
| 50 | 2026-10-26T08:58:22Z | decision | budget "C1b: 4 Guy-hours/week; USD 300/month; windows 14 days" |
| 51 | 09:10:19Z | key | herald-1 (merge) |
| 66, 67 | 2026-10-27T07:03–07:04Z | decision, amend | transmute A4; A4, activate_at 68 |
| 82 | 28 Oct 09:40Z | key | herald-1 +resolution |
| 136, 137 | 2026-10-30T09:59Z | decision, amend | transmute A5; A5, activate_at 138 |
| 188 | 2026-10-31T10:42:10Z | decision | promote C1a |
| 197 | 13:04:49Z | push | 30976b3b… (cap 6,900) |
| 201 | 13:48:22Z | key | herald-2 (merge) |
| 216, 217 | 16:02Z | key | builder-3 → []; herald-1 → [] |
| 337 | 2026-11-01T11:31:58Z | decision | promote C1b |
| 367 | 15:04:14Z | push | afe633a2… (C2a's opening; cap 7,800) |

## Kernel

```
python3 tools/count_kernel.py
kernel/__init__.py 0; kernel/check.py 138; kernel/log.py 172; kernel/sig.py 140; total 450
```

Other sizes, `wc -l`: `judge/judge.py` 320; `harness/diff.py` 62 (bound 65, SPEC §9a.6); `tools/clerk.py` 88; `tools/value.py` 181; `tools/status.py` 450.

## Windows

C1a at its exit prefix:

```
python3 tools/status.py --subject C1a --as-of 2026-10-31T10:42:10Z --runs transcripts/evidence/runs-tests-20261031.json
window C1a: 2026-10-25T16:44:10Z .. 2026-10-31T10:42:10Z (prefix to seq 188)
criteria 1–6 met; forecasts 63/20; proposers 4/3; resolutions 19/10; world-typed with evidence 12/5
A3.4 ratio: procedure 127 : object 32; J7: 0 of 63 unresolved past resolves_by
promote C1a: lawful
```

C1b at its exit prefix:

```
python3 tools/status.py --subject C1b --as-of 2026-11-01T11:31:58Z --runs transcripts/evidence/runs-tests-20261101b.json --acts transcripts/evidence/acts-20261101.csv
window C1b: 2026-10-31T10:42:10Z .. 2026-11-01T11:31:58Z (prefix to seq 337)
criteria 1–7 met; counted 6882/6900; kernel 450/500; attack green 2026-10-31T13:32:21Z
criterion 5: live E 214358881/8398080 >= 20; items 9
A3.4 ratio: procedure 67 : object 82; late-reported repairs 0; off-log repairs 0; J7: 0 of 48
promote C1b: lawful
```

C2a, as of 2026-11-03T04:34Z, with the committed evidence only:

```
python3 tools/status.py --subject C2a --runs transcripts/evidence/runs-tests-20261101b.json
window C2a: 2026-11-01T15:04:14Z .. 2026-11-15T15:04:14Z (prefix to seq 806)
criterion 4: attack green on main before first scored cutoff: unverified SHORT
criterion 5: value E 1.000000 >= 20 SHORT     (0 events: the gate is unverified from committed evidence)
criterion 6: continued liveness E 41144777789250865278081232758997200423491/28618374016028403579210301440000000000000 (≈ 1.44) over 40 items SHORT
criterion 7: off-log repairs: unknown (no acts file)
A3.4 ratio: procedure 170 : object 269
J7: 6 of 191 window forecasts unresolved past resolves_by (seqs 442–447, builder, due 2026-11-02T05:00:00Z)
```

**Not for any draft** (gate waived; the tool's own label is "illustrative fixture only"):

```
python3 tools/value.py --no-attack-gate
value: E 20.131519 over 114 events; window events 114
```

This figure is recorded here so that the book's chapter 4 can be checked against the gated figure when counsel's `data/C2a-exit.md` names the committed run. If the two differ, the difference is the events whose cutoffs fell before the attack tests were green, which BRIEF-C2a says are reported and not scored.
