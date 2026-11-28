# Referee report on draft 1 — round 1 (the claim session reviewing its own draft as an arXiv/ML-venue referee would)

*25 November 2026. A self-review: the outside cold read, by another model family, comes after this round. Each point carries the fix taken in draft 2.*

**Summary.** The paper argues that the institution governing a self-modifying agent is forced, piece by piece, by results in computability, probability, control and law. It states six guarantees of a reference design and proposes that the law be built before the agent and tested on its builders. The forcing analysis and the propositions are the contribution; the implementation is evidence only that the design can be built.

**Recommendation on draft 1:** major revision. Two technical points are wrong or under-stated (M1, M2). The novelty claims need sharper definitions (M3, M4). One fact about the implementation is overclaimed (m5), and one is omitted (M6).

## Major

- **M1. The value null depends on the filtration, and the natural null needs one bet per sitting.** Proposition 3 conditions on $\mathcal F_{i-1}$, which in resolution order includes outcomes realised at the same moment as event $i$. The null one wants is: no advantage *given what was known when the forecasts were fixed*. That null does not imply the per-event condition. When events forecast at one sitting are dependent, the per-event e-process can reject without any forecasting skill. Henzi & Ziegel (2021) give the remedy: bet once per block (or lag class) on the block's mean score difference. The book's open issue #36 records an unreviewed analysis in which this construction takes $E$ to single digits. *Fix:* Proposition 3 is restated for blocks, with its assumption explicit. A remark says that the reference implementation bets per event, so its reported value figures are not evidence of skill.
- **M2. Proposition 1(b) is misstated.** As written it is not the binding property of a hash chain. *Fix:* if a log has the published head hash $h$, then under collision resistance it equals $L$ entry by entry.
- **M3. "The institution is promoted" is never defined.** A sceptical reader will say that a layer's promotion is just a gated code change. *Fix:* §4.3 now defines a layer and a window, and says what makes the hypothesis about the institution rather than about an edit:
  - the statistic is computed over the live record of all parties' acts and claims in the window;
  - the act that follows is a grant of powers;
  - the operator's `promote` is itself refused unless the evaluator in force finds every criterion met.
- **M4. Law as a fold looks like event sourcing (Regimes).** *Fix:* §4.1 says what is new. The validity predicate is parameterised by state folded from the log — keys, charter in force, trusted base — so the law itself changes only by entries and binds only forward. An event-sourced runtime projects state from a log. It does not make the admissibility of the next entry a function of the law in force before it.
- **M5. The argument that the builders must be the first subjects is informal, and meets an obvious objection: builders are not adversaries.** *Fix:* §5.2 says what testing on builders does and does not establish. It surfaces cases and nulls, and shows the law can be lived under. Adversarial testing is a separate obligation: the charter requires a simulator of named attacks before any model touches a layer (CHARTER §6), and C3 will need a red team in the sense of Greenblatt et al.
- **M6. One scored stream is operated by the operator.** `world.renavon` resolves from the modification time of a page on the operator's own data marketplace, and the operator holds forecast power. This is the case row A.22 warns about, and the book says so (App. A, A.22). *Fix:* stated in §8.

## Minor

- **m1.** Proposition 4(b): the false-crossing probability with independent restarts is $1-(1-\alpha)^k$, about $k\alpha$ when $k\alpha$ is small. Reworded.
- **m2.** Proposition 6(c): finite agreement does not fix behaviour elsewhere, and equivalence is undecidable in general. Reworded.
- **m3.** Table 1, Hart row: the three secondary rules are held by the core — kernel, judge and key entries — not by the kernel alone (CHARTER A1.1). Fixed.
- **m4.** Table 1: pins pair the kernel's rules and the judge's grounds, not "every rule". Fixed.
- **m5.** Table 1, Waismann row: the book says the mechanism for fixing a claim's text at the forecast's position is "None in code" (App. A, A.19). Draft 1 implied that it exists. Now marked as forced but not built.
- **m6.** §6: the safety survey states "utility does not authorize promotion" as a takeaway, not a finding. Reworded.
- **m7.** Terms. "Operator" is now used throughout and defined once as the principal and owner of the utility.
- **m8.** arXiv limits the abstract field to 1,920 characters. The abstract is shortened to fit.
- **m9.** Length: about 7,300 words of body is too long. Trimmed towards 6,000.
- **m10.** Henzi & Ziegel (2021) added. Why the logarithmic score in particular is now said in one sentence (the mixture is then itself a forecaster, with regret $\ln K$ and no tuning).
- **m11.** References: verified against Crossref and arXiv on 25 November. The daggers are removed where verified. Classic books without DOIs are given in standard form.
- **m12.** A figure of layers and loops would help a reader. Planned for the LaTeX version.

## Round 3: referee pass on draft 3 (25 November)

Read as a referee for arXiv cs.AI and an ML or AI-safety venue.

**Major**
- **R3-M1. Prop. 3(b) bounded the wrong quantity.** The regret bound held for the mixture's *joint* forecast, but the test statistic used the *marginals* $q_i$. When members disagree within a block, the marginals can lose more than $\ln K$. *Fixed:* $\bar D_m$ is now built from the joint forecast $Q_m$, which reduces to the charter's per-event difference for blocks of one. Part (b) is now a pathwise bound on the tested quantity, with a telescoping proof.
- **R3-M2. The Remark asserted invalidity without showing it.** *Fixed:* there is now a worked example with a seeded simulation (`sim_filtration.py`, an arXiv ancillary file). Under a null in which the aggregate is strictly worse than the base rate, per-event betting crosses $1/\alpha$ in 13% of runs with 20 shared-outcome events per sitting, and in 50% with 50. Block betting never crosses, and nor does the per-event form when outcomes are independent. The implementation's streams do resolve in batches (seqs 550–563).
- **R3-M3. The operator was both "scored" (§4.2) and "the one party not scored" (§4.5).** *Fixed:* his forecasts are scored; his acts are confined and priced. The wording in §3.2, §4.5 and §5.3 now agrees.

**Minor**
- The thesis said "exactly where", which claims sufficiency. It now says "only where".
- "Leave little choice" contradicted §3's minimality-not-uniqueness. It now reads "fix what the institution must contain, though not how each part is built".
- Gödel was named without a citation; Gödel (1931) is added.
- Henzi & Ziegel is cited as 2022, matching its volume.
- The reference list is re-sorted; Freund & Schapire is dropped as uncited.
- Liveness items are now indexed by realisation order, and simultaneous items form blocks.
- The abstract is now plain prose, as arXiv's abstract field requires.
- The bullet-heavy passages in §§1, 2, 3.1, 4.1, 5.2, 6, 7 and 8 are now prose; a referee would have called the draft slide-like.
- Figure 1, a diagram of the construction, is added to the LaTeX build.
- A duplicated comparison with per-edit gates is cut from §4.3.

**Remaining, for the outside reader to judge**
- Length: about 14 pages of body and 4 of references at 11pt on A4. The brief asked for 8–12. The next cut would fall on §3.2 and §6.
- Whether the propositions are too easy for a research venue. Props 3–5 carry the content; 1, 2 and 6 are definitional, and the paper says so.
