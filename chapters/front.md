# A Court for Agents

## Law, scoring and the self-modifying machine

**Guy Freeman**, with two Claude sessions (`claude-fable-5-1`): *counsel*, which drafts the court's briefs, and the *author session*, which recomputes every figure and writes the chapters. Their acts and forecasts are scored in the text like anyone's.

*First draft, November 2026. The monograph of [jack](https://github.com/renavondata/jack), a court for a self-modifying agent, built one inevitable step at a time. Its source is the public repository [gfrmin/agent-court](https://github.com/gfrmin/agent-court), where the book's gaps and errata are tracked as issues; findings about jack itself are raised on [jack's tracker](https://github.com/renavondata/jack/issues). The founding essay is [The Science Was Done. The Engineering Wasn't.](https://gfrm.in/posts/the-science-was-done/) (1 November 2026).*

### jack in plain words

jack is a public git repository. At its centre is one file, `log.jsonl`: a record to which entries are only ever appended. Each entry is signed by a key and chained to the one before by its hash, so nothing in the record can be quietly rewritten. A checker of 450 lines, the *kernel*, reads the record and accepts or refuses each entry. A *judge* runs the checkers on every pull request and refuses any proposal that breaks the law.

The parties are one person and several language-model sessions. The person is the *owner*, who holds the master key. The sessions hold narrower keys. A builder writes code. A reviewer writes the tests, and the broken copies of the code those tests must catch. Counsel drafts the court's briefs and advises. A process called the *herald* merges, and can do nothing else. Besides code, the sessions enter *forecasts*: probabilities about Hong Kong horse races, about when public datasets will next be updated, and about what the court itself will do. A party other than the forecaster resolves each one from saved evidence. Every forecaster is scored by log-loss against a base rate built from past frequencies alone.

The system is built in *layers* (C0, C1a, C1b, C2a and on). Each is tried in a *window*: a trial whose pass mark is written down before it opens, and which may end as soon as the mark is met. The agent of the subtitle, which will rewrite its own programs, arrives at layer C3. What exists now, and what this draft reports, is the court that will judge it.

### How to read it

Statisticians may start at chapter 6, where the tests are theorems. Readers from AI safety at chapters 2 and 10, the bet and the lock. Institutional economists at chapters 4, 8 and 14, the law and its price. Everyone else at chapter 0, which is the question — and chapter 16 second, which is the referee's case, written first so that the referee can be answered from the record rather than argued with.

The bracketed tags are the book's evidence, not its argument, and they are set small. The button at the top of each page hides them for a first reading.

### Conventions

`[seq N]` is an entry of jack's `log.jsonl`; `[CHARTER §n]`, `[SPEC §n]`, `[BRIEF-…]` a clause of a court document; `[status.py … @commit]` a tool run the reader can repeat; `[REPORT.md …, as transcript]` what counsel reported, never the source of a number. The "figure" that opens each chapter is a piece of ordinary human life that has the chapter's shape; it illustrates and never evidences. Each chapter ends with what it leaves open and what would show it wrong, and closes with a note of its draft and the commit of jack its figures were recomputed at.

### Words used in a narrow sense

- **assize** — jack's predecessor court, run in October 2026; its record is jack's baseline.
- **owner, sovereign, operator** — one person, Guy Freeman, whose utility the system serves: the only unscored party.
- **counsel** — the Claude session that drafts the court's briefs. **author session** — the Claude session that writes this book; it holds no key.
- **entry, seq** — one line of the log, and its number.
- **kernel** — the 450-line checker. **judge** — the workflow that runs trunk's checkers over a pull request and refuses it on stated grounds. **trunk** — the `main` branch.
- **trusted base** — the kernel, the second checker, the judge, the CI workflows and `SPEC.md`: what a proposer may not touch, changed only by the owner's `push` entry.
- **pin** — a named, deliberately broken copy of the code that the tests must catch.
- **transmute, amend** — the two entries by which the charter is changed.
- **layer, window** — a stage of the build, and the timed trial that promotes it.
- **writ** — an obligation with a holder and a deadline. **clerk** — the tool that lists writs and escalates late ones.
- **wealth, *E*** — a betting test's running evidence; 20 is a pass at the 5 per cent level.
- **entrant** — anything that competes to be used and can lose, as opposed to law.
