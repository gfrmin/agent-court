# Cold read 6 of the claim paper: report and disposition

- **Reader:** `google/gemini-4-argon`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1369, filed under Guy's standing yes. The session ran from 03:58Z to 04:18Z on 26 November.
- **Text read:** draft 11, at `5f3022e`.
- **Verdict:** minor revision. The reader found the propositions and Lean statements sound and reproduced every figure in §6. The remaining points were factual or provenance corrections.
- **Drafts 12 and 13 answer it.** Draft 12, written while the read ran, already held the paper to its abstract on Guy's instruction. It cut the Waismann and Crawford–Ostrom rows, the regress catalogue and the minimality section. Draft 13 makes the remaining corrections. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What drafts 12 and 13 do |
|---|---|
| §2 "fix the shape"; Löb stated too broadly | Now "bear on". Löb is now stated with its condition: adoption on a proof in the agent's own consistent theory. "This obstructs proof-based self-trust, not every form of trust." |
| Rules of conduct are not built (Table 1 Hart row; §5.2) | The Hart row says "are to enter only from cases, and none has yet (§8)". §5.2 says "should enter". |
| Not every rule has a mutant (Crawford–Ostrom row) | The row is cut (draft 12). §4.4 says "mutant pins", with no universal. |
| Waismann row; the §3.2 regress list | Both cut (draft 12). |
| `transmuted` is missing from the kernel state | Added. Verified at `kernel/check.py` line 16. |
| Provenance and enforcement of kernel2 | Now: written from the specification and its test vectors, by Codex at C0 and Gemini for C1a [REPORT §8; `kernel2/NOTES.md`]. The judge refuses on `checker_drift` [SPEC §10, item 5], and CI runs 300 simulated logs through both kernels. |
| The ~80 non-stream proposals | Now "about 620 of the 702 proposals … the other 80 or so are reads and reviews, code and pins, fixes, and other forecasts". The 702 and 622 are recounted from titles; no finer split is claimed. |
| Table 2's nine repairs | Now "nine rows off the record that a classifier labels as repairs". |
| C2a′'s ratio at the veto | Now 320 to 1,296 at seq 7180, and 459 to 1,786 by seq 7809. Both were recomputed with `judge/status.py --subject C2a --as-of` at `e580b64`. |
| How counsel's and the operator's forecasts are scored | Now: they are scored by `tools/entry.py` `score`; none is a value event of §6, where both count as abstentions. |
| SPEC also replays the commits after T | Stated, with $R^+$; Proposition 6(a) and (c) changed to match. |
| The Lean note on 4(b) | Now: the union bound on measures, and the independent case only as an inequality between real numbers. |

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

A self-modifying agent can be trusted only as far as it is governed by an institution outside its reach that is built first, imposed first on its builders, and granted authority layer by layer only through valid sequential tests on its own signed record. That record must be able to expose flaws in the institution's own tests and baselines — as demonstrated when a block-valid value test replaces the implementation's invalid per-event test and reveals that its apparent predictive advantage came entirely from a pooled baseline rather than per-dataset skill.

**Does the abstract state it, and does the body deliver it?** Yes to both. The abstract (line 15) follows the four-sentence structure fixed in `ABSTRACT-FIRST.md` (problem, theoretical motivation, institutional construction with six propositions and the block-valid correction, and the negative empirical finding against a per-dataset base rate). The body delivers the construction, the six propositions with their machine-checked core, the filtration counterexample and simulation (§4), the build-order argument (§5), and the retrospective recomputation on `renavondata/jack` (§6).

**What in the body does not serve it:**
- **Parts of Table 1 and §3.2 (lines 65–92, 100–104):** Once §3 softens the classical references from deductive necessities to design motivations and analogies, carrying seventeen literature rows (including the unbuilt Waismann row on line 88 and the unbuilt primary-rule clause in the Hart row on line 85) plus the seven-place regress taxonomy in §3.2 dilutes the paper's sharp contributions in §§4–6.
- **Residual necessity phrasing in §2 (lines 50, 52):** Line 50 still says "three results fix the shape of what governs the object", which sits awkwardly next to §3's more careful "What the results motivate".

---

## 2. Correctness

All line numbers below refer to `draft.md` at commit `5f3022e06d035cd19170af48be662b5f8e175252`.

- **Proposition 1 (prospectivity, lines 140–149).** *Correct.*
  - Part (a): Because $S_i$ is a pure fold of $e_0, \dots, e_{i-1}$ and $V(S_i, e_i)$ depends only on $(S_i, e_i)$, appending $M$ to $L$ cannot alter the verdict on any entry of $L$.
  - Part (b): Requiring entries to be numbered by position from $0$ (`seq` $= i$) closes the proper-suffix counterexample. Walking backward from the last lines of $L$ and $L^* \neq L$ (which share hash $h$), either two unequal lines share a hash at some step, or one log is a proper suffix of the other; in the latter case, the step before the shorter log's genesis entry pairs two identical lines whose `parent` fields agree, so the shorter log's genesis line (`seq` $= 0$) and the longer log's corresponding line (`seq` $> 0$) differ and share a SHA-256 hash.

- **Proposition 2 (propriety; no self-judgement, lines 158–165).** *Correct.*
  - Part (a): For $\pi \in (0,1)$, $g(p) = \pi\ln p + (1-\pi)\ln(1-p)$ has $g'(p) = (\pi - p)/(p(1-p))$ and $g''(p) = -\pi/p^2 - (1-\pi)/(1-p)^2 < 0$, so $g$ is strictly concave on $(0,1)$ with unique maximum at $p = \pi$. Because $g$ is strictly increasing on $(0, \pi]$ and strictly decreasing on $[\pi, 1)$, its maximum on the per-mille grid $\{1,\dots,999\}/1000$ is attained at one (or, by intermediate value, at most two tied) grid points adjacent to $\pi$, or at the nearer boundary ($0.001$ or $0.999$) when $\pi$ lies outside $[0.001, 0.999]$.
  - Part (b): Matches `SPEC §8` step 8a and `kernel/check.py:82–83` (`state.forecasts[body["forecast"]] == e["proposer"]`), checked after step 8 verifies that `e["proposer"]` equals the signing key's `principal`. The caveats on performativity, collusion, and nonlinear downstream rewards (lines 166–168) are accurate.

- **Proposition 3 (value, lines 180–206).** *Correct.*
  - Under per-mille clipping $p_{k,i}, b_i \in [10^{-3}, 1-10^{-3}]$, for any non-empty resolved subset $R_m \subseteq B_m$ and any outcome vector $y \in \{0,1\}^{R_m}$, every member's product likelihood $\prod_{i \in R_m} p_{k,i}(y_i)$ and their convex combination $Q_m(y)$ lie in $[10^{-3|R_m|}, (999/1000)^{|R_m|}]$. Dividing $\ln Q_m(Y_{R_m}) - \sum_{i \in R_m} \ln b_i(Y_i)$ by $|R_m|\ln 999$ yields $\bar D_m \in [-1, 1]$ (and $\bar D_m = 0$ when $R_m = \varnothing$, contributing factor $1$).
  - Part (a): Under assumption (A), $\lambda_m \in [0, 1 - 1/(m+1)] \subset [0,1)$ is $\mathcal G_{m-1}$-measurable and $1 + \lambda_m \bar D_m > 0$. Under $H_0^{\mathrm{val}}: \mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 0$ (stated for the resolved-subset statistic on line 180), $\mathbb E[W_m \mid \mathcal G_{m-1}] = W_{m-1}(1 + \lambda_m \mathbb E[\bar D_m \mid \mathcal G_{m-1}]) \le W_{m-1}$, so $W_t$ is a non-negative supermartingale with $W_0 = 1$, and Ville's inequality gives $\Pr(\sup_t W_t \ge 1/\alpha) \le \alpha$. When sittings are split online into lag classes $\ell = 1, 2, \dots$ with pre-fixed thresholds $\ell(\ell+1)/\alpha$, the union bound gives $\sum_{\ell \ge 1} \alpha/[\ell(\ell+1)] = \alpha$.
  - Part (b): With uniform prior $w_{k,1} = 1/K$ and posterior updates $w_{k,m+1} = w_{k,m} \prod_{i \in R_m} p_{k,i}(Y_i) / Q_m(Y_{R_m})$ within a single non-overlapping sequence, $\prod_{m \le t} Q_m(Y_{R_m}) = \frac{1}{K}\sum_{k=1}^K \prod_{m \le t} \prod_{i \in R_m} p_{k,i}(Y_i) \ge \frac{1}{K}\max_k \prod_{m \le t} \prod_{i \in R_m} p_{k,i}(Y_i)$. Taking logs and subtracting $\sum_{m \le t}\sum_{i \in R_m} \ln b_i(Y_i)$ gives the first inequality, and inclusion of the base-rate forecaster in the roster gives $\ge -\ln K$.

- **Remark and Example in §4.3 (lines 209–212).** *Correct and reproduced.*
  - The Remark accurately identifies why per-event betting in resolution order fails when simultaneous outcomes are dependent under a forecast-time null: later bets within a sitting condition on earlier outcomes of the same sitting, and even with frozen stakes within a sitting, a product of correlated factors with conditional mean $\le 1$ need not have expected product $\le 1$. It also correctly notes that a Bayes mixture of product forecasts can gain joint log-score advantage over an independent base-rate product by capturing within-sitting dependence even without marginal superiority, whereas forming the block forecast as the product of marginals $\prod_{i \in B_m} q_i(Y_i)$ would lose Proposition 3(b)'s $\ln K$ regret bound.
  - In the Example (line 211), with $n$ events sharing $Y \sim \mathrm{Bern}(1/2)$, $b_i = 1/2$, and $q \in \{0.95, 0.05\}$ chosen by an independent fair coin, $\bar D_m = D_i = \ln(2q(Y))/\ln 999$ has conditional expectation $\frac{1}{2}(\ln 1.9 + \ln 0.1)/\ln 999 \approx -0.1202 < 0$. Running `sim_filtration.py` reproduces every figure in line 211:
    - Default (`n=20, d=0.45, blocks=300, runs=4000, alpha=0.05`): per-event crossing rate `0.1325` (13%), block crossing rate `0.0000`.
    - `50 0.45 200 2000`: per-event crossing rate `0.5035` (50%), block crossing rate `0.0000`.
    - `--independent` (for both $n=20$ and $n=50$): per-event crossing rate `0.0000`.
    - `--roster 20 300 2000` (kept in the script for reference and rightly omitted from the paper's text): `0.2850` implementation form vs. `0.0000` block form; as the script's docstring now notes, the 3-member roster `(0.5, 0.95, 0.05)` is not a true null for the joint score because at block 1, $Q_1(Y) = \frac{1}{3}(0.5^{20} + 0.95^{20} + 0.05^{20}) \approx 0.1195 \gg 0.5^{20}$, giving initial expected $\bar D_1 \approx +0.085 > 0$.

- **Proposition 4 (liveness, with wealth carried across windows, lines 219–227).** *Correct.*
  - Part (a): Since $0 \le s_j \le n_j$, $\hat q_j = (s_j+1)/(n_j+2) \in (0,1)$, so $\lambda_j = \max(0, (\hat q_j - p_0)/(p_0(1-p_0))) \in [0, 1/p_0)$. For $Y_j \in [0,1]$ (or batch average $\bar Y_j \in [0,1]$), $1 + \lambda_j(Y_j - p_0) \ge 1 - \lambda_j p_0 > 0$ and $\mathbb E[1 + \lambda_j(Y_j - p_0) \mid \mathcal F_{j-1}] \le 1$ under $H_0^{\mathrm{live}}$. Carrying wealth across windows makes all window boundaries stopping times of a single non-negative supermartingale $M_t$, so Ville's inequality bounds the lifetime false-crossing probability by $\alpha$.
  - Part (b): For $k$ restarted tests with false-crossing probabilities $r_j \le \alpha$, independence gives $1 - \prod_{j=1}^k (1 - r_j) \le 1 - (1-\alpha)^k$ (attained when $r_j = \alpha$), and the general union bound gives $\sum_{j=1}^k r_j \le k\alpha$.

- **Proposition 5 (conjunctive promotion, lines 233–235).** *Correct.*
  - Since promotion at prefix $t$ requires both $W_t \ge 1/\alpha$ and $M_t \ge 1/\alpha$, the event that promotion ever occurs is contained in $\{\sup_t W_t \ge 1/\alpha\} \cap \{\sup_t M_t \ge 1/\alpha\}$. Under $H_0^{\mathrm{val}} \cup H_0^{\mathrm{live}}$, at least one of the two crossing events has probability at most $\alpha$.

- **Proposition 6 (replay-bound change, lines 249–260).** *Correct relative to the paper's stated admission rule.*
  - Parts (a)–(c) follow immediately from the definitions in lines 243–247 and `SPEC §10` item 15. (See §6 below on one difference between lines 243–247 and `SPEC §10` regarding commits after $T$.)

---

## 3. The Lean files

I inspected `lean/README.md` and all seven files under `lean/Claimproofs/`. As permitted, I did not run `lake build`; no file contains `sorry` or non-standard axioms.

1. **`HashChain.lean` (`Claim.collision_of_ne`) $\leftrightarrow$ Proposition 1(b):**
   - *Comparison:* Matches the mathematical core of Prop. 1(b). Logs are formalised backwards as non-empty lists `x :: xs : List α` with abstract functions `hash parent : α → β` and `seq : α → ℕ`. `RevLinked` requires `parent x = hash y` for adjacent elements (leaving genesis's `parent` unconstrained, which slightly weakens the hypothesis and strengthens the lemma), and `RevNumbered` requires `seq x = rest.length`. It proves that if `x :: xs ≠ x' :: xs'` and `hash x = hash x'`, then `∃ a b, a ≠ b ∧ hash a = hash b`.
   - *Differences:* Canonical JSON formatting, SHA-256, and the complexity-theoretic adversary phrasing are informal context.

2. **`Propriety.lean` (`Claim.log_score_proper`, `Claim.log_score_strict`) $\leftrightarrow$ Proposition 2(a):**
   - *Comparison:* Proves that for $\pi, p \in (0,1)$, `expScore π p ≤ expScore π π`, with strict inequality when `p ≠ π`, using `Real.log_le_sub_one_of_pos` ($\ln(x) \le x - 1$).
   - *Differences:* Does not prove strict concavity ($g'' < 0$) or the per-mille grid consequence. Both omissions are explicitly disclosed in `draft.md` (lines 118–119) and `lean/README.md`.

3. **`Mixture.lean` (`Claim.prod_Q`, `Claim.regret`, `Claim.regret_base`) $\leftrightarrow$ Proposition 3(b):**
   - *Comparison:* Takes abstract block likelihoods `P : Fin K → ℕ → ℝ` with `0 < K` and `∀ k m, 0 < P k m`, defines uniform-prior Bayes mixture block probabilities `Q P T`, proves the telescoping product `∏ m ∈ range T, Q P m = S P T / K` (`prod_Q`), proves `∀ k, ∑ m ∈ range T, log (P k m) - log K ≤ ∑ m ∈ range T, log (Q P m)` (`regret`), and proves that if `P k₀ = B` then `-log K ≤ ∑ m ∈ range T, (log (Q P m) - log (B m))` (`regret_base`).
   - *Differences:* Positivity `0 < P k m` is weaker (more general) than clipped per-mille product probabilities. The identification of `P k m` with $\prod_{i \in B_m} p_{k,i}(Y_i)$ and of $\ln Q_m - \ln B_m$ with $|B_m|\ln 999\,\bar D_m$, as well as combining the universally quantified `regret` into a single `Finset.sup'` ($\max_k$) expression, are left as informal bridges (disclosed at lines 118–120).

4. **`Ville.lean` (`Claim.ville_finite`) & `Wealth.lean` (`Claim.wealth_supermartingale`, `Claim.wealth_level`, `Claim.value_factor`, `Claim.liveness_factor`) $\leftrightarrow$ Propositions 3(a) and 4(a):**
   - *Comparison:* `ville_finite` derives the finite-horizon maximal inequality $\varepsilon \cdot \mu\{\omega \mid \varepsilon \le \max_{k \le n} W_k(\omega)\} \le \mathbb E[W_0]$ for any non-negative supermartingale `W` from Mathlib's optional stopping theorem (`expected_stoppedValue_mono` applied to the submartingale `-W` and `hittingBtwn`). `wealth_supermartingale` and `wealth_level` prove that `wealth L D` is a non-negative supermartingale satisfying the finite-horizon level bound whenever `0 ≤ L ≤ M`, `|D| ≤ B`, `0 ≤ 1 + L * D ≤ C`, `D n` is `𝒢 n`-strongly measurable, `L (n+1)` is `𝒢 n`-strongly measurable (predictable), and `μ[D (n+1) | 𝒢 n] ≤ᵐ[μ] 0`. `value_factor` and `liveness_factor` verify the factor bounds `[0, 2]` and `[0, 1/p₀]` for scalar inputs satisfying `0 ≤ l ≤ 1, |d| ≤ 1` and `0 < p₀ < 1, 0 ≤ y ≤ 1, 0 ≤ l ≤ 1/p₀`.
   - *Differences:* The specific plug-in stake rules (lines 193 and 217) and their strict upper bounds ($\lambda_m < 1$, $\lambda_j < 1/p_0$) are abstracted into the bounded predictable process `L`, and `wealth_level` proves the bound for every finite horizon $n$ rather than $\sup_{t \in \mathbb N}$ (which follows by monotone continuity of measure). All of these are accurately disclosed in lines 118–121 and `lean/README.md`.

5. **`Restart.lean` (`Claim.restart_independent`, `Claim.restart_union`) $\leftrightarrow$ Proposition 4(b):**
   - *Comparison:* `restart_union` proves the measure-theoretic union bound $\mu(\bigcup_{j \in \mathrm{Fin}\,k} A_j) \le k\alpha$ from $\forall j, \mu(A_j) \le \alpha$. `restart_independent` proves the real algebraic inequality $1 - \prod_{j \in \mathrm{Fin}\,k} (1 - r_j) \le 1 - (1 - \alpha)^k$ under $\forall j, r_j \le \alpha$ and $\alpha \le 1$.
   - *Differences:* `restart_independent` is a statement about real numbers `r : Fin k → ℝ`, not about independent events in a probability space (it does not formalise independence or $\mu(\bigcup_j A_j) = 1 - \prod_j (1 - \mu(A_j))$). `lean/README.md` states this clearly; line 118 of `draft.md` says only "it proves the inequality, not that independent windows attain it" and should match the README.

6. **`Conjunctive.lean` (`Claim.conjunctive_promotion`) $\leftrightarrow$ Proposition 5:**
   - *Comparison:* Proves that if `Promote ⊆ CrossW`, `Promote ⊆ CrossM`, and `μ CrossW ≤ α ∨ μ CrossM ≤ α`, then `μ Promote ≤ α`.
   - *Differences:* Takes the component crossing bounds as hypotheses rather than instantiating them with `wealth_level`, as disclosed at line 118.

---

## 4. The recomputation

Running `curl -sL $U/block_on_log.py | python3 - --rev e580b64` reproduces every number in §6 (lines 332–346):
- **Selection and sittings:** `2820` implementation-selected resolved value events (`E = 1.51983e+60`), with `2795` forecasts by `reviewer` and `12` by `builder` (`guy`, `counsel`, and `base` are on the opening roster with 0 issued value forecasts). Observed to `2026-11-25T11:05:35Z` (seq 7809), there are `476` completed sittings and `4` pending sittings, containing `2803` member events in completed sittings, of which `170` expired unresolved at their deadline (`168` resolved only after their deadline). `19` resolved events had no forecast before their cutoff and are excluded from sitting membership.
- **Lag classes:** `5` classes with total sittings `[216, 196, 48, 16, 4]` and scored (completed) sittings `[215, 195, 47, 15, 4]`, tested against thresholds $\ell(\ell+1)/\alpha = [40, 120, 240, 400, 600]$ at $\alpha = 0.05$.
- **Pooled by event type:** Final wealth by class `['1.993e+04', '1.109e+04', '3.009', '1.159', '1.022']`, running maxima `['1.993e+04', '1.19e+04', '3.009', '1.159', '1.022']`; classes 1 and 2 cross their thresholds (`40` and `120`). The two ablations give `2.492e+58` (per-event with stakes, weights, and base rates frozen before each cutoff) and `1.739e+10` (single block process without lag-class splitting).
- **Kept per dataset:** Final wealth `['0.9989', '0.9998', '1', '1', '1']`, running maxima `['1', '1', '1', '1', '1']`; no class ever exceeds 1.

**Is the method in `block_on_log.py` valid as §4.3 and §6 describe it?** Yes.
1. *Cutoff-time membership and deadlines:* An event $k$ enters sitting $c$ (`fkey`, lines 69–76) only if a forecast for $k$ was recorded with timestamp `< c`, and its deadline $d_{\mathrm{deadline}}(k)$ is fixed from those pre-cutoff forecasts.
2. *Stopping-time completion and online lag-class assignment:* Each member event's completion time is $\tau_e = \min(t_{\mathrm{res}}(e), d_{\mathrm{deadline}}(e))$, which is a stopping time with respect to the log's timestamp filtration because for any later cutoff $c' > c$, $\{\tau_e < c'\} = \{t_{\mathrm{res}}(e) < c' \text{ and } t_{\mathrm{res}}(e) \le d_{\mathrm{deadline}}(e)\} \cup \{d_{\mathrm{deadline}}(e) < c'\}$ depends only on entries recorded before $c'$. Consequently, sitting $c$'s completion time $\tau(B_m) = \max_{e \in B_m} \tau_e$ is also a stopping time, and the greedy assignment `if d < c:` (lines 113–121, run over all sittings `all_order` including those still pending at $T_{\mathrm{obs}}$) depends only on whether the last sitting in class $i$ had already completed strictly before $c$. Furthermore, within each lag class, only the final sitting can be pending at $T_{\mathrm{obs}}$ (since any earlier sitting in the class completed before the next sitting's cutoff $\le T_{\mathrm{obs}}$), so the scored sittings in every class form an unbroken prefix.
3. *Pre-cutoff predictability:* Base rates use `bisect_left(times, c)` (strictly `< c`), mixture weights update only over `done_events` with `done < c`, and stakes $\lambda_m$ update only from prior sittings in the same lag class. As line 336 accurately notes, because mixture weights pool resolved events across lag classes and from partly resolved sittings, Proposition 3(b)'s telescoping regret bound does not apply, while Proposition 3(a)'s supermartingale validity holds.

---

## 5. The revisions

The fifth referee's points (`REVIEW-cold-5.md`) were resolved in Draft 11 as follows:

1. **Rice, Löb and Goodhart framed as necessities (Report §6.1, Priority 1):** *Resolved in substance.* The abstract (line 15) now says "limit what … can establish"; §3 is titled "What the results motivate" with Table 1 columns "Motivates" and "Response"; line 65 calls the rows "design arguments" and notes that "several rows are analogies or design commitments rather than consequences"; line 52 notes that proofs remain possible for restricted languages; and line 404 says "We have argued". (One residual phrasing remains at lines 50 and 52; see §6 below.)
2. **Uniqueness and Goodhart-immunity of proper scores (Report §6.2):** *Resolved.* Line 53 now specifies "Under expected-score incentives, a proper score can be held fixed at every level without rewarding misreport" and adds that a weak comparator, omitted objective, or strategic participation can still be exploited.
3. **Skalse et al.'s policy-space scope (Report §6.3):** *Resolved.* Line 80 now specifies "for unrestricted stochastic policies, no non-trivial proxy is unhackable".
4. **Bahadur–Savage tail condition (Report §6.4):** *Resolved.* Line 82 now specifies "Without tail restrictions, small means of unbounded variables cannot be certified".
5. **Conant–Ashby, requisite variety, and the seven-stop regress (Report §6.5, Priority 1):** *Resolved.* Line 65 qualifies Table 1's rows as design commitments/analogies, and line 102 states that each regress is stopped "by engineering choice".
6. **Wheeler's diverse double-compiling and Arrow–Fisher / Henry option value (Report §6.6, Priority 1):** *Resolved.* Line 90 distinguishes "(diversity of authors, not diverse double-compiling)" and line 91 says "Irreversible acts merit a hard gate".
7. **Attested vs. recomputed promotion evidence (Report §6.7, Priority 2):** *Resolved.* Line 57 now states the exception: "promotion evidence is checked for presence and hash, not truth, and its contents are attested by the operator [SPEC §10, item 15]."
8. **"Judged once" in Proposition 6(b) (Report §2, §6.8, Priority 3):** *Resolved.* Line 253 now says "assessed with one historical evaluator: the one in force at its `seq`. A later evaluator does not change that verdict, although the current judge drives the assessment and may re-run it."
9. **Scrivens [2026] theorem scope (Report §6.9, Priority 1):** *Resolved.* Lines 229 and 362 now restrict the finite-total-TPR claim to "power-law risk schedules and overlap conditions [Scrivens 2026, Thm. 1]".
10. **Typing and taint exceptions (`window_fixes`) (Report §6.10, Priority 3):** *Resolved.* Lines 270–271 now state that a `fix` naming a failed window is typed as a decision and qualifying fixes lose their taint at the next push.
11. **Nine operator repairs vs. classifier rows under a shared login (Report §6.11, Priority 2):** *Mostly resolved.* Line 330 now says "found nine rows that its classifier labels as repairs under the operator's login. One suffices", though Table 2 (line 325) still says "failed on nine repair rows found off the record" without that qualification.
12. **Record-earned authority and builders' record (Report §6.12, Priority 3):** *Resolved.* Line 297 says "The builders' record is the nearest record that does", and line 306 notes that C0 and `seq 51` granted powers before statistical promotions.
13. **Resolved subset $R_m$ throughout, empty blocks, cutoff-time null, and `--roster` docstring (Report §2, §3, §4, Priority 4):** *Resolved.* Line 180 makes the $R_m$ replacement across $Q_m$, $\bar D_m$, posterior updates, and $|B_m|$ in 3(b), as well as the $R_m = \varnothing$ unit factor and cutoff-conditioned null, explicit. `sim_filtration.py` documents that `--roster` is not a true null for the joint score. (One minor wording gap on Lean's `restart_independent` remains at line 118; see §6.)
14. **Audit information sets and ablation gap wording (Report §6.13, Priority 5):** *Resolved.* Line 336 distinguishes the eligible event sets for weights and base rates, and line 346 notes that "the ablations do not use exactly the same events".
15. **Post-veto counting interval for procedure:object ratio (Report §6.14, Priority 5):** *Resolved.* Line 348 states that `459 to 1,786` counted from `seq 5565` to `seq 7809`, past the veto at `seq 7180`.
16. **Murphy decomposition (Brier vs. log score) and split-$\alpha$ recency (Report §6.15):** *Resolved.* Lines 380 and 384 now state that Murphy's decomposition is for the Brier score (leaving a log-score gate open) and that a split-$\alpha$ process keeps validity while trading power for recency.

---

## 6. Backing

### Claims verified against the implementation (`e580b64`), book (`007a007`), and external sources

I checked the following twenty-four claims directly against `git show e580b64:<path>`, `gfrmin/agent-court` at `007a007`, and the cited literature:

1. **Line 21 (`Zhang et al. 2025`, arXiv:2505.22954v3):** SWE-bench score 20% $\to$ 50% and App. H hallucination-marker removal despite instructions. *Holds.*
2. **Line 21 (`Chen, Zhu & Zheng 2026`, arXiv:2610.27610v1):** Full-text census of 114 RSI studies distinguishing product from process evaluation. *Holds.*
3. **Line 57 (`SPEC §10`, item 15):** Promotion evidence checked for file presence and SHA-256 hash (`transcripts/evidence/`), attested by the operator rather than recomputed. *Holds (`SPEC.md:432–436, 467–470`).*
4. **Line 96 (`Kim et al. 2025`, arXiv:2506.07962v1; `Pato Nogueira et al. 2026`, arXiv:2607.02808v1; `Ron, Baudry & Monperrus 2026`, arXiv:2606.20158v1):** Correlated errors across $>350$ LLMs and correlated failures in LLM N-version programming. *Holds.*
5. **Line 126 & 136 (`SPEC §§1–6, 8–9`):** Seven canonical JSON fields, Ed25519 SSHSIG in namespace `core-entry`, and fourteen closed refusal reason codes. *Holds (`SPEC.md:72–84, 138–145, 295–297`).*
6. **Line 150 (`SPEC §7`, `SPEC §10` item 12):** Amendment entered at seq $a$ requires `activate_at` $k > a$ (`kernel/check.py:71–72`), and no `push` is lawful strictly between $a$ and $k$ (`SPEC.md:405–407`). *Holds.*
7. **Line 152 (Key powers at `seqs 0, 1, 6, 34, 201`; `CHARTER A2.5`):** `builder-1` (`seq 6`) holds `proposal, spec_conflict`; `builder-2` (`seq 34`) adds `forecast, resolution`; `herald-2` (`seq 201`) holds `merge` alone; `guy-master` (`seq 0`) holds `genesis, key, proposal, merge` and at `seq 1` adds `amend, push, decision` (plus `forecast, resolution` at `seq 33`); losing the last `key` power is refused (`kernel/check.py:86–87`). *Holds.*
8. **Line 162 (`SPEC §7`, `SPEC §8` step 8a):** Self-resolution refused by principal (`self_judged`). *Holds (`kernel/check.py:82–83`).*
9. **Line 172 (`seqs 31, 33`; log at `seq 7809`):** `counsel-2` (`seq 31`) and `guy-master` (`seq 33`) hold `forecast`; at `seq 7809` `counsel` has entered 100 forecasts and `guy` 3 (`reviewer` 2,942; `builder` 26). *Holds (with the scoring caveat noted below).*
10. **Line 213 (`judge/value.py:113–135`, `judge/entries.py:resolution_rates`, `seqs 550–563`):** Per-event resolution-order updates of stakes and weights; base rate counts earlier resolutions of the same batch; `seqs 550–563` are 14 `resolution` entries between `12:15:08Z` and `12:15:58Z` on `2026-11-02`. *Holds.*
11. **Line 217 (`judge/status.py:score_items`, log at `seq 7809`):** Of `641` liveness items at `seq 7809`, `190` share a timestamp with another item (`188` of kind `expiry` and `2` of kind `batch`). *Holds.*
12. **Line 229 (`Scrivens 2026, Thm. 1`, arXiv:2603.28650v2):** Under power-law risk schedules $\delta_n = O(n^{-p})$ ($p > 1$) and distribution overlap conditions, classifier gates satisfy $\sum_n \mathrm{TPR}_n < \infty$. *Holds.*
13. **Line 241 & 247 (`SPEC §10` item 15, `judge/judge.py:installing_push`, `tests/promotion_replay_spot.py`, `grant seq 6851`, `push seq 7281`):** Item 15 applies after the installing push (`seq 7281`, authorised by `grant` at `seq 6851`), exempting `seqs 188` and `337`; `tests/promotion_replay_spot.py` replays 3 rows (indices `592, 593, 705`) of the 706-row table `spec/vectors/promotion-replay.json`. *Holds.*
14. **Line 262 (`Iacob et al. 2026, §3.2`, arXiv:2606.26294v3):** RQGM gates evaluator replacement on a replacement criterion and applies selective erasure to utility records that depended on the replaced evaluator. *Holds.*
15. **Line 270–271 (`judge/status.py:window_fixes`, `item_process`):** Repairs taint open writs ($Y=0$), except qualifying `window_fixes` which are typed as decisions and whose taint is cleared at the next `push` (`judge/status.py:111–123, 371–402`). *Holds.*
16. **Line 273 (`transcripts/BRIEF-C2a-draft.md`, criterion 7):** Off-log repairs collected from the platform's event history fail the window if non-zero (`BRIEF-C2a-draft.md:197`). *Holds.*
17. **Line 302 (`Sengupta 2026, §4.4`, arXiv:2607.00871v1):** SEA recommends deploying its statistical gate first and leaves composition guarantees under an endogenous proposer as open conjectures. *Holds.*
18. **Line 302 (Log counts at `seq 7809`):** `seqs 6–8` declared `builder-1`, `reviewer-1`, `counsel-1` on `2026-10-19`; builder and reviewer keys signed `6,621` of `7,810` entries (`2,968` forecasts + `2,951` resolutions = `5,919`, plus `702` proposals, of which `623` are stream proposals). *Holds (except for the description of the remaining 79 proposals; see below).*
19. **Line 316 (`seq 0`, `tools/count_kernel.py`, `REPORT §8.1`):** Genesis `seq 0` is at `2026-10-14T05:41:39Z` with charter SHA-256 `383867d0…`; Python kernel is `450` lines (`check.py` 138 + `log.py` 172 + `sig.py` 140); `REPORT.md:223` records agreement on `100,000` seeded logs and `658,885` prefixes at C0 exit. *Holds.*
20. **Line 324 (Table 2, C1b promotion at `seq 337`):** `judge/status.py:item_process` at `seq 337` gives $M = 214358881/8398080 \approx 25.525$ over 9 items against $p_0 = 6/11$. *Holds.*
21. **Line 325–327 (Table 2, C2a windows):** C2a opened at `seq 367` (`2026-11-01`), fixed at `seq 5563`; C2a′ opened at `seq 5564` (`2026-11-17`), vetoed at `seq 5879` (pre-A6) and ended by veto at `seq 7180` (post-A6, `2026-11-22`); third window grant at `seq 7615` (`2026-11-24`). *Holds.*
22. **Line 348 (`judge/status.py` at `seq 7809`):** C2a′ procedure-to-object count at `seq 7809` is `459` to `1,786` over the `2,245` entries in `seqs 5565..7809`. *Holds.*
23. **Line 380 & 382 (`transcripts/AUDIT-criteria-20261117.md`):** Fixed 6-dataset lookup table (**F**) crosses $E \ge 20$ at event 53 (line 26 of the audit); 9 of 28 audited criteria are classified as `empty` / passable without skill, including liveness (**L**) and ratio padding (**R**) (lines 5, 27–28 of the audit). *Holds.*
24. **Line 392 (`CHARTER A2.1`; log at `seq 7809`):** `log.jsonl` contains `0` entries of type `rule`. *Holds.*

### Statements in `draft.md` that remain unbacked, incomplete, or discrepant with their sources

1. **Lines 50 and 52 — Unqualified architectural-necessity and Löb claims in §2:**
   - *What is said:* Line 50 states "In this setting, three results fix the shape of what governs the object [Freeman 2026, §0.2]", and line 52 states "By Löb's theorem, an agent reasoning in a fixed formal theory cannot trust a successor that reasons in the same theory [Löb 1955; Yudkowsky & Herreshoff 2013]."
   - *What is missing:* Unlike §3 (which was revised to "What the results motivate"), line 50 still states that the three results "fix the shape" of the institution. On line 52, Löb's theorem obstructs a specific proof-based self-modification rule (requiring a formal proof in a consistent sound theory $T \supseteq \mathrm{PA}$ that a successor reasoning in $T$ satisfies a sentence $\varphi$ before adopting it, unless $T \vdash \varphi$ already); it does not forbid all forms of trust or statistical certification between systems sharing a formal language.

2. **Lines 65, 85, and 296 — Primary rules of conduct ("rules of conduct enter only from cases") are presented as built without the `◦` marker:**
   - *What is said:* Line 65 states "Rows marked ◦ are argued but not yet built" (marking only the Waismann row on line 88). Line 85 (Table 1, Hart 1961 row) says "The core holds exactly these three, in code; rules of conduct enter only from cases", and line 296 (§5.2) says "1. **Rules of conduct enter only from cases** [CHARTER A2.1; Hart 1961; Hayek 1973]."
   - *What is missing:* In the implementation at `e580b64`, the primary-rule mechanism of `CHARTER §3` and `A2.1` (`rule` and `repeal` entries, witnesses, and lapse) is **not built**: `SPEC §4` (line 80) and `SPEC §7` (lines 239–240) admit no `rule` entry ("Recognition (c) of CHARTER §3 … holds vacuously: no rule can be admitted"), and `CHARTER A2.1` explicitly defers building the primary-rule language until a real case arises (as line 392 later notes). Only charter amendments (`amend`) and hard-coded judge grounds (`SPEC §10`) have entered from cases so far. The second clause of line 85 should be marked `◦` (or explicitly restricted to amendments and judge grounds).

3. **Line 87 — Not every kernel rule and judge ground has a mutant pin in `pins/`:**
   - *What is said:* Table 1 (Crawford & Ostrom 1995 row) states: "Kernel rules and judge grounds each paired with a mutant that must be killed".
   - *What is missing:* At `e580b64`, 13 of the 14 kernel refusal reasons (`SPEC §9`) and 13 of the 15 judge refusal grounds (`SPEC §10`) are paired with mutants in `pins/`. Kernel reason `genesis_misplaced` (`SPEC §8` step 5) and judge grounds `prefix_broken` (`SPEC §10` item 3) and `genesis_by_proposal` (`SPEC §10` item 4) are tested by vector and unit tests (`spec/vectors/logs/18_genesis_misplaced.jsonl`, `tests/test_check.py`, `tests/test_judge.py`), not by mutant pins in `pins/`. In addition, three pins for recent tool/runner fixes were deferred to C2c (`grant` at `seq 7615`, `transcripts/BRIEF-C2a-3-draft.md`).

4. **Line 118 — Lean description for Proposition 4(b) understates what `Restart.lean` omits:**
   - *What is said:* "For 4(b), it proves the inequality, not that independent windows attain it."
   - *What is missing:* `Claim.restart_independent` in `Restart.lean` proves only the real-number algebraic inequality $1 - \prod_{j \in \mathrm{Fin}\,k}(1 - r_j) \le 1 - (1-\alpha)^k$ for a function `r : Fin k → ℝ` with `r j ≤ α` and `α ≤ 1`. As `lean/README.md` acknowledges, it does not formalise independent events in a probability space or the identity $\Pr(\bigcup_j A_j) = 1 - \prod_j (1 - \Pr(A_j))$ at all — not merely attainment when $r_j = \alpha$.

5. **Line 134 — Omission of `transmuted` from the kernel state summary:**
   - *What is said:* "The state also carries the charter and trusted-base digests in force. The judge reads these from the entries; the kernel does not."
   - *What is missing:* In `kernel/check.py:16, 98–100` and `SPEC §7` (line 223) / `§8` step 9 (line 269), the kernel's `State` tuple also carries `transmuted` (the `frozenset` of amendment IDs unlocked by `decision` entries of kind `transmute`), which the kernel folds and the judge enforces under `SPEC §10` item 13 (`amend_untransmuted`).

6. **Line 172 vs. Line 338 — Counsel's 100 forecasts and the operator's 3 forecasts are not scored in the C2a value test:**
   - *What is said:* Line 172 states: "So the counsel session that drafted the charter, and the operator himself, forecast on the same ledger and are scored in the same way. Both keys hold the power to forecast, and by seq 7809 counsel had entered 100 forecasts and the operator 3 [seqs 31, 33; log at seq 7809]."
   - *What is missing:* First, line 172 cites no scoring implementation (`tools/entry.py:score`, which tabulates per-proposer log-loss across all resolved forecasts on `log.jsonl`, should be cited). Second, none of counsel's 100 forecasts (`76` `counsel.programme`, `18` pre-C2a `world.hkjc`, `5` untyped `free`, `1` `world.assize`) and none of the operator's 3 forecasts (all `world.assize`) is a post-opening C2a value event in `judge/value.py`; in the C2a value ledger (line 338), both `counsel` and `guy` have 0 forecasts across all 2,820 events and are scored purely as base-rate abstentions. Stating this prevents an apparent contradiction between lines 172 and 338.

7. **Lines 243–247 and 255 — Incomplete statement of `SPEC §10`'s replay admission condition after $T$:**
   - *What is said:* Lines 243–247 define $R$ as the first-parent commits of trunk up to $T$ and state that the specification admits the push installing $E'$ if $E'$ agrees with $E$ outside $\mu(r)$ and with the grant on $\mu(r)$ across $r \in R$. Proposition 6(c) (line 255) then states: "Nothing is certified about $E'$ on any other input: after $T$, or on a recorded prefix read with different evidence".
   - *What is missing:* `SPEC §10` ("The promotion evaluator", lines 520–523) and the replay session template (`transcripts/sessions/c2a-3-replay.md`, lines 17, 43–46) require agreement not only on the table's rows up to $T$, but also on **every first-parent commit of `main` after $T$ up to the installing push's parent**, compared against the frozen evaluator run there under the same marks. Thus, under the specification's full admission rule, first-parent commits between $T$ and the installing push's parent are also covered; what is uncertified is commits after the installing push's parent (and any commit not yet replayed by CI or the reviewer session).

8. **Line 264 — `kernel2` was written from `SPEC.md` plus the test vector suites, not `SPEC.md` alone, and the citations do not back its provenance or CI enforcement:**
   - *What is said:* "The kernel exists twice, in Python and in Go. The second was written from the specification alone by a different model family, and CI fails on any disagreement between the two [CHARTER §5; SPEC §9a]."
   - *What is missing:* `kernel2/README.md:10–11` and `kernel2/NOTES.md:7` record that `kernel2` (`google/gemini-4-argon`) was written from `SPEC.md`, `spec/vectors/`, and `tests/vectors/`, not the specification text alone. Moreover, `CHARTER §5` and `SPEC §9a` specify the design requirement and `harness/diff.py`; the provenance record is `kernel2/NOTES.md` (and `REPORT §8.3.7`), and CI failing on disagreement is enforced by `SPEC §10` item 5 (`judge/judge.py:365–368`) and `.github/workflows/tests.yml` (which runs 300 seeds of `harness/diff.py`, as `transcripts/AUDIT-criteria-20261117.md` row 2 notes).

9. **Line 302 — Inaccurate description of the ~80 non-stream builder and reviewer proposals:**
   - *What is said:* "Builder and reviewer keys have since signed 6,621 of the log's 7,810 entries. Most of these are the hourly stream: 5,919 forecasts and resolutions, and about 620 proposals that carry them. About 80 are reviews, reads and fixes [log at seq 7809]."
   - *What is missing:* At `seq 7809`, builder and reviewer keys signed `5,919` forecasts/resolutions and `702` proposals (`623` carrying the scheduled freshness/HKJC streams and `79` other proposals). Those `79` non-stream proposals are **not** all "reviews, reads and fixes": `40` are reviews/cold reads (`REVIEW-*` and `read:`), `3` are fixes (`FIX-*`), `14` are code, pin, and replay-table proposals (`tools/jack`, `sim:`, `tools/status.py`, `C1b`, `C2a`, `C2b`, and the two promotion replay tables), and `22` are proposals carrying non-hourly-stream forecasts or resolutions (M2 race cards/resolutions and procedure/counsel forecast resolutions).

10. **Line 325 — Table 2 omits the shared-login / classifier qualification on C2a's nine repair rows:**
    - *What is said:* Table 2 (line 325) states: "**failed** on nine repair rows found off the record; `fix` at seq 5563".
    - *What is missing:* While line 330 was revised to say "nine rows that its classifier labels as repairs under the operator's login", Table 2 still states "nine repair rows found off the record" without qualification. As `transcripts/RESEARCH-witness-ledger-20261107.md` (row 3) and `Freeman 2026, §6.4` document, before the court GitHub App was installed on 4 November, non-operator sessions acted under the operator's login and only one of the nine classified rows was the operator's own act.

11. **Line 348 — Missing the actual end-of-window procedure:object count for C2a′ at `seq 7180`:**
    - *What is said:* "For C2a′ the count stood at 459 to 1,786 [`judge/status.py` at seq 7809]. The evaluator counted from seq 5565 to seq 7809, past the veto that ended the window at seq 7180."
    - *What is missing:* Give the count at the veto that actually ended C2a′ (`seq 7180`): over `seqs 5565..7180`, `judge/status.py` gives **320 procedure to 1,296 object** (out of 1,616 entries in the window).

---

## 7. Overclaiming and clarity

The manuscript is commendably forthright about its negative empirical result (§6), its no-skill criteria audit (§8), and the fact that no self-modifying agent (C3) exists yet (lines 15, 33, 328, 398). The remaining places where the presentation overreaches or could be tightened are modest:

- **Residual necessity language in §2 (lines 50, 52):** Harmonise lines 50 and 52 with §3 so that Rice, Löb, and Goodhart are consistently presented as motivating constraints under explicit formal hypotheses rather than results that "fix the shape" of the institution.
- **Unbuilt mechanisms in Table 1 and §5.2 (lines 85, 88, 296):** Because neither the primary-rule language (`CHARTER §3`, `A2.1`) nor the open-texture text-anchoring rule (Waismann row, line 88) has been built, presenting "rules of conduct enter only from cases" in Table 1 without a `◦` marker overstates what the 450-line kernel and current law implement.
- **What could be cut without loss:**
  1. The Waismann row in Table 1 (line 88), which is unbuilt (`◦`) and plays no role in §§4–6.
  2. The seven-stop regress enumeration in §3.2 (lines 100–104), which is already summarized in Contribution 3 (line 30) and belongs more naturally to the book (`Freeman 2026, ch. 12`) than to a concise research paper.

---

## 8. Recommendation

**Minor revision.** The mathematical core in §4 and its Lean 4 formalisation are sound, the filtration counterexample and retrospective block recomputation in §6 are valid and reproducible, and the revisions after the fifth referee report resolved every major methodological and scoping objection. Only minor factual and provenance corrections against the repository at `e580b64` remain.

The five changes that matter most, in order:

1. **Correct the remaining implementation and record discrepancies in §§3–6 (lines 85, 87, 134, 264, 302, 325, 348):**
   - In Table 1, mark "rules of conduct enter only from cases" (line 85) as not yet built for primary rules (`CHARTER A2.1`), and qualify line 87 to note that 13 of 14 kernel reasons and 13 of 15 judge grounds have mutant pins in `pins/` (while `genesis_misplaced`, `prefix_broken`, and `genesis_by_proposal` are covered by vector/unit tests).
   - Add `transmuted` to the kernel state summary on line 134; note on line 264 that `kernel2` was written from `SPEC.md` plus the vector suites (`kernel2/NOTES.md`) and that CI runs `SPEC §10` item 5 and a 300-seed differential sample; correct line 302's description of the 79 non-stream builder/reviewer proposals (`40` reviews/reads, `3` fixes, `14` code/pin/table builds, `22` non-hourly forecast/resolution batches); add the classifier/shared-login qualification to Table 2 (line 325); and report C2a′'s actual at-veto (`seq 7180`) procedure-to-object count (`320` to `1,296`) alongside the post-veto `seq 7809` figure on line 348.
2. **Clarify how counsel's 100 and the operator's 3 forecasts are scored (line 172 vs. line 338):**
   - Cite `tools/entry.py` (`score`) on line 172 and note that all 100 of counsel's and all 3 of the operator's forecasts are either pre-C2a or non-value types (`counsel.programme`, `world.assize`, `free`), so neither party has issued a post-opening C2a value forecast in `judge/value.py` (where both are scored as base-rate abstentions).
3. **Align lines 243–247 and Proposition 6(c) (line 255) with `SPEC §10`'s post-$T$ chain replay requirement:**
   - Note that `SPEC §10` ("The promotion evaluator") requires replay agreement not only on the frozen table $R$ up to commit $T$, but also on first-parent commits after $T$ up to the installing push's parent, and adjust Proposition 6(c)'s "after $T$" boundary accordingly.
4. **Align line 118's description of `Restart.lean` with `lean/README.md`:**
   - State on line 118 that for Proposition 4(b), `restart_independent` proves the real algebraic inequality $1 - \prod_j (1-r_j) \le 1 - (1-\alpha)^k$ rather than formalising independent events or their union probability.
5. **Harmonise lines 50 and 52 with §3 and trim §3.2:**
   - Replace "three results fix the shape of what governs the object" (line 50) with motivating language matching §3, state the formal proof-theoretic condition on Löb's theorem (line 52), and compress §3.2's seven-stop regress list.

RECOMMENDATION: minor revision
exit=0
```

