# 5. The clerk

*Draft 1, the author session, 3 November 2026. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## The figure: the writ

Habeas corpus is a demand addressed to whoever holds a prisoner: produce the body, and say by what authority you hold it. What made it an institution rather than a sentiment was the Act of 1679, which put a deadline on the answer and a penalty on the custodian who let it pass; the writ ran from the state of affairs — someone is held — and not from anyone's complaint. Empires fail on the other side of this. The frontier stalls, the garrison waits for orders, and the order is lost on the road because the system that was to carry it reacted to messengers rather than to the state of the frontier. A courier watching the road is how the predecessor court found its stalls [CHARTER §1, F3]. This chapter builds the clerk: the thing that reads the state of the record and the clock, derives every obligation the state implies, gives each a deadline, and escalates when the deadline passes — without being told.

## 5.1 What we have, and what it cannot do

We have a law of three rules over a record (chapter 4). The record now holds promises — every forecast carries a `resolves_by` [SPEC §5] — and the law holds no one to them. A forecast can expire unresolved; a merge can land with no green run before it; a window's criteria can be met for days with nothing to say so. The rules of chapter 4 are all *safety* rules: each refuses a bad entry when it arrives. None of them can say that a good entry has failed to arrive. That is a different kind of property, and the theory says it needs a different kind of mechanism.

## 5.2 Safety and liveness are different kinds of thing — Alpern and Schneider (1985)

**Result** (theorem). Take a property to be a set of infinite executions. A *safety* property is one whose violation is visible at a finite point: every execution outside it has a finite prefix none of whose extensions is inside. A *liveness* property can never be refuted by a finite prefix: every finite prefix has some extension inside it. Every property is the intersection of a safety and a liveness property. Lamport (1977) drew the distinction — nothing bad ever happens; something good eventually happens — and this is its exact form.

**What it forces.** "Nothing invalid was ever admitted" is safety: one entry refutes it, and a replay of the prefix checks it exactly (chapter 4; appendix A §A.14). "Obligations do not rot" is liveness: no finite record refutes it, so the only honest claim about it has a *deadline* in it — "by then, or escalated" — and the only honest test of it is statistical. A liveness obligation stated without a deadline is untestable in principle. So every obligation the clerk derives must carry one, and the clerk's output must be something a test can count (chapter 6).

**Mechanism.** The charter states the division in these words: "recognition and adjudication carry safety, writs carry liveness" [CHARTER §4]. The deadline is the charter's third maxim: "Every obligation is derived from present state and the clock, carries a deadline, and escalates when the deadline passes. No component waits for an event; each reconciles state" [CHARTER §2.3].

## 5.3 Level-triggered, not event-triggered — Burns et al. (2016)

**Result** (engineering principle, with the witness that makes it a necessity here). A controller that reconciles desired and actual state loses nothing when an event is missed: the next tick reads the same state. One that reacts to events loses the obligation with the event.

**What it forces.** The clerk keeps no state of its own and subscribes to nothing. It reads the record and the clock, computes what is owed, and prints it; a tick missed costs nothing because the next tick computes the same answer.

**The witness.** Before the clerk existed, the court tried to hold its obligations in a session's memory. Four forecasts — three by the sovereign, one by counsel — expired undischarged in the ledger's first window and were resolved one, eight and nearly four hours late [seqs 45, 46, 47, 56; their resolutions at seqs 52, 69, 70, 108]. The clerk's brief names those four as its forcing witness, and the lesson is the maxim's second sentence made concrete: a reminder is an event, and a missed event is a lost obligation.

## 5.4 The clerk

`tools/clerk.py` is 88 lines and is the builder's [BRIEF-C1b §The clerk]. Run on a timer or by hand, it prints every open writ — the obligation, who may discharge it, the deadline — and marks one past its deadline **ESCALATED**, naming the sovereign. Three writ classes exist, because three kinds of obligation have witnesses on the record and "a class with no witness is not built":

- **W1, a forecast.** Every `forecast` entered after a window's opening is a writ from its entry; its holders are every key with `resolution` power whose principal is not the forecaster's; its deadline is `resolves_by` itself — "the obligation the entry already carries"; it is discharged by a `resolution`. A writ is overdue when the clock is strictly after the deadline. The brief refused a grace period on the ground that every late case on the record would have been timely under one, "which would leave the deadline no witness".
- **W3, an unwitnessed merge.** A `merge` entry on `main` whose commit had no green `tests` run before the merge commit's time; held by counsel; discharged by a line naming it as precedent. Its witness is a merge that landed before its run finished [REPORT.md, C1a §4.4, as transcript].
- **W4, window state.** Every line of `status.py` that is not `met`, including the count of the sovereign's acts off the log; held by counsel; deadline the window's end. A `promote` entered while a criterion did not hold is printed as a sovereign REPAIR.

The ladder is the charter's: re-invite; re-invite on another runner or model; writ to the sovereign [CHARTER §5]. The clerk decides nothing about validity and holds no change power; it cannot make an entry, sign one, or fetch anything [`tools/status.py` docstring: "No entry, no signing, no fetch. The clock enters only as --as-of"]. It is, in the charter's word, dumb — and that is a design property, because a clerk with judgement would be a reviewer (chapter 2 §2.2).

## 5.5 The item

What the clerk produces, besides writs, is the quantity chapter 6 will test. An **item** is a writ landing a timely act without the sovereign's hand: a resolution entered before its forecast's deadline by a principal other than the forecaster's, in a batch the herald merged; and a writ past its deadline is finalised as an item with *Y* = 0, as is any item the sovereign's key completes [BRIEF-C1b §Liveness]. Each item is a 0 or a 1, which is what Bahadur and Savage require of anything that is to be tested (chapter 6 §6.3), and whether it is a 1 is decided by the record and the clock, not by anyone's judgement. In the clerk's first window there were nine, every one a 1, and the ninth closed the window [`status.py --subject C1b --as-of 2026-11-01T11:31:58Z --runs transcripts/evidence/runs-tests-20261101b.json --acts transcripts/evidence/acts-20261101.csv @6b800e14`: items 9; seq 337].

## 5.6 What this chapter leaves open

We have a record, a law, and a clerk that turns the record's promises into deadlines and the deadlines into a sequence of zeros and ones. We do not yet know when the thing has *worked*. The sequence will be looked at by one person, when he wakes, who wants the layer promoted the day it has earned it and not at the end of a term — and a fixed-sample test lies to anyone who looks before the sample is complete. A test that may be looked at whenever one likes, on a bounded outcome, with the stake decided before the outcome, is chapter 6.

## 5.7 What would show this chapter wrong

A liveness claim made from a replay, or a safety claim made from a statistic — the division of §5.2 crossed. An obligation without a deadline, which would be untestable. A writ class built with no witness, or a witness with no class: the brief's rule is that the two match, and a referee can check the three classes against the record's late cases. And the top rung of the ladder exercised: the writ to the sovereign is read by a person, which is to say the ladder ends in him; the chapter claims only that it ends there visibly, and chapter 12 §12.4 prices what that costs.
