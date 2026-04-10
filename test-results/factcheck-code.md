# tests/factcheck-code.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 1m 50s
[ralph-garage/agent-logs/20260409T210608.982511-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.982511-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and is fully consistent with the paper's formulas, parameters, and quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`). Produces three exhibits directly into `paper/exhibits/`:

1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
2. `fig-extension-panels.pdf` — two-panel extension figure (Exhibit 2)
3. `fig-ai-valuations.pdf` — AI valuations vs. market (Exhibit 3)

All three are referenced in `paper/paper.tex`. No other files exist in `paper/exhibits/`. The `data/` directory is empty; all data is downloaded at runtime (NASDAQ from FRED, S&P 500 from Shiller/datahub). No precomputed caches or intermediate files.

## Execution status

- **Locally reproducible.** The pipeline ran from scratch in under 180 seconds, downloading external data and regenerating all exhibits. The regenerated `table-pd-ratios.tex` is byte-identical to the committed version.
- **Runtime dependencies:** R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. All available in the test environment.
- **Network dependencies:** Downloads from FRED and datahub. Required for the empirical figure (Exhibit 3). Consistent with spec III.3.d ("including any external data download").
- **Warnings:** Two cosmetic ggplot warnings about rows outside scale range in the extension panels figure (by design — the large-singularity P/D diverges near tau=0 and is intentionally capped).

## Paper-code consistency

### P/D formula (Proposition 1 vs. `compute_pd`)
The code computes `K = beta * (1+g)^(1-gamma) * [(1-p) + p*(1-xi) * phi^(-gamma) * (1+eta)^(-gamma) * Gamma_j]` and returns `K/(1-K)`. This matches equations (4)-(5) in the paper exactly.

### Dividend growth factors
- Code: `Gamma_AI = [(theta + dtheta*(1-theta))/theta] * (1+eta)` — matches paper definition.
- Code: `Gamma_N = [(1-theta - dtheta*(1-theta))/(1-theta)] * (1+eta)` — matches paper definition.

### Parameters
Code parameters match the paper's table footnote and text exactly: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.20.

### Extension figure parameters
Code: alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50, baseline (eta=0.5, phi=0.5), large singularity (eta=9.0, phi=0.05). All match paper text (Section 4.2).

### Transfer formulas
- `consumption_growth` computes `phi*(1+eta) + tau*(1-delta*tau)*(1-phi*alpha)/alpha * (1+eta)`, matching equation (8) divided by pre-singularity household consumption.
- `phi_eff = phi + tau*(1-delta*tau)*(1-phi*alpha)/alpha` matches the paper's effective displacement parameter.

### Numerical claims verified against table
- "P/D of roughly 18 ... near 11 ... ratio of about 1.6" at p=0.5%, xi=0: Table shows 17.5, 11.1, 1.6. Correct.
- "ratio rises to nearly 6 to 1" at p=1%: Table shows 5.8 at xi=0. Correct.
- "1.5 to 6 times higher" across 0.5-1% range: Table confirms 1.6 to 5.8. Correct.

### Arithmetic claims verified
- phi(1+eta) = 0.5*1.5 = 0.75 (paper: "household consumption falls by 25%"). Correct.
- Large singularity: phi(1+eta) = 0.05*10 = 0.5 (paper: "consumption halves"). Correct.
- phi^(-gamma) = 0.05^(-4) = 160,000 (paper text). Correct.

### Data sources
Paper caption: "NASDAQ from FRED; S&P 500 from the Shiller dataset." Code downloads NASDAQ via FRED API and S&P 500 from datahub Shiller CSV. Consistent.

## Reproducibility classification

| Output | Classification |
|---|---|
| table-pd-ratios.tex | Locally reproducible |
| fig-extension-panels.pdf | Locally reproducible |
| fig-ai-valuations.pdf | Locally reproducible (requires network for FRED/datahub download) |

All paper exhibits are reproducible from the canonical local analysis path. No violations found.
