#!/bin/sh
# Build the arXiv source package, the PDF and the gfrm.in Markdown from the paper's Markdown.
# Usage: CLAIM_EMAIL=you@example.org CLAIM_DATE="November 2026" ./release.sh
# In the repository the paper is ../draft.md; in the Project workspace it is ../claim/02-draft.md.
set -eu
here=$(cd "$(dirname "$0")" && pwd)
if [ -f "$here/../draft.md" ]; then claim="$here/.."; draft="$claim/draft.md"
else claim="$here/../claim"; draft="$claim/02-draft.md"; fi
fig="$here/figure.tex"; [ -f "$fig" ] || fig="$here/tex/figure.tex"
out="$here/release"
rm -rf "$out" && mkdir -p "$out/arxiv/anc"
python3 "$here/md2tex.py" "$draft" "$out/arxiv" >/dev/null
cp "$fig" "$out/arxiv/"
cp "$claim/sim_filtration.py" "$claim/block_on_log.py" "$claim/04-selfcheck.md" "$out/arxiv/anc/"
cp -r "$claim/lean" "$out/arxiv/anc/lean"
rm -rf "$out/arxiv/anc/lean/.lake" "$out/arxiv/anc/lean/build"
# compile in a clean copy, as arXiv would (pdflatex, no BibTeX)
t=$(mktemp -d); cp -r "$out/arxiv/." "$t/"
( cd "$t" && pdflatex -interaction=nonstopmode paper.tex >/dev/null && pdflatex -interaction=nonstopmode paper.tex >/dev/null ) || { echo "compile failed"; grep '^!' "$t/paper.log" | head; exit 1; }
if grep -E 'undefined|^!' "$t/paper.log" | grep -v 'There were undefined' >/dev/null; then grep -E 'undefined|^!' "$t/paper.log" | head; fi
cp "$t/paper.pdf" "$out/law-before-the-agent.pdf"
( cd "$out/arxiv" && rm -f paper.pdf paper.aux paper.log paper.out && tar czf "$out/law-before-the-agent-arxiv.tar.gz" . )
python3 "$here/release_md.py" "$draft" "$out"
echo "pages: $(pdfinfo "$out/law-before-the-agent.pdf" | awk '/Pages/{print $2}')"
ls -la "$out"
