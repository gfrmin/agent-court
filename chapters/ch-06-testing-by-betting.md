# 6. Testing by betting

*Draft 1, the author session, 3 November 2026. The theory and the liveness evidence are here; the value evidence waits for counsel's `data/C2a-exit.md` (`plan.md` F2) and will be added in draft 2. Provenance tags as `plan.md` §2; the record is `renavondata/jack` at `6ebea1a`.*

## The figure: the punter

A punter at the window may cash out whenever he likes. That is the whole difference between him and a scientist running a trial: the scientist must say in advance how many patients, and if she looks at the data halfway and stops because it looks good, her p-value is a lie. The punter's wealth is honest at every moment. If he started with a pound, never bet more than he had, and has twenty now, then the house's claim that the races are fair is in trouble at odds of twenty to one — whenever he stops, whatever his reasons, however many times he peeked. The operator of chapter 0 is the punter. He looks at the record when he wakes. The tests must be built so that looking costs nothing.

## 6.1 What we have, and what it cannot do

We have a clerk that turns the record's promises into a sequence of zeros and ones (chapter 5), and we will shortly have forecasts and their scores (chapter 2) to compare against a base rate. We need to say when a layer has worked — when the items are being completed without the operator's hand more often than they were under the predecessor, when the forecasts are worth more than knowing nothing — in a form that one person can act on the moment it is true. A fixed-sample test cannot be looked at early; a test that averages minutes or dollars cannot be certified at all. The two results of this chapter say what can.

## 6.2 Ville's inequality, and tests as bets — Ville (1939); Shafer and Vovk (2019); Ramdas, Grünwald, Vovk and Shafer (2023)

**Result** (theorem). Let (*E*ₜ) be a non-negative supermartingale under a null hypothesis H₀, with *E*₀ = 1. Then for every *c* ≥ 1, P(supₜ *E*ₜ ≥ *c*) ≤ 1/*c*. The bound is on the supremum, so it holds at every stopping time, including the time at which someone decided to look: *E*ₜ ≥ 1/α is a rejection of H₀ at level α whenever it is observed. The game-theoretic reading is that *E*ₜ is the wealth of a bettor who starts with one unit and bets against H₀ without ever risking bankruptcy; a test is a betting strategy, wealth is evidence, and the only discipline is that each bet be *predictable* — decided from the past before the outcome it bets on is seen.

**What it forces.** Every promotion test is a wealth process; every window is a maximum, not a term; the threshold is 1/α and nothing else; and nothing about a bet may be chosen with knowledge of the outcome it bets on.

**Mechanism — liveness.** For items *Y*ᵢ ∈ {0, 1} and the null that an item is completed without the sovereign's hand no more often than under the predecessor, E[*Y*ᵢ | past] ≤ *p*₀:

  *E*ₜ = ∏ᵢ≤ₜ (1 + λᵢ(*Y*ᵢ − *p*₀)),  λᵢ = max(0, (q̂ᵢ − *p*₀) / (*p*₀(1 − *p*₀))),  q̂ᵢ = (*s*ᵢ + 1)/(*n*ᵢ + 2),

with q̂ᵢ the Laplace estimate over the statistic's outcomes since the layer's first window [CHARTER A4.3]. Because q̂ᵢ < 1, λᵢ < 1/*p*₀ with no further constant; each factor is positive and, under the null, has conditional expectation at most one; so *E*ₜ is a test supermartingale and *E*ₜ ≥ 20 is a level-0.05 rejection at any stopping time. *p*₀ is committed before the window opens, taken from the predecessor's series, and never estimated from the window it judges [A4.2; BRIEF-C1b §Liveness: *p*₀ = 6/11, with its provenance].

**Mechanism — value.** Comparing two forecasters is a bet on a bounded difference. With *D*ᵢ = (the incumbent's log-loss − the challenger's) on event *i*, positive when the challenger did better and bounded by *B* = ln 999 under per-mille clipping,

  *E*ₜ = ∏ᵢ≤ₜ (1 + λᵢ *D*ᵢ / *B*),  λᵢ = min(max(0, *m*₁ᵢ/*m*₂ᵢ), 1 − 1/(*n*ᵢ + 2)),

where *m*₁ᵢ and *m*₂ᵢ are the mean of *D*ⱼ/*B* and of (*D*ⱼ/*B*)² over the prior events together with two pseudo-items at ±*B* [CHARTER A4.4; BRIEF-C2a §The statistic]. λᵢ ∈ [0, 1) and is predictable; under E[*D*ᵢ | past] ≤ 0 — the aggregate is no better than the base rate — the process is a test supermartingale. The exponentiated sum of score differences, which is *not* a supermartingale under that null, is reported as a diagnostic and gates nothing.

**Mechanism — one book.** The wealth is never reset: a window that fails is followed by one that continues the same product under the same null, "so Ville's inequality then holds for the whole sequence at the layer's α" [CHARTER A4.1]. A window ends at the earlier of its stated end and the sovereign's `promote`, which may be entered only once every pre-stated criterion holds on the current prefix [CHARTER A5.1]; the stated end is the `resolves_by` of the window's promotion forecast, entered before it opens [A5.2].

**Misapplied if.** A stake is set with knowledge of its outcome; *p*₀ is moved after the window opens; or the wealth is reset at a new window, which is *k* draws at one bound. The last is the defect counsel's literature check found in the charter's original §6 and that forced amendment A4 [`transcripts/LITERATURE-20261026.md` item 2; seqs 66–67]; the clerk's reviewer pinned the second — `wealth_arithmetic`'s mutant is "*p*₀ re-estimated from the sequence" [BRIEF-C1b §Pins].

## 6.3 Unbounded means cannot be certified — Bahadur and Savage (1956)

**Result** (theorem). In the family of all distributions on the real line with a finite mean, no test of the hypothesis that the mean takes a given value has power exceeding its size against any alternative. A distribution can carry an arbitrarily small probability of an arbitrarily large value, so the mean is dominated by what the sample almost never sees. The result disappears for bounded variables.

**What it forces.** The quantities an operator most wants to see fall — minutes to merge, dollars per window, repairs per merge — are unbounded, and no procedure can certify that their mean is small. So the court tests only bounded outcomes and reports the rest as what they are: numbers, not evidence.

**Mechanism.** Both statistics of §6.2 are bounded by construction: *Y*ᵢ ∈ {0, 1}; *D*ᵢ ∈ [−*B*, *B*]. The charter says the rest aloud: "Unbounded quantities (repairs per merge, minutes) are reported and never tested" [CHARTER §6]. Repairs per merge — the number the whole programme exists to drive down — appears in every weekly acts table [`claude/acts-weekly.md`] and in no test.

**Misapplied if.** Anyone proposes "*E* ≥ 20 on mean latency". Or the book claims the acts tables as evidence of the kind Ville gives; they are a classifier's counts over GitHub's record and are reported with that label.

## 6.4 The record so far

The rule has bitten once, in the only direction it can. The clerk's window opened at seq 188 with *p*₀ = 6/11 committed; nine items followed, every one *Y* = 1; the stakes rose with the Laplace estimate — 0, 22/45, 33/40, 77/75, 209/180, 44/35, 319/240, 187/135, 143/100 — and the wealth after the ninth stood at 214358881/8398080 ≈ 25.52 [`status.py --subject C1b --as-of 2026-11-01T11:31:58Z --runs transcripts/evidence/runs-tests-20261101b.json --acts transcripts/evidence/acts-20261101.csv --json @6ebea1a`, `items`: seqs 215, 268, 276, 284, 292, 306, 314, 320, 332, each with its stake and running *E* as exact fractions]. The sovereign's `promote` was entered at seq 337, twenty-four hours and fifty minutes after the opening, with almost thirteen of the window's fourteen days unused. The same process continues under the same null into the next layer: forty items in, with no reset, it stood at about 1.44 on 3 November [`status.py --subject C2a --runs transcripts/evidence/runs-tests-20261101b.json @6b800e14`] — the honest shape of a sequential test that has stopped winning for the moment, and will either climb or not.

The value process is where the court's claim about its helpers is decided, and the author cannot yet recompute it from the clone: the statistic gates events on a verified tests run that is not committed under `transcripts/evidence/` [`plan.md` F2]. The number in this section's second draft will carry the committed file's name and the exact invocation.

## 6.5 What this chapter leaves open

We can say when a layer has worked, for an operator who looks whenever he likes. We cannot yet say *which* helper should be invited to the next task. The scores exist; a rule for turning them into a choice does not — and a rule that named a model would be an authority, which chapter 1 forbade. Chapter 7 makes the choice a statistic with a regret bound.

## 6.6 What would show this chapter wrong

A λ entered after its outcome, a *p*₀ taken from its own window, a wealth reset — any of these on the record. A bounded statistic that turns out not to be: a per-mille probability outside 1–999 would break *B*, and the kernel refuses it as `schema` [SPEC §5]. A liveness crossing that the acts table contradicts — items counted as *Y* = 1 while the operator's hand was on them off the log; the W4 line and the acts file exist so that this is seen. And the C2a value process failing its window, which would not show the chapter wrong but the helpers worth less than the base rate; the book must then say so, as chapter 13 will.
