# 7. The election

## The figure: the canon

Nobody chose the canon. No committee sat to decide that one play would be read in four centuries and its contemporaries would not; what happened is that each generation re-read what the last had kept, and kept what still paid. The score was proper — nothing is gained by pretending to enjoy a book — and the outcome was one no author controlled. Critics are the review loop, and a critic who is wrong about what will last is scored by the shelves. A canon is an election by record, run over centuries with no returning officer; the mixture of what is read now is the weights, and the weights move. This chapter builds the same thing for the helpers of chapter 0, with the centuries compressed to a window and the shelves to a log.

## 7.1 What we have, and what it cannot do

We have helpers whose every suggestion is a scored bet (chapter 2), a record of the scores (chapter 3), and a test that says when a layer has worked (chapter 6). We do not have a way to decide *which* helper should be invited to the next task, and the obvious ways are all forbidden. Naming one in law makes it an authority that stops being tested, and gives the pool the variety of one source (chapter 1). Letting a person choose puts his attention back in the loop and makes the choice a judgement with no score on it. Letting the helpers choose themselves is self-judgement. What is left is to make the choice a *statistic* — a function of the record with a bound on how badly it can do — and to make that statistic itself an entrant that can lose.

## 7.2 Aggregation with a bound — Freund and Schapire (1997)

**Result** (theorem). Hedge: keep a weight on each of *K* experts, multiply each weight by e^(−η · loss) after every round, and predict with the weighted mixture. The cumulative loss of the mixture is within ln *K* /η + η *T*/8 of the best expert's (for bounded losses), and for the logarithmic loss at η = 1 the mixture is the Bayes mixture — the posterior predictive under a uniform prior over the experts — and its cumulative log-loss is within ln *K* of the best expert's with no other term: the telescoping identity of chapter 2 §2.4.

**What it forces.** The aggregate is the Bayes mixture with the uniform prior and no learning rate, because "η = 1 is the telescoping identity, the uniform prior the minimax choice for the ln *K* bound" [BRIEF-C2a §Scope, the aggregate]. The one constant it carries, ln *K*, is derived; a hand-set rate or prior would be an authority.

**Mechanism.** The roster is frozen at the window's opening — every principal holding `forecast` at that instant, plus the base-rate forecaster [BRIEF-C2a §Scope, the entrants]. Weights are taken in *resolution* order: an event resolves at its first `resolution` entry, and the aggregate's probability for it is the weighted mean of the entrants' probabilities with weight proportional to each entrant's likelihood on the events resolved before — none at the opening. The entrants' probabilities are their forecasts fixed before the event's cutoff; the weights are fixed by the resolved prefix; "nothing about the event itself enters either". An entrant that made no forecast on an event abstains, and an abstention scores as the base rate — Blackwell's garbling (appendix A §A.15), and the reason the base rate is the null. Two keys of one principal are one entrant; the first forecast per principal per event stands and a later one is a `revision`; a forecast at or after the cutoff is `rigged` and not used. Probabilities and weights are exact fractions [BRIEF-C2a §Scope].

**Misapplied if.** A weight, prior or rate is set by hand — the pins `uniform_prior` and `no_learning_rate` kill that mutant — or the weights are taken at an event's first forecast rather than its resolution, which breaks the identity (the counterexample is in the brief's first cold read [`transcripts/REVIEW-C2a-v1.md`, F3]).

## 7.3 The bandit case — Auer, Cesa-Bianchi, Freund and Schapire (2002)

**Result** (theorem). When only the chosen expert's outcome is observed — the invited helper's forecasts resolve; the others' would-have-beens do not exist — EXP3 keeps exponential weights on importance-weighted gains and draws the next arm from a mixture of the weights and a uniform exploration term; its expected regret against the best fixed arm is of order √(*TK* ln *K*). Joulani, György and Szepesvári (2013) handle feedback that arrives *D* rounds late by running *D* + 1 independent instances, each seeing a complete record of its own rounds.

**What it forces.** An invitation — "this helper runs the next session" — is a bandit decision: the court learns what the invited one earned and nothing about the rest. So from the first invite the election is EXP3, and because a round's six outcomes resolve about three hours after its invite while three later invites are due, the clerk runs four interleaved instances, round *t* going to instance *t* mod 4 [BRIEF-C2b §The election]. A round whose previous round is not yet resolved when its draw is due waits, and is skipped at the window's end rather than drawn on stale weights, "because an invite drawn on stale weights is outside the theorem".

**Mechanism.** An invitation is a `forecast` of type `election.invite` signed by the clerk's key; the kernel reads neither `type` nor `args`, so the election needs no kernel change [BRIEF-C2b, preamble; SPEC §5]. The round's gain is built from the invited arm's mean log-loss ℓ over the six events of its stream window, with an unresolved event counted at the maximum: *g* = (ln 1000 − ℓ) / ln 999, which lies in [0, 1] and is larger the better the arm forecast [BRIEF-C2b, the round's gain]. The importance weight divides by the *recorded* propensity — the grid mass of the arm's interval at the draw, an exact rational saved in the invite — never a later one. The bound is stated as what it is: expected, loose at this horizon, and "the election is an entrant".

## 7.4 The draw, and its three assumptions

The theorem needs a draw the entrants cannot anticipate and the record can replay. The clerk's draw is the SHA-256 of the clerk key's Ed25519 signature over the round string `election.invite <stream> <W0>`, read as an integer on the grid of 2²⁵⁶ and matched against cuts computed from the weights; the signature is recorded in the invite, so anyone can verify it against the public key and replay the arm [BRIEF-C2b §The draw]. Ed25519 signing is deterministic, so an honest signer produces one signature per round. But verification cannot prove the deterministic nonce was used: the key's custodian could sign the same string with other nonces until the hash picked the arm he wanted, and every such signature verifies.

The brief therefore says what the draw is and is not — "a deterministic signature the record can verify and replay, unpredictable to anyone without the key, and a fair draw only under named assumptions" — and names the three: (i) the custodian signs once, with the prescribed nonce — the same custody every `merge` already rests on; (ii) the hash of a fresh signature is indistinguishable from uniform on its grid; (iii) the round's reward vector is fixed before the draw, because the outcomes come from a process that reads no entry of the record and each arm's forecasts are the same function of the public record whether or not the arm was drawn [BRIEF-C2b §The draw, (i)–(iii)]. A verifiable random function would discharge (i); the brief does not have one and says so. This is the general move of chapter 12 §12.6: where no theorem is available, the assumption is written where it can be attacked.

## 7.5 The election as an entrant

The charter is explicit that the election rule is not law: "Which proposer is invited is an election by Hedge or Fixed Share on proper scores … EXP3 under bandit feedback … an entrant, not law" [CHARTER §5]. Herbster and Warmuth's Fixed Share (1998), which can change its mind about who is best when the experts drift, enters later as a competitor to Hedge, scored like anything else; so would Thompson sampling, a finer prior, any base rate finer than a type. The audit criterion counsel drew from amendment A4 — the law names scores and competitions, never competitors [`claude/literature-review.md` §6] — is what keeps the election from becoming the authority it replaced.

## 7.6 What the record shows before the election acts

The scores that the election will consume already exist, and they already discriminate. On the log as it stands, the builder scores worse than the base rate on the freshness stream — a mean log-loss of 0.629 against the base rate's 0.394 over twelve resolved events — and counsel worse on its one resolved assize forecast, while the reviewer scores better than the base rate on all four streams it has entered, and counsel better on three of its four [`jack score @6ebea1a`; `data/counsel-forecasts.md`]. In the Bayes mixture those entrants' weights have already moved the way the election would move them. The window exists to establish this in advance rather than in hindsight.

## 7.7 What this chapter leaves open

The loop now chooses its own helpers by their record, and the rule that chooses is itself one that can be beaten. Every mechanism so far has been built from a text: a brief that pre-stated it, pins that a reviewer named, code a builder wrote to the text. But the texts began as sentences in English — a wish, a ruling, a draft — and nothing yet says how a sentence becomes a refusal, or how much of what was said ever did. That is chapter 8.

## 7.8 What would show this chapter wrong

The mixture's weights taken at the wrong instant, a learning rate or prior set by hand, a propensity recomputed after the draw: each has a pin or a cold-read finding behind it, and chapter 13 lists which fired. The draw's three assumptions exercised against it — a custodian re-signing until the hash obliged — which the record could not detect but which the brief locates exactly. And the election losing to a fixed choice: if, at C2b's exit, inviting the same helper every round would have scored better than EXP3 did, the regret bound was not the point and the chapter must say what was.

---

*Draft note. Draft 1, the author session, 3 November 2026. The theory and the brief as it stands are here; the election's own record waits for C2b's exit and `data/C2b-exit.md`. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`; the C2b brief cited is `transcripts/BRIEF-C2b-draft.md` v6, under cold review as this is written.*
