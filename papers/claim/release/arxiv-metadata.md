# arXiv submission metadata

**Title:** Law Before the Agent: Testing the Institution That Judges Self-Modifying AI

**Authors:** Guy Freeman

**Abstract** (1554 characters; the limit is 1,920). Paste the ASCII form, which uses TeX accents:

```
Systems that rewrite their own code are now practical. Results of Rice, L\"ob and Goodhart limit what inspection, self-proof and measures within an agent's reach can establish about such systems, yet in the leading examples the evaluator that judges them is held fixed and trusted as infrastructure. We propose that the institution which judges a self-modifying agent be built before the agent, imposed first on the model sessions that build it, and granted powers only by anytime-valid tests on its own record. Its law is a fold over a signed, append-only log; claims of merit count only as forecasts under the logarithmic score; and a layer is promoted only when its sequential tests pass, of liveness, measured by the principal's repairs, and, once there are forecasts to aggregate, of predictive value. We state the guarantees in six propositions, whose statistical core is machine-checked in Lean, show by example and simulation that the natural per-event test of value loses its level when outcomes resolve together, and prove that a block form keeps it. Applied retrospectively to the public record of a reference implementation, the block-form test finds an advantage over a base rate pooled across datasets and no evidence of one over a base rate kept per dataset, so the institution's own book shows that its first evidence of value rested on a weak baseline. The paper offers a design and an audit, not an evaluation: the implementation has not yet tied its powers to these tests, and no self-modifying agent has yet been built under the design.
```

**Comments:** 25 pages, 1 figure, 3 tables. Lean 4 proofs and the analysis scripts are ancillary files.

**Primary category:** cs.AI. Possible cross-lists: cs.LO (the Lean proofs), stat.ME (the sequential tests).

**Licence:** your choice; CC BY 4.0 lets anyone reuse the text with credit.

**Files:** upload `law-before-the-agent-arxiv.tar.gz`. It holds `paper.tex`, `figure.tex` and `anc/` (the Lean project, `sim_filtration.py`, `block_on_log.py` and `04-selfcheck.md`). arXiv builds it with pdflatex and needs no BibTeX run.

**Before submitting:**
- A first submission to cs.AI needs an endorsement from someone who has published there.
