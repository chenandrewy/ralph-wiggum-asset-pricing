Title: Figure 1 Failure Trace
Date: 2026-04-02
Time: 07:10:08 EDT

# Human Summary

It seems like what happened is that somewhere along the lines, one of the agents thought that the words credentials were not set. And it wrote this down in the paper saying words credentials needed. This was in fact false, but everyone got anchored to this.


# AI Details

Figure 1 stayed broken for a persistent process reason, not just a code reason.

The immediate code problem appears to have been a runtime SQL/schema failure in `code/main.R` rather than missing WRDS access. The project history, however, repeatedly converged on the wrong diagnosis: "Figure 1 is blocked on WRDS credentials" or "blocked by environment." Once that diagnosis took hold, later plans and tests inherited it instead of re-testing it.

## What the test required

`tests/factcheck-code.py` explicitly instructs the agent to run the canonical analysis path when feasible:

- Step 3 at line 40: "Run the canonical local analysis steps in dependency order when feasible under the execution model required by the paper spec."

This matters because a bad column name is a runtime error. Static review of the SQL can miss it.

## What the factcheck-code agent actually did

The saved `factcheck-code` logs show the agent did not run `Rscript code/main.R`.

Instead, in `ralph-garage/agent-logs/20260402T050928.548716-0400_factcheck-code_claude_opus.log`, it:

1. Listed `code/` and `data/`.
2. Read `code/main.R`.
3. Checked whether R and packages were installed with:
   `R --version 2>&1 | head -3 && Rscript -e 'installed.packages()[,"Package"]' 2>&1 | head -20`
4. Read `ralph/code-templates/query-wrds-example.R`.
5. Wrote the report without invoking `Rscript code/main.R`.

The same log shows R was installed and `DBI` / `RPostgres` were present. After that check, the agent said it had enough information to write the report. I do not see a logged command running the pipeline itself, and I do not see the runtime strings that `code/main.R` would emit:

- `Querying WRDS for CRSP monthly data...`
- `Retrieved ... rows.`
- `Figure written to paper/exhibits/ai-vs-nonai-pd.pdf`

So the agent did not do the one action most likely to reveal the true failure.

## How the wrong diagnosis propagated

The improvement-plan history shows a repeated shift from "run the code" to "blocked on WRDS."

Early and mid-run plans repeatedly framed Figure 1 as a credentials/access problem:

- "Run `code/main.R` with WRDS credentials to generate the real figure."
- "If WRDS credentials are available, run `code/main.R`."
- "The WRDS query in `code/main.R` has never been executed."
- "These will remain FAIL until `code/main.R` is run with WRDS credentials."

Later plans did identify one real code issue in `code/main.R`:

- stock-split adjustment via `cfacpr` / `cfacshr`
- stale comment cleanup

But even there, the root framing remained "fix code, then regenerate once WRDS is available." That still assumed access was the blocker.

## Why Figure 1 stayed out of the paper

The failure chain appears to be:

1. `code/main.R` was added as the canonical Figure 1 pipeline.
2. The figure remained a placeholder.
3. Test agents and planning agents inferred that WRDS access or environment was the blocker.
4. `factcheck-code` used static inspection plus an environment probe instead of executing the pipeline, despite the test instruction to run it when feasible.
5. Because the pipeline was not executed, the actual runtime error was not surfaced in the history.
6. The placeholder PDF remained in place, causing repeated failures in:
   - `factcheck-exhibits`
   - `factcheck-bysection`
   - `visual-figures`
   - `visual-pages`

In other words, the persistent failure to include Figure 1 was not only "the code was wrong." It was "the loop settled on the wrong blocker diagnosis and then stopped testing the hypothesis."

## Process mistakes

- Anchoring: once "WRDS credentials unavailable" appeared in reports, later agents reused it.
- Static-analysis substitution: the code looked structurally plausible, so agents reasoned about likely SQL bugs without running it.
- Feasibility slippage: the test required execution when feasible, but the agent downgraded execution to optional after checking local R/package availability.
- Summary inheritance: improvement plans copied the previous diagnosis instead of falsifying it.

## Bottom line

Figure 1 was persistently absent because the loop did not reliably exercise the canonical pipeline. The code path for the figure existed, but the critical runtime step was skipped. That allowed a false "WRDS-blocked" story to dominate the history while the real runtime failure in `code/main.R` stayed hidden.

## Audit of all factcheck-code logs

I checked every saved `factcheck-code` log under `ralph-garage/agent-logs/`. None of them contain an actual command invoking `Rscript code/main.R`.

### 1. `20260401T222029.448602-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** tried to inspect the repo layout (`find /workspace/code`, `find /workspace/data`, `ls -la /workspace/code /workspace/data /workspace/paper/exhibits`) and concluded there was no code to run.
- **Conclusion reached:** fail because `code/` was empty and no exhibits existed.

### 2. `20260401T231820.337874-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** same structural inspection as the prior run (`find`/`ls` on `code`, `data`, and `paper/exhibits`).
- **Conclusion reached:** fail because `code/` was empty and no canonical path existed.

### 3. `20260401T235917.677885-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** listed `code/`, `data/`, and `paper/exhibits/`, then treated the paper as purely theoretical with nothing to execute.
- **Conclusion reached:** pass on a vacuous reading because the paper had zero exhibits.

### 4. `20260402T001555.504308-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** listed `code/`, `data/`, and `paper/exhibits/`, then again treated the repo as missing any runnable code.
- **Conclusion reached:** fail because the canonical pipeline and exhibit infrastructure were absent.

### 5. `20260402T004753.405779-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** inspected directory structure for `code/`, `data/`, `paper/exhibits/`, and `paper/`.
- **Conclusion reached:** this run still did not exercise the pipeline; it remained an inspection-only pass over the repo structure.

### 6. `20260402T011319.688508-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** inspected directories, checked whether `R` and `Rscript` existed, queried installed packages via `Rscript -e`, and ran a trivial `Rscript -e 'cat("test")'`.
- **Conclusion reached:** treated execution as blocked by missing WRDS credentials and analyzed the code path without running it.

### 7. `20260402T042006.074588-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** inspected `code/`, `data/`, and `paper/exhibits/`, checked whether `R`/`Rscript` existed, and looked at the exhibit output directory.
- **Conclusion reached:** another static inspection run; no end-to-end pipeline execution.

### 8. `20260402T043338.175499-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** inspected `code/`, `data/`, `paper/exhibits/`, and counted lines in `paper.tex`. It then wrote a report claiming execution was blocked by environment / credentials and reasoned from static code inspection.
- **Conclusion reached:** pass on canonical-path structure with “blocked by environment” framing, despite not running the pipeline.

### 9. `20260402T044727.276518-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** listed directories, grepped `paper.tex` for exhibit references and CRSP mentions, checked `R` / `Rscript`, and verified that `library(DBI); library(RPostgres)` loaded.
- **Conclusion reached:** fail based on a static diagnosis of split-adjustment defects, while still treating execution as blocked.

### 10. `20260402T050928.548716-0400_factcheck-code_claude_opus.log`

- **Did it run `code/main.R`?** No.
- **What it did instead:** listed directories, read `code/main.R`, checked `R --version`, inspected installed packages, and read `ralph/code-templates/query-wrds-example.R`.
- **Conclusion reached:** fail based on a static diagnosis of a date-join bug and split-adjustment omission, while stating execution was blocked by credentials/network.

## Summary of the factcheck-code audit

- Early logs (1–4) did not run code because `code/` was genuinely absent.
- Once `code/main.R` existed (logs 5–10), the test still never ran it.
- The later pattern was consistent:
  - read `code/main.R`
  - inspect directories and the existing placeholder exhibit
  - check local R / package availability
  - infer a WRDS or environment blocker
  - write the report without executing the canonical pipeline

This is the core procedural failure. The test instruction required running the canonical steps when feasible, but the saved `factcheck-code` runs stopped at static inspection plus environment probing. That is why the loop repeatedly discussed hypothetical SQL defects while missing the actual runtime failure that prevented Figure 1 from ever being generated.

## New confirming evidence

After this audit, a fresh direct run of `tests/factcheck-code.py` surfaced the SQL bug in `code/main.R`.

The WRDS environment did not change. This matters because it removes one possible explanation for the earlier logs. The difference was not that WRDS access later became available. The earlier saved `factcheck-code` runs had the same underlying environment but did not execute `code/main.R`; they stopped at static inspection and environment probing instead.

So the record now shows two things side by side:

- the saved earlier `factcheck-code` logs do not contain an actual `Rscript code/main.R` invocation;
- a later direct run of the same test in the same WRDS environment was able to surface the SQL/schema bug.
- when queried directly, session `7d6e8547-49e6-4996-892f-913646e63003` reported that it had assumed the WRDS credentials were not set, but did not give a concrete reason for that assumption.

## Iteration timeline for the late runs

This section focuses only on one question: did `factcheck-code` actually run `code/main.R`?

### Iteration 8

- **Author plan time:** 2026-04-02 04:14:30 EDT
- **factcheck-code start:** 2026-04-02 04:20:06 EDT
- **Log:** `20260402T042006.074588-0400_factcheck-code_claude_opus.log`
- **Did it run `code/main.R`?** No.
- **What it did instead:** listed `code/`, `data/`, and `paper/exhibits/`; checked whether `R` / `Rscript` existed; inspected the output directory.

The logged commands are directory and runtime probes only. There is no logged command invoking `Rscript code/main.R`.

### Iteration 9

- **Author plan time:** 2026-04-02 04:30:10 EDT
- **factcheck-code start:** 2026-04-02 04:33:38 EDT
- **Log:** `20260402T043338.175499-0400_factcheck-code_claude_opus.log`
- **Did it run `code/main.R`?** No.
- **What it did instead:** listed `code/`, `data/`, and `paper/exhibits/`; counted lines in `paper.tex`; wrote a report from static inspection.

Again, there is no logged command invoking `Rscript code/main.R`.

### Iteration 10

- **Author plan time:** 2026-04-02 04:44:09 EDT
- **factcheck-code start:** 2026-04-02 04:47:27 EDT
- **Log:** `20260402T044727.276518-0400_factcheck-code_claude_opus.log`
- **Did it run `code/main.R`?** No.
- **What it did instead:** listed directories, grepped `paper.tex`, checked `R` / `Rscript`, and verified that `DBI` and `RPostgres` loaded.

This run still did not execute the pipeline. It diagnosed only the split-adjustment issue and still claimed credentials were unavailable.

### Iteration 11

- **Author plan time:** 2026-04-02 05:04:36 EDT
- **factcheck-code start:** 2026-04-02 05:09:28 EDT
- **Log:** `20260402T050928.548716-0400_factcheck-code_claude_opus.log`
- **Did it run `code/main.R`?** No.
- **What it did instead:** listed directories, read `code/main.R`, checked `R --version`, inspected installed packages, and read the WRDS example script.

This is the first saved Ralph run that reported the SQL/date-join bug, but it still did so without actually running `code/main.R`.

## Sequence summary

Across Iterations 8, 9, 10, and 11:

- `factcheck-code` did **not** run `code/main.R`.
- Iteration 8 did not run it.
- Iteration 9 did not run it.
- Iteration 10 did not run it.
- Iteration 11 still did not run it.

The difference across these iterations was not whether the pipeline was executed. The difference was only what the agent inferred from static inspection.
