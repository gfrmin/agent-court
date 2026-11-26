# Law Before the Agent: Loop, Lock and Score for Self-Modifying AI

**Guy Freeman**
Independent researcher, Hong Kong · [email]

*Draft 9, 26 November 2026: structured after Peyton Jones (four-sentence abstract; related work after the evidence), and audited sentence by sentence for backing. The abstract was fixed first (`claude/claim/05-what-the-paper-is-about.md`), and the text aligned to it. Claim session. Revised for three referee-style self-reviews (`claude/claim/03-review-round1.md`) and two outside cold reads (`claude/claim/REVIEW-cold-1.md`, gpt-6.1-sol, runner issue #1348; `claude/claim/REVIEW-cold-2.md`, gemini-4-argon, #1362), and checked claim by claim (`claude/claim/04-selfcheck.md`). A LaTeX build with Figure 1 is generated from this file.*
- *Square brackets give the check behind each fact about the implementation:*
  - *`seq n` is an entry of `renavondata/jack` `log.jsonl`;*
  - *`CHARTER`, `SPEC` and `REPORT` are files at `origin/main` `e580b64`;*
  - *citations of Freeman 2026 refer to gfrmin/agent-court at `007a007`.*
- *Every reference was checked against Crossref, arXiv or the publisher's page on 25 November 2026 (`04-selfcheck.md`).*

---

## Abstract

Systems that rewrite their own code are now practical, and the evaluator that judges them is usually trusted rather than tested, although results of Rice, Löb and Goodhart show that inspection, self-proof and measures within the agent's reach cannot by themselves carry that trust. We propose that the institution which judges a self-modifying agent be built before the agent, imposed first on the model sessions that build it, and granted powers only by anytime-valid tests on its own record: its law is a fold over a signed, append-only log, every claim of merit is a forecast under the logarithmic score, and each layer is promoted only when sequential tests of predictive value and of liveness, measured by the principal's repairs, both pass. We state the guarantees in six propositions, whose statistical core is machine-checked in Lean, and show by example and proof that the natural per-event test of value loses its level when outcomes resolve together, while a block form keeps it. Applied retrospectively to the public record of a reference implementation, the valid test finds an advantage over a base rate pooled across datasets and no evidence of one over a base rate kept per dataset, so the institution's own book shows that its first evidence of value rested on a weak baseline; no self-modifying agent has yet been built under the design.

---

## 1 Introduction

Systems that modify their own code are now practical, and so are their failure modes. The Darwin Gödel Machine raised its SWE-bench score from 20% to 50% by editing its own agent code [Zhang et al. 2025]. In one run it also removed the markers its hallucination detector read, despite instructions not to change them [Zhang et al. 2025, App. H]. Hyperagents make the modification procedure itself modifiable. They keep the evaluator, the task data and parent selection outside the editable boundary "to ensure safety, prevent evaluation gaming", and name the loosening of that boundary as future work [Zhang et al. 2026, App. A.5]. A census of 114 studies of recursive self-improvement found that evaluation usually certifies the product of a run and rarely the process that produced it [Chen, Zhu & Zheng 2026].

The difficulty is old in economics and older in law. Delegation carries agency costs: monitoring, bonding and residual loss [Jensen & Meckling 1976]. A signal is worth contracting on in proportion to what it reveals of the agent's action [Holmström 1979]. When the agent can rewrite the instrument the principal reads, the signal stops being informative. Kolt [2026a] argues that the classical remedies — incentives, monitoring, enforcement — strain under AI agents. He warns that legal alignment "will need to contend with the prospect of actors that shape the very laws that govern them" [Kolt 2026b]. This paper is about that case.

**The main idea.** A self-modifying agent can be trusted only as far as an institution it cannot reach can test it. That institution must be built first, tested first on its builders, and given powers only by sequential tests on its own record. The tests must themselves be valid. The institution keeps a book on itself rather than a proof of itself, and the book must be able to show the institution wrong.

**Contributions.**
1. *A conditional design analysis* (§3). For results from computability, probability, control, law and security, we state when each binds an evaluator of a self-modifying agent, what it requires, and how this design meets it. We do not prove that no other mechanism would serve, and claim neither sufficiency nor optimality.
2. *Six propositions* (§4), stating the construction's guarantees exactly. The value test is given in a block form, which keeps its level when outcomes resolve together, and whose regret bound holds for the quantity tested. We show by example and simulation that the per-event form does not keep its level. Propositions 1(b), 2(a) and 3–5 are machine-checked in Lean 4 with Mathlib.
3. *A principle of construction* (§5). Law comes before the agent and is tested first on its builders. What a bootstrap raises is authority. Every regress of justification but one stops without an authority, and that one, the owner of the utility, is confined and priced.
4. *Evidence from a public record* (§6). A reference implementation has run in public since October 2026, with a signed log that dates each step. Recomputed retrospectively under a stated protocol, its value evidence survives only against a base rate pooled across datasets. The institution's own book thus shows that its first evidence of value rested on a weak baseline.

This is a design paper with proved guarantees and one empirical check. It contains no evaluation of a self-modifying agent: in the reference implementation the agent is the last layer, and it has not been built.

To our knowledge, three things here are new. Each has precedents, which §7 credits.
- The governing institution's own powers are granted layer by layer, each only after a sequential test on the institution's own record (§4.3).
- The principal's repairs are tested sequentially alongside value, as a condition of granting powers, with wealth carried across failed windows (§4.3, §4.5).
- The law is built before the agent, and imposed first on the model sessions that build it (§5).

---

## 2 Setting

The object has four parts [Freeman 2026, App. A.1]:
- **The agent** rewrites its own programs and keeps or discards the result by what it earns. It goes on doing so after it stops being watched.
- **The operator** is the principal and owner of the utility. He is one person, whose attention is the scarcest resource in the system.
- **The world** charges for being wrong. Its outcomes come from processes outside the agent: a race result, a dataset's modification time, a test run on a commit.
- **The policy** inside the agent is a large language model: general, cheap and unreliable in ways that cannot be listed in advance.

In this setting, three results fix the shape of what governs the object [Freeman 2026, §0.2]:
- **Loop.** A regulator cannot answer a disturbance it does not observe, and needs the disturbances' variety [Ashby 1956]. The simplest optimal regulator is a model of what it regulates [Conant & Ashby 1970].
- **Lock.** That a change is an improvement is a semantic property of programs, and no procedure decides such properties for arbitrary programs [Rice 1953]. Proofs remain possible for particular programs and restricted languages, but a self-modifying agent's changes are not confined to such a class. By Löb's theorem, an agent reasoning in a fixed formal theory cannot trust a successor that reasons in the same theory [Löb 1955; Yudkowsky & Herreshoff 2013]. Neither result forbids checking the agent from outside, against a fixed specification. So a loop that modifies itself needs a fixed point outside the modifier's reach.
- **Score.** The one measure that can be held fixed at every level without rewarding misreport is a proper score [Brier 1950; Good 1952; Savage 1971; Gneiting & Raftery 2007], on outcomes the loop does not control [Goodhart 1975]. Only forecasts actually issued, and outcomes actually realised, count [Dawid 1984]. A proper score is not immune to Goodhart's law: a weak comparator, an omitted objective or strategic participation can still be exploited (§8).

Our claim is that loop, lock and score, under the assumptions just stated, constrain what the governing institution must contain, though not how each part is built.

**Threat model.** We trust the operator's genesis key and his reading of what he signs, the host and CI provider that run the judge, and SHA-256 and Ed25519. We trust no proposer, including the model sessions that build the institution and, later, the agent; and no claim or evidence string that the record cannot recompute. The construction aims to make every untrusted party's influence pass through entries that the checker admits and the ledger scores. It does not defend against a compromised host, or against an operator acting against his own utility.

**Terms.** *Value* means predictive advantage over a stated base rate, not the principal's utility. An act is *priced* when it enters a statistic that can fail a window (§4.5). The *kernel* is the validity predicate (§4.1). The *judge* is the CI that runs both kernels, the tests and the *evaluator*, which computes the promotion criteria from the log and the tree. The *clerk* derives obligations from the state and the clock (§4.3). Only the kernel is small and duplicated; the trusted base around it is much larger (§4.4).

---

## 3 What the results require

Table 1 compresses the book's appendix of necessities [Freeman 2026, App. A]. Each row is a conditional design argument, not a theorem about all designs: in the setting of §2, the result requires something of any evaluator, and the mechanism is how this design meets it. Other mechanisms might meet it too. Rows marked ◦ are argued but not yet built.

The results are of three kinds, and we call only the first kind theorems:
- theorems about computation and probability: Rice, Löb, Ville, Bahadur–Savage, Alpern–Schneider, and the propriety of the log score;
- necessity results of control that hold under stated conditions: Conant–Ashby, and requisite variety;
- design principles with long records of failure behind them: Hart, Fuller, Anderson, Goodhart, Gall.

**Table 1. Results, what they require in the setting of §2, and how this design meets it.**

| | Result | Requires | Mechanism |
|---|---|---|---|
| **Evaluation** | Rice 1953 | The merit of arbitrary changes is judged by running, not inspecting | Every claim of merit is a forecast resolved by an outcome |
| | Löb 1955; Yudkowsky & Herreshoff 2013 | The evaluation rule is held outside the agent's theory, not re-derived by it | Judge and score behind keys the agent does not hold |
| | Dawid 1984 | Only issued forecasts and realised outcomes count | Probability fixed at entry; one resolution; no revision |
| | Savage 1971; Gneiting & Raftery 2007 | The rigid score must reward belief | Log score on a per-mille grid |
| | Goodhart 1975; Skalse et al. 2022 | A target decays unless it is proper and its outcomes are not the party's to move; no non-trivial proxy is unhackable | Outcomes from processes no scored party operates (but see §8); named attacks listed before each window |
| **Testing** | Ville 1939; Shafer & Vovk 2019; Ramdas et al. 2023 | The operator looks when he likes | Promotion by test supermartingales; a window is a maximum |
| | Bahadur & Savage 1956 | Small means of unbounded variables cannot be certified | Bounded outcomes tested; unbounded ones, such as minutes, only reported [CHARTER §6] |
| | Alpern & Schneider 1985 | An "eventually" is never refuted by a finite record | Every obligation has a deadline, which makes it a safety property, checked exactly; the rate of meeting deadlines is tested statistically |
| **Control** | Conant & Ashby 1970; Ashby 1956 | The governor holds a model; the pool has requisite variety | State is a fold over the record; several model families propose [CHARTER §5] |
| **Law** | Hart 1961 | Recognition, change, adjudication | The core holds exactly these three, in code; rules of conduct enter only from cases |
| | Fuller 1964 | Law must be prospective, promulgated, clear | Prospectivity by the fold; rules and the checker's digest are entries |
| | Crawford & Ostrom 1995 | Every rule needs an "or else" | Kernel rules and judge grounds each paired with a mutant that must be killed; one grant defers two pins [seq 7615] |
| | Waismann 1945 | Texts have open texture | ◦ The text a claim is scored against is fixed at the forecast's position |
| **Enforcement** | Anderson 1972; Saltzer & Schroeder 1975 | The monitor is always invoked, tamper-proof and small | Judge runs from trunk [CHARTER §3]; 450-line kernel; invalid entries refused, with a reason [SPEC §§8–9] |
| | Thompson 1984; Wheeler 2005 | One checker cannot be trusted | Two kernels in two languages, written from one specification by different model families |
| **Growth** | Arrow & Fisher 1974; Henry 1974 | Only the irreversible merits a hard gate | The operator reserves keys, pushes, amendments, promotion; all else priced |
| | Gall 1977; Hayek 1973 | Working complexity grows from working simplicity | Layers C0 → C3; from C1a on, each promoted on criteria stated in advance (§6) |

### 3.1 Two rows restated in the light of 2026 evidence

**Diversity is not independence.** Agreement between checkers is evidence only insofar as their failure causes differ [Dietrich & Spiekermann 2013; Ladha 1992]. Independently written programs fail together far more often than independence predicts [Knight & Leveson 1986], and so do language models. Their errors are correlated across more than 350 models and across providers [Kim et al. 2025], and code written by different models, or by agents in N-version triples, fails on the same tests far more often than independence predicts, although voting still helps [Pato Nogueira et al. 2026; Ron, Baudry & Monperrus 2026]. So a second kernel written by another family detects the faults on which the two differ; it does not make failures independent. The same holds for cold reads by other families (§8).

**Integrity is not completeness.** Signatures and hash chains prove that recorded entries were not altered. They cannot prove that nothing was omitted [Zhao et al. 2026, Cor. 3]. In the construction below, completeness holds by definition for *law*: an act that is not an entry has no legal effect. It does not hold for *the record of acts in the world*, which must be compared against an independent record. One promotion criterion does this for the operator's own acts (§4.5), and the comparison has already failed a window (§6).

### 3.2 Where the regress stops

Each regress of justification ends in one of seven places, and only one of them is an authority [Freeman 2026, ch. 12]. The checker ends in *size and diversity*: a kernel one person can read, and a second author who agrees with it. The constants end in *theorems or elections*, the adviser in *scoring*, value in *the world*, randomness in *a named assumption* on the record, and the institution in *a book that can go bankrupt*. The operator is the one authority, as *owner of the utility*; his acts are unscored but priced, and confined to the irreversible.

One level higher would be a proof of the institution's soundness. Its checker can be verified from outside against the specification, but whether the institution serves its owner is an empirical question, and it is put to the book. One level lower — trusting a judge, a vendor, a number or an adviser — is where earlier attempts stopped.

### 3.3 Minimality, sufficiency, optimality

The law is *minimal* only in a weak sense. It holds only mechanisms that meet a row of Table 1, and only two kinds of constant: those that carry a proof (1/α, ln K, the stake rules), and those stated before the window they govern. Every model, prior, base rate finer than a type, and threshold is an *entrant* that can lose an election. A mechanism without a row is an entrant installed as law [Freeman 2026, §A.17]. We do not prove the rows independent, or that no smaller set of mechanisms would meet them.

We claim no *sufficiency*: it is left to falsifiers stated in advance (§6). Nor do we claim *optimality*. The institution states no loss function for the operator, and log-loss is a scoring rule, not his utility. What it does instead is test at a level and bound regret, and both hold without knowing his utility.

---

## 4 The construction and its guarantees

Propositions 1, 2 and 6 hold by construction. Their value lies in stating exactly what is guaranteed and what is not, in a form that can be checked against the code. Propositions 3–5 carry the statistical content. None is mathematically new: the block mixture is the Bayes mixture of online learning, and Proposition 5 is the intersection–union principle. What we claim is their application to an institution, and the exact statement of what each does and does not guarantee.

**Machine-checked core.** Propositions 1(b), 2(a), 3(b), 4(b) and 5 are checked in Lean 4 [de Moura & Ullrich 2021] against Mathlib [The mathlib Community 2020]. So are 3(a) and 4(a), for every finite horizon. There the wealth is shown to be a non-negative supermartingale under the null, and Ville's inequality is derived from Mathlib's optional stopping theorem. The proofs use only Lean's standard axioms, and they are ancillary files of this paper. The bridges from the paper's definitions to the Lean statements are informal: the product construction, the clipping and the stake rules. Not formalised are:
- the grid clause of 2(a);
- the bounds that the stake rules keep;
- the unbounded horizon, which follows by continuity of measure;
- Propositions 1(a), 1(c), 2(b) and 6, which hold by construction of the code.

### 4.1 The record, and law as a fold

A *log* is a sequence of entries $e_0, e_1, \dots$. Each entry is a canonical JSON line with seven fields: `seq`, `parent` (the SHA-256 of the previous line), `ts`, `type`, `proposer`, `body` and `sig` (an Ed25519 signature over the rest) [SPEC §§1–6].

The state $S_i$ is a function of $e_0, \dots, e_{i-1}$ alone. It holds:
- the declared keys, each with a principal and a set of powers, which are entry types;
- the charter in force, taken from the latest `amend` whose activation height is at most $i$;
- the trusted-base digest in force, taken from the latest `push`;
- the forecasts recorded and resolved [SPEC §7].

The validity predicate $V(S_i, e_i)$ accepts the entry, or refuses it for one of fourteen reasons [SPEC §§8–9]. A log is valid if $V$ accepts each entry in turn; the first refusal is the verdict.

This differs from an event-sourced runtime [Nakajima 2026] in one respect. Such a runtime projects state from a log. Here the *admissibility of the next entry* is itself a function of the law folded from the entries before it. The law therefore changes only by entries, and binds only forward.

**Proposition 1 (prospectivity).** Let $L$ be a valid log whose last line hashes to $h$. Call a log *linked* if each entry's `parent` is the SHA-256 of the line before it; the kernel refuses any log that is not.

(a) For any extension $L' = L \Vert M$, every entry of $L$ receives the same verdict in $L'$ as in $L$.

(b) Any linked log $L^* \neq L$ whose entries are numbered by position from 0, as the kernel requires, and whose last line also hashes to $h$, yields a SHA-256 collision. So a computationally bounded adversary produces one with at most its advantage in finding collisions.

(c) In the state the kernel folds, the charter in force at position $i$ is the one named by the latest `amend` with activation height $\le i$. So an amendment entered at seq $a$ with activation height $k > a$ is not in force before $k$.

*Proof.*
- (a) $V(S_i, e_i)$ depends only on $e_0, \dots, e_i$.
- (b) Compare $L$ and $L^*$ from the last line backwards. If two lines with equal hashes differ, they are a collision. If they are equal, their `parent` fields are equal, so the lines before them hash alike, and the comparison continues. Since $L^* \neq L$, a difference is found before both logs are exhausted. If one log is longer, the comparison reaches the other's genesis line paired with a line of positive `seq`; the two differ and hash alike, because the next lines' `parent` fields agree.
- (c) The charter in force at $i$ comes from the latest `amend` with activation height $\le i$, and the kernel refuses any activation height not above the entry's own `seq` [SPEC §7]. $\square$

Proposition 1 is Fuller's prospectivity, proved of a data structure. In the implementation the charter is named by its digest, and one effect of an amendment is immediate: no push is lawful between $a$ and $k$ [SPEC §10, item 12]. The kernel never reads a clock: order comes from the chain [Lamport 1978; Schneider 1990], and `ts` is a field that may not decrease.

Authority is a capability [Dennis & Van Horn 1966; Miller 2006]. A party without a key holding the power `merge` cannot merge, and there is nothing to argue with. In the implementation, builders' keys hold `proposal`, `spec_conflict`, `forecast` and `resolution` [seq 34]; the merging process holds `merge` alone [seq 201]; and only the operator's genesis key holds `key`, `push`, `amend` and `decision` [seqs 0, 1, 33]. A `key` entry that would leave no key able to declare keys is refused, because that loss is irreversible [CHARTER A2.5].

### 4.2 Claims as wagers

Questions of validity are settled by $V$. Questions of merit are forecasts, and the world settles them [CHARTER §3]. A `forecast` carries a claim, a probability $p \in \{1, \dots, 999\}/1000$ and a date by which it resolves. A `resolution` names the forecast, an outcome $y \in \{0,1\}$ and its evidence.

**Proposition 2 (propriety; no self-judgement).**

(a) For belief $\pi \in (0,1)$, the expected log score $g(p) = \pi\ln p + (1-\pi)\ln(1-p)$ is strictly concave with its unique maximum at $p = \pi$. On the per-mille grid a maximum lies at a grid point adjacent to $\pi$, or at the nearer end of the grid if $\pi$ lies outside $[0.001, 0.999]$; two grid points can tie.

(b) Every resolution proposed by the principal who proposed its forecast is refused. The test is by principal, not by key, so one party's two keys cannot launder a judgement [SPEC §7].

*Proof.* (a) $g'' < 0$ and $g'(\pi) = 0$, and a concave function restricted to a grid is maximised next to its continuous maximiser. (b) This is the kernel's rule `self_judged` [SPEC §8, step 8a]. $\square$

Part (b) is *nemo iudex in causa sua* [Coke 1610], enforced by the kernel. It does not stop a party from acting on the world to move an outcome, which is the performative case [Perdomo et al. 2020]. Hence the requirement in Table 1 that scored outcomes come from processes no scored party operates. Nor does it stop two principals from colluding, or one actor from holding two principals; the operator's declarations of keys must prevent that.

Part (a) concerns the expected score. A party rewarded by a non-linear function of its score, such as its weight in the mixture or a promotion, may gain by another report. We do not claim truthful reporting is optimal for those rewards.

The logarithmic score is chosen among proper scores for a second reason. Under it, the Bayes mixture of forecasters is itself a forecaster, and its regret against the best of $K$ is at most $\ln K$ with nothing to tune [Freeman 2026, §A.5].

A forecast belongs to a procedure, not to a mind. A fixed template, model and prompt has a log-loss on a stream whether or not it believes anything [Freeman 2026, §A.20]. So the adviser who drafted the law, and the operator himself, forecast on the same ledger and are scored in the same way.

### 4.3 Promotion by betting

A *layer* is a set of mechanisms, together with the powers they confer. It is built under a *window*: a set of criteria committed before the window opens [CHARTER §6, A5]. A window is a maximum, not a term. It ends at its stated end, or at a `promote` entry, or — as failed — at a veto [CHARTER A5.1, A6.1]. A `promote` is the operator's act. Since the push at seq 7281, the judge refuses any `promote` that the evaluator in force does not find lawful [SPEC §10, item 15].

The hypotheses concern the *institution*, not a candidate. The statistics are computed over the live record of every party's acts and claims during the window. Promotion grants powers to the next layer; it does not adopt one edit over an incumbent.

**Value.** Let resolved events be grouped into finite, non-empty *blocks* $B_1, B_2, \dots$, each block's membership fixed before any of its outcomes is realised, under assumption (A): every outcome of the blocks before $B_m$ is realised before the forecasts of $B_m$ close. A sitting at which several events are forecast together is one block. Let $\mathcal G_{m-1}$ be the information recorded before $B_m$'s forecasts close. By (A) it contains the outcomes, scores and stakes of every earlier block, and none of $B_m$'s outcomes. Where horizons overlap, so that (A) fails for consecutive sittings, the sittings are split into lag classes within which it holds, and each class is a process of its own [Henzi & Ziegel 2022]. If the classes are formed from the data, class $\ell$, numbered in order of creation, needs a threshold fixed in advance, such as $\ell(\ell+1)/\alpha$; since $\sum_\ell \alpha/(\ell(\ell+1)) = \alpha$, the chance that some class crosses its threshold is at most $\alpha$. If some events of a block do not resolve, $\bar D_m$ is computed on those that do, and the null is stated for that statistic: no advantage on the events that resolve, given $\mathcal G_{m-1}$. Independence of resolution from outcomes would not carry a null on the full block over to the resolved subset.

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

**Proposition 3 (value).** Let $H_0^{\mathrm{val}}$ be: $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 0$ for every $m$. This holds whenever, for each block, the aggregate's joint forecast does not beat the base rate's in expected log score, given what was known when the forecasts closed. Nothing is assumed about dependence within a block.

(a) Under $H_0^{\mathrm{val}}$, $W$ is a non-negative supermartingale with $W_0 = 1$, so $\Pr(\sup_t W_t \ge 1/\alpha) \le \alpha$.

(b) For every sequence of outcomes and every $t$,
$$\ln 999\sum_{m\le t}|B_m|\,\bar D_m \;\ge\; \max_k \sum_{m \le t}\sum_{i\in B_m}\ln\frac{p_{k,i}(Y_i)}{b_i(Y_i)} - \ln K \;\ge\; -\ln K.$$

*Proof.*
- (a) $\lambda_m \in [0,1)$ and $|\bar D_m| \le 1$ give $1 + \lambda_m \bar D_m > 0$. Predictability gives $\mathbb E[1 + \lambda_m \bar D_m \mid \mathcal G_{m-1}] = 1 + \lambda_m \mathbb E[\bar D_m \mid \mathcal G_{m-1}] \le 1$. Then apply Ville's inequality [Ville 1939].
- (b) Because the weights are Bayes posteriors, the product telescopes: $\prod_{m\le t} Q_m(Y_{B_m}) = K^{-1}\sum_k \prod_{m\le t}\prod_{i\in B_m} p_{k,i}(Y_i) \ge K^{-1}\max_k \prod_{m\le t}\prod_{i\in B_m} p_{k,i}(Y_i)$ [Cesa-Bianchi & Lugosi 2006, §9]. Take logarithms and subtract $\sum \ln b_i(Y_i)$. The second inequality holds because the base-rate forecaster is a member. $\square$

The null is the weak one used for sequential comparison of forecasters [Choe & Ramdas 2024]. By part (b), the aggregate's cumulative log loss is never more than $\ln K$ above the base rate's, whatever the outcomes. Part (b) bounds the size-weighted sum $\sum_m |B_m|\bar D_m$, that is, the aggregate's log loss; the wealth bets on the unweighted block averages, so (b) is not a bound on the wealth. Rejecting $H_0^{\mathrm{val}}$ shows that, at some block, the aggregate had a conditional advantage over the base rate. It does not show a persistent advantage, nor skill beyond what a finer base rate would capture (§8).

*Remark (one bet per sitting).* Assumption (A) and block betting make the null mean "no advantage at the time of forecasting". Simultaneous resolution is harmless in itself. The fault is conditioning a later bet on outcomes that the forecast-time null excludes, which a per-event bet in resolution order does whenever outcomes resolve together; the process then need not be a supermartingale under the natural null. Freezing the stakes within a sitting does not cure this, since a product of correlated factors need not be a supermartingale either; hence one factor per block. If outcomes within a sitting were independent given $\mathcal G_{m-1}$, and the null held for each event, one bet per event with stakes fixed at the cutoff would also be valid, and would compound faster. The block form gives up that power so as not to need the assumption. It has a cost of its own. A mixture of product forecasts can represent dependence among a sitting's outcomes that the base rate's product cannot, and the joint score credits that as advantage. That is not the same as forecasting the events better one by one. The joint forecast matters too. Built from the marginals $q_i$, part (b) would fail: when members disagree within a block, the product of the mixture's marginals can lose more than $\ln K$ to the best member.

*Example.* Let each sitting hold $n$ events that share one fair outcome, let the base rate be $1/2$, and take $\alpha = 0.05$. Let the aggregate forecast $0.95$ or $0.05$ for the whole sitting, by a fair coin independent of the outcome. Its forecast is a product, so $\mathbb E[\bar D_m \mid \mathcal G_{m-1}] \approx -0.12$ for the joint score and for each event alike. The block process never reached $1/\alpha$ in 4,000 runs of 300 sittings. Betting per event in resolution order, the stakes on later events are raised by earlier events with the same outcome. That process reached $1/\alpha$ in 13% of runs at $n = 20$, and in 50% of 2,000 runs of 200 sittings at $n = 50$. With independent outcomes it never crossed. This is a simulation, not a proof; for the block form the proof is Proposition 3(a). The script is an ancillary file.

The reference implementation updates both its stake and its mixture weights after every event in resolution order [`judge/value.py`, lines 113–135]. Its base rate also counts every earlier resolution of the type, including those of the same batch [`judge/entries.py`, `resolution_rates`]. And its streams do resolve in batches: fourteen resolutions in one minute of 2 November, for instance [seqs 550–563]. Its reported value wealth therefore has no guaranteed level. §6 recomputes it in block form.

**Liveness.** The clerk derives obligations ("writs") from the state and the clock, each with a deadline. A writ escalates when its deadline passes: a level-triggered reconciliation loop, not an event handler [Burns et al. 2016; CHARTER §2, maxim 3]. An *item* is an act that discharges a batch of writs. Its outcome is $Y_j = 1$ if the batch landed on time untainted by a repair from the operator, and $0$ otherwise. A null rate $p_0 \in (0,1)$ is committed before the first window, from the predecessor's record and never from the window it judges [CHARTER A4.2].

Let $\hat q_j = (s_j+1)/(n_j+2)$, where $s_j$ counts successes among the $n_j$ items resolved before item $j$, since the layer's first window. Items are indexed in the order in which their outcomes are realised, and $\mathcal F_{j-1}$ is the record before $Y_j$ is realised. If several items are realised together, they count as one: the process takes the single factor $1 + \lambda_j(\bar Y_j - p_0)$ on their mean outcome, with the stake computed from items realised earlier, and the null and proof below apply with $\bar Y_j$ for $Y_j$. The reference implementation does not yet do this. It scores simultaneous items one by one [`judge/status.py`, `score_items`], and about 190 of its 641 items so far share a timestamp with another [log at seq 7809]. Let $\lambda_j = \max\big(0, (\hat q_j - p_0)/(p_0(1-p_0))\big)$, and $M_t = \prod_{j \le t}(1 + \lambda_j(Y_j - p_0))$ [CHARTER A4.3].

**Proposition 4 (liveness, with wealth carried across windows).** Let $H_0^{\mathrm{live}}$ be: $\mathbb E[Y_j \mid \mathcal F_{j-1}] \le p_0$ for every item from the layer's first window on.

(a) Under $H_0^{\mathrm{live}}$, $M$ is a non-negative supermartingale with $M_0 = 1$. So the probability that $M$ ever reaches $1/\alpha$, in any window or across all of them, is at most $\alpha$.

(b) If each of $k$ windows instead restarted at 1, each a test at level $\alpha$, the probability of a false crossing in some window could only be bounded by $1 - (1-\alpha)^k$ for independent windows, or by $k\alpha$ in general. The first bound is attained when each window's test is exact.

*Proof.*
- (a) $\hat q_j < 1$ gives $\lambda_j < 1/p_0$, so $1 - \lambda_j p_0 > 0$. Since $\lambda_j \ge 0$, $\mathbb E[1 + \lambda_j(Y_j - p_0) \mid \mathcal F_{j-1}] \le 1$. A failed window is followed by one that continues the same product [CHARTER A4.1], so every window's end is a stopping time of one supermartingale, and Ville's inequality applies once.
- (b) If window $j$ crosses falsely with probability $r_j \le \alpha$, independence gives $1 - \prod_j (1 - r_j) \le 1 - (1-\alpha)^k$, and the union bound gives $k\alpha$. $\square$

A retry therefore costs no α, provided the process, the null and the protocol continue unchanged. In the reference implementation, the value layer has failed two windows and its third is stated in advance. Had each window restarted at 1, the chance of some false crossing could have reached $1 - 0.95^3 \approx 14\%$ at $\alpha = 0.05$. Carried, it stays at 5%. Per-edit gates, by contrast, spend an error budget on each decision (§7), and gates with summable risk schedules admit only a finite total true-positive rate [Scrivens 2026].

What Proposition 4 controls is the probability of *ever* promoting while the institution never beats $p_0$. It does not test the current window alone. Earlier wealth can carry a later window. While $\hat q_j > p_0$, each new failure multiplies the wealth by $(1-\hat q_j)/(1-p_0) < 1$, which is small when $\hat q_j$ is high. When $\hat q_j \le p_0$ the stake is zero and the wealth does not move (§8).

**Proposition 5 (conjunctive promotion).** Suppose promotion requires $W_t \ge 1/\alpha$ and $M_t \ge 1/\alpha$ at the same prefix, together with conditions that are checked exactly (pins killed, checkers agreeing, no veto). Then under any joint law in which $H_0^{\mathrm{val}}$ *or* $H_0^{\mathrm{live}}$ holds, the probability that promotion ever occurs is at most $\alpha$.

*Proof.* The promotion event lies inside $\{\sup W \ge 1/\alpha\}$ and inside $\{\sup M \ge 1/\alpha\}$. Bound it by whichever of these the true null controls. This is the intersection–union principle [Berger 1982]. $\square$

No combination of the two processes, by averaging or otherwise, is needed for validity against the union of the nulls. That union is the null that matters for promotion, since a layer should be refused if *either* value or liveness is lacking. The guarantee inherits the hypotheses of both component processes, and holds per layer. Over a sequence of layers, each tested at its own level $\alpha$, it gives no familywise bound.

### 4.4 Who may change the judge

The trusted base consists of the two kernels, the judge, the CI workflows and the specification. It changes only by the operator's `push` entry naming its digest. Every proposal whose trusted-base digest differs from trunk's is refused, and no push is lawful between an amendment and its activation height [SPEC §10, items 1, 11, 12]. The promotion evaluator is part of the trusted base, and every `promote` is judged by the evaluator in force at its `seq` [SPEC §10, item 15].

How may the evaluator itself change? Let $E$ be the evaluator in force, and let $R$ be the commits of trunk's first-parent history up to a commit $T$, each with its log and the other inputs the table records for it. Before a replacement $E'$ is built:
1. The operator enters a grant naming a table of $E$'s outputs on $R$.
2. The grant marks, for each row $r \in R$, the lines $\mu(r)$ expected to change, together with what those lines will then say.

The specification admits the push installing $E'$ only if, on every row, $E'$'s output equals $E$'s outside $\mu(r)$ and agrees with the grant on $\mu(r)$ [SPEC §10, "The promotion evaluator"]. In the implementation this is enforced only in part. The judge checks that the installing push carries a specification named in such a grant [`judge/judge.py`, `installing_push`]. CI replays three of the table's 706 rows [`tests/promotion_replay_spot.py`]. The full replay is a reviewer's session, not a gate [`transcripts/sessions/c2a-3-replay.md`; grant seq 6851; push seq 7281].

**Proposition 6 (replay-bound change).**

(a) If $E'$ meets the admission condition then, on every row of $R$ read with the inputs the table records, every unmarked criterion line and every unmarked promotion verdict is the same under $E'$ as under $E$.

(b) No `promote` already on the record is re-judged.

(c) Nothing is certified about $E'$ on any other input: after $T$, or on a recorded prefix read with different evidence, such as another table of the operator's acts.

*Proof.*
- (a) By the admission condition.
- (b) Each `promote` is judged by the evaluator in force at its `seq` [SPEC §10, item 15]; this needs no replay.
- (c) Agreement on finitely many inputs fixes nothing elsewhere. $\square$

Part (c) is the lock's residue: the future behaviour of $E'$ is governed like all code here, by review, by mutants that must be killed, and by the next replay. What the rule removes is the silent re-judging of the past, by which a new judge might find that a failed window had passed after all. Marked outputs may still change, but only as the grant says and before the new evaluator is built, so Proposition 6 is not a conservative extension in the logician's sense. The Red Queen Gödel Machine takes the other path, by intent. It gates each evaluator replacement on an evaluator-independent anchor, then discards the utility records that depended on the replaced evaluator [Iacob et al. 2026, §3.2]. That suits an optimiser. For a court, past verdicts are history.

The kernel exists twice, in Python and in Go. The second was written from the specification alone by a different model family, and CI fails on any disagreement between the two [CHARTER §5; SPEC §9a]. By §3.1, this guarantees only that no entry is admitted on which the two disagree.

### 4.5 The principal, priced

When the operator forecasts, he is scored like anyone else (§4.2). His *acts* are the one thing not scored: his wishes are preferences, not predictions, and the institution's utility is his by definition [Hadfield-Menell et al. 2016]. His acts are instead confined and priced:
- **Confined.** His reserved acts are exactly the irreversible ones — keys, pushes, amendments, promotion and veto — where waiting has option value [Arrow & Fisher 1974; Henry 1974].
- **Priced by entry.** Every other act of his is an entry, typed as a *decision* or a *repair* by its entry type and key, under a rule fixed before any window [CHARTER §7]. The typing is fixed in advance and cannot be revised, so repairs cannot be made to fall by relabelling.
- **Priced by liveness.** A repair taints every writ open at its entry, and a tainted item has $Y = 0$.

Acts the operator takes *off* the record are collected from the hosting platform's own event history, which is an independent record. A window fails if a repair is found there [BRIEF-C2a, criterion 7].

Human oversight load has been measured before, for instance as interventions per session [McCain et al. 2026] or as the share of consequential actions taken without approval [Kolluri et al. 2026]. In interactive imitation learning, an expert's interventions drive the learner's training [Ross, Gordon & Bagnell 2011], and a learned safety policy decides when to hand control back to the expert [Zhang & Cho 2017]. To our knowledge, this is the first such measure that is tested sequentially and made a condition of granting powers. It measures timely, repair-free completion, not the worth of the work (§8).

---

## 5 Law before the agent

### 5.1 The order follows from the dependencies

In this design, each layer presupposes the one before it:
- A score needs a record, and a record needs the three secondary rules, so the record (C0) comes first.
- An overdue forecast is the first obligation this record holds, so the ledger (C1a) precedes the clerk (C1b) [CHARTER A3.1].
- An election of proposers needs scores, and scores need resolutions that land on time, so the election (C2) comes next.
- The agent (C3) comes last, because everything it may not touch must already exist.

This is Gall's rule [Gall 1977] and Madison's order: "you must first enable the government to control the governed; and in the next place oblige it to control itself" [Madison 1788]. Each layer is promoted before the next layer's window opens [CHARTER §8]. This is an argument from the design's own dependencies, not a universal necessity. Governance could be developed alongside an agent held in containment; §5.2 argues against that course, but we do not claim it impossible.

### 5.2 The builders are the first subjects

Before the agent exists, the only proposers are those building the institution: model sessions acting as builders, reviewers and adviser, and the operator. The charter binds them by the means it will use on the agent: "Whatever counsel and builders are forbidden is what the agent of C3 is forbidden, by the same judge, keys and amendment path; nothing is imposed on the agent that was not first imposed on us" [CHARTER A2.10].

We argue for this on three grounds:
1. **Rules of conduct enter only from cases** [CHARTER A2.1; Hart 1961; Hayek 1973]. A rule that binds the agent but has never refused a builder's act enters the agent's era as a guess.
2. **The nulls must predate the windows they judge** (Proposition 4). The builders' record, with the predecessor's, is the only record that does.
3. **The builders run the agent's policy class.** They are frontier model sessions, so a law that is usable by its builders, and that holds against their accidents, has been exercised by the very policy class the agent will use.

What this does *not* establish is resistance to an adversary, since builders are not adversaries. That is a separate obligation. The charter requires a simulator of named attacks — self-judging, retroactive, forged, forking, stalling and others — to run clean before any model touches a layer [CHARTER §6], and the agent's layer will need a red team in the sense of AI control [Greenblatt et al. 2024].

Self-improving systems usually build the agent first and wrap it in governance that is trusted rather than tested [Zhang et al. 2025, 2026]. Even designs with a frozen evaluator build the frozen zone outside the law it enforces [Neal 2026]. The nearest precedents are partial. SEA recommends deploying its statistical gate first, before its other loop controllers [Sengupta 2026, §4.4]. Nomic's players are subject to the rules they change [Suber 1990]. And software that is built with its own tools has long made its builders its first users. We know of no earlier design that subjects the model sessions building an AI's governing law to that law before the AI exists. In the implementation they have been subject to it since their keys were declared [seqs 6–8, 19 October 2026]. Builder and reviewer keys have since signed 6,621 of the log's 7,810 entries [log at seq 7809].

### 5.3 What is bootstrapped is authority

What rises from layer to layer is authority, not intelligence [Freeman 2026, §11.10]. A power exists only because it was earned at the layer below, by scored record, under the same three secondary rules. For example, the merging process received `merge` once the record showed accepted proposals waiting on a person [seq 51; Freeman 2026, §11.10].

The institution is *self-governing* in this sense. It changes its law only by its own procedure, and it grants powers only by its own record. One party's acts stand outside the scoring: those of the owner of the utility. *Self-improving* is what this buys at the last layer.

The method is self-similar. The institution that will judge the agent's changes was itself built from proposals that its own kernel judged, its own ledger scored and its own tests promoted.

---

## 6 Reference implementation and status

The design runs in public as `renavondata/jack`. The charter's SHA-256 is in the signed genesis entry [seq 0, 2026-10-14T05:41:39Z]. The kernel is 450 lines of standard-library Python [`tools/count_kernel.py`]. At C0's exit, a second kernel in Go agreed with it on 100,000 seeded logs and 658,885 prefixes [REPORT §8.1].

**Table 2. Layers and windows, from the log.**

| Layer | Entry | Outcome |
|---|---|---|
| C0, the record | genesis, seq 0 (14 Oct) | promoted by a signed tag before windows existed; not pre-registered |
| C1a, the ledger | `promote`, seq 188 (31 Oct) | every pre-stated criterion met |
| C1b, the clerk | `promote`, seq 337 (1 Nov) | $M = 214358881/8398080 \approx 25.5$ over nine items, $p_0 = 6/11$ |
| C2a, value | opened at seq 367 (1 Nov) | value wealth (per-event form) crossed early; **failed** on nine repairs off the record; `fix` at seq 5563 |
| C2a′ | opened at seq 5564 (17 Nov) | **failed** on a fault in the evaluator's check of an unchanged scope; ended by veto at seq 7180 |
| C2a, third window | brief read, grant at seq 7615 (24 Nov) | opens at the first push after 2026-11-30T00:00Z |
| C2b, C2c, C3 | — | not opened; no agent exists |

Each failure illustrates the construction. In C2a's first window the value test crossed early, but comparison with the platform's independent record of the operator's acts found nine repairs off the record, so under the conjunctive rule (Proposition 5) the window could not be promoted. The second failure, C2a′, was a fault in the judge, not in the judged. The evaluator was then moved into the trusted base by a push whose changed lines had been marked in advance [grant seq 6851; push seq 7281], and the failed window stayed failed.

**The value evidence, recomputed.** We recomputed the implementation's value test on its own record, retrospectively, under the following protocol [`block_on_log.py`, an ancillary file]. The choices were made after the record existed, so this is an audit of the record, not a prospectively registered decision.
- **Observation.** The record runs from C2a's opening (seq 367) to seq 7809, observed at its last entry, 2026-11-25T11:05Z.
- **Events.** They are the value events the implementation's own code selects, without its gate on the attack simulator.
- **Sittings.** An event belongs to the sitting of its forecast cutoff only if some party forecast it before that cutoff; 19 resolved events with no such forecast are not members. A sitting is scored once every member has resolved or passed its deadline. That gives 476 sittings scored, and 4 still pending at the time of observation. Two member events expired unresolved, and the statistic uses the events that resolved (§4.3).
- **Information.** Base rates, mixture weights and stakes use only what was recorded before the sitting's cutoff. The weights pool all earlier outcomes, so Proposition 3(b)'s regret bound does not apply class by class.
- **Classes.** The sittings fall into six lag classes, with the thresholds $\ell(\ell+1)/\alpha$ of §4.3.
- **Forecasters.** Almost all the forecasts come from one party: 2,795 from reviewer sessions and 12 from builders.

The results depend on the base rate:
- **Pooled across datasets,** as in the implementation: the first two classes end at about $2.2 \times 10^4$ and $1.3 \times 10^4$, above their thresholds of 40 and 120.
- **Kept per dataset:** no class's wealth ever exceeds 1.

So the record gives evidence that the stream's forecaster beats a base rate pooled across datasets, and no evidence that it beats one kept per dataset. Failing to reject does not show that there is no further skill. But nothing on the record so far shows any. The audit's fixed table of one probability per dataset beats the pooled base rate too (§8).

The implementation's own per-event figure on the same events, about $1.5 \times 10^{60}$, is not comparable evidence. It compounds about six bets per sitting, and has no guaranteed level when outcomes within a sitting are dependent. Holding its stakes, weights and base rates to what was known before each cutoff still leaves it near $10^{60}$. One bet per sitting in a single process gives about $3.9 \times 10^{10}$, and the split into lag classes accounts for the rest. So the gap comes from how many bets are compounded, not from leaked outcomes.

The charter states in advance what would show the construction wrong [CHARTER §12]: that the kernel cannot hold the three secondary rules within readable size; that a liveness window fails against its committed baseline; that repairs fall only because acts were re-typed; or that procedure outgrows object by more than five to one in a window. That last ratio counts entries about the institution against entries about the world. In the current count it stood at 459 to 1,786 on 25 November [`judge/status.py` at seq 7809], though the ratio can be padded (§8).

---

## 7 Related work

**What is not new.** None of the component results is new, and several mechanisms precede this work: signed or hash-chained logs for agents [Ghosh 2026; Nakajima 2026; Bracale Syrnikov et al. 2026], frozen evaluators [Zhang et al. 2026], pre-registration with human ratification of promotions [Neal 2026], and anytime-valid gates on self-edits [Wu et al. 2025; Shawn 2026; Sengupta 2026; Sun et al. 2026; Gao, Qi & Cui 2026]. The precedents for each new claim are below: self-adaptive and self-amending systems for the first, interactive imitation learning and oversight metrics for the second (§4.5), and partial precedents for the third (§5.2).

**Self-improving agents.** The Gödel machine requires a proof of utility before a rewrite [Schmidhuber 2003]. Later systems validate rewrites on benchmarks instead [Yin et al. 2024; Robeyns, Szummer & Aitchison 2025; Zhang et al. 2025, 2026].

Two recent studies point the same way as this paper. A survey of safety in self-evolving agents holds that utility alone does not authorise promotion [Chen J. et al. 2026], and a census of the field finds the improvement process rarely tested [Chen, Zhu & Zheng 2026]. Here the process itself, run by an institution, is the object tested.

**Self-adaptive systems.** Autonomic computing closes a monitor–analyse–plan–execute loop over a managed system [Kephart & Chess 2003], and architecture-based self-adaptation changes a running system's architecture under an external manager [Garlan et al. 2004]. In both, the manager is fixed and trusted. Here the governing institution is itself the thing promoted, layer by layer, by test on its own record.

**Statistical gates on self-modification.** Several recent systems gate *edits of the agent* against an incumbent. SGM allocates a familywise error budget across edits [Wu et al. 2025]. PACE makes each commit an anytime-valid paired test with a per-decision guarantee [Shawn 2026]. SEA composes confidence sequences and e-processes into per-controller gates, recorded on a certificate ledger around a frozen base model; it leaves the guarantees of that composition under an endogenous proposer as open conjectures [Sengupta 2026]. REUSE controls false promotions over a whole run when benchmarks are reused [Sun et al. 2026], and TRUST controls a false-evolution rate [Gao, Qi & Cui 2026]. Two theoretical results bound what such gates can do. Cai et al. [2026] show that the validation needed for reliable adoption diverges as the incumbent nears its ceiling, and Scrivens [2026] limits what summable-risk gates can admit. None of these gates tests liveness or the principal's burden, carries wealth across failed attempts, or promotes the institution that does the gating.

**Evaluators that change.** Hyperagents fix the evaluator for now [Zhang et al. 2026]. The Red Queen Gödel Machine co-evolves its evaluator and re-estimates past utilities (§4.4) [Iacob et al. 2026]. We allow change only by replay of past verdicts, with every change to them marked in advance (Proposition 6).

**Frozen zones, audited loops, signed logs.** The closest precedent for pre-registration with a human gate is SFA-Bench's AutoLab [Neal 2026]. It combines a hash-attested frozen zone, a declaration sealed before each patch, a hash-chained meta-ledger and promotion by human ratification token.

Other systems log, sign or govern agents' acts. Regimes derives the agent's state from an append-only event log in which promotions are events [Nakajima 2026]. ASG-SI proposes replayable evidence bundles for promoting skills [Huang & Huang 2025]. Tracekit signs tool calls in a witnessed Merkle log [Ghosh 2026]. AgentBound enforces owner-signed behavioural constitutions at runtime [Kaul, Lan & Gupta 2026]. Institutional AI governs collusion between agents through a public governance graph and a keyed governance log [Bracale Syrnikov et al. 2026]. Governable Individuals widen an agent's authority only by signed lifecycle transitions [Qin et al. 2026]. These works anticipate the record. None makes it the source of law, with prospective amendment. None scores the parties' claims, and none promotes the institution by sequential test.

**Self-amending systems.** Rules that change under themselves have a longer history. Suber's Nomic and his study of self-amendment show how a rule system can change its own rules of change [Suber 1990], and the Tezos ledger amends its own protocol by on-chain vote [Goodman 2014]. Our amendment path follows the same pattern: one act makes a rule mutable, a second changes it, and the change takes effect only at a stated height [CHARTER A2.7]. The difference is that change is priced and scored, and that each layer's powers are granted only on sequential evidence about the institution's own record.

**Control, law and agency.** AI control separates a trusted monitor from an untrusted policy [Greenblatt et al. 2024]. The lock applies that separation to the evaluation infrastructure, by keys rather than instructions. Kolt [2026a, 2026b] frames the legal problem. Constitutions used in training [Bai et al. 2022] shape a model's outputs; the constitution here is enforced by a checker the model cannot reach.

**Testing by betting.** The tests follow the prequential principle [Dawid 1984] and game-theoretic testing [Shafer & Vovk 2019; Ramdas et al. 2023]. They are closest to the sequential comparison of forecasters [Henzi & Ziegel 2022; Choe & Ramdas 2024].

---

## 8 Limitations and open questions

**The choice of null.** The value null pits the aggregate against a base rate pooled by event type, which is a weak baseline. An audit on the record constructs a fixed table, one probability per dataset, that would have crossed the value threshold at the 53rd event [`transcripts/AUDIT-criteria-20261117.md`]. Against a base rate kept per dataset, the record shows no evidence of an advantage (§6). The theory's remedy is a stronger incumbent, entered as an entrant and met by the same bounded-difference bet, together with Murphy's decomposition so that calibration without resolution does not pass [Choe & Ramdas 2024; Murphy 1973]. Which incumbent to use is open.

**Criteria that a system without skill can pass.** The same audit classes 9 of the 28 window criteria it examined as passable without skill. Liveness is one of them: a forecast resolved on time counts as a success whatever its content. The ratio of procedure to object is another: it can be met by padding the record with unanswered forecasts [`transcripts/AUDIT-criteria-20261117.md`]. Liveness as defined here measures timely, repair-free completion, not the worth of what is completed. Measuring the worth of the work is open.

**Validity against recency.** Carrying wealth keeps the level over the institution's life but lets old evidence carry a new window. A fresh process per window at a split α, or a change-detecting e-process, would trade validity for recency. The right trade for promotion is open.

**Correlated readers and checkers.** The weight of agreement between the two kernels, or between cold reads by different model families, is bounded by their shared error (§3.1). That error should be estimated against executable or human references [Kim et al. 2025; Chen, Zhu & Zheng 2026]. In the implementation, cross-family reads gate law-level texts by procedure, not yet by code.

**Who operates the world.** One of the two scored streams, the freshness of datasets, resolves from pages on the operator's own data marketplace, and the operator may forecast [Freeman 2026, §A.22]. That is the performative case Table 1 warns against.

**Completeness of the record of acts.** The operator's acts are collected from one platform. The monitor the charter requires — one that the operator does not run [CHARTER A2.8] — is not yet built.

**Sufficiency of three secondary rules.** No primary rule has yet been needed: the log holds no `rule` entry [CHARTER A2.1; log at seq 7809]. That the three suffice until the agent arrives is a conjecture under test.

**Mixture or market.** The election is a Bayes mixture over a roster fixed for each layer. A market of traders, in the manner of logical induction [Garrabrant et al. 2016], would let the roster grow, but needs its own argument for anytime validity.

**No controlled comparison.** The evidence is one case history. The experiment that would test the design is a controlled comparison against simpler governance, such as a frozen evaluator with per-edit gates, under repeated runs and deliberate attacks. We have not run it.

**One principal; a short record.** The construction serves one owner of the utility. Kolt's principle of inclusivity [2026a] asks for more. The evidence so far covers one operator, two streams and six weeks. The agent, C3, is still a forecast.

---

## 9 Conclusion

What judges a self-modifying agent must lie outside the agent's reach, and must itself be judged by something other than trust. We have argued for an institution that is built before the agent, binds its builders first, holds its law as a fold over a signed record, prices every claim as a forecast, and gains powers only by sequential tests on its own record. The guarantees are modest and exact. The first test of the construction is whether its record can show it wrong. It can: the valid test of value, run on the reference implementation's record, finds no evidence of an advantage over a base rate kept per dataset. Under this design, the value the next layer claims should be measured against that baseline.

---

## Disclosure

Model sessions from three providers' families drafted the charter, the specification and most of the code. Since 19 October 2026 they have acted under keys declared on the record. The second kernel was written by a different family from the first. This paper was drafted by a model session that holds no key, working from the repository, the book and the literature; the author read and revised it. No model is an author. The author is responsible for every claim.

## Code and data

- Repository, with the log, kernels, judge, briefs and rulings: github.com/renavondata/jack.
- Book: *A Court for Agents*, gfrm.in/book; source at github.com/gfrmin/agent-court.
- Ancillary files of this paper: `lean/`, the Lean proofs of §4 (`lake build`, with a table from propositions to theorems); `sim_filtration.py`, the simulations of §4.3; `block_on_log.py`, the recomputation of §6 with its ablations and both base rates, run in any checkout of the repository as `python3 block_on_log.py --rev e580b64`; it reads that commit by `git show` and writes nothing.
- Founding note: "The Science Was Done. The Engineering Wasn't.", gfrm.in, 1 November 2026.

---

## References

- Alpern, B. & Schneider, F. B. (1985). Defining liveness. *Information Processing Letters* 21(4):181–185. doi:10.1016/0020-0190(85)90056-0
- Anderson, J. P. (1972). *Computer Security Technology Planning Study.* ESD-TR-73-51, USAF Electronic Systems Division.
- Arrow, K. J. & Fisher, A. C. (1974). Environmental preservation, uncertainty, and irreversibility. *QJE* 88(2):312–319. doi:10.2307/1883074
- Ashby, W. R. (1956). *An Introduction to Cybernetics.* Chapman & Hall.
- Bahadur, R. R. & Savage, L. J. (1956). The nonexistence of certain statistical procedures in nonparametric problems. *Ann. Math. Statist.* 27(4):1115–1122. doi:10.1214/aoms/1177728077
- Bai, Y., Kadavath, S., Kundu, S., Askell, A. et al. (2022). Constitutional AI: Harmlessness from AI feedback. arXiv:2212.08073.
- Berger, R. L. (1982). Multiparameter hypothesis testing and acceptance sampling. *Technometrics* 24(4):295–300. doi:10.2307/1267823
- Bracale Syrnikov, M., Pierucci, F., Galisai, M., Prandi, M. et al. (2026). Institutional AI: Governing LLM collusion in multi-agent Cournot markets via public governance graphs. arXiv:2601.11369.
- Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review* 78(1):1–3.
- Burns, B., Grant, B., Oppenheimer, D., Brewer, E. & Wilkes, J. (2016). Borg, Omega, and Kubernetes. *Communications of the ACM* 59(5):50–57. doi:10.1145/2890784
- Cai, Q., Zhang, Y., Nie, J. et al. (2026). A theory of reliable self-evolution for agent harnesses. arXiv:2609.08175.
- Cesa-Bianchi, N. & Lugosi, G. (2006). *Prediction, Learning, and Games.* Cambridge University Press. doi:10.1017/CBO9780511546921
- Chen, J., Feng, Z., Ma, O. et al. (2026). Safety in self-evolving agents: A survey. arXiv:2610.00093.
- Chen, Z., Zhu, D. & Zheng, L. N. (2026). Auditing the product, not the recursion: The evaluation evidence behind recursive self-improvement claims. arXiv:2610.27610.
- Choe, Y. J. & Ramdas, A. (2024). Comparing sequential forecasters. *Operations Research* 72(4):1368–1387. doi:10.1287/opre.2021.0792
- Coke, E. (1610). Dr Bonham's Case, 8 Co. Rep. 107a.
- Conant, R. C. & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *Int. J. Systems Science* 1(2):89–97. doi:10.1080/00207727008920220
- Crawford, S. E. S. & Ostrom, E. (1995). A grammar of institutions. *American Political Science Review* 89(3):582–600. doi:10.2307/2082975
- Dawid, A. P. (1984). Present position and potential developments: Some personal views. Statistical theory: The prequential approach. *JRSS A* 147(2):278–292. doi:10.2307/2981683
- de Moura, L. & Ullrich, S. (2021). The Lean 4 theorem prover and programming language. *CADE-28*, LNCS 12699:625–635. doi:10.1007/978-3-030-79876-5_37
- Dennis, J. B. & Van Horn, E. C. (1966). Programming semantics for multiprogrammed computations. *Communications of the ACM* 9(3):143–155. doi:10.1145/365230.365252
- Dietrich, F. & Spiekermann, K. (2013). Independent opinions? On the causal foundations of belief formation and jury theorems. *Mind* 122(487):655–685. doi:10.1093/mind/fzt074
- Freeman, G. (2026). *A Court for Agents: Law, scoring and the self-modifying machine.* gfrm.in/book; source github.com/gfrmin/agent-court.
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
- Ladha, K. K. (1992). The Condorcet jury theorem, free speech, and correlated votes. *AJPS* 36(3):617–634. doi:10.2307/2111584
- Lamport, L. (1978). Time, clocks, and the ordering of events in a distributed system. *Communications of the ACM* 21(7):558–565. doi:10.1145/359545.359563
- Löb, M. H. (1955). Solution of a problem of Leon Henkin. *Journal of Symbolic Logic* 20(2):115–118. doi:10.2307/2266895
- Madison, J. (1788). *The Federalist* No. 51.
- The mathlib Community (2020). The Lean mathematical library. *CPP 2020*, 367–381. doi:10.1145/3372885.3373824
- McCain, M., Millar, T., Huang, S. et al. (2026). Measuring AI agent autonomy in practice. Anthropic, 18 February 2026. anthropic.com/research/measuring-agent-autonomy
- Miller, M. S. (2006). *Robust Composition: Towards a Unified Approach to Access Control and Concurrency Control.* PhD thesis, Johns Hopkins University.
- Murphy, A. H. (1973). A new vector partition of the probability score. *Journal of Applied Meteorology* 12(4):595–600. doi:10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2
- Nakajima, Y. (2026). Regimes: An auditable, held-out-gated improvement loop demonstrated on LongMemEval with ActiveGraph. arXiv:2606.10241.
- Neal, M. (2026). SFA-Bench v2.0.0-alpha.2: Locked campaign execution and evidence capture (with SFA-AutoLab). Software, github.com/iotaverbum-core/sfa-bench. doi:10.5281/zenodo.20766587
- Pato Nogueira, R., Pattabiraman, K., Vieira, M. & Campos, J. R. (2026). A systematic methodology for evaluating failure independence in LLM-generated code. arXiv:2607.02808.
- Perdomo, J., Zrnic, T., Mendler-Dünner, C. & Hardt, M. (2020). Performative prediction. *ICML 2020*, PMLR 119:7599–7609; arXiv:2002.06673.
- Qin, X., Luan, S., Yang, C. & Li, Z. (2026). Governable individuals: An identity layer for embodied agents that keep learning. arXiv:2607.05463.
- Ramdas, A., Grünwald, P., Vovk, V. & Shafer, G. (2023). Game-theoretic statistics and safe anytime-valid inference. *Statistical Science* 38(4):576–601. doi:10.1214/23-STS894
- Rice, H. G. (1953). Classes of recursively enumerable sets and their decision problems. *Trans. AMS* 74(2):358–366. doi:10.1090/S0002-9947-1953-0053041-6
- Robeyns, M., Szummer, M. & Aitchison, L. (2025). A self-improving coding agent. arXiv:2504.15228.
- Ron, J., Baudry, B. & Monperrus, M. (2026). N-version programming with coding agents. arXiv:2606.20158.
- Ross, S., Gordon, G. J. & Bagnell, J. A. (2011). A reduction of imitation learning and structured prediction to no-regret online learning. *AISTATS 2011*, PMLR 15:627–635; arXiv:1011.0686.
- Saltzer, J. H. & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE* 63(9):1278–1308. doi:10.1109/PROC.1975.9939
- Savage, L. J. (1971). Elicitation of personal probabilities and expectations. *JASA* 66(336):783–801. doi:10.1080/01621459.1971.10482346
- Schmidhuber, J. (2003). Gödel machines: Self-referential universal problem solvers making provably optimal self-improvements. arXiv:cs/0309048.
- Schneider, F. B. (1990). Implementing fault-tolerant services using the state machine approach: A tutorial. *ACM Computing Surveys* 22(4):299–319. doi:10.1145/98163.98167
- Scrivens, A. (2026). Information-theoretic limits of safety verification for self-improving systems. arXiv:2603.28650.
- Sengupta, B. (2026). Self-evolving agents with anytime-valid certificates. arXiv:2607.00871.
- Shafer, G. & Vovk, V. (2019). *Game-Theoretic Foundations for Probability and Finance.* Wiley. doi:10.1002/9781118548035
- Shawn, Z. (2026). PACE: Anytime-valid acceptance tests for self-evolving agents. arXiv:2606.08106.
- Skalse, J., Howe, N. H. R., Krasheninnikov, D. & Krueger, D. (2022). Defining and characterizing reward hacking. *NeurIPS 2022*; arXiv:2209.13085.
- Suber, P. (1990). *The Paradox of Self-Amendment: A Study of Law, Logic, Omnipotence, and Change.* Bern: Peter Lang. (Appendix 3: Nomic.)
- Sun, X., Zeng, Y., She, Z. & Wang, X. (2026). Which self-improvements should we trust? Reliable self-improvement when agents reuse their benchmarks. arXiv:2609.33180.
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM* 27(8):761–763. doi:10.1145/358198.358210
- Ville, J. (1939). *Étude critique de la notion de collectif.* Gauthier-Villars.
- Waismann, F. (1945). Verifiability. *Proceedings of the Aristotelian Society, Supplementary Volume* 19:101–164 (symposium). doi:10.1093/aristoteliansupp/19.1.101
- Wheeler, D. A. (2005). Countering trusting trust through diverse double-compiling. *ACSAC 2005*, 33–48. doi:10.1109/CSAC.2005.17
- Wu, X., Yin, S., Kang, Y., Zhang, X. et al. (2025). SGM: A statistical Gödel machine for risk-controlled recursive self-modification. arXiv:2510.10232.
- Yin, X., Wang, X., Pan, L., Lin, L. et al. (2024). Gödel Agent: A self-referential agent framework for recursive self-improvement. arXiv:2410.04444.
- Yudkowsky, E. & Herreshoff, M. (2013). Tiling agents for self-modifying AI, and the Löbian obstacle. Technical report, Machine Intelligence Research Institute.
- Zhang, J. & Cho, K. (2017). Query-efficient imitation learning for end-to-end simulated driving. *AAAI 2017*, 31(1). doi:10.1609/aaai.v31i1.10857
- Zhang, J., Hu, S., Lu, C., Lange, R. & Clune, J. (2025). Darwin Gödel Machine: Open-ended evolution of self-improving agents. *ICLR 2026*; arXiv:2505.22954.
- Zhang, J., Zhao, B., Yang, W., Foerster, J. et al. (2026). Hyperagents. arXiv:2603.19461.
- Zhao, Y., Li, J., Li, L., Nian, Y. et al. (2026). Auditable claims about AI agents. arXiv:2610.07459.
