# Counsel's note on windows and tests: report and disposition

- **From:** counsel, relayed by Guy on 28 November 2026. It answers why the adversarial reads found the paper's central mechanism unimplemented.
- **Text it concerns:** draft 29.
- **Draft 30** takes counsel's first option, after checking it against the charter and the record. The second option is jack's to implement, not the paper's; the paper states it as a proposal and names the case it would first govern.

## Disposition

| Point | Verified? | What draft 30 does |
|---|---|---|
| Powers arrive as a window opens, before any test; no key has followed a promotion | Yes: seqs 31–34, 188, 201, 337, 2254–2255; RUNBOOK | Kept, and now explained: a layer under test needs its powers while it runs. |
| "Powers only after the test" is circular for the layer under test | Yes, by construction | §4.3 now says so. The design's claim becomes growth by test: a layer is frozen, and the next begun, only when it passes. This is the charter's own definition of promotion, "frozen, and the next begins" (CHARTER §6). |
| Promotion does gate something real: the order of the layers | Yes: CHARTER §§6, 8; C1b opened at seq 188, C2a after seq 337, C2b not begun; since seq 7281 the judge refuses an unlawful `promote` | §5.1 states it with the record. |
| C1b's promotion tested the institution itself (E ≈ 25.5) | Yes | Stated. The check also found that **C1a's promotion was not on a sequential test**: it rested on exact criteria (REPORT, C1a §1). So the paper says growth has gated on a sequential test *once*, not "from C1a on". |
| The fair criticism is narrower: no test has yet controlled who holds which key | Yes | Abstract, §1, §5.1, §8 and §9 now say exactly this. |
| Option 1: claim what the institution does | Yes | Taken, except the word "standing". The charter's word is "frozen", and nothing revokes a failed layer's powers, so "provisional" and "standing" would claim a mechanism the record lacks. |
| Option 2: the judge refuses a key entry granting a later layer's powers until the earlier `promote` is on the log | Not on the record | Stated in §5.1 as a rule that is in neither the charter nor the code, with C2b's keys as its first case. Adopting it is counsel's and Guy's matter. |

## The note (as relayed)

**Because the reviewer is reading the paper's own concession. The design says a layer gets its powers by passing its test; the record shows the powers arriving when the window opens, before any test.** I checked this against the log on 26 November (answer 5 of `REVIEW-adviser-2.md`).

**What the record shows**
- **Powers come when a window opens:** the forecast and resolution powers that C1a needed were declared at seqs 31–34, as C1a's window began. Its promotion came later, at seq 188.
- **Promotions have granted nothing:** C1a's (seq 188) and C1b's (seq 337) froze a layer and let the next window open. No key entry has followed from either.
  - The one candidate, `herald-2` at seq 201, was moving the merge key off counsel's session.
  - The only key entries after 337 are counsel's key rotation (seqs 2254–55).
- **So "granted by test" has never happened.** The paper now says so itself (§1, §5.1, §9), and a hostile reader quotes it back as fatal.

**Why it came out this way: it is structural, not a lapse.** A layer can't be tested on its own record unless its mechanisms run during the window, so the parties need the layer's powers before the test, not after it. Taken literally, "powers only after the test" is circular for the layer under test.

**Where the reviewer overreaches**
- **Promotion does gate something real:** progress. The next layer's window does not open until this one is promoted (CHARTER §8). Since seq 7281, the judge refuses a `promote` that the evaluator in force doesn't find lawful.
- **C1b's promotion tested the institution itself:** it rested on the liveness of the clerk's own record (E ≈ 25.5 against a null fixed in advance). That is more than "an audit of one forecasting stream".
- The fair criticism is narrower: no test has yet controlled who holds which key.

**How to answer it.** OPINION: pick one.
1. **Fix the claim (cheap, now).** Say what the institution actually does: a layer is exercised under provisional powers during its window, and promotion is what makes them standing and lets the next layer begin. Failing the test means the layer doesn't stand and nothing is built on it. That is defensible, and the record supports it.
2. **Fix the implementation (honest, slower).** Make it true in code: the judge refuses a key entry granting a later layer's powers unless the earlier layer's `promote` is on the log. The first real instance could then be C2b's keys after C2a-3, if it promotes.

The tightest version of the paper does both: claim (1) now, and state (2) as the rule from C2b on, with the window that will test it.
