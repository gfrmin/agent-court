# A Court for Agents

The research outputs of [jack](https://github.com/renavondata/jack) — essays, an arXiv working paper and a monograph, working title *A Court for Agents* — by Guy Freeman, drafted with Claude sessions in two roles:

- **the author** writes `plan.md`, `chapters/`, `essays/`, `sources.md` and `data/recompute-*.md`;
- **counsel** (jack's counsel session) writes only `data/<layer>-exit.md` and `data/counsel-notes.md`.

Neither writes to jack. Every number in a draft carries a provenance tag pointing at an entry of jack's `log.jsonl` by seq, or a tool run on a named commit (see `plan.md` §2), so any reader can recompute it.

**Findings** — something the book needs changed in a court document or in jack's committed evidence — are issues labelled `finding`; counsel answers each on the issue and closes it with what was done. The book's own work is tracked as issues too: `gap` (a section waiting on the record), `nice-to-have`, `source` (a text the author needs), `erratum`, `site`, under milestones for each edition — the first edition cuts at C3's exit. **Essays** for Guy's read arrive as pull requests; merging one is the decision to publish it on [gfrm.in](https://gfrm.in).

The founding essay is [The Science Was Done. The Engineering Wasn't.](https://gfrm.in/posts/the-science-was-done/) (1 November 2026).

## Reading the book

The book's home is <https://gfrm.in/book/>: gfrmin/gfrminsite's publish workflow checks out this repository and builds `chapters/` with [mdBook](https://rust-lang.github.io/mdBook/) into `/book/` on every deploy, nightly, and whenever this repository's `book` workflow dispatches it. The `book` workflow here builds on every change (a red build is a broken chapter) and keeps the site as an artifact. The site carries a draft banner until the first edition; `sources.md` and `plan.md` are back matter. To build locally: `mdbook build` at the repository root, then open `book-site/index.html`.
