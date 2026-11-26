# Cold read 8 of the claim paper: report and disposition

- **Reader:** `google/gemini-4-argon`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1372, filed under Guy's standing yes. The session ran from 04:46Z to 05:08Z on 26 November.
- **Text read:** draft 14, at `5f549f9`.
- **Verdict:** **accept**, with five sentence-level corrections. This is the first accept in eight reads. The reader again reproduced every figure and found the propositions and the Lean statements sound.
- **Draft 15** makes the five corrections and the trims the reader suggested. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What draft 15 does |
|---|---|
| The kernel does not read `transmuted` or the charter digests | Both are now described as recorded, not used for admission. The judge checks trunk's charter against the latest digest entered and refuses an untransmuted amendment [SPEC §7; §10, items 2 and 13]. Verified against SPEC §7 ("The kernel records them; the judge enforces them") and `judge/judge.py`, `promulgated_charter`. |
| An amendment's second immediate effect | Stated: trunk's charter must match at once, as well as the freeze on pushes [SPEC §10, items 2 and 12]. |
| The forecaster counts and the ablation wording in §6 | The counts are now stated for the implementation's 2,820 selected events. The per-event figure is "on its 2,820 selected events". The ablation "scores only events resolved by their deadline", while base rates use every pre-cutoff resolution. |
| Kernel2's provenance | Now "by OpenAI and Google model sessions, at C0 and in later revisions [REPORT §8.2; the history of `kernel2/NOTES.md`]". Checked: `a6f36b4` names `openai/gpt-6-astra`; `8fcd821`, `432e385` and `7ae10a3` are the revisions. |
| Trim §4.5, §4.2 and the second ratio figure; Hyperagents' App. E.5 | §4.5 keeps the list of non-repair types and points to the code for the rest. §4.2 drops the forecast counts. §6 gives only the ratio at the veto. Hyperagents now keep parent selection fixed "except in one experiment". |
| "Every claim of merit is a forecast" read as a rule on proposals | The abstract, §1, Table 1 and the conclusion now say "claims of merit count only as forecasts". |

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

A self-modifying AI agent can be trusted only as far as an institution outside its reach can test it, and that judging institution must itself be tested rather than trusted: built before the agent, imposed first on the model sessions that build it, and granted powers layer by layer only through valid sequential tests of repair-free liveness and predictive value on its own signed record. Those sequential tests must themselves keep their level under simultaneous resolution, and when a valid block test is applied retrospectively to the public record of the reference implementation, it reveals that the institution's apparent predictive value rests on a weak type-pooled baseline and vanishes against a per-dataset base rate.

**Does the abstract state it, and does the body deliver it?** Yes to both. The abstract states the message in four sentences matching `ABSTRACT-FIRST.md`: the problem and the classical limits (Rice, Löb, Goodhart), the institutional design (law as a fold over a signed log, claims as log-scored forecasts, conjunctive sequential promotion on liveness and value before the agent exists), the formal guarantees and block-form correction to per-event betting, and the negative empirical finding on the reference implementation's record. The body delivers each part in turn: §§2–3 motivate the ingredients, §4 proves the six propositions and demonstrates the per-event level failure by example and simulation, §5 explains the layer order and why builders come first, and §6 reports the retrospective block recomputation on `renavondata/jack`.

**What in the body does not serve it:**
1. **Low-level implementation exceptions in §4.5 (lines 244–245):** The detailed encoding of `window_fixes` (when a `fix` decision's taint lifts at the next push) and the side effect that a sovereign entry clears pending resolutions waiting for a merge (`judge/status.py`, `item_process`) are code-level edge cases that obscure the clean conceptual partition of the principal's acts into reserved irreversible decisions and priced repairs.
2. **The non-value forecast digression in §4.2 (line 146):** The philosophical remark that a forecast belongs to a procedure rather than a mind and the tally of counsel's 100 and the operator's 3 non-stream forecasts (immediately noted as excluded from §6's value test) do not advance the core argument.
3. **Dual-timestamp accounting of the procedure-to-object ratio in §6 (line 316):** Reporting C2a′'s procedure-to-object ratio both at the veto (`320 to 1,296` at `seq 7180`) and after the evaluator kept counting (`459 to 1,786` at `seq 7809`), followed by its padding flaw, duplicates §8 (line 350) without contributing to the liveness or value tests.

---

## 2. Correctness

All line numbers below refer to `draft.md` at commit `5f549f996ba9d703621e2ea1c8a433eb0d21b04c`.

- **Proposition 1 (prospectivity, lines 114–123):** *Correct.*
  - *Part (a):* Because $S_i$ is a pure fold of $e_0, \dots, e_{i-1}$, the validity predicate $V(S_i, e_i)$ depends only on the prefix $e_0, \dots, e_i$. Appending $M$ to a valid log $L$ cannot alter the verdict on any entry of $L$.
  - *Part (b):* Requiring both logs $L$ and $L^* \neq L$ to be linked and numbered by position from $0$ (`seq` $= i$) makes the collision reduction rigorous. Walking backwards from the last lines (which both hash to $h$), either two distinct lines share a SHA-256 hash at some step, or the suffixes match until the shorter log reaches its genesis line (`seq` $= 0$) paired with an entry of the longer log at positive index (`seq` $> 0$). Infact, because entries are numbered by position from $0$, when $|L| \neq |L^*|$ the two last lines themselves already differ in their `seq` field while sharing hash $h$, yielding an immediate collision at the first step.

- **Proposition 2 (propriety; no self-judgement, lines 132–139):** *Correct.*
  - *Part (a):* For $\pi \in (0,1)$, $g(p) = \pi\ln p + (1-\pi)\ln(1-p)$ has $g'(p) = (\pi - p)/(p(1-p))$ and $g''(p) = -\pi/p^2 - (1-\pi)/(1-p)^2 < 0$ on $(0,1)$, so $p = \pi$ is the unique continuous maximiser. By strict monotonicity on $(0,\pi]$ and $[\pi,1)$, restricting $p$ to $\{1,\dots,999\}/1000$ places the maximum at a grid point adjacent to $\pi$ (or at the nearer boundary $0.001$ or $0.999$ when $\pi \notin [0.001, 0.999]$), with ties possible between the two adjacent grid points bracketing $\pi$.
  - *Part (b):* Enforced by `SPEC §8` step 8a (`kernel/check.py:82–83`), which compares the resolution's `proposer` against the recorded `proposer` of the forecast after step 8 verifies that `proposer` matches the signing key's registered `principal`. The qualifications regarding performativity, inter-principal collusion, and nonlinear downstream rewards (lines 140–142) are well taken.

- **Proposition 3 (value, lines 154–182):** *Correct.*
  - *Setup and bounds:* For any non-empty resolved subset $R_m \subseteq B_m$, clipping all $p_{k,i}, b_i$ to $[10^{-3}, 1 - 10^{-3}]$ bounds each member's product likelihood $\prod_{i \in R_m} p_{k,i}(Y_i)$ and their convex combination $Q_m(Y_{R_m})$ within $[10^{-3|R_m|}, (999/1000)^{|R_m|}]$. Thus $\ln Q_m(Y_{R_m}) - \sum_{i \in R_m} \ln b_i(Y_i) \in [-|R_m|\ln 999, |R_m|\ln 999]$, giving $\bar D_m \in [-1, 1]$ (and factor $1$, equivalent to $\bar D_m = 0$, when $R_m = \varnothing$).
  - *Sufficient condition (line 170):* Conditioning on both $\mathcal G_{m-1}$ and which events resolve ($R_m$) fixes the divisor $|R_m|$ on each atom of $R_m$, so non-positive conditional expected joint log-score advantage given $(\mathcal G_{m-1}, R_m)$ implies $\mathbb E[\bar D_m \mid \mathcal G_{m-1}, R_m] \le 0$ and hence $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 0$ by the tower property. As line 170 now rightly notes, without conditioning on $R_m$ the implication can fail because $|R_m|$ is random.
  - *Part (a):* Under assumption (A), $\lambda_m \in [0, 1 - 1/(m+1)] \subset [0,1)$ is $\mathcal G_{m-1}$-measurable and $1 + \lambda_m \bar D_m \ge 1 - \lambda_m > 0$. Under $H_0^{\mathrm{val}}$, $\mathbb E[1 + \lambda_m \bar D_m \mid \mathcal G_{m-1}] = 1 + \lambda_m \mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 1$, so $W_t$ is a non-negative supermartingale with $W_0 = 1$, and Ville's inequality yields $\Pr(\sup_t W_t \ge 1/\alpha) \le \alpha$. Splitting overlapping sittings into online lag classes $\ell = 1, 2, \dots$ with thresholds $\ell(\ell+1)/\alpha$ preserves level $\alpha$ by the union bound since $\sum_{\ell \ge 1} \alpha/[\ell(\ell+1)] = \alpha$.
  - *Part (b):* With uniform initial weights $w_{k,1} = 1/K$ and Bayes updates $w_{k,m+1} = w_{k,m} \prod_{i \in B_m} p_{k,i}(Y_i) / Q_m(Y_{B_m})$ along a single sequence of blocks, the product $\prod_{m \le t} Q_m(Y_{B_m})$ telescopes to $\frac{1}{K}\sum_{k=1}^K \prod_{m \le t}\prod_{i \in B_m} p_{k,i}(Y_i) \ge \frac{1}{K}\max_k \prod_{m \le t}\prod_{i \in B_m} p_{k,i}(Y_i)$. Taking logs and subtracting $\sum_{m \le t}\sum_{i \in B_m}\ln b_i(Y_i)$ gives the first inequality, and because the base-rate forecaster is in the roster, the maximum is at least $0$, giving $\ge -\ln K$.

- **Remark and Example in §4.3 (lines 183–187):** *Correct and reproduced.*
  - The Remark accurately explains why per-event betting in resolution order loses validity under a cutoff-time null when outcomes within a sitting are dependent: later bets condition on earlier outcomes of the same sitting, and even freezing the stake at the cutoff leaves a product of correlated factors $\prod_{i \in B_m}(1 + \lambda_m D_i)$ whose conditional expectation need not be $\le 1$. It also correctly identifies the trade-off of the joint mixture $Q_m$: a mixture of product distributions can capture within-sitting correlation that the base rate's single product cannot, whereas replacing $Q_m$ by the product of marginals $\prod_{i \in B_m} q_i(Y_i)$ forfeits the $\ln K$ regret bound of Proposition 3(b).
  - Running `sim_filtration.py` reproduces every figure in the Example (line 185):
    - For $b = 1/2$ and $q \in \{0.95, 0.05\}$ chosen by an independent fair coin on $n$ events sharing $Y \sim \mathrm{Bern}(1/2)$, $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] = \frac{1}{2}(\ln 1.9 + \ln 0.1)/\ln 999 \approx -0.1202$.
    - At $n = 20$ (300 sittings, 4,000 runs, $\alpha = 0.05$): per-event crossing rate `0.1325` (13%), block crossing rate `0.0000`.
    - At $n = 50$ (`50 0.45 200 2000`): per-event crossing rate `0.5035` (50%), block crossing rate `0.0000`.
    - With independent outcomes (`--independent`, for both $n=20$ and $n=50$): per-event crossing rate `0.0000`.
    - Running `--roster 20 300 2000` gives `0.2850` (implementation form) vs. `0.0000` (block form); as the script's docstring notes, the three-member roster $(0.5, 0.95, 0.05)$ is rightly excluded from the paper's text as a null experiment because the mixture of $0.95^n$ and $0.05^n$ captures the shared-outcome dependence at $m=1$, violating the joint-score null ($\mathbb E[\bar D_1] \approx +0.085 > 0$).

- **Proposition 4 (liveness, with wealth carried across windows, lines 193–202):** *Correct.*
  - *Part (a):* Since $0 \le s_j \le n_j$, $\hat q_j = (s_j+1)/(n_j+2) \in (0,1)$, so $\lambda_j = \max(0, (\hat q_j - p_0)/(p_0(1-p_0))) \in [0, 1/p_0)$. For $Y_j \in \{0,1\}$ (or simultaneous-item mean $\bar Y_j \in [0,1]$), $1 + \lambda_j(Y_j - p_0) \ge 1 - \lambda_j p_0 > 0$ and $\mathbb E[1 + \lambda_j(Y_j - p_0) \mid \mathcal F_{j-1}] \le 1$ under $H_0^{\mathrm{live}}$. Continuing the same product across windows makes all window ends stopping times of one non-negative supermartingale, so Ville's inequality bounds the lifetime false-crossing probability by $\alpha$.
  - *Part (b):* For $k$ windows each restarted at $1$ with false-crossing probability $r_j \le \alpha$, independence gives $1 - \prod_{j=1}^k(1-r_j) \le 1 - (1-\alpha)^k$ (attained when $r_j = \alpha$), and the union bound gives $\sum_{j=1}^k r_j \le k\alpha$.

- **Proposition 5 (conjunctive promotion, lines 207–210):** *Correct.*
  - Promotion at prefix $t$ requires both $W_t \ge 1/\alpha$ and $M_t \ge 1/\alpha$, so the event that promotion ever occurs lies in $\{\sup_t W_t \ge 1/\alpha\} \cap \{\sup_t M_t \ge 1/\alpha\}$. Under $H_0^{\mathrm{val}} \cup H_0^{\mathrm{live}}$, whichever component null holds bounds the intersection's probability by $\alpha$ (Berger's intersection–union principle).

- **Proposition 6 (replay-bound change, lines 224–235):** *Correct.*
  - Parts (a), (b), and (c) follow directly from the replay admission condition over $R^+$, `SPEC §10` item 15's dispatch to the historical evaluator in force at the promotion's `seq`, and the fact that agreement on finitely many inputs constrains nothing outside $R^+$ or under altered evidence inputs.

---

## 3. The Lean files

I inspected `lean/README.md` and all seven files in `lean/Claimproofs/`. I have not run `lake build` to verify compilation against Mathlib; by inspection, no file contains `sorry` or non-standard axioms.

1. **`HashChain.lean` (`Claim.collision_of_ne`) $\leftrightarrow$ Proposition 1(b):**
   - *Comparison:* Faithful to the combinatorial reduction. Logs are represented backwards as non-empty lists `x :: xs : List α` with abstract functions `hash parent : α → β` and `seq : α → ℕ`. `RevLinked` requires `parent x = hash y` for adjacent elements (leaving genesis's `parent` unconstrained, a weaker hypothesis that strengthens the theorem), and `RevNumbered` requires `seq x = rest.length`. It proves that `hash x = hash x'` and `x :: xs ≠ x' :: xs'` imply `∃ a b, a ≠ b ∧ hash a = hash b`.
   - *Differences:* `parent` and `seq` are treated as total functions on abstract entries (assuming canonical parsing), the existential witness `a, b : α` does not state list-membership in the conclusion, and the complexity-theoretic adversary sentence of Prop. 1(b) is informal context.

2. **`Propriety.lean` (`Claim.log_score_proper`, `Claim.log_score_strict`) $\leftrightarrow$ Proposition 2(a):**
   - *Comparison:* Proves that for $\pi, p \in (0,1)$, `expScore π p ≤ expScore π π`, with strict inequality for `p ≠ π`, via `Real.log_le_sub_one_of_pos` and `Real.log_lt_sub_one_of_pos`.
   - *Differences:* Proves strict propriety (unique global maximum at $p = \pi$) rather than strict concavity ($g'' < 0$) or the per-mille grid clause. Both omissions are explicitly disclosed in lines 92–93 and `lean/README.md`.

3. **`Mixture.lean` (`Claim.prod_Q`, `Claim.regret`, `Claim.regret_base`) $\leftrightarrow$ Proposition 3(b):**
   - *Comparison:* Takes abstract block likelihoods `P : Fin K → ℕ → ℝ` with `0 < K` and `∀ k m, 0 < P k m`, defines uniform-prior posterior mixture probabilities `Q P T = S P (T+1) / S P T`, proves the telescoping product `∏ m ∈ range T, Q P m = S P T / K` (`prod_Q`), proves `∀ k, ∑ m ∈ range T, log (P k m) - log K ≤ ∑ m ∈ range T, log (Q P m)` (`regret`), and proves that if `∀ m, P k₀ m = B m` then `-log K ≤ ∑ m ∈ range T, (log (Q P m) - log (B m))` (`regret_base`).
   - *Differences:* Requiring only `0 < P k m` is weaker (more general) than clipped per-mille product probabilities. The within-block product $\prod_{i \in B_m} p_{k,i}(Y_i)$, the identity $|B_m|\ln 999\,\bar D_m = \ln Q_m - \ln B_m$, and packaging `∀ k` into $\max_k$ are informal bridges (disclosed at line 92).

4. **`Ville.lean` (`Claim.ville_finite`) and `Wealth.lean` (`Claim.wealth_supermartingale`, `Claim.wealth_level`, `Claim.value_factor`, `Claim.liveness_factor`) $\leftrightarrow$ Propositions 3(a) and 4(a):**
   - *Comparison:* `ville_finite` proves the finite-horizon maximal inequality $\varepsilon \cdot \mu\{\omega \mid \varepsilon \le \max_{k \le n} W_k(\omega)\} \le \mathbb E[W_0]$ for any non-negative supermartingale `W` under a finite measure `μ`, derived from Mathlib's `expected_stoppedValue_mono` applied to the submartingale `-W` and the bounded hitting time `hittingBtwn`. `wealth_supermartingale` and `wealth_level` prove that `wealth L D` is a non-negative supermartingale satisfying $\varepsilon \cdot \mu\{\omega \mid \varepsilon \le \max_{k \le n} \mathrm{wealth}_{L,D}(k,\omega)\} \le 1$ under a probability measure whenever `0 ≤ L ≤ M`, `|D| ≤ B`, `0 ≤ 1 + L * D ≤ C`, `D n` is `𝒢 n`-strongly measurable, `L (n+1)` is `𝒢 n`-strongly measurable (predictable), and `μ[D (n+1) | 𝒢 n] ≤ᵐ[μ] 0`. `value_factor` and `liveness_factor` verify the scalar bounds $1 + l d \in [0, 2]$ (for $0 \le l \le 1, |d| \le 1$) and $1 + l(y - p_0) \in [0, 1/p_0]$ (for $0 < p_0 < 1, 0 \le y \le 1, 0 \le l \le 1/p_0$).
   - *Differences:* (i) The bound is proved for every finite horizon $n$ rather than $\sup_{t \in \mathbb N}$ (which follows by monotone continuity of measure). (ii) The concrete plug-in stake formulas $\lambda_m, \lambda_j$ and their strict upper bounds ($< 1$ and $< 1/p_0$) are abstracted into the bounded predictable process `L` and non-negative factor hypothesis `0 ≤ 1 + L * D` (weakening strict positivity `> 0` to `≥ 0`, which suffices for Ville's inequality). (iii) The conditional-expectation null `μ[D (n+1) | 𝒢 n] ≤ᵐ[μ] 0` is taken directly as a hypothesis rather than formalising the conditioning on the random resolved subset $R_m$ discussed in Prop. 3. All of these are accurately disclosed in lines 92–95 and `lean/README.md`.

5. **`Restart.lean` (`Claim.restart_independent`, `Claim.restart_union`) $\leftrightarrow$ Proposition 4(b):**
   - *Comparison:* `restart_union` proves the measure-theoretic union bound $\mu(\bigcup_{j \in \mathrm{Fin}\,k} A_j) \le k\alpha$ from $\forall j, \mu(A_j) \le \alpha$. `restart_independent` proves the real-number inequality $1 - \prod_{j \in \mathrm{Fin}\,k}(1 - r_j) \le 1 - (1 - \alpha)^k$ under $\forall j, r_j \le \alpha$ and $\alpha \le 1$.
   - *Differences:* As both line 92 and `lean/README.md` note, `restart_independent` is pure real algebra and does not model independent events or their union probability in a measure space (nor the attainment sentence for exact tests, which is immediate when $r_j = \alpha$).

6. **`Conjunctive.lean` (`Claim.conjunctive_promotion`) $\leftrightarrow$ Proposition 5:**
   - *Comparison:* Proves that `Promote ⊆ CrossW`, `Promote ⊆ CrossM`, and `μ CrossW ≤ α ∨ μ CrossM ≤ α` imply `μ Promote ≤ α`.
   - *Differences:* Takes the component crossing bounds as hypotheses rather than chaining `wealth_level`, as disclosed at line 92.

---

## 4. The recomputation

Running `curl -sL $U/block_on_log.py | python3 - --rev e580b64` reproduces every figure reported in §6 (lines 301–314):
- **Implementation baseline:** `2820` resolved value events; roster `['guy', 'counsel', 'reviewer', 'builder', 'base']`; implementation per-event wealth `E = 1.51983e+60`; forecasts in those 2,820 events: `{'reviewer': 2795, 'builder': 12}`.
- **Sittings and censoring:** Observed to `2026-11-25T11:05:35Z` (`seq 7809`), `476` completed sittings and `4` pending sittings; `2803` member events in completed sittings, of which `170` expired unresolved at their deadline (`168` resolved only after their deadline), leaving `2,633` in-time resolved events scored (`451` of the `476` completed sittings have at least one resolved event; `25` have $R_m = \varnothing$ and `10` are partially resolved); `19` resolved events had no forecast before their cutoff and are excluded from sitting membership.
- **Lag classes:** `5` classes with total sittings `[216, 196, 48, 16, 4]` and scored (completed) sittings `[215, 195, 47, 15, 4]` (in each of classes 1–4, the single pending sitting is the final sitting of its class); thresholds $\ell(\ell+1)/\alpha = [40, 120, 240, 400, 600]$ at $\alpha = 0.05$.
- **Pooled by event type:** Final wealth by class `['1.993e+04', '1.109e+04', '3.009', '1.159', '1.022']`; running maxima `['1.993e+04', '1.19e+04', '3.009', '1.159', '1.022']`; classes 1 and 2 cross their thresholds (`40` and `120`).
- **Ablations (pooled by type):** Per-event with stakes, weights, and base rates frozen before each cutoff gives `2.492e+58`; single block process without lag-class splitting gives `1.739e+10`.
- **Kept per dataset:** Final wealth `['0.9989', '0.9998', '1', '1', '1']`; running maxima `['1', '1', '1', '1', '1']`; no class crosses its threshold or ever exceeds $1$.

**Is the method in `block_on_log.py` valid as §4.3 and §6 describe it?** Yes, for the sequential test of Proposition 3(a) in the recorded-timestamp filtration:
1. *Pre-cutoff sitting membership and deadlines:* An event enters sitting $c$ (`fkey`, lines 88–94) only if some forecast for it was recorded with `ts < c`, and its deadline $d_{\mathrm{deadline}}$ is the maximum of `resolves_by` over those pre-cutoff forecasts.
2. *Online-implementable lag-class assignment:* Each member event's completion instant is $\tau_e = \min(t_{\mathrm{res}}(e), d_{\mathrm{deadline}}(e))$, and a sitting's completion instant is $\tau(B_m) = \max_{e \in B_m} \tau_e$. For any later cutoff $c > c'$, the condition $\tau(B_{c'}) < c$ holds if and only if every member event of $c'$ either resolved in time strictly before $c$ or had its pre-committed deadline pass strictly before $c$. Because both events are determined by the log before $c$, the greedy class assignment (`if d < c:`, lines 138–145, run over all sittings `all_order` including pending ones) is $\mathcal G_{m-1}$-measurable and satisfies assumption (A) within every lag class.
3. *Predictability of weights, base rates, and stakes:* At cutoff $c$, mixture weights `w` update only over in-time resolved events with `done < c` (lines 162–166), base rates `base(key, c)` use `bisect_left(times, c)` (strictly `< c`), and class stakes `stake(S[i], Q[i], M[i])` use only earlier completed sittings in the same lag class `i`. Empty resolved blocks ($R_m = \varnothing$) are skipped (`if not block: continue`, line 168), which leaves $W_i$ multiplied by $1$ and keeps later stakes in class $i$ predictable. As line 304 notes, because weights pool resolved events across lag classes and from partly resolved sittings, Proposition 3(b)'s telescoping bound does not apply, while Proposition 3(a)'s supermartingale guarantee holds. (See §6 below for two minor wording discrepancies in lines 306 and 314 regarding the event counts and base-rate deadline filtering.)

---

## 5. The revisions

The seventh referee's points (`REVIEW-cold-7.md`) were resolved in Draft 14 as follows:

1. **Proposition 3's sufficient condition under random resolved-subset size $|R_m|$:** *Resolved.* Line 170 now adds "and given which events resolve. Without the second condition it can fail, because $\bar D_m$ divides by the random size $|R_m|$."
2. **Outcome truth, evidence interpretation, and recorded timestamps outside the trust boundary:** *Resolved.* Line 56 now states that a resolution's outcome is taken as entered (`SPEC §5`), cites the known wrong resolution that stands (`seq 123`, `REPORT, C1a §4`), states that timestamps are checked only for format and order, and restricts the guarantees to the recorded outcomes and times.
3. **"Every claim of merit is a forecast" read as kernel enforcement:** *Resolved.* Line 130 now clarifies that in the design a claim of merit has standing only as a forecast, a proposal asserts nothing about its merit, and the ledger scores forecasts rather than proposals.
4. **"Carried, it stays at 5%" applied to the implementation:** *Resolved.* Line 203 now restricts the 5% figure to "a valid process carried unchanged" and notes that "the implementation's per-event value process is not one (Example, above)."
5. **Repair-typing exclusions and clearing of pending resolutions in `item_process`:** *Resolved.* Lines 244–245 now list the exact non-repair types (`genesis, key, amend, push and proposal, and decisions other than fix`) and state that any other entry under the operator's key drops pending resolutions waiting for a merge from the count.
6. **Key redeclaration under the same `key_id` and charter state description:** *Partially resolved.* Line 104 now accurately says every public key ever declared "belongs to its first identifier for the life of the log". However, lines 105–108 still misstate the kernel/judge boundary for `transmuted` and the charter digest (see §6, item 1 below).
7. **Comparative boundaries (`Regimes`, self-adaptive systems, related work):** *Resolved.* Line 112 narrows the event-sourcing contrast to Regimes (`Nakajima 2026`), line 328 restricts the fixed-manager statement to "In the systems cited", and lines 330 and 336 qualify the literature comparisons with "In our reading".
8. **Holmström rendered as proportionality:** *Resolved.* Line 23 now reads: "A signal is worth conditioning the contract on when it is informative about the agent's action [Holmström 1979]."
9. **"Usually trusted" and "can be trusted only as far":** *Resolved.* Line 25 frames the thesis with "We argue that…", and "usually trusted rather than tested" in the abstract is supported by the §1 examples and census.
10. **Compress Table 1 and introductory analogies:** *Acceptable as kept.* Table 1 was already reduced to the 13 rows matching the abstract in Draft 12, and the single agency-cost paragraph in §1 (line 23) earns its space.

---

## 6. Backing

### Twenty-two claims verified against `renavondata/jack` (`e580b64`), `Freeman 2026` (`007a007`), and external sources

1. **Line 21 (`Zhang et al. 2025`, arXiv:2505.22954v3):** DGM raises SWE-bench from 20.0% to 50.0% (abstract) and in App. H (Node 114) removes the special-token logging read by its hallucination detector despite instructions. *Holds.*
2. **Line 21 (`Zhang et al. 2026, App. A.5`, arXiv:2603.19461v2):** Hyperagents keep the evaluator, task data, and parent selection (except in App. E.5) outside the editable boundary "to ensure safety, prevent evaluation gaming" and name pushing that boundary outward as future work. *Holds (with the minor App. E.5 qualification noted below).*
3. **Line 21 (`Chen, Zhu & Zheng 2026`, arXiv:2610.27610v1):** Census of 114 studies (90 self-described RSI) showing evaluation focuses on product rather than process repeatability. *Holds.*
4. **Line 23 (`Kolt 2026b`, arXiv:2603.28669v1):** Direct quote on p. 19: legal alignment "will need to contend with the prospect of actors that shape the very laws that govern them." *Holds.*
5. **Line 56 (`SPEC §10` item 15; `SPEC §5`; `REPORT, C1a §4`):** Promotion evidence (`run`, `runs`, `acts`) is checked only for regular-file presence and SHA-256 hash (`SPEC.md:432–436, 467–470`); resolution schema requires only forecast `seq`, outcome `0` or `1`, and non-empty `evidence` string (`SPEC.md:102`); resolution of forecast `seq 123` was entered as `1` although PR #41 carried no pins (`REPORT.md:371–374`). *Holds.*
6. **Line 84 (`Zhao et al. 2026, Cor. 3`, arXiv:2610.07459v1):** Corollary 3 ("Integrity versus completeness") proves that signatures, hash chains, and checkpoints cannot detect omitted actions ("it cannot show events it never recorded (Corollary 3)"). *Holds.*
7. **Lines 100, 110 (`SPEC §§1–6, 8–9`):** Seven canonical JSON fields, Ed25519 SSHSIG in namespace `core-entry`, and fourteen closed refusal reason codes. *Holds (`SPEC.md:72–84, 138–145, 295–297`).*
8. **Line 126 (`seqs 0, 1, 6, 34, 201`; `CHARTER A2.5`):** `builder-1` (`seq 6`) holds `proposal, spec_conflict`; `builder-2` (`seq 34`) adds `forecast, resolution`; `herald-2` (`seq 201`, after `herald-1` is revoked at `seq 217`) holds `merge` alone; `guy-master` holds `genesis, key, proposal, merge` at `seq 0` and adds `amend, push, decision` at `seq 1`; losing the last `key` power is refused (`kernel/check.py:86–87`). *Holds.*
9. **Line 136 (`SPEC §7`, `SPEC §8` step 8a):** Self-resolution is refused by principal (`self_judged`, `kernel/check.py:82–83`). *Holds.*
10. **Line 146 (`seqs 31, 33`; log at `seq 7809`; `tools/entry.py:score`):** At `seq 7809`, `counsel` has entered `100` forecasts and `guy` `3` (`reviewer` `2,942`; `builder` `26`), scored by `tools/entry.py:score` (lines 122–147); none of counsel's 100 or guy's 3 forecasts is a post-opening C2a value event in `judge/value.py`. *Holds.*
11. **Line 187 (`judge/value.py:113–135`; `judge/entries.py:resolution_rates`; `seqs 550–563`):** `judge/value.py` updates stakes and mixture weights after every event in resolution order; `resolution_rates` updates the Laplace base rate after each resolution entry in `seq` order; `seqs 550–563` are 14 `resolution` entries between `12:15:08Z` and `12:15:58Z` on `2026-11-02`. *Holds.*
12. **Line 191 (`judge/status.py:score_items`; log at `seq 7809`):** `item_process` at `seq 7809` yields `641` items, of which `190` share a timestamp with another item (`188` expiries and `2` batches). *Holds.*
13. **Lines 203, 330 (`Scrivens 2026, Thm. 1`, arXiv:2603.28650v2):** Under power-law risk schedules $\delta_n = O(n^{-p})$ ($p > 1$) and overlapping safe/unsafe distributions, classifier gates satisfy $\sum_n \mathrm{TPR}_n < \infty$. *Holds.*
14. **Lines 215, 221 (`SPEC §10` item 15; `judge/judge.py:installing_push`; `tests/promotion_replay_spot.py`; `seqs 6851, 7281`):** Item 15 judges promotions after the installing push (`seq 7281`, authorised by `grant` at `seq 6851`), exempting `seqs 188` and `337`; `tests/promotion_replay_spot.py` replays 3 rows (`592, 593, 705`) of the 706-row table `spec/vectors/promotion-replay.json`. *Holds.*
15. **Lines 236, 332 (`Iacob et al. 2026, §3.2`, arXiv:2606.26294v3):** RQGM gates evaluator replacement on an evaluator-independent anchor and erases utility records that depended on the displaced evaluator. *Holds.*
16. **Lines 244–245 (`judge/status.py:item_process, window_fixes`):** Non-repair types under the sovereign key are `genesis, key, amend, push, proposal` and `decision` with `kind != "fix"` (lines 111–112); a qualifying `window_fixes` entry is not reported late and its taint lifts at the next `push` (lines 114–123, 371–402); a sovereign resolution or merge scores $Y=0$ and any sovereign entry clears `pending` resolutions (lines 129–136). *Holds.*
17. **Lines 278, 330 (`Sengupta 2026, §4.4`, arXiv:2607.00871v1):** SEA §4.4 states that Alg. 4 (`SGM-CS`) "is the governance layer to deploy first", and §§1, 4, 10 state that the composite guarantees under the endogenous loop remain open conjectures. *Holds.*
18. **Line 278 (Log counts at `seq 7809`):** `seqs 6–8` were declared on `2026-10-19`; builder (`3,410`) and reviewer (`3,211`) keys signed `6,621` of `7,810` entries, comprising `5,919` forecasts and resolutions (`2,968` + `2,951`) and `702` proposals (`625` in blocks carrying world forecasts/resolutions and `77` others). *Holds.*
19. **Line 284 (`seq 0`; `tools/count_kernel.py`; `REPORT §8.1`):** Genesis `seq 0` is at `2026-10-14T05:41:39Z`; Python kernel is `450` lines (`check.py` 138 + `log.py` 172 + `sig.py` 140); `REPORT.md:223` records agreement on `100,000` seeded logs and `658,885` prefixes at C0 exit. *Holds.*
20. **Lines 290–295 (Table 2):** `c0-exit` is a signed git tag; C1a promoted at `seq 188` (`31 Oct`); C1b promoted at `seq 337` (`1 Nov`) with $M = 214358881/8398080 \approx 25.525$ over 9 items at $p_0 = 6/11$; C2a opened at `seq 367` (`1 Nov`), fixed at `seq 5563`; C2a′ opened at `seq 5564` (`17 Nov`), ended by veto at `seq 7180` (`22 Nov`); third window grant at `seq 7615` (`24 Nov`), opening after `2026-11-30T00:00Z`. *Holds.*
21. **Line 316 (`judge/status.py --subject C2a` at `seqs 7180, 7809`):** For C2a′, `judge/status.py` gives `320` procedure to `1,296` object at `seq 7180` (`2026-11-22T11:44:05Z`) and `459` to `1,786` at `seq 7809` (`2026-11-25T11:05:35Z`). *Holds.*
22. **Lines 348, 350 (`transcripts/AUDIT-criteria-20261117.md`):** The audit's fixed 6-dataset lookup table (**F**, line 26) crosses $E \ge 20$ at event 53, and 9 of 28 criteria are classified as `empty` / passable without skill, including liveness (**L**) and ratio padding (**R**) (lines 5, 27–28). *Holds.*

### Statements not genuinely backed or discrepant with their sources

1. **Lines 102–108 — Inaccurate division of what the kernel vs. the judge reads from `State`:**
   - *Line 102 & 105:* Line 102 introduces bullets 103–106 with "The kernel reads from it what it needs to admit or refuse $e_i$ [SPEC §7; `kernel/check.py`]:", and line 105 includes "and of those a `transmute` decision has made mutable". In `kernel/check.py`, `state.transmuted` is recorded at line 99 (`transmuted = transmuted | {body["subject"]}`), **never read by the kernel**. Refusing an untransmuted amendment (`amend_untransmuted`) is enforced by `judge/judge.py` (lines 382–387, `SPEC §10` item 13), as `SPEC §7` (line 224) explicitly says: *"The kernel records them; the judge enforces them (§10.13)."*
   - *Line 108:* "The state also carries each charter digest entered, with its activation height, and the trusted-base digest. The judge derives the charter in force from these; the kernel does not read them." In `judge/judge.py` (lines 143–153, 347–348), the judge never calls `State.charter_at` and never derives the *charter in force* from activation heights; it checks `charter_mismatch` (`SPEC §10` item 2) against the *promulgated* charter (the latest valid `genesis` or `amend` entry's `charter` field, regardless of `activate_at`). `State.charter_at` in `kernel/check.py:19–20` is never called by either the kernel or the judge.

2. **Line 124 — An `amend` entry has two immediate effects at seq $a$, not one:**
   - *What is said:* "An amendment entered at seq $a$ names an activation height $k > a$, which the kernel checks [SPEC §7]. It takes effect at $k$, and has one immediate effect: no push is lawful between $a$ and $k$ [SPEC §10, item 12]."
   - *What is missing:* By `SPEC §7` (line 214) and `SPEC §10` item 2 (`charter_mismatch`, lines 356–360; `judge/judge.py:143–153, 347–348`), entering an `amend` at seq $a$ also immediately changes the *promulgated* charter digest that trunk's `CHARTER.md` must match, before height $k$ is reached.

3. **Line 306 — Forecast counts (`2,795` and `12`) belong to the implementation's 2,820-event set, not the 2,633 events scored by the recomputation protocol:**
   - *What is said:* Under "**The value evidence, recomputed**", line 306 states: "**Forecasters.** Almost all the forecasts come from one party: 2,795 from reviewer sessions and 12 from builders."
   - *What is missing:* In `block_on_log.py` (lines 79–80), `{'reviewer': 2795, 'builder': 12}` counts forecasts across `v["rows"]`—all `2,820` resolved events selected by `judge/value.py` (which includes the 168 late-resolved events and 18 resolved events in the 4 pending sittings). Across the `2,633` in-time resolved events actually scored in the 476 completed sittings of the recomputation protocol (line 303), the counts are **`2,627` from reviewer sessions and `12` from builders** (with 6 events forecast by both).

4. **Line 314 — Internal inconsistency on "on the same events" and inaccurate description of base-rate deadline filtering in the $10^{58}$ ablation:**
   - *What is said:* "The implementation's own per-event figure on the same events, about $1.5 \times 10^{60}$, is not comparable evidence… Holding its stakes, weights and base rates to what was known before each cutoff, and counting only resolutions made by the deadline, still leaves it near $10^{58}$… Compounding, not leakage, accounts for most of the gap, though the ablations do not use exactly the same events."
   - *What is missing:* First, "on the same events" in the first sentence contradicts the final clause of the paragraph: $1.5 \times 10^{60}$ is computed over `2,820` events, whereas the block recomputation and both ablations (`2.492e+58` and `1.739e+10`) are computed over the `2,633` in-time resolved events in the 476 completed sittings. Second, in `block_on_log.py` (lines 103–119), the base-rate function `make_base("type")` used in the $2.492 \times 10^{58}$ ablation (`We`) does **not** filter to "only resolutions made by the deadline"—it includes every resolution in `val.resolution_rates(es)` recorded before cutoff `c` (as line 304 correctly states); only the scored events, mixture weights, and stakes filter out late resolutions.

5. **Line 238 — `kernel2/NOTES.md` at `e580b64` does not document C0's Codex authorship or C1's intermediate revision:**
   - *What is said:* "The second was written without reading the first, from the specification and its test vectors, by Codex at C0 and by Gemini for C1a's changes [REPORT §8; `kernel2/NOTES.md`]."
   - *What is missing:* At `e580b64`, `kernel2/NOTES.md` was overwritten during the C1a update (`7ae10a33`) and records only `google/gemini-4-argon` (`c1a-kernel2`). Moreover, between C0 (where `REPORT §8.2` line 238 credits Codex and `a6f36b4c:kernel2/NOTES.md` names `openai/gpt-6-astra`) and C1a, C1's four new entry types (`amend, push, decision, spec_conflict`) and the last-key guard were added to `kernel2/` at commits `8fcd821c` (`openai/gpt-6-astra`) and `432e3855` (`google/gemini-4-argon`).

6. **Line 21 — Minor omission on parent selection in `Zhang et al. 2026, App. A.5`:**
   - *What is said:* "They keep the evaluator, the task data and parent selection outside the editable boundary 'to ensure safety, prevent evaluation gaming'… [Zhang et al. 2026, App. A.5]."
   - *What is missing:* Appendix A.5 of `Zhang et al. 2026` states that parent selection lies outside the editable boundary *"(except in Appendix E.5)"*, where they test making parent selection editable.

---

## 7. Overclaiming and clarity

Draft 14 is unusually candid about its scope and negative findings: it states up front that no self-modifying agent (C3) exists yet (lines 15, 32, 296, 366), that its statistical propositions apply classic results rather than proving new theorems (line 90), that the block recomputation is a retrospective audit whose evidence vanishes against a per-dataset base rate (lines 15, 30, 300, 310–312), and that 9 of 28 audited window criteria can be passed without skill (§8, line 350).

Two minor points of framing and clarity remain:
- **"Every claim of merit is a forecast" in the abstract and §1 (lines 15, 28, 70):** While §4.2 (line 130) now explains clearly that proposals carry no merit forecast and that "a claim of merit has standing only as a forecast" on the separate forecast ledger, the shorthand in the abstract and Table 1 can still read on first encounter as if every proposal must carry a forecast.
- **What could be cut without loss:** The coded details of `window_fixes` and `pending = []` in §4.5 (lines 244–245), the non-value forecast paragraph in §4.2 (line 146), and the post-veto `459 to 1,786` ratio sentence in §6 (line 316) could all be trimmed by a few lines each to tighten the paper further.

---

## 8. Recommendation

**Accept** (with five minor text corrections for the final version). Every mathematical proposition and proof in §4 is now sound, the Lean 4 formalisation matches its stated scope in §4 and `lean/README.md`, the simulation in §4.3 and the retrospective recomputation in §6 reproduce exactly from the ancillary scripts, and all substantive objections from the seventh referee have been resolved. The remaining items below are sentence-level factual alignment fixes against the repository at `e580b64`.

The five changes that matter most, in order:

1. **Fix the kernel vs. judge state description in §4.1 (lines 102–108):** Move `transmuted` out of the list of fields the kernel reads to admit or refuse $e_i$ (line 105) into line 108 (since `kernel/check.py` only records `state.transmuted` and `judge/judge.py` enforces `amend_untransmuted` under `SPEC §10` item 13), and correct line 108 to say that the judge checks the *promulgated* charter (`SPEC §10` item 2) rather than deriving the charter in force from activation heights.
2. **Harmonise the event counts and base-rate description in §6 (lines 306 and 314):** Clarify on line 306 that `2,795` reviewer and `12` builder forecasts are the counts across the implementation's `2,820` events (`2,627` and `12` across the `2,633` in-time resolved events scored by the block protocol); replace "on the same events" at the start of line 314 with "on its 2,820 selected events"; and note on line 314 that deadline filtering in the $10^{58}$ ablation applies to the scored events, weights, and stakes (while base rates use all pre-cutoff resolutions, as stated at line 304).
3. **Note the second immediate effect of an amendment in §4.1 (line 124):** State that an `amend` entry at seq $a$ also immediately updates the promulgated charter digest checked by the judge (`SPEC §10` item 2), in addition to forbidding pushes between $a$ and $k$ (`SPEC §10` item 12).
4. **Update the `kernel2` provenance sentence in §4.4 (line 238):** Note that C1's opening entry types were also added between C0 and C1a, and that C0's authorship is recorded in `REPORT §8.2` and historical commits of `kernel2/NOTES.md` (since `e580b64:kernel2/NOTES.md` records only the C1a revision).
5. **Trim the implementation-specific edge cases in §4.5 (lines 244–245) and qualify `Zhang et al. 2026` in §1 (line 21):** Shorten the `window_fixes` taint-lifting and pending-resolution clearing details in §4.5 to a parenthetical pointer to `judge/status.py`, and note parenthetically at line 21 that Hyperagents keep parent selection fixed except in their Appendix E.5 experiment.

RECOMMENDATION: accept
exit=0
```

