# tests/factcheck-code.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 1m 34s
[ralph-garage/agent-logs/20260409T212047.311942-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.311942-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and is consistent with the paper's quantitative claims.

## Canonical local analysis path

- **Entry point**: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`)
- **Dependencies**: R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`
- **External data**: Downloads S&P 500 data from datahub (Shiller dataset) and NASDAQ data from FRED. No credentials required.
- **Outputs** (all to `paper/exhibits/`):
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — Two-panel extension figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — AI valuations vs. market figure (Exhibit 3)
- All three outputs are referenced in `paper/paper.tex`; no unused exhibit files exist.
- Single canonical entry point satisfies spec requirement III.3.b.

## Execution status

- **Status**: Successfully executed from scratch in this environment.
- **Runtime**: Well under the 180-second spec limit (III.3.d).
- **From-scratch compliance**: The script downloads all external data at runtime and computes all model outputs from parameters. No precomputed caches or intermediate files are used (III.3.c). The `data/` directory is empty, confirming no hidden local inputs.
- **Warnings**: Two benign ggplot warnings about removed rows outside scale range (expected: the large-singularity P/D line is clipped in Panel A).

## Paper-code consistency

### Parameters
All parameters in the code match the paper's stated values:

| Parameter | Code | Paper | Match |
|-----------|------|-------|-------|
| beta | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| gamma | 4 | 4 | Yes |
| phi | 0.50 | 0.5 | Yes |
| eta | 0.50 | 0.5 | Yes |
| theta | 0.15 | 0.15 | Yes |
| dtheta | 0.20 | 0.2 | Yes |
| phi_large | 0.05 | 0.05 | Yes |
| alpha0 | 0.70 | 0.70 | Yes |
| delta | 0.50 | 0.5 | Yes |
| p_ext | 0.005 | 0.5% | Yes |
| xi_ext | 0.05 | 5% | Yes |

### P/D formula
The code's `compute_pd` function implements K/(1-K) where K = beta*(1+g)^(1-gamma)*[(1-p) + p*(1-xi)*phi^(-gamma)*(1+eta)^(-gamma)*gamma_j]. This matches the paper's equations (3)-(4) exactly.

### Table claims verified against generated output
- Paper: "P/D of roughly 18, non-AI near 11, ratio about 1.6" at p=0.5%, xi=0 -> Table: 17.5 / 11.1 / 1.6. Consistent.
- Paper: "At p=1%, ratio rises to nearly 6 to 1" -> Table: 76.4 / 13.3 / 5.8. Consistent.

### Extension figure claims
- Paper: "phi(1+eta) = 0.75, household consumption falls by 25%" -> 0.5*1.5 = 0.75. Correct.
- Paper: "phi(1+eta) = 0.5, consumption halves under large singularity" -> 0.05*10 = 0.5. Correct.
- Paper: "phi^{-gamma} = 160,000" -> 0.05^(-4) = 160,000. Correct.
- Code's `consumption_growth` and `compute_pd_with_transfer` functions match paper equations (8) and the phi_eff definition.
- Paper's claim that the transfer ratio (eq. 9) is independent of eta is verified: the code's consumption_growth divided by phi*(1+eta) yields 1 + tau*(1-delta*tau)*(1-phi*alpha)/(phi*alpha), which cancels eta.

### Empirical figure
- Paper describes "Monthly closing prices for the NASDAQ Composite and the S&P 500, normalized to January 2015 = 100." The code downloads these two series, normalizes to the first common month = 100, and plots them. Consistent.
- Per-share data concern (Requirement 5): Not applicable. The code uses index-level price data, not per-share quantities combined with share counts.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` | Locally reproducible (model computation, no external data needed) |
| `fig-extension-panels.pdf` | Locally reproducible (model computation, no external data needed) |
| `fig-ai-valuations.pdf` | Locally reproducible (downloads public data from FRED/datahub at runtime; no credentials needed) |
| All paper quantitative claims | Consistent with code outputs |

No violations found.
