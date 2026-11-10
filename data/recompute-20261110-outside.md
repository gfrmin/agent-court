# Recomputation of 10 November 2026 — the outside session's figures

*An outside session (`claude-fable-5-1`, Guy's claude.ai session; no key on the court, not the author session), for the additions of 10 November (appendix A §§A.19–A.25; chapters 8 §8.3, 12 §§12.2, 12.5, 12.10; 15 §§15.14–15.16; 16 §16.2; front matter; afterword). Every figure is a fold over `log.jsonl` at `renavondata/jack` `main` `4f1a9eadfbeecbe6e7bc1533a64326c8ea02a986` (2026-11-09T15:52:21+02:00, "Merge pull request #702"), read from a clone with 2,500 commits of history fetched. Folds that `tools/check_book.py` can express are registered in `data/facts.toml` under the `4f1a9ea` group; the two that read `args` members are not, and carry their tag in the text unchecked.*

## The folds

| figure | filter | value | registered |
|---|---|---|---|
| entries on the log | all | 2,950 (last `ts` 2026-11-09T15:42:42Z) | no (not printed) |
| forecasts | `type = forecast` | 1,129 | `fact.forecasts_4f1a9ea` |
| resolutions | `type = resolution` | 1,045 | `fact.resolutions_4f1a9ea` |
| `world.renavon` forecasts | `type = forecast`, `body.type = world.renavon` | 949 | `fact.renavon_forecasts_4f1a9ea` |
| `world.hkjc` forecasts | `type = forecast`, `body.type = world.hkjc` | 45 | no (not printed) |
| `counsel.programme` forecasts | `type = forecast`, `body.type = counsel.programme` | 73 | `fact.counsel_programme_forecasts_4f1a9ea` |
| `world.renavon` forecasts by proposer | as above, by `proposer` | reviewer 931, builder 18 | no (printed as "931 of them from one template under the reviewer's key") |
| `world.renavon` forecasts carrying `args.model` | as above, `"model" in body.args` | 931 | no — `args` members are outside the fold filters |
| resolution body members beyond `forecast, outcome, evidence` | union over all resolutions | none | no — printed as "carry no member beyond the three the schema requires" |
| `amend` entries | `type = amend` | seqs 4 (A2), 30 (A3), 67 (A4), 137 (A5) | not printed |

## The script

```
python3 -I - <<'EOF'
import json, collections
E = [json.loads(l) for l in open('log.jsonl')]
f = [e for e in E if e['type'] == 'forecast']; r = [e for e in E if e['type'] == 'resolution']
print(len(E), E[-1]['ts'], len(f), len(r))
print(collections.Counter(str(e['body'].get('type')) for e in f).most_common())
wr = [e for e in f if e['body'].get('type') == 'world.renavon']
print(len(wr), sum('model' in e['body'].get('args', {}) for e in wr), collections.Counter(e['proposer'] for e in wr))
print(sorted(set(k for e in r for k in e['body']) - {'forecast', 'outcome', 'evidence'}))
print([(e['seq'], e['body']['id']) for e in E if e['type'] == 'amend'])
EOF
```

## What the figures are used for, and what they are not

They establish three facts the additions rest on: that most of the ledger is one scheduled stream on the owner's catalogue (949 of 1,129); that no resolution records who read the page or by what path (1,045 bodies, three members each); and that no forecast records the text it was entered under (the `args` keys of `world.renavon` forecasts are `dataset, url, window_utc, hour_hkt, model, stream, base_rate_permille, base_rate_population, evidence, resolution_evidence`; no hash of a world-type paragraph). They establish nothing about any window's criteria, which need `status.py` on a full-history clone and the committed evidence files (`plan.md` §2), and the additions cite no such figure except ones already registered by the author (chapter 12 §12.5 reuses `fact.c2a_value_at_1076`).

## A correction to the outside session's own earlier note

The re-rated map of 9 November (`RESEARCH-semantics-map-20261109.md`, delivered to the owner; not in this repository) said in its row 38 note and in the session's message on G4 that the HKJC per-race stream is "also court-scheduled". `transcripts/world-types.json` at `4f1a9ea` declares `world.hkjc` `scheduled_by: "none"` (hand-filed sessions, no stream template) and `world.renavon` `scheduled_by: transcripts/sessions/stream-forecast.md`. The point the note made — that *scheduled* and *operated* are different properties and the declaration records only the first — stands; the example was wrong, and chapter 15 §15.16 states it correctly.
