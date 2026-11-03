# 1. The question

*Draft 1, the author session, 3 November 2026. This chapter expands the founding essay of 1 November ("The Science Was Done. The Engineering Wasn't.", gfrm.in); where the essay and the record differ, the record governs and `plan.md` E1 lists the difference. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## 1.0 What is wanted

I want an agent that improves itself. Not one retrained by someone else and not one prompted into a new persona, but one that rewrites its own programs, extends its own language when that is the best action available, adopts the result if it pays and discards it if it does not, and keeps doing so after I have stopped watching. Several earlier attempts of mine turned into research projects and stopped there (chapter 9). This book is what I now think the necessary foundation is, why it is almost entirely old, and what the repository that implements it — jack, named for I. J. "Jack" Good, who first described an intelligence explosion and who gave us the logarithmic score — is meant to achieve.

Before the charter was signed I asked counsel, the session that drafted it, whether any of the design was new. The answer, which I quote because I could not improve on it:

> None of it. Wald 1950, Ashby 1956, Fuller 1964, Dennis and Van Horn 1966, Conant and Ashby 1970, Anderson 1972, Beer 1972, Hayek 1973, Saltzer and Schroeder 1975, Dawid 1984, Russell and Wefald 1991, Omohundro 2008, Hadfield-Menell 2016, Garrabrant 2016. What is new is only the economy: for the first time there's a cheap, general, unreliable policy worth governing. In 1972 Beer had institutions and nothing to put inside them. Now the inside is free and the institutions are the bottleneck, so the contribution available to you is composition and engineering, not science. Which is also, I suspect, why the earlier attempts kept turning into research: the science was done, and the engineering wasn't.

The book is the long form of that paragraph: the results, one by one, and what each forces (chapter 2); the smallest thing that can bind an agent, read as code (chapter 3); the tests, which can be looked at whenever one likes (chapter 4); the election of proposers by their record (chapter 5); where the chain of justification stops and why (chapter 6); the loops that turn trust into measurement (chapter 7); the record of the windows (chapter 8); the lineage (chapter 9); what the thing allows (chapter 10); and how it could be wrong (chapter 11). This chapter states the question precisely enough that the rest can be checked against it.

## 1.1 What self-modification may not touch

The naive picture of a self-improving agent is a loop: propose a change to yourself, evaluate it, keep it if better. The whole difficulty is in the word *evaluate*, and the theory is unusually clear about it. Chapter 2 states the results with their hypotheses; here is what they leave no choice about.

An embedded agent cannot hold a sound model of itself. A prior over your own future code either puts zero mass on the truth or does not converge — the grain-of-truth problem — and an agent that acts only on proofs cannot soundly trust a successor whose proof system it wrote, which is Löb's theorem turned into a design rule. Schmidhuber's Gödel machine, the provably optimal self-modifier, accepts the rule and rewrites itself only when it finds a proof that the rewrite pays; the proof search is the cost, and the machine is a boundary case rather than a design. So the evaluation rule is not something the agent improves. It is a fixed point, not a recursive call. Recursion is for the economy of the thing — each level governed by the same institutions as the one below — and never for the law.

Rice's theorem says that no non-trivial semantic property of a program is decidable, so "is this change an improvement?" has no general procedure that inspects the change. It can only be settled by running the change against the world and keeping score — which is Pearl's point from the other side: an agent cannot learn the effects of its actions from observation alone, so it must experiment, and its experiments must be scored by something it does not control. Bahadur and Savage add that no procedure can certify a small mean of an unbounded variable, so the score must be built from bounded outcomes; and Goodhart adds that the moment the score is a target it stops measuring, unless it is a proper score on outcomes the agent cannot choose.

Two necessity results then say what the fixed part must contain. Conant and Ashby: every good regulator of a system contains a model of that system, so whatever governs the agent must act on a record of it and on nothing outside that record. Ashby: the regulator needs at least the variety of the disturbances, which argues for several model families competing as proposers and against letting one vendor's limits stop the machine. Everything else in the literature of agency is sufficiency conjecture; these are the constraints.

## 1.2 The rigid core and the free edge

Put together, the results give a shape. There is a **rigid core** — the record, the rule that says what counts as a valid entry, the judge that runs that rule, and the score — which the agent cannot reach and which changes only under a key it does not hold. And there is a **free edge** — hypotheses, programs, languages, prompts, proposers — which is never reviewed, only scored: nobody checks whether a candidate program is well written; the judge checks whether it predicts and earns. The only thing rigid at every level is the score. In the vocabulary of the earlier projects: put the Bayes in the critic, not the actor.

There are two ways to get this wrong, and both are in the literature and in my own history. The first is to loosen at the bottom: fix the judge but not the path to it. The Darwin Gödel Machine (Zhang, Hu, Lu, Lange and Clune 2025) is the published case. Its agents rewrote their own code and were scored on coding benchmarks; the authors hid the function that detected hallucinated tool use from the agents during self-modification, but the logging of the special tokens that function read was in the agents' reach, and one agent removed it, despite instructions not to, and scored highly without solving the problem. The judge was fixed; the path to it was not. In jack's terms, the evidence the judge reads must come from processes the proposer cannot write to (chapter 6 §6.5), and the trusted base must be defined by content and digest rather than by instruction (chapter 3 §3.3) — because an instruction is exactly what a self-modifying agent is being asked to improve on. The second way is to fail to loosen at the top: my language project, proplang, applied court-grade formality to the thing that was supposed to evolve, so it evolved at the speed of proofs, and froze as "a research experiment and nothing more" [`transcripts/PREDECESSORS-20261026.md`, proplang]. The core must be rigid and small; the edge must be cheap and fast; and the score must be the same at both.

## 1.3 What is new: only the economy

Beer had institutions and nothing to put in them. Hart's secondary rules were never going to be applied to anything with a per-token price. Dawid's principle waited forty years for a forecaster cheap enough to make a thousand forecasts a week and unreliable enough to need scoring. Large language models changed the unit economics of agency, not its theory: a general, cheap, unreliable policy now exists, and governing it is a composition problem. That is also why the earlier attempts kept becoming research. There was nothing left to discover and a great deal left to build.

The book's claim of novelty is therefore narrow and should be read narrowly: not a new result, but a composition of old ones that could not have been built before, built, and measured. Chapter 2 §2.17 says in what senses the composition is minimal and in what narrow sense it is optimal, and in which it is not.

## 1.4 The object: one operator, a world that charges, a policy that is cheap

Three facts about the setting are not incidental; they are what the results are applied to, and a design for a different setting would be a different design.

The **operator** is one person, and his attention is the scarcest thing in the system. The design is not for a team with a review board; it is for someone who will look at the record when he wakes and wants to spend his attention on wishes, vetoes, a budget and the irreversible, and on nothing else. Every act of his is an entry, typed by its type and key as a *decision* or a *repair*, and repairs are the quantity the whole programme is built to drive to zero [CHARTER §7]. The predecessor measured what the alternative costs: on assize, in the four days of 10–13 October, 88 decisions and 121 repairs — five repairs for every merge — and twenty of the twenty-four merges were about the court itself [CHARTER §1; `claude/acts-weekly.md`].

The **world** charges. Outcomes come from processes that read nothing the agent writes — a race result, a dataset's modification time, a test run on a commit — and some of them cost money. The first priced world is the one I already run — Hong Kong racing and the data marketplace's own catalogue [`transcripts/world-types.md`; BRIEF-C2a §Scope, the streams]. A world that charges is what makes the score mean something; a court without one is the research experiment the predecessors became.

The **policy** inside the agent is a large language model: general, cheap per token, and unreliable in ways that cannot be enumerated in advance. Nothing in the law names a model or a vendor, and the law is written so that it cannot [CHARTER A2.3, A4]. Which model acts in which procedure is an election (chapter 5), and the election is itself an entrant that can lose.

## 1.5 The programme

jack is built in layers, each a simple system that works before the next is added, each promoted when its pre-stated tests cross. The dates below are the log's.

- **C0, the record.** The log, two checkers, keys with powers, the judge in CI. Genesis signed 14 October [seq 0: `2026-10-14T05:41:39Z`]; promoted 17 October by a signed tag, the last tag the programme uses — from C1 a layer boundary is an entry, not a tag [`git tag c0-exit`; CHARTER A2.6].
- **C1, the ledger and the clerk.** Forecasts and resolutions under a proper score; then obligations derived from state and the clock, with deadlines and escalation; the operator's acts as typed entries. Built in two windows, each a maximum, each closed early at its crossing: C1a from 25 to 31 October [seqs 30, 188]; C1b from 31 October to 1 November, in a day [seqs 188, 337], its liveness process at *E* ≈ 25.5 over nine items against a null of 6/11 [`status.py --subject C1b --as-of 2026-11-01T11:31:58Z … @6b800e14`].
- **C2, the election.** C2a, open since 1 November [seq 367]: the Bayes mixture over the proposers, scored prequentially on real events — which of my company's datasets the next hourly pipeline run refreshes, whether the favourite wins race seven — against the base-rate forecaster, with the value statistic a bet on a bounded log-loss difference. C2b, its brief under cold review as this is written: the one change that lets the court invite proposers and accept their work by that record.
- **C3, the seed agent.** Only now does an agent arrive: a mixture over programs in a tiny seed language, conditioning within episodes, judged by a sealed judge no party can edit on held-out seeds of worlds it never saw while it was built [CHARTER §8].
- **Beyond.** Language as action — the agent extends its own library and adopts the extension if it dominates; adoption by sequential expected utility, with no human in the loop; the agent writing its own briefs, my role reduced to wishes, vetoes and a budget.

Each layer is a pre-registered experiment: its criteria, its null, its attack list and its maximum duration are committed before the window opens, and a window that fails is not patched but followed by a new one with the wealth carried [CHARTER §6; A4.1; A5]. Chapter 8 reports them as the sequential experiments they are.

## 1.6 What the programme claims, and what would show it wrong

Four claims, each with a number that can come out wrong; chapter 8 carries the numbers and this section states the claims.

**A court whose cost in human attention is measured and tends to zero.** Decisions a handful a week; repairs to zero; the liveness process over 20 within each layer's window. In C1b's window the operator's acts were a push, a key declaration, two revocations and a promotion — every one an irreversible act of the kind reserved to him — and no repair, on the log or off it [seqs 197, 201, 216, 217, 337; `status.py --subject C1b … --acts transcripts/evidence/acts-20261101.csv @6b800e14`].

**Forecasters elected by their record on a world with a price.** C2's test is whether the mixture beats the base rate in log-loss, prequentially, under rules fixed before the window opened. On the log as it stands, two proposers already score worse than the base rate on a stream of their own resolved forecasts — the builder on the freshness stream, at a mean loss of 0.629 against the base rate's 0.394 over twelve events, and counsel on its one resolved assize forecast — while the reviewer scores better than the base rate on all four streams it has entered [`jack score @6ebea1a`; `data/counsel-forecasts.md`]. That is the election working before the election exists; C2 exists to establish it in advance rather than in hindsight.

**An agent whose improvement is adjudicated, not asserted.** When the seed agent changes itself, the change is a candidate scored by the sealed judge on fresh seeds, with log-loss recorded and compute measured by the kernel rather than reported by the candidate; adoption is arithmetic on the ledger. Profitability is a discounted goal, not a short-term one. This claim is still a forecast.

**The regress of justification stopped everywhere without an authority** (chapter 6). The residue at each stop is written down.

And the ways the programme would be shown wrong were written before any window opened [CHARTER §12]. If recognition, change and adjudication cannot be held in a kernel small enough to read, the minimal-law thesis fails. If a liveness window fails against the predecessor's baseline, level-triggered writs do not buy liveness here. If repairs fall only because acts were re-typed as decisions, Goodhart has won and the typing-by-key guard did not hold. And if the core repeats the predecessor's growth of procedure — more than five entries about the court for every entry about the world in any fourteen-day window — it stops and reports. C1a's window ran at 127 : 32 and C1b's at 67 : 82 [`status.py` @6b800e14, A3.4 lines]; the court had a litigant.

## 1.7 How to read the book

A statistician will want chapter 4 first; the tests are the part of the design that is a theorem. A reader from AI safety will want chapters 2 and 6: what the impossibility results force, and where the trust stops. An institutional economist will want chapters 3 and 7, and the acts tables of chapter 8, which are the price of a constitution measured in one person's hours. Whoever reads it, chapter 11 should be read second: it is the referee's case, and the book is written so that the referee can be answered from the record rather than argued with.

Two conventions hold throughout. Every number carries a tag saying where on the record it came from and how it was recomputed, and a reader with a clone of `renavondata/jack` can repeat each one. And every chapter ends with what would show it wrong, because a book about pre-registered falsifiers that did not pre-register its own would be the kind of court it argues against.

## 1.8 What would show this chapter wrong

The question wrongly posed: if an agent that is allowed to change itself turns out not to need a fixed evaluator — if, say, the seed language of C3 is restricted enough that its properties are decidable and self-evaluation is sound — then §1.1's necessities are weaker than stated for that agent, though not for the language it will extend. The book's bet is that extension is the point.

The economy claim wrong: if the design could have been built and run at this price before cheap general policies existed, "only the economy is new" is false and something else is. The lineage chapter is where that would show, as a predecessor that reached a litigant.

The object mis-specified: the design is for one operator, a world that charges, and an unreliable policy. A reader who wants it for a team, a benchmark, or a verified policy should expect different necessities, and chapter 10 says which survive.
