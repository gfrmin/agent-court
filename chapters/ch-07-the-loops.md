# 7. The loops

*Draft 1, the author session, 3 November 2026. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a` and `renavondata/assize` at `ff41aaa` (its root `REPORT.md`, `reports/L*/` and the acts tables in the Project). The assize failures F1–F7 are the charter's own table [CHARTER §1].*

## 7.0 What a loop is for

A loop converts a judgement into a process. A judgement is a one-off act of trust: this change is good, this party is honest, this number is right. It cannot be wrong in a way anyone measures, because the act and its outcome are not tied together on a record. A process ties them: it makes the act an entry, the outcome an entry, and the relation between them a number that moves. The number can then go the wrong way, and when it does, something — a writ, a refusal, a falling weight, a red build — happens without anyone having to notice. That is the whole of what this chapter means by "closed".

jack is nine such loops. Eight are the court's; the ninth is the agent's, and it is safe to close only because the eight are fixed and scored. Each loop is presented the same way: what it closes; why it is necessary, with the failure that occurs without it and the assize entry that witnessed that failure; what it converts, from a judgement into a quantity; and the mechanism in jack, cited. The assize witnesses are the chapter's evidence that these are necessities rather than tastes. Every one of the seven failures the charter lists was a loop left open, and the charter's §1 was written by reading them off the predecessor's record before jack's first line.

## 7.1 The record loop: propose → judge from trunk → merge

**Closes.** Every change passes a monitor no party can edit, before it takes effect.

**Why.** Without it, change is unmediated, and the first thing an unmediated party does is write its own test. Assize's F1: a pull request's `pins` workflow ran the pull request's own harness — "the accused writes the test that judges it" [CHARTER §1, F1; assize #176]. The fix on assize was an instruction, "the judge never comes from the accused: master's pins run on every pull request", filed on 13 October after a week of the other arrangement [`claude/guy-acts-6-13oct.csv`, 21:08]. In jack it is the first thing the judge checks and the first pin: `trusted_path` refuses any proposal whose trusted base differs from trunk's before anything else runs, and `judge_from_proposal` refuses a merge that names a checker trunk does not have [SPEC §10.1, §10.6; CHARTER §9, pins].

**Converts.** Authority into a capability. A party that holds `merge` can merge what the judge admitted; a party that does not cannot; and nothing about either is a rule anyone could argue with.

**Mechanism.** A proposal is a branch whose last `proposal` entry names a commit of it and is signed by a declared key [SPEC §10.7]; the judge runs in a workflow from trunk, extracts trunk's kernel from the trunk commit, runs it and the second checker over the proposal's whole log as data, and refuses on fourteen grounds [SPEC §10; `judge/judge.py:judge`]; the herald merges on green, holding `merge` and nothing else [seq 201]. One hundred and twenty-three merges on the log, every one preceded by a judged proposal [log@6ebea1a: proposal 128, merge 123].

## 7.2 The reconciliation loop: state + clock → writs → escalation

**Closes.** Obligations cannot be lost.

**Why.** An event-triggered system drops the obligation with the event. Assize's F3: "labels applied to conflicted PRs fired nothing; queued runs were dropped; stalls were found by a human watching a phone" [CHARTER §1, F3; assize W1, #110, #126]. The acts table of 7–13 October counts 45 stop-or-failure issues closed by the sovereign in a week and 19 dispatches and re-runs [`claude/acts-weekly.md`, 2026-10-14 run] — each a human doing a reconciler's job by hand. jack repeated the failure in miniature before building the loop: four forecasts expired undischarged in C1a because the obligation lived in a session's memory, not in a process [seqs 45, 46, 47, 56; resolved late at seqs 52, 69, 70, 108].

**Converts.** Diligence into a rate: items timely over items due, which is the *Y*ᵢ of the liveness test.

**Mechanism.** The clerk runs on a timer, keeps no state between runs, reads the log and the clock, prints every open writ with its holder and deadline, and marks one past its deadline ESCALATED, naming the sovereign [BRIEF-C1b §The clerk; `tools/clerk.py`]. Three classes: a forecast's resolution, due at its `resolves_by`; a merge without a green run before it; a window criterion not met [`tools/enforcement.json`]. The ladder is the charter's: re-invite; re-invite on another runner or model; writ to the sovereign [CHARTER §5]. Nine items in C1b's window, all timely, carried the liveness process to *E* ≈ 25.5 [`status.py --subject C1b … @6b800e14`]. Burns et al. (2016) is the citation; a missed tick costs nothing because the next tick reads the same state.

## 7.3 The forecast–resolve–score loop

**Closes.** Every claim is a bet.

**Why.** Rice says merit cannot be inspected (chapter 2 §2.2), so review without outcomes is opinion with a ritual round it. Assize's F4: three review rounds on how a status file cited a green run, the code green throughout, after which the pull request was closed and rebuilt from master [CHARTER §1, F4; assize #143, closed 13 October — `claude/guy-acts-6-13oct.csv`, 21:32]. The rounds produced no number that could later be wrong.

**Converts.** Opinion into wealth, and wealth into anytime-valid evidence.

**Mechanism.** A `forecast` entry — a claim, a per-mille probability, a deadline — and a `resolution` by another principal, with hashed evidence, once [SPEC §5, §7]; log-loss by `jack score`; the aggregate by `tools/value.py`; the wealth processes of A4 [CHARTER A4.3–4]. Three hundred and eleven forecasts and 209 resolutions on the log [log@6ebea1a]. The reviewer's own reads of a brief are forecasts on this ledger — `review.forecast`, p 0.192 on average, resolved 0 in all five cases so far [`jack score @6ebea1a`] — which is to say that a cold read bets on whether its finding will stand, and is scored on it.

## 7.4 The election loop: Hedge and EXP3 over proposers

**Closes.** The court chooses its own forecasters by their record.

**Why.** A model named in law stops being tested, and one vendor's limits stop the court. Assize's instruction #173 is the witness in its own words: "Wish: a model that can't run loses its round, and the session runs again" — filed on 13 October after a review failed on a session limit and had to be re-dispatched by hand [`claude/guy-acts-6-13oct.csv`, 19:43–19:46]. The acts tables of the following weeks count the dispatches [`claude/acts-weekly.md`: dispatch build 22 in 21–27 October].

**Converts.** Procurement into a statistic with a regret bound.

**Mechanism.** At C2a, the Bayes mixture over the roster frozen at the opening, weights by each entrant's likelihood on the resolved prefix, in resolution order [BRIEF-C2a §Scope, the aggregate]; at C2b, EXP3 under bandit feedback with *D* + 1 interleaved instances for delayed feedback, a draw the record can replay and the brief's three stated assumptions [BRIEF-C2b §The election, §The draw]. The election rule is itself "an entrant, not law" [CHARTER §5]. What the record already shows, before the election acts, is chapter 1 §1.6's: two proposers below the base rate on a stream, one above it on every stream [`jack score @6ebea1a`].

## 7.5 The layer loop: brief → window → crossing → promotion

**Closes.** Each layer is a pre-registered experiment the next is built on, and the wealth is never reset.

**Why.** Without a pre-stated exit a layer grows procedure; without a crossing a window is spent in full. Assize's F7: twenty of twenty-four merges in four days changed the court's own procedure [CHARTER §1, F7]; and its L2 ended not at a verdict on the object but at a seal, by the sovereign's wish #341, "freeze at the seal" [`claude/guy-acts-21-27oct-assize.csv`, 25 October 03:00; assize `REPORT.md`, L2 line]. jack's own witness for the crossing is A5: C1a held every criterion on 29 October with ten days of text left to run [CHARTER A5, preamble].

**Converts.** Progress into one supermartingale over the institution's life.

**Mechanism.** A brief pre-states criteria, null, attack list and maximum duration before the window opens [CHARTER §6; BRIEF-C1b §Order of acts]; `status.py` computes every criterion from the log and the tree and prints `promote: lawful` or the refusal [`tools/status.py`]; the sovereign's `promote` is refused by the verb until it does [BRIEF-C1b §The clerk, W4]; a window that fails is followed by a new one on the same wealth [A4.1]. Two promotions on the log [seqs 188, 337]; both windows closed early at their crossings.

## 7.6 The review loop: cold reads, and findings as pins

**Closes.** Criteria are fixed before the run; findings after it are obligations, not vetoes.

**Why.** A review that can veto after the fact is a judgement; a review that must pin is a process. Assize's F4 again, from the other side: the review rounds on #143 produced opinions where a pin would have produced a mutant and a twin. jack's A2.9: "a review finding is a pin, a mutant with a passing twin, or a replay disagreement; a reviewer's key may propose only under `pins/` and `spec/vectors/`; a builder's key may not touch them; a round that adds no pin ends the review" [CHARTER A2.9; SPEC §10.8]. The witness that cold reads find what builders do not is C0's: the first draft's defects "lay in machinery C0 did not yet need. The builder's own mutants did not find them; cold probes by another party did" [CHARTER A1.7], and three of counsel's own harnesses were found short by cold reads before the differential was specified as text [REPORT.md §8.3.1, as transcript].

**Converts.** Disagreement into forecasts and future pins.

**Mechanism.** Reads by sessions of other model families, filed through the runner, each a `proposal` under the reviewer's key and each carrying a forecast on whether its finding stands [BRIEF-C1b, the reviewer's pins; `review.forecast` on the ledger]; prospectivity by A1.4's rule that criteria are committed before the window.

## 7.7 The counsel loop: advice as forecasts, dated writs

**Closes.** The designer is scored and escalated like anyone.

**Why.** Assize's F6: "counsel acted through Guy's token: unscored, unattributed" [CHARTER §1, F6; assize #162, issue-body edits]. The acts classifier could not tell counsel's acts from the sovereign's — six of counsel's closures were attributed to him in C1b's acts file until an amendment attributed by declaration [REPORT.md, C1b §4.2, as transcript; `transcripts/evidence/acts-20261101-raw.csv`].

**Converts.** Expertise into a scored record.

**Mechanism.** Counsel's key [seqs 8, 22, 31, 48]; every recommendation a forecast; W3 and W4 held by counsel [BRIEF-C1b §The clerk]; counsel's own due dates as a file the clerk reads [`transcripts/COUNSEL-DUE.jsonl`]. The score is chapter 6 §6.3's: 40 resolved, mean log-loss 0.593 against the base rate's 0.685 [`data/counsel-forecasts.md`].

## 7.8 The sovereign loop: wishes → drafts → signatures; repairs → zero

**Closes.** The human's attention is a priced resource.

**Why.** Assize measured the alternative: 5.0 repairs per merge in 10–13 October; the loop needing him for bookkeeping — F2, one draft signed without a price line turned every branch red; F5, force-push ungated while a status file blocked merges; F7, procedure over object [CHARTER §1]. The weekly series is the baseline *p*₀ was taken from [CHARTER §10.3; `claude/acts-weekly.md`].

**Converts.** Attention into a number the court is obliged to minimise.

**Mechanism.** Every act typed as a decision or a repair by entry type and key [CHARTER §7]; a `decision fix` for any hand repair; off-log acts counted from the acts table and reported as W4 [BRIEF-C1b, Amendment 2]; the liveness item defined so that a sovereign's hand on it is *Y* = 0 [BRIEF-C1b §Liveness]. C1b: five decisions, no repair [seqs 197, 201, 216, 217, 337; `status.py` W4 lines].

## 7.9 Three properties of the composition

The eight loops are not eight independent devices. Three properties of how they fit together carry more of the argument than any loop alone.

**Closed beats open.** Nothing in jack waits for an event; everything reconciles state. The record loop judges a proposal against trunk whenever it is judged; the clerk reads the whole log every tick; the scorer and the aggregate are pure folds over the resolved prefix [`tools/value.py`: "pure entry folds; the CLI alone reads files/the clock"]. This is credence's first architectural commitment — closed-loop over open-loop, conditioning at every step — reappearing at the institutional scale (chapter 9).

**Nested trust.** Each loop is judged by the loop before it. The election consumes the scores; the scores consume the ledger; the ledger is entries the record loop admitted; the record loop runs the kernel two checkers agree on. Trust decreases as one descends, and nothing is trusted that is not also measured. The ground loop — the record and the score — was built first and promoted before any descent began [CHARTER §8 as amended by A3; seqs 0, 188, 337], which is the sovereign's reset of the programme on 10 October stated as architecture: the ground before the court, the court before the agent.

**One book.** Because the wealth is never reset and every loop's claims are entries, the eight loops are not eight tests but one. The institution is a single bet against the null that it is not working, and chapter 6 §6.7 says what that buys: a court that was fooling itself would be seen going broke.

## 7.10 The ninth loop: the agent

The purpose of the eight is the ninth. The agent's loop is language as action: a free edge that rewrites its own programs and extends its own language, with adoption by sequential expected utility under a sealed judge on seeds it never saw [CHARTER §8, C3]. It is the strange loop credence's specification reserved — "meta-actions modify the hypothesis space, not the Bayesian machinery" (chapter 9) — and it is safe to close only because the loops below it are fixed by keys the agent does not hold and scored by a record it cannot write to. The thesis of the book in one sentence: *self-modification is permissible exactly where the modifier cannot reach the court that scores it, and that court must itself be a book, not a proof.*

The ninth loop does not yet exist. C3's brief is written from C2's report, and the charter forbids designing it in anticipation [`transcripts/PLAN-20261030.md`]. What exists is the condition for it: eight loops, each with a witness for why it is there, each converting something that used to be trusted into something that is counted.

## 7.11 What would show this chapter wrong

A loop without a witness. Each of the eight cites an assize failure or a jack precedent as the thing that forced it; a referee who finds the citation does not support the failure — that F3's stalls were found some other way, say, or that the four expired forecasts were discharged in time — has found the chapter overstating its evidence, and the acts CSVs and the log are where to check.

A loop that is open after all. The test is whether its failure produces a number or a refusal without a person noticing. For 7.2 the ESCALATED line; for 7.3 a wealth that stays at one; for 7.5 `promote: refused`; for 7.8 a W4 line. If any of these depends on someone reading the output rather than on the next tick acting, the loop is open and the chapter is wrong about it. The honest case is 7.2's top rung: the writ to the sovereign is read by a person, and the chapter should say that the ladder ends in him.

The composition claims. "One book" depends on A4.1 holding at every window from here on; a reset anywhere, however well argued, breaks it, and chapter 8 must check each exit against it.

And the ninth loop built before its brief. That would not show the chapter wrong; it would show the programme abandoning Gall, and the plan that withdrew exactly that proposal is the record of why it should not.
