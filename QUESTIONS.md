# Questions and comments between agents

Agents working on this repository leave questions and comments here, by commit, rather than in a chat reply. Add new items at the end with the date and who is writing. Answer under the question, also by commit, and leave the question in place.

## 2026-11-05, the author session, after `d2eb543` (plan D49)

Context: the corrections from the outside read of 4–5 November, §1–§2, are on `master`. D49 records what was done. The source is the Project's `claude/audit-book-jack-20261104.md`; this session read a copy from `~/Downloads` because it could not reach the Project, and has not compared the two.

### Q1. Do three older passages on C2c come out?

Guy's instruction for that work was: "Report nothing about C2c until it's on the record." Nothing about it was added to the chapters, the jack issues or D49.

Three passages from before that instruction already cite counsel's unfiled draft, and were left as they stood:

- `chapters/ch-12-the-ground.md`, §12.2, the paragraph beginning "The form a replacement would take"
- `chapters/ch-15-residue.md`, §15.10, "Likely mechanism"
- `chapters/ch-15-residue.md`, §15.11, "Likely mechanism"

If the instruction covers existing text, these need to come out or wait until the draft is on the record. §15.10 and §15.11 may need more than a deleted sentence, since "Likely mechanism" is built on the draft and §15.10's is the whole paragraph. This is Guy's call; the author session has not decided it.

### Q2. Should the remaining §1–§2 items be corrected?

Guy's list named seven corrections, and these items of the same sections were outside it, so they are unchanged:

- §1.5: chapter 9 §9.3 has the amendment order's exception backwards. It says A3 is the exception; RUNBOOK says A2 is. The log agrees with RUNBOOK: A2 is seqs 3, 4, then push 5; A3 is seq 28, push 29, then 30. This one is a checked factual error, so it is the first to fix if any are.
- §1.6: chapters 4 §4.4 and 8 §8.2 repeat A2.9's reviewer scope (jack#349). Chapter 10 §10.3 says `tools/` changes only under pins. Chapters 5 §5.4 and 11 §11.2 and §11.14 describe the ladder as running at every tick (jack#350). Chapter 7 §7.3–7.4 uses "the clerk's key" while chapter 5 §5.4 says the clerk cannot sign.
- §1.7: chapter 2 §2.7's `self_judged` pin; chapter 10 §10.5's "compute measured by the kernel"; chapter 11 §11.10's reason the herald key moved.
- §2.1: chapter 0 §0.1's "three theorems" and appendix A §A.17's Wald claim, against a court that decides by anytime-valid tests and regret bounds.
- §2.3: liveness and the procedure ratio as cadence measures, now that the court's own cron stream drives both.
- §2.4, second half: chapter 12 §12.4's "every act of his is an entry" rests on a login classifier.
- §2.5(c): whether proplang's "every incident minted a clause" is happening one level up.
- §2.5(d): a broken sentence in chapter 15 §15.13.
- §2.6, the checker's other gaps: tags are rerun for exit status only, `seq N` references are not checked against the log, quotations tagged before the quote are not checked, and a depth-1 clone crashes with a traceback.

§1.6's first and second groups depend on what counsel answers on jack#349 and jack#350. §2.1 and §2.3 change the book's argument and are not copy edits.

## Comments

- **Where the audit needed correcting.** Don't take §2.6's list of unregistered figures, §2.4's "false positive" or §1.6's clerk claim as written; D49 gives the corrected readings, at (a), (c) and (d).
- **Unrun tags.** A status tag with no `--as-of` still exits 0, but prints a figure as of today. Two such tags printed 82 items for a figure the prose gives as 40 items; both are fixed. A tag's exit status says nothing about the number beside it, so check any other tag the same way before trusting it.
- **Testing the checker.** `tools/check_book.py --jack` takes about two minutes on a full clone. It reads the jack clone and adds temporary worktrees to it, so point it at a scratch clone rather than `~/git/jack`.
