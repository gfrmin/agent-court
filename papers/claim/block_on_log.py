"""Recompute jack's value test in block form on its own record (read only).

Usage, from any checkout of renavondata/jack:
  python3 block_on_log.py --rev e580b64 [as_of]
reads log.jsonl and the judge's code as of that commit by `git show`, and writes nothing.
Without --rev it uses the working tree.
Rows (events, members' forecasts, outcomes) come from judge/value.py's own selection,
with no_attack_gate=True so that every event since C2a's opening counts. Then:
  implementation form: judge/value.py's own wealth (per event, resolution order);
  block form: sittings = events sharing a cutoff; base rate and mixture weights use only
  outcomes realised before the sitting's cutoff; one bet per sitting on the joint mixture
  (Proposition 3); sittings split greedily into lag classes so that assumption (A) holds
  within each class; each class is its own test supermartingale, and the union bound
  gives the threshold L/alpha for "some class crosses".
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
es = [json.loads(l) for l in lines if l]
as_of = args[0] if args else None
v = val.value(es, as_of=as_of, no_attack_gate=True)
rows = v["rows"]
ts_of = {e["seq"]: e["ts"] for e in es}
types = {}
for r, f, _, _ in val.resolution_rates(es):
    types[r["seq"]] = (f["body"].get("type", "free"), r["ts"], r["body"]["outcome"])
roster = list(rows[0]["weights_before"].keys()) if rows else []
print(f"events {len(rows)}; roster {roster}; implementation-form E = {float(v['E_value']):.6g}")

LN = math.log(999)
def clip(p): return min(max(p, 0.001), 0.999)
def lik(p, y): return p if y else 1 - p

# base rate known at time t for a type: Laplace over resolutions realised strictly before t
res_by_type = collections.defaultdict(list)
for seq, (typ, ts, y) in types.items():
    res_by_type[typ].append((ts, y))
for k in res_by_type: res_by_type[k].sort()
def base_at(typ, t):
    s = n = 0
    for ts, y in res_by_type[typ]:
        if ts >= t: break
        s += y; n += 1
    return clip((s + 1) / (n + 2))

ev = []
for r in rows:
    typ = r["key"][0]
    rts = ts_of[r["resolution_seq"]]
    ev.append(dict(key=r["key"], typ=typ, cutoff=r["cutoff"], rts=rts, Y=r["Y"],
                   fc={k: float(p) for k, (s, p) in r["forecasts"].items()}))
sittings = collections.defaultdict(list)
for e in ev: sittings[e["cutoff"]].append(e)
order = sorted(sittings)

# lag classes: a sitting joins the first class whose previous sitting's outcomes were all realised before its cutoff
classes, last_done = [], []
assign = {}
for c in order:
    done = max(e["rts"] for e in sittings[c])
    for i, d in enumerate(last_done):
        if d < c:
            assign[c] = i; last_done[i] = done; break
    else:
        assign[c] = len(classes); classes.append([]); last_done.append(done)
    classes[assign[c]].append(c)
L = len(classes)

def stake(S, Q, m): return min(max(0.0, S / (2 + Q)), 1 - 1 / (m + 1))
W = [1.0] * L; S = [0.0] * L; Q = [0.0] * L; M = [0] * L; peak = [1.0] * L
for c in order:
    block = sittings[c]
    # weights: Bayes posterior over the roster from every event realised before this cutoff
    logw = {k: 0.0 for k in roster}
    for e in ev:
        if e["rts"] < c:
            b = base_at(e["typ"], e["cutoff"])
            for k in roster:
                p = clip(e["fc"].get(k, b)) if k != "base" else b
                logw[k] += math.log(lik(p, e["Y"]))
    mx = max(logw.values()); w = {k: math.exp(x - mx) for k, x in logw.items()}; z = sum(w.values()); w = {k: x / z for k, x in w.items()}
    lb = 0.0; prods = {k: 0.0 for k in roster}
    for e in block:
        b = base_at(e["typ"], c)
        lb += math.log(lik(b, e["Y"]))
        for k in roster:
            p = clip(e["fc"].get(k, b)) if k != "base" else b
            prods[k] += math.log(lik(p, e["Y"]))
    lq = math.log(sum(w[k] * math.exp(prods[k]) for k in roster))
    D = (lq - lb) / (len(block) * LN)
    i = assign[c]; M[i] += 1
    lam = stake(S[i], Q[i], M[i]); W[i] *= 1 + lam * D; S[i] += D; Q[i] += D * D
    peak[i] = max(peak[i], W[i])
print(f"sittings {len(order)}; lag classes L = {L}; sittings per class {[len(x) for x in classes]}")
print("block-form final wealth per class:", [f"{x:.4g}" for x in W])
print("block-form running maximum per class:", [f"{x:.4g}" for x in peak])
print(f"threshold for some class at alpha=0.05 with the union bound: L/alpha = {L/0.05:g}")
