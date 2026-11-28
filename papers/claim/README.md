# The claim paper: "Law Before the Agent"

This branch holds the arXiv paper on jack's theory and everything behind it. It was written at Guy's request by the claim session, which holds no key on jack. The paper is not part of the book, and `master` is untouched.

## The paper

- `draft.md`: draft 32 of 28 November 2026, the final text. It restates the design as growth by test (a layer frozen, and the next begun, only on passing), after counsel's note (`REVIEW-counsel-1.md`), adversarial read 3 and cold reads 18–20. Draft 29, the earlier release candidate, is `history/draft-d29.md`.
- `ABSTRACT-FIRST.md`: the paper's one idea, contributions and abstract, fixed before the text was written.
- `release/law-before-the-agent.md`: the gfrm.in post (Hugo, `draft: true`). The line `arXiv:XXXX.XXXXX` needs the real identifier.
- `release/arxiv-metadata.md`: the title, the ASCII abstract to paste, comments, categories and licence.

## Ancillary files (these go to arXiv in `anc/`)

- `lean/`: the machine-checked core (Lean 4 + Mathlib; run `lake build`). Its README maps propositions to theorems.
- `sim_filtration.py`: the simulations of §4.3.
- `block_on_log.py`: the recomputation of §6. Run it in a jack checkout as `python3 block_on_log.py --rev e580b64`; it writes nothing.
- `04-selfcheck.md`: every factual claim checked against its source, round by round (rounds 1–25).

## Building the release

`build/release.sh` writes `build/release/`, which git ignores. It holds:
- `law-before-the-agent.pdf`;
- `law-before-the-agent-arxiv.tar.gz`, the tarball to upload, compiled once in a clean directory as arXiv would (pdflatex, no BibTeX);
- the post and the metadata.

```sh
cd papers/claim/build
CLAIM_EMAIL=mail@gfrm.in CLAIM_DATE="November 2026" ./release.sh
```

It needs Python 3, pandoc, pdflatex with TikZ, and `pdfinfo`. Its parts:
- `md2tex.py` converts `draft.md` to `paper.tex`;
- `figure.tex` is the construction diagram;
- `release_md.py` writes the post and the metadata.

## The reviews

Each review file holds its disposition table, followed by the reader's report verbatim.

| Read | Model | Runner issue | Verdict | Note |
|---|---|---|---|---|
| `REVIEW-cold-1.md` | gpt-6.1-sol | #1348 | major revision | |
| `REVIEW-cold-2.md` | gemini-4-argon | #1362 | major revision | |
| `REVIEW-cold-3.md` | gpt-6.1-sol | #1364 | major revision | |
| `REVIEW-cold-4.md` | gemini-4-argon | #1365 | minor revision | a backing audit |
| `REVIEW-cold-5.md` | gpt-6.1-sol | #1368 | minor revision | |
| `REVIEW-cold-6.md` | gemini-4-argon | #1369 | minor revision | |
| `REVIEW-cold-7.md` | gpt-6.1-sol | #1371 | minor revision | |
| `REVIEW-cold-8.md` | gemini-4-argon | #1372 | accept | |
| `REVIEW-cold-9.md` | gpt-6.1-sol | #1375 | minor revision | with the adviser's answers |
| `REVIEW-cold-10.md` | gemini-4-argon | #1381 | accept | |
| `REVIEW-cold-11.md` | gpt-6.1-sol | #1385 | minor revision | |
| `REVIEW-cold-12.md` | gpt-6.1-sol | #1387 | minor revision | |
| `REVIEW-cold-13.md` | gpt-6.1-sol | #1388 | accept | draft 23 |
| `REVIEW-cold-14.md` | gpt-6.1-sol | #1389 | accept | the change from 23 to 24 |
| `REVIEW-adversarial-1.md` | gpt-6.1-sol | #1394 | reject | draft 24, hostile brief |
| `REVIEW-adversarial-2.md` | gpt-6.1-sol | #1400 | reject | draft 26, hostile brief |
| `REVIEW-cold-15.md` | gpt-6.1-sol | #1446 | minor revision | draft 28, all edits taken |
| `REVIEW-cold-16.md` | gemini-4-argon | #1447 | accept | draft 28, all edits taken |
| `REVIEW-cold-17.md` | gpt-6.1-sol | #1448 | accept | the change from 28 to 29 |
| `REVIEW-adversarial-3.md` | gpt-6.1-sol | #1456 | reject | draft 30, hostile brief; concedes the promotion/key distinction |
| `REVIEW-cold-18.md` | gemini-4-argon | #1457 | minor revision | the change from 29 to 30, all points taken |
| `REVIEW-cold-19.md` | gpt-6.1-sol | #1459 | minor revision | the change from 30 to 31; its one sentence taken |
| `REVIEW-cold-20.md` | gpt-6.1-sol | #1460 | accept | the change from 31 to 32 |

Both adversarial reads rejected on one ground: the mechanism that grants powers by test is neither implemented nor evaluated. Guy chose on 28 November to publish the paper as a design and an audit. The paper says so in its abstract, §1 and §8.

Three more reviews:
- `REVIEW-adviser-1.md`: the adviser's audit of the release text against the record.
- `REVIEW-adviser-2.md`: the adviser's answers to `notes/QUESTIONS-to-counsel-1.md`.
- `REVIEW-counsel-1.md`: counsel's note on windows and tests, with its disposition (draft 30).
- `07-paragraph-review.md`: the claim session's paragraph-by-paragraph pass over draft 24.

## Working record

- `prompts/`: the exact prompt of every read filed through the courier on renavondata/opencode-runner.
  - `runner-read-N.md` is cold read N; `11b` re-ran read 11.
  - `A1`, `A2` and `A3` are the adversarial reads; `A2b` re-ran A2 on GPT after a Gemini server error.
  - `READ-PROMPT.md` is the first cold-read prompt.
- `history/`: earlier drafts, `draft-d4.md` to `draft-d31.md`, and `draft-r3-before.md`.
  - Drafts 1–3 and 16 were not kept as separate files.
  - Drafts 20 to 29 are also in this branch's commits.
- `notes/`: the claim session's working notes:
  - the reading log and the outline;
  - the first self-review;
  - the questions put to counsel;
  - `issue-book.md`, notes on the book that arose while writing.

Guy's Project, under `claude/claim/`, mirrors most of this. The Project's `02-draft.md` and `release/law-before-the-agent.md` are pointers to this branch.
