# Cold read 10 of the claim paper: report and disposition

- **Reader:** `google/gemini-4-argon`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1381. The session ran from 09:02Z to 09:37Z on 26 November.
- **Text read:** draft 20, at `4eda7b8`. The prompt listed every claim added in drafts 16–20 and asked for each to be checked against the record.
- **Verdict:** **accept**, with five clarifications. The reader checked 24 claims against `e580b64`, the runner and the literature. It re-ran the four per-window ratios in a temporary extraction, and recounted the runner sessions by model itself (about 84%).
- **Draft 21** makes the five clarifications. The disposition comes first; the report follows verbatim.

## Disposition

| Point | What draft 21 does |
|---|---|
| p₀ = 6/11 is not the brief's own replay | Now: measured on the builders' record through seq 163 and committed before the window; the more demanding of two attributions, since the brief's own rule gives 5/11. |
| Title counts | Now 627 stream batches (adding the five `M2 race` titles) and 75 others, 46 of them reads and reviews (the two read-gate proposals moved out). |
| Gemini's kernel2 revision did not touch the C1 code | Now: "that code stands: the Google revision that followed added only the last-key guard" (`git diff 8fcd821 432e385`). The first kernel's C1a author is cited from the REPORT. |
| The 14-day clause of the fourth falsifier | Computed over every full 14-day interval. One exceeds 5 : 1: the first, from genesis, at 63 : 5, before any key could forecast. From C1a's opening on, the worst is 871 : 1,755. The section's lead now says this falsifier was met once, on a literal reading, rather than "none has been met". |
| Trim the §4.2 aside | Cut to two sentences, tied to §6's stream: the stream's forecaster is a fixed template, model and prompt. |

## The report (verbatim, from §1 of the reader's final message)

## 1. The one idea

A self-modifying AI agent can be trusted only as far as an institution outside its reach can test it, and that judging institution must itself be built before the agent, imposed first on the model sessions that build it, and granted authority layer by layer only through valid sequential tests on its own signed record. Because the institution keeps a book on itself rather than a proof of itself, replacing the natural per-event value test (which loses its level under simultaneous batch resolution) with a valid block test reveals that the reference implementation's first evidence of predictive value rested on a weak type-pooled baseline and vanishes against a per-dataset base rate.

**Does the abstract state it, and does the body deliver it?** Yes to both. The abstract follows the four-sentence form fixed in `ABSTRACT-FIRST.md`—the problem and classical limits (Rice, Löb, Goodhart), the institutional design (law as a fold over a signed log, claims of merit counted only as log-scored forecasts, conjunctive sequential promotion on repair-free liveness and predictive value before the agent exists), the six propositions with their Lean-checked statistical core and block-valid correction, and the negative retrospective finding on the public record—and §§1–9 deliver each part in order.

**What in the body does not serve it:**
1. **Repository plumbing around the C2a′ commit-walk bug (§4.4, line 220; §6, line 297):** The specifics of criterion 3's all-ancestor vs. first-parent git walk and the three pin row indices (`300, 400 and 593` of `706`) document CI mechanics rather than the paper's statistical or institutional thesis.
2. **The non-value forecast paragraph in §4.2 (line 145):** Remarking that a forecast belongs to a procedure rather than a mind and noting that counsel and the operator also forecast outside §6's value events is an aside that does not advance the main argument.

---

## 2. Correctness

All line numbers below refer to `draft.md` at commit `4eda7b89e64d712b2e83aa85f7412e0820af7900`.

- **Proposition 1 (prospectivity, lines 113–122):** *Correct.*
  - *Part (a):* Because $S_i$ is a function of $e_0, \dots, e_{i-1}$ alone, $V(S_i, e_i)$ depends only on $e_0, \dots, e_i$, so appending $M$ to a valid log $L$ cannot alter the verdict on any entry of $L$.
  - *Part (b):* Requiring both logs $L$ and $L^* \neq L$ to be linked and numbered by position from $0$ (`seq` $= i$) makes the backward-induction reduction to a SHA-256 collision valid. Comparing backwards from the terminal lines (which both hash to $h$), either two distinct lines share a hash at the current step or they are identical and therefore share their `parent` hash; if the logs have different lengths, their terminal lines already differ in `seq` (and the backward walk reaches `seq = 0` paired with `seq > 0`), yielding a collision.

- **Proposition 2 (propriety; no self-judgement, lines 131–138):** *Correct.*
  - *Part (a):* For $\pi \in (0,1)$, $g(p) = \pi\ln p + (1-\pi)\ln(1-p)$ has $g'(p) = (\pi - p)/(p(1-p))$ and $g''(p) = -\pi/p^2 - (1-\pi)/(1-p)^2 < 0$ on $(0,1)$, so $p = \pi$ is the unique continuous maximiser. By strict concavity on $(0,1)$, restricting $p$ to $\{1, \dots, 999\}/1000$ places the maximum at a grid point adjacent to $\pi$ (or at the nearer boundary $0.001$ or $0.999$ when $\pi \notin [0.001, 0.999]$), with ties possible between the two grid points bracketing $\pi$.
  - *Part (b):* Enforced by construction in `SPEC §8` step 8a (`self_judged`, `kernel/check.py:82–83`), which compares the resolution's `proposer` against the recorded `proposer` of its forecast after step 8 verifies that `proposer` equals the signing key's registered `principal`. The caveats on performativity, inter-principal collusion, and non-linear downstream rewards (lines 139–141) are well stated.

- **Proposition 3 (value, lines 153–180):** *Correct.*
  - *Setup and bounds:* For any non-empty resolved subset $R_m \subseteq B_m$, clipping all $p_{k,i}, b_i$ to $[10^{-3}, 1 - 10^{-3}]$ bounds each member's product likelihood $\prod_{i \in R_m} p_{k,i}(Y_i)$ and their convex combination $Q_m(Y_{R_m})$ within $[10^{-3|R_m|}, (999/1000)^{|R_m|}]$. Dividing $\ln Q_m(Y_{R_m}) - \sum_{i \in R_m} \ln b_i(Y_i)$ by $|R_m|\ln 999$ gives $\bar D_m \in [-1, 1]$ (and factor $1$ when $R_m = \varnothing$).
  - *Sufficient condition (line 169):* Conditioning on both $\mathcal G_{m-1}$ and which events resolve ($R_m$) fixes the divisor $|R_m|$, so non-positive conditional expected joint log-score advantage given $(\mathcal G_{m-1}, R_m)$ implies $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 0$ by the tower property. Line 169 rightly notes that without conditioning on $R_m$ this implication can fail because $|R_m|$ is random.
  - *Part (a):* Under assumption (A), $\lambda_m \in [0, 1 - 1/(m+1)] \subset [0,1)$ is $\mathcal G_{m-1}$-measurable and $1 + \lambda_m \bar D_m \ge 1 - \lambda_m > 0$. Under $H_0^{\mathrm{val}}$, $\mathbb E[1 + \lambda_m \bar D_m \mid \mathcal G_{m-1}] = 1 + \lambda_m \mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 1$, so $W_t$ is a non-negative supermartingale with $W_0 = 1$, and Ville's inequality gives $\Pr(\sup_t W_t \ge 1/\alpha) \le \alpha$. For overlapping sittings split online into lag classes $\ell = 1, 2, \dots$ with thresholds $\ell(\ell+1)/\alpha$ (line 153), the union bound gives $\sum_{\ell \ge 1} \alpha/[\ell(\ell+1)] = \alpha$.
  - *Part (b):* With uniform prior weights $w_{k,1} = 1/K$ and posterior updates along the same sequence of blocks, $\prod_{m \le t} Q_m(Y_{B_m}) = K^{-1}\sum_{k=1}^K \prod_{m \le t}\prod_{i \in B_m} p_{k,i}(Y_i) \ge K^{-1}\max_k \prod_{m \le t}\prod_{i \in B_m} p_{k,i}(Y_i)$. Taking logs and subtracting $\sum_{m \le t}\sum_{i \in B_m}\ln b_i(Y_i)$ gives the first inequality, and inclusion of the base-rate forecaster in the roster makes the maximum at least $0$, giving $\ge -\ln K$.

- **Remark and Example in §4.3 (lines 182–185):** *Correct and reproduced.*
  - The Remark accurately explains why per-event betting in resolution order fails under a cutoff-time null when outcomes within a sitting are dependent (later bets condition on earlier outcomes of the same sitting), why freezing stakes at the cutoff is insufficient without conditional independence ($\mathbb E[\prod_{i \in B_m}(1 + \lambda_m D_i) \mid \mathcal G_{m-1}]$ need not be $\le 1$ when factors are positively correlated), and why the mixture of product forecasts can capture within-sitting dependence whereas the product of marginals $\prod_{i \in B_m} q_i(Y_i)$ would lose Proposition 3(b)'s $\ln K$ regret bound.
  - Line 184 explicitly labels the Example as an isolated betting counterexample with a single randomised product forecaster ($q \in \{0.95, 0.05\}$ equiprobably, $b = 1/2$, shared fair outcome $Y \sim \mathrm{Bern}(1/2)$), for which $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] = \frac{1}{2}(\ln 1.9 + \ln 0.1)/\ln 999 \approx -0.1202 < 0$. Running `sim_filtration.py` reproduces every figure:
    - Default ($n = 20$, $300$ sittings, $4{,}000$ runs, $\alpha = 0.05$): per-event crossing rate `0.1325` (13%), block crossing rate `0.0000`.
    - $n = 50$ (`50 0.45 200 2000`): per-event crossing rate `0.5035` (50%), block crossing rate `0.0000`.
    - Independent outcomes (`--independent`, $n = 20$ and $n = 50$): per-event crossing rate `0.0000`.
    - Roster mode (`--roster 20 300 2000`): `0.2850` (implementation form) vs. `0.0000` (block form); as the script's docstring notes, the three-member roster $(0.5, 0.95, 0.05)$ is not a true null for the joint score because the mixture captures the shared-outcome dependence at $m = 1$ ($\mathbb E[\bar D_1] \approx +0.085 > 0$).

- **Proposition 4 (liveness, with wealth carried across windows, lines 192–201):** *Correct.*
  - *Part (a):* Since $0 \le s_j \le n_j$, $\hat q_j = (s_j+1)/(n_j+2) \in (0,1)$, so $\lambda_j = \max(0, (\hat q_j - p_0)/(p_0(1-p_0))) \in [0, 1/p_0)$. For $Y_j \in \{0,1\}$ (or simultaneous-item mean $\bar Y_j \in [0,1]$), $1 + \lambda_j(Y_j - p_0) \ge 1 - \lambda_j p_0 > 0$ and $\mathbb E[1 + \lambda_j(Y_j - p_0) \mid \mathcal F_{j-1}] \le 1$ under $H_0^{\mathrm{live}}$. Continuing the same product across failed windows makes every window end a stopping time of one non-negative supermartingale, so Ville's inequality bounds the lifetime false-crossing probability by $\alpha$.
  - *Part (b):* For $k$ restarted windows with false-crossing probabilities $r_j \le \alpha$, independence gives $1 - \prod_{j=1}^k(1-r_j) \le 1 - (1-\alpha)^k$ (attained when $r_j = \alpha$), and the union bound gives $\sum_{j=1}^k r_j \le k\alpha$.

- **Proposition 5 (conjunctive promotion, lines 206–209):** *Correct.*
  - Because promotion requires $W_t \ge 1/\alpha$ and $M_t \ge 1/\alpha$ at the same prefix $t$, the promotion event lies in $\{\sup_t W_t \ge 1/\alpha\} \cap \{\sup_t M_t \ge 1/\alpha\}$ and has probability at most $\alpha$ whenever $H_0^{\mathrm{val}}$ or $H_0^{\mathrm{live}}$ holds (Berger's intersection–union principle).

- **Proposition 6 (replay-bound change, lines 223–234):** *Correct.*
  - Parts (a), (b), and (c) follow directly from the replay admission condition on $R^+$, `SPEC §10` item 15's dispatch to the evaluator in force at the promotion's `seq`, and the fact that agreement on finitely many inputs constrains nothing outside $R^+$ or under different evidence files.

---

## 3. The Lean files

I inspected `lean/README.md` and all seven files under `lean/Claimproofs/`. I have not run `lake build` to verify compilation against Mathlib; by inspection, no file contains `sorry` or non-standard axioms.

1. **`HashChain.lean` (`Claim.collision_of_ne`) $\leftrightarrow$ Proposition 1(b):**
   - *Comparison:* Faithful to the combinatorial reduction. Logs are represented backwards as non-empty lists `x :: xs : List α` with abstract functions `hash parent : α → β` and `seq : α → ℕ`. `RevLinked` requires `parent x = hash y` for adjacent elements (leaving genesis's `parent` unconstrained, a weaker hypothesis that strengthens the theorem), and `RevNumbered` requires `seq x = rest.length`. It proves that `hash x = hash x'` and `x :: xs ≠ x' :: xs'` imply `∃ a b, a ≠ b ∧ hash a = hash b`.
   - *Differences:* `parent` and `seq` are total functions on abstract entries (abstracting away JSON parsing and SHA-256), the conclusion does not state list-membership of the collision witnesses `a, b`, and the computational-adversary sentence of Prop. 1(b) is informal context.

2. **`Propriety.lean` (`Claim.log_score_proper`, `Claim.log_score_strict`) $\leftrightarrow$ Proposition 2(a):**
   - *Comparison:* Proves that for $\pi, p \in (0,1)$, `expScore π p ≤ expScore π π`, with strict inequality when `p ≠ π`, using `Real.log_le_sub_one_of_pos` and `Real.log_lt_sub_one_of_pos`.
   - *Differences:* Proves strict propriety (unique global maximum at $p = \pi$) rather than strict concavity ($g'' < 0$) or the per-mille grid clause. Both omissions are explicitly disclosed at lines 91–92 and in `lean/README.md`.

3. **`Mixture.lean` (`Claim.prod_Q`, `Claim.regret`, `Claim.regret_base`) $\leftrightarrow$ Proposition 3(b):**
   - *Comparison:* For abstract block likelihoods `P : Fin K → ℕ → ℝ` with `0 < K` and `∀ k m, 0 < P k m`, defines uniform-prior posterior mixture likelihoods `Q P T = S P (T + 1) / S P T`, proves `∏ m ∈ range T, Q P m = S P T / K` (`prod_Q`), proves `∀ k, ∑ m ∈ range T, log (P k m) - log K ≤ ∑ m ∈ range T, log (Q P m)` (`regret`), and proves that if `∀ m, P k₀ m = B m` then `-log K ≤ ∑ m ∈ range T, (log (Q P m) - log (B m))` (`regret_base`).
   - *Differences:* Assuming only `0 < P k m` is weaker (more general) than clipped per-mille product probabilities; the within-block product $\prod_{i \in B_m} p_{k,i}(Y_i)$, the identity $|B_m|\ln 999\,\bar D_m = \ln Q_m - \ln B_m$, and packaging `∀ k` into $\max_k$ are informal bridges (disclosed at line 91).

4. **`Ville.lean` (`Claim.ville_finite`) and `Wealth.lean` (`Claim.wealth_supermartingale`, `Claim.wealth_level`, `Claim.value_factor`, `Claim.liveness_factor`) $\leftrightarrow$ Propositions 3(a) and 4(a):**
   - *Comparison:* `ville_finite` proves the finite-horizon maximal inequality $\varepsilon \cdot \mu\{\omega \mid \varepsilon \le \max_{k \le n} W_k(\omega)\} \le \mathbb E[W_0]$ for any non-negative supermartingale `W` under a finite measure `μ`, via Mathlib's `expected_stoppedValue_mono` applied to `-W` and the bounded hitting time `hittingBtwn`. `wealth_supermartingale` and `wealth_level` prove that `wealth L D` is a non-negative supermartingale satisfying $\varepsilon \cdot \mu\{\omega \mid \varepsilon \le \max_{k \le n} \mathrm{wealth}_{L,D}(k,\omega)\} \le 1$ under a probability measure whenever `0 ≤ L ≤ M`, `|D| ≤ B`, `0 ≤ 1 + L * D ≤ C`, `D n` is `𝒢 n`-strongly measurable, `L (n+1)` is `𝒢 n`-strongly measurable (predictable), and `μ[D (n+1) | 𝒢 n] ≤ᵐ[μ] 0`. `value_factor` and `liveness_factor` prove the scalar bounds $1 + l d \in [0,2]$ and $1 + l(y - p_0) \in [0, 1/p_0]$.
   - *Differences:* (i) Proved for every finite horizon $n$ rather than $\sup_{t \in \mathbb N}$ (which follows by monotone continuity of measure). (ii) The plug-in stake formulas $\lambda_m, \lambda_j$ and their strict upper bounds ($< 1$ and $< 1/p_0$) are abstracted into bounded predictable `L` and non-negative factors `0 ≤ 1 + L * D`. (iii) The conditional-expectation null `μ[D (n+1) | 𝒢 n] ≤ᵐ[μ] 0` is taken as a hypothesis without formalising the conditioning on the random resolved subset $R_m$. All are disclosed at lines 91–95 and in `lean/README.md`.

5. **`Restart.lean` (`Claim.restart_independent`, `Claim.restart_union`) $\leftrightarrow$ Proposition 4(b):**
   - *Comparison:* `restart_union` proves the measure-theoretic union bound $\mu(\bigcup_{j \in \mathrm{Fin}\,k} A_j) \le k\alpha$ from $\forall j, \mu(A_j) \le \alpha$. `restart_independent` proves the real-number inequality $1 - \prod_{j \in \mathrm{Fin}\,k}(1 - r_j) \le 1 - (1 - \alpha)^k$ under $\forall j, r_j \le \alpha$ and $\alpha \le 1$.
   - *Differences:* As line 91 and `lean/README.md` disclose, `restart_independent` is pure real algebra and does not formalise independent events or the attainment clause for exact tests ($r_j = \alpha$).

6. **`Conjunctive.lean` (`Claim.conjunctive_promotion`) $\leftrightarrow$ Proposition 5:**
   - *Comparison:* Proves that `Promote ⊆ CrossW`, `Promote ⊆ CrossM`, and `μ CrossW ≤ α ∨ μ CrossM ≤ α` imply `μ Promote ≤ α`.
   - *Differences:* Takes the component crossing bounds as hypotheses rather than chaining `wealth_level`, as disclosed at line 91.

---

## 4. The recomputation

Running `curl -sL $U/block_on_log.py | python3 - --rev e580b64` reproduces every figure in §6 (lines 300–313):
- **Implementation baseline:** `2820` resolved value events; roster `['guy', 'counsel', 'reviewer', 'builder', 'base']`; implementation per-event wealth `E = 1.51983e+60` ($1.52 \times 10^{60}$); forecasts by party in those 2,820 events: `{'reviewer': 2795, 'builder': 12}`.
- **Sittings and deadlines:** Observed to `2026-11-25T11:05:35Z` (`seq 7809`), `476` completed sittings and `4` pending sittings; `2803` member events in completed sittings ($2803 / 476 \approx 5.89 \approx 5.9$ per sitting), of which `170` expired unresolved at their deadline (`168` resolved only after their deadline), leaving `2,633` in-time resolved events scored; `19` resolved events had no forecast before their cutoff and are excluded from sitting membership.
- **Lag classes:** `5` classes with total sittings `[216, 196, 48, 16, 4]` and scored sittings `[215, 195, 47, 15, 4]`; thresholds $\ell(\ell+1)/\alpha = [40, 120, 240, 400, 600]$ at $\alpha = 0.05$.
- **Pooled by event type:** Final wealth by class `['1.993e+04', '1.109e+04', '3.009', '1.159', '1.022']` ($1.99 \times 10^4$ and $1.11 \times 10^4$ for classes 1 and 2); running maxima `['1.993e+04', '1.19e+04', '3.009', '1.159', '1.022']` ($1.19 \times 10^4$ peak for class 2); classes 1 and 2 cross their thresholds (`40` and `120`).
- **Ablations and orders-of-magnitude split (pooled by type):** Per-event with stakes, weights, and base rates frozen before each cutoff and scoring only timely resolutions gives `2.492e+58` ($2.49 \times 10^{58}$); single block process without lag classes gives `1.739e+10` ($1.74 \times 10^{10}$). In base-10 logarithms, the 55.88-order-of-magnitude drop from $1.51983 \times 10^{60}$ to $1.993 \times 10^4$ decomposes as $1.79 \approx 1.8$ (leakage and late resolutions), $48.16 \approx 48.2$ (compounding one bet per event vs. one per sitting), and $5.94 \approx 5.9$ (splitting into lag classes), matching line 313.
- **Kept per dataset:** Final wealth `['0.9989', '0.9998', '1', '1', '1']`; running maxima `['1', '1', '1', '1', '1']`; no class ever exceeds $1$.

**Is the method in `block_on_log.py` valid as §4.3 and §6 describe it?** Yes, for the sequential test of Proposition 3(a) in the recorded-timestamp filtration. Each event enters sitting $c$ only if forecast before $c$, with deadline equal to the maximum `resolves_by` among those pre-cutoff forecasts (line 94). A sitting's completion instant $\tau(B_c) = \max_{e \in B_c} \min(t_{\mathrm{res}}(e), d_{\mathrm{deadline}}(e))$ satisfies $\tau(B_{c'}) < c$ if and only if every member event of $c'$ either resolved in time before $c$ or had its pre-committed deadline pass before $c$. Both conditions are determined by the log before $c$, so greedy lag-class assignment over all sittings (`all_order`, lines 138–145) is $\mathcal G_{m-1}$-measurable (I verified directly across intermediate cutoffs `as_of = c` that `assign[c']` for $c' \le c$ never changes as later outcomes arrive) and satisfies assumption (A) within each class. At cutoff $c$, mixture weights `w`, base rates `base(key, c)`, and class stakes `stake(S[i], Q[i], M[i])` use only information recorded strictly before $c$, and empty resolved blocks ($R_m = \varnothing$) contribute factor $1$ without advancing `M[i]`, matching lines 302–304.

---

## 5. The revisions

All points raised by the ninth referee (`REVIEW-cold-9.md`) were resolved in Draft 20:

1. **Line 264 (formerly 265), proposals "its own ledger scored", and line 151 (formerly 152), universal statistical coverage:** *Resolved.* Line 264 now says the institution was "built from proposals that its own kernel admitted and its own judge checked, while every forecast made along the way was scored on its own ledger." Line 151 now specifies exact operational coverage (the two brief-named streams in `judge/value.py` for value; timely resolution of every forecast with operator entries as candidate repairs for liveness; wealth carried from the first window).
2. **Line 22 (formerly 23), categorical loss of informativeness under Holmström, and lines 14, 20, 277, frequency of untested evaluators:** *Resolved.* Line 22 now reads "how informative the signal is becomes the agent's choice." Line 14 narrows the abstract to "in the leading examples the evaluator that judges them is held fixed and trusted rather than tested," line 277 says "The leading self-improving systems," and line 20 adds the exact census figure from Chen, Zhu & Zheng [2026] (22% of the 90 self-described RSI studies audit two or more reruns of the full loop).
3. **Line 311 (formerly 312), "nothing on the record so far shows any" further skill:** *Resolved.* Line 311 now reads: "Failing to reject does not show that there is no further skill. But this recomputation finds none, and a fixed table of one probability per dataset also beats the pooled base rate (§8)."
4. **Lines 184 and 302, audit recipe details and labelling the Example:** *Resolved.* Line 302 now states the maximum-`resolves_by` deadline rule and that an empty resolved sitting contributes factor 1 without advancing its class's stake count; line 184 explicitly labels the Example as "a single randomised forecaster, not the mixture of Proposition 3; it isolates the betting."
5. **Line 335, specification vs. enforcement in §7:** *Resolved.* Line 335 now reads: "Our specification allows change only by replay of past verdicts, with every change to them marked in advance (Proposition 6); CI enforces three rows of the replay (§4.4)."

---

## 6. Backing

### Twenty-four claims checked against `renavondata/jack` at `e580b64`, `renavondata/opencode-runner`, and external sources

1. **Line 20 (`Chen, Zhu & Zheng 2026`, arXiv:2610.27610v1; `Zhang et al. 2025`, arXiv:2505.22954v3; `Zhang et al. 2026`, arXiv:2603.19461v2):** The abstract of arXiv:2610.27610v1 reports full-text coding of 114 eligible studies, including 90 self-described RSI studies of which "Only 22% audit two or more reruns of the full loop." DGM raises SWE-bench from 20% to 50% and removes hallucination-detector markers in App. H; Hyperagents App. A.5 keeps the evaluator, task data, and (except in App. E.5) parent selection outside the editable boundary "to ensure safety, prevent evaluation gaming." *Holds.*
2. **Line 22 (`Kolt 2026b`, arXiv:2603.28669v1):** Direct quote on p. 19 ("will need to contend with the prospect of actors that shape the very laws that govern them"). *Holds.*
3. **Line 55 (`SPEC §10`, item 15; `SPEC §5`; `REPORT`, C1a §4):** `SPEC.md:432–435, 467–470` checks promotion evidence only for presence and SHA-256 hash under operator attestation; `SPEC.md:102` checks only that a resolution names a forecast, an outcome in `{0,1}`, and a non-empty evidence string; `REPORT.md:371–374` documents that the wrong resolution of forecast `seq 123` stands in the score. *Holds.*
4. **Line 83 (`Zhao et al. 2026, Cor. 3`, arXiv:2610.07459v1):** Corollary 3 ("Integrity versus completeness") states that cryptographic integrity of recorded entries cannot detect omitted events. *Holds.*
5. **Lines 99–109, 123, 135 (`SPEC §§1–9`; `SPEC §10`, items 2, 12, 13; `kernel/check.py`):** Seven canonical JSON fields, fourteen refusal reasons, principal-based `self_judged` refusal at step 8a, `State` fields read by `kernel/check.py` vs. `transmuted` and promulgated-charter digest enforced by `judge/judge.py`, and both immediate effects of an `amend` entry (promulgated charter match and push freeze up to `activate_at`). *Holds.*
6. **Line 186 (`judge/value.py:113–135`; `judge/entries.py:resolution_rates`; `seqs 550–563`):** `judge/value.py` updates stakes and weights after each resolved event; `resolution_rates` updates the pooled Laplace rate in `seq` order; `seqs 550–563` are 14 `resolution` entries between `12:15:08Z` and `12:15:58Z` on `2026-11-02`. *Holds.*
7. **Line 190 (`judge/status.py:item_process, score_items`; log at `seq 7809`):** Running `item_process` on `e580b64:log.jsonl` (with `after_seq=188` and `window_fixes`) yields `641` items, of which `190` share a timestamp with another item (`188` of kind `expiry` and `2` of kind `batch`). *Holds.*
8. **Lines 202, 333 (`Scrivens 2026, Thm. 1`, arXiv:2603.28650v2):** Theorem 1 proves that under power-law risk schedules $\delta_n = O(n^{-p})$ ($p > 1$) and distribution overlap, classification gates have finite total true-positive rate $\sum_n \mathrm{TPR}_n < \infty$. *Holds.*
9. **Lines 214, 220 (`SPEC §10`, item 15 and "The promotion evaluator"; `judge/judge.py:installing_push`; `pins/replay.py`; `.github/workflows/tests.yml`; `transcripts/sessions/c2a-3-replay.md`; `seqs 188, 337, 6851, 7281`):** `installing_push` finds `seq 7281` (authorised by `grant` at `seq 6851`), exempting `seqs 188` and `337`; `spec/vectors/promotion-replay.json` has `706` rows; `pins/replay.py` (line 49, run by `pins/run.py` in `.github/workflows/tests.yml`) replays rows `300, 400 and 593`; `transcripts/sessions/c2a-3-replay.md` defines the reviewer's full-replay session. *Holds.*
10. **Lines 235, 335 (`Iacob et al. 2026, §3.2`, arXiv:2606.26294v3):** RQGM §3.2 gates evaluator replacement on an evaluator-independent ground-truth anchor and performs selective erasure of utility records dependent on the displaced evaluator. *Holds.*
11. **Line 237 (Kernel authorship in `kernel/` and `kernel2/`; `kernel2/NOTES.md` at `a6f36b4`, `8fcd821`, `432e385`; absence of ruling on C1 lapse):** At C0, `kernel/` was written by `claude-fable-5-1` (Anthropic) and `kernel2/` (`a6f36b4`) by `openai/gpt-6-astra` (OpenAI). On 18 October, C1's four new entry types (`amend, push, decision, spec_conflict`) were written into `kernel/` at `2b6b835` by `openai/gpt-6.1-sol` and into `kernel2/` at `8fcd821` by `openai/gpt-6-astra` (both OpenAI), followed by `432e385` (`google/gemini-4-argon`). Searching all files under `transcripts/`, `CHARTER.md`, `SPEC.md`, and `REPORT.md` at `e580b64` confirms that no ruling, waiver, or finding addresses the same-family C1 authorship lapse. *Holds (with the two precision nuances noted below).*
12. **Lines 242–246 (`CHARTER §7`; `judge/status.py:item_process, window_fixes`; `transcripts/BRIEF-C2a-draft.md`, criterion 7):** Confirmed against `judge/status.py:111–136` and `BRIEF-C2a-draft.md:197`. *Holds.*
13. **Line 264 (`RUNBOOK.md`, `jack key`; `key` entries in `log.jsonl`):** `e580b64:log.jsonl` contains `19` entries of type `key` (at `seqs 1, 6, 7, 8, 22, 23, 31, 32, 33, 34, 48, 49, 51, 82, 201, 216, 217, 2254, 2255`), `14` of them before the first promotion at `seq 188`. `RUNBOOK.md:80–86` confirms that `forecast` and `resolution` powers were granted at `seqs 31–34` as C1a opened, and `herald-2` (`seq 201`) moved the merge key off counsel's session. *Holds.*
14. **Line 268 (`CHARTER A2.10` quotation):** Exact match to `CHARTER.md:298–300`. *Holds.*
15. **Line 272 (`transcripts/BRIEF-C1b-draft.md`, "Null"):** `BRIEF-C1b-draft.md:123` commits $p_0 = 6/11$ before C1b's window opened from the replay through `seq 163`. *Holds (with the attribution nuance noted below).*
16. **Line 277 (`Sengupta 2026, §4.4`, arXiv:2607.00871v1; log counts at `seq 7809`):** SEA §4.4 calls Alg. 4 (`SGM-CS`) "the governance layer to deploy first." In `e580b64:log.jsonl` (`7,810` entries, `seqs 0–7809`), `seqs 6–8` were declared on `2026-10-19`; builder (`3,410`) and reviewer (`3,211`) keys signed `6,621` entries, consisting of `5,919` forecasts and resolutions (`2,968` + `2,951`) and `702` proposals (`622` titled as freshness/`world.hkjc` stream batches and `80` others). *Holds (with the title-count nuance on the 80 others noted below).*
17. **Line 283 (`seq 0`; `tools/count_kernel.py`; `REPORT §8.1`):** Genesis `seq 0` is at `2026-10-14T05:41:39Z` with `CHARTER.md` SHA-256 `383867d0…`; Python kernel is `450` physical lines (`check.py` 138 + `log.py` 172 + `sig.py` 140); `REPORT.md:223` records agreement on `100,000` seeded logs and `658,885` prefixes at C0 exit. *Holds.*
18. **Lines 285–297 (Table 2 and C2a's nine repair rows; `transcripts/evidence/acts-20261103T2144.csv`; `transcripts/BRIEF-C2a-prime-draft.md:56–66`; `transcripts/BRIEF-C2a-3-draft.md`):** `acts-20261103T2144.csv` contains exactly nine rows with `class == "repair"`: one `issue event (convert_to_draft)` on `#236` (the operator's own act at counsel's request), one `re-run judge` (`41452947275`), one `PR closed unmerged` on `#236` (closed by a keyword), three `label added (documentation)` on `#243, #244, #245`, and three `own issue closed` on `#243, #244, #245` (whose hand could not be established). This matches `BRIEF-C2a-prime-draft.md:58–65` and line 297. *Holds.*
19. **Line 305 (`world.renavon` forecasting model in `log.jsonl` at `seq 7809`):** Of the `2,887` forecasts with `body.type == "world.renavon"`, `2,869` have `body.args.model` present (`18` have no `model` key), and all `2,869` equal `"openai/gpt-5.4-mini"`. *Holds.*
20. **Lines 315–319 (Four falsifiers of `CHARTER §12`; `git log -S'body["kind"] != "fix"' e580b64 -- judge tools`; `judge/status.py --as-of`):** All four quotations match `CHARTER.md:187–190` verbatim. `git log -S'body["kind"] != "fix"' e580b64 -- judge tools` returns the single commit `879caf93` (`2026-10-31`). Running `judge/status.py` on a temporary extraction of `e580b64` at the four window timestamps reproduces `127 : 32` for C1a (`2026-10-31T10:42:10Z`), `67 : 82` for C1b (`2026-11-01T11:31:58Z`), `1131 : 3449` for C2a (`2026-11-15T15:04:14Z`), and `320 : 1296` for C2a′ at its veto (`2026-11-22T11:44:05Z`). *Holds (see item 4 below on 14-day intervals).*
21. **Lines 351–353 (`transcripts/AUDIT-criteria-20261117.md`):** Line 26 of the audit constructs the fixed per-dataset table **F** crossing $E \ge 20$ at event 53, and line 5 classifies 9 of 28 criteria as `empty` (passable without skill), including liveness (**L**) and ratio padding with unanswered forecasts (**R**). *Holds.*
22. **Line 363 (`log.jsonl` at `seq 7809`):** Zero entries in `log.jsonl` have `type == "rule"`. *Holds.*
23. **Line 381 (Disclosure: `CHARTER.md` head; commit trailers of `SPEC.md`; single book citation `Freeman 2026`):** `CHARTER.md:3` credits Claude (`claude-opus-5-5`); `git log e580b64 -- SPEC.md` carries Claude trailers (`claude-fable-5-1`, `claude-fable-5-2`, `claude-opus-5-5`); `[Freeman 2026]` is cited once in the body (line 381, as provenance in the Disclosure) and listed in References (line 411). *Holds.*
24. **Line 381 (Disclosure: share of runner sessions by model in `renavondata/opencode-runner`):** Querying all issues of `renavondata/opencode-runner` via `gh api` up to `e580b64` (`2026-11-25T11:05:35Z`), of the `853` `builder:` and `reviewer:` session issues whose titles name a model (`868` including `build`/`resolver`/`review by pins` variants), `720` name `gpt-5.4-mini` ($84.4\%$, or $82.9\%$ of $868$; across all $881$ builder/reviewer issues up to `2026-11-26`, $741/881 = 84.1\%$), matching "about four in five." *Holds.*

### Statements with minor backing gaps or source discrepancies

1. **Line 272 — Provenance of $p_0 = 6/11$ in `transcripts/BRIEF-C1b-draft.md` ("Null", lines 123–130):**
   - *What is said:* "C1b's null, $p_0 = 6/11$, is the Laplace rate of timely, repair-free items on the builders' record through seq 163, committed before C1b's window opened [`transcripts/BRIEF-C1b-draft.md`, 'Null']."
   - *What is missing:* `BRIEF-C1b-draft.md` (lines 123–130) explains that the nine items through `seq 163` are four expired writs and five herald batches, and that under the brief's adopted repair-attribution rule (tainting *every* open writ, which §4.5 line 244 and `item_process` implement), one batch (`merge 110`) is tainted, giving four successes and a Laplace rate of **$5/11$**. The figure $6/11 = (5+1)/(9+2)$ was the Laplace rate under an earlier superseded draft (`v5`, which attributed a repair only to the oldest open writ), and `BRIEF-C1b` v7 committed $6/11$ as a tighter constant while explicitly stating "that it is not this rule's own replay, which is 5/11."

2. **Line 277 — Title classification of the `80` non-stream proposals and `48` reads/reviews at `seq 7809`:**
   - *What is said:* "Most of these are the hourly streams: 5,919 forecasts and resolutions, and the 622 of the 702 proposals whose titles mark them as stream batches. Of the other 80, 48 are reads and reviews of briefs and code; the rest carry code and pins, fixes, and forecasts outside the streams [titles in the log at seq 7809]."
   - *What is missing:* In `e580b64:log.jsonl`, two small title-matching artefacts affect the `622 / 80 / 48` split: (a) five of the `80` "other" proposals (`seqs 237, 305, 313, 319, 331`, titled `M2 race card...` and `M2 races ... resolved...`) are HKJC race-stream proposals (one of the two scored value streams of §4.3) that lack the substrings `freshness` or `world.hkjc`; and (b) among the `80`, the count of `48` "reads and reviews of briefs and code" includes two proposals (`seq 654`, `C2b read gate under C2a's cap: jack push --opens, tests...`, and `seq 657`, `pins: the read gate, three KILLED with passing twins`) that matched the word `read` because they implement and pin the "read gate," leaving `46` actual read/review proposals.

3. **Line 237 — Scope of the Google revision `432e385` on `kernel2/` and source of C1a's `kernel/` family attribution:**
   - *What is said:* "Its author's family differed from the first kernel's at C0 (OpenAI against Anthropic) and at C1a (Google against Anthropic). It did not for C1's new entry types: OpenAI models wrote them into both kernels on the same day, before a Google model revised the second [commit trailers of `kernel/` and `kernel2/`, 2b6b835 and 8fcd821; `kernel2/NOTES.md` at each revision]."
   - *What is missing:* (a) Inspecting `git diff 8fcd821 432e385 -- kernel2/checker.go` shows that the Google revision `432e385` (`google/gemini-4-argon`) only added the `last_key_revocable` check for `key` declarations (which in `kernel/` was written by `claude-opus-5-5` at `8d1dda9`) and did not modify `8fcd821`'s (`openai/gpt-6-astra`) code for C1's four new entry types (`amend, push, decision, spec_conflict`). (b) At C1a, the commit trailers of `kernel/` (`eafb69ca`, `bcb19f70`) say only `Proposer: builder builder-1`; that `builder-1` was an Anthropic (Claude) session is recorded in `REPORT.md` (C1a §2, line 340), not in the commit trailer.

4. **Lines 315 and 319 — Fourth falsifier of `CHARTER §12` ("in any 14-day window") vs. per-window counts:**
   - *What is said:* Line 315 claims "None of its four falsifiers has been met on the record," while line 319 quotes `"at more than assize's 5 : 1 (20 : 4) in any 14-day window"`, gives the four per-window counts, and notes: "The evaluator counts per window, not per 14 days."
   - *What is missing:* Because line 319 notes that the evaluator does not check 14-day windows, the claim in line 315 that the fourth falsifier has not been met is left unverified for 14-day windows. Checking every full 14-day interval $[t, t + 14\text{ days}]$ on `e580b64:log.jsonl` shows that from C1a's opening (`seq 32`, `2026-10-25`, when `forecast` and `resolution` entries were introduced and from which `CHARTER A3.4` begins counting) onward, the maximum procedure-to-object ratio in any 14-day interval is $871 : 1{,}755 \approx 0.50 : 1 \le 5 : 1$ (whereas the 14-day interval starting at `seq 0` on `2026-10-14`, eleven days before object entries existed, is $63 : 5 = 12.6 : 1$). Stating this explicitly backs line 315 under both A3.4's window count and 14-day intervals after object entries existed.

---

## 7. Overclaiming and clarity

The manuscript is now exceptionally disciplined in matching its claims to its evidence. It states clearly in the abstract, introduction, §6, §8, and §9 that no self-modifying agent (C3) has yet been built, that the mathematical results apply classical tools to an institutional setting rather than proving new theorems, that the block recomputation is a retrospective audit rather than a prospectively registered promotion decision, and that nine of twenty-eight audited criteria in the reference implementation can be passed without skill.

**What could be cut without loss:**
- The non-value forecast paragraph at line 145 (§4.2) and the ancestor-walk details of C2a′ at line 297 (§6) could be trimmed by a few lines each without losing any part of the argument.

---

## 8. Recommendation

**Accept.** The paper has a clear and original central thesis, all six propositions and their proofs are mathematically sound, the Lean 4 formalisation matches its disclosed scope, every simulation and retrospective recomputation figure reproduces from the ancillary scripts, and all points raised by the ninth referee have been resolved. The remaining items below are minor factual clarifications against the repository at `e580b64`.

The five changes that matter most, in order:

1. **Clarify the provenance of $p_0 = 6/11$ in §5.2 (line 272):** Note that under the brief's adopted all-open-writs taint rule (`BRIEF-C1b-draft.md`, "Null"), the Laplace rate on the nine items through `seq 163` was $5/11$, and $6/11$ was the rate under an earlier single-writ attribution rule (`v5`), retained as a stricter pre-committed bound.
2. **Refine the proposal title counts in §5.2 (line 277):** Either count the five `M2` race-stream proposals (`seqs 237, 305, 313, 319, 331`) with the stream batches (`627` stream proposals and `75` others) or note that "stream batches" there refers to the `622` proposals titled as `freshness` or `world.hkjc`, and adjust `48` to `46` reads and reviews (since `seqs 654` and `657` are code and pins for the read gate).
3. **Clarify the C1/C1a kernel authorship details in §4.4 (line 237):** Note that the Google revision `432e385` added the last-key guard (`8d1dda9` in `kernel/`) rather than rewriting `8fcd821`'s C1 entry-type code, and add `REPORT, C1a §2` alongside the commit trailers for C1a's Anthropic authorship of `kernel/`.
4. **Back the 14-day window clause of the fourth falsifier in §6 (line 319):** Add that over every full 14-day interval since object entries entered at C1a's opening (`seq 32`), the procedure-to-object ratio is at most $0.50 : 1$ (`871 : 1,755`).
5. **Trim the non-value forecast aside in §4.2 (line 145):** Shorten or cut the paragraph on counsel's and the operator's non-stream forecasts.

RECOMMENDATION: accept
exit=0
```

