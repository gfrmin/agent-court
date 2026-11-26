# Cold read 14 of the claim paper: the final change

- **Reader:** `openai/gpt-6.1-sol`, run as a read-only session on the runner. The issue is renavondata/opencode-runner #1389, which ran from 11:02Z to 11:04Z on 26 November.
- **Scope:** draft 24 against draft 23 (cold read 13 accepted draft 23). The read covered the three passages that changed, and only those.
- **Verdict:** **accept**. All three are backed by the record and introduce no error. The reader recounted the proposal recipe from the log (702; 627; 75; 46), re-ran the 14-day scan, and re-ran `block_on_log.py`.

So the release candidate, draft 24, has had a cold read in full: draft 23 by cold read 13, and the change from 23 to 24 by this one.

## The report (verbatim)

## Referee report: draft 24’s three changed passages

The in-memory diff confirms exactly three passage changes. I checked them against the cited record at `e580b64`, CHARTER §12, and the paper’s ancillary computation.

### 1. Status of the four falsifiers (§6)

**Backing: supported.** The revised summary correctly distinguishes untested clauses from clauses not triggered:

- **First, size clause:** the kernel’s Python files total **450 physical lines** (138 + 172 + 140), below 1,500.
- **First, Datalog clause:** the record contains **no `rule` entry**. The paper appropriately reports this clause as untested.
- **Second, assize baseline:** C1a and C1b were promoted at seqs **188 and 337**, but the C1b brief explicitly commits the builders’ **\(6/11\)** null and says assize’s figures are “reported beside it, not bet on.” Calling the specifically worded assize comparison untested is justified.
- **Third, re-typing:** the repair predicate’s introduction is the sole matching `git log -S` change, at **879caf93**. The raw/attributed CSV pairs reproduce **7→1** and **81→9** repair rows through attribution changes. The distinction between re-attribution and re-typing is supported.
- **Fourth, procedure growth:** my complete-14-day scan reproduces the genesis interval’s **63:5** ratio. Breaching start times are confined to **14–17 October**, before forecast authority at seq 31 on 25 October. The maximum for starts at or after seq 31 is **872:1,755**.

**Consistency: no error introduced.** The summary now agrees with the four following bullets. “One clause has been tested and not met” identifies the first falsifier’s size clause; the subsequent sentences separately state the third and fourth falsifiers’ status. It no longer treats an unperformed comparison as a survived test.

### 2. What the recomputation’s thresholds bound (§6)

**Backing: supported, under the null and information assumptions stated in §4.3.** I reran `block_on_log.py` directly from memory against `e580b64`. It reproduces **476 completed sittings, four pending**, and thresholds **40, 120, 240, 400, 600**.

For a fixed protocol, the class-specific crossing bounds are \(\alpha/[\ell(\ell+1)]\); summing over classes gives at most **\(\alpha=0.05\)**. This accommodates the protocol’s adaptive creation of lag classes. It does not supply a correction for selecting the protocol itself after examining the record.

The rerun also reproduces pooled-baseline final wealth of approximately **19,930** and **11,090** in the first two classes, while every per-dataset running maximum is **1**.

**Consistency: no error introduced.** The addition correctly separates the fixed-protocol mathematical guarantee from retrospective protocol selection. It neither repairs nor claims to repair the implementation’s invalid per-event compounding, and it agrees with the surrounding retrospective-audit qualification.

### 3. Proposal-title classification recipe (§5.2)

**Backing: supported.** Selecting proposals by `builder` and `reviewer` gives **702**. Applying the stated, case-sensitive title prefixes—`due `, `freshness`, `hkjc`, `M2 race`—gives **627**, leaving **75**.

Among those 75, matching **whole words** `read` or `review`, case-insensitively, gives **48**. Excluding the two named read-gate proposals, seqs **654 and 657**, leaves exactly **46**. Whole-word matching correctly avoids counting “reviewer” in the forecast proposal at seq 91 and the freshness-note proposal at seq 1496. The remaining **29** titles concern tooling/code, pins, replay tables, fixes, and other forecasts or resolutions.

The adjacent activity totals also reproduce: **6,621** builder/reviewer entries; **5,919** forecasts/resolutions; **5,811** of the two exact stream types.

**Consistency: no error introduced.** The recipe reproduces the existing figures and supports the routine-versus-construction conclusion. “Naming a read or review” has the natural whole-word interpretation needed for the reported count.

All three changes are supported and resolve the requested clarifications.

RECOMMENDATION: accept
exit=0
```

