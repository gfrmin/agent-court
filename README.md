# A Court for Agents

The research outputs of [jack](https://github.com/renavondata/jack) — essays, an arXiv working paper and a monograph, working title *A Court for Agents* — by Guy Freeman, drafted with Claude sessions in two roles:

- **the author** writes `plan.md`, `chapters/`, `essays/`, `sources.md` and `data/recompute-*.md`;
- **counsel** (jack's counsel session) writes only `data/<layer>-exit.md` and `data/counsel-notes.md`.

Neither writes to jack. Every number in a draft carries a provenance tag pointing at an entry of jack's `log.jsonl` by seq, or a tool run on a named commit (see `plan.md` §2), so any reader can recompute it.

**Findings** — something the book needs changed in a court document or in jack's committed evidence — are issues labelled `finding`; counsel answers each on the issue and closes it with what was done. The book's own work is tracked as issues too: `gap` (a section waiting on the record), `nice-to-have`, `source` (a text the author needs), `erratum`, `site`, under milestones for each edition — the first edition cuts at C3's exit. **Essays** for Guy's read arrive as pull requests; merging one is the decision to publish it on [gfrm.in](https://gfrm.in).

The founding essay is [The Science Was Done. The Engineering Wasn't.](https://gfrm.in/posts/the-science-was-done/) (1 November 2026).

## Reading the book

The chapters are built into a book site by [mdBook](https://rust-lang.github.io/mdBook/) on every push to `master` (`.github/workflows/book.yml`, `book.toml`, `chapters/SUMMARY.md`) and published by GitHub Pages at <https://gfrmin.github.io/agent-court/>. The site carries a draft banner until the first edition; `sources.md` and `plan.md` are included as back matter. To build locally: `mdbook build` at the repository root, then open `book-site/index.html`.
