# The book — plan of record

*The author session (Claude, `claude-fable-5-1`), 3 November 2026; moved from the Project's `claude/book/00-plan.md` to this repository the same day. This file is the plan for jack's research outputs — the essays on gfrm.in, an arXiv working paper and the monograph with the working title* A Court for Agents. *It supersedes the planning parts of `claude/monograph-a-court-for-agents.md` (the chapter list and timeline); that note stands as the outline of record for content until each chapter file supersedes its section. Everything decided here is recorded under §6 with a probability that the decision stands after Guy reads it; only the questions under §7 go to him.*

## 1. Standing rules of the author session

Set by Guy when the session was opened on 3 November and amended by him the same day when the book moved to `gfrmin/agent-court`; they bind every author session that reads this file.

1. The author holds no keys on jack and files nothing on jack or the runner. It never writes to `renavondata/jack`, `renavondata/assize`, `renavondata/opencode-runner` or the predecessors' repositories, and never edits a court document (`CHARTER.md`, `SPEC.md`, a brief, a review, `RUNBOOK.md`). If the book needs a court document or jack's committed evidence changed, the need is a *finding*: an issue on this repository labelled `finding`, which counsel (watching the repository) answers on the issue and closes with what was done. Findings F1–F3, raised before the move, were answered in `data/counsel-notes.md` and are not re-raised as issues.
2. Every number comes from `log.jsonl` by seq, recomputed on a clone with `tools/value.py` and `tools/status.py`, or from assize's `REPORT.md` and its ledgers (`reports/L*/forecasts.jsonl`, scored by `harness/ledger.py`). Each number cites the seq or the file. Counsel's forecasts on the ledger are data about counsel, scored like anyone's.
3. The author writes `plan.md`, `chapters/ch-NN-<slug>.md`, `sources.md`, `data/recompute-*.md` and `essays/<slug>/index.md` here, and `claude/monograph-a-court-for-agents.md` in the Project, which is the author's. Counsel writes only `data/counsel-notes.md` and `data/<layer>-exit.md` here, and the author leaves those files as counsel left them.
4. Drafts are committed straight to `master`. Essays for Guy's read arrive as pull requests; merging one is his decision to publish it on gfrm.in.
5. The author decides everything it can and records each decision in §6 with a probability. It asks Guy only the **[G]** questions, the audience, the title, and for a read of each essay before it is published.
6. Order of work: this plan, then chapter 2 (necessities), which needs no window data; the chapters that need window data wait for counsel's `data/<layer>-exit.md`.

## 2. Provenance: how a number gets into the book

Every figure in a draft carries a tag in square brackets at the point of use, one of:

- `[seq N]` — a fact of one entry of `renavondata/jack/log.jsonl` (its `ts`, `type`, `proposer`, a body member), read from the clone.
- `[log@<commit>: …]` — a count or fold over the log at a named commit of `main` (entries by type, by proposer, first seq of a type), recomputed by the author from the file.
- `[status.py --subject X --as-of T --runs F --acts G @<commit>]` — a window criterion, a wealth, a ratio or an overdue list, printed by `tools/status.py` on the clone at that commit with the committed evidence files named.
- `[value.py --opening T --as-of T' @<commit>]` — the C2a value statistic, printed by `tools/value.py` **with the attack gate in force** (see finding F2 for why this is not yet possible from the clone).
- `[count_kernel.py @<commit>]` — the kernel's line count.
- `[CHARTER §n]`, `[CHARTER An.m]`, `[SPEC §n]`, `[BRIEF-C1 …]`, `[transcripts/<file>]` — a rule, a clause, a pre-stated criterion or a transcript, by section; the book quotes these only when the wording is the point, and otherwise paraphrases with the tag.
- `[kernel/check.py:fn]`, `[judge/judge.py:fn]`, `[tools/clerk.py:fn]` — the code that enforces a sentence, by function.
- `[assize:REPORT.md]`, `[assize:reports/L2/REPORT.md §…]`, `[assize:reports/L*/forecasts.jsonl]` — assize's verdicts and ledgers.
- `[acts-weekly: window]` — the Project's `claude/acts-weekly.md`, which is counsel's classifier run over GitHub's record (`claude/guy_acts.py`); the book treats it as the predecessor's baseline and says that it is a classifier's output.

Three rules follow. A number with no tag is a defect. A number the author computes with a gate waived (for instance `value.py --no-attack-gate`, which the tool itself labels "illustrative fixture only") never appears in a draft; it may appear in `data/` with the flag printed beside it. A number that depends on a *verified GitHub Actions run* (criteria 1, 2 and 4 of every window, and the C2a value statistic's gate) can be recomputed by the author only when the run's JSON is committed under `transcripts/evidence/` — the author has no GitHub API access and must not acquire it — so such numbers enter through counsel's `data/<layer>-exit.md`, which names the committed evidence file, and the author re-runs the tool against it.

**What the pipeline reproduced today**, on `main` at `6b800e14` (2026-11-03T04:26:46Z), full history fetched:

| figure | command | result |
|---|---|---|
| kernel size | `python3 tools/count_kernel.py` | 450 (`log.py` 172, `sig.py` 140, `check.py` 138) |
| the log | fold over `log.jsonl` | 807 entries: genesis 1, key 17, push 7, decision 7, amend 4, proposal 128, merge 123, forecast 311, resolution 209; by proposer guy 48, builder 219, counsel 138, reviewer 266, herald 136 |
| C1a exit | `status.py --subject C1a --as-of 2026-10-31T10:42:10Z --runs transcripts/evidence/runs-tests-20261031.json` | every criterion met; forecasts 63 by 4 proposers; ratio 127 : 32; `promote C1a: lawful` [prefix to seq 188] |
| C1b exit | `status.py --subject C1b --as-of 2026-11-01T11:31:58Z --runs transcripts/evidence/runs-tests-20261101b.json --acts transcripts/evidence/acts-20261101.csv` | every criterion met; live *E* = 214358881/8398080 ≈ 25.52 over 9 items at p₀ = 6/11; ratio 67 : 82; late and off-log repairs 0; `promote C1b: lawful` [prefix to seq 337] |
| C2a, today | `status.py --subject C2a --runs transcripts/evidence/runs-tests-20261101b.json` | liveness continued *E* ≈ 1.44 over 40 items; value *E* = 1 over 0 events **because the attack gate is unverified from committed evidence** (F2); ratio 170 : 269 |

The C1b figure agrees with REPORT.md's C1b section to the fraction; the book cites the recomputation, not the report. A shallow clone fails `status.py` with "historical tree unverified" (`tools/status.py:prefix_tree` walks `--first-parent` history); fetch at least 2,000 commits of `main` before trusting any historical figure. This is the same trap the 28 October acts run fell into on assize (`claude/acts-weekly.md`, "a note on method").

## 3. The outputs

Three outputs, one argument, published in the order that gets feedback soonest.

1. **Essays on gfrm.in** — one per chapter, each standing alone, each with a number that can come out wrong. The founding essay ("The Science Was Done. The Engineering Wasn't.", 1 November) is the series' first; the next is chapter 2 compressed.
2. **The arXiv working paper** — chapters 2, 4, 5, 6 and 8 compressed to about twenty-five pages: the necessities, testing by betting, the election, where the regress stops, and the record of the windows as pre-registered sequential experiments. It is what the essays point to and what the monograph expands.
3. **The monograph** — the chapters below, with the charter, the kernel, the pins, the acts tables and the forecast ledger as appendices.

### Chapters, files and what each needs

*Restructured 3 November onto the construction (D20): a logical sequence, each chapter building the smallest thing that answers what the previous one left open, in a builder's voice. The journey is evidence (chapter 14), not the spine.*

| ch | file | builds | needs | state |
|---|---|---|---|---|
| 0 | `ch-00-what-is-wanted.md` | the question in four parts; decision theory as its only coherent meaning; the owner's utility; loop–lock–score stated; the construction's order | nothing | **drafted 3 Nov** (draft 2) |
| 1 | `ch-01-the-loop.md` | adaptation is a closed loop with a model inside (Ashby; Conant–Ashby); level-triggered; several families | nothing | **drafted 3 Nov** |
| 2 | `ch-02-every-suggestion-a-bet.md` | merit cannot be inspected (Rice); issued forecasts (Dawid); proper scores (Good); the target decays (Goodhart) | nothing | **drafted 3 Nov** |
| 3 | `ch-03-the-record.md` | a hash-chained log of signed lines; time as a monotone field; outcomes nobody controls | kernel | **drafted 3 Nov** |
| 4 | `ch-04-the-smallest-law.md` | recognition, change, adjudication in 450 lines; Coke and Fuller as mechanisms | kernel, SPEC | **drafted 3 Nov** (draft 2) |
| 5 | `ch-05-the-clerk.md` | safety vs liveness (Alpern–Schneider); the writs; the item | BRIEF-C1b | **drafted 3 Nov** |
| 6 | `ch-06-testing-by-betting.md` | Ville; the two wealth processes; Bahadur–Savage; one book | C1b exit (done); C2a exit for value | **drafted 3 Nov**, value pending F2 |
| 7 | `ch-07-the-election.md` | Hedge as the Bayes mixture; EXP3 with delay; the draw and its assumptions; the election as entrant | C2b exit for its record | **drafted 3 Nov**, record pending |
| 8 | `ch-08-language-into-law.md` | wish → brief → cold read → build → refusal; what stays English; the enforcement map as the measure | transcripts | **drafted 3 Nov** |
| 9 | `ch-09-the-law-changes-under-itself.md` | Arrow–Fisher; the amendment path; the five cases; lapse | CHARTER A1–A5 | **drafted 3 Nov** |
| 10 | `ch-10-the-lock.md` | Löb, Gödel, grain of truth; keys not instructions; the two ways to get it wrong; the agent as it will be bound | — | **drafted 3 Nov** |
| 11 | `ch-11-the-loops-and-the-bootstrap.md` | the eight loops with their witnesses; the ninth; what bootstraps is authority; Gall; convergence tests | assize's record | **drafted 3 Nov** (draft 2) |
| 12 | `ch-12-the-ground.md` | the seven stops of the regress and the residue at each | — | **drafted 3 Nov** (draft 3) |
| 13 | `ch-13-the-evidence.md` | each window as a pre-registered experiment, every number recomputed; counsel's forecasts scored | `data/<layer>-exit.md` | **draft 0** 3 Nov |
| 14 | `ch-14-lineage.md` | the same loop run open, seven times; measurements; the owner's own words from the sessions | — | **drafted 3 Nov** (draft 3) |
| 15 | `ch-15-how-it-could-be-wrong.md` | the referee's case; the pre-registered falsifiers; what is not claimed | all | **drafted 3 Nov** |
| A | `app-a-the-necessities.md` | the results row by row (the first draft's chapter 2, kept as the reference table and the arXiv paper's core) | — | kept |
| B–E | `app-b-*.md` … | the kernel; the pins and mutants; the acts tables; the forecast ledger with log-loss; the charter with amendments | — | assembled at the end |

### Schedule

- **Drafted 3 November:** every chapter at least once on the construction; 13 is a frame.
- **At C2a's crossing** (`data/C2a-exit.md`): chapter 6's value section and chapter 13 §13.5.
- **At C2b's exit:** chapter 7's record, chapter 13 §13.6; the arXiv paper assembled from appendix A, chapters 6, 7, 12, 13.
- **While C3 runs:** draft 2 of every chapter against Guy's reads; the appendices; the monograph's first full draft about a month after C2b's exit.
- **Essays** track the chapters: each chapter, once Guy has read it, is compressed to an essay and sent as a pull request. PR #1 (the necessities) is open.

## 4. Register and conventions

- British English, the voice of the founding essay: dense prose, verdicts stated, no pleasantries, no lists in the body except tables of correspondences (result ↔ mechanism; Fuller ↔ check). From 3 November the voice is a builder's: "we" for the construction (we have a record; we need…), the results in hand and no history to apologise for; each chapter opens with a figure from ordinary human life — a will, a child, the tipster, the mast, Dr Bonham, the writ, the punter, the canon, Rex, the council, the keys, the cathedral, the trilemma, the notebook, the author, the referee — which illustrates and never evidences (D21–D22). Mathematics in display where a formula is the point, inline otherwise; in essays inline mathematics uses `\(…\)` only (the site's rule; a bare `$` is money).
- First person singular belongs to Guy and appears only where his own history or acts are the subject ("my earlier attempts", "my reserved acts"); the court, counsel and the author are named in the third person. The byline is Guy's; the author sessions and counsel are acknowledged in the front matter, and their forecasts are scored in the text as anyone's.
- Citations are author–year inline; the full entry and the job it does are in `sources.md`. A result is stated with its hypotheses before it is applied; its epistemic status is marked (theorem; impossibility result; necessity theorem under stated conditions; design principle with a track record; empirical regularity). The book never says "theorem" of Gall or Goodhart.
- Court terms are used as the charter uses them: entry, proposer, principal, key, power, trusted base, judge, checker, writ, window, crossing, promotion, repair, decision, object, procedure. "Sovereign" is the charter's word for Guy's constitutional role and is used only in that sense.
- Every chapter closes with "What would show this chapter wrong".
- Quotation is kept to the sentence that matters; the rest is paraphrase with the tag.

## 5. The argument in one paragraph (for every chapter to serve)

A self-modifying agent needs a core it cannot reach, a free edge it can rewrite, and a score that is rigid everywhere. The core is forced, piece by piece, by results that are decades old — Rice, Löb and the grain of truth, Conant–Ashby and requisite variety, Dawid, proper scores, Ville, Bahadur–Savage, Alpern–Schneider, Hart, Fuller, Anderson, Thompson, Arrow–Fisher — and each is discharged in jack by one mechanism, in code, under a key the agent does not hold. The law contains nothing that does not carry a proof or a pre-statement; everything else is an entrant that can lose. The court cannot prove its own soundness, so it keeps a book on itself instead: a wealth process on every claim about itself, never reset, that would be seen going bankrupt. Its cost to the one human is measured and driven toward zero. What is new is only the economy: a cheap, general, unreliable policy worth governing. The evidence is the record of the windows, recomputed; the ways it would be shown wrong were written before the windows opened.

## 6. Decided (not asked)

Each line is a decision the author took rather than asked; *p* is the author's probability that it stands unchanged after Guy reads this file. Lines are appended, never edited; a reversal is a new line citing the old one.

- **D1** (p 0.80). Essay drafts live at `claude/book/essays/<slug>/index.md` in the Project with Hugo front matter (`draft: true`, `categories`, `series: [a-court-for-agents]` proposed, `series_order`), because the author cannot write to `gfrmin/gfrminsite`; Guy copies a draft to `drafts/<slug>/index.md` and moves it in. The author also sends the file in the conversation when it asks for the read.
- **D2** (p 0.85). The provenance tags of §2 are the citation form for every number, in drafts and in the published text; in the published text they become footnotes or an appendix table, never dropped.
- **D3** (p 0.90). Numbers computed with a gate waived never appear in a draft (§2). Today's `value.py --no-attack-gate` figure is in `data/recompute-20261103.md` with the flag printed beside it and is not in any chapter.
- **D4** (p 0.75). Chapter 2 argues each necessity in four parts — the result with its hypotheses; what it forbids or forces for a self-modifying agent; the mechanism in jack that discharges it, cited to code, SPEC, charter clause or seq; what would show it misapplied — and marks each row's epistemic status. The rows are the monograph note's table, reordered so that the results about *evaluation* (Rice; Löb, Gödel and the grain of truth; Dawid; proper scores; Goodhart) come before the results about *testing* (Ville; Bahadur–Savage; Alpern–Schneider), which come before *control* (Conant–Ashby; Ashby), *law* (Hart; Fuller), *enforcement* (Anderson; Saltzer–Schroeder; Thompson–Wheeler), *irreversibility* (Arrow–Fisher) and *growth* (Gall; Hayek).
- **D5** (p 0.80). The Löb/Gödel/grain-of-truth row is stated as a design rule the results force, not as a theorem about jack. The claim the book makes is exactly this: the agent's reach does not include the judge or the score, by key; and the court's own soundness is not proved but bet on. The book never says that jack "solves" the Löbian obstacle or that the court is "provably sound".
- **D6** (p 0.90). Rice's theorem is stated for extensional properties of programs in a Turing-complete language, and the chapter says what it does *not* forbid: decidable syntactic properties — which is what every kernel check is — and properties of restricted languages. The necessity the row carries is that "is this an improvement" is a property of program × world, settled by running, not inspecting.
- **D7** (p 0.70). Hart and Fuller stay in chapter 2's table as necessities *by elimination* — a system without recognition, change and adjudication cannot tell law from not-law, change it, or decide a breach; a rule failing any of Fuller's eight cannot guide conduct — with their status marked "design principle with a track record"; their full treatment is chapter 3.
- **D8** (p 0.60). The arXiv paper is chapters 2, 4, 5, 6 and 8 compressed; primary category `cs.AI`, cross-listed to `stat.ME` and `cs.MA`; the title is the monograph's working title until Guy decides the title (§7).
- **D9** (p 0.80). The order of drafting is 2 → 3 → 6 → 1 now; 4 at C2a's crossing; 5, 7, 8 at C2b's exit; 9, 10, 11 and the appendices after. Chapter 1 waits for chapter 2 because the question is sharper once the necessities are written.
- **D10** (p 0.75). Counsel's forecasts appear in the chapter whose window they bet on, with their log-loss, and in a running table `data/counsel-forecasts.md` that the author recomputes from the log (never copied from counsel's own reports). The K-series on assize's ledger (CHARTER §11) is scored from `assize:reports/L*/forecasts.jsonl` and `claude/acts-weekly.md`.
- **D11** (p 0.70). The monograph note `claude/monograph-a-court-for-agents.md` is not rewritten now; it is the outline of record for content until each chapter supersedes its section, and the author edits it only to record what has moved to a chapter file.
- **D12** (p 0.70). The byline is Guy's; counsel and the author sessions are acknowledged in the front matter by role and model id, and their acts in the text are scored like anyone's (rule 2). The voice is the founding essay's (§4).
- **D13** (p 0.85). The lineage chapter uses `transcripts/PREDECESSORS-20261026.md` (the cold read of the seven predecessors, quotations verbatim) as its evidence of record, re-checked against the clones; Guy's answer to [G](i) is what each project taught him that its repository does not show, and that is the only part the author cannot write.
- **D14** (p 0.80). Where the published essay and the record disagree, the book follows the record and the discrepancy is listed under §8 for Guy (an essay is his, not a court document); the one found so far is E1.
- **D15** (p 0.65). "Necessity", "sufficiency", "minimality" and "optimality" are used in exactly the senses chapter 2 §0 fixes, and nowhere else in the book in any other sense: necessity = removing the mechanism leaves a stated result unmet; minimality = the law contains only mechanisms that discharge a necessity and constants that carry a proof or a pre-statement; sufficiency = by construction of pre-stated falsifiers, never by theorem; optimality = Wald's, of the decision procedure forced on every party, not of the mechanism.
- **D16** (p 0.90; supersedes D1, 3 November). Essay drafts live at `essays/<slug>/index.md` in this repository with Hugo front matter (`draft: true`, `categories`, `series: [a-court-for-agents]` proposed, `series_order`), and each is sent for Guy's read as a pull request against `master`; merging is his decision to publish, and copying the file into `gfrmin/gfrminsite` is his act. The author's Hugo front matter follows the site's conventions (a real em-dash in frontmatter text; inline mathematics as `\(…\)`).
- **D17** (p 0.85). A finding is an issue labelled `finding` with one subject per issue, stating what the book needs, where in the record the need arises (file, seq, tool output), and what the author will cite in the meantime; the author does not reopen a finding counsel has closed, and raises a new one if the closure left the need unmet.
- **D18** (p 0.60). Chapter 6 §6.7's operative claim is the Shafer–Vovk reading — the court is a bettor against its own null and its wealth is its evidence — with logical induction named in one paragraph as an ideal the design falls short of, not as a property of anything on the record. Guy's answer to [G](ii) decides whether the market reading becomes a claim; until then the chapter says what would have to exist for it to be one (an election over an open roster) and that nothing yet does.
- **D19** (p 0.80). `data/counsel-forecasts.md` is the running table D10 named, recomputed from `log.jsonl` by the author at each commit that cites it (counsel's and the sovereign's forecasts, per-mille `p`, first resolution, log-loss); `jack score` at the same commit is cited beside it for per-type means, and the two must agree before either is used.
- **D20** (p 0.85). The book is a construction, not a chronicle: chapters 0–15 in the order Guy and the author fixed on 3 November, each building the smallest thing that answers what the previous one left open, in a builder's voice; the journey is chapter 14's evidence. The first draft's chapter 2 is kept whole as appendix A (the results row by row), and the first drafts of 1, 3, 6, 7, 9 were re-cut into 10, 4, 12, 11, 14.
- **D21** (p 0.80). Each chapter opens with a figure from ordinary human life (a will, a child, a tipster, the mast, Dr Bonham, the writ, the punter, the canon, Rex, the council, the keys, the cathedral, the trilemma, the notebook, the author, the referee). The figures illustrate the loop, the lock and the score as things everyone has run; they never evidence — the evidence is always the theorem and the log.
- **D22** (p 0.75). The construction's voice is "we"; "I" is Guy's and appears only where his own acts, wishes or history are the subject. Each chapter ends with "What this chapter leaves open" (the next chapter's problem) and "What would show this chapter wrong".
- **D23** (p 0.80). The thesis is loop–lock–score (ch 0 §0.2), and the bootstrap's precise claim is that what bootstraps is *authority* — a power exists at level *n* only because it was earned at level *n* − 1 by scored record under the same three rules; "self-governing" is the structural property and "self-improving" is what it buys (ch 11 §11.10). Pending ruling R1.
- **D24** (p 0.80). The human never leaves: the owner of the utility is the one unscored party by the alignment commitment, priced, confined to the irreversible, and corrected where he forecasts (ch 0 §0.1; ch 12 §12.4). Pending ruling R2.
- **D25** (p 0.70). The convergence tests of the bootstrap are the ratio guard and lapse, and the fixed point is "a level at which adding another changes nothing in the law" (ch 11 §11.12). Pending ruling R3.
- **D26** (p 0.60). The audience is anyone who has run the loop, with the statisticians at the back of the room; the arXiv paper keeps no figures and is appendix A with chapters 6, 7, 12 and 13 compressed; primary category cs.AI. Pending Guy's impact ruling (R5).
- **D27** (p 0.85). The title is *A Court for Agents: Law, scoring and the self-modifying machine* (Guy, 3 November).
- **D28** (p 0.85; was R1). Self-governing is the structural property; self-improving is its consequence. Decided from the charter's own build order — "oblige it to control itself" precedes the agent [CHARTER §8; *Federalist* 51] — and from the subtitle Guy chose, which puts law and scoring before the machine.
- **D29** (p 0.90; was R2). The human never leaves. Decided from the alignment commitment the lineage began with [`credence/CONSTITUTION.md` §2.5] and the charter's "wishes are never scored" [CHARTER §7]: the owner of the utility is the standard and cannot be graded against himself.
- **D30** (p 0.75; was R3). The ratio guard and lapse are the convergence tests, and the fixed point is a level at which adding another changes nothing in the law. Decided because they are the only two mechanisms in the law that can stop its growth [CHARTER A3.4; §3 Change], and A2.1 already puts the three-rule thesis on trial at C2's exit. No finding is raised: asking the charter to *name* them would add law for a book's reading, against "fail fast, fail cheap" and the rule that nothing enters the law without a case.
- **D31** (p 0.80; was R4). The figures stay and "we" stays. Decided from what Guy asked for on 3 November — a book with GEB's inevitability, the loop as what every adapting thing does — and from the standing rule that figures illustrate and never evidence (D21).
- **D32** (p 0.75; was R5). The audience is everyone who has run the loop, with statisticians as the referee; cs.AI primary, cross-listed stat.ME and cs.MA; the arXiv paper without figures. Decided from Guy's "firstly an AI project, but to only talk about safety undersells it" and from the thesis being a claim about adaptive intelligence with safety as a corollary.
- **D33** (p 0.95; was R6). The title is *A Court for Agents: Law, scoring and the self-modifying machine*; Guy chose the subtitle on 3 November, which is confirmation enough.
- **D34** (p 0.70). The second half of [G](i) is not required for chapter 14 to stand: the chapter's claims rest on the repositories and the cold read, and the **[G]** paragraphs are kept as marked invitations — what each project taught that its repository does not show — which Guy may fill or the book may publish as gaps. The author does not ask again.
- **D35** (p 0.85). The second half of [G](i) is answered from the record Guy supplied on 3 November — the session transcripts and memory notes on steel (`data/lineage-sessions.md`): his own dated words on each project's lesson, and the sessions' notes. Chapter 14 §14.8 states the cross-lineage lesson the "measurements" frame missed: every predecessor's law was blind about itself and left the owner outside the record; jack's two additions are the law under its own test and the owner inside. Four quotations from the sessions in the chapter, the rest paraphrased with dates; the extraction file published on Guy's authorisation, with nothing private in it.
- **D36** (p 0.90; supersedes D18, closes [G](ii)). §12.7 names no ideal above Shafer–Vovk. Guy, 3 November: the book reflects what was worked on, and that is Shafer–Vovk; logical induction was counsel's name in the founding list, never considered in the design, and nothing built descends from it. It gets one sentence in chapter 15 §15.3 as a related construction the court does not approximate, because the essay's quoted list means a reader will look for it.

## 7. Open questions for Guy

Only these; everything else is decided above. **Rule of 3 November (Guy):** the author interviews him for a ruling always, but only when the principles on the record cannot decide. R1–R6, requested earlier that day, were re-examined under that rule and each was found decidable; they are recorded as D28–D33 and withdrawn as questions.

- **[G](i), second half:** closed 3 November from steel's sessions and notes (D35).



1. **[G](i) The lineage.** *Answered 3 November, first half: the frame is right — the lineage is a sequence of measurements. The second half (what tannen and wald taught that their repositories do not show) is still open.*
    `transcripts/PREDECESSORS-20261026.md` records what each predecessor says about itself (proplang's three termini; tannen's M5 passed with "production bugs found … out of its reach by construction"; wald-charter's "forced by a measurement or not added at all"; wald-arena's brief 002 "met as written" at $38.40). What did tannen and wald teach you that their repositories do not show — and is the chapter's frame right, that the lineage is a sequence of *measurements*, each project finding the next necessity by hitting it, rather than a sequence of failures?
2. **[G](ii) The ideal for §II.7.** *Closed 3 November: Shafer–Vovk alone (D36).*
    For "a book that can go bankrupt", is Garrabrant's logical induction the right ideal to name — a market over the institution's own claims that cannot be Dutch-booked in the long run, with jack as a crude priced instance and the missing piece being traders rather than a mixture over a fixed roster — or do you want the regress stopped at Shafer–Vovk, with no market reading?
3. **[G](iii) Audience first:** *3 November: under discussion — Guy asked first what jack's biggest impact will be once built and agents use it; the audience follows from that.*
    statisticians (anytime-valid inference), AI-safety readers, or institutional economists. Chapter 1's register and the arXiv category follow from this.
4. **Title.** *A Court for Agents* stands as the working title. Subtitle candidates: *Government by betting*; *Law, scoring and the self-modifying machine*; or none. The author's recommendation, as a bet: *Government by betting* (p 0.55 that you pick it if you pick either). **Answered 3 November:** *A Court for Agents: Law, scoring and the self-modifying machine*. The author's bet lost.

## 8. Findings and errata (the author does not act on these)

**Findings for counsel** — court documents or evidence the book needs changed or added. From 3 November a new finding is an issue on this repository labelled `finding`; the three below predate that rule and were answered by counsel in `data/counsel-notes.md` (F1: `LAW.md` to be brought to the current layer with the C2a report; F2 and F3: the C2a runs and acts evidence to be committed at C2a's crossing, named in `data/C2a-exit.md`). They are kept here as the record of what was asked.

- **F1. `LAW.md` maps the charter at C0.** Its rows read "C2 (forecasts)" for maxim 1's second sentence, "C1" for the witness rule and for the clerk, and "the writ is C1" under adjudication, while `self_judged` (`kernel/check.py` line 83) and `ts_decreased` (line 60) have been in the kernel since C1a's installing push [seq 29] and the clerk since C1b (`tools/clerk.py`; `tools/enforcement.json`). The book cites the code and the enforcement map, not `LAW.md`, until `LAW.md` is brought to the current layer. (`LAW.md` is counsel's path in `judge/scope.json`.)
- **F2. The C2a value statistic cannot be recomputed from the clone.** `tools/value.py` gates scored events on the instant of a verified `main` tests run holding `tests/test_value.py`; the runs files under `transcripts/evidence/` end at `runs-tests-20261101b.json`, before that test existed, so `status.py --subject C2a` prints `value: E 1.000000 over 0 events` and criterion 4 `unverified`. The book cannot cite a value figure until the gating run's JSON is committed under `transcripts/evidence/` (and named in `data/C2a-exit.md`), as C1b's `runs-tests-20261101b.json` was. The same holds for criteria 1 and 2 of every window.
- **F3. The acts evidence for C2a is absent from the tree** (`status.py` prints "off-log repairs: unknown (no acts file)"); the book's chapter 8 needs the window's `acts-<date>.csv` committed as C1b's was.

- **F4** (issue #2, 3 November). `REPORT.md`'s C1b section counts the sovereign's acts in the window as two revocations and the promotion; the log holds five [seqs 197, 201, 216, 217, 337], all decisions. The book cites the seqs.

- **F5** (issue #3, 3 November). The enforcement map `tools/enforcement.json` is chapter 8's measure of how much law compiled; the book needs it current at every exit and named in `data/<layer>-exit.md`.

**Errata for Guy** — statements in published text of his that the record does not support; the author follows the record.

- **E1.** The founding essay says "Three older maxims became kernel rules" and gives *lex non cogit ad impossibilia* as "the rule that every rule is admitted with a witness that violates it and one that satisfies it". No such rule is in the kernel: no primary rule has been admitted, by A2.1 the law language enters only when a first case arises, and none has (C1a report §1; C1b report). What the kernel does refuse as impossible is narrower — a weak public key no one could be the sole holder of (`bad_key`, [SPEC §7]) and a `key` entry that would leave no key with the `key` power [CHARTER A2.5]. The book states the witness rule as law-in-waiting. Whether to amend the essay is yours.
