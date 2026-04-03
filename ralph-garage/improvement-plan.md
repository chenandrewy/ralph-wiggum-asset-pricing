# Improvement Plan
AUTHOR PLAN — 2026-04-02 22:53:34 EDT

**Date:** 2026-04-02
**Branch:** ralph/run
**Test results:** 12/16 pass, 4 fail. No referee outputs. Build succeeds.

## Current Failures

| Test | Issue |
|---|---|
| factcheck-bysection | Line 238: "shrinking fraction ω̃" is wrong — ω̃ is a fixed constant post-singularity, not shrinking |
| factcheck-code | `run-all.R` wraps CRSP script in `tryCatch`, silently skipping Exhibit 1 when WRDS credentials are absent. Spec requires the pipeline to run from scratch without relying on cached files |
| factcheck-freely | Exhibit 2 table headers use `V_0` notation; paper body uses `V_pre`. Inconsistency originates in `code/numerical-illustration.R` |
| factcheck-lit | `references.bib` lists `author = {Zhang, Lu}` for Zhang2019. Actual author is Miao Ben Zhang (USC Marshall), not Lu Zhang (Ohio State) |

## Plan

### 1. Fix "shrinking" wording (factcheck-bysection)

**File:** `paper/paper.tex`, line 238
**Change:** Replace "remains a shrinking fraction ω̃ of total output" with "remains a fixed fraction ω̃ of total output — smaller than ω, but constant" (or similar phrasing that conveys the share is permanently lower, not progressively declining).

### 2. Fix silent skip of Exhibit 1 (factcheck-code)

**File:** `code/run-all.R`
**Change:** Remove the `tryCatch` wrapper around the CRSP figure script. If WRDS credentials are unavailable, the pipeline should fail hard. Optionally, delete any stale `ai-valuations.pdf` before running the query so a missing exhibit is visible.

### 3. Fix V_0 → V_pre notation in table (factcheck-freely)

**File:** `code/numerical-illustration.R` (lines ~71, ~83)
**Change:** Replace `V_0` with `V_{\mathrm{pre}}` in the generated table column headers and notes, matching the paper body notation.

### 4. Fix Zhang2019 author (factcheck-lit)

**File:** `paper/references.bib`
**Change:** Replace `author = {Zhang, Lu}` with `author = {Zhang, Miao Ben}`.

## Overhaul Assessment

No overhaul needed. The model section is clean — all theory, arithmetic, and proofs pass verification (factcheck-theory, factcheck-bysection model section, quality-formalism all pass). The four failures are isolated fixes: one wording error, one code robustness issue, one notation inconsistency, and one bib metadata error.
