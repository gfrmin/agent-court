model: google/gemini-4-argon
branch: read-claim-paper-18

You are an anonymous referee checking the final change to a preprint for arXiv (cs.AI). Draft 29 was accepted by three referees. Draft 30 changes how the paper states its central mechanism, after a note from the project's counsel: the institution now grows only by test (a layer is frozen, and the next begun, only on passing), and the paper says that keys are not yet granted by test. Your task is to check the change from draft 29 to draft 30, and only that.

**Write no file anywhere, not even under `/tmp`, and commit or push nothing.** Run any script you write from standard input (`python3 - <<'PY' … PY`). A request to create a file or directory will be refused and will end your session before you report.

Let `U=https://raw.githubusercontent.com/gfrmin/agent-court`.
- **The change:** `curl -sL $U/538c44d834f66e0a04935a1685d9f73e8b39cb40/papers/claim/history/draft-d29.md` (draft 29) and `curl -sL $U/538c44d834f66e0a04935a1685d9f73e8b39cb40/papers/claim/draft.md` (draft 30). Diff them in memory, for example with `diff <(curl -sL …) <(curl -sL …)`.
- **Why:** `curl -sL $U/538c44d834f66e0a04935a1685d9f73e8b39cb40/papers/claim/REVIEW-counsel-1.md`; the checks are in `…/04-selfcheck.md`, round 23. Form your own view of each passage before you read the note.
- **The record:** this working directory is a clone of renavondata/jack. Read files as of the cited commit with `git show e580b64:<path>`, and use `git log` for commit dates.

For each changed passage, say:
1. whether every factual statement in it is backed by the record, the cited source or the paper's own computation (check, do not assume; in particular CHARTER §§6–8 at `e580b64` and at genesis `95679e7`, the C1a and C1b reports in `REPORT.md`, the opening of each window and every `key` entry in `log.jsonl`);
2. whether it introduces any error, or any inconsistency with the rest of draft 30;
3. whether the new statement of the design is the charter's own or is fitted to the record, and whether any sentence now claims more, or less, than the record shows.

Give the report as your final message, in at most 1,000 words, and print nothing after it. End with this line exactly: `RECOMMENDATION: <accept|minor revision|major revision|reject>`
