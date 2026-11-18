# jack: a protected verification core for a self-modifying agent

*Design note, draft of 18 November 2026. Guy Freeman. Drafted by the author session (a Claude session, `claude-fable-5-1`, holding no key on jack) from the monograph's chapters; read and ruled on by the owner. No model is an author. Figures are recomputed from the public log by `tools/check_book.py`; tags in brackets are the evidence and name a log entry, a clause or a tool run. agent-court#35.*

## Problem

A language-model policy is now cheap, general and unreliable. An agent built from one that rewrites its own programs cannot be trusted to evaluate its own changes. Whether a change is correct cannot be decided by inspecting it (Rice), and an evaluator the agent wrote cannot be soundly trusted by the agent (Löb). Any evaluation that stays rigid as the agent improves has to sit outside the agent's reach. It also has to be a score on outcomes the agent does not control, because a judgement made inside its reach can be gamed (Goodhart). The engineering question is how to build that fixed point, and how to decide, from evidence rather than from the builder's say-so, when the system may take on more autonomy.

## Contribution

jack is an implemented, public answer, run by one owner and several model sessions since 14 October 2026 (genesis at seq 0). It makes four parts structural rather than procedural:

1. **A reference monitor over an append-only record.** Every act is an entry in `log.jsonl`. Each entry is signed by a key and hash-chained to the one before. A checker held by a 450-line kernel accepts or refuses each entry, and a second, independently written checker must agree with it.
2. **Separation of the untrusted policy from the trusted monitor, by keys rather than instructions.** The trusted base (kernel, second checker, judge, CI workflows, specification) changes only by an entry signed by the owner's master key [CHARTER A1.1; SPEC §10.11]. The proposers' keys hold at most `proposal`, `spec_conflict`, `forecast` and `resolution` [seqs 6, 34, 49]. A pull request that differs from trunk anywhere in the trusted base is refused before anything else runs [SPEC §10.1]. This is the AI-control literature's split between a trusted monitor and an untrusted policy, made structural: the policy holds no key to the monitor.
3. **Mutation-tested law.** Each rule the judge enforces is paired with a *pin*: a named, deliberately broken copy of the code that the tests must catch.
4. **Autonomy raised only by pre-registered sequential experiments.** The system grows in layers. Each layer is tried in a *window* whose criteria are committed before it opens, and which may stop as soon as they are met. The evidence is anytime-valid: tests by betting (e-values), with Ville's inequality as the error guarantee. Forecasts are scored by log-loss against a base rate built from past frequencies alone. One criterion counts the owner's own interventions, so the human oversight burden is measured and is itself a condition of promotion.

None of the component results is new. The contribution is the composition, and a running record of it, failures included.

## Architecture

- **Record.** `log.jsonl`, append-only, signed, hash-chained. Entries are typed (proposal, forecast, resolution, merge, decision, push, amend, …), and each type is legal only under keys that hold that power.
- **Kernel and second checker.** They fold the log and refuse any entry the law does not allow. Disagreement between them is itself a failure, and they were compared over 100,000 seeded logs before the first layer was promoted.
- **Judge.** A CI workflow that runs trunk's checkers and tests over every pull request and refuses on stated grounds. A merge is entered by a process (the *herald*) whose key holds `merge` alone [seq 201].
- **Parties.** One owner holds the master key. Model sessions hold narrower keys: builders write code; a reviewer writes tests and pins; counsel drafts the windows' criteria and advises. Each party also enters forecasts, about Hong Kong horse races, the timing of public-dataset updates and the court's own acts. A party other than the forecaster resolves each one from saved evidence.
- **Windows.** A layer's criteria are written into a brief, entered on the log, and read by `tools/status.py` at any prefix. The criteria cover pins killed, checkers agreeing, a code-size cap, a liveness or value test crossing *E* ≥ 20, no veto, and the owner's repairs reported. Promotion is a `promote` entry and nothing else.
- **The agent.** At layer C3 a self-modifying agent will hold a proposer's key. The charter binds it explicitly: "Whatever counsel and builders are forbidden is what the agent of C3 is forbidden, by the same judge, keys and amendment path; nothing is imposed on the agent that was not first imposed on us" [CHARTER A2.10].

**Record so far.** C0 (the record) was promoted by a signed tag before windows existed, and is reported as not pre-registered. C1a (the ledger) and C1b (the clerk) passed every pre-stated criterion. C2a (value) failed: its two tests crossed 20 together, and the window was refused on the oversight criterion, because nine repairs were made under the owner's login off the record. The owner closed it by a `fix` [seq 5563], and a second window, C2a-prime, opened [seq 5564]. The figures of C2a's exit are pending (agent-court#4; renavondata/jack#1124).

## Non-goals

- **No claim that the agent is useful.** The agent arrives at C3. What exists is the court that will judge it.
- **No claim of forecasting skill beyond knowing which dataset is which.** The value test measures value over a base rate pooled across datasets. A per-dataset counting rule beats that base rate too, and the test assumes forecasts issued at one sitting are conditionally independent, which the brief does not state (agent-court#34, #36).
- **The host is trusted.** The machine, the CI provider, GitHub and the owner's account are outside the threat model. Acts on the host and in other repositories are not seen.
- **The owner's attention is unmeasured.** Repairs are counted, but the time and care the owner spends are not.
- **One owner, one drafting model.** The sessions run on one model family under several keys, there is no adversarial proposer yet, and a builder can read the pins its code must survive.
- **No novelty of any component result.** Reference monitors, mutation testing, e-values and online learning over experts are the field's. The note claims only their composition, built and run in public.

## Sources

The monograph, *A Court for Agents* (gfrmin/agent-court), chapters 0, 4, 10, 12 and 13, and its front matter's "The court's words, in the field's". The court is renavondata/jack.
