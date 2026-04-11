# tests/factcheck-code.py
Started: 2026-04-11 15:12:18 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260411T151218.770486-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T151218.770486-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path is coherent, runs from scratch, and all code outputs match the paper's quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`. Run via `Rscript code/generate-exhibits.R`. Produces three outputs directly into `paper/exhibits/`:

1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1 / Table 1)
2. `fig-extension-panels.pdf` — Government transfers figure (Exhibit 2 / Figure 2)
3. `fig-ai-valuations.pdf` — AI valuations vs. market figure (Exhibit 3 / Figure 1)

Additionally prints the veto numerical example (Section 4.1) to console.

Dependencies: R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. No local data files required; the `/workspace/data/` directory is empty. The empirical figure downloads S&P 500 data from datahub (Shiller dataset) and NASDAQ data from FRED at runtime.

## Execution status

**Fully executed.** The canonical pipeline ran from scratch in this environment within the 180-second spec limit. All three exhibit files were regenerated. The veto computation printed correct qualitative results to console.

- R and all required packages were available.
- Network downloads (FRED, datahub) succeeded.
- Warnings about removed rows in ggplot are expected (axis-limit clipping in the extension figure).

## Paper-code consistency

### Parameters
All parameters match between `paper.tex` and `generate-exhibits.R`:

| Parameter | Paper | Code | Match |
|-----------|-------|------|-------|
| β | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| γ (table) | 4 | 4 | Yes |
| φ | 0.5 | 0.5 | Yes |
| η | 0.5 | 0.5 | Yes |
| θ | 0.15 | 0.15 | Yes |
| Δθ | 0.2 | 0.2 | Yes |
| φ_large | 0.05 | 0.05 | Yes |
| η_large | 9 | 9 | Yes |
| α | 0.70 | 0.70 | Yes |
| δ | 0.5 | 0.5 | Yes |
| p (extension fig) | 0.5% | 0.005 | Yes |
| ξ (extension fig) | 5% | 0.05 | Yes |
| γ (veto) | 10 | 10 | Yes |
| p (veto) | 1% | 0.01 | Yes |
| κ (veto) | 1% | 0.01 | Yes |
| q (veto) | 0.70 | 0.70 | Yes |

### Quantitative claims verified

- **Table 1**: Paper states "AI stocks trade at a P/D of about 15.5" at p=0.5%, ξ=0%. Table output: 15.5. Paper states ratio "rises to 2" at p=1%. Table output: 2.0. Confirmed.
- **φ(1+η) = 0.75** (baseline): 0.5 × 1.5 = 0.75. Paper says "household consumption falls by 25%." Confirmed.
- **φ_large(1+η_large) = 0.5**: 0.05 × 10 = 0.5. Paper says "consumption halves under the large singularity." Confirmed.
- **φ^{-γ} = 160,000**: 0.05^{-4} = 160,000. Paper cites this value in discussing the divergence of the pricing sum. Confirmed.
- **Veto example**: Code output shows V_veto > V_develop under incomplete markets (VETO), V_develop > V_veto under complete markets (develop). Paper claims the same qualitative result. Confirmed.

### Formula verification

- **P/D formulas** (Propositions 1): The code's `compute_pd_approx` and `compute_pd_ai_exact` implement the closed-form and backward-recursion versions of the Euler equation. The SDF term `phi^{-γ} × (1+η)^{-γ} × Γ^j` matches the paper's eq. (3)–(4).
- **Consumption growth** with transfers: Code's `consumption_growth()` matches paper eq. (9): φ(1+η) + τ(1−δτ)(1−φα)/α × (1+η).
- **Effective displacement** φ_eff: Code matches paper eq. (10): φ + τ(1−δτ)(1−φα)/α.
- **Dividend growth factors**: Γ^AI = [θ + Δθ(1−θ)]/θ × (1+η) and Γ^N = [1−θ−Δθ(1−θ)]/(1−θ) × (1+η) match the paper's definitions.

### Per-share data (Requirement 5)
Not applicable. The empirical figure uses index-level prices (NASDAQ Composite, S&P 500) normalized to a base date. No per-share quantities or share counts are combined.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| table-pd-ratios.tex | Locally reproducible |
| fig-extension-panels.pdf | Locally reproducible |
| fig-ai-valuations.pdf | Locally reproducible (requires network for FRED/datahub download) |
| Veto numerical example (console) | Locally reproducible |
| Theoretical propositions | Pure math; not code-dependent |

No violations found. The canonical path is a single R script that regenerates all exhibits from scratch, downloads empirical data at runtime, and produces outputs consistent with every quantitative claim checked in the paper.
