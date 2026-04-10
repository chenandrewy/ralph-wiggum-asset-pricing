# tests/factcheck-code.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 1m 58s
[ralph-garage/agent-logs/20260409T203927.588151-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.588151-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical local analysis path

- **Single entry point**: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`).
- **Outputs**: Three exhibits directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — Extension two-panel figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — AI valuations vs. market figure (Exhibit 3)
- **External data**: Downloads NASDAQ from FRED and S&P 500 from the datahub Shiller dataset at runtime. No precomputed caches or manually prepared intermediates.
- **Dependencies**: R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.
- **Per-share data**: Not applicable. The code uses index-level price data (NASDAQ Composite, S&P 500 index), not per-share quantities. No share-count or split-adjustment issues arise.

## Execution status

| Step | Status |
|---|---|
| Full pipeline from scratch | **Succeeded** (all three exhibits regenerated) |
| Runtime | Well under 180 seconds |
| Network downloads (FRED, datahub) | Completed successfully |
| R and required packages | Available in this environment |

No execution blockers. The pipeline ran end-to-end with one benign ggplot warning (1 row removed from a capped y-axis in Panel A of the extension figure, which is intentional).

## Paper-code consistency

| Paper claim | Code/table value | Status |
|---|---|---|
| Parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2 | Matches lines 18-24 of code | Consistent |
| phi(1+eta)=0.75, household consumption falls 25% | 0.5*1.5=0.75 | Consistent |
| phi_large(1+eta_large)=0.5, consumption halves | 0.05*10=0.5 | Consistent |
| p=0.5%, xi=0%: AI P/D "roughly 18", non-AI "near 11", ratio "about 1.6" | Table: 17.5, 11.1, 1.6 | Consistent |
| p=1%: ratio "nearly 6 to 1" | Table: 5.8 | Consistent |
| P/D ratios 1.5-6x across p=0.5%-1% | Table range: 1.4-5.8 | Consistent |
| phi_large^(-gamma) = 160,000 | 0.05^(-4) = 160,000 | Consistent |
| Catastrophe markers: 50% loss (large), 25% loss (baseline) at tau=0 | Code annotations match | Consistent |
| Extension params: alpha=0.70, p=0.5%, xi=5%, delta=0.5 | Code lines 108-109, 127-128 | Consistent |
| P/D formula uses phi_eff = phi + tau(1-delta*tau)(1-phi*alpha)/alpha | Code line 119 | Consistent |
| Gamma^AI = [theta+dtheta(1-theta)]/theta * (1+eta) | Code lines 34-37 | Consistent |
| NASDAQ from FRED; S&P 500 from Shiller dataset (as stated in figure caption) | Code lines 254-264 | Consistent |

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` (P/D ratio table) | **Locally reproducible** — pure computation from parameters |
| `fig-extension-panels.pdf` (extension panels) | **Locally reproducible** — pure computation from parameters |
| `fig-ai-valuations.pdf` (valuations figure) | **Locally reproducible** — downloads data at runtime from public sources (FRED, datahub) |
| Propositions 1-3 and proofs | Not code-dependent; theoretical derivations in LaTeX |

All paper outputs are reproducible from the canonical local analysis path. No exhibits are external, nonlocal, or non-canonical. The pipeline satisfies the spec's requirement of a single canonical entry point that regenerates every exhibit from scratch.
