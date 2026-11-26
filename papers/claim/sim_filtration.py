"""Per-event vs block betting under a true null, with outcomes shared within a block.

Each block ("sitting") has n events whose outcomes are one coin, Y ~ Bern(1/2),
realised together. The base rate is b = 1/2. The aggregate forecasts q = 1/2 + d or
1/2 - d for the whole block, by a fair coin independent of Y. So, given what was known
when the forecasts closed, the aggregate does not beat the base rate:
E[ln q(Y) - ln b(Y)] = (ln(2(1/2+d)) + ln(2(1/2-d)))/2 < 0.

Stake: the charter's plug-in rule lambda = min(max(0, S/(2+Q)), 1 - 1/(m+1)),
with S, Q the running sum and sum of squares of past differences.
  per-event: one bet per event, in resolution order (the implementation's form);
  block:     one bet per block on the block's mean joint difference (Proposition 3).
Reports the fraction of runs in which wealth ever reaches 1/alpha.

The figures in the paper's Example (section 4.3) come from:
  python3 sim_filtration.py                    # n=20, d=0.45, 300 sittings, 4000 runs
  python3 sim_filtration.py 50 0.45 200 2000   # n=50
  python3 sim_filtration.py --independent      # outcomes independent within a sitting
  python3 sim_filtration.py 50 0.45 200 2000 --independent
  python3 sim_filtration.py --roster 20 300 2000   # the full construction (below)
Seeded, so the output is reproducible.

--roster runs Proposition 3's full construction. It is NOT a true null for the joint score: the
mixture of the two constant members represents the shared outcome, which the base rate's product
cannot, so the block form's null fails there. Kept for reference; the paper does not use it.
The construction: a Bayes mixture with uniform prior over a
roster of three, the base rate (1/2) and two members that always forecast 0.95 and 0.05,
none with any skill. It compares the block form with the implementation's form
(judge/value.py at e580b64), which updates both the stake and the mixture weights
after every event, in resolution order.
"""
import math, random, sys

def stake(S, Q, m):
    return min(max(0.0, S / (2 + Q)), 1 - 1 / (m + 1))

def run(n, d, blocks, alpha, rng, shared=True):
    L = math.log(999)
    W_e = W_b = 1.0
    Se = Qe = 0.0; me = 0
    Sb = Qb = 0.0; mb = 0
    hit_e = hit_b = False
    for _ in range(blocks):
        y = rng.random() < 0.5
        q = 0.5 + d if rng.random() < 0.5 else 0.5 - d
        D = math.log((q if y else 1 - q) / 0.5) / L
        # per-event, in resolution order: the n outcomes land together
        for _ in range(n):
            if not shared:
                yi = rng.random() < 0.5
                D = math.log((q if yi else 1 - q) / 0.5) / L
            me += 1
            lam = stake(Se, Qe, me)
            W_e *= 1 + lam * D
            Se += D; Qe += D * D
            if W_e >= 1 / alpha: hit_e = True
        # block: one bet on the mean joint difference (equal to D when shared)
        if not shared:
            continue
        mb += 1
        lam = stake(Sb, Qb, mb)
        W_b *= 1 + lam * D
        Sb += D; Qb += D * D
        if W_b >= 1 / alpha: hit_b = True
    return hit_e, hit_b

def run_roster(n, blocks, alpha, rng, members=(0.5, 0.95, 0.05)):
    L = math.log(999)
    lik = lambda p, y: p if y else 1 - p
    K = len(members)
    wb = [1 / K] * K; Wb = 1.0; Sb = Qb = 0.0; mb = 0; hitb = False
    we = [1 / K] * K; We = 1.0; Se = Qe = 0.0; me = 0; hite = False
    for _ in range(blocks):
        y = rng.random() < 0.5
        prods = [lik(p, y) ** n for p in members]
        Qj = sum(w * pr for w, pr in zip(wb, prods))
        D = (math.log(Qj) - n * math.log(0.5)) / (n * L)
        mb += 1; lam = stake(Sb, Qb, mb); Wb *= 1 + lam * D; Sb += D; Qb += D * D
        if Wb >= 1 / alpha: hitb = True
        wb = [w * pr / Qj for w, pr in zip(wb, prods)]
        for _ in range(n):
            q = sum(w * p for w, p in zip(we, members))
            x = math.log(lik(q, y) / 0.5) / L
            me += 1; lam = stake(Se, Qe, me); We *= 1 + lam * x; Se += x; Qe += x * x
            if We >= 1 / alpha: hite = True
            ls = [lik(p, y) for p in members]; t = sum(w * l for w, l in zip(we, ls)); we = [w * l / t for w, l in zip(we, ls)]
    return hite, hitb

if __name__ == "__main__" and "--roster" in sys.argv:
    a = [x for x in sys.argv[1:] if x != "--roster"]
    n, blocks, runs = (int(a[0]), int(a[1]), int(a[2])) if a else (20, 300, 2000)
    rng = random.Random(20261125); he = hb = 0
    for _ in range(runs):
        e, b = run_roster(n, blocks, 0.05, rng); he += e; hb += b
    print(f"roster n={n} sittings={blocks} runs={runs}: implementation form {he/runs:.4f}, block form {hb/runs:.4f}")
    sys.exit(0)

if __name__ == "__main__":
    n, d, blocks, runs, alpha = 20, 0.45, 300, 4000, 0.05
    args = [a for a in sys.argv[1:] if a != "--independent"]
    shared = "--independent" not in sys.argv
    if args: n, d, blocks, runs = int(args[0]), float(args[1]), int(args[2]), int(args[3])
    rng = random.Random(20261125)
    he = hb = 0
    for _ in range(runs):
        e, b = run(n, d, blocks, alpha, rng, shared)
        he += e; hb += b
    drift = (math.log(2 * (0.5 + d)) + math.log(2 * (0.5 - d))) / 2 / math.log(999)
    print(f"n={n} d={d} blocks={blocks} runs={runs} alpha={alpha} shared={shared} E[D]={drift:.4f}")
    print(f"per-event crossing rate {he/runs:.4f}; block crossing rate " + (f"{hb/runs:.4f}" if shared else "n/a (no shared block)"))
