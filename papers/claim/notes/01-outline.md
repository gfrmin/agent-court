# Claim note — outline v2 (step 1)

*Claim session, 25 November 2026, on Guy's direction that the note be about the theory: why these ingredients, and why the vision is right, not how the build went. It replaces v1. Repository facts are checked against `renavondata/jack` `origin/main` `e580b64`, with the log to seq 7809.*

**Working title.** *Law before the agent: record, wager and court for a self-modifying machine.*

**Form.** A research paper, not a position paper. arXiv's CS section now turns away position papers that have not been peer reviewed. Two things keep this note out of that class:
- the argument is carried by stated propositions with short proofs;
- it describes a running reference implementation, cited only where it shows that a mechanism is buildable.

**Thesis, in one sentence.** Self-modification is safe to permit exactly where the modifier cannot reach the court that scores it. That court must therefore be built first, be tested on its own builders, and keep a book on itself rather than a proof of itself.

## Sections (about 10 pages)

**1. The problem: principal and agent, when the agent can rewrite itself (1½ pp).** The principal cannot inspect the merit of a change. Rice's theorem leaves only outcomes to judge by. The agent cannot certify its successor: the Löbian obstacle and the grain-of-truth problem put the evaluator outside its reach. The principal's attention is scarce and is itself a cost. Goodhart's law and Bahadur–Savage restrict what may be scored. DGM's objective hacking is the witness: its evaluator was fixed, but the path to it was not. The design question is therefore institutional, not algorithmic.

**2. The ingredients, each derived from what forces it (4 pp; the core).** This section is a compressed form of the book's Appendix A, "The necessities" (gfrmin/agent-court `007a007`). It takes the appendix's rows in its own groups: evaluation, testing, control, law, enforcement, irreversibility and growth, and meaning and measurement. Each row keeps four parts:
- the result, stated with its hypotheses;
- what it forces;
- the mechanism that discharges it;
- what would show it misapplied.

The section uses the appendix's word "necessary": removing the mechanism leaves a stated result unmet. Following §A.17, minimality is claimed, while sufficiency and optimality are not; sufficiency is left to the record. The propositions below are where the forcing argument becomes mathematics.
- **The record.** The law is a fold over a signed, append-only log, as in Conant–Ashby, Lamport and Schneider. Keys are capabilities, after Dennis and Van Horn. *Proposition 1 (prospectivity):* the validity of entry *i* depends only on entries 0..*i*; so no later act, amendment included, can change an earlier verdict (SPEC.md §1, §7).
- **The wager.** Every claim is a forecast under log-loss, following Dawid and Gneiting–Raftery, and is resolved by a different principal. *Proposition 2:* reporting one's belief truthfully is each party's unique optimum, and no party can resolve its own forecast. The second clause is the kernel's `self_judged` rule (SPEC.md 228–234).
- **The test.** A layer is promoted by an e-process, which is Ville's inequality and Shafer–Vovk betting. *Proposition 3:* value is the likelihood ratio of a Bayes mixture of all parties against the base rate, so it is a test martingale under a calibrated base rate, and its regret is at most ln *K*. *Proposition 4:* liveness is a bet with a Laplace plug-in stake, and the wealth carried across failed windows is a test supermartingale over the institution's whole life, so a retry costs no α (CHARTER A4.1–A4.3). Contrast SGM, SEA and PACE, which spend α per edit or bound each decision on its own.
- **The court.** The sovereign is the one unscored party, because he owns the utility. His reserved acts are exactly the irreversible ones (Arrow–Fisher). Every other act of his is typed as a decision or a repair, and his repairs are what liveness drives towards zero. The judge has two kernels from different model families (Thompson; Wheeler). *Proposition 5:* the evaluator changes only by a replay that reproduces every earlier verdict except lines marked in advance, so it can never re-judge the past silently (SPEC.md §10, item 15).
- **The loops.** Seven loops (record, reconciliation, wager, election, layer, review, sovereign) each turn a one-off act of trust into a measured process. Closed, level-triggered loops beat open, event-triggered ones (the Borg paper; habeas corpus).
- **Where the regress stops.** No regress ends in an authority. Each ends instead in one of these:
  - size and diversity;
  - a theorem or an election;
  - the world;
  - the owner of the utility;
  - a book that can go bankrupt. This is a priced reading of logical induction.

**3. Why law comes before the agent (1½ pp).** This section draws on the book's chapter 11, "the order is forced, not chosen".
- Gall's law and *Federalist* 51 give the order of layers: C0 record, C1 ledger and clerk, C2 election, C3 the agent.
- The self-similar loop: the builders are the law's first subjects, and "nothing is imposed on the agent that was not first imposed on us" (CHARTER.md 298–300).
- Language as action comes after C3.
- The order is forced, because an agent introduced before its court is the DGM case.

**4. Related work (1½ pp).** SGM, SEA, PACE; DGM, Hyperagents; ASG-SI, SFA-Bench/AutoLab, Regimes; Institutional AI, Governable Individuals; Trusting Trust Revisited. Each is cited for what it does, with where the argument here departs.

**5. The reference implementation and its status (½ p).** The record exists and is public: genesis was 2026-10-14 and the charter is hashed into seq 0. C1a was promoted at seq 188 and C1b at seq 337. C2 is under way, and its first two windows failed and were recorded as precedent. No agent exists yet. Facts only, each with its seq and timestamp.

**6. Open questions (½–1 p), all theoretical.**
- **The choice of null.** A base-rate null is easy to beat, so the value test certifies calibration more than skill (the audit on the record).
- **Whether three secondary rules suffice.** No primary rule has yet been needed (A2.1).
- **Election and market.** A mixture over a fixed roster, against a market of traders.
- **One sovereign.**

**Claims of priority**, unchanged from v1 in substance, but argued as theory:
1. The law is built before the agent and tested first on its builders.
2. The institution is promoted by one continued e-process that tests liveness as well as value, with the principal's repairs as the measured quantity.
3. The judge cannot be changed retroactively: the law is a fold over prior entries, the validity predicate is replicated in diverse implementations, and the evaluator changes only by replay.

Signed logs, frozen evaluators, human ratification and anytime-valid acceptance tests are conceded to prior work.

**The book's design note.** The book already holds a two-page design note, `papers/design-note/design-note.md` (draft of 18 November 2026, agent-court#35). The paper builds on it rather than duplicating it: its contribution list and its non-goals are the starting text for §§1, 5 and 6.

**Literature.** A survey current to November 2026 is running. Its findings will be placed row by row against Appendix A and against the three claims.

**Authorship.** Guy Freeman as sole author, with one paragraph disclosing the model sessions' roles.
