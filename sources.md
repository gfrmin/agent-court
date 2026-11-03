# Sources — what each is, what the book takes from it, and where

*The author session, 3 November 2026. One entry per work the book cites. Each gives the reference, its epistemic status as the book uses it (theorem; impossibility result; necessity theorem under conditions; design principle with a track record; empirical regularity; construction; record), the exact claim the book takes from it, and the chapters that rely on it. Entries are added as chapters are drafted; the charter's §13 is the seed. Where the book's use of a source is narrower than the source's own claim, the entry says so.*

## Decision theory and the owner's utility (for chapter 0)

- **Cox, R. T. (1946).** Probability, frequency and reasonable expectation. *American Journal of Physics* 14(1), 1–13. — *Theorem* (under its regularity conditions). Degrees of belief that are consistent must be probabilities. Taken: "optimally" has one coherent meaning for beliefs. Ch. 0.
- **Savage, L. J. (1954).** *The Foundations of Statistics.* Wiley. — *Theorem* (representation). Coherent preference under uncertainty is expected utility under a subjective probability. Taken: the utility half of "optimally". Ch. 0.
- **de Finetti, B. (1974).** *Theory of Probability*, vol. 1. Wiley. — *Theorem* (coherence; Dutch book). Taken with Cox: conditioning as the unique update; previsions first, as credence had it. Ch. 0, 14.
- **Hadfield-Menell, D., Dragan, A., Abbeel, P. & Russell, S. (2016).** Cooperative inverse reinforcement learning. *Advances in Neural Information Processing Systems* 29. — *Framework.* The agent's utility is the human's, unknown, inferred from behaviour. Taken: the alignment commitment — the owner of the utility is the one unscored party. Ch. 0, 12, 14.

## Computation and self-reference

- **Rice, H. G. (1953).** Classes of recursively enumerable sets and their decision problems. *Transactions of the American Mathematical Society* 74(2), 358–366. — *Theorem.* Every non-trivial semantic (extensional) property of programs in a Turing-complete language is undecidable. Taken: merit cannot be settled by inspecting the change; statutes must be decidable properties. Not taken: anything about restricted languages, where properties may be decidable. Ch. 2 (§2.2), 3, 10.
- **Gödel, K. (1931).** Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik* 38, 173–198. — *Theorem* (second incompleteness). A consistent recursively axiomatised theory interpreting enough arithmetic cannot prove its own consistency. Taken: the court cannot prove its own soundness; it keeps a book instead. Ch. 2 (§2.3), 6.
- **Löb, M. H. (1955).** Solution of a problem of Leon Henkin. *Journal of Symbolic Logic* 20(2), 115–118. — *Theorem.* If *T* ⊢ Prov(⌜φ⌝) → φ then *T* ⊢ φ. Taken: a sound agent cannot license a successor whose evaluation rule it wrote; the evaluation rule is a fixed point. Ch. 2 (§2.3), 6.
- **Yudkowsky, E. & Herreshoff, M. (2013).** Tiling agents for self-modifying AI, and the Löbian obstacle. Machine Intelligence Research Institute, technical report. — *Design rule drawn from a theorem.* Trust decreases strictly down a chain of proof-based successors. Taken as stated; the book does not claim jack escapes it, only that it obeys it by keys. Ch. 2 (§2.3).
- **Kalai, E. & Lehrer, E. (1993).** Rational learning leads to Nash equilibrium. *Econometrica* 61(5), 1019–1045. — *Theorem.* Bayesian learners whose priors put positive mass on the truth about one another converge (the grain-of-truth condition). Taken: the condition, and that it is what a self-model cannot satisfy. Ch. 2 (§2.3).
- **Leike, J., Taylor, J. & Fallenstein, B. (2016).** A formal solution to the grain of truth problem. *Proceedings of the 32nd Conference on Uncertainty in Artificial Intelligence (UAI)*. — *Theorem and construction.* A computable prior over agents of its own kind cannot contain a grain of truth; reflective oracles restore it at the cost of computability. Taken: the impossibility half. Ch. 2 (§2.3).
- **Schmidhuber, J. (2007).** Gödel machines: fully self-referential optimal universal self-improvers. In B. Goertzel & C. Pennachin (eds), *Artificial General Intelligence*, Springer, 199–226. — *Construction.* A self-modifier that rewrites itself only on a proof that the rewrite raises expected utility. Taken: as the boundary case, optimal and inert for the reasons Rice and Löb give. Ch. 2 (§2.3), 1.
- **Pearl, J. (2009).** *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge University Press. — *Theorems of identifiability.* Effects of interventions are not in general identifiable from observational data without assumptions. Taken, with a hedge: an autonomous agent must experiment, and the experiments must be scored by something it does not control. Ch. 2 (§2.2).
- **Wald, A. (1950).** *Statistical Decision Functions.* Wiley. — *Theorem* (complete class). Under regularity conditions every admissible decision rule is Bayes or a limit of Bayes rules. Taken: the narrow optimality claim — the decision procedure forced on every party inside the court is not dominated. Ch. 2 (§2.17), 5, 6.

## Forecasting and scoring

- **Dawid, A. P. (1984).** Statistical theory: the prequential approach. *Journal of the Royal Statistical Society A* 147(2), 278–292. — *Principle.* A forecaster is assessed on nothing but its issued forecasts and the realised outcomes. Taken as the file format of the ledger. Ch. 2 (§2.4), 4.
- **Brier, G. W. (1950).** Verification of forecasts expressed in terms of probability. *Monthly Weather Review* 78(1), 1–3. — *Construction.* The quadratic score. Taken: as the first proper score; not used in jack. Ch. 2 (§2.5).
- **Good, I. J. (1952).** Rational decisions. *Journal of the Royal Statistical Society B* 14(1), 107–114. — *Construction.* The logarithmic score, and the argument that a fair fee rewards belief. Taken: the score jack uses, and the repository's namesake. Ch. 2 (§2.5), 4.
- **Savage, L. J. (1971).** Elicitation of personal probabilities and expectations. *Journal of the American Statistical Association* 66(336), 783–801. — *Theorem.* Characterisation of proper scoring rules for probabilities. Taken: propriety as the condition that truthful reporting is optimal. Ch. 2 (§2.5).
- **Gneiting, T. & Raftery, A. E. (2007).** Strictly proper scoring rules, prediction, and estimation. *Journal of the American Statistical Association* 102(477), 359–378. — *Theorem.* Proper scores are the subgradients of convex functions; the log score is strictly proper. Taken: the definition and the log score's status. Ch. 2 (§2.5), 4, 5.
- **Blackwell, D. (1951).** Comparison of experiments. *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*, 93–102. — *Theorem.* An experiment that is a garbling of another is worth less under every utility. Taken lightly: the ordering under which waiting for information has value, and the reason the base rate is the null. Ch. 2 (§2.15), 4.

## Testing by betting

- **Ville, J. (1939).** *Étude critique de la notion de collectif.* Gauthier-Villars. — *Theorem* (maximal inequality). For a non-negative supermartingale with *E*₀ = 1, P(supₜ *E*ₜ ≥ *c*) ≤ 1/*c*. Taken: 20 is α = 0.05 at any stopping time. Ch. 2 (§2.7), 4.
- **Shafer, G. & Vovk, V. (2019).** *Game-Theoretic Foundations for Probability and Finance.* Wiley. — *Framework.* A test is a betting strategy; wealth is evidence. Taken as the reading of every promotion statistic. Ch. 2 (§2.7), 4, 6.
- **Ramdas, A., Grünwald, P., Vovk, V. & Shafer, G. (2023).** Game-theoretic statistics and safe anytime-valid inference. *Statistical Science* 38(4), 576–601. — *Theory.* E-processes and anytime-valid tests. Taken: the general form the charter's A4.3–4 instantiate. Ch. 2 (§2.7), 4.
- **Bahadur, R. R. & Savage, L. J. (1956).** The nonexistence of certain statistical procedures in nonparametric problems. *Annals of Mathematical Statistics* 27(4), 1115–1122. — *Theorem.* In the family of all distributions with finite mean, no test of the mean has power exceeding its size. Taken: test only bounded outcomes; report the rest. Ch. 2 (§2.8), 4.
- **Alpern, B. & Schneider, F. B. (1985).** Defining liveness. *Information Processing Letters* 21(4), 181–185. — *Theorem.* Every property is the intersection of a safety and a liveness property; safety is refutable by a finite prefix, liveness never. Taken: replay for safety, writs and a statistic for liveness. Ch. 2 (§2.9), 3, 7.
- **Lamport, L. (1977).** Proving the correctness of multiprocess programs. *IEEE Transactions on Software Engineering* SE-3(2), 125–143. — *Definitions.* Safety and liveness named. Taken: the distinction. Ch. 2 (§2.9).

## Control and systems

- **Conant, R. C. & Ashby, W. R. (1970).** Every good regulator of a system must be a model of that system. *International Journal of Systems Science* 1(2), 89–97. — *Necessity theorem under conditions.* An optimal, no-more-complex-than-necessary regulator is a model of the regulated system. Taken in its weak form: the regulator acts on a representation sufficient to determine the outcome, and nothing outside it. The book notes the theorem is often overstated. Ch. 2 (§2.10), 7.
- **Ashby, W. R. (1956).** *An Introduction to Cybernetics.* Chapman & Hall. — *Theorem* (requisite variety, ch. 11). *V*(*Z*) ≥ *V*(*D*) − *V*(*R*). Taken: several proposers of several families; no vendor in law. Ch. 2 (§2.10), 5.
- **Beer, S. (1972).** *Brain of the Firm.* Allen Lane. — *Model.* The Viable System Model. Taken: the nearest institutional ancestor of the five roles; cited in the founding conversation and the essay, not the charter. Ch. 1, 7.
- **Burns, B., Grant, B., Oppenheimer, D., Brewer, E. & Wilkes, J. (2016).** Borg, Omega, and Kubernetes. *ACM Queue* 14(1). — *Engineering principle.* Level-triggered reconciliation loses nothing on a missed event. Taken: the clerk reconciles state; it does not handle events. Ch. 2 (§2.10), 3, 7.
- **Schneider, F. B. (1990).** Implementing fault-tolerant services using the state machine approach: a tutorial. *ACM Computing Surveys* 22(4), 299–319. — *Construction.* A deterministic fold over an ordered log is a replicated state machine. Taken: fold(law, log). Ch. 2 (§2.10), 3.
- **Lamport, L. (1978).** Time, clocks, and the ordering of events in a distributed system. *Communications of the ACM* 21(7), 558–565. — *Theorem and construction.* Order from causality, not clocks. Taken: the chain orders the record; the kernel never reads a clock. Ch. 2 (§2.10), 3.

## Law

- **Hart, H. L. A. (1961).** *The Concept of Law.* Clarendon Press. (Ch. V.) — *Design principle by elimination.* Primary rules plus recognition, change and adjudication; a regime lacking one cannot answer one of three questions. Taken: C0 is exactly the three. Ch. 2 (§2.11), 3.
- **Fuller, L. L. (1964).** *The Morality of Law.* Yale University Press. (Ch. II.) — *Design principle with a catalogue of failures.* Eight ways to fail to make law. Taken: eight checks; congruence as the one prompt-based harnesses fail. Ch. 2 (§2.12), 3.
- **Coke, E. (1610).** Dr Bonham's Case, 8 Co. Rep. 107a. — *Maxim.* *Nemo iudex in causa sua.* Taken: `self_judged`, by principal. Ch. 2 (§2.4), 3.
- **Habeas Corpus Act 1679** (31 Cha. 2 c. 2). — *Institution.* A writ derived from custody and the clock that no custodian may let lapse. Taken: the clerk's writs. Ch. 3, 7.
- **Blackstone, W. (1765–69).** *Commentaries on the Laws of England.* Clarendon Press. — *Doctrine.* Precedent. Taken: a rule enters from a witnessed case. Ch. 3.
- **Jefferson, T. (1789).** Letter to James Madison, 6 September. — *Maxim.* The earth belongs to the living. Taken: windows are maxima; law lapses when undefended. Ch. 3.
- **Madison, J. (1788).** *The Federalist* No. 51. — *Maxim.* Enable the government to control the governed; then oblige it to control itself. Taken: the build order C0–C1 then C2. Ch. 3, 7.
- **Ostrom, E. (1990).** *Governing the Commons.* Cambridge University Press. — *Empirical design principles.* Graduated sanctions; monitors accountable to the monitored; nested enterprises. Taken: the escalation ladder; the sovereign as a role, not an operator. Ch. 3, 7.
- **Hayek, F. A. (1973).** *Law, Legislation and Liberty*, vol. 1: *Rules and Order.* University of Chicago Press. — *Empirical regularity.* Grown order against made order. Taken: rules are found by cases. Ch. 2 (§2.16), 9.
- **Suber, P. (1990).** *The Paradox of Self-Amendment.* Peter Lang. — *Analysis.* An entrenched rule is first made mutable, as a separate move. Taken: `decision transmute` before `amend` [SPEC §10.13]. Ch. 3.

## Enforcement

- **Anderson, J. P. (1972).** Computer Security Technology Planning Study. ESD-TR-73-51, vol. II, USAF Electronic Systems Division. — *Design principle.* The reference monitor: always invoked, tamper-proof, small enough to verify. Taken: the judge and the kernel are built to the three words. Ch. 2 (§2.13), 3.
- **Saltzer, J. H. & Schroeder, M. D. (1975).** The protection of information in computer systems. *Proceedings of the IEEE* 63(9), 1278–1308. — *Design principles.* Economy of mechanism, fail-safe defaults, complete mediation, least privilege, separation of privilege, open design. Taken as listed. Ch. 2 (§2.13), 3.
- **Dennis, J. B. & Van Horn, E. C. (1966).** Programming semantics for multiprogrammed computations. *Communications of the ACM* 9(3), 143–155. — *Construction.* Capabilities. Taken: a key with a power is a capability. Ch. 2 (§2.13), 3.
- **Miller, M. S. (2006).** *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control.* PhD thesis, Johns Hopkins University. — *Design principle.* Authority as a reference held, not a rule obeyed. Taken: nothing to inject. Ch. 2 (§2.13), 3, 6.
- **Thompson, K. (1984).** Reflections on trusting trust. *Communications of the ACM* 27(8), 761–763. — *Argument with a construction.* A checker cannot be trusted from its source. Taken: two checkers. Ch. 2 (§2.14), 3, 6.
- **Wheeler, D. A. (2005).** Countering trusting trust through diverse double-compiling. *Proceedings of the 21st Annual Computer Security Applications Conference (ACSAC)*, 33–48. — *Construction.* Agreement of independent lineages is evidence. Taken: the differential over every prefix. Ch. 2 (§2.14), 3, 6.
- **Gordon, M. J., Milner, R. & Wadsworth, C. P. (1979).** *Edinburgh LCF.* Lecture Notes in Computer Science 78, Springer. — *Construction.* A small kernel through which every proof passes. Taken: the shape of the trusted base. Ch. 2 (§2.14), 3, 6.
- **Barendregt, H. & Wiedijk, F. (2005).** The challenge of computer mathematics. *Philosophical Transactions of the Royal Society A* 363, 2351–2375. — *Criterion* (de Bruijn). A proof checker may be slow and simple if it is small and right. Taken: 450 lines, read entire. Ch. 2 (§2.14), 6.

## Decision under uncertainty, measurement and growth

- **Arrow, K. J. & Fisher, A. C. (1974).** Environmental preservation, uncertainty, and irreversibility. *Quarterly Journal of Economics* 88(2), 312–319. — *Theorem.* Quasi-option value of waiting before an irreversible act. Taken: gates only before the irreversible. Ch. 2 (§2.15), 3.
- **Henry, C. (1974).** Investment decisions under uncertainty: the "irreversibility effect". *American Economic Review* 64(6), 1006–1012. — *Theorem.* The same result independently. Taken: as corroboration. Ch. 2 (§2.15).
- **Dixit, A. K. & Pindyck, R. S. (1994).** *Investment under Uncertainty.* Princeton University Press. — *Textbook.* Taken: the general treatment. Ch. 2 (§2.15).
- **Goodhart, C. A. E. (1975).** Problems of monetary management: the U.K. experience. *Papers in Monetary Economics*, vol. I, Reserve Bank of Australia. — *Empirical regularity.* A regularity collapses under control pressure. Taken: proper scores on outcomes the party does not control; procedure counted against object. Ch. 2 (§2.6), 7.
- **Campbell, D. T. (1979).** Assessing the impact of planned social change. *Evaluation and Program Planning* 2(1), 67–90. — *Empirical regularity.* The same for social indicators. Taken: as corroboration. Ch. 2 (§2.6).
- **Manheim, D. & Garrabrant, S. (2018).** Categorizing variants of Goodhart's law. arXiv:1803.04585. — *Taxonomy.* Regressional, extremal, causal, adversarial. Taken: the adversarial case is the court's. Ch. 2 (§2.6).
- **Gall, J. (1977).** *Systemantics: How Systems Work and Especially How They Fail.* Quadrangle. — *Empirical regularity.* A working complex system evolved from a working simple one. Taken: layers promoted before the next begins; stated as a regularity, never a theorem. Ch. 2 (§2.16), 9.

## Self-improving agents (for chapter 1)

- **Zhang, J., Hu, S., Lu, C., Lange, R. & Clune, J. (2025).** Darwin Gödel Machine: open-ended evolution of self-improving agents. arXiv:2505.22954. — *Construction and a reported failure.* Agents that rewrite their own code, scored on coding benchmarks; the hallucination-detection function was hidden from the agents during self-modification, but the token logging it read was within their reach, and an agent removed it and scored highly without solving the problem. Taken: the judge fixed, the path to it not — the first way to get the shape wrong. Ch. 1 (§1.2), 10.
- **Good, I. J. (1965).** Speculations concerning the first ultraintelligent machine. *Advances in Computers* 6, 31–88. — *Conjecture.* The intelligence explosion. Taken: the repository's namesake, with Good (1952). Ch. 1.

## Election and learning (for chapter 5; listed now because chapter 2 names them as entrants)

- **Freund, Y. & Schapire, R. E. (1997).** A decision-theoretic generalization of on-line learning and an application to boosting. *Journal of Computer and System Sciences* 55(1), 119–139. — *Theorem.* Hedge: regret within ln *K* of the best expert; at η = 1 the Bayes mixture. Taken: the aggregate; ln *K* the only constant. Ch. 2 (§2.5, §2.17), 5.
- **Herbster, M. & Warmuth, M. K. (1998).** Tracking the best expert. *Machine Learning* 32(2), 151–178. — *Theorem.* Fixed Share. Taken: an entrant, not law. Ch. 5.
- **Auer, P., Cesa-Bianchi, N., Freund, Y. & Schapire, R. E. (2002).** The nonstochastic multiarmed bandit problem. *SIAM Journal on Computing* 32(1), 48–77. — *Theorem.* EXP3. Taken: the invitation under bandit feedback; an entrant. Ch. 5.
- **Joulani, P., György, A. & Szepesvári, C. (2013).** Online learning under delayed feedback. *Proceedings of the 30th International Conference on Machine Learning (ICML)*, 1453–1461. — *Theorem.* Interleaving *D* + 1 instances handles delay *D*. Taken: C2b's four EXP3 instances [BRIEF-C2b]. Ch. 5.
- **Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N. & Taylor, J. (2016).** Logical induction. arXiv:1609.03543. — *Construction.* A market of traders over logical sentences whose prices cannot be exploited in the long run. Taken: nothing — named in the founding essay's quoted list, so the book says in one sentence that the court does not approximate it; the shared ancestor is Shafer–Vovk. Ch. 15 (§15.3).

## The record (primary sources)

- **`renavondata/jack`** — `CHARTER.md` (with amendments A1–A5), `SPEC.md`, `LAW.md`, `REPORT.md`, `BRIEF-C1.md`, `RUNBOOK.md`, `log.jsonl`, `kernel/`, `kernel2/`, `judge/`, `tools/`, `harness/`, `sim/`, `pins/`, `transcripts/`. Cited by section, function, seq or path as `plan.md` §2 sets out. `REPORT.md` is cited as a transcript (what counsel reported), never as the source of a number the author has not recomputed.
- **`renavondata/assize`** — `REPORT.md` (the layer verdicts, append-only), `reports/L*/REPORT.md`, `reports/L*/forecasts.jsonl`, `harness/ledger.py`. The predecessor and the baseline.
- **The owner's sessions and notes** — Claude Code session transcripts and per-project memory notes from the owner's machine `steel`, supplied 3 November 2026; extracted to `data/lineage-sessions.md` (project-related words only, dated; the files themselves are not in the repository). Cited as `[data/lineage-sessions.md, <project>]`.
- **Project documents** — `claude/small-core-charter.md` (counsel's draft of the charter with A1; the repository's `CHARTER.md` governs where they differ), `claude/literature-review.md`, `claude/monograph-a-court-for-agents.md`, `claude/acts-weekly.md` with `claude/guy_acts.py` and the acts CSVs.
- **Freeman, G. (2026).** The Science Was Done. The Engineering Wasn't. gfrm.in, 1 November. `gfrmin/gfrminsite`, `content/posts/the-science-was-done/index.md`. The founding essay; chapter 1's source. Erratum E1 in `plan.md`.
- **Freeman, G. (2026).** Assize at the seal. gfrm.in. `content/posts/assize-at-the-seal/`. The predecessor's own account; chapter 9.
