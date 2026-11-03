# 2. Every suggestion is a bet

*Draft 1, the author session, 3 November 2026. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`. The four results here are set out row by row, with hypotheses, in appendix A.*

## The figure: the tipster

A racing tipster tells you the favourite will win the seventh. You cannot inspect the tip. You can read his reasoning, which is fluent, and his record, which he wrote. The only thing that tells you whether to pay for the next tip is the one thing neither of you controls: the seventh race, run. And even that tells you nothing unless the tip was fixed before the off, the result was recorded by someone other than him, and the thing he is paid on is a number that rewards him for saying what he actually believes rather than what sounds confident. Every tipping service that has lasted has those four properties; every one that has not had the reasoning and the record. The helpers of chapter 0 are tipsters, and this chapter is the four properties.

## 2.1 What we have, and what it cannot do

We have a loop (chapter 1) that keeps suggestions that paid and discards those that did not. The suggestions are a language model's: a program, a probability, a plan, a draft. The loop needs to tell a good one from a bad one, and the natural way — read it, think about it, decide — is the one thing the theory forbids.

## 2.2 Merit cannot be inspected — Rice (1953)

**Result** (theorem). In a language that can write the next version of itself, every non-trivial property of what a program *does* — as opposed to what its text looks like — is undecidable. The hypotheses are two: full computational power, and the property being extensional, a property of the function computed. Decidable properties remain: syntactic ones, and semantic ones of languages that are not Turing-complete.

**What it forces.** "This change is an improvement" is a property of the program's behaviour, and for any language the helpers will want to use, Rice says no procedure settles it by inspection. And it is a property not of the program alone but of the program in the world: a forecasting program is better only if the races come out as it said. So the only route left is to run the change and observe, and the observing must be done by something that reads the world, not the program. Pearl (2009, ch. 3) is the same point from the learner's side: the effects of actions are not identifiable from observation alone, so an autonomous agent must experiment, and its experiments must be scored by something it does not control. *Nothing is reviewed on its merits; every claim of merit is a forecast, resolved by the world.*

**Mechanism.** The charter confines its statutes to decidable properties on exactly this ground and separates validity from merit in the same clause — questions of merit "are forecasts, scored when the world resolves them" [CHARTER §3, Adjudication]. Every check the kernel makes is syntactic and terminates [SPEC §8]; every ground the judge may refuse on must be "decidable from git and the log alone" [CHARTER A2.3]. The judge never runs a proposal's code; it runs trunk's checkers over the proposal's entries *as data* [SPEC §10.5; `judge/judge.py:run_kernel`]. For the agent of chapter 10, merit is a sealed judge running the candidate on seeds it never saw [CHARTER §8, C3].

**Misapplied if.** Someone proposes that the judge "check that the change is good", or the court mistakes a decidable fact for merit — a green test run is a decidable fact about a commit and evidence of nothing about worth, which is why the predecessor's three review rounds on how a status file cited a green run are recorded as a failure [CHARTER §1, F4].

## 2.3 Only issued forecasts count — Dawid (1984)

**Result** (principle; its force is what it excludes). A forecaster is assessed on nothing but the probability forecasts it actually issued and the outcomes that then occurred — no model of the forecaster, no revision of an issued forecast after its outcome, no "what it would have said".

**What it forces.** If merit can only be scored, the evidence must be of this form: a probability fixed at a known time before the outcome, and an outcome recorded by someone else, once. Anything else — a revision after the event, a second resolution correcting the first, a score recomputed from forecasts the forecaster did not issue — reopens the inspection Rice closed, through the back door.

**Mechanism.** The ledger is the file format of the principle. A `forecast` entry carries a claim, a probability `p` as an integer from 1 to 999 per mille, and a `resolves_by` not earlier than its own timestamp; a `resolution` names the forecast's seq, an outcome in {0, 1}, and evidence [SPEC §5]. The probability is fixed at the entry's position because timestamps do not decrease along the record [SPEC §7; `kernel/check.py` line 59] and the chain fixes the position [SPEC §3]. A second resolution is refused as `schema`; a resolution by the forecast's own principal as `self_judged` [SPEC §8 steps 7 and 8a; `kernel/check.py` line 82]. The world's evidence is a page saved and hashed into the tree before the resolution cites it [BRIEF-C1 criterion 4].

**Misapplied if.** A score uses a probability fixed after its event. The record names the two ways: a forecast timestamped at or after the event's cutoff is listed as `rigged` and not used — three are on the log, seqs 288–290 — and a later forecast of the same event by the same principal is a `revision`; the first stands [BRIEF-C2a §Scope, the entrants].

## 2.4 Only a proper score rewards belief — Good (1952), Savage (1971), Gneiting and Raftery (2007)

**Result** (theorem). A scoring rule is *proper* if, whatever the forecaster believes, reporting that belief maximises its expected score, and *strictly proper* if it is the unique maximiser. The logarithmic score, ln *P*(*y*), is strictly proper; on a grid of reports, truthfulness holds to within the grid.

**What it forces.** The score is the one thing in the construction that will be rigid at every level, so it must be one that cannot be gamed by shading. Among strictly proper scores the logarithmic one is chosen by a second consideration. Under it, the Bayes mixture over *K* forecasters is the posterior predictive, so aggregating is conditioning (chapter 0), and its loss telescopes to at most ln *K* more than the best of them at η = 1, with no tuning constant. Other mixable losses reach a bound of that form through Vovk's (1990) aggregating algorithm, the Brier score even at η = 1. But for them the forecast is produced by a substitution step, not by the mixture itself, so the aggregate is not conditioning. The bound alone would not force the log score; the bound together with conditioning does. That bound will be the only constant the election is allowed to carry (chapter 7).

**Mechanism.** Probabilities are per mille because canonical lines admit integers only and because 1–999 bounds the log-loss without a clipping rule [SPEC §5]. The score is log-loss, computed outside the kernel by `jack score` [SPEC §12.11]. The base-rate forecaster every value test runs against is Laplace's rule over the resolved prefix of the forecast's type, clipped to [1/1000, 999/1000] so that a difference of two losses is bounded by *B* = ln 999 [BRIEF-C2a §Scope, the base rate; CHARTER A4.4].

**Misapplied if.** A score that is not strictly proper enters a promotion criterion or an election, or a transformation is applied that breaks propriety (a cap on the loss per forecast would; the per-mille grid, which bounds the report, does not).

## 2.5 The target decays — Goodhart (1975)

**Result** (regularity, not a theorem). Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes. Manheim and Garrabrant (2018) separate the mechanisms — regressional, extremal, causal, adversarial — and for a court whose entrants are optimising policies the adversarial case is the one that matters.

**What it forces.** A measure that is a target is safe only when the measured party cannot move it except by doing the thing it measures. The score being proper gives half of that; the other half is that the outcomes scored come from processes the party does not control. A third condition follows for the court itself: its own statistics — items completed, forecasts resolved — can be manufactured by producing more court, so it must count its procedure against its object and stop when the ratio turns.

**Mechanism.** Outcomes come from the world: `world.hkjc` resolves from the HKJC's results page, saved and hashed, by a principal other than the forecaster's; `world.renavon` from the `dateModified` of a public catalogue page fetched after the window [BRIEF-C2a §Scope, the streams; `transcripts/world-types.md`]. The sovereign's own acts are typed by entry type and signing key, "so the split is mechanical and fixed in advance, not judged afterwards" [CHARTER §7]. The ratio of procedure to object entries is computed every window and stops the layer above 5 : 1, the predecessor's figure [CHARTER A3.4; `tools/status.py:assess`]: the first ledger window ran at 127 : 32, the clerk's at 67 : 82 — the first in which the court wrote more about the world than about itself [`status.py --subject C1a` and `--subject C1b` at their exit prefixes @6b800e14].

**Misapplied if.** A promotion statistic counts something a proposer can produce without doing the work. The design has one such count — the first ledger window's criterion of at least twenty forecasts by three proposers [BRIEF-C1] — and the book calls it what it is: a test that the record was alive, not that anything in it was worth anything.

## 2.6 What this chapter leaves open

We now know what a suggestion is: a claim, with a probability fixed before the outcome, scored properly against an outcome nobody in the loop controls. We do not yet have anywhere to put it. "Fixed before the outcome" and "recorded by someone else, once" are properties of a *record* — one that cannot be rewritten, in which order is a fact, and in which who wrote what is a fact rather than a claim. Building that record, and only that, is chapter 3.

## 2.7 What would show this chapter wrong

A helper whose suggestions can be verified rather than scored — a policy whose outputs are checkable by inspection. Rice says not in a language that can write the next version of itself; a restricted language may escape it (chapter 10 §10.5). A score in the court that is not strictly proper, or a resolution by a forecaster's second key — the pins `forecast_before_cutoff`, `rigged`, `revision` and `self_judged` exist so these fire in CI rather than in a reader's hand. And the one that would matter most: an outcome stream that the proposers turn out to control — a catalogue that reads the election, a results page a session can edit. The hashes in the tree and the resolver's key make that an act with a signature on it, and chapter 12 §12.5 says what residue remains.
