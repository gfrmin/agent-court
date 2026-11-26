"""Recompute jack's value test in block form on its own record (read only).

Usage, from any checkout of renavondata/jack:
  python3 block_on_log.py --rev e580b64 [as_of]
reads log.jsonl and the judge's code as of that commit by `git show`, and writes nothing.
Without --rev it uses the working tree.

Events (members' forecasts, outcomes) come from judge/value.py's own selection, with
no_attack_gate=True so that every event since C2a's opening counts. A sitting is the set of
value events sharing a forecast cutoff. An event belongs to a sitting only if some party
forecast it before the cutoff, so membership is fixed by what was recorded then. A sitting is
scored once it is done: every member event resolved or past its deadline, by the time of
observation (the last log entry, or as_of). Sittings not yet done are pending and not scored.
The statistic is computed on the events of the sitting that resolved, and the null is stated
for that statistic. Base rates, mixture weights and stakes use only what is recorded
before the cutoff. Sittings are split greedily into lag classes so that every earlier
sitting of a class is done before the next one's cutoff (assumption (A)); class number l,
counted from 1 in order of creation, has the fixed threshold l(l+1)/alpha, and since
sum_l alpha/(l(l+1)) = alpha, "some class crosses its threshold" has probability at most alpha.

Printed: the implementation's per-event wealth; two ablations that explain the gap (per event
with nothing leaked; one block process without classes, which is not valid when horizons
overlap); and the block-form test against two base rates, pooled by type (as the
implementation) and by dataset.
"""

import math, sys, collections, json, subprocess, importlib.abc, importlib.util

args = sys.argv[1:]
REV = None
if "--rev" in args:
    i = args.index("--rev"); REV = args[i + 1]; del args[i:i + 2]

if REV:
    def show(path):
        r = subprocess.run(["git", "show", f"{REV}:{path}"], capture_output=True)
        return r.stdout if r.returncode == 0 else None
    class GitFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
        def find_spec(self, name, path, target=None):
            top = name.split(".")[0]
            if top not in ("judge", "kernel"):
                return None
            rel = name.replace(".", "/")
            if show(rel + ".py") is not None:
                return importlib.util.spec_from_loader(name, self, origin=f"{REV}:{rel}.py")
            if show(rel + "/__init__.py") is not None or subprocess.run(["git", "cat-file", "-e", f"{REV}:{rel}"]).returncode == 0:
                spec = importlib.util.spec_from_loader(name, self, origin=f"{REV}:{rel}/", is_package=True)
                spec.submodule_search_locations = []
                return spec
            return None
        def create_module(self, spec):
            return None
        def exec_module(self, module):
            rel = module.__spec__.name.replace(".", "/")
            src = show(rel + ".py")
            if src is None:
                src = show(rel + "/__init__.py") or b""
            module.__file__ = rel + ".py"   # value.py extends sys.path from it; the finder makes that moot
            exec(compile(src, module.__spec__.origin, "exec"), module.__dict__)
    sys.meta_path.insert(0, GitFinder())
    lines = show("log.jsonl").decode().splitlines()
else:
    sys.path.insert(0, ".")
    lines = open("log.jsonl").read().splitlines()

from judge import value as val
from bisect import bisect_left

es = [json.loads(l) for l in lines if l]
as_of = args[0] if args else None
ALPHA = 0.05
LN = math.log(999)
v = val.value(es, as_of=as_of, no_attack_gate=True)
rows = v["rows"]
ts_of = {e["seq"]: e["ts"] for e in es}
roster = list(rows[0]["weights_before"].keys())
opening = v["opening"]
print(f"events {len(rows)}; roster {roster}; implementation-form E = {float(v['E_value']):.6g}")
cnt = collections.Counter(who for r in rows for who in r["forecasts"])
print("forecasts by party in these events:", dict(cnt))

def clip(p): return min(max(p, 0.001), 0.999)
def lik(p, y): return p if y else 1 - p

# every forecast's physical event, resolved or not, with its deadline
T_obs = as_of or max(e["ts"] for e in es)
fkey = {}
for e in es:
    if e["type"] == "forecast" and (as_of is None or e["ts"] <= as_of):
        ident = val.event(e)
        if ident and ident[1] > opening and e["ts"] < ident[1]:      # forecast before the cutoff
            k, c = ident
            d = fkey.setdefault(k, {"cutoff": c, "deadline": e["body"].get("resolves_by", c)})
            d["deadline"] = max(d["deadline"], e["body"].get("resolves_by", c))
resolved = {r["key"]: r for r in rows}

def group(key, by):
    typ = key[0]
    if by == "type": return typ
    return (typ, key[2]) if typ == "world.renavon" else (typ, key[-1])

# prequential Laplace base rates from every resolution, by group, as of a time
res_events = []
for r, f, _, _ in val.resolution_rates(es):
    if as_of is not None and r["ts"] > as_of: continue
    ident = val.event(f)
    res_events.append((r["ts"], ident[0] if ident else None, f["body"].get("type", "free"), r["body"]["outcome"]))
def make_base(by):
    seqs = collections.defaultdict(list)
    for ts, key, typ, y in sorted(res_events, key=lambda x: x[0]):
        g = typ if by == "type" else (group(key, by) if key else None)
        if g is not None: seqs[g].append((ts, y))
    cum = {g: ([t for t, _ in L], [0] + list(__import__("itertools").accumulate(y for _, y in L))) for g, L in seqs.items()}
    def base(key, t):
        g = group(key, by) if by != "type" else key[0]
        if g not in cum: return 0.5
        times, cs = cum[g]; n = bisect_left(times, t)
        return clip((cs[n] + 1) / (n + 2))
    return base

ev = []
for k, d in fkey.items():
    r = resolved.get(k)
    ev.append(dict(key=k, cutoff=d["cutoff"], done=ts_of[r["resolution_seq"]] if r else d["deadline"],
                   Y=r["Y"] if r else None, fc={w: float(p) for w, (s_, p) in r["forecasts"].items()} if r else {}))
sittings = collections.defaultdict(list)
for e in ev: sittings[e["cutoff"]].append(e)
pending = [c for c in sittings if max(e["done"] for e in sittings[c]) > T_obs]
for c in pending: del sittings[c]
ev = [e for c in sittings for e in sittings[c]]
order = sorted(sittings)
unresolved = sum(1 for e in ev if e["Y"] is None)
late_only = sum(1 for k in resolved if k not in fkey)

classes, last_done, assign = [], [], {}
for c in order:
    done = max(e["done"] for e in sittings[c])
    for i, d in enumerate(last_done):
        if d < c:
            assign[c] = i; last_done[i] = done; break
    else:
        assign[c] = len(classes); classes.append([]); last_done.append(done)
    classes[assign[c]].append(c)
print(f"observed to {T_obs}; sittings done {len(order)}, pending {len(pending)}; events in done sittings {len(ev)}, of which expired unresolved {unresolved}; resolved events with no forecast before the cutoff (not members) {late_only}")
print(f"lag classes {len(classes)}: {[len(x) for x in classes]}")

def stake(S, Q, m): return min(max(0.0, S / (2 + Q)), 1 - 1 / (m + 1))
def prob(e, k, b): return b if k == "base" else clip(e["fc"].get(k, b))

def run(by):
    base = make_base(by)
    done_events = sorted((e for e in ev if e["Y"] is not None), key=lambda e: e["done"])
    logw = {k: 0.0 for k in roster}; ptr = 0
    L = len(classes)
    W = [1.0] * L; S = [0.0] * L; Q = [0.0] * L; M = [0] * L; peak = [1.0] * L
    W1 = 1.0; S1 = Q1 = 0.0; M1 = 0                      # one block process, no classes
    We = 1.0; De = []                                     # per event, nothing leaked
    for c in order:
        while ptr < len(done_events) and done_events[ptr]["done"] < c:
            e = done_events[ptr]; b = base(e["key"], e["cutoff"])
            for k in roster: logw[k] += math.log(lik(prob(e, k, b), e["Y"]))
            ptr += 1
        mx = max(logw.values()); w = {k: math.exp(x - mx) for k, x in logw.items()}; z = sum(w.values()); w = {k: x / z for k, x in w.items()}
        block = [e for e in sittings[c] if e["Y"] is not None]
        if not block: continue
        lb = 0.0; prods = {k: 0.0 for k in roster}; per_event = []
        for e in block:
            b = base(e["key"], c); lb += math.log(lik(b, e["Y"]))
            q = 0.0
            for k in roster:
                p = prob(e, k, b); prods[k] += math.log(lik(p, e["Y"])); q += w[k] * p
            per_event.append(math.log(lik(q, e["Y"]) / lik(b, e["Y"])) / LN)
        D = (math.log(sum(w[k] * math.exp(prods[k]) for k in roster)) - lb) / (len(block) * LN)
        i = assign[c]; M[i] += 1
        lam = stake(S[i], Q[i], M[i]); W[i] *= 1 + lam * D; S[i] += D; Q[i] += D * D; peak[i] = max(peak[i], W[i])
        M1 += 1; lam = stake(S1, Q1, M1); W1 *= 1 + lam * D; S1 += D; Q1 += D * D
        if by == "type":
            prior = [x for (t, x) in De if t < c]
            for x in per_event:
                lam = min(max(0.0, sum(prior) / (2 + sum(y * y for y in prior))), 1 - 1 / (len(prior) + 2))
                We *= 1 + lam * x
            De += [(max(e["done"] for e in block), x) for x in per_event]
    return W, peak, W1, We

for by in ("type", "dataset"):
    W, peak, W1, We = run(by)
    thr = [(l + 1) * (l + 2) / ALPHA for l in range(len(W))]
    crossed = [l + 1 for l in range(len(W)) if peak[l] >= thr[l]]
    print(f"\nbase rate pooled by {by}:")
    if by == "type":
        print(f"  ablation, per event with nothing leaked (stakes, weights, base before the cutoff): {We:.4g}")
        print(f"  ablation, one block process without lag classes (not valid here): {W1:.4g}")
    print("  block form, final wealth by class:", [f"{x:.4g}" for x in W])
    print("  block form, running maximum by class:", [f"{x:.4g}" for x in peak])
    print("  thresholds l(l+1)/alpha:", [f"{x:g}" for x in thr])
    print(f"  classes crossing their threshold: {crossed if crossed else 'none'}")
