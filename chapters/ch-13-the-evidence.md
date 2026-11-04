# 13. The evidence: the windows

## The figure: the laboratory notebook

A result in a notebook is worth what the entry before it says: what was to be measured, how, and what would count as failure — written before the measurement, in ink. Everything after that is a number against a line that was already there. This chapter is the court's notebook. Each window is reported as the pre-registered experiment it was: its criteria, null, attack list and maximum duration as committed before it opened; what the record shows at the exit prefix; what counsel forecast about it and how that scored; and what the window's precedents cost. Nothing here is a number the author did not recompute.

## 13.1 How a window is read

Every window has four texts, and the chapter cites them in this order: the brief, which pre-states everything; the opening entry, which fixes the instant from which events count; the exit prefix, which is the log at the instant of the sovereign's `promote` [CHARTER A5.1]; and the tool run — `tools/status.py` with the committed evidence files, or `tools/value.py` — that prints each criterion from the log and the tree. Counsel's exit report is cited as what counsel said; the figure in the text is the author's rerun. Where the two differ, the chapter says so.

## 13.2 C0 — the record (14–17 October)

Pre-stated: the charter's §9 criteria as amended by A1.5 — every pin killed with a passing twin from trunk; the two checkers agreeing on the real log and 10⁵ seeded logs; the kernel within 450 lines; the sovereign having read it and signed genesis. No window was stated and the layer was patched in place throughout — counsel's own disclosure [REPORT.md §8.3.4, as transcript] — so C0 is the one layer the chapter reports as *not* a pre-registered experiment, and the reason every later layer is one. Exit: genesis at seq 0 (2026-10-14T05:41:39Z); the run of record on commit `46543de` compared 100,000 logs and 658,885 prefixes with no disagreement [`transcripts/diff-100000-20261017T1001Z-part00…11.json`]; the kernel at 411 lines then and 450 now; promotion by a signed tag, the last the programme uses [`git tag c0-exit`, 2026-10-17].

## 13.3 C1a — the ledger (25–31 October)

Pre-stated [BRIEF-C1]: pins killed; checkers agreeing; kernel within 500 and `judge/scope.json` unchanged from the installing push; at least twenty forecasts by three proposers, ten resolutions, five world-typed with hashed evidence; the score vectors reproduced; no veto. Opened at seq 30 (`amend A3`, in force from seq 31, 2026-10-25T16:44:10Z); closed at seq 188 (2026-10-31T10:42:10Z), day six of fourteen, by the first `promote` under A5. Recomputed at the exit prefix [`status.py --subject C1a --as-of 2026-10-31T10:42:10Z --runs transcripts/evidence/runs-tests-20261031.json @6b800e14`]: every criterion met; 63 forecasts by four proposers, 19 resolutions, 12 world-typed with evidence whose hashes the tool recomputed from the files; counted code 5,998 of 6,900 as `status.py` prints it (the cap in force at that instant was 6,200, raised to 6,900 at seq 197 that afternoon); procedure : object 127 : 32; no forecast unresolved past its deadline. Counsel's six forecasts on the window [seqs 37–42] resolved five of six, all but J6 — a checker disagreement on a simulated log — as counsel bet; their log-loss is in `data/counsel-forecasts.md`. The window's precedents: four forecasts expired undischarged (chapter 5 §5.3); a resolution counsel's herald entered wrongly and the kernel would not let anyone correct [REPORT.md, C1a §4.2, as transcript]; three brief versions blocked on defects the previous version introduced.

## 13.4 C1b — the clerk (31 October – 1 November)

Pre-stated [BRIEF-C1b v7]: pins killed; checkers agreeing; counted lines within 6,900 and kernel within 500; the attack test green on `main` before the first counted item; liveness *E* ≥ 20 at *p*₀ = 6/11; no veto; the enforcement-map rows the layer moved reading `code`; late and off-log repairs reported. Opened at seq 188; closed at seq 337 (2026-11-01T11:31:58Z), twenty-four hours and fifty minutes later. Recomputed [`status.py --subject C1b --as-of 2026-11-01T11:31:58Z --runs transcripts/evidence/runs-tests-20261101b.json --acts transcripts/evidence/acts-20261101.csv --json @6ebea1a`]: every criterion met; nine items, all *Y* = 1, stakes 0, 22/45, 33/40, 77/75, 209/180, 44/35, 319/240, 187/135, 143/100, wealth 214358881/8398080 ≈ 25.52; counted 6,882 of 6,900; the attack test first green at 2026-10-31T13:32:21Z, the first item at 15:50:40Z; procedure : object 67 : 82; late-reported repairs 0, off-log repairs 0; the sovereign's five acts all decisions [seqs 197, 201, 216, 217, 337; `plan.md` F4]. The window's precedents are the clerk's brief's §4 and chapter 11 §11.5's.

## 13.5 C2a — value (1 November –)

Pre-stated [BRIEF-C2a v2]: the value statistic as A4.4's bet on the bounded log-loss difference between the Bayes mixture and the base rate, over two streams with declared identities and cutoffs; the roster frozen at the opening; eighteen pins; a cap of 7,800 raised by one push; *E*ᵥ ≥ 20 with the liveness process continued. Opened at seq 367 (2026-11-01T15:04:14Z). What the author could recompute on the morning of 3 November: the liveness process continued, about 1.44 over forty items; the ratio 170 : 269; six builder forecasts overdue on 2 November [`status.py --subject C2a --runs transcripts/evidence/runs-tests-20261101b.json @6b800e14`]. By the afternoon the attack gate's instant was derivable from a committed tests run, and the value statistic with it [`plan.md` F2, discharged]. The window's first two days, as a joint table of the two processes that must cross together (chapter 6 §6.4): liveness at 20 or more only until 04:55Z on 2 November, peaking at 605.7; value at 20 or more only between 03:12Z and 04:18Z on 3 November, peaking at 20.131519; the smaller of the two never above 2.450887 (seq 454); then four expiries at 06:00Z taking liveness from 2.33 to 0.556 [`status.py --subject C2a --as-of <instant> --runs transcripts/evidence/runs-tests-20261103-resolve.json @33fb4a0`, and `runs-tests-20261103.json` for the expiries; counsel's full table, `transcripts/evidence/counsel-rm-joint-20261103.txt`]. As a pre-registered experiment the window has not failed — it is a maximum, and it runs to 15 November — but its first forty hours are the record of two processes that each crossed, apart. This section is completed from `data/C2a-exit.md`.

## 13.6 C2b — the election

Pre-stated [BRIEF-C2b v6, under review]. Completed from `data/C2b-exit.md`.

## 13.7 Counsel's forecasts, scored

The running table is `data/counsel-forecasts.md`, recomputed by the author from the log at each commit that cites it: forty resolved at a mean log-loss of 0.593 against the base rate's 0.685 on the same events, as of `6ebea1a`. The K-series on the predecessor's ledger [CHARTER §11] is scored in `claude/acts-weekly.md` and will be restated here from `assize:reports/L*/forecasts.jsonl`.

## 13.8 What would show this chapter wrong

A figure in it that a reader with the clone cannot reproduce with the stated invocation. A criterion reported `met` whose evidence file is not committed. A window's stated end moved, or its wealth reset, between the brief and the exit. And the ordinary way an experiment is wrong: a crossing on paper that the next window undoes — which is why the wealth is one process and chapter 11 §11.12 names the convergence tests.

---

*Draft note. Draft 0, the author session, 3 November 2026 — the frame and what the author can recompute today; each window's section is completed from counsel's `data/<layer>-exit.md` as it lands, with every figure re-run by the author on the clone. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*
