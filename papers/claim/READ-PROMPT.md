You are an anonymous referee for an arXiv preprint (cs.AI) and for a peer-reviewed venue in machine learning or AI safety. Read cold. You have not seen how this paper was written, and you owe its author nothing.

The paper is `papers/claim/draft.md` in this directory. Its claims about the reference implementation can be checked against `papers/claim/.jack/`, a clone of github.com/renavondata/jack at commit e580b64 (`log.jsonl`, `CHARTER.md`, `SPEC.md`, `REPORT.md`, `judge/`, `transcripts/`). Its claims about the book can be checked against this repository (`chapters/`). You may fetch any cited arXiv paper to check what the draft says of it. The simulation behind the example in §4.3 is `papers/claim/sim_filtration.py`; rerun it and say whether it shows what the paper says.

Write a referee report with these parts, in this order:

1. **Summary**: what the paper claims, in five sentences at most.
2. **Correctness**: check each of the six propositions and its proof. Say whether its hypotheses are stated, whether the proof is complete, and whether the statement says more than the proof gives. Be exact: name the line and give the counterexample when there is one.
3. **Novelty**: the paper claims three things as new; they are listed at the end of §1. For each claim, name any prior work that anticipates it, including work the paper does not cite. Say whether the related-work section treats the cited works fairly.
4. **Facts**: test at least ten of the bracketed checks (`[seq n]`, `[CHARTER …]`, `[SPEC …]`, `[book …]`) against the clones. List each one with "holds" or "fails", and give the line you read.
5. **Overclaiming and clarity**: say where the paper claims more than it shows, and where a reader would get lost.
6. **Is this a research paper or a position paper?** arXiv's CS moderators now reject position papers that have not been peer reviewed. Say which this is, and what would move it further towards a research paper.
7. **Recommendation**: one of accept, minor revision, major revision or reject, followed by the five changes that matter most, in order.

Write the whole report to `papers/claim/REVIEW-cold-1.md`. Do not edit any other file, and do not commit or push. End the report with one line: `RECOMMENDATION: <accept|minor revision|major revision|reject>`.
