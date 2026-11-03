#!/usr/bin/env python3
"""Check that the book's prose agrees with the record, with itself and with its sources.

The prose keeps literal numbers, names and quotations — it is read raw on GitHub, in
review diffs, and in the essays copied to gfrm.in, which Hugo renders and mdBook does
not. Nothing is substituted. Instead this script fails when the prose and the thing it
reports disagree. Four checks:

  facts      every figure in data/facts.toml is recomputed from renavondata/jack at
             the commit it is pinned to, and every phrase that prints it prints the
             recomputed value — wherever the phrase occurs, so a stale copy fails too.
  counts     numbers the book states about itself ("the fifteen rows above") are
             counted from the book's own files.
  citations  every "Author (Year)" in a chapter or essay has an entry in sources.md,
             and every entry there is cited somewhere or listed as uncited on purpose.
  quotes     every quotation attributed to a jack document (CHARTER, SPEC, LAW, a
             BRIEF, a bare amendment clause such as A2.10) occurs verbatim in that
             document at the commit the citing file pins.

Usage:
  tools/check_book.py --jack PATH      # all four; PATH is a clone of renavondata/jack
                                       # with full history (status.py needs it)
  tools/check_book.py --no-jack        # counts and citations only, for a quick local run

Exit status 0 when every check passes, 1 otherwise. Nothing is written anywhere.
Standard library only (Python 3.11+, for tomllib).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import tomllib
import unicodedata
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
WORD_RE = "|".join(sorted(NUMBER_WORDS, key=len, reverse=True))
MONTHS = {"January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"}

errors: list[str] = []


def err(where: str, msg: str) -> None:
    errors.append(f"{where}: {msg}")


# ---------------------------------------------------------------- the book's files

def prose_files() -> list[Path]:
    """Chapters and essays: the files a reader sees. Symlinks (plan.md, sources.md in
    chapters/) and the summary are excluded; plan.md is the author's working record."""
    out = []
    for p in sorted((ROOT / "chapters").glob("*.md")):
        if p.is_symlink() or p.name == "SUMMARY.md":
            continue
        out.append(p)
    out += sorted((ROOT / "essays").glob("*/index.md"))
    return out


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def strip_code(text: str) -> str:
    """Blank out fenced blocks, inline code and link targets, keeping line numbers."""
    text = re.sub(r"```.*?```", lambda m: re.sub(r"[^\n]", " ", m.group()), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group()), text)
    text = re.sub(r"\]\([^)\s]*\)", lambda m: "]" + " " * (len(m.group()) - 1), text)
    return text


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


# ---------------------------------------------------------------- number rendering

def render(value, style: str) -> str:
    if style == "words":
        return NUMBER_WORDS[value]
    if style == "Words":
        return NUMBER_WORDS[value].capitalize()
    if style == "comma":
        return f"{value:,}"
    return str(value)


def placeholder_re(style: str) -> str:
    if style in ("words", "Words"):
        return rf"(?i:{WORD_RE})"
    if style == "comma":
        return r"\d{1,3}(?:,\d{3})+|\d+"
    if style == "fraction":
        return r"\d+/\d+"
    return r"[\d.]+"


def check_phrases(fid: str, value, phrases: list[dict], files: list[Path]) -> None:
    """Each phrase is a template with one {style} placeholder. Every occurrence of the
    template, with any number in the placeholder, in any prose file, must carry the
    value; and each file the phrase names must contain at least one occurrence."""
    texts = {p: p.read_text(encoding="utf-8") for p in files}
    for ph in phrases:
        tmpl = ph["text"]
        m = re.search(r"\{(\w+)\}", tmpl)
        if not m:
            err(f"facts.toml [{fid}]", f"phrase has no placeholder: {tmpl!r}")
            continue
        style = m.group(1)
        before, after = tmpl[:m.start()], tmpl[m.end():]
        pat = re.compile(re.escape(before).replace(r"\ ", r"\s+") + f"({placeholder_re(style)})"
                         + re.escape(after).replace(r"\ ", r"\s+"))
        want = render(value, style)
        named = {ROOT / f for f in ph.get("in", [])}
        found_in = set()
        for p, t in texts.items():
            for hit in pat.finditer(t):
                found_in.add(p)
                got = hit.group(1)
                ok = got.lower() == want.lower() if style in ("words", "Words") else got == want
                if not ok:
                    err(f"{rel(p)}:{line_of(t, hit.start())}",
                        f"[{fid}] prints {got!r} where the record gives {want!r}: …{hit.group()}…")
        for p in named - found_in:
            if p.exists():
                err(rel(p), f"[{fid}] expected the phrase {before + want + after!r} and found none")


# ---------------------------------------------------------------- jack

class Jack:
    def __init__(self, path: Path):
        self.path = path
        self._worktrees: dict[str, Path] = {}
        self._tmp = tempfile.TemporaryDirectory(prefix="check-book-")

    def git(self, *args: str) -> str:
        return subprocess.run(["git", "-C", str(self.path), *args], check=True,
                              capture_output=True, text=True).stdout

    def resolve(self, commit: str) -> str:
        return self.git("rev-parse", "--verify", f"{commit}^{{commit}}").strip()

    def show(self, commit: str, path: str) -> str | None:
        r = subprocess.run(["git", "-C", str(self.path), "show", f"{commit}:{path}"],
                           capture_output=True, text=True)
        return r.stdout if r.returncode == 0 else None

    def ls(self, commit: str, path: str = "") -> list[str]:
        return self.git("ls-tree", "--name-only", commit, path).split()

    def log(self, commit: str) -> list[dict]:
        return [json.loads(l) for l in self.show(commit, "log.jsonl").splitlines() if l.strip()]

    def worktree(self, commit: str) -> Path:
        if commit not in self._worktrees:
            wt = Path(self._tmp.name) / commit
            self.git("worktree", "add", "--detach", "--quiet", str(wt), commit)
            self._worktrees[commit] = wt
        return self._worktrees[commit]

    def close(self) -> None:
        for wt in self._worktrees.values():
            subprocess.run(["git", "-C", str(self.path), "worktree", "remove", "--force", str(wt)],
                           capture_output=True)
        self._tmp.cleanup()


def fold(entries: list[dict], spec: dict) -> int:
    """A count over the log. Filters: type, proposer, seq_gt, seq_le."""
    n = 0
    for e in entries:
        if "type" in spec and e["type"] != spec["type"]:
            continue
        if "proposer" in spec and e["proposer"] != spec["proposer"]:
            continue
        if "seq_gt" in spec and not e["seq"] > spec["seq_gt"]:
            continue
        if "seq_le" in spec and not e["seq"] <= spec["seq_le"]:
            continue
        n += 1
    return n


def recompute(jack: Jack, fid: str, f: dict):
    commit = jack.resolve(f["commit"])
    how = f["how"]
    if how == "fold":
        return fold(jack.log(commit), f["where"])
    if how == "files":
        total = 0
        for name in jack.ls(commit, f["dir"]):
            if re.search(f["match"], name):
                d = json.loads(jack.show(commit, name))
                v = d[f["field"]]
                total += len(v) if isinstance(v, list) else v
        return total
    if how == "command":
        wt = jack.worktree(commit)
        r = subprocess.run([sys.executable, *f["argv"]], cwd=wt,
                           capture_output=True, text=True)
        out = r.stdout + r.stderr
        m = re.search(f["extract"], out)
        if not m:
            err(f"facts.toml [{fid}]", f"`{' '.join(f['argv'])}` at {commit[:8]} printed nothing "
                f"matching {f['extract']!r}:\n{out.strip()[-600:]}")
            return None
        g = m.group(1)
        return Fraction(g) if "/" in g else int(g.replace(",", ""))
    err(f"facts.toml [{fid}]", f"unknown method {how!r}")
    return None


def check_facts(facts: dict, jack: Jack | None, files: list[Path]) -> None:
    for fid, f in facts.get("fact", {}).items():
        value = f["value"]
        if isinstance(value, str) and "/" in value:
            value = Fraction(value)
        if jack is not None:
            got = recompute(jack, fid, f)
            if got is not None and got != value:
                err(f"facts.toml [{fid}]", f"recomputes to {got} at jack {f['commit'][:8]}, "
                    f"but the file says {value}")
        check_phrases(fid, f["value"], f.get("phrase", []), files)


# ---------------------------------------------------------------- counts

def check_counts(facts: dict, files: list[Path]) -> None:
    for cid, c in facts.get("count", {}).items():
        text = (ROOT / c["file"]).read_text(encoding="utf-8")
        n = len(re.findall(c["pattern"], text, flags=re.M))
        if "expect" in c and n != c["expect"]:
            err(f"facts.toml [{cid}]", f"{c['file']} has {n} matches of {c['pattern']!r}; "
                f"the file expects {c['expect']} — update the expectation and the prose together")
        check_phrases(cid, n, c.get("phrase", []), files)


# ---------------------------------------------------------------- citations

def surname_key(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s.lower().replace("’", "'")


def sources_index() -> dict[tuple[str, str], int]:
    """(first author's surname, year) -> line in sources.md, for every entry and every
    extra year the entry carries in bold, e.g. Nachbar (1997) ... **(2005)**."""
    idx = {}
    for i, line in enumerate((ROOT / "sources.md").read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"- \*\*(.+?)\*\*", line)
        if not m:
            continue
        head = m.group(1)
        sm = re.match(r"([^,(]+?),", head)
        if not sm:
            continue
        name = surname_key(sm.group(1).strip())
        years = re.findall(r"\((\d{4})", head) + re.findall(r"\*\*\((\d{4})\)\*\*", line)
        for y in years:
            idx[(name, y)] = i
    return idx


NAME = r"(?:de |van |von |Van |De )?[A-Z][\w’']*?[\w](?:-[A-Z][\w]+)?(?:['’]s)?"
CITE = re.compile(
    rf"(?P<names>{NAME}(?:(?:,\s+|\s+and\s+|\s+&\s+){NAME})*(?:\s+et al\.)?)"
    rf",?\s+\(?(?P<years>\d{{4}}[a-z]?(?:,\s*\d{{4}}[a-z]?)*)\b")


def check_citations(facts: dict, files: list[Path]) -> None:
    conf = facts.get("citations", {})
    ignore = set(conf.get("not_names", []))
    uncited_ok = set(conf.get("uncited_ok", []))
    idx = sources_index()
    used: set[tuple[str, str]] = set()
    for p in files:
        raw = p.read_text(encoding="utf-8")
        text = strip_code(raw)
        for m in CITE.finditer(text):
            names = re.split(r",\s+|\s+and\s+|\s+&\s+", m.group("names").replace(" et al.", ""))
            first = re.sub(r"['’]s$", "", names[0])
            if first in MONTHS or first in ignore or first.split()[-1] in ignore:
                continue
            for y in re.findall(r"\d{4}", m.group("years")):
                if not 1600 <= int(y) <= 2030:
                    continue
                key = (surname_key(first), y)
                if key in idx:
                    used.add(key)
                else:
                    err(f"{rel(p)}:{line_of(text, m.start())}",
                        f"cites {first} ({y}), which has no entry in sources.md")
    # An entry also counts as cited when its surname appears in the prose without a
    # year and no other entry shares the surname, so the reference is unambiguous.
    prose = surname_key(" ".join(strip_code(p.read_text(encoding="utf-8")) for p in files))
    by_name: dict[str, int] = {}
    for (name, _y) in idx:
        by_name[name] = by_name.get(name, 0) + 1
    for key, line in sorted(idx.items(), key=lambda kv: kv[1]):
        label = f"{key[0]} {key[1]}"
        if key not in used and by_name[key[0]] == 1 and re.search(rf"\b{re.escape(key[0])}\b", prose):
            continue
        if key not in used and label not in uncited_ok:
            err(f"sources.md:{line}", f"{label} is cited by no chapter or essay "
                "(cite it, drop it, or list it under [citations] uncited_ok)")


# ---------------------------------------------------------------- quotations

QUOTE = re.compile(r'"([^"\n]{12,}?)"|“([^”\n]{12,}?)”')
DOC = re.compile(r"\b(CHARTER|SPEC|LAW(?:\.md)?|BRIEF-[A-Z0-9a-z]+|A\d+\.\d+|RUNBOOK)\b")


def norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[*_`]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def doc_path(jack: Jack, commit: str, tag: str) -> str | None:
    if re.fullmatch(r"A\d+\.\d+", tag) or tag == "CHARTER":
        return "CHARTER.md"
    if tag == "SPEC":
        return "SPEC.md"
    if tag.startswith("LAW"):
        return "LAW.md"
    if tag == "RUNBOOK":
        return "RUNBOOK.md"
    if tag.startswith("BRIEF-"):
        for cand in (f"{tag}.md", f"transcripts/{tag}.md", f"transcripts/{tag}-draft.md"):
            if jack.show(commit, cand) is not None:
                return cand
    return None


def pin_of(text: str, default: str) -> str:
    m = (re.search(r"`renavondata/jack` at `([0-9a-f]{7,40})`", text)
         or re.search(r"at commit \[`([0-9a-f]{7,40})`\]", text))
    return m.group(1) if m else default


def check_quotes(facts: dict, jack: Jack, files: list[Path]) -> None:
    default = facts["pins"]["jack"]
    cache: dict[tuple[str, str], str | None] = {}
    for p in files:
        text = p.read_text(encoding="utf-8")
        commit = jack.resolve(pin_of(text, default))
        for m in QUOTE.finditer(text):
            q = m.group(1) or m.group(2)
            tail = text[m.end():m.end() + 90]
            d = DOC.search(tail)
            if not d or d.start() > 60:
                continue
            path = doc_path(jack, commit, d.group(1))
            where = f"{rel(p)}:{line_of(text, m.start())}"
            if path is None:
                err(where, f"quotes {d.group(1)}, which is not in jack at {commit[:8]}")
                continue
            if (commit, path) not in cache:
                body = jack.show(commit, path)
                cache[(commit, path)] = norm(body) if body is not None else None
            body = cache[(commit, path)]
            if body is None:
                err(where, f"{path} is not in jack at {commit[:8]}")
                continue
            parts = [norm(x) for x in re.split(r"…|\.\.\.|\[[^\]]*\]", q) if norm(x)]
            pos = 0
            for part in parts:
                i = body.find(part, pos)
                if i < 0 and part:  # an initial capital may be lowered or raised to fit
                    alt = part[0].swapcase() + part[1:]
                    i = body.find(alt, pos)
                if i < 0:
                    err(where, f"quotation not verbatim in {path} at {commit[:8]}: \"{part}\"")
                    break
                pos = i + len(part)


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--jack", type=Path, help="a clone of renavondata/jack with full history")
    g.add_argument("--no-jack", action="store_true", help="skip the checks that need jack")
    a = ap.parse_args()

    facts = tomllib.loads((ROOT / "data" / "facts.toml").read_text(encoding="utf-8"))
    files = prose_files()
    jack = Jack(a.jack.resolve()) if a.jack else None
    try:
        check_facts(facts, jack, files)
        check_counts(facts, files)
        check_citations(facts, files)
        if jack is not None:
            check_quotes(facts, jack, files)
    finally:
        if jack is not None:
            jack.close()

    scope = "facts, counts, citations, quotes" if jack else "counts, citations, phrases (no jack)"
    if errors:
        print(f"check_book: {len(errors)} problem(s) [{scope}]")
        for e in errors:
            print("  " + e)
        return 1
    print(f"check_book: ok [{scope}] over {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
