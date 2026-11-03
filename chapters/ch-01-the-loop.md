# 1. The loop

*Draft 1, the author session, 3 November 2026. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## The figure: a child

A baby does not plan. It proposes everything — a reach, a sound, a face — and the world resolves each proposal at once: the cup falls, the sound is answered, the face is returned. Nothing is reviewed. No one inspects the hypothesis before it is tried, and the child has no language in which it could be inspected. What it has is a loop: act, observe, keep what paid, discard what did not, act again. Learning begins before words because the loop does not need them; it needs only that the world answer and that the answer reach the thing that acted. Every adapting system anyone has ever seen has this shape, and this chapter's claim is that it could not have any other.

## 1.1 What we have, and what it cannot do

We have a question (chapter 0): a system that acts optimally for us, from what we say, through imperfect helpers, in a world that charges, after we have stopped watching. The simplest thing that could answer it is a plan: decide once, from everything known now, what the system should do, and have it do that. A plan is an open loop. Its outputs do not depend on what the world does in response; and so it cannot adapt, by definition, because adapting is changing what you do in response to what the world did.

The question has "after we have stopped watching" in it, and a world that charges, which means a world that changes. So the system must adapt, and the plan is ruled out before any theorem is stated. The theorems say what rules it out, and — more useful — what the loop that replaces it must contain.

## 1.2 Requisite variety — Ashby (1956)

**Result** (theorem; chapter 11 of *An Introduction to Cybernetics*). Let a system be subject to disturbances *D* and regulated by a regulator *R* that acts on the outcome *Z*. Then the variety of the outcomes can be reduced by the regulator by no more than the regulator's own variety: *V*(*Z*) ≥ *V*(*D*) − *V*(*R*). "Only variety can destroy variety." A regulator with fewer distinguishable responses than the disturbances it faces cannot hold the outcome within bounds, whatever it does.

**What it forces.** A regulator that cannot see the disturbance cannot respond to it; its effective variety against that disturbance is one. So a system that is to hold its outcomes within bounds against a world it does not control must observe the world and respond — must be a closed loop — and must have, in its responses, at least the variety of what the world can do to it. For the system of chapter 0 the second half has a concrete consequence: the helpers inside it are the regulator's variety, and the disturbances include the helpers' own failures — one vendor's outage, one model's blind spot, one account's limit. A pool of helpers from one source has the variety of that source. The law will therefore never name a model or a vendor, and the pool will be several families competing (chapter 7). The Renaissance is the figure for this half: when courts, cities, patrons and presses multiplied past any one authority's reach, the rate at which Europe adapted jumped, and no one planned it.

**Mechanism.** The judge's grounds are "stated over powers and paths and never over a party's name" [CHARTER A2.3]; the election rule is "an entrant, not law" [CHARTER §5]; the proposers on the record are sessions of more than one model family [`kernel2/NOTES.md`; the C1b window's sessions in `transcripts/`]; and the charter's own argument for several families is Ashby's, in these words: the pool "must carry at least the variety of the disturbances it absorbs" [CHARTER §5, last paragraph].

**Misapplied if.** The law names a vendor or a model, or the pool collapses to one source. Assize's instruction #173 is the witness in its own words — "a model that can't run loses its round, and the session runs again" — filed after a review failed on one provider's session limit and had to be re-dispatched by hand [`claude/guy-acts-6-13oct.csv`, 13 October 19:43–19:46].

## 1.3 Every good regulator is a model — Conant and Ashby (1970)

**Result** (necessity theorem, under conditions that must be stated because the theorem is often overstated). For a regulator *R* of a system *S* against disturbances *D*, with outcomes *Z* = ψ(*D*, *R*) and the goal of minimising the variety of *Z*: any regulator that is optimal and no more complex than it need be is a model of *S* — its behaviour is a mapping of the system's state that reproduces the system's response. What the theorem establishes, read carefully, is that an optimal regulator's action must be a function of a representation of the regulated system that is sufficient to determine the outcome; anything the regulator acts on that is not in that representation is either redundant or wrong.

**What it forces.** The loop must have, inside it, a model of the thing it governs that is complete enough to determine what the governor should do — and it must act on that model and on nothing else, because anything outside it is unaccountable. For the system of chapter 0 the model is a *record*: everything that has been proposed, resolved, promised and done, in an order no one can rewrite, folded by a fixed rule into a state. Nothing that governs may bypass it. The baby's model is its body; ours will be a log.

**Mechanism.** The state the law folds the record into is ten things — the head of the chain, the keys and their powers, the charter in force, the trusted base, the forecasts and which are resolved, the previous timestamp [`kernel/check.py:State`; SPEC §7] — and the checker that folds it reads nothing else: no clock, no network, no model [CHARTER §9, refusal list; `kernel2/NOTES.md`]. The clerk derives every obligation from that state and the clock, and the clock enters only as an argument [`tools/status.py` docstring; `tools/clerk.py`]. The record is a replicated state machine (Schneider 1990), ordered by its chain and not by wall time (Lamport 1978).

**Misapplied if.** An obligation lives outside the record. The predecessor's stalls were found by a human watching a phone [CHARTER §1, F3]; jack's own four forecasts expired undischarged in its first ledger window while the clerk was still in a session's memory rather than a process [seqs 45, 46, 47, 56; resolved late at seqs 52, 69, 70, 108]. Chapter 5 is built on that witness.

## 1.4 Closed beats open — the form of the loop

Two further facts about the loop's form are engineering rather than theorem, and the record supplies the witness for each.

**Level-triggered, not event-triggered** (Burns et al. 2016). A controller that reconciles desired and actual *state* loses nothing when an event is missed; one that reacts to events loses the obligation with the event. Nothing in jack waits for an event: the record loop judges a proposal against trunk whenever it is judged, the clerk reads the whole log every tick and keeps no state between ticks, the scorer and the aggregate are pure folds over the resolved prefix [BRIEF-C1b §The clerk; `tools/value.py`: "pure entry folds; the CLI alone reads files/the clock"]. The one event-triggered component is the judge, which runs when a pull request opens, and the charter assigns reconciliation to the clerk rather than to it [LAW.md §2.3].

**Conditioning at every step.** This is the oldest commitment in the lineage: credence's first architectural choice was closed-loop over open-loop, with beliefs changed only by conditioning on what the world returned [`credence/CONSTITUTION.md` §2.1; chapter 14]. It reappears at the institutional scale as: nothing is decided once; every window, every election, every promotion is recomputed from the prefix.

## 1.5 What this chapter leaves open

We have the shape: a closed loop with a record inside it, responding with the variety of several helpers. We do not yet have the thing the loop runs *on*. A helper makes a suggestion; the loop must keep it if it paid and discard it if it did not. The baby's world answered at once and unambiguously. Ours will answer later, partially, and in a currency — and the suggestion, unlike a reach for a cup, is a piece of code or a probability whose merit cannot be seen by looking at it. How to tell a good suggestion from a bad one, when inspection is not available, is chapter 2.

## 1.6 What would show this chapter wrong

An adapting system that is not a loop — a plan that holds its outcomes within bounds against a changing world without observing it. Ashby says there is none; a counterexample would be a disturbance with no variety, which is to say a world that does not change, which is not the question. A regulator shown to act well on information not in its model — which would mean the model was not sufficient, and the fix is a larger record, not a smaller one. And the mechanism rows above failing on the record: a ground that names a party, a tool that reads the clock in a fold, an obligation held in a head. The pins exist so these fire in CI; chapter 13 lists which have.
