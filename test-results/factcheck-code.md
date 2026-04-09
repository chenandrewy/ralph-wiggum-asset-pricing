# tests/factcheck-code.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260409T182005.674550-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.674550-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and is consistent with the paper's formulas and quantitative claims.

## Canonical local analysis path

- Single entry point: `code/generate-exhibits.R`
- Run command: `Rscript code/generate-exhibits.R`
- No external inputs: all parameters defined inline; no data downloads, no WRDS queries, no credentials
- Produces 3 exhibits directly to `paper/exhibits/`:
  - `table-pd-ratios.tex` (Exhibit 1: P/D ratio table)
  - `fig-extension-panels.pdf` (Exhibit 2: government transfers two-panel figure)
  - `fig-ai-valuations.pdf` (Exhibit 3: illustrative AI vs market valuations)
- All 3 exhibits are referenced in `paper/paper.tex`; no unused exhibits in the directory
- Dependencies: R with `ggplot2`, `dplyr`, `tidyr`, `gridExtra` (all standard CRAN packages)
- The code structure is logically organized: parameters, then exhibits 1–3 in sequence

## Execution status

- **Executed successfully from scratch** in this environment
- Runtime: well under 180 seconds (spec requirement III.3.d)
- All 3 output files regenerated with correct content
- No precomputed caches or intermediate files required (spec requirement III.3.c satisfied)

## Paper-code consistency

### Formulas
- **P/D ratios (Proposition 1):** Code implements Γ^AI, Γ^N, and the K/(1-K) formula exactly as in equations (4)–(5). Verified by static comparison.
- **Transfer consumption (eq. 6):** Code's `consumption_growth()` function computes c^H_post / c^H_pre = φ(1+η) + τ(1-δ₀τ)(1-φα)/α · (1+η), consistent with equation (6) divided by pre-singularity household consumption.
- **P/D with transfers:** Code computes an effective φ_eff that correctly incorporates the transfer into the household's SDF.

### Parameters
- Paper states: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2. Code matches exactly.
- Extension uses p=3%, ξ=5%, α₀=0.70, δ₀=0.50, η∈{0.5, 9.0}. These are in the code and consistent with the paper's discussion.

### Quantitative claims
- "P/D of roughly 18" at p=0.5%, ξ=0%: table shows 17.5. Consistent with "roughly."
- "ratio rises to nearly 6 to 1" at p=1%: table shows 5.8. Consistent with "nearly 6."
- "household consumption falls to 75%": φ(1+η) = 0.5×1.5 = 0.75. Exact match.
- "two to six times higher across a range of singularity probabilities": table ratios range 1.1–5.8; the stated range is approximate and refers to the salient region (p ≥ 0.5%), which is reasonable.
- Extinction compresses the AI premium: confirmed across all ξ columns in the table.

### Illustrative figure (Exhibit 3)
- Uses hardcoded approximate P/E data for AI-exposed firms vs. S&P 500, 2015–2025.
- Paper caption labels it "(Illustrative)" and text says "approximate values from public sources."
- This is appropriate: spec requirement I.8.b calls for limited empirical content that is illustrative.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` (Exhibit 1) | **Locally reproducible** — regenerated from scratch |
| `fig-extension-panels.pdf` (Exhibit 2) | **Locally reproducible** — regenerated from scratch |
| `fig-ai-valuations.pdf` (Exhibit 3) | **Locally reproducible** — uses hardcoded illustrative data, labeled as such in the paper |

## Per-share data handling (Requirement 5)

Not applicable. The code works entirely with model-derived ratios and shares (θ, α, φ), not with per-share market data from different sources. No share-count or split-adjustment issues arise.

## Violations

None found.
