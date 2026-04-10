# tests/factcheck-code.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260409T202148.445952-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.445952-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all three exhibits, and its logic and outputs are consistent with the paper's formulas, parameters, and quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`). Generates all three exhibits used in `paper/paper.tex`:

1. `paper/exhibits/table-pd-ratios.tex` — Exhibit 1 (P/D ratio table)
2. `paper/exhibits/fig-extension-panels.pdf` — Exhibit 2 (government transfers two-panel figure)
3. `paper/exhibits/fig-ai-valuations.pdf` — Exhibit 3 (NASDAQ vs S&P 500 time series)

No other code files exist under `code/`. The `data/` directory is empty; all data is downloaded at runtime. No precomputed caches or intermediate files are used.

## Execution status

- **Execution result**: All three exhibits generated successfully with no errors.
- **Runtime**: Well under 180 seconds.
- **Network access**: Required for Exhibit 3 (downloads NASDAQ from FRED, S&P 500 from Shiller/datahub). This is compatible with the spec, which explicitly allows external data downloads within the canonical pipeline.
- **R packages used**: ggplot2, dplyr, tidyr, gridExtra, scales. All available in this environment. No undocumented dependencies.

## Paper-code consistency

### Parameters (all match)
| Parameter | Code | Paper (Section 3) |
|-----------|------|--------------------|
| beta | 0.96 | 0.96 |
| g | 0.02 | 0.02 |
| gamma | 4 | 4 |
| phi | 0.50 | 0.5 |
| eta | 0.50 | 0.5 |
| theta | 0.15 | 0.15 |
| dtheta | 0.20 | 0.2 |
| phi_large | 0.05 | 0.05 |
| eta_large | 9 | 9 |
| alpha | 0.70 | 0.70 |
| delta | 0.50 | 0.5 |
| p_ext | 0.005 | 0.5% |
| xi_ext | 0.05 | 5% |

### Formulas (all match)

- **Gamma^AI**: Code computes `(theta + dtheta*(1-theta))/theta * (1+eta)`, matching Proposition 1's definition.
- **P/D ratio**: Code computes `K/(1-K)` where `K = beta*(1+g)^(1-gamma)*[(1-p) + p*(1-xi)*phi^(-gamma)*(1+eta)^(-gamma)*Gamma_j]`, matching equations (4)-(5).
- **Existence condition**: Code returns NA when K >= 1, consistent with Remark 1.
- **Effective phi**: Code computes `phi + tau*(1-delta*tau)*(1-phi*alpha)/alpha`, matching the paper's phi_eff definition.
- **Consumption growth**: Code computes `phi*(1+eta) + tau*(1-delta*tau)*(1-phi*alpha)/alpha*(1+eta)`, consistent with equation (7) normalized by the pre-singularity household consumption.

### Quantitative claims (all match)

- Paper: "AI stocks trade at a P/D of roughly 18" at p=0.5%, xi=0%. Table: 17.5. Consistent.
- Paper: "non-AI stocks trade near 11". Table: 11.1. Consistent.
- Paper: "a ratio of about 1.6". Table: 1.6. Exact match.
- Paper: "At p=1%, the ratio rises to nearly 6 to 1". Table: 5.8. Consistent.
- Paper: "consumption halves under the large singularity (phi(1+eta) = 0.5)". Code: 0.05*10 = 0.5. Exact match.
- Paper: "falls by 25% under the baseline (phi(1+eta) = 0.75)". Code: 0.5*1.5 = 0.75. Exact match.
- Paper: "phi^{-gamma} = 160,000". Code: 0.05^(-4) = 160,000. Exact match.

### Exhibit 3 data sources
- Paper caption: "NASDAQ from FRED; S&P 500 from the Shiller dataset." Code downloads NASDAQCOM from FRED and S&P 500 from datahub's Shiller dataset. Consistent.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| Exhibit 1 (table-pd-ratios.tex) | Locally reproducible |
| Exhibit 2 (fig-extension-panels.pdf) | Locally reproducible |
| Exhibit 3 (fig-ai-valuations.pdf) | Locally reproducible (requires network for data download, which is part of the canonical path per spec) |
| All theoretical propositions and proofs | Not code-dependent; analytic derivations in paper |
| All parameter claims in Section 3 | Locally reproducible; match code parameters exactly |

No per-share data issues: the code uses only index-level price series (NASDAQ Composite, S&P 500), normalized to a common base date. No share counts or per-share adjustments are involved.

No violations found.
