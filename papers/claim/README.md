# The claim paper (draft, not the book)

This branch holds the draft of the arXiv paper on jack's theory, "Law Before the Agent". It was written at Guy's request by the claim session, which holds no key on jack. The draft lives here only so that a cold reader from another model family can fetch it on steel. It is not part of the book, and `master` is untouched.

- `draft.md`: the paper, draft 29, the release candidate (cold reads 15 and 16's verified edits; draft 28 stated the scope as a design and an audit, at Guy's choice of 28 Nov 2026; earlier: adversarial read 2's verified fixes; paragraph pass and adversarial read 1; earlier: cold read 13 accepted draft 23; three of its final edits; cold read 12's corrections; cold read 11's corrections; cold read 10 accepted draft 20; its clarifications are in; cold read 9 and the adviser's answers; two fixes from the adviser's audit; strongest backed claims, not softened ones; kernel authorship checked per revision; held to its abstract since draft 12; revised for cold read 8, which accepted; stands alone, citing the book once as provenance).
- `ABSTRACT-FIRST.md`: the paper's one idea, contributions and abstract, fixed before the text.
- `lean/`: the machine-checked core (Lean 4 + Mathlib; `lake build`).
- `READ-PROMPT.md`: the instructions for the outside cold read.
- `sim_filtration.py`: the simulations behind the examples in §4.3.
- `block_on_log.py`: the block-form recomputation in §7 (`python3 block_on_log.py --rev e580b64` in a jack checkout).
- `REVIEW-cold-1.md`: cold read 1 (gpt-6.1-sol, opencode-runner #1348) with its disposition.
- `REVIEW-cold-2.md`: cold read 2 (gemini-4-argon, opencode-runner #1362) with its disposition.
- `REVIEW-cold-3.md`: cold read 3 (gpt-6.1-sol, opencode-runner #1364) with its disposition.
- `REVIEW-cold-4.md`: cold read 4 (gemini-4-argon, #1365), a backing audit, with its disposition.
- `REVIEW-cold-5.md`: cold read 5 (gpt-6.1-sol, #1368) with its disposition.
- `REVIEW-cold-6.md`: cold read 6 (gemini-4-argon, #1369) with its disposition.
- `REVIEW-cold-7.md`: cold read 7 (gpt-6.1-sol, #1371) with its disposition.
- `REVIEW-cold-8.md`: cold read 8 (gemini-4-argon, #1372), accept, with its disposition.
- `REVIEW-cold-9.md`: cold read 9 (gpt-6.1-sol, #1375), with its disposition and the adviser's answers.
- `REVIEW-cold-10.md`: cold read 10 (gemini-4-argon, #1381), accept, with its disposition.
- `REVIEW-cold-11.md`: cold read 11 (gpt-6.1-sol, #1385), with its disposition.
- `REVIEW-cold-12.md`: cold read 12 (gpt-6.1-sol, #1387), with its disposition.
- `REVIEW-cold-13.md`: cold read 13 (gpt-6.1-sol, #1388), accept.
- `REVIEW-cold-14.md`: cold read 14 (gpt-6.1-sol, #1389), accept: the final change, draft 23 to 24.

The working notes are in Guy's Project under `claude/claim/`: the outline, reading log, self-reviews, self-check and LaTeX build.
- `REVIEW-adversarial-1.md`: adversarial read 1 (gpt-6.1-sol, #1394), reject, with its disposition.
- `07-paragraph-review.md`: the claim session's paragraph-by-paragraph pass of draft 24.
- `04-selfcheck.md`: every factual claim checked against its source, round by round.
- `REVIEW-adversarial-2.md`: adversarial read 2 (gpt-6.1-sol, #1400), reject, with its disposition.
- `REVIEW-cold-15.md`: cold read 15 (gpt-6.1-sol, #1446), minor revision, on the release candidate (draft 28), with its disposition.
- `REVIEW-cold-16.md`: cold read 16 (gemini-4-argon, #1447), accept, on the release candidate (draft 28), with its disposition.
