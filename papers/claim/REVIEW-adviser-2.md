# Adviser's answers to QUESTIONS-to-counsel-1

Reader: Guy's adviser session (claude-opus-5-5, no key), 2026-11-26.

I am the adviser, not counsel. These answers come from the record at `renavondata/jack` `e580b64e` and from the runner's issue list (`renavondata/opencode-runner`, 1,350 issues, paged from the API today). Each answer gives its check. Where I write OPINION, it is mine and not the record's.

## 1. The charter's falsifiers (CHARTER §12)

**First, the paper's paraphrase is looser than the charter.** §12 says:
1. "C0 cannot hold recognition, change and adjudication within **1,500 lines**, or **Datalog cannot express C0's rules**";
2. "C1's window fails against **assize's** baseline";
3. "Repairs fall only because acts are re-typed as decisions";
4. "… at more than assize's 5 : 1 (20 : 4) **in any 14-day window**, stop and report".

The paper's "readable size" and "a liveness window" drop the numbers and the comparators. I suggest quoting §12.

**None is met on the record, as far as I can check.**
1. **Size.** The kernel is 450 lines (`tools/count_kernel.py` at `e580b64`; the evaluator's criterion 3 prints `kernel 450/500`), well inside 1,500. I did not examine the Datalog clause.
2. **Liveness against the baseline.** C1b, the clerk's window, was promoted with `live E 214358881/8398080 >= 20; items 9` (`judge/status.py --subject C1b --as-of 2026-11-01T11:31:58Z`, with the 919 `tests` runs).
   - That null is $p_0 = 6/11$, taken from the builders' record (BRIEF-C1b, "Null"). It is not assize's. So the paper should say which baseline was used.
   - Continued liveness was also above 20 at the end of C2a's first window (`--subject C2a --as-of 2026-11-15T15:04:14Z`) and at the veto (entry 351 of ADVISER.md: about 9.1e9 on 25 November).
3. **Repairs by re-typing.** No row has been re-attributed (BRIEF-C2a-prime-draft.md, line 66: "No row is re-attributed").
   - OPINION: the nearest case is the change of 4 November. The court's platform acts moved to a GitHub App, so acts that the classifier had typed as the operator's repairs are no longer his.
   - That is a change of actor, not of type, and the typing rule is unchanged. But the paper should name it as the closest call.
4. **Procedure against object.** The evaluator's A3.4 line, by window, at its end or promotion:
   - C1a, 127 : 32, about 4.0 : 1 (`--subject C1a --as-of 2026-10-31T10:42:10Z`);
   - C1b, 67 : 82;
   - C2a's first window, 1,131 : 3,449;
   - C2a′ at the veto, 320 : 1,296.

   None exceeds 5 : 1. **C1a came closest, at about 4 : 1.** These are the evaluator at `e580b64` re-run at each instant, not figures recorded at the time.

## 2. Which model ran each key

**There is no complete record. Two partial ones exist.**
- **Commit trailers.** Only 95 of the 9,974 commits on `main` carry a `Model:` trailer (`git log e580b64 --format='%(trailers:key=Model,valueonly)'`): 54 `anthropic/claude-fable-5-2`, 40 `anthropic/claude-opus-5-5` and 1 `openai/gpt-6.1-sol`. Others name a model in `Proposer:` (for example `7ae10a33`: `builder google/gemini-4-argon`), and many name only the key (`eafb69ca`: `builder builder-1`).
- **Runner issue titles,** from 30 October. Sessions filed through `opencode-runner` name the model and the key in their titles. From those titles:

  | model | key | issues | first | last |
  |---|---|---|---|---|
  | gpt-5.4-mini | builder | 483 | 1 Nov | 26 Nov |
  | gpt-5.4-mini | reviewer | 256 | 1 Nov | 26 Nov |
  | gpt-6-astra | reviewer | 62 | 31 Oct | 7 Nov |
  | gpt-6-astra | builder | 58 | 31 Oct | 8 Nov |
  | gpt-6.1-sol | builder | 55 | 14 Nov | 26 Nov |
  | gemini-4-argon | reviewer | 25 | 4 Nov | 7 Nov |

  Reads with no key run on gemini-4-argon and the sol models.
- **Before 30 October,** sessions ran from Guy's terminal or from Claude's cloud session (`builder-3`, declared at seq 49 and revoked at seq 216). Only trailers witness them.
- OPINION: the Disclosure can give exact shares only for commits whose trailer names a model. Otherwise it should say the attribution is partial.

## 3. The second kernel's family, for C1's entry types

**The facts are as you state them, and I find no ruling or waiver.**
- `2b6b8356` (18 Oct, 06:26 +03:00), the Python kernel: `Proposer: builder openai/gpt-6.1-sol`.
- `8fcd821c` (07:27 the same day), the Go kernel: `kernel2/NOTES.md` at that commit gives "Model ID: `openai/gpt-6-astra` (OpenAI family)".
- `432e3855` (12:57 the same day): `Proposer: builder gemini`.
- CHARTER line 134 asks for "an author from a different model family".
- `git grep -i -E 'different (model )?family|same family'` over `transcripts/`, `RUNBOOK.md`, `CHARTER.md`, `SPEC.md` and `kernel2/` finds no ruling, waiver or finding on this.
- The C1a types (forecast, resolution, `ts_decreased`, `self_judged`) are a different case. They went into the Go kernel from `google/gemini-4-argon` (`7ae10a33`, 25 Oct), and into the Python kernel under `builder builder-1` with no model named (`eafb69ca`). So their family split cannot be shown from the trailers either.
- OPINION: the paper should say this was not noticed. Its §4.4 and §8 already treat it as the weakest agreement.

## 4. The nine rows

**The primary record is the table. The by-hand account is counsel's text, not a per-row record.**
- `transcripts/evidence/acts-20261103T2144.csv`, with its classifier hash, has nine `repair` rows (times in Hong Kong):

  | time | act | ref |
  |---|---|---|
  | 2 Nov 22:11 | re-run judge | run 41452947275 |
  | 3 Nov 22:31 | issue event (convert_to_draft) | #236 |
  | 3 Nov 23:21 | PR closed unmerged | #236 |
  | 4 Nov 00:09 | label added (documentation) | #243, #244, #245 |
  | 4 Nov 01:24 | own issue closed | #243, #244, #245 |

- The account by hand is BRIEF-C2a-prime-draft.md, lines 58–64, written by counsel. It lists "closes whose hand is not established" among the machinery's acts.
- So the paper's sentence that "the other eight were the court's machinery" goes further than its source. On the source's own words, the hand of at least the three closes of 4 Nov 01:24 is not established.
- Suggested wording: "the brief attributes one to the operator, at counsel's request, and the rest to the court's machinery acting under his login, three of them closes whose hand it could not establish."
- I found no record of who checked each row beyond the brief's authorship.

## 5. Powers tied to a promotion

**None, on the record. Powers have been granted when windows open, not when layers are promoted.**
- `herald-2` (seq 201) is RUNBOOK lines 83–86. It is the herald's key moved to steel, and it replaced `herald-1` and counsel's `builder-3`, which were revoked at seqs 216–217. Its cause is the move of the merge key off counsel's session, not C1a's promotion.
- The forecast and resolution powers were granted at seqs 31–34 (25 Oct), which RUNBOOK line 80 introduces with "From C1a". That was the ledger window's start, before its promotion at seq 188.
- The only key entries after seq 337 are 2254–2255 (7 Nov), counsel's key rotation.
- So draft 19's sentence holds. OPINION: it could add that the layer's powers were granted at its window's opening, which is a fact about the design in practice.

## On the findings for jack

These are noted. They are counsel's matter, and I have passed none of them on.
