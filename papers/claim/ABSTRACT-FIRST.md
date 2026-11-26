# What the paper is about (fixed before the rest is revised)

*26 November 2026, claim session. Guy asked that the abstract be ready first, so that everything else serves it. This file fixes the paper's one idea, its four-sentence form, its contributions and its abstract. The draft is then aligned to them.*

## Advice applied

- **One idea.** A paper should have one clear, sharp idea, its "ping". State it outright ("The main idea of this paper is …"), and write the list of contributions first, because that list drives the paper (Peyton Jones, *How to write a great research paper*).
- **Four sentences.** The abstract can be four sentences long (Kent Beck, quoted by Peyton Jones):
  1. the problem;
  2. why it is interesting;
  3. what the solution achieves;
  4. what follows from it.
- **A single message.** Papers that push several contributions at once convince less on each (Mensh & Kording, "Ten simple rules for structuring papers", *PLoS Comput Biol* 13(9):e1005619, 2017).
- **Context, content, conclusion.** The abstract holds all three: the gap, what fills it, and how it moves the field (Mensh & Kording).
- **When to write the abstract.** Both Peyton Jones and Whitesides ("Writing a Paper", *Adv. Mater.* 16:1375, 2004) write the *final* abstract last, and work from an outline. So we fix the idea and the contributions now, and treat this abstract as the target the text must reach. Its wording is checked again at the end.

## The ping

**A self-modifying agent can be trusted only as far as an institution it cannot reach can test it. That institution must be built first, tested first on its builders, and given powers only by valid sequential tests on its own record. Those tests must themselves be valid: on a public record, the natural version reports evidence that is not there.**

## Four sentences

1. An agent that rewrites its own code must be judged by something it cannot rewrite, and today that judge is trusted rather than tested.
2. Rice, Löb and Goodhart show why inspection, self-proof and measures within the agent's reach each fall short.
3. We build the judging institution first, impose it first on its builders, and grant it powers only by anytime-valid tests on its own record. We prove what this guarantees, and correct the natural test of value, which is not valid.
4. On a public record, the valid test shows that the institution's own first evidence of value came from a weak baseline. That is the kind of failure a judge of self-modification must make visible.

## Contributions (these drive the paper)

1. **The design, and why each ingredient (§§2–3).** A conditional analysis from Rice, Löb, Goodhart, Ville, Hart, Fuller and others to a log, a lock and a score.
2. **Its guarantees (§4).** Six propositions, including a block-valid test of value, with an example, a simulation and a proof that the per-event form is not valid. The statistical core is to be machine-checked in Lean.
3. **The order of construction (§5).** Law before the agent, imposed first on its builders; what is bootstrapped is authority.
4. **The evidence (§7).** The valid test, applied to the public record, finds value only against a pooled base rate, and none against a base rate per dataset.

## Abstract (target; about 1,600 characters, against arXiv's limit of 1,920)

Systems that rewrite their own code are now practical, and the evaluator that judges them is usually trusted rather than tested. Three results motivate the design. Whether a change to an arbitrary program is an improvement cannot be decided by inspection (Rice). An agent cannot, by proofs in its own theory, trust a successor that reasons in that theory (Löb). A measure within the agent's reach decays once it becomes a target (Goodhart).

We propose that the institution which judges a self-modifying agent be built before the agent, imposed first on the model sessions that build it, and granted powers only by anytime-valid tests on its own record. Its law is a fold over a signed, append-only log. Every claim of merit, the principal's included, is a forecast under the logarithmic score, resolved by another party. Each layer is promoted only when sequential tests of predictive value and of liveness, measured by the principal's repairs, both pass.

Six propositions state what this guarantees, and their statistical core is machine-checked in Lean. We show by example, simulation and proof that the natural per-event test of value loses its level when outcomes resolve together, and we give a block form that keeps it. Applied retrospectively to the public record of a reference implementation, the valid test finds an advantage over a base rate pooled across datasets, and no evidence of one over a base rate kept per dataset. The institution's own book thus shows that its first evidence of value rested on a weak baseline. Making such failures visible on the record is what a judge of self-modification must do.

No self-modifying agent has yet been built under this design.
