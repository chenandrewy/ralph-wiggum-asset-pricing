# tests/factcheck-code.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 2m 19s
[ralph-garage/agent-logs/20260402T215920.395380-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T215920.395380-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: FAIL
REASON: The CRSP figure code combines per-share dividends with month-end shares outstanding without verifying split-adjustment consistency, violating Requirement 5.

## Canonical local analysis path

The canonical entry point is `code/run-all.R`, which runs two scripts in order:

1. `code/numerical-illustration.R` — generates `paper/exhibits/numerical-illustration.tex` (Table 1 / Exhibit 2). No external dependencies; parameters are hardcoded from the paper's Section 3.
2. `code/ai-valuations-figure.R` — generates `paper/exhibits/ai-valuations.pdf` (Figure 1 / Exhibit 1). Requires WRDS credentials to query CRSP data.

Both scripts output directly to `paper/exhibits/`. The pipeline is coherent, logically organized, and satisfies spec requirements III.3.a–g (R code, single entry point, from-scratch execution, outputs to exhibits, no precomputed caches, WRDS query in the canonical path, under 180 seconds).

## Execution status

- **numerical-illustration.R**: Executed successfully. Locally reproducible.
- **ai-valuations-figure.R**: Executed successfully with WRDS credentials present in this environment. In environments without WRDS credentials, this script fails with `stop()`, and `run-all.R` also fails. The `run-all.R` header comment ("If WRDS credentials are unavailable, the numerical table is still generated") is misleading: the table file exists only because it runs first, but the pipeline itself exits with an error.
- **Full pipeline (`run-all.R`)**: Completed successfully in this environment. All exhibits regenerated from scratch.

## Paper-code consistency

### Numerical illustration (Table 1)

Parameters in code match the paper exactly: beta=0.96, gamma=3, g=0.02, g_tilde=0.05, theta=0.05, theta_tilde=0.15, nu=0.55, nu_tilde=0.30.

Code output matches every numerical claim in the paper:
- V0_A approx 16.1 at p=0.01: **matches** (code: 16.1)
- V0_N approx 11.6 at p=0.01: **matches** (code: 11.6)
- Ratio "roughly 1.4": **matches** (16.1/11.6 = 1.39)
- Both approx 11.9 at p=0: **matches** (code: 11.9)
- V0_A_CM approx 12.9: **matches** (code: 12.9)
- Hedging premium "about 25%": **matches** (code: 24.8%)

The formulas in the code (`V0_A`, `V0_N`, `Phi_A`, `Phi_N`, `V1`, complete-markets variant) are faithful implementations of equations (7)–(12) in the paper.

### CRSP figure (Figure 1)

The figure queries CRSP for monthly prices and dividends, computes trailing 12-month P/D ratios for AI stocks (NVDA, MSFT, GOOGL, META, AMZN) versus the rest of the CRSP universe, consistent with the paper's caption and description.

**Per-share data violation (Requirement 5):** The SQL query computes total dividends as `mcap / prc * divamt`, which is effectively `shrout * divamt`. Here `shrout` comes from `crsp.msf` (month-end shares outstanding) and `divamt` comes from `crsp.msedist` (per-share dividend on the ex-date). These quantities have different timing: shrout is end-of-month while divamt is as of the ex-date. If a stock split occurs between the ex-date and month-end (e.g., NVDA's 10-for-1 split in June 2024), post-split shrout would be multiplied by pre-split divamt, overstating dividends by the split factor. The code does not verify, document, or adjust for this timing mismatch.

### Exhibit label mismatch

The generated file `numerical-illustration.tex` contains the comment `% Exhibit 1` on the label line, but `paper.tex` marks the table as `% Exhibit 2` and the figure as `% Exhibit 1`. This is a cosmetic inconsistency in the code-generated comment.

## Reproducibility classification

| Paper object | Classification |
|---|---|
| Table 1 (numerical illustration) | **Locally reproducible** — runs from scratch with no external dependencies; output matches paper claims exactly |
| Figure 1 (AI valuations, CRSP) | **Blocked by credentials** in environments without WRDS access; **locally reproducible** in this environment but with a per-share data handling defect |
| All theoretical results (Propositions 1–4, Remarks 1–2) | Not code-dependent; analytic derivations in the paper |

## Violations

1. **Requirement 5 (per-share data handling):** The CRSP query combines month-end `shrout` from `crsp.msf` with per-share `divamt` from `crsp.msedist` without verifying split-adjustment consistency. Stock splits that occur between the dividend ex-date and month-end cause the product to be incorrect.
2. **Minor: Exhibit label comment mismatch** in generated `numerical-illustration.tex` (`% Exhibit 1` should be `% Exhibit 2`).
3. **Minor: Misleading `run-all.R` comment** about graceful degradation without WRDS credentials — the pipeline fails, it just happens that the table was already written.
