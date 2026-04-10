# tests/factcheck-code.py
Started: 2026-04-09 22:04:35 EDT
Runtime: 2m 12s
[ralph-garage/agent-logs/20260409T220435.859367-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T220435.859367-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and is consistent with the paper's quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`. The script generates all three exhibits used in the paper:

1. `paper/exhibits/table-pd-ratios.tex` (Table 1 / Exhibit 1): P/D ratio grid.
2. `paper/exhibits/fig-extension-panels.pdf` (Figure 2 / Exhibit 2): Two-panel extension figure.
3. `paper/exhibits/fig-ai-valuations.pdf` (Figure 1 / Exhibit 3): NASDAQ vs S&P 500 normalized price chart.

The code downloads external data (S&P 500 from the Shiller/datahub dataset, NASDAQ from FRED) as part of the canonical pipeline. No precomputed local caches or intermediate files are required. The `data/` directory is empty and unused, consistent with a from-scratch execution model.

## Execution status

- **Full pipeline executed successfully** in this environment in under 30 seconds.
- R 4.2.2 is available; all required packages (`ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`) loaded without issue.
- Network downloads from FRED and datahub completed successfully.
- Two `geom_line` warnings about removed rows are benign (NA values from undefined P/D at extreme parameters, handled intentionally by the plotting code).
- All three output files were regenerated and written to `paper/exhibits/`.

## Paper-code consistency

All verified claims match:

| Paper claim | Code/output verification | Status |
|---|---|---|
| Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2 | Lines 18-24 of code match exactly | Consistent |
| phi(1+eta) = 0.75 (25% consumption loss) | 0.5 * 1.5 = 0.75 | Consistent |
| phi_large(1+eta_large) = 0.5 (50% loss) | 0.05 * 10 = 0.5 | Consistent |
| AI P/D ~16 at p=0.5%, xi=0% | Table output: 15.5 | Consistent |
| Non-AI P/D ~11 at p=0.5%, xi=0% | Table output: 11.1 | Consistent |
| Ratio ~1.4 at p=0.5% | Table output: 1.4 | Consistent |
| Ratio rises to 2 at p=1% | Table output: 2.0 (at xi=0%) | Consistent |
| P/D ratios 1.3-2x across p=0.5-1% | Table range: 1.3 to 2.0 | Consistent |
| phi^(-gamma) = 160,000 for phi=0.05, gamma=4 | 0.05^(-4) = 160,000 | Consistent |
| P/D undefined at tau=0 for large singularity | K_term = 1.59 >= 1, existence violated | Consistent |
| Transfers restore finite P/D | phi_eff increases with tau, K < 1 for tau >= 0.05 | Consistent |
| AI exact P/D via backward recursion over theta chain | Euler equation verified numerically (residual < 1e-10) | Consistent |
| Non-AI closed form is exact (Gamma^N theta-independent) | Gamma^N = (1-dtheta)(1+eta), no theta dependence | Consistent |
| Figure caption: NASDAQ from FRED, S&P 500 from Shiller | Code: `download_fred("NASDAQCOM")`, datahub Shiller CSV | Consistent |
| Extension figure parameters: alpha=0.70, p=0.5%, xi=5%, delta=0.5 | Code lines 140-141, 183-184 match | Consistent |
| Transfer ratio (eq 7) independent of eta | Algebraically confirmed from code formula | Consistent |

## Reproducibility classification

| Output | Classification |
|---|---|
| Table 1 (P/D ratios) | **Locally reproducible** -- pure computation, no external data needed |
| Figure 2 (extension panels) | **Locally reproducible** -- pure computation, no external data needed |
| Figure 1 (AI valuations) | **Locally reproducible with network access** -- requires downloading FRED and datahub CSV data; no credentials needed |
| Proposition 1 (closed-form P/D) | Not code-generated; theoretical derivation in paper. Code implements the exact backward recursion described in the appendix |
| Proposition 2 (comparative statics) | Not code-generated; theoretical derivation. Table values are consistent with stated comparative statics |
| Proposition 3 (veto) | Not code-generated; theoretical result. No code implementation expected |

### Per-share data handling (Requirement 5)

The empirical exhibit (Figure 1) uses index-level price data (NASDAQ Composite, S&P 500), not per-share quantities. No share counts are involved. No per-share mixing concern applies.

### Spec compliance

- **One canonical entry point** (spec III.3.b): Yes, `generate-exhibits.R`.
- **Runs from scratch** (spec III.3.c): Yes, no precomputed caches.
- **Executes in <180 seconds** (spec III.3.d): Yes, completed in ~30 seconds.
- **Outputs to paper/exhibits/** (spec III.3.e): Yes.
- **Written in R** (spec III.3.a): Yes.
- **All files in paper/exhibits/ used in paper** (spec III.1.d): Yes, all three are referenced.
