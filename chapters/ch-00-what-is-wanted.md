# 0. What is wanted

*Draft 2, the author session, 3 November 2026 — rewritten on the construction (`plan.md` §3, D20–D25). Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## The figure: a will

A will is an instruction to act for someone after they can no longer act for themselves. It is written in a language the testator understands and executed by people he will never meet, in circumstances he could not foresee, against a world that does not care what he wanted. Every part of what this book builds is already in it. The executor acts *for* the testator, not for himself: his duty is the testator's utility, not his own reading of it. The instruction is in words, and words must become acts: an estate is not divided by a sentence but by a court that can compel the division. The executor is imperfect and may be dishonest, so the law prices his acts — accounts, audits, a bond — rather than trusting them. And the testator does not get to come back and check. The will must work without him. That is the question: how to build something that acts for us, from what we say, through helpers we cannot fully trust, in a world that charges, after we have stopped watching.

## 0.1 The question, in four parts

We want a system that acts optimally *for us*; that can take what we say and make it binding; that acts through helpers whose suggestions are good but imperfect; and that does so in a world where being wrong costs money, after we have stopped watching. Each part has a precise meaning, and the precise meanings are what the rest of the book builds from.

**For us.** "Optimally" has one coherent meaning once we admit uncertainty: maximise expected utility under beliefs that are probabilities and that change only by conditioning on evidence. That is not a preference; it is a theorem three times over — Cox for the probabilities, Savage for the utilities, Wald for the decisions (a rule that is not Bayes is dominated by one that is). Everything the system does will be a bet, and a bet is only coherent under those three. "For us" is the part the theorems do not settle: *whose* utility. The answer this book takes from its predecessors is the one credence wrote first — the agent's utility is the owner's, unknown, inferred from behaviour, and the ground truth arrives from outside the agent (Hadfield-Menell et al. 2016, cooperative inverse reinforcement learning; `credence/CONSTITUTION.md` §2.5). The owner's wishes are therefore the standard and cannot be graded against themselves. One party in the system will be unscored, and it is the one whose utility is being served. The horizon is discounted: profit is a term in the utility, and so is time, and nothing is optimised for the next quarter that would not be optimised for the next decade at the same rate.

**From what we say.** We will not write the system's law in a formal language; we will say what we want, in English, and something must turn that into a rule that refuses. A rule that does not refuse is a suggestion, and a system built from suggestions is governed by whoever reads them. So between the wish and the refusal there is a compiler — not a program, as it turns out, but a procedure with people and sessions in it — and the measure of the system's law is how much of it reached the refusal end (chapter 8).

**Through imperfect helpers.** The policy that will do the work is a large language model: general, cheap per token, and unreliable in ways nobody can list in advance. Its suggestions are good — often better than ours — and sometimes wrong in ways that look right. Nothing in what follows depends on which model, and the law will be written so that it cannot (chapter 7). What it depends on is that the helpers' suggestions are *claims*, and claims can be scored.

**In a world that charges.** Outcomes come from processes that read nothing the system writes: a race result, a dataset's modification time, a test run on a commit, a price paid. A world that charges is what makes a score mean something; a system built against a world that does not charge is a research project, and chapter 14 is a catalogue of them.

**After we have stopped watching.** The operator is one person. His attention is the scarcest resource in the system, and the design is for spending it on wishes, vetoes, a budget and the acts that cannot be undone, and on nothing else. Every act of his will be an entry, typed as a *decision* or a *repair*, and repairs are the quantity the whole construction is built to drive to zero [CHARTER §7]. The predecessor measured the alternative: in four days of October, 88 decisions and 121 repairs — five repairs for every merge — and twenty of twenty-four merges about the court itself [CHARTER §1].

## 0.2 The thesis, stated before it is built

The book's claim is that these four parts, taken seriously, leave almost no choice about what the system is. Three results carry most of it.

An intelligence that adapts must be a **loop**: it cannot regulate what it does not observe (Ashby), and it must contain a model of what it regulates (Conant and Ashby). A loop that modifies itself must have one point that does not move — a **lock**: it cannot evaluate its own changes by inspection (Rice) and cannot soundly trust an evaluator it wrote (Löb), so the fixed point lies outside the modifier's reach. And the fixed point must be a **score**, not a judgement: the only thing that can be held rigid at every level without decaying is a proper score on outcomes the loop does not control (Dawid, Good, Goodhart). Loop, lock, score. The chapters that follow build each, in the only order they can be built, and show at each step that the thing built is the smallest thing the results allow.

The claim of novelty is narrow and should be read narrowly. None of the results is new; the oldest is a 1610 judgement and the newest is from 2023. What is new is only the economy: for the first time there is a cheap, general, unreliable policy worth governing, and governing it is a composition problem. The predecessors kept becoming research because the science was done and the engineering was not.

## 0.3 How the construction proceeds

Each chapter starts from what the previous one built, names the problem it cannot solve, states the result that leaves no choice, and builds the smallest thing that discharges it — in code where it is code, cited to the line; in a clause where it is law, cited to the clause; and at a numbered entry of the record where it is an act. Each chapter ends with what it leaves open, which is the next chapter's problem, and with what would show it wrong.

1. *The loop* — adaptation requires a closed loop with a model inside it.
2. *Every suggestion is a bet* — merit cannot be inspected, so a helper's suggestion is a forecast under a proper score.
3. *The record* — a score needs a record nobody can rewrite and outcomes nobody controls.
4. *The smallest law* — who may write to the record, what counts, and who decides: three rules in 450 lines.
5. *The clerk* — obligations rot unless something derives them from state and the clock.
6. *Testing by betting* — when has it worked, for an operator who looks whenever he likes.
7. *The election* — which helper, chosen by its record.
8. *Language into law* — from a wish to a refusal, and the measure of how much compiled.
9. *The law changes under itself* — amendment, the irreversible, lapse.
10. *The lock* — the system changes its own programs, under a judge it cannot reach.
11. *The loops and the bootstrap* — why in layers, why this order, why the same law at every level; what bootstraps is authority.
12. *The ground* — where every chain of justification stops.
13. *The evidence* — the windows, as pre-registered experiments, every number recomputed.
14. *Lineage* — the same loop run open, seven times, measured.
15. *How it could be wrong.*

Three conventions hold throughout. Every number carries a tag saying where on the record it came from and how it was recomputed, and a reader with a clone of `renavondata/jack` can repeat it. Each chapter opens with a figure from ordinary human life — a will, a child, a vow, a court, a courier, a canon — because the loop, the lock and the score are things everyone has run; the figures illustrate and never evidence, and the evidence is always the theorem and the log. And every chapter ends with what would show it wrong, because a book about pre-registered falsifiers that did not pre-register its own would be the kind of system it argues against.

## 0.4 What this chapter leaves open

Everything. We have a question with four parts and a thesis in three words. We do not yet have a reason to believe the system must be a loop at all, rather than a plan executed once. That is chapter 1.

## 0.5 What would show this chapter wrong

The question mis-posed. If "optimally for us" has a coherent meaning other than expected utility under an owner's inferred utility, the construction starts somewhere else; the book's bet is that the three theorems leave none. If the helpers' suggestions can be verified rather than scored — if a policy arrives whose outputs are checkable by inspection — chapter 2's necessity weakens and much of the court is unnecessary; the book's bet is that any policy worth governing is one whose outputs are claims. And if the economy is not what is new — if the composition could have been built and run at this price before cheap general policies existed — then something else is new, and chapter 14 is where it would show, as a predecessor that reached a litigant.
