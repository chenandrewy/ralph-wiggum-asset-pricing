# tests/factcheck-code.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260402T214942.812068-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.812068-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces both exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical local analysis path

- **Entry point:** `code/run-all.R` (invoked via `Rscript code/run-all.R`).
- **Scripts (in order):**
  1. `code/numerical-illustration.R` — generates `paper/exhibits/numerical-illustration.tex` (Table 1 / Exhibit 2). No external dependencies.
  2. `code/ai-valuations-figure.R` — generates `paper/exhibits/ai-valuations.pdf` (Figure 1 / Exhibit 1). Requires WRDS credentials (`WRDS_USERNAME`, `WRDS_PASSWORD`).
- **Outputs:** Both files land directly in `paper/exhibits/` in the correct format for `paper.tex`, satisfying spec III.3.f.
- The pipeline has no intermediate files, no manual steps, and no precomputed caches (spec III.3.c).

## Execution status

| Script | Status | Notes |
|---|---|---|
| `numerical-illustration.R` | Ran successfully | Pure computation, no external deps |
| `ai-valuations-figure.R` | Ran successfully | Connected to WRDS, retrieved 168 rows, wrote PDF |

Both scripts executed end-to-end in this environment. The full pipeline completes within the 180-second budget (spec III.3.d).

## Paper-code consistency

### Numerical illustration (Table 1)

Paper text (Section 3, "Numerical illustration" paragraph) states:
- At p = 0.01: V0_A ~ 16.1, V0_N ~ 11.6, ratio ~ 1.4, V0_A_CM ~ 12.9, hedging premium ~ 25%.
- At p = 0: both equal ~ 11.9.

Code output confirms: V0_A = 16.1, V0_N = 11.6 (ratio 1.39), V0_A_CM = 12.9, hedging premium = 24.8%. At p = 0, both = 11.9. All claims match.

Parameters in code match those stated in the paper: beta = 0.96, gamma = 3, g = 0.02, g_tilde = 0.05, theta = 0.05, theta_tilde = 0.15, nu = 0.55, nu_tilde = 0.30.

The code formulas (R, Phi_A, Phi_N, V1, V0_A, V0_N, V0_A_CM) correctly implement equations (7)-(11) from the paper.

### Empirical figure (Figure 1)

- Paper caption: "Price-dividend ratios for AI stocks (NVDA, MSFT, GOOGL, META, AMZN) versus the rest of the CRSP universe, computed using trailing 12-month dividends."
- Code queries exactly these five tickers from `crsp.stocknames`, computes trailing 12-month dividends from `crsp.msedist`, and plots portfolio-level P/D ratios. Consistent.

### Per-share data handling (Requirement 5)

The CRSP query computes total dividends as `SUM(mcap / prc * divamt)`, which simplifies to `SUM(shrout * divamt)`. Both `shrout` and `divamt` come from CRSP (msf and msedist respectively), which maintains internally consistent split adjustment. The join is at monthly frequency (end-of-month shrout matched to same-month ex-date dividends), introducing at most minor within-month timing noise. For an illustrative figure (spec IV.8.b, IV.8.d), this is appropriate.

### Minor cosmetic issue

The R code labels the table comment as `% Exhibit 1`, while the paper treats the table as Exhibit 2 (the figure is Exhibit 1). This is a comment-only discrepancy with no effect on compilation or output.

## Reproducibility classification

| Paper object | Classification |
|---|---|
| Table 1 (numerical illustration) | **Locally reproducible** — runs from scratch with no external dependencies |
| Figure 1 (AI valuations) | **Blocked by credentials** — requires WRDS access; ran successfully in this environment with credentials present |
| All theoretical propositions/proofs | Not code-dependent; derivations are in the paper text |

No paper output is mislabeled as locally reproducible when it is not. The WRDS dependency is documented in run-all.R's header comment and is part of the canonical pipeline as required by spec III.3.e.
