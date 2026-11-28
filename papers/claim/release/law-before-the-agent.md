---
title: "Law Before the Agent: Testing the Institution That Judges Self-Modifying AI"
date: 2026-11-28
draft: true
math: true
summary: "Systems that rewrite their own code are now practical."
---

*This is the web version of a preprint: arXiv:XXXX.XXXXX [cs.AI]. The Lean proofs and the two scripts it relies on are ancillary files there.*

- *Square brackets give the check behind each fact about the implementation:*
  - *`seq n` is an entry of `renavondata/jack` `log.jsonl`;*
  - *`CHARTER`, `SPEC` and `REPORT` are files at `origin/main` `e580b64`.*

---

## Abstract

Systems that rewrite their own code are now practical. Results of Rice, Löb and Goodhart limit what inspection, self-proof and measures within an agent's reach can establish about such systems, yet in the leading examples the evaluator that judges them is held fixed and trusted as infrastructure. We propose that the institution which judges a self-modifying agent be built before the agent, imposed first on the model sessions that build it, and allowed to grow only by anytime-valid tests on its own record. Its law is a fold over a signed, append-only log; claims of merit count only as forecasts under the logarithmic score; and each layer after the record is frozen, and the next begun, only when its sequential tests pass, of liveness, measured by the principal's repairs, and, once there are forecasts to aggregate, of predictive value. We state the guarantees in six propositions, whose statistical core is machine-checked in Lean, show by example and simulation that the natural per-event test of value loses its level when outcomes resolve together, and prove that a block form keeps it. Applied retrospectively to the public record of a reference implementation, the block-form test finds an advantage over a base rate pooled across datasets and no evidence of one over a base rate kept per dataset, so the institution's own book shows that its first evidence of value rested on a weak baseline. The paper offers a design and an audit, not an evaluation: the implementation has promoted one layer on a sequential test, no rule yet ties its keys to promotion, and no self-modifying agent has yet been built under the design.

---

## 1 Introduction

Systems that modify their own code are now practical, and so are their failure modes. The Darwin Gödel Machine raised its SWE-bench score from 20% to 50% by editing its own agent code [Zhang et al. 2025]. In one run it also removed the markers its hallucination detector read, despite instructions not to change them [Zhang et al. 2025, App. H]. Hyperagents make the modification procedure itself modifiable. They keep the evaluator, the task data and, except in one experiment, parent selection outside the editable boundary "to ensure safety, prevent evaluation gaming", and name the loosening of that boundary as future work [Zhang et al. 2026, App. A.5]. A census of 114 studies of recursive self-improvement found that evaluation usually certifies the product of a run and rarely the process that produced it: of the 90 studies that call themselves recursive self-improvement, only 22% audit two or more reruns of the full loop [Chen, Zhu & Zheng 2026].

The difficulty is old in economics and older in law. Delegation carries agency costs: monitoring, bonding and residual loss [Jensen & Meckling 1976]. A signal is worth conditioning the contract on when it is informative about the agent's action [Holmström 1979]. When the agent can rewrite the instrument the principal reads, how informative the signal is becomes the agent's choice. Kolt [2026a] argues that the classical remedies — incentives, monitoring, enforcement — strain under AI agents. He warns that legal alignment "will need to contend with the prospect of actors that shape the very laws that govern them" [Kolt 2026b]. This paper is about that case.

**The main idea.** We argue that a self-modifying agent can be trusted only as far as an institution it cannot reach can test it. That institution should be built first, tested first on its builders, and allowed to grow only by valid sequential tests on its own record. The institution keeps a book on itself rather than a proof of itself, and the book can show the institution wrong.

**Contributions.**
1. *A design* (§§3–5). The institution that judges a self-modifying agent is built before the agent and imposed first on the model sessions that build it. Its law is a fold over a signed, append-only log; claims of merit count only as forecasts under the logarithmic score; and each layer after the record is frozen, and the next begun, only when sequential tests pass, of liveness, measured by the principal's repairs, and of predictive value. §3 sets out the results behind each ingredient, as design arguments rather than proofs of necessity.
2. *Six propositions* (§4), none mathematically new, stating the construction's guarantees exactly. The value test is given in a block form, which keeps its level when outcomes resolve together, and whose regret bound holds for the quantity tested. We show by example and simulation that the per-event form does not keep its level. The statistical core is machine-checked in Lean 4 with Mathlib.
3. *Evidence from a public record* (§6). A reference implementation has run in public since October 2026, with a signed log that dates each step. Recomputed retrospectively under a stated protocol, its value evidence survives only against a base rate pooled across datasets. The institution's own book thus shows that its first evidence of value rested on a weak baseline. The record also shows how far promotion has governed so far: it has gated the order of the layers, once on a sequential test, but no rule yet ties the grant of keys to it (§5.1).

This is a design paper with proved guarantees and one empirical check. It contains no evaluation of a self-modifying agent: in the reference implementation the agent is the last layer, and it has not been built. Nor does it validate the institution. The record shows the design's ingredients running, and one of its tests exposing the institution's own weak evidence. It does not show that growing by these tests improves on simpler governance, nor that passing them predicts useful or safe autonomy.

To our knowledge, three things here are new. Each has precedents, which §7 credits.
- The governing institution itself grows layer by layer, each layer frozen and the next begun only after a sequential test on the institution's own record (§4.3). The implementation has done this once (§5.1).
- The principal's repairs are tested sequentially alongside value, as a condition of promotion, with wealth carried across failed windows (§4.3, §4.5).
- The law is built before the agent, and imposed first on the model sessions that build it (§5).

---

## 2 Setting

What is to be governed has four parts:
- **The agent** rewrites its own programs and keeps or discards the result by what it earns. It goes on doing so after it stops being watched.
- **The operator** is the principal and owner of the utility. He is one person, whose attention is the scarcest resource in the system.
- **The world** charges for being wrong. Its outcomes come from processes outside the agent: a race result, a dataset's modification time, a test run on a commit.
- **The policy** inside the agent is a large language model: general, cheap and unreliable in ways that cannot be listed in advance.

In this setting, three results bear on what governs the object:
- **Lock.** That a change is an improvement is a semantic property of programs, and no procedure decides such properties for arbitrary programs [Rice 1953]. Proofs remain possible for particular programs and restricted languages, but a self-modifying agent's changes are not confined to such a class. By Löb's theorem, an agent that adopts a successor only on a proof, in its own consistent theory, that the successor's conclusions are sound cannot in general obtain that proof for a successor reasoning in the same theory [Löb 1955; Yudkowsky & Herreshoff 2013]. This obstructs proof-based self-trust, not every form of trust. Neither result forbids checking the agent from outside, against a fixed specification. So we put the evaluation rule outside the modifier's reach.
- **Score.** Under expected-score incentives, a proper score can be held fixed at every level without rewarding misreport [Brier 1950; Good 1952; Savage 1971; Gneiting & Raftery 2007], provided the scored parties do not control the outcomes [Goodhart 1975]. Only forecasts actually issued, and outcomes actually realised, count [Dawid 1984]. A proper score is not immune to Goodhart's law: a weak comparator, an omitted objective or strategic participation can still be exploited (§8).
- **Anytime validity.** The operator reads the record when he likes and acts when it suits him. A test whose level survives such looking is naturally built from a test supermartingale, by Ville's inequality [Ville 1939; Shafer & Vovk 2019; Ramdas et al. 2023].

A fourth, which we call *loop*, is that the simplest optimal regulator is a model of what it regulates [Conant & Ashby 1970]. Here it motivates holding the institution's state as a fold over its record, and no more; the fold's practical merits are that the state can be rebuilt and audited by anyone holding the log. These results motivate the construction's ingredients; they do not fix how each is built (§3).

**Threat model.** We trust the operator's genesis key and his reading of what he signs, the host and CI provider that run the judge, and SHA-256 and Ed25519. We trust no proposer, including the model sessions that build the institution and, later, the agent. We trust no claim that the record cannot recompute, with three exceptions. Promotion evidence is checked for presence and hash, not truth, and the operator attests its contents [SPEC §10, item 15]. A resolution's outcome is taken as entered: the kernel checks that it names an outcome and some evidence [SPEC §5], not that the evidence implies it, and one resolution on the record is known to be wrong and stands [REPORT, C1a §4]. Times are those the entries carry, checked only for format and order. The guarantees below therefore concern the recorded outcomes and times. The construction aims to make every untrusted party's influence pass through entries that the checker admits and the ledger scores. It does not defend against a compromised host, or against an operator acting against his own utility.

**Terms.** *Value* means predictive advantage over a stated base rate, not the principal's utility. An act is *priced* when it enters a statistic that can fail a window (§4.5). The *kernel* is the validity predicate (§4.1). The *judge* is the CI that runs both kernels, the tests and the *evaluator*, which computes the promotion criteria from the log and the tree. The *clerk* derives obligations from the state and the clock (§4.3). Only the kernel is small and duplicated; the trusted base around it is much larger (§4.4).

---

## 3 Why these ingredients

Table 1 maps each ingredient of the design to the results behind it. Each row is a design argument, not a theorem about all designs, and other responses are possible. Among the results, Rice, Löb, Ville, Alpern–Schneider, the propriety of the log score and the option-value results of Arrow–Fisher and Henry are theorems within their own models. Conant–Ashby holds under stated conditions. The rest are principles from statistics, law, security and engineering, with records of failure behind them. We claim neither that the ingredients suffice, which the falsifiers of §6 put to the record, nor that they are optimal: log loss is a scoring rule, not the operator's utility.

**Table 1. The ingredients, the results behind them, and this design's response.**

| Ingredient | Result | Motivates | Response |
|---|---|---|---|
| **Outside reach** | Rice 1953 | No general inspection decides the merit of arbitrary changes, so judge merit by outcomes | A claim of merit counts only as a forecast resolved by an outcome |
| | Löb 1955; Yudkowsky & Herreshoff 2013 | The evaluation rule is held outside the agent's theory, not re-derived by it | Judge and score behind keys the agent does not hold |
| | Anderson 1972; Saltzer & Schroeder 1975 | The monitor is always invoked, tamper-proof and small | Judge runs from trunk [CHARTER §3]; 450-line kernel, inside a larger trusted base (§4.4); invalid entries refused, with a reason [SPEC §§8–9] |
| **A fold** | Conant & Ashby 1970 | The governor holds a model of what it governs | State is a fold over the record |
| | Hart 1961 | Recognition, change, adjudication | The core holds exactly these three, in code; rules of conduct are to enter only from cases, and none has yet (§8) |
| | Fuller 1964 | Law must be prospective, promulgated, clear | Prospectivity by the fold (Proposition 1); rules and the checker's digest are entries |
| **Forecasts** | Dawid 1984 | Only issued forecasts and realised outcomes count | Probability fixed at entry; one resolution; no revision |
| | Savage 1971; Gneiting & Raftery 2007 | A score held fixed should reward belief | Log score on a per-mille grid (Proposition 2) |
| | Goodhart 1975 | A target decays when its outcomes are the scored party's to move | Outcomes from processes no scored party operates, which the freshness stream does not meet (§8); named attacks listed before each window |
| **Tests** | Ville 1939; Shafer & Vovk 2019; Ramdas et al. 2023 | The operator looks when he likes | Promotion by test supermartingales; a window is a maximum (Propositions 3–5) |
| | Gall 1977; Hayek 1973 | Working complexity grows from working simplicity | Layers C0 → C3; from C1a on, each promoted on criteria stated in advance, with recorded departures (§4.3, §6) |
| **Liveness** | Alpern & Schneider 1985 | An "eventually" is never refuted by a finite record | Every obligation has a deadline, which makes it a safety property, checked exactly; the rate of meeting deadlines is tested statistically |
| | Arrow & Fisher 1974; Henry 1974 | Irreversible acts merit a hard gate | The operator reserves keys, pushes, amendments, promotion and veto; all else is priced (§4.5) |

Two points about the record complete the table. Relative to an authenticated head (Proposition 1), signatures and hash chains prove that recorded entries were not altered, not that nothing was omitted [Zhao et al. 2026, Cor. 3]. For *law*, completeness holds by definition: an act that is not an entry has no legal effect. For *acts in the world* it does not, so the operator's acts are compared against an independent record (§4.5), and that comparison has already failed a window (§6). And the institution keeps a book on itself rather than a proof of itself. Its checker can be verified from outside against the specification, but whether the institution serves its owner is an empirical question, and it is put to the record.

---

## 4 The construction and its guarantees

Propositions 1, 2 and 6 are elementary. Their value lies in stating exactly what is guaranteed and what is not, in a form that can be checked against the code. Propositions 3–5 carry the statistical content. None is mathematically new: the block mixture is the Bayes mixture of online learning, and Proposition 5 is the intersection–union principle. What we claim is their application to an institution, and the exact statement of what each does and does not guarantee.

**Machine-checked core.** Propositions 1(b), 2(a), 3(b), 4(b) and 5 are checked in Lean 4 [de Moura & Ullrich 2021] against Mathlib [The mathlib Community 2020]. So are 3(a) and 4(a), for every finite horizon. There the wealth is shown to be a non-negative supermartingale under the null, and Ville's inequality is derived from Mathlib's optional stopping theorem. The proofs use only Lean's standard axioms, and they are ancillary files of this paper. The bridges from the paper's definitions to the Lean statements are informal: the product construction, the clipping and the stake rules. Three statements are narrower than the propositions they serve. For 2(a), Lean proves that the expected score has its unique maximum at the belief, not strict concavity. For 4(b), it proves the union bound on measures, and the independent case only as an inequality between real numbers, without modelling independent events. For 5, it takes the component bounds as hypotheses. Not formalised are:
- the grid clause of 2(a);
- the bounds that the stake rules keep;
- the unbounded horizon, which follows by continuity of measure;
- Propositions 1(a) and 2(b), which hold by construction of the code, and 6, which restates the specification's admission condition and is enforced only in part (§4.4).

### 4.1 The record, and law as a fold

A *log* is a sequence of entries $e_0, e_1, \dots$. Each entry is a canonical JSON line with seven fields: `seq`, `parent` (the SHA-256 of the previous line, or zeros for the genesis entry), `ts`, `type`, `proposer`, `body` and `sig` (an OpenSSH signature, by an Ed25519 key, over the entry without `sig`) [SPEC §§1–6].

The state $S_i$ is a function of $e_0, \dots, e_{i-1}$ alone. The kernel reads from it what it needs to admit or refuse $e_i$ [SPEC §7; `kernel/check.py`]:
- the hash of the last line and the last timestamp;
- the declared keys, each with a principal and a set of powers (entry types), and every public key ever declared, each bound to its first identifier for the life of the log;
- the identifiers of amendments already entered;
- the forecasts recorded and resolved.

The state also records the charter digests entered, the trusted-base digest and the amendments a `transmute` decision has made mutable. The kernel does not use these to admit or refuse. The judge checks trunk's charter against the latest digest entered, and refuses an amendment that has not been transmuted [SPEC §7; §10, items 2 and 13].

The validity predicate $V(S_i, e_i)$ accepts the entry, or refuses it for one of fourteen reasons [SPEC §§8–9]. A log is valid if $V$ accepts each entry in turn; the first refusal is the verdict.

This differs from the event-sourced runtime of Regimes [Nakajima 2026], which projects the agent's state from its log. Here the *admissibility of the next entry* is itself a function of the law folded from the entries before it. The law therefore changes only by entries, and binds only forward.

**Proposition 1 (prospectivity).** Let $L$ be a valid log whose last line hashes to $h$. Call a log *linked* if each entry's `parent` is the SHA-256 of the line before it; the kernel refuses any log that is not.

(a) For any extension $L' = L \Vert M$, every entry of $L$ receives the same verdict in $L'$ as in $L$.

(b) Any linked log $L^* \neq L$ whose entries are numbered by position from 0, as the kernel requires, and whose last line also hashes to $h$, yields a SHA-256 collision. So a computationally bounded adversary can produce such a log with probability no greater than its probability of finding a SHA-256 collision.

*Proof.*
- (a) $V(S_i, e_i)$ depends only on $e_0, \dots, e_i$.
- (b) If $L$ and $L^*$ differ in length, their last lines carry different `seq`, since entries are numbered by position, and both hash to $h$: that is a collision. Otherwise compare them from the last line backwards. If two lines with equal hashes differ, they are a collision. If they are equal, their `parent` fields are equal, so the lines before them hash alike, and the comparison continues. Since $L^* \neq L$, a difference is found before both logs are exhausted. $\square$

Proposition 1 gives one computational ingredient of Fuller's prospectivity: under a fixed predicate, later entries cannot change the verdict on earlier ones. The kernel does not interpret the charter's substantive law, and changes to the checker's own code lie outside the proposition (§4.4). An amendment entered at seq $a$ names an activation height $k > a$, which the kernel checks [SPEC §7]. It takes effect at $k$, but two things change at $a$ itself: trunk's charter must match the amendment's text from then on, and no push is lawful until $k$ [SPEC §10, items 2 and 12]. The kernel never reads a clock: order comes from the chain [Lamport 1978; Schneider 1990], and `ts` is a field that may not decrease.

Authority is a capability [Dennis & Van Horn 1966; Miller 2006]. A party without a key holding the power `merge` cannot enter a merge, and there is nothing to argue with. In the implementation, builders' keys hold `proposal` and `spec_conflict` [seq 6], and later ones `forecast` and `resolution` as well [seq 34]. The merging process now holds `merge` alone [seq 201]. Only the operator's key holds `key`, and from seq 1 also `push`, `amend` and `decision` [seqs 0, 1]. A `key` entry that would leave no key able to declare keys is refused, because that loss is irreversible [CHARTER A2.5].

### 4.2 Claims as wagers

Questions of validity are settled by $V$. Questions of merit are forecasts, and the world settles them [CHARTER §3]. In the design a claim of merit has standing only as a forecast: a proposal asserts nothing about its merit, and the ledger scores forecasts, not proposals. The implementation does not yet require a proposed change to carry a forecast of its own merit. A `forecast` carries a claim, a probability $p \in \{1, \dots, 999\}/1000$ and a date by which it resolves. A `resolution` names the forecast, an outcome $y \in \{0,1\}$ and its evidence.

**Proposition 2 (propriety; no self-judgement).**

(a) For belief $\pi \in (0,1)$, the expected log score $g(p) = \pi\ln p + (1-\pi)\ln(1-p)$ is strictly concave with its unique maximum at $p = \pi$. On the per-mille grid a maximum lies at a grid point adjacent to $\pi$, or at the nearer end of the grid if $\pi$ lies outside $[0.001, 0.999]$; two grid points can tie.

(b) Every resolution proposed by the principal who proposed its forecast is refused. The test is by principal, not by key, so one party's two keys cannot launder a judgement [SPEC §7].

*Proof.* (a) $g'' < 0$ and $g'(\pi) = 0$, and a concave function restricted to a grid is maximised next to its continuous maximiser. (b) This is the kernel's rule `self_judged` [SPEC §8, step 8a]. $\square$

Part (b) is *nemo iudex in causa sua* [Coke 1610], enforced by the kernel. It does not stop a party from acting on the world to move an outcome, which is the performative case [Perdomo et al. 2020]. Hence the requirement in Table 1 that scored outcomes come from processes no scored party operates. Nor does it stop two principals from colluding, or one actor from holding two principals; the operator's declarations of keys must prevent that.

Part (a) concerns the expected score. A party rewarded by a non-linear function of its score, such as its weight in the mixture or a promotion, may gain by another report. We do not claim truthful reporting is optimal for those rewards.

The logarithmic score is chosen among proper scores for a second reason. Under it, the Bayes mixture of forecasters is itself a forecaster, and its regret against the best of $K$ is at most $\ln K$ with nothing to tune [Cesa-Bianchi & Lugosi 2006, §9]; Proposition 3(b) restates this for blocks.

A forecast belongs to a procedure, not to a mind: a template, model and prompt have a log-loss on a stream whether or not they believe anything. The stream of §6 is such a procedure: one named model (§6), with a prompt revised five times after it was put on the record on 2 November [`git log -- transcripts/sessions/stream-forecast.md`]. Anyone holding the power may forecast, counsel and the operator included, and is scored the same way [seqs 31, 33; `tools/entry.py`, `score`].

### 4.3 Promotion by betting

A *layer* is a set of mechanisms, together with the powers they confer. It is built under a *window*: a set of criteria committed before the window opens [CHARTER §6, A5]. A layer can be tested on its own record only if it runs during its window, so its parties must hold its powers before the test, not after it. What passing grants is promotion: the layer is frozen, and the next begins [CHARTER §6]. A layer that fails is not patched in place; the fix is a change entry, the window starts again, and the next layer's window waits [CHARTER §§6, 8]. The implementation has departed from this in three ways. Its counted-line cap was raised three times against what had been stated, each time recorded as a finding against the pre-statement, the third time after C1b's window had opened [seq 197; SPEC §10]. The rule attributing off-record acts by declaration was adopted during C1b's window, before its exit evaluation [`transcripts/BRIEF-C1b-draft.md`, Amendment 2]. And A5, which lets a window end early at a `promote`, entered during C1a's window [seq 137], which then closed early under it [REPORT, C1a report]. A window is a maximum, not a term. It ends at its stated end, or at a `promote` entry, or — as failed — at a veto [CHARTER A5.1, A6.1]. A `promote` is the operator's act. Since the push at seq 7281, the judge refuses any `promote` that the evaluator in force does not find lawful [SPEC §10, item 15].

The hypotheses concern the *institution*, not a candidate. The statistics are computed over the live record, whoever made it. Value is computed over the forecasts of the two streams the brief names, dataset freshness and race results [`judge/value.py`]. Liveness is computed over the timely resolution of every forecast, with every entry under the operator's key a candidate repair. Both carry wealth from the layer's first window. Promotion lets the next layer begin; it does not adopt one edit over an incumbent. The record (C0) needs safety alone. Until there are forecasts to aggregate, a layer's value is its liveness rate; from the election (C2) on, it is predictive value against the base rate [CHARTER §6].

**Value.** Let events be grouped into finite, non-empty *blocks* $B_1, B_2, \dots$, each block's membership fixed before any of its outcomes is realised, under assumption (A): when the forecasts of $B_m$ close, every outcome of the blocks before $B_m$ is realised and none of $B_m$'s own is. A sitting at which several events are forecast together is one block. Let $\mathcal G_{m-1}$ be the information recorded before $B_m$'s forecasts close. By (A) it contains, for every earlier block, its outcomes, which of its events resolved, its scores and its stakes, and none of $B_m$'s outcomes; the $\mathcal G_m$ increase with $m$.

Where horizons overlap, so that (A) fails for consecutive sittings, the sittings are split into lag classes within which it holds, and each class is a process of its own [Henzi & Ziegel 2022]. If the classes are formed from the data, class $\ell$, numbered in order of creation, needs a threshold fixed in advance, such as $\ell(\ell+1)/\alpha$; since $\sum_\ell \alpha/(\ell(\ell+1)) = \alpha$, the chance that some class crosses its threshold is at most $\alpha$.

If some events of a block do not resolve, write $R_m \subseteq B_m$ for those that do. Then $R_m$ replaces $B_m$ throughout: in $Q_m$, in $\bar D_m$, in the posterior updates and in the size multiplier of part (b). A block with $R_m = \varnothing$ contributes the factor 1, and the null is stated for that statistic: no advantage on the events that resolve, given $\mathcal G_{m-1}$. Independence of resolution from outcomes would not carry a null on the full block over to the resolved subset.

For event $i$ in block $B_m$, with outcome $Y_i$:
- $b_i$ is the base-rate forecaster's probability: the past frequency for the event's type;
- $p_{k,i}$ is the probability of member $k$ of a roster of $K$ forecasting parties *that includes the base-rate forecaster*;
- a party that abstains is scored as the base rate;
- all are $\mathcal G_{m-1}$-measurable and clipped to $[10^{-3}, 1-10^{-3}]$.

Write $p(1) = p$ and $p(0) = 1-p$. The aggregate's forecast for a block is the Bayes mixture, with uniform prior, of the members' product forecasts:
$$Q_m(y) = \sum_k w_{k,m}\prod_{i\in B_m} p_{k,i}(y_i), \qquad w_{k,m} \propto \prod_{j<m}\,\prod_{i\in B_j} p_{k,i}(Y_i).$$
Its marginal for event $i$ is the usual mixture $q_i = \sum_k w_{k,m}\, p_{k,i}$. Let
$$\bar D_m = \frac{\ln Q_m(Y_{B_m}) - \sum_{i \in B_m}\ln b_i(Y_i)}{|B_m|\,\ln 999} \in [-1,1].$$
For a block of one event, $\bar D_m = \ln(q_i(Y_i)/b_i(Y_i))/\ln 999$, the charter's per-event difference [CHARTER A4.4]. Let
$$\lambda_m = \min\Big(\max\big(0, \tfrac{\sum_{j<m}\bar D_j}{2 + \sum_{j<m}\bar D_j^2}\big),\, 1 - \tfrac{1}{m+1}\Big),$$
the plug-in ratio of the first to the second moment with two pseudo-observations at $\pm 1$ [CHARTER A4.4]. Set $W_t = \prod_{m \le t}(1 + \lambda_m \bar D_m)$.

**Proposition 3 (value).** Let $H_0^{\mathrm{val}}$ be: $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 0$ for every $m$. This holds whenever, for each block, the aggregate's joint forecast does not beat the base rate's in expected log score on the events that resolve, given what was known when the forecasts closed and given which events resolve. Without the second condition it can fail, because $\bar D_m$ divides by the random size $|R_m|$. Nothing is assumed about dependence within a block.

(a) Under $H_0^{\mathrm{val}}$, $W$ is a non-negative supermartingale with $W_0 = 1$, so $\Pr(\sup_t W_t \ge 1/\alpha) \le \alpha$.

(b) For every sequence of outcomes and every $t$,
$$\ln 999\sum_{m\le t}|B_m|\,\bar D_m \;\ge\; \max_k \sum_{m \le t}\sum_{i\in B_m}\ln\frac{p_{k,i}(Y_i)}{b_i(Y_i)} - \ln K \;\ge\; -\ln K.$$

*Proof.*
- (a) $\lambda_m \in [0,1)$ and $|\bar D_m| \le 1$ give $1 + \lambda_m \bar D_m > 0$. Predictability gives $\mathbb E[1 + \lambda_m \bar D_m \mid \mathcal G_{m-1}] = 1 + \lambda_m \mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 1$. Then apply Ville's inequality [Ville 1939].
- (b) Because the weights are Bayes posteriors, the product telescopes: $\prod_{m\le t} Q_m(Y_{B_m}) = K^{-1}\sum_k \prod_{m\le t}\prod_{i\in B_m} p_{k,i}(Y_i) \ge K^{-1}\max_k \prod_{m\le t}\prod_{i\in B_m} p_{k,i}(Y_i)$ [Cesa-Bianchi & Lugosi 2006, §9]. Take logarithms and subtract $\sum \ln b_i(Y_i)$. The second inequality holds because the base-rate forecaster is a member. $\square$

In the terms of the sequential comparison of forecasters, this is the strong, pointwise null: no conditional advantage at any block [Choe & Ramdas 2024a]. Rejecting it says less than rejecting their weak null, of no advantage on average. By part (b), the aggregate's cumulative log loss is never more than $\ln K$ above the base rate's, whatever the outcomes. Part (b) bounds the size-weighted sum $\sum_m |B_m|\bar D_m$, that is, the aggregate's log loss; the wealth bets on the unweighted block averages, so (b) is not a bound on the wealth. Rejecting $H_0^{\mathrm{val}}$ at level $\alpha$ is evidence that, at some block, the aggregate had a conditional advantage over the base rate. It is not evidence of a persistent advantage, nor of skill beyond what a finer base rate would capture (§8).

*Remark (one bet per sitting).* Assumption (A) and block betting make the null mean "no advantage given what is known at the cutoff". Betting per event breaks this by a mismatch of filtrations. The null is stated given what is known at the cutoff, but a per-event bet in resolution order conditions later bets on outcomes that this information excludes; the process then need not be a supermartingale under the null. Simultaneous resolution is how the mismatch arises here, not the defect itself, and evidence valid in one filtration need not be valid in another [Choe & Ramdas 2024b]. Freezing the stakes within a sitting does not cure this, since a product of correlated factors need not be a supermartingale either; hence one factor per block.

If outcomes within a sitting were independent given $\mathcal G_{m-1}$, and the null held for each event, one bet per event with forecasts and stakes fixed at the cutoff would also be valid, and would compound faster. The block form gives up that power so as not to need the assumption. It has a cost of its own. A mixture of product forecasts can represent dependence among a sitting's outcomes that the base rate's product cannot, and the joint score credits that as advantage. That is not the same as forecasting the events better one by one. Nor can the joint forecast be replaced by the product of the marginals $q_i$: when members disagree within a block, that product can lose more than $\ln K$ to the best member, and part (b) would fail.

*Example.* Let each sitting hold $n$ events that share one fair outcome, let the base rate be $1/2$, and take $\alpha = 0.05$. Let the aggregate forecast $0.95$ or $0.05$ for the whole sitting, by a fair coin independent of the outcome. This is a single randomised forecaster, not the mixture of Proposition 3; it isolates the betting. Its forecast is a product, so $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \approx -0.12$ for the joint score and for each event alike. The block process never reached $1/\alpha$ in 4,000 runs of 300 sittings (95% upper bound 0.075%, by the rule of three). Betting per event in resolution order, the stakes on later events are raised by earlier events with the same outcome. That process reached $1/\alpha$ in 13.3% of runs at $n = 20$ (95% interval 12.2–14.3%), and in 50.4% of 2,000 runs of 200 sittings at $n = 50$ (48.2–52.5%). With independent outcomes it never crossed. This is a simulation, not a proof; for the block form the proof is Proposition 3(a). The script is an ancillary file.

The reference implementation updates both its stake and its mixture weights after every event in resolution order [`judge/value.py`, lines 113–135]. Its base rate also counts every earlier resolution of the type, including those of the same batch [`judge/entries.py`, `resolution_rates`]. And its streams do resolve in batches: fourteen resolutions in one minute of 2 November, for instance [seqs 550–563]. Its reported value wealth therefore has no guaranteed level. §6 recomputes it in block form.

**Liveness.** The clerk derives obligations ("writs") from the state and the clock, each with a deadline. A writ escalates when its deadline passes: a level-triggered reconciliation loop, not an event handler [Burns et al. 2016; CHARTER §2, maxim 3]. An *item* is either an act that discharges a batch of writs, with $Y_j = 1$ if the batch landed on time untainted by a repair from the operator and $0$ otherwise, or a single writ that expired, with $Y_j = 0$ [`judge/status.py`, `item_process`]. A null rate $p_0 \in (0,1)$ is committed before the window opens, taken from the incumbent's series and never from the window it judges [CHARTER A4.2].

Let $\hat q_j = (s_j+1)/(n_j+2)$, where $s_j$ counts successes among the $n_j$ items resolved before item $j$, since the layer's first window. Items are indexed in the order in which their outcomes are realised, and $\mathcal F_{j-1}$ is the record before $Y_j$ is realised. If several items are realised together, they count as one: the process takes the single factor $1 + \lambda_j(\bar Y_j - p_0)$ on their mean outcome, with the stake computed from items realised earlier, and the null and proof below apply with $\bar Y_j$ for $Y_j$. Such a rule must first put expiries on the same unit as batches, since averaging a dozen expired writs into one factor would count them as one failure. That unit is an open operational definition, and until it is fixed the batching rule is not a deployable protocol. The reference implementation does not batch at all. It scores simultaneous items one by one [`judge/status.py`, `score_items`], and 190 of its 641 items so far share a timestamp with another: 188 expiries and 2 batches [log at seq 7809]. Let $\lambda_j = \max\big(0, (\hat q_j - p_0)/(p_0(1-p_0))\big)$, and $M_t = \prod_{j \le t}(1 + \lambda_j(Y_j - p_0))$ [CHARTER A4.3].

**Proposition 4 (liveness, with wealth carried across windows).** Let $H_0^{\mathrm{live}}$ be: $\mathbb E[Y_j \mid \mathcal F_{j-1}] \le p_0$ for every item from the layer's first window on.

(a) Under $H_0^{\mathrm{live}}$, $M$ is a non-negative supermartingale with $M_0 = 1$. So the probability that $M$ ever reaches $1/\alpha$, in any window or across all of them, is at most $\alpha$.

(b) If each of $k$ windows instead restarted at 1, each a test at level $\alpha$, the probability of a false crossing in some window is bounded only by $1 - (1-\alpha)^k$ for independent windows, or by $k\alpha$ in general. The first bound is attained when each window's test is exact.

*Proof.*
- (a) $\hat q_j < 1$ gives $\lambda_j < 1/p_0$, so $1 - \lambda_j p_0 > 0$. Since $\lambda_j \ge 0$, $\mathbb E[1 + \lambda_j(Y_j - p_0) \mid \mathcal F_{j-1}] \le 1$. A failed window is followed by one that continues the same product [CHARTER A4.1], so every window's end is a stopping time of one supermartingale, and Ville's inequality applies once.
- (b) If window $j$ crosses falsely with probability $r_j \le \alpha$, independence gives $1 - \prod_j (1 - r_j) \le 1 - (1-\alpha)^k$, and the union bound gives $k\alpha$. $\square$

A retry therefore costs no α, provided the process, the null and the protocol continue unchanged. In the reference implementation, the value layer has failed two windows and its third is stated in advance. Had each window restarted at 1, the chance of some false crossing at $\alpha = 0.05$ could have reached $1 - 0.95^3 \approx 14\%$ for independent windows, and 15% in general. For a valid process carried unchanged, it stays at 5%; the implementation's per-event value process is not one (Example, above). Per-edit gates ask a different question, whether each edit beats its incumbent, and spend an error budget on each decision (§7), and, under power-law risk schedules and overlap conditions, gates admit only a finite total true-positive rate [Scrivens 2026, Thm. 1].

What Proposition 4 controls is the probability of *ever* promoting while the institution never beats $p_0$. It does not test the current window alone. Earlier wealth can carry a later window. While $\hat q_j > p_0$, each new failure multiplies the wealth by $(1-\hat q_j)/(1-p_0) < 1$, which is small when $\hat q_j$ is high. When $\hat q_j \le p_0$ the stake is zero and the wealth does not move (§8).

**Proposition 5 (conjunctive promotion).** Suppose promotion requires $W_t \ge 1/\alpha$ and $M_t \ge 1/\alpha$ at the same prefix, together with conditions that are checked exactly (pins killed, checkers agreeing, no veto). Then under any joint law in which $H_0^{\mathrm{val}}$ *or* $H_0^{\mathrm{live}}$ holds, the probability that promotion ever occurs is at most $\alpha$.

*Proof.* The promotion event lies inside $\{\sup W \ge 1/\alpha\}$ and inside $\{\sup M \ge 1/\alpha\}$. Bound it by whichever of these the true null controls. This is the intersection–union principle [Berger 1982]. $\square$

No combination of the two processes, by averaging or otherwise, is needed for validity against the union of the nulls. That union is the null that matters for promotion, since a layer should be refused if *either* null holds. The guarantee inherits the hypotheses of both component processes, and holds per layer. Over a sequence of layers, each tested at its own level $\alpha$, it gives no familywise bound.

### 4.4 Who may change the judge

The trusted base consists of the two kernels, the judge, the CI workflows and the specification. It changes only by the operator's `push` entry naming its digest. Every proposal whose trusted-base digest differs from trunk's is refused, and no push is lawful between an amendment and its activation height [SPEC §10, items 1, 11, 12]. The promotion evaluator is part of the trusted base. Every `promote` after the installing push (seq 7281) is judged by the evaluator in force at its `seq` [SPEC §10, item 15]. The two earlier promotions (seqs 188 and 337) are not judged in this way, although the evaluator's report re-assesses them.

How may the evaluator itself change? Let $E$ be the evaluator in force, and let $R$ be the commits of trunk's first-parent history up to a commit $T$, each with its log and the other inputs the table records for it. Before a replacement $E'$ is built:
1. The operator enters a grant naming a table of $E$'s outputs on $R$.
2. The grant marks, for each row $r \in R$, the lines $\mu(r)$ expected to change, together with what those lines will then say.

The specification admits the push installing $E'$ only if, on every row, $E'$'s output equals $E$'s outside $\mu(r)$ and agrees with the grant on $\mu(r)$. It also requires the same agreement, under the same marks, at every first-parent commit after $T$ up to the installing push's parent, against $E$ run there [SPEC §10, "The promotion evaluator"]. Write $R^+$ for $R$ together with those commits. In the implementation this is enforced only in part. The judge checks that the installing push carries a specification named in such a grant [`judge/judge.py`, `installing_push`]. CI replays three of the table's 706 rows, 300, 400 and 593, through the `replay_drift` pin [`pins/replay.py`, run by `pins/run.py` in `.github/workflows/tests.yml`]. The full replay is a reviewer's session, not a gate [`transcripts/sessions/c2a-3-replay.md`; grant seq 6851; push seq 7281].

**Proposition 6 (replay-bound change).**

(a) If $E'$ meets the admission condition then, on every commit of $R^+$ read with the inputs the specification states, every unmarked criterion line and every unmarked promotion verdict is the same under $E'$ as under $E$.

(b) Each `promote` after the installing push is assessed with one historical evaluator: the one in force at its `seq`. A later evaluator does not change that verdict, although the current judge drives the assessment and may re-run it.

(c) Nothing is certified about $E'$ on any other input: after the installing push's parent, or on a recorded prefix read with different evidence, such as another table of the operator's acts.

*Proof.*
- (a) By the admission condition.
- (b) This is item 15's dispatch [SPEC §10, item 15]; it needs no replay.
- (c) Agreement on finitely many inputs fixes nothing elsewhere. $\square$

Part (c) is the lock's residue: the future behaviour of $E'$ is governed like all code here, by review, by mutant pins, and by the next replay. What the rule removes is the silent re-judging of the past, by which a new judge might find that a failed window had passed after all. Marked outputs may still change, but only as the grant says and before the new evaluator is built, so Proposition 6 is not a conservative extension in the logician's sense. The Red Queen Gödel Machine takes the other path, by intent. It gates each evaluator replacement on an evaluator-independent anchor, then discards the utility records that depended on the replaced evaluator [Iacob et al. 2026, §3.2]. That suits an optimiser. For a court, past verdicts are history.

The kernel exists twice, in Python and in Go. The second was written without reading the first, from the specification and its test vectors. Its author's family differed from the first kernel's at C0 (OpenAI against Anthropic) and at C1a (Google against Anthropic) [REPORT, C1a report, for the first kernel's C1a author]. It did not for C1's new entry types, which OpenAI models wrote into both kernels on the same day; the Google revision that followed added only the last-key guard, so that code stands [commit trailers of `kernel/` and `kernel2/`, 2b6b835 and 8fcd821; `kernel2/NOTES.md` at each revision; `git diff 8fcd821 432e385`]. No ruling, waiver or finding in the record addresses this; this paper's audit is the first to record it [`git grep` over `transcripts/`, RUNBOOK, CHARTER, SPEC and `kernel2/`]. The judge refuses any proposal on whose log the two disagree, and CI runs 300 simulated logs through both [SPEC §10, item 5; `.github/workflows/tests.yml`]. This guarantees only that no entry is admitted on which the two disagree. Independently written programs fail together far more often than independence predicts [Knight & Leveson 1986], and so do language models [Kim et al. 2025].

### 4.5 The principal, priced

When the operator forecasts, he is scored like anyone else (§4.2). His *acts* are the one thing not scored: his wishes are preferences, not predictions, and the institution's utility is his by definition [Hadfield-Menell et al. 2016]. His acts are instead confined and priced:
- **Confined.** His decisions are listed by the charter: wishes, the budget, and the irreversible acts — keys, pushes, amendments, promotion and veto — where waiting has option value [CHARTER §7; Arrow & Fisher 1974; Henry 1974].
- **Priced by entry.** Every other act of his is an entry, typed as a *decision* or a *repair* by its entry type and key, under a rule the charter fixed before any window, so repairs cannot be made to fall by revising it [CHARTER §7]; §6 records how they fell by re-attribution instead. The line of code that types an entry as a repair entered on 31 October, during C1b's window, and has not changed since [879caf9]. Entries of type genesis, key, amend, push and proposal, and decisions other than `fix`, are not repairs. Every other entry under his key is, with one coded exception, added on 11 November, for a `fix` that names a failed window [4c1f9c97; `judge/status.py`, `item_process`, `window_fixes`].
- **Priced by liveness.** A repair taints every writ open at its entry, and a tainted item has $Y = 0$. His own resolutions and merges count as failures, and his other entries drop pending resolutions from the count [`judge/status.py`, `item_process`].

Acts the operator takes *off* the record are collected from the hosting platform's own event history, which is an independent record. A window fails if a repair is found there after attribution by declaration (§6) [`transcripts/BRIEF-C2a-draft.md`, criterion 7].

Human oversight load has been measured before, for instance as interventions per session [McCain et al. 2026] or as the share of consequential actions taken without approval [Kolluri et al. 2026]. In interactive imitation learning, an expert's interventions drive the learner's training [Ross, Gordon & Bagnell 2011], and a learned safety policy decides when to hand control back to the expert [Zhang & Cho 2017]. To our knowledge, this is the first such measure that is tested sequentially and made a condition of promotion. It measures timely, repair-free completion, not the worth of the work (§8).

---

## 5 Law before the agent

### 5.1 The order follows from the dependencies

In this design, each layer presupposes the one before it:
- A score needs a record, and a record needs the three secondary rules, so the record (C0) comes first.
- An overdue forecast is the first obligation this record holds, so the ledger (C1a) precedes the clerk (C1b) [CHARTER A3.1].
- An election of proposers needs scores, and scores need resolutions that land on time, so the election (C2) comes next.
- The agent (C3) comes last, because everything it may not touch must already exist.

This is Gall's rule [Gall 1977] and Madison's order: "you must first enable the government to control the governed; and in the next place oblige it to control itself" [Madison 1788]. Each layer is promoted before the next layer's window opens [CHARTER §8]. This is an argument from the design's own dependencies, not a universal necessity. Governance could be developed alongside an agent held in containment; §5.2 argues against that course, but we do not claim it impossible.

What the layers raise is authority, not intelligence, and what promotion gates is their order: no later layer's window opens on a layer that has not passed. Keys are another matter. They are the operator's grants, among the irreversible acts he reserves (§4.5), and the charter does not tie them to promotion [CHARTER §7]. In the implementation every key is the operator's grant: 19 `key` entries by seq 7809, 14 of them before the first promotion at seq 188 [log]. Powers have come as windows opened, which is when a layer under test needs them: the forecast and resolution powers at seqs 31–34, as C1a's window began [RUNBOOK, `jack key`]. No key has followed from a promotion; the herald's second key (seq 201) moved the merge key off counsel's session [same]. Promotion has gated the order. C1b's window opened at C1a's promotion (seq 188), and C2a's after C1b's (seq 337); with C2a unpromoted after two failed windows, C2b has not begun (Table 2). Two layers have been promoted: C0 on safety criteria, without a pre-stated window and patched in place throughout [REPORT §8.2], and C1 at the exit of its second window, C1b, on a sequential test of liveness whose wealth reached 25.5 against a null fixed in advance [CHARTER §6, A3.2]. The close of C1's first window, C1a, rested on exact criteria written in its brief: pins, agreement of the checkers, the kernel's size, and counts of forecasts and resolutions [REPORT, C1a report §1]. Promotion has not governed who holds which key. Since a layer must hold its own powers while it is tested, a rule that made promotion govern keys could only require the earlier layer's promotion before a later layer's keys are granted: the judge would refuse such a key entry until the earlier `promote` is on the log. No such rule is in the charter or the code. What the implementation has done is change its law only by its own procedure and, from C1a on, promote its layers only on its own record. The institution that will judge the agent's changes was thus built from proposals its own kernel admitted and its own judge checked, while every forecast made along the way was scored on its own ledger.

### 5.2 The builders are the first subjects

Before the agent exists, the only proposers are those building the institution: model sessions acting as builders, reviewers and counsel, the merging process, and the operator [seqs 0, 34, 51, 201]. The charter binds them by the means it will use on the agent: "Whatever counsel and builders are forbidden is what the agent of C3 is forbidden, by the same judge, keys and amendment path; nothing is imposed on the agent that was not first imposed on us" [CHARTER A2.10].

We argue for this on three grounds:
1. **Rules of conduct should enter only from cases** [CHARTER A2.1; Hart 1961; Hayek 1973]. A rule that binds the agent but has never refused a builder's act enters the agent's era as a guess.
2. **The nulls must predate the windows they judge** (Proposition 4). The builders' record supplies them. C1b's null, $p_0 = 6/11$, was measured on the builders' record through seq 163 and committed before C1b's window opened. It is the more demanding of two ways of attributing repairs to writs: the brief's own rule gives $5/11$ [`transcripts/BRIEF-C1b-draft.md`, "Null"]. It is a threshold fixed in advance, not a confidence bound on the builders' own rate.
3. **The builders run the agent's policy class.** They are sessions of large language models, from frontier models to small ones, so a law that is usable by its builders, and that holds against their accidents, has been exercised by the policy class the agent will use.

What this does *not* establish is that reliability transfers from builders to the agent, or resistance to an adversary, since builders are not adversaries. That is a separate obligation. The charter requires a simulator of named attacks — self-judging, retroactive, forged, forking, stalling and others — to run clean before any model touches a layer [CHARTER §6], and the agent's layer will need a red team in the sense of AI control [Greenblatt et al. 2024].

The leading self-improving systems build the agent first and wrap it in governance held fixed and trusted as infrastructure [Zhang et al. 2025, 2026]. Even designs with a frozen evaluator build the frozen zone outside the law it enforces [Neal 2026]. The nearest precedents are partial. SEA recommends deploying its statistical gate first, before its other loop controllers [Sengupta 2026, §4.4]. Nomic's players are subject to the rules they change [Suber 1990]. And a compiler that compiles itself has long made its builders its first users [Thompson 1984]. We know of no earlier design that subjects the model sessions building an AI's governing law to that law before the AI exists.

In the implementation the builders have been subject to it since their keys were declared [seqs 6–8, 19 October 2026]. Builder and reviewer keys have since signed 6,621 of the log's 7,810 entries. Most of these are the two streams: 5,811 of their 5,919 forecasts and resolutions are of the two stream types, and 627 of their 702 proposals are titled as batches of either stream. Of the other 75, 46 are reads and reviews of briefs and code; the rest carry code and pins, fixes, and other forecasts [titles in the log at seq 7809: stream batches are titles beginning `due `, `freshness`, `hkjc` or `M2 race`; reads and reviews are titles naming the word read or review, less the two read-gate proposals at seqs 654 and 657]. So the law has been exercised far more by routine than by construction.

---

## 6 Reference implementation and status

The reference implementation runs in public as `renavondata/jack`. The charter's SHA-256 is in the signed genesis entry [seq 0, 2026-10-14T05:41:39Z]. The kernel is 450 lines of standard-library Python [`tools/count_kernel.py`]. At C0's exit, a second kernel in Go agreed with it on 100,000 seeded logs and 658,885 prefixes [REPORT §8.1].

**Table 2. Layers and windows, from the log.**

| Layer | Entry | Outcome |
|---|---|---|
| C0, the record | genesis, seq 0 (14 Oct) | promoted by a signed tag before windows existed; not pre-registered |
| C1a, the ledger (C1's first window) | `promote`, seq 188 (31 Oct) | every pre-stated criterion met; closed early under A5, entered during the window |
| C1b, the clerk (C1's second window) | `promote`, seq 337 (1 Nov) | C1 promoted: $M = 214358881/8398080 \approx 25.5$ over nine items, $p_0 = 6/11$; cap and attribution rule changed during the window (§4.3) |
| C2a, value | opened at seq 367 (1 Nov) | value wealth (per-event form) crossed early; **failed**: nine repair rows off the record under the operator's login, one his own act; `fix` at seq 5563 |
| C2a′ | opened at seq 5564 (17 Nov) | **failed** on a fault in the evaluator's check of an unchanged scope; ended by veto at seq 7180 |
| C2a, third window | brief read, grant at seq 7615 (24 Nov) | opens at the first push after 2026-11-30T00:00Z |
| C2b, C2c, C3 | — | not opened; no agent exists |

Each failure illustrates the construction. In C2a's first window the value test crossed early, but comparison with the platform's independent record of the operator's acts found nine acts under the operator's login that its classifier types as repairs. Counsel checked them by hand. One was the operator's own act, at counsel's request. Five were the court's machinery acting under his login: a re-run of the judge, a pull request closed by a keyword, and three labels. The hand behind the remaining three, closes of issues, could not be established. The classifier can only type all nine as his [`transcripts/BRIEF-C2a-prime-draft.md`, "The nine rows"; `transcripts/evidence/acts-20261103T2144.csv`]. One suffices: under the conjunctive rule (Proposition 5) the window could not be promoted. None of the nine was re-attributed. The remedy gave the court's platform acts an identity of their own, a GitHub App [seqs 5562–5563]. The second failure, C2a′, was a fault in the judge, not in the judged: the evaluator's walk of the commits for criterion 3 [`transcripts/BRIEF-C2a-3-draft.md`]. The evaluator was then moved into the trusted base by a push whose changed lines had been marked in advance [grant seq 6851; push seq 7281], and the failed window stayed failed.

**The value evidence, recomputed.** We recomputed the implementation's value test on its own record, retrospectively, under the following protocol [`block_on_log.py`, an ancillary file]. The choices were made after the record existed, so this is an audit of the record, not a prospectively registered decision. Its thresholds bound the false-crossing probability of this protocol as fixed. They do not cover the choice among the protocols considered while this paper was revised. That choice changed four rules in turn: membership by a forecast before the cutoff, resolutions after the deadline counted as expiries, pending sittings left unscored, and every sitting assigned to a class at its cutoff. In every version, the first two classes crossed against the pooled base rate, with final wealth from $1.99 \times 10^4$ to $2.23 \times 10^4$ and from $1.11 \times 10^4$ to $1.62 \times 10^4$. In every version that computed it, the per-dataset wealth never exceeded 1 [`04-selfcheck.md`, rounds 4–8, an ancillary file].
- **Observation.** The record runs from C2a's opening (seq 367) to seq 7809, observed at its last entry, 2026-11-25T11:05Z.
- **Events.** They are the value events the implementation's own code selects, without its gate on the attack simulator.
- **Sittings.** An event belongs to the sitting of its forecast cutoff only if some party forecast it before that cutoff; 19 resolved events with no such forecast are not members. Its deadline is the latest `resolves_by` among those forecasts. A sitting is scored once every member has resolved or passed its deadline. A resolution that lands after the deadline does not count: the event expired at the deadline. A sitting none of whose members resolved in time contributes the factor 1 and does not advance its class's stake count. That gives 476 sittings scored and 4 still pending at the time of observation. 170 member events expired, 168 of them resolved only after the deadline, and the statistic uses the events that resolved in time (§4.3).
- **Information.** Base rates, mixture weights and stakes use only what was recorded before the sitting's cutoff. The weights use every member event resolved by its deadline and before the cutoff, across classes and from partly resolved sittings; base rates use every resolution recorded before the cutoff. So Proposition 3(b)'s regret bound applies neither class by class nor over the whole sequence.
- **Classes.** Every sitting, pending or not, is assigned when its cutoff passes, so the assignment does not change as later outcomes arrive. The sittings fall into five lag classes, with the thresholds $\ell(\ell+1)/\alpha$ of §4.3.
- **Forecasters.** Almost all the forecasts in the implementation's 2,820 selected events come from one party: 2,795 from reviewer sessions and 12 from builders. The forecasting procedure is one small model: of the log's 2,887 freshness forecasts, 2,869 name their model in their arguments, and all of those name `openai/gpt-5.4-mini` [log at seq 7809].

The results depend on the base rate:
- **Pooled across datasets,** as in the implementation: the first two classes end at $1.99 \times 10^4$ and $1.11 \times 10^4$ (the second peaked at $1.19 \times 10^4$), far above their thresholds of 40 and 120.
- **Kept per dataset:** no class's wealth ever exceeds 1.

So the record gives evidence that the stream's forecaster had, at some sitting, a conditional advantage over a base rate pooled across datasets, and no evidence of one over a base rate kept per dataset. Failing to reject does not show that there is no further skill, and gives no bound on how much there might be. But this recomputation finds none, and a fixed table of one probability per dataset also beats the pooled base rate (§8).

The implementation's own per-event figure on its 2,820 selected events, $1.52 \times 10^{60}$, is not comparable evidence. It compounds one bet per event, 5.9 per sitting on average, and has no guaranteed level when outcomes within a sitting are dependent. Table 3 removes its departures from the block form one at a time, against the pooled base rate. Of the 56 orders of magnitude between the implementation's figure and the first lag class's, the step from one bet per event to one per sitting accounts for 48. The differences between successive rows are not a causal decomposition, since the rows also differ in which events they use and in what they score.

**Table 3. From the implementation's figure to the block form, against the pooled base rate.**

| Process | Events | Scored | Wealth | Orders removed |
|----------|-----|-----|----|---|
| The implementation's: one bet per event | all 2,820 | each event's marginal | $1.52 \times 10^{60}$ | — |
| Only information recorded before the cutoff; late resolutions expire | resolved in time | each event's marginal | $2.49 \times 10^{58}$ | 1.8 |
| One bet per sitting, in one process | resolved in time | the sitting's joint forecast | $1.74 \times 10^{10}$ | 48.2 |
| One bet per sitting, in lag classes (class 1) | resolved in time | the sitting's joint forecast | $1.99 \times 10^{4}$ | 5.9 |

The charter states in advance four falsifiers, results that would show the construction wrong [CHARTER §12]. On the record: the first's size clause has been tested and not met, and its Datalog clause has not been tested; the second has not been tested as worded, since it names the baseline of assize, the programme's earlier repository [CHARTER §1]; the third has not been met, though re-attribution came near it; and the fourth has been met on a literal reading, by 14-day intervals that begin in the first days after genesis, before any key could forecast.
- *"C0 cannot hold recognition, change and adjudication within 1,500 lines, or Datalog cannot express C0's rules."* The kernel holds them in 450 lines. The Datalog clause has not been put to the test, because no rule has been entered (§8).
- *"C1's window fails against assize's baseline."* Both of C1's windows passed and were promoted. C1b's liveness test crossed with $M \approx 25.5$, but against a null taken from the builders' own record, $p_0 = 6/11$, not assize's (Table 2; §5.2).
- *"Repairs fall only because acts are re-typed as decisions."* No entry on the log has been re-typed: the typing predicate has not changed since it entered the code [`git log -S`, 879caf9, 31 October]. Off the log, repairs did fall by re-attribution. Under a rule stated before C1b's exit evaluation, a platform act under the operator's login is attributed to the party that declared it. That cut the repair rows from 7 to 1 in the acts table of 1 November, from 61 to 1 in the first of 3 November, and from 81 to 9 in the second, taken at 21:44 [`transcripts/BRIEF-C1b-draft.md`, Amendment 2; `acts-20261101`, `acts-20261103` and `acts-20261103T2144`, each against its `-raw` twin]. This moves acts to other parties rather than re-typing them as decisions, so the falsifier as worded is not met; but it is the nearest case. The nine rows that remained were not re-attributed, and C2a failed on them. The coded exception for a `fix` naming a failed window lifts a taint without re-typing the act (§4.5).
- *Procedure outgrowing object "at more than assize's 5 : 1 (20 : 4) in any 14-day window".* By the evaluator's count per window, procedure to object stood at 127 : 32 for C1a (4.0 : 1, the closest), 67 : 82 for C1b, 1,131 : 3,449 for C2a's first window, and 320 : 1,296 for C2a′ at its veto [`judge/status.py --as-of` each end]. The evaluator counts per window, not per 14 days. Counted over complete 14-day intervals within the record (each ending by its last entry), by the evaluator's own rule for object entries, the ratio exceeds 5 : 1 only for some intervals that begin between genesis and 17 October. The worst begins at genesis, at 63 : 5. No key could forecast until A3 came into force at seq 31, on 25 October, and the first object entry is seq 38. Every interval that begins at or after seq 31 stays at or below 872 : 1,755, about 0.5 : 1 [log at seq 7809; `judge/status.py`, the `world` set; intervals half-open, with every start time at which a count changes]. The count classes as procedure the proposals that carry stream forecasts, and the ratio can be padded (§8).

---

## 7 Related work

**What is not new.** None of the component results is new, and several mechanisms precede this work: signed or hash-chained logs for agents [Ghosh 2026; Nakajima 2026; Bracale Syrnikov et al. 2026], frozen evaluators [Zhang et al. 2026], pre-registration with human ratification of promotions [Neal 2026], and anytime-valid gates on self-edits [Wu et al. 2025; Shawn 2026; Sengupta 2026; Sun et al. 2026; Gao, Qi & Cui 2026]. The precedents for each new claim are below: self-adaptive and self-amending systems for the first, interactive imitation learning and oversight metrics for the second (§4.5), and partial precedents for the third (§5.2).

**Self-improving agents.** The Gödel machine requires a proof of utility before a rewrite [Schmidhuber 2003]. Later systems validate rewrites on benchmarks instead [Yin et al. 2024; Robeyns, Szummer & Aitchison 2025; Zhang et al. 2025, 2026].

Two recent studies point the same way as this paper. A survey of safety in self-evolving agents holds that utility alone does not authorise promotion [Chen J. et al. 2026], and a census of the field finds the improvement process rarely tested [Chen, Zhu & Zheng 2026]. Here the process itself, run by an institution, is the object tested.

**Self-adaptive systems.** Autonomic computing closes a monitor–analyse–plan–execute loop over a managed system [Kephart & Chess 2003], and architecture-based self-adaptation changes a running system's architecture under an external manager [Garlan et al. 2004]. In the systems cited, the manager is fixed and trusted. Here the governing institution is itself the thing promoted, layer by layer, by test on its own record.

**Statistical gates on self-modification.** Several recent systems gate *edits of the agent* against an incumbent. SGM allocates a familywise error budget across edits [Wu et al. 2025]. PACE makes each commit an anytime-valid paired test with a per-decision guarantee [Shawn 2026]. SEA composes confidence sequences and e-processes into per-controller gates, recorded on a certificate ledger around a frozen base model; it leaves the guarantees of that composition under an endogenous proposer as open conjectures [Sengupta 2026]. REUSE controls false promotions over a whole run when benchmarks are reused [Sun et al. 2026], and TRUST controls a false-evolution rate [Gao, Qi & Cui 2026]. Two theoretical results bound what such gates can do. Cai et al. [2026] show that the validation needed for reliable adoption diverges as the incumbent nears its ceiling, and Scrivens [2026] bounds what gates with power-law risk schedules can admit, under overlap conditions. In our reading, none of these gates tests liveness or the principal's burden, or promotes the institution that does the gating. SEA does accumulate each version's evidence across rounds [Sengupta 2026, §4.4]; what is particular here is that one institutional test's wealth continues across failed windows.

**Evaluators that change.** Hyperagents fix the evaluator for now [Zhang et al. 2026]. The Red Queen Gödel Machine co-evolves its evaluator and re-estimates past utilities (§4.4) [Iacob et al. 2026]. Our specification allows change only by replay of past verdicts, with every change to them marked in advance (Proposition 6); CI enforces three rows of the replay (§4.4).

**Frozen zones, audited loops, signed logs.** The closest precedent for pre-registration with a human gate is SFA-Bench's AutoLab [Neal 2026]. It combines a hash-attested frozen zone, a declaration sealed before each patch, a hash-chained meta-ledger and promotion by human ratification token.

Secure audit logs are older still [Schneier & Kelsey 1999]. Other systems log, sign or govern agents' acts. Regimes derives the agent's state from an append-only event log in which promotions are events [Nakajima 2026]. ASG-SI proposes replayable evidence bundles for promoting skills [Huang & Huang 2025]. Tracekit signs tool calls in a witnessed Merkle log [Ghosh 2026]. AgentBound enforces owner-signed behavioural constitutions at runtime [Kaul, Lan & Gupta 2026]. Institutional AI governs collusion between agents through a public governance graph and a keyed governance log [Bracale Syrnikov et al. 2026]. Governable Individuals widen an agent's authority only by signed lifecycle transitions [Qin et al. 2026]. These works anticipate the record. In our reading, none makes the log the source of law in this sense: that the admissibility of each entry is a function of the law folded from the entries before it, so that the law changes only by entries and binds only forward. None scores the parties' claims, and none promotes the institution by sequential test.

**Electronic institutions.** Executable institutions for agents have a long history in multi-agent systems. Law-governed interaction enforces explicit policies on heterogeneous agents through generic controllers [Minsky & Ungureanu 2000]. Norm-governed computational societies are specified in executable logic [Artikis, Sergot & Pitt 2009]. Their rules can be changed at run time by the agents they govern [Artikis 2012]. Six of Ostrom's eight principles for self-governing institutions have been axiomatised in the Event Calculus and run in a testbed [Pitt, Schaumeier & Artikis 2012]. AgentCity has agents legislate operational rules as smart contracts, which it calls the law itself, under a human chain of ownership [Ruan & Zhang 2026]. These works anticipate law as executable rules that change under themselves. In our reading, none lets its institution grow only by sequential test on its own record, scores the parties' claims as forecasts, or is built before, and first imposed on, the agents it will govern.

**Self-amending systems.** Rules that change under themselves have a longer history. Suber's Nomic and his study of self-amendment show how a rule system can change its own rules of change [Suber 1990], and the Tezos ledger amends its own protocol by on-chain vote [Goodman 2014]. Our amendment path follows the same pattern: one act makes a rule mutable, a second changes it, and the change takes effect only at a stated height [CHARTER A2.7]. The difference is that change is priced and scored, and that each layer after the record is frozen, and the next begun, only on sequential evidence about the institution's own record.

**Control, law and agency.** AI control separates a trusted monitor from an untrusted policy [Greenblatt et al. 2024]. The lock applies that separation to the evaluation infrastructure, by keys rather than instructions. Kolt [2026a, 2026b] frames the legal problem. Constitutions used in training [Bai et al. 2022] shape a model's outputs; the constitution here is enforced by a checker the model cannot reach.

**Testing by betting.** The tests follow the prequential principle [Dawid 1984] and game-theoretic testing [Shafer & Vovk 2019; Ramdas et al. 2023]. They are closest to the sequential comparison of forecasters [Henzi & Ziegel 2022; Choe & Ramdas 2024a], and the lag classes and blocks answer the problem of filtrations that Choe & Ramdas [2024b] treat in general.

---

## 8 Limitations and open questions

**The choice of null.** The value null pits the aggregate against a base rate pooled by event type, which is a weak baseline. An audit on the record constructs a fixed table, one probability per dataset, that would have crossed the value threshold at the 53rd event [`transcripts/AUDIT-criteria-20261117.md`]. Against a base rate kept per dataset, the record shows no evidence of an advantage (§6). The theory's remedy is a stronger incumbent, entered as an entrant and met by the same bounded-difference bet [Choe & Ramdas 2024a], with a separate check of resolution as well as calibration. Murphy's decomposition does this for the Brier score [Murphy 1973], and the expected score of any strictly proper score, the logarithmic among them, decomposes into uncertainty, resolution and reliability [Bröcker 2009]. A sequential gate built on that decomposition, and the choice of incumbent, are open.

**What passing certifies.** Passing is evidence, at level $\alpha$, against two pointwise nulls over the layer's life: that the aggregate never had a conditional advantage over the base rate, and that the institution never completed its own work on time and free of repairs at a rate above $p_0$. It is not a guarantee of current performance, since earlier wealth can carry a later window (§4.3). Nor does it certify that letting the next layer begin improves the principal's welfare or safety. That link is the design's hypothesis, and testing it needs the controlled comparison below.

**Criteria that a system without skill can pass.** The same audit classes 9 of the 28 window criteria it examined as passable without skill. Liveness is one of them: a forecast resolved on time counts as a success whatever its content. The ratio of procedure to object is another: it can be met by padding the record with unanswered forecasts [`transcripts/AUDIT-criteria-20261117.md`]. Liveness as defined here measures timely, repair-free completion, not the worth of what is completed. Measuring the worth of the work is open.

**Validity against recency.** Carrying wealth keeps the level over the institution's life but lets old evidence carry a new window. A fresh process per window at a split α, or a change-detecting e-process, would keep validity and trade power for recency. The right trade for promotion is open.

**Correlated readers and checkers.** The weight of agreement between the two kernels, or between cold reads by different model families, is bounded by their shared error (§4.4). For C1's new entry types the two kernels were written by models of one family, so their agreement on that code is the weakest the implementation has. That error should be estimated against executable or human references, as Kim et al. [2025] do for language models. In the implementation, cross-family reads gate law-level texts by procedure, not yet by code.

**Who operates the world.** One of the two scored streams, the freshness of datasets, resolves from pages of renavon.com, a data marketplace the author operates, and the operator's key holds the power to forecast [forecasts of type `world.renavon`; seq 33], though none of his three forecasts is on that stream [log at seq 7809]. That exposes the stream to the performative case Table 1 warns against: he could move these outcomes, and the record could not show it.

**Completeness of the record of acts.** The operator's acts are collected from one platform. The monitor the charter requires — one that the operator does not run [CHARTER A2.8] — is not yet built.

**Sufficiency of three secondary rules.** No primary rule has yet been needed: the log holds no `rule` entry [CHARTER A2.1; log at seq 7809]. That the three suffice until the agent arrives is a conjecture under test.

**Mixture or market.** The election is a Bayes mixture over a roster fixed for each layer. A market of traders, in the manner of logical induction [Garrabrant et al. 2016], would let the roster grow, but needs its own argument for anytime validity.

**No controlled comparison.** The evidence is one case history, with one promotion on a sequential test (§5.1). The experiment that would test the design is a controlled comparison of growth by test against simpler governance, such as a frozen evaluator with per-edit gates, under repeated runs and deliberate attacks. We have not run it.

**One principal; a short record.** The construction serves one owner of the utility. Kolt's principle of inclusivity [2026a] asks for more. The evidence so far covers one operator, two streams and six weeks. The agent, C3, is still a forecast.

---

## 9 Conclusion

We have argued that what judges a self-modifying agent should lie outside the agent's reach, and should itself be judged by something other than trust. The institution we propose is built before the agent, binds its builders first, holds its law as a fold over a signed record, prices claims of merit as forecasts, and grows only by sequential tests on its own record. The reference implementation does this for the order of its layers, once so far on a sequential test, and no rule yet ties its keys to promotion. The guarantees are modest and exact. The natural per-event test of value loses its level when outcomes resolve together, and the block form keeps it. The first test of the construction is whether its record can show it wrong. It can: the block-form test of value, run retrospectively on the reference implementation's record, finds no evidence of an advantage over a base rate kept per dataset. Under this design, the value the next layer claims should be measured against that baseline.

---

## Disclosure

Claude drafted the charter and the specification [CHARTER, head; commit trailers of `SPEC.md`]. Models from Anthropic, OpenAI and Google wrote the code. Where a commit's trailer names the model, that is the record. Since 19 October 2026 the model sessions have acted under keys declared on the record. Of the builder and reviewer sessions filed through the runner from 30 October to the observation of §6 on 25 November, 720 of about 850 whose issue titles name their model ran `openai/gpt-5.4-mini` [titles of renavondata/opencode-runner issues; the count of titles naming a model depends on how they are parsed]. The second kernel was written without reading the first (§4.4). This paper was drafted by a model session that holds no key, working from the repository and the literature; the author read and revised it. It develops part of the author's book-length account of the programme [Freeman 2026], which is not peer-reviewed. The paper is meant to stand alone, and relies on the book for no claim. No model is an author. The author is responsible for every claim.

## Code and data

- Repository, with the log, kernels, judge, briefs and rulings: github.com/renavondata/jack.
- Ancillary files of this paper: `lean/`, the Lean proofs of §4 (`lake build`, with a table from propositions to theorems); `sim_filtration.py`, the simulations of §4.3; `block_on_log.py`, the recomputation of §6 with its ablations and both base rates, run in any checkout of the repository as `python3 block_on_log.py --rev e580b64`; it reads that commit by `git show` and writes nothing. `04-selfcheck.md`, the check of each factual claim against its source, round by round.
- Founding note: "The Science Was Done. The Engineering Wasn't.", gfrm.in, 1 November 2026.

---

## References

- Alpern, B. & Schneider, F. B. (1985). Defining liveness. *Information Processing Letters* 21(4):181–185. doi:10.1016/0020-0190(85)90056-0
- Anderson, J. P. (1972). *Computer Security Technology Planning Study.* ESD-TR-73-51, USAF Electronic Systems Division.
- Artikis, A. (2012). Dynamic specification of open agent systems. *Journal of Logic and Computation* 22(6):1301–1334.
- Artikis, A., Sergot, M. & Pitt, J. (2009). Specifying norm-governed computational societies. *ACM Transactions on Computational Logic* 10(1):1–42.
- Arrow, K. J. & Fisher, A. C. (1974). Environmental preservation, uncertainty, and irreversibility. *QJE* 88(2):312–319. doi:10.2307/1883074
- Bai, Y., Kadavath, S., Kundu, S., Askell, A. et al. (2022). Constitutional AI: Harmlessness from AI feedback. arXiv:2212.08073.
- Berger, R. L. (1982). Multiparameter hypothesis testing and acceptance sampling. *Technometrics* 24(4):295–300. doi:10.2307/1267823
- Bracale Syrnikov, M., Pierucci, F., Galisai, M., Prandi, M. et al. (2026). Institutional AI: Governing LLM collusion in multi-agent Cournot markets via public governance graphs. arXiv:2601.11369.
- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review* 78(1):1–3.
- Bröcker, J. (2009). Reliability, sufficiency, and the decomposition of proper scores. *Quarterly Journal of the Royal Meteorological Society*. doi:10.1002/qj.456; arXiv:0806.0813.
- Burns, B., Grant, B., Oppenheimer, D., Brewer, E. & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *Communications of the ACM* 59(5):50–57. doi:10.1145/2890784
- Cai, Q., Zhang, Y., Nie, J. et al. (2026). A theory of reliable self-evolution for agent harnesses. arXiv:2609.08175.
- Cesa-Bianchi, N. & Lugosi, G. (2006). *Prediction, Learning, and Games.* Cambridge University Press. doi:10.1017/CBO9780511546921
- Chen, J., Feng, Z., Ma, O. et al. (2026). Safety in self-evolving agents: A survey. arXiv:2610.00093.
- Chen, Z., Zhu, D. & Zheng, L. N. (2026). Auditing the product, not the recursion: The evaluation evidence behind recursive self-improvement claims. arXiv:2610.27610.
- Choe, Y. J. & Ramdas, A. (2024a). Comparing sequential forecasters. *Operations Research* 72(4):1368–1387. doi:10.1287/opre.2021.0792
- Choe, Y. J. & Ramdas, A. (2024b). Combining evidence across filtrations. arXiv:2402.09698.
- Coke, E. (1610). Dr Bonham's Case, 8 Co. Rep. 107a.
- Conant, R. C. & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *Int. J. Systems Science* 1(2):89–97. doi:10.1080/00207727008920220
- Dawid, A. P. (1984). Present position and potential developments: Some personal views. Statistical theory: The prequential approach. *JRSS A* 147(2):278–292. doi:10.2307/2981683
- de Moura, L. & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. *CADE-28*, LNCS 12699:625–635. doi:10.1007/978-3-030-79876-5_37
- Dennis, J. B. & Van Horn, E. C. (1966). Programming semantics for multiprogrammed computations. *Communications of the ACM* 9(3):143–155. doi:10.1145/365230.365252
- Freeman, G. (2026). *A Court for Agents: Law, scoring and the self-modifying machine.* Online book, not peer-reviewed. gfrm.in/book; source github.com/gfrmin/agent-court, commit 007a007.
- Fuller, L. L. (1964). *The Morality of Law.* Yale University Press.
- Gall, J. (1977). *Systemantics: How Systems Work and Especially How They Fail.* Quadrangle.
- Gao, Z., Qi, Z. & Cui, Y. (2026). Trustworthy recursive self-improvement with statistical guarantees. arXiv:2611.10787.
- Garlan, D., Cheng, S.-W., Huang, A.-C., Schmerl, B. & Steenkiste, P. (2004). Rainbow: Architecture-based self-adaptation with reusable infrastructure. *Computer* 37(10):46–54. doi:10.1109/MC.2004.175
- Garrabrant, S., Benson-Tilsen, T., Critch, A., Soares, N. & Taylor, J. (2016). Logical induction. arXiv:1609.03543.
- Ghosh, B. (2026). Tracekit: Tamper-evident intent-reasoning-action auditing for AI agents. arXiv:2609.35659.
- Gneiting, T. & Raftery, A. E. (2007). Strictly proper scoring rules, prediction, and estimation. *JASA* 102(477):359–378. doi:10.1198/016214506000001437
- Good, I. J. (1952). Rational decisions. *JRSS B* 14(1):107–114. doi:10.1111/j.2517-6161.1952.tb00104.x
- Goodhart, C. A. E. (1975). Problems of monetary management: The U.K. experience. *Papers in Monetary Economics*, vol. I. Reserve Bank of Australia.
- Goodman, L. M. (2014). Tezos — a self-amending crypto-ledger. White paper, 2 September 2014. tezos.com/whitepaper.pdf
- Greenblatt, R., Shlegeris, B., Sachan, K. & Roger, F. (2024). AI control: Improving safety despite intentional subversion. *ICML 2024*; arXiv:2312.06942.
- Hadfield-Menell, D., Dragan, A., Abbeel, P. & Russell, S. (2016). Cooperative inverse reinforcement learning. *NeurIPS 29*; arXiv:1606.03137.
- Hart, H. L. A. (1961). *The Concept of Law.* Clarendon Press.
- Hayek, F. A. (1973). *Law, Legislation and Liberty, vol. 1: Rules and Order.* University of Chicago Press.
- Henry, C. (1974). Option values in the economics of irreplaceable assets. *Review of Economic Studies* 41:89–104. doi:10.2307/2296373
- Henzi, A. & Ziegel, J. F. (2022). Valid sequential inference on probability forecast performance. *Biometrika* 109(3):647–663. doi:10.1093/biomet/asab047
- Holmström, B. (1979). Moral hazard and observability. *Bell Journal of Economics* 10(1):74–91. doi:10.2307/3003320
- Huang, K. & Huang, J. (2025). Audited skill-graph self-improvement for agentic LLMs via verifiable rewards, experience synthesis, and continual memory. arXiv:2512.23760.
- Iacob, A., Jovanović, A., Shen, W. F. et al. (2026). The Red Queen Gödel Machine: Co-evolving agents and their evaluators. arXiv:2606.26294.
- Jensen, M. C. & Meckling, W. H. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. *Journal of Financial Economics* 3(4):305–360. doi:10.1016/0304-405X(76)90026-X
- Kaul, A., Lan, Q. & Gupta, P. (2026). Behavioral governance for autonomous AI agents: The AgentBound framework. arXiv:2606.30970.
- Kephart, J. O. & Chess, D. M. (2003). The vision of autonomic computing. *Computer* 36(1):41–50. doi:10.1109/MC.2003.1160055
- Kim, E., Garg, A., Peng, K. & Garg, N. (2025). Correlated errors in large language models. *ICML 2025*; arXiv:2506.07962.
- Knight, J. C. & Leveson, N. G. (1986). An experimental evaluation of the assumption of independence in multiversion programming. *IEEE TSE* SE-12(1):96–109. doi:10.1109/TSE.1986.6312924
- Kolluri, A., Sharma, R., Costa, M., Köpf, B. & Nießen, T. (2026). Optimizing agent planning for security and autonomy. arXiv:2602.11416.
- Kolt, N. (2026a). Governing AI agents. *Notre Dame Law Review* 101:335; arXiv:2501.07913.
- Kolt, N. (2026b). Superintelligence and law. arXiv:2603.28669.
- Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system. *Communications of the ACM* 21(7):558–565. doi:10.1145/359545.359563
- Löb, M. H. (1955). Solution of a problem of Leon Henkin. *Journal of Symbolic Logic* 20(2):115–118. doi:10.2307/2266895
- Madison, J. (1788). *The Federalist* No. 51.
- The mathlib Community (2020). The Lean mathematical library. *CPP 2020*, 367–381. doi:10.1145/3372885.3373824
- McCain, M., Millar, T., Huang, S. et al. (2026). Measuring AI agent autonomy in practice. Anthropic, 18 February 2026. anthropic.com/research/measuring-agent-autonomy
- Miller, M. S. (2006). *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control.* PhD thesis, Johns Hopkins University.
- Minsky, N. H. & Ungureanu, V. (2000). Law-governed interaction: a coordination and control mechanism for heterogeneous distributed systems. *ACM Transactions on Software Engineering and Methodology* 9(3):273–305. doi:10.1145/352591.352592
- Murphy, A. H. (1973). A new vector partition of the probability score. *Journal of Applied Meteorology* 12(4):595–600. doi:10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2
- Nakajima, Y. (2026). Regimes: An auditable, held-out-gated improvement loop demonstrated on LongMemEval with ActiveGraph. arXiv:2606.10241.
- Neal, M. (2026). SFA-Bench v2.0.0-alpha.2: Locked campaign execution and evidence capture (with SFA-AutoLab). Software, github.com/iotaverbum-core/sfa-bench. doi:10.5281/zenodo.20766587
- Perdomo, J., Zrnic, T., Mendler-Dünner, C. & Hardt, M. (2020). Performative prediction. *ICML 2020*, PMLR 119:7599–7609; arXiv:2002.06673.
- Pitt, J., Schaumeier, J. & Artikis, A. (2012). Axiomatization of socio-economic principles for self-organizing institutions: concepts, experiments and challenges. *ACM Transactions on Autonomous and Adaptive Systems* 7(4). doi:10.1145/2382570.2382575
- Qin, X., Luan, S., Yang, C. & Li, Z. (2026). Governable individuals: An identity layer for embodied agents that keep learning. arXiv:2607.05463.
- Ramdas, A., Grünwald, P., Vovk, V. & Shafer, G. (2023). Game-theoretic statistics and safe anytime-valid inference. *Statistical Science* 38(4):576–601. doi:10.1214/23-STS894
- Rice, H. G. (1953). Classes of recursively enumerable sets and their decision problems. *Trans. AMS* 74(2):358–366. doi:10.1090/S0002-9947-1953-0053041-6
- Robeyns, M., Szummer, M. & Aitchison, L. (2025). A self-improving coding agent. arXiv:2504.15228.
- Ross, S., Gordon, G. J. & Bagnell, J. A. (2011). A reduction of imitation learning and structured prediction to no-regret online learning. *AISTATS 2011*, PMLR 15:627–635; arXiv:1011.0686.
- Ruan, A. & Zhang, X. (2026). AgentCity: Constitutional governance for autonomous agent economies via separation of power. arXiv:2604.07007.
- Saltzer, J. H. & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE* 63(9):1278–1308. doi:10.1109/PROC.1975.9939
- Savage, L. J. (1971). Elicitation of personal probabilities and expectations. *JASA* 66(336):783–801. doi:10.1080/01621459.1971.10482346
- Schmidhuber, J. (2003). Gödel machines: Self-referential universal problem solvers making provably optimal self-improvements. arXiv:cs/0309048.
- Schneider, F. B. (1990). Implementing fault-tolerant services using the state machine approach: A tutorial. *ACM Computing Surveys* 22(4):299–319. doi:10.1145/98163.98167
- Schneier, B. & Kelsey, J. (1999). Secure audit logs to support computer forensics. *ACM Transactions on Information and System Security* 2(2):159–176.
- Scrivens, A. (2026). Information-theoretic limits of safety verification for self-improving systems. arXiv:2603.28650.
- Sengupta, B. (2026). Self-evolving agents with anytime-valid certificates. arXiv:2607.00871.
- Shafer, G. & Vovk, V. (2019). *Game-Theoretic Foundations for Probability and Finance.* Wiley. doi:10.1002/9781118548035
- Shawn, Z. (2026). PACE: Anytime-valid acceptance tests for self-evolving agents. arXiv:2606.08106.
- Suber, P. (1990). *The Paradox of Self-Amendment: A Study of Law, Logic, Omnipotence, and Change.* Bern: Peter Lang. (Appendix 3: Nomic.)
- Sun, X., Zeng, Y., She, Z. & Wang, X. (2026). Which self-improvements should we trust? Reliable self-improvement when agents reuse their benchmarks. arXiv:2609.33180.
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM* 27(8):761–763. doi:10.1145/358198.358210
- Ville, J. (1939). *Étude critique de la notion de collectif.* Gauthier-Villars.
- Wu, X., Yin, S., Kang, Y., Zhang, X. et al. (2025). SGM: A statistical Gödel machine for risk-controlled recursive self-modification. arXiv:2510.10232.
- Yin, X., Wang, X., Pan, L., Lin, L. et al. (2024). Gödel Agent: A self-referential agent framework for recursive self-improvement. arXiv:2410.04444.
- Yudkowsky, E. & Herreshoff, M. (2013). Tiling agents for self-modifying AI, and the Löbian obstacle. Technical report, Machine Intelligence Research Institute.
- Zhang, J. & Cho, K. (2017). Query-efficient imitation learning for end-to-end simulated driving. *AAAI 2017*, 31(1). doi:10.1609/aaai.v31i1.10857
- Zhang, J., Hu, S., Lu, C., Lange, R. & Clune, J. (2025). Darwin Gödel Machine: Open-ended evolution of self-improving agents. *ICLR 2026*; arXiv:2505.22954.
- Zhang, J., Zhao, B., Yang, W., Foerster, J. et al. (2026). Hyperagents. arXiv:2603.19461.
- Zhao, Y., Li, J., Li, L., Nian, Y. et al. (2026). Auditable claims about AI agents. arXiv:2610.07459.
