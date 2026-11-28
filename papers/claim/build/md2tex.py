#!/usr/bin/env python3
"""Convert claude/claim/02-draft.md to an arXiv-ready LaTeX source (pdflatex).

Usage: md2tex.py DRAFT.md OUT_DIR
Writes OUT_DIR/paper.tex (with the bibliography inline) and leaves
figure.tex, which paper.tex \\input{}s, for the caller to provide.
"""
import os, re, sys, subprocess, unicodedata, pathlib

src, outdir = sys.argv[1], pathlib.Path(sys.argv[2])
md = open(src, encoding="utf-8").read()

# ---------- split off parts ----------
title = re.search(r"^# (.+)$", md, re.M).group(1).strip()
abstract = md.split("## Abstract\n", 1)[1].split("\n---\n", 1)[0].strip()
body = md.split("## 1 Introduction", 1)[1]
body = "## 1 Introduction" + body
body, refs = body.split("## References", 1)
body = body.replace("\n---\n", "\n")

# ---------- references -> keys ----------
def ascii_lower(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()

def surnames(authors):
    # "Jensen, M. C. & Meckling, W. H." -> ["Jensen","Meckling"]; et al. flagged
    etal = "et al." in authors
    a = authors.replace("et al.", "")
    parts = re.split(r"\s*&\s*|,\s*(?=[A-Z][a-zäöüé\-]+(?: [A-Z][a-z]+)?,)", a)
    names = []
    for p in parts:
        p = p.strip().strip(",")
        if not p:
            continue
        names.append(p.split(",")[0].strip())
    return names, etal

bib = []      # (key, label, year, text)
lookup = {}   # (surname_norm, year) -> [key]
for line in refs.splitlines():
    if not line.startswith("- "):
        continue
    m = re.match(r"- (.+?) \((\d{4}[a-z]?)\)\. (.*)$", line)
    if not m:
        sys.exit("unparsed reference: " + line)
    authors, year, rest = m.groups()
    names, etal = surnames(authors)
    first = names[0]
    if etal or len(names) >= 4:
        label = f"{first} et al."
    elif len(names) == 3:
        label = f"{names[0]}, {names[1]} and {names[2]}"
    elif len(names) == 2:
        label = f"{names[0]} and {names[1]}"
    else:
        label = first
    base = re.sub(r"[^a-z]", "", ascii_lower(first))
    key = base + year
    if first == "Chen":
        key = ("chenz" if "Zhu" in names else "chenj") + year
    bib.append((key, label, year, line[2:]))
    lookup.setdefault((base, year[:4], year[4:]), []).append(key)

def key_for(names_text, year):
    first = re.split(r",| &| and | et al\.", names_text)[0].strip()
    first = re.sub(r" [A-Z]\.$", "", first)          # "Chen J." -> "Chen"
    base = re.sub(r"[^a-z]", "", ascii_lower(first))
    y, suf = year[:4], year[4:]
    if base == "chen":
        return ("chenz" if "Zhu" in names_text else "chenj") + y
    ks = lookup.get((base, y, suf))
    return ks[0] if ks else None

# ---------- citations -> placeholders (outside maths) ----------
PH = {}
def ph(latex):
    k = f"QQCITE{len(PH):03d}QQ"
    PH[k] = latex
    return k

def conv_textual(t):
    # Kolt's principle of inclusivity [2026a]
    t = re.sub(r"Kolt's principle of inclusivity \[2026a\]",
               lambda m: "Kolt's principle of inclusivity " + ph(r"\citeyearpar{kolt2026a}"), t)
    def rep(m):
        names, years = m.group(1), m.group(2)
        ks = [key_for(names, y.strip()) for y in years.split(",")]
        if None in ks:
            return m.group(0)
        return ph(r"\citet{" + ",".join(ks) + "}")
    return re.sub(r"\b([A-Z][\w\-]+(?: et al\.| and [A-Z][\w\-]+)?) \[(\d{4}[a-z]?(?:, \d{4}[a-z]?)*)\]", rep, t)

CITE_PART = re.compile(r"^(?P<names>(?:de |van |von )?[A-ZÖÄÉ][^\[\]]*?) (?P<years>\d{4}[a-z]?(?:, \d{4}[a-z]?)*)(?:, (?P<loc>.+))?$")
def conv_part(p):
    p = p.strip()
    m = CITE_PART.match(p)
    if m:
        ks = [key_for(m["names"], y.strip()) for y in m["years"].split(",")]
        if None not in ks:
            loc = m["loc"]
            if loc:
                loc = loc.replace(" ", "~", 1) if loc.startswith(("App.", "Cor.", "ch.")) else loc
                return ph(r"\citealp[" + loc + "]{" + ",".join(ks) + "}")
            return ph(r"\citealp{" + ",".join(ks) + "}")
    return None

def conv_brackets(t):
    def rep(m):
        inner = m.group(1)
        if inner.startswith("http") or inner == "email":
            return m.group(0)
        parts = inner.split("; ")
        out, any_cite = [], False
        for p in parts:
            c = conv_part(p)
            if c:
                any_cite = True
                out.append(c)
            else:
                out.append(None)
        if not any_cite and not re.match(r"^(seqs? |CHARTER|SPEC|REPORT|BRIEF|log at|grant|`)", inner):
            return m.group(0)
        res = []
        for p, c in zip(parts, out):
            res.append(c if c else ph(r"\rec{" + pandoc_inline(p) + "}"))
        return ph("[") + "; ".join(res) + ph("]")
    return re.sub(r"(?<![\w\]])\[([^\[\]\n]+)\](?!\()", rep, t)

def pandoc_inline(t):
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "latex"], input=t, capture_output=True, text=True, check=True)
    return r.stdout.strip()

def convert_text(t):
    segs = re.split(r"(\$\$.*?\$\$|\$[^$\n]+\$)", t, flags=re.S)
    for i in range(0, len(segs), 2):
        segs[i] = conv_brackets(conv_textual(segs[i]))
    return "".join(segs)

def conv_table1(t):
    out=[]
    for line in t.split("\n"):
        if line.startswith("| **") or line.startswith("| |"):
            cells=line.split(" | ")
            if len(cells)==4 and cells[1] not in ("Result",):
                parts=[]
                for p in cells[1].split("; "):
                    c=conv_part(p) if "[" not in p else None
                    parts.append(c if c else p)
                cells[1]="; ".join(parts)
                line=" | ".join(cells)
        out.append(line)
    return "\n".join(out)
body = re.sub(r"^- (\([a-z]\) )", r"\n\1", body, flags=re.M)
body = conv_table1(body)
body = convert_text(body)
abstract_tex = pandoc_inline(abstract)

# Table 1 column widths
body = body.replace("| Ingredient | Result | Motivates | Response |\n|---|---|---|---|",
                    "| Ingredient | Result | Motivates | Response |\n|---|------|-------|--------|")
body = body.replace("| Process | Events | Scored | Wealth | Orders removed |\n|----------|-----|-----|----|---|",
                    "| Process | Events | Scored | Wealth | Orders removed |\n|-----------|-----|------|----|---|")
body = body.replace("| Layer | Entry | Outcome |\n|---|---|---|",
                    "| Layer | Entry | Outcome |\n|----|-----|-----------|")

# headings: drop manual numbers; LaTeX numbers them in the same order
body = re.sub(r"^## \d+ (.+)$", r"# \1", body, flags=re.M)
body = re.sub(r"^### \d+\.\d+ (.+)$", r"## \1", body, flags=re.M)
body = re.sub(r"^## (Disclosure|Code and data)$", r"# \1 {-}", body, flags=re.M)

r = subprocess.run(["pandoc", "-f", "markdown-implicit_figures-auto_identifiers-fancy_lists+lists_without_preceding_blankline", "-t", "latex", "--wrap=preserve"],
                   input=body, capture_output=True, text=True, check=True)
tex = r.stdout

# placeholders back
for k, v in PH.items():
    tex = tex.replace(k, v)
    abstract_tex = abstract_tex.replace(k, v)
assert "QQCITE" not in tex, re.findall(r"QQCITE\d+QQ", tex)[:5]

# propositions and proofs
def props(t):
    t = re.sub(r"\\textbf\{Proposition (\d) \(([^)]*)\)\.\}",
               lambda m: "\\begin{proposition}[" + m.group(2) + "]\\label{prop:" + m.group(1) + "}", t)
    t = t.replace("\\emph{Proof.}", "\\end{proposition}\n\n\\begin{proof}")
    t = re.sub(r"\\\(\\square\\\)", r"\\end{proof}", t)
    t = re.sub(r"\$\\square\$", r"\\end{proof}", t)
    return t
tex = props(tex)
assert tex.count("\\begin{proposition}") == 6 == tex.count("\\end{proposition}"), "proposition count"
assert tex.count("\\begin{proof}") == tex.count("\\end{proof}"), "proof count"
tex = re.sub(r"\\emph\{Remark \(([^)]*)\)\.\}", r"\\begin{remark}[\1]", tex)
tex = tex.replace("\\(\\mathcal G_{m-1}\\)-measurable", "\\(\\mathcal G_{m-1}\\)-measurable")

# tables: caption from the bold line before each table
def table_caption(t):
    t = re.sub(r"\\textbf\{Table 1\. ([^}]*)\}\s*\n\s*\n\\begin\{longtable\}",
               r"\\begin{longtable}", t, count=1)
    return t
def cap(t):
    while True:
        m = re.search(r"\\textbf\{Table (\d)\. ([^}]*)\}\s*\n", t)
        if not m: return t
        n, caption = m.group(1), m.group(2).rstrip(".")
        t = t[:m.start()] + t[m.end():]
        a = t.index("\\begin{longtable}", m.start())
        b = t.index("\\end{longtable}", a) + len("\\end{longtable}")
        lt = t[a:b]
        spec = re.match(r"\\begin\{longtable\}\[\]\{(.*?)\}\n\\toprule", lt, re.S).group(1)
        head = lt.split("\\toprule\\noalign{}\n",1)[1].split("\\midrule\\noalign{}\n",1)[0]
        rows = lt.split("\\endlastfoot\n",1)[1].rsplit("\\end{longtable}",1)[0]
        new = ("\\begin{table}[tbp]\n\\caption{" + caption + "}\\label{tab:" + n + "}\n\\small\n"
               "\\begin{tabular}{" + spec.replace("\\columnwidth","\\linewidth") + "}\n\\toprule\n" + head + "\\midrule\n" + rows + "\\bottomrule\n\\end{tabular}\n\\end{table}")
        t = t[:a] + new + t[b:]
tex = cap(tex)

# close remark at the paragraph end
tex = re.sub(r"(\\begin\{remark\}\[[^\]]*\].*?)(\n\n)", lambda m: m.group(1) + "\n\\end{remark}" + m.group(2), tex, flags=re.S)

# figure after section 2's threat model paragraph
tex = tex.replace("\\section{Why these ingredients}", "\\input{figure}\n\n\\section{Why these ingredients}", 1); assert "\\input{figure}" in tex

# bibliography
def bib_tex(text):
    t = pandoc_inline(re.sub(r"doi:(\S+)$", "", text).strip())
    m = re.search(r"doi:(\S+)$", text)
    if m:
        t += " \\doi{" + m.group(1) + "}"
    return t
bibitems = []
for key, label, year, text in bib:
    bibitems.append(f"\\bibitem[{label}({year})]{{{key}}}\n{bib_tex(text)}")
bibliography = "\\begin{thebibliography}{99}\n\\small\n" + "\n\n".join(bibitems) + "\n\\end{thebibliography}\n"

preamble = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[british]{babel}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{microtype}
\usepackage{longtable,booktabs,array,calc}
\usepackage{enumitem}
\setlist{itemsep=1pt,topsep=3pt,parsep=0pt}
\usepackage{newunicodechar}
\newunicodechar{α}{\ensuremath{\alpha}}
\newunicodechar{◦}{\ensuremath{\circ}}
\newunicodechar{′}{\ensuremath{'}}
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{·}{\textperiodcentered}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,fit,backgrounds}
\usepackage[square,authoryear]{natbib}
\setcitestyle{notesep={, },aysep={}}
\usepackage{etoolbox}\AtBeginEnvironment{longtable}{\small}
\usepackage{xcolor}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue!50!black]{hyperref}
\usepackage{caption}
\captionsetup{font=small,labelfont=bf}
\providecommand{\tightlist}{\setlength{\itemsep}{1pt}\setlength{\parskip}{0pt}}
\newcommand{\rec}[1]{{\small #1}}
\newcommand{\doi}[1]{\href{https://doi.org/#1}{\nolinkurl{doi:#1}}}
\theoremstyle{plain}
\newtheorem{proposition}{Proposition}
\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\setlength{\parskip}{3pt}
\setlength{\LTpre}{6pt}\setlength{\LTpost}{6pt}
\def\LTcaptype{table}
"""
doc = preamble + r"""
\title{""" + title + r"""}
\author{Guy Freeman\\[2pt]\normalsize Independent researcher, Hong Kong\\\normalsize\texttt{""" + os.environ.get("CLAIM_EMAIL", "[email]") + r"""}}
\date{""" + os.environ.get("CLAIM_DATE", "Draft, 26 November 2026") + r"""}
\begin{document}
\maketitle
\begin{abstract}
""" + abstract_tex + r"""
\end{abstract}

{\renewcommand{\thefootnote}{}\footnotetext{Facts about the reference implementation carry their check in square brackets: \rec{seq $n$} is an entry of the signed log \texttt{log.jsonl} of \texttt{renavondata/jack}; \rec{CHARTER}, \rec{SPEC} and \rec{REPORT} are files of that repository at commit \texttt{e580b64}. Citations of \citet{freeman2026} refer to \texttt{gfrmin/agent-court} at commit \texttt{007a007}.}}

""" + tex + "\n" + bibliography + "\n\\end{document}\n"
(outdir / "paper.tex").write_text(doc, encoding="utf-8")
print("ok", len(PH), "placeholders,", len(bib), "references")
