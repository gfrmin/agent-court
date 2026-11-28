#!/usr/bin/env python3
"""Write the gfrm.in Markdown and the arXiv metadata from the paper's Markdown source.

Usage: release_md.py <02-draft.md> <outdir>
"""
import datetime, os, pathlib, re, subprocess, sys

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
d = src.read_text(encoding="utf-8")

title = d.splitlines()[0].lstrip("# ").strip()
abstract = d[d.index("## Abstract\n") + len("## Abstract\n"):d.index("\n---\n\n## 1 Introduction")].strip()
assert len(abstract) <= 1920, len(abstract)
ntables = len(re.findall(r'^\*\*Table \d+\.', d, flags=re.M))
email_note = '' if os.environ.get('CLAIM_EMAIL') else '- Put your email in the author block: `CLAIM_EMAIL=... ./release.sh` rebuilds with it.\n'

# gfrm.in: front matter, a pointer to the preprint, then the paper from the reading note on
start = d.index("- *Square brackets give")
body = d[start:]
front = f'''---
title: "{title}"
date: {datetime.date.today().isoformat()}
draft: true
math: true
summary: "{abstract.split('. ')[0]}."
---

*This is the web version of a preprint: arXiv:XXXX.XXXXX [cs.AI]. The Lean proofs and the two scripts it relies on are ancillary files there.*

'''
(out / "law-before-the-agent.md").write_text(front + body, encoding="utf-8")

# arXiv metadata
pdf = out / "law-before-the-agent.pdf"
pages = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1) if pdf.exists() else "?"
tex_abstract = (abstract.replace("ö", '\\"o').replace("é", "\\'e").replace("—", "--")
                .replace("’", "'").replace("“", "``").replace("”", "''"))
meta = f"""# arXiv submission metadata

**Title:** {title}

**Authors:** Guy Freeman

**Abstract** ({len(abstract)} characters; the limit is 1,920). Paste the ASCII form, which uses TeX accents:

```
{tex_abstract}
```

**Comments:** {pages} pages, 1 figure, {ntables} tables. Lean 4 proofs and the analysis scripts are ancillary files.

**Primary category:** cs.AI. Possible cross-lists: cs.LO (the Lean proofs), stat.ME (the sequential tests).

**Licence:** your choice; CC BY 4.0 lets anyone reuse the text with credit.

**Files:** upload `law-before-the-agent-arxiv.tar.gz`. It holds `paper.tex`, `figure.tex` and `anc/` (the Lean project, `sim_filtration.py`, `block_on_log.py` and `04-selfcheck.md`). arXiv builds it with pdflatex and needs no BibTeX run.

**Before submitting:**
{email_note}- A first submission to cs.AI needs an endorsement from someone who has published there.
"""
(out / "arxiv-metadata.md").write_text(meta, encoding="utf-8")
