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

1. An agent that rewrites its own code must be judged by something it cannot rewrite, and in the leading systems that judge is held fixed and trusted as infrastructure.
2. Rice, Löb and Goodhart show why inspection, self-proof and measures within the agent's reach each fall short.
3. We build the judging institution first, impose it first on its builders, and grant it powers only by anytime-valid tests on its own record. We prove what this guarantees, and correct the natural test of value, which is not valid.
4. On a public record, the valid test shows that the institution's own first evidence of value came from a weak baseline. That is the kind of failure a judge of self-modification must make visible.

## Contributions (these drive the paper; draft 12 holds every section to them)

1. **The design (§§3–5).** Built before the agent, imposed first on its builders; law as a fold over a signed log; claims of merit count only as forecasts under the log score; layers promoted only by sequential tests of liveness (the principal's repairs) and of predictive value. §3 gives the results behind each ingredient as design arguments.
2. **Its guarantees (§4).** Six propositions, including a block-valid test of value, with an example, a simulation and a proof that the per-event form is not valid when outcomes resolve together; statistical core in Lean.
3. **The evidence (§6).** The valid test, applied retrospectively to the public record, finds value only against a pooled base rate, and none against a base rate per dataset.

What draft 12 cut, because the abstract does not claim it: the broader "appendix of necessities" rows (Bahadur–Savage, Crawford–Ostrom, Waismann, Thompson–Wheeler, Skalse), the regress catalogue, the minimality section and the diversity-of-checkers essay (one sentence of it survives in §4.4). The title lost "Loop, Lock and Score", which the abstract does not use; §2 keeps lock and score by name and loop as the motive for the fold.

## Abstract (in Peyton Jones's four-sentence form: problem, why it matters, the idea, what follows; 1413 characters)

Systems that rewrite their own code are now practical, and in the leading examples the evaluator that judges them is held fixed and trusted as infrastructure, although results of Rice, Löb and Goodhart limit what inspection, self-proof and measures within the agent's reach can establish. We propose that the institution which judges a self-modifying agent be built before the agent, imposed first on the model sessions that build it, and granted powers only by anytime-valid tests on its own record: its law is a fold over a signed, append-only log, claims of merit count only as forecasts under the logarithmic score, and each layer is promoted only when sequential tests pass: of liveness, measured by the principal's repairs, and, once there are forecasts to aggregate, of predictive value. We state the guarantees in six propositions, whose statistical core is machine-checked in Lean, show by example and simulation that the natural per-event test of value loses its level when outcomes resolve together, and prove that a block form keeps it. Applied retrospectively to the public record of a reference implementation, the valid test finds an advantage over a base rate pooled across datasets and no evidence of one over a base rate kept per dataset, so the institution's own book shows that its first evidence of value rested on a weak baseline; no self-modifying agent has yet been built under the design.