# tests/factcheck-code.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 2m 6s
[ralph-garage/agent-logs/20260412T154740.773298-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.773298-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and is consistent with the paper's quantitative claims.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`). Produces all three exhibits used in `paper/paper.tex`:

1. `paper/exhibits/table-pd-ratios.tex` — P/D ratio table (Exhibit 2)
2. `paper/exhibits/fig-extension-panels.pdf` — Extension panels figure (Exhibit 3)
3. `paper/exhibits/fig-ai-valuations.pdf` — AI valuations figure (Exhibit 1)

Additionally computes and prints the veto numerical example (Section 4.1) to console.

Dependencies: R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra` (and `scales` as a transitive dependency). All standard CRAN packages. External data downloaded at runtime from datahub.io (Shiller S&P 500) and FRED (NASDAQ index). No local caches or precomputed intermediates used. The `data/` directory is empty.

## Execution status

- Pipeline ran from scratch successfully in ~2.2 seconds (well under 180-second limit).
- All three output files were regenerated.
- Minor ggplot warnings about removed rows (points outside axis limits in the extension panels figure) are cosmetic and expected.
- All R packages are installed in this environment.
- Network downloads from datahub.io and FRED completed successfully.

## Paper-code consistency

**Parameters verified consistent between code and paper text:**

| Parameter | Code | Paper | Match |
|-----------|------|-------|-------|
| β | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| γ (table) | 4 | 4 | Yes |
| φ | 0.50 | 0.5 | Yes |
| η | 0.50 | 0.5 | Yes |
| θ | 0.15 | 0.15 | Yes |
| Δθ | 0.20 | 0.2 | Yes |
| α₀ | 0.70 | 0.70 | Yes |
| δ (figure) | 0.50 | 0.5 (caption) | Yes |
| φ_large | 0.05 | 0.05 | Yes |
| η_large | 9.0 | 9 | Yes |

**Veto example (Section 4.1) verified:**
- Code: γ=10, p=1%, κ=1%, φ=0.5, η=0.5, ξ=5%, q=70%, α=0.70
- Incomplete markets: V_develop=-15.5327, V_veto=-15.3222 → VETO (matches paper claim)
- Complete markets: V_develop=-13.4615, V_veto=-15.3222 → develop (matches paper claim)

**In-text δ=0.9 illustration verified:**
- Paper claims: net transfer rate = 0.219 at τ=0.30 → consumption multiple ≈ 3.5×, vs. 0.5× catastrophe without transfers
- Computed: net rate = 0.219, consumption multiple = 3.52, without transfers = 0.5 → all match

**Formulas verified consistent:**
- P/D closed-form (Proposition 1) matches `compute_pd_approx` for non-AI and the exact backward recursion `compute_pd_ai_exact` for AI stocks
- Transfer consumption equation matches `consumption_growth` function
- φ_eff formula matches `compute_pd_with_transfer`

**Per-share data (Requirement 5):** The empirical exhibit uses index-level prices from consistent sources (Shiller for S&P 500 price and dividend; FRED for NASDAQ index). P/D is computed within the Shiller dataset (same source for numerator and denominator). The NASDAQ/S&P ratio uses index levels, not per-share quantities. No cross-source per-share combination issues.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| table-pd-ratios.tex | Locally reproducible (verified) |
| fig-extension-panels.pdf | Locally reproducible (verified) |
| fig-ai-valuations.pdf | Locally reproducible, requires network (datahub.io, FRED) |
| Veto numerical example | Locally reproducible (verified, console output) |
| In-text δ=0.9 illustration | Locally reproducible (verified manually, not in code output) |
