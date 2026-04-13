# tests/factcheck-code.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 2m 29s
[ralph-garage/agent-logs/20260412T200023.666091-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.666091-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`. The script:

1. Computes Table 1 (`table-pd-ratios.tex`) via backward recursion over post-singularity states (AI stocks) and closed-form (non-AI stocks).
2. Generates Figure 3 (`fig-extension-panels.pdf`): two-panel extension figure (AI P/D vs. tax rate; household consumption growth vs. tax rate).
3. Downloads S&P 500 (Shiller/datahub) and NASDAQ (FRED) data, then generates Figure 1 (`fig-ai-valuations.pdf`): two-panel empirical valuation figure.
4. Prints veto example computations (Section 4.1) to console.

All three exhibit files are output to `paper/exhibits/` and are the only files in that directory. All three are referenced in `paper/paper.tex`. No hidden intermediate files or caches are required.

## Execution status

- **Executed successfully** in this environment with R and required packages (ggplot2, dplyr, tidyr, gridExtra, scales).
- External data downloads (datahub.io for Shiller S&P 500, FRED for NASDAQ) completed without error.
- Runtime well under 180 seconds.
- Minor ggplot warnings about removed rows (expected: large-singularity P/D values go to infinity/NA at low tax rates, intentionally excluded from plot range).

## Paper-code consistency

All quantitative claims verified against code output:

| Paper claim | Code output | Status |
|---|---|---|
| P/D AI ≈ 15.5 at p=0.5%, ξ=0% | 15.5 | Match |
| P/D non-AI ≈ 11 at p=0.5%, ξ=0% | 11.1 | Match |
| Ratio ≈ 1.4 at p=0.5%, ξ=0% | 1.4 | Match |
| Ratio rises to 2 at p=1% | 2.0 (at ξ=0%) | Match |
| Extinction attenuates ratio | Ratio decreasing in ξ across all p | Match |
| Veto under incomplete markets (γ=10, p=1%) | V_veto=-15.32 > V_develop=-15.53 | Match |
| No veto under complete markets | V_develop=-13.46 > V_veto=-15.32 | Match |
| Consumption halves under large singularity (φ(1+η)=0.5) | 0.05×10 = 0.5 | Match |
| Baseline consumption falls 25% (φ(1+η)=0.75) | 0.5×1.5 = 0.75 | Match |
| δ=0.9 robustness: 3.5× at τ=0.30 | 3.52 | Match |
| Net transfer factor 0.219 at δ=0.9, τ=0.30 | 0.219 | Match |

Parameters in code match parameters stated in paper: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2, α=0.70, δ=0.5, φ_large=0.05.

Formula implementations verified by static inspection:
- P/D closed-form and exact backward recursion match paper equations (1)-(3).
- φ_eff formula matches paper equation (5).
- Consumption growth formula matches paper equation (4).
- Veto Bellman equations match paper Section 4.1 description.

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | **Locally reproducible** — pure computation, no external data |
| `fig-extension-panels.pdf` | **Locally reproducible** — pure computation, no external data |
| `fig-ai-valuations.pdf` | **Reproducible with network access** — requires downloads from datahub.io and FRED |
| Veto example (console output) | **Locally reproducible** — pure computation, referenced in-text but not an exhibit file |
| All in-text quantitative claims | **Consistent with code** — verified against code output |

Per-share data handling: The empirical figure uses S&P 500 price and dividend data from a single source (Shiller dataset), avoiding cross-source share count issues. The NASDAQ/S&P ratio uses index-level prices from FRED, which are already adjusted. No per-share quantity combinations from different sources.

No undocumented dependencies, no hidden auxiliary files, no precomputed caches required.
