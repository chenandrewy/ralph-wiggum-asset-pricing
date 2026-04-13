# tests/factcheck-code.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 1m 48s
[ralph-garage/agent-logs/20260412T201203.489833-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.489833-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and paper claims are consistent with the code.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`). Produces three exhibits:

1. `paper/exhibits/table-pd-ratios.tex` — P/D ratio table (Exhibit 2)
2. `paper/exhibits/fig-extension-panels.pdf` — Extension panels figure (Exhibit 3)
3. `paper/exhibits/fig-ai-valuations.pdf` — AI valuations figure (Exhibit 1)

Additionally prints veto example computations referenced in Section 4.1 to console.

Dependencies: R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. External data downloaded at runtime from datahub.io (Shiller S&P 500) and FRED (NASDAQ index). No local data files, precomputed caches, or manually prepared intermediates are used.

## Execution status

- **Executed successfully from scratch.** All three exhibits regenerated. Runtime well under 180 seconds.
- Two external downloads completed (datahub.io Shiller dataset, FRED NASDAQ series). These are required by the canonical path and permitted by the spec ("including any external data download").
- R and all required packages were available in the environment.
- No credentials or authentication required.

## Paper-code consistency

All checked quantitative claims match the code:

| Paper claim | Code/output verification |
|---|---|
| p=0.5%, ξ=0: AI P/D ≈ 15.5, Non-AI ≈ 11, ratio ≈ 1.4 | Table: 15.5, 11.1, 1.4 |
| p=1%, ξ=0: ratio ≈ 2 | Table: 2.0 |
| Baseline φ(1+η) = 0.75 | 0.50 × 1.50 = 0.75 |
| Large singularity φ(1+η) = 0.5 | 0.05 × 10 = 0.5 |
| φ^{-γ} = 160,000 for large singularity | 0.05^{-4} = 160,000 |
| Veto example: γ=10, p=1%, κ=1%, household vetoes under incomplete markets | V_develop = -15.53, V_veto = -15.32, VETO |
| Complete markets: household develops | V_develop_CM = -13.46 > V_veto = -15.32, develop |
| δ=0.9, τ=0.30: net transfer rate 0.219, consumption multiple ≈ 3.5× | τ(1-δτ) = 0.219; growth ≈ 3.52 |
| Parameters in table footnote match code globals | β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 |
| Extension figure uses α=0.70, p=0.5%, ξ=5%, δ=0.5 | Code: alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50 |

Model formulas in the code (SDF construction, backward recursion for AI P/D, consumption growth with transfers, φ_eff, veto Bellman equations) are consistent with the paper's equations.

The empirical figure (fig-ai-valuations) uses S&P 500 P/D from Shiller data and NASDAQ/S&P price ratio normalized to Jan 2015 = 100. No per-share data is combined with share counts from different sources; all quantities are index-level.

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | Locally reproducible (pure computation) |
| `fig-extension-panels.pdf` | Locally reproducible (pure computation) |
| `fig-ai-valuations.pdf` | Locally reproducible with network access (downloads from datahub.io and FRED) |
| Veto example (Section 4.1 in-text) | Locally reproducible (console output; not saved to file) |
| All theoretical propositions and proofs | Not code-dependent (analytical derivations in LaTeX) |
