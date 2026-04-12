# tests/factcheck-code.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 1m 55s
[ralph-garage/agent-logs/20260412T095842.947969-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.947969-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims and parameters.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`). It generates all three exhibits used in `paper/paper.tex`:

1. `paper/exhibits/table-pd-ratios.tex` — P/D ratio table (Exhibit 2)
2. `paper/exhibits/fig-extension-panels.pdf` — Extension two-panel figure (Exhibit 3)
3. `paper/exhibits/fig-ai-valuations.pdf` — Empirical valuation figure (Exhibit 1)

Additionally, the script prints the veto numerical example (Section 4.1) to console.

Dependencies: R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. External data downloaded at runtime from datahub.io (Shiller S&P 500) and FRED (NASDAQ). No precomputed caches or intermediate files are used.

## Execution status

- **Executed successfully** in this environment with R 4.2.2.
- All three exhibit files were regenerated from scratch.
- External downloads (Shiller dataset, FRED NASDAQ) completed without error.
- Runtime was well under the 180-second spec limit.
- Minor ggplot warnings about removed rows (NA/out-of-range values in the extension figure) are expected behavior from axis limits and do not affect correctness.

## Paper-code consistency

All verified consistent:

| Paper claim | Code | Status |
|---|---|---|
| Table params: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 | Lines 18–24 match exactly | ✓ |
| p=0.5%, ξ=0: AI P/D ≈ 15.5, Non-AI ≈ 11, ratio ≈ 1.4 | Table output: 15.5, 11.1, 1.4 | ✓ |
| p=1%, ξ=0: ratio rises to 2 | Table output: ratio = 2.0 | ✓ |
| AI P/D computed by Euler equation iteration (exact) | `compute_pd_ai_exact` uses 60-step backward recursion over theta chain | ✓ |
| Non-AI P/D in closed form (exact, since Γ^N = (1−Δθ)(1+η) is theta-independent) | `compute_pd_approx` used; confirmed exact because share_ratio_non = 1−Δθ = 0.8 is constant | ✓ |
| Veto example: φ=0.5, η=0.5, ξ=5%, p=1%, γ=10, α=0.70, q=0.70, κ=1% | Code lines 422–427 match exactly | ✓ |
| Household vetoes under incomplete markets | Code output: V_veto(−15.32) > V_develop(−15.53) | ✓ |
| Household does not veto under complete markets | Code output: V_develop_CM(−13.46) > V_veto(−15.32) | ✓ |
| Extension fig params: γ=4, α=0.70, p=0.5%, ξ=5%, δ=0.5 | Code lines 183–184, 140–141 match | ✓ |
| Baseline: η=0.5, φ=0.5; large: η=9, φ=0.05 | Code lines 186–194 match | ✓ |
| φ(1+η) = 0.75 baseline, 0.5 large singularity | 0.5×1.5=0.75, 0.05×10=0.5 | ✓ |
| φ^{−γ} = 160,000 for large singularity | 0.05^(−4) = 160,000 | ✓ |
| Transfer formula: φ_eff = φ + τ(1−δτ)(1−φα)/α | Code line 152 matches eq. (9) | ✓ |
| Consumption growth formula matches eq. (7) | Code `consumption_growth` function matches | ✓ |
| In-text δ=0.9 illustration: τ=0.30 yields 3.5× consumption multiple | Manual verification: 0.05×10 + 0.219×(0.965/0.70)×10 ≈ 3.52 | ✓ |

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | **Locally reproducible** — pure computation, no external data |
| `fig-extension-panels.pdf` | **Locally reproducible** — pure computation, no external data |
| `fig-ai-valuations.pdf` | **Locally reproducible with network** — requires downloads from datahub.io and FRED; executed successfully in this run |
| Veto numerical example (console) | **Locally reproducible** — pure computation |
| All in-text quantitative claims checked | **Consistent with code** |

## Per-share data handling

The empirical exhibit uses index-level S&P 500 data (Shiller) and the NASDAQ Composite index (FRED). P/D is computed as index level divided by trailing dividend, both at the index level. The NASDAQ/S&P ratio is a price-index ratio. No per-share quantities or share counts are involved, so no split-adjustment or timing issues arise.

## Code structure

The script is logically organized into clearly labeled sections (parameters, Exhibit 1 table, Exhibit 2 extension figure, Exhibit 3 empirical figure, veto computation). Helper functions are appropriately scoped. The single-file structure is appropriate for the scope of the analysis.
