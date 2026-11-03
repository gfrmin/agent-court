# The predecessors' sessions — what the local record on steel holds, 3 November 2026

*The author's extraction from the Claude Code session files on the owner's machine `steel` (`~/.claude/projects/`), supplied by him as archives on 3 November. Only three projects still have session transcripts there — assize (41 sessions, 4–28 Oct), jack (8, 13–26 Oct), proplang (7, 25–26 Jul); the sessions of credence, credence-governor, life-agent, tannen, wald-arena and wald-charter have expired, and what remains of them is the per-project memory notes Claude Code keeps (293 Markdown files, 2 MB). The transcripts and notes themselves are not in this repository. What is quoted below is confined to the projects — the owner's words about his own design, dated, and the sessions' notes about the projects' lessons, marked as such. Quotations are verbatim; `[G]` marks the owner's own words, `[S]` a session's note or echo.*

## proplang — the exact-freeze sitting, 25–26 July 2026 (session `63f789bd`)

- 12:56 [G] "I want to create a language that can only be used to make decisions that maximise expected utility under Bayesian decision theory, i.e. a language to create Bayesian-optimal agents, including metareasoning."
- 13:14 [G] Six reviewer mandates, each a named historical failure shape: "Is any THEOREM installed as a DEFINITION?" — "the Savage expected-utility shape — was twice committed as a primitive definition rather than proved of the implementation … a green that cannot fail"; "Is any RULING asserted N times and DERIVED zero times? (… called M5: … repetition substituting for proof)"; "Is any LOAD-BEARING QUANTITY defined NOWHERE? (… called H)"; "Does any TYPE on the frozen surface LACK ITS DERIVATION from the brief? (… a type named `Util a y` sat on the surface for 86 commits hiding a calculator, because the deletion audit polices TERMINALS but nothing policed TYPES)"; "Is any CONVENTION silently OVERLOADED?"; "For every NEW OBJECT … WHAT IS IT A FUNCTION OF?"
- 13:27 [S] Six reviewers with no shared context: "four of them independently converged on the same three defects (noget, the doorless route, the dead anchors) while each contributed findings no other found."
- 13:39 [G] "I feel that what should be a simple system in its foundations is actually too complicated and unmanageable... All I want is a small set of primitives (which reflect Bayesian decision-theoretic axioms/types), and everything else composed from them... Is that too much to ask for????"
- 13:40 [S] The diagnosis: "the process never got the deletion test … The *protocol* only accretes: every incident mints a clause, and no clause ever retires. CLAUDE.md's increment protocol is now the bloated alphabet, one level up." And: "the record is not the artifact. Of the ~26k lines of markdown, almost none is the language — it's custody."
- 13:46 [G] "I don't want to rely on prose and vigilance any more, ever..." and, on the alphabet: "If we have to choose between Add and Sub I'd rather keep Add (unless somehow we can get rid of both??)" — ruled by algebra: Sub generates Add; the table shipped 9/1.
- 14:05 [G] "so we have the language, but how do we know it's necessary and sufficient for a Bayesian agent, including metareasoning?"
- 14:09 [G] "I guess the architecture of this codebase still isn't clear to me, its supposed author."
- 14:16 [G] "I don't want to rely on markdown... Can't the agent also be primitives + derivations? What is the 'oracle world'? It just seems fragile in the way the 'calculator' isn't."
- 14:33 [G] "how do we make it a closed system, so, for example, metareasoning happens automatically?"
- 14:35 [G] "what does 'the oracle is law' mean? Is our oracle optimal?"
- 14:44 [S] The remedy drafted that afternoon: "An oracle row earns its seat by a unique kill … Nothing in the system holds a seat by familiarity once Phase 2 closes."
- 26 Jul 06:25 [S] "the living tree … went from 42,113 lines at the transport freeze to 25,887 at this tag"; "it's finished for necessity. The programme still has two unproven halves and one undemonstrated one — nothing yet proves the language is enough (sufficiency), metareasoning is sayable but not yet automatic (closure), and no agent has yet made a live decision outside the oracle worlds."
- 26 Jul 06:34 [S] "After 5, the roadmap terminates. Everything else stays what it already is — named, demand-gated residue … the one genuinely deep research item left from the brief: §6's self-compression — the agent buying its own macros … That one is a research programme, not an increment."
- 26 Jul 06:37 [G] "good, but why not give the roadmap and reasoning behind it too? But I suppose it doesn't matter as long as you have oversight...."

## credence — the memory notes (April–July 2026)

- 20 Apr [S] Merge authority granted to the session: "The author/Claude conversation loop *is* the review — there is no separate human reviewer role … Do not escalate or ask for confirmation on individual merges once the pattern is established; that is friction without value."
- 20 Apr [S] "Codify ad-hoc judgement after its second well-executed instance; don't wait for a third where it fails."
- 1 Jul [G, as the note reports] Ratifying a read-only wire verb: a scalar across the wire "reintroduces the hardcoded-threshold failure mode EU-max exists to eliminate … the engine cannot enforce a float's use once it crosses the wire … The only binding surface left is the protocol contract itself."
- 3 Jul [G] "ratified, just design a better experiment next time beforehand" — after three gate rounds ran against a measure the agent was never asked to optimise; the note's rule: derive the gate's statistic from the declared utility "IN THE DESIGN DOC, before the first run".
- 4 Jul [G] "arent you manually modelling too much instead of using the general prior, metareasoning etc?" — the note's gloss: "a bespoke corrector for the winner's curse, a bespoke detector for drift, and the framework dies of a thousand locally-reasonable patches."
- [S] On the governor: "every gated decision is an overridable ask by default — the governor SURFACES risk to the human operator (the final authority), it never hard-refuses on its own … a categorical deny implies *infinite* disutility, but harm-cost H is finite."
- [S] On the metric: "accuracy is a corruptible metric — the agent can hit any accuracy target by overusing the default action. Calibration … is the harder metric."
- [S] Standing: "There is one learning mechanism: `update`. Everything else is a hypothesis."

## tannen — the memory notes (August–September 2026)

- 28 Aug [G, standing instruction] anything requiring review goes to the phone.
- 30 Aug [S] "A cure that has not been measured is a guess with a citation."
- 12 Sep [G] "Interview me for my rulings, that's a standing order."
- 12 Sep [G] "My rulings have now been corrected by measurement on the custody question, by the spec-table guard on the supersession path, and by the floor audit on the remote. In each case the correction came from an artifact the repository built to be checkable, wielded against the owner's instruction. That is the strongest available evidence the governance layer earns its cost — not that it prevents error, but that it makes the owner's errors cheap to find and expensive to ignore."
- 16 Sep [G] "we need to speed up development without losing too much rigour"; "it's rigorous but too slow"; "why do we have all these dates?"; "so why did you ask me, if we can wait for gate sitting?" — the note's measurement: "18 min of hooks per commit (19 for a one-file docs commit), 46 min make verify, 41 min CI … The M4 sitting driver: 19 steps, 3h03m, rehearsed twice full. 265 records in 23 days at 79 lines. The rigour that matters (frozen laws, poison matrix, doors, append-only store, resolving bindings) was never where the time went."
- [S] On green-that-cannot-fail: "across tannen's whole life this is one class with nine instances … Seven of the nine are inside artifacts written to close an earlier instance of the same class … Writing the discipline down does not install it — the observed pattern is that the *production* rate of this class does not fall with attention, only the *catch* rate does, and only when something mechanically forces the failure to be seen."
- [S] "a green frozen suite is the protocol's definition of done, **not** evidence of soundness against an adversarial world."

## wald-charter and wald-arena — the memory notes (September–October 2026)

- [S] The cage door: `gfrmin/wald` master guarded by a ruleset with no bypass actors; "the author's commits to master … go through the door, which only the owner opens … A push with the door shut fails with 'push declined due to repository rule violations'. That is expected, not an error to work around."

## assize — the sessions on steel (4–28 October 2026)

- The owner's 95 short turns in 24 days are mostly the operator's hands: tokens into the keyring and files deleted (22 turns mention a token, PAT, keyring or secret), runners and services restarted (18), status reports sent to a phone (7). Among them: 5 Oct "Label PR #2 measure. Have the session append the host witness … That discharges brief 0's 'Guy confirms the host run' without me confirming anything by hand"; 9 Oct "how does 32 need me? is there an issue?"; "wont 34 close automatically?"
- 6–7 Oct [G, in every builder prompt] "Stop and report under the brief's boundaries. A stopped session with a clear STATUS is a success. A session that asks Guy something it could have decided and recorded has failed."
- 24 Oct [G] On the wish to freeze at the seal, keeping a pre-committed bound rather than loosening it: "a bound missed by one is a recorded fact about the price of the sovereign, which is the thing the price line exists to measure, and loosening it now to make the forecast safer is the habit we're trying to break."
- 24 Oct [S] "I made the same mistake in the earlier question by offering 'bound 3, a safer bound' as an option."

## jack — the founding sessions on steel (13–26 October 2026)

- 13 Oct 15:23 [G] The founding prompt: "Build C0 exactly as its §9 describes, and nothing beyond it. CHARTER.md is the founding text: never edit it; propose changes in REPORT.md … Pins: every pin in §9 with its named mutant, KILLED, with a passing twin … A pin that cannot fail is a defect … A stopped session with a clear report is a success."
- 14 Oct 01:36 [S] The scope cut, "in Guy's order": the rule language removed, C0 the record only, 392 kernel lines.
- 14 Oct 07:36 [G] "you surmised correctly why i need those non-anthropic models" — the second checker by another family.
