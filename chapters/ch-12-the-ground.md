# 12. The ground: where the regress stops, and why

*Draft 3, the author session, 3 November 2026 — renumbered on the construction; §12.7 settled on Shafer–Vovk alone (D36). Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## The figure: the trilemma

Ask why a claim is true and the answer is another claim; ask again and either the chain goes on for ever, or it circles back on itself, or it stops at something taken on no authority but its own. Agrippa's trilemma is two thousand years old and has no solution, only a choice of where to stand. Every institution makes the choice and most make it badly: the chain stops at a person, a party, a number someone picked. This chapter is where jack stands, seven times over, and why each place is the weakest thing the results allow.

## 12.0 Quis custodiet

Every institution of trust faces the same regress. The checker checks the entry; what checks the checker? The score scores the forecaster; who chose the score? The adviser advises the sovereign; who scores the adviser? The sovereign holds the keys; what holds him? Push on any of these and the usual answer, after a step or two, is an authority: a trusted party, a vendor, a number someone picked, a committee, a proof whose checker is taken on faith. Most institutions stop there and are the better for admitting it. The predecessors of jack (chapter 14) stopped there too — a judge, a vendor, a constant, an adviser — and the assize record is the measurement of how well that held: a hundred and twenty-one repairs in four days, twenty of twenty-four merges about the court itself [CHARTER §1].

jack's design principle for the regress is that **no chain of justification ends in an authority**. Each ends instead in one of seven things, and this chapter names them: size and diversity; a theorem or an election; a score; the owner of the utility; the world; a named assumption on the record; and a book that can go bankrupt. The claim is not that these are beyond question. It is that each is stated where a reader can find it, that each is the weakest thing the result it rests on allows, and that the residue of trust at each stop is written down rather than hidden. The chapter ends by saying why these are the right places to stop — why one level higher is impossible and one level lower is the mistake the predecessors made.

## 12.1 The judge and the checker end in size and diversity

What checks the checker? Two things, and the record says what they are.

*Size.* The kernel is 450 lines — `log.py` 172, `sig.py` 140, `check.py` 138 [`count_kernel.py @6ebea1a`] — and a person read it before he signed the line that made it law [CHARTER §9 criterion 4; seq 0]. That is the de Bruijn criterion applied to a court: the thing every entry passes through is small enough to be read entire, and the cleverness — the differential, the simulator, the clerk, the scorer, the election — is kept outside it, in tools that can be wrong without the record being wrong. The charter's stop condition is 1,500 lines; every layer has set a tighter bound, and the kernel has been within the sovereign's own target of 450 since C1a's installing push [CHARTER §9; A1.5; A2.4; seq 29].

*Diversity.* A second implementation, in Go, by sessions of another model family, written from `SPEC.md` and the vectors and nothing else [`kernel2/NOTES.md`]; compared with the first on every proper prefix of every one of 100,000 seeded logs with no disagreement in the run of record [`transcripts/diff-100000-20261025T1328Z-part00…11.json`: 100,000 logs, 636,392 prefixes, 0 disagreements], and on every proposal and every push since [SPEC §10.5, `checker_drift`]. Thompson's point is that one checker is evidence of nothing; Wheeler's is that two independent lineages agreeing is evidence of the specification. The specification is written for that purpose — a second author "who never sees the Python" must produce "the same verdict on every log" [SPEC, preamble] — and where the Python and the text disagree, the text wins and the disagreement is a finding.

The residue, stated: the differential cannot prove that the second checker is independent. Counsel's exit report said so — "that rests on the trusted-base rule, its provenance (`kernel2/NOTES.md`, `REVIEW-gemini.md`) and Guy's reading" [REPORT.md §8.3.7, as transcript] — and the book repeats it rather than improves on it. What the regress rests on at this stop is exactly: one person has read 450 lines, and two authors whose independence is a matter of record rather than proof agree on every input anyone has produced. That is less than a proof and more than any predecessor had.

## 12.2 The constants end in theorems or elections

Who chose the numbers? The law may contain a number on two conditions only, and the chapter 11 §11.10 audit — and appendix A §A.17 — is the test: it carries a proof, or it is a resource constant pre-stated before the window it bounds and enters no score. Every constant the law now carries, with its provenance:

| constant | value | provenance |
|---|---|---|
| the level | *E* ≥ 20 | 1/α at α = 0.05; Ville's inequality [CHARTER §6] |
| the mixture's regret | ln *K* | the sequential Bayes mixture's bound; η = 1 is the telescoping identity, the uniform prior the minimax choice for it [BRIEF-C2a §Scope, the aggregate] |
| the liveness stake | λᵢ = max(0, (q̂ᵢ − *p*₀)/(*p*₀(1 − *p*₀))), q̂ᵢ Laplace over the prefix | derived from the prefix "with no further constant"; λᵢ < 1/*p*₀ [CHARTER A4.3] |
| the value stake | λᵢ = min(max(0, *m*₁ᵢ/*m*₂ᵢ), 1 − 1/(*n*ᵢ + 2)), with two pseudo-items at ±*B* | predictable from the prior differences [CHARTER A4.4] |
| the bound on a difference | *B* = ln 999 | the per-mille grid [SPEC §5] |
| the base rate | (*s* + 1)/(*n* + 2) per type, in resolution order | Laplace's rule, pooled by type — "nothing finer than the type: a base rate per dataset or per venue would be a model, and a model is an entrant, not the null" [BRIEF-C2a §Scope, the base rate] |
| the null | *p*₀ = 6/11 for C1b | committed before the window, from the incumbent's series, never from the window it judges [CHARTER A4.2; BRIEF-C1b §Liveness] |
| windows | fourteen days, a maximum | the sovereign's budget [seq 50]; A5 |
| the cap | 7,800 counted lines at C2a | a resource constant raised by one push at the opening; enters no score [BRIEF-C2a §Scope, the cap; seq 367] |
| the procedure ratio | 5 : 1 | assize's measured figure, as the stop [CHARTER A3.4; §1] |

Everything that is not in that table is an entrant. The charter is explicit about the election rule itself — "an entrant, not law" [CHARTER §5] — and the C2a brief about the alternatives: Hedge with η < 1 "may enter later as an entrant of its own", a finer base rate would be a model, every model of the sovereign's answers is a competitor [BRIEF-C2a §Scope]. The regress of "who chose the number" therefore ends in one of two places: a bound someone can check, or a competition someone can lose. There is no third.

## 12.3 The adviser ends in scoring

Who scores the one who designed the court? The answer is the mechanism that assize's F6 forced: "counsel acted through Guy's token: unscored, unattributed" [CHARTER §1]. In jack counsel has a key of its own on the log [seqs 8, 22, 31, 48], acts only through entries that carry it, and every recommendation it makes to the sovereign is a forecast, resolved by what he did and by what happened, and scored like anyone's [CHARTER §2.4, corollary].

The score, recomputed by the author from the log and not copied from counsel's reports [`data/counsel-forecasts.md`; `jack score @6ebea1a`]: counsel has entered 82 forecasts, of which 40 are resolved, at a mean log-loss of 0.593 against 0.685 for the base-rate forecaster on the same events. On the world — eighteen resolved Hong Kong race forecasts — counsel's mean loss is 0.700 against the base rate's 0.736; on its own programme — seventeen resolved forecasts about what the court would do — 0.451 against 0.627. Counsel's worst single forecast on the ledger is a bet on the predecessor: p 0.3 that assize's `REPORT.md` would carry an L2 verdict line by 8 November, which it did, for a loss of 1.204 [seq 38; resolved at seq 109]. Counsel's first in-session forecasts about its own harness — that reviews would come back clean, at p 0.3, 0.75, 0.7 — all missed, and the exit report said so [REPORT.md §8.4, as transcript]. The point of the table is not that counsel forecasts well; it is that the question has an answer on the record, and the answer is a number that can fall.

The adviser is also subject to the clerk. Counsel's obligations are writs — W3 and W4 are held by counsel [BRIEF-C1b §The clerk] — and the four forecasts that expired in counsel's custody in C1a [seqs 45, 46, 47, 56] are the window's recorded failure and C1b's forcing witness. The designer of the court is inside it. That is Ostrom's principle, that monitors are accountable to the monitored, applied to the one party that had the pen.

## 12.4 The sovereign ends in the owner of the utility

What holds the one who holds the keys? Here the design stops deliberately at an authority, and the chapter says why and what is done about it.

The sovereign is the one unscored party, because the court's utility is his by definition: a wish is a preference, not a prediction, and "wishes are never scored" [CHARTER §7]. This is the CIRL commitment the programme began with in credence (chapter 14): the agent's utility is the owner's, so the owner's preference is the standard and cannot be graded against itself. The regress of "who judges the sovereign's wishes" ends in the owner of the utility and nowhere else, and the book does not pretend otherwise.

What is done about it is three things, each on the record. He is *priced*: every act of his is an entry, typed by its entry type and the key that signs it as a decision or a repair, "so the split is mechanical and fixed in advance" [CHARTER §7], and repairs are the quantity the liveness test exists to drive to zero. The classifier that counted his acts on assize — 88 decisions and 121 repairs in four days [CHARTER §1] — is the baseline; C1b's window counted none [`status.py --subject C1b … @6b800e14`: late-reported repairs 0, off-log repairs 0]. He is *confined* to the irreversible: the master key's verbs are `genesis`, `key`, `amend`, `push` and `decision` [seq 33], and a `decision` by any other key is refused [SPEC §10.14]. And he is *corrected where he forecasts*: his own three resolved forecasts stand on the ledger at a mean log-loss of 0.655 [`data/counsel-forecasts.md`; `jack score @6ebea1a`], resolved by a principal other than himself, and nothing about his role exempts them from the score. The first maxim was extended to him by amendment: someone other than the owner checks that the record's history was never rewritten [CHARTER A2.8].

The residue, stated: the sovereign could revoke every other key, veto every window and stop the court, and nothing in the law prevents it. The law does not try to. It makes each such act an entry on a record he cannot rewrite [A2.8], so that a court he stopped would show, to anyone who reads the log, exactly where and how.

## 12.5 Value ends in the world

What settles whether a forecast was right? Not a party. Outcomes come from processes that read no entry of the record: a race result from the HKJC's page, a dataset's `dateModified` from a public catalogue, a test run on a commit [BRIEF-C2a §Scope, the streams; `transcripts/world-types.md`]. The page is saved and its hash committed before the resolution cites it [BRIEF-C1 criterion 4]; the resolver is never the forecaster [`self_judged`]; and the C2a brief's third assumption about the election's draw is the same fact from the other side — the reward "is produced by a process that reads no entry of the record (renavon's public catalogue, which does not know the election exists)" [BRIEF-C2b §The draw].

This is Popper's stop and Dawid's at once. A claim is scored only against an outcome the claimant did not produce; the forecast is a move that cannot be taken back; and the world's answer is the last word, not because the world is an authority but because it is the only party with no stake. The residue at this stop is the evidence's provenance — a saved page can be forged — and the law's answer is the hash in the tree and the resolver's key, which make a forged resolution an act with a signature on it.

## 12.6 Randomness ends in a named assumption on the record

Where no theorem is available, the regress is stopped by stating the assumption where a reader can falsify it, never by hiding it. The clearest case is the election's draw (chapter 7 §7.4). EXP3 needs a draw the entrants cannot anticipate and the record can replay; jack's is the SHA-256 of the clerk key's Ed25519 signature over a round string, recorded in the invite so that anyone can verify the signature and replay the arm [BRIEF-C2b §The draw]. But a verifier cannot prove that the deterministic nonce was used: the key's custodian could sign the string repeatedly until the hash picked an arm of his choosing, and every such signature verifies. The brief therefore says what the draw is and is not — "a deterministic signature the record can verify and replay, unpredictable to anyone without the key, and a fair draw only under named assumptions about the key's custodian" — and names the three: the custodian signs once with the prescribed nonce; the hash of a fresh signature is indistinguishable from uniform on its grid; the round's reward vector is fixed before the draw [BRIEF-C2b §The draw, (i)–(iii)].

That is the general move. A verifiable random function would discharge the first assumption; the brief does not have one, says so, and records that the custody the draw rests on is the same custody every `merge` already rests on. A referee who wants to attack the election knows exactly where to push, and so does the court: the assumption is one line away from being a pin.

## 12.7 The court itself ends in a book that can go bankrupt

What checks the court? Not a proof of its own soundness: Gödel's second theorem forbids a consistent system that proves its own consistency, and Löb's forbids one that trusts its own proofs in general (chapter 10 §10.2). The substitute is not a weaker form of trust but a different object. The court keeps a wealth process on every claim it makes about itself, and never resets it.

Concretely: each layer's promotion is a bet against a null — that items are completed without repair no more often than the predecessor's rate; that the aggregate forecasts no better than the base rate — and the wealth of that bet, *E*ₜ, is a test supermartingale whose history is one sequence from the layer's first window onward [CHARTER A4.1: "*E* is never set back to 1 and no α is split. Ville's inequality then holds for the whole sequence at the layer's α"]. A window that fails does not start again; it continues the same product. The court's claims about itself — counsel's forecasts that a window will cross, that an amendment will bite, that the kernel will stay within its bound — are on the same ledger as its claims about the world and scored by the same rule [`data/counsel-forecasts.md`; seqs 37–42, 60, 121, 180–185]. So the whole institution is one sequential test against the null that it is not working, and a court that was fooling itself would be seen going broke: its wealth would sit at one, its forecasts about itself would lose to the base rate, and the acts tables would show its operator back in the loop. None of that can be hidden, because all of it is a fold over a log two checkers agree on.

The claim stops here, at Shafer and Vovk: the court is a bettor against its own null, its wealth is its evidence, and the kernel and amendment A4 are what prove it. Nothing is named as an ideal above that, because nothing above it was built or shaped what was built; chapter 15 §15.3 says in one sentence what the book does not claim of a related construction.

## 12.8 Why here, and not higher or lower

One level higher would be a proof of the court's correctness. Löb forbids it, and if it were produced it would need a checker of its own, and the regress would begin again one floor up. The book claims no such proof, and chapter 10 §10.2 is the record of why it does not try.

One level lower is where every predecessor stopped. A judge trusted because it was the judge (the predecessor's F1: the accused writing the test that judged it). A vendor trusted because it was the vendor (the charter's argument from requisite variety against naming one). A number trusted because someone picked it (the restart at each window that A4 removed). An adviser trusted because it had the pen (F6). The assize record is the empirical witness that this does not hold: not because the parties were dishonest, but because an unscored source of influence has unknown value, and a system with unknown values in it cannot drive its operator's cost to zero, because it cannot tell which of his acts it caused.

Between the proof that cannot exist and the authority that cannot be trusted, the seven stops of this chapter are where the regress can be held: a size a person can read and a second author who agrees; a bound or a competition; a score; the one party whose utility is the standard, priced and confined; the world; an assumption written where it can be attacked; and a book that can be seen to go bankrupt. Each is the weakest thing its result allows. Each is on the record. The residue at each is stated. That is the ground.

## 12.9 What this chapter leaves open

The construction is complete and its regress is grounded. What remains is to show that it ran: that the windows crossed on the terms pre-stated for them, with every number recomputed; that the lineage is the same loop run open; and that the ways it could be wrong were written before the evidence came in. Chapters 13 to 15.

## 12.10 What would show this chapter wrong

A stop that is actually an authority. The test for each section: can a reader find, on the record, the thing the chapter says the regress ends in, and check it? For §12.1 the kernel and the differential's reports; for §12.2 the table and the charter's clauses; for §12.3 and §12.4 the ledger, recomputed; for §12.5 the hashed pages; for §12.6 the brief's three assumptions; for §12.7 the wealth process and A4.1. If any of these turns out to rest on something the chapter has not named — a constant with no provenance, a resolution by a forecaster's second key, a reset — the chapter has an authority in it and must say which.

The residues understated. Each section names what its stop does not cover. A referee who finds a larger residue — that the two checkers share a defect because both authors read the same misleading sentence of `SPEC.md`, say, which the differential cannot detect — has found something the book must add, and the C0 report's finding that three disagreements came from reviews and byte probes and none from a simulated log [REPORT.md §8.4, as transcript] is the kind of evidence that would support it.

The sovereign's residue exercised. If the sovereign revoked keys and stopped the court, the chapter's claim is only that the record would show it; it makes no claim that the court would survive. That is the one place the design accepts an authority, and the book should be read as saying so.


