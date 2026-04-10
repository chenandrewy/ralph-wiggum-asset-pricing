# tests/factcheck-code.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 2m 25s
[ralph-garage/agent-logs/20260409T194838.522671-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.522671-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all three exhibits, and is consistent with the paper's formulas and parameters, with one minor documentation gap.

## Canonical local analysis path

- **Entry point:** `code/generate-exhibits.R` (single canonical script)
- **Run command:** `Rscript code/generate-exhibits.R`
- **Outputs:** Three exhibits written directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — Two-panel extension figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — NASDAQ vs. S&P 500 time series (Exhibit 3)
- **External data:** Downloads S&P 500 (datahub/Shiller) and NASDAQ (FRED) at runtime. No local caches or precomputed intermediate files.
- **No WRDS queries or credentials required.** All data comes from public URLs.
- The paper includes exactly three exhibit references (`\input` / `\includegraphics`), all matching the code's outputs.

## Execution status

- **Result:** Successful. All three exhibits generated without error.
- **Runtime:** Well under the 180-second spec limit.
- **Environment:** R is available with all required packages (`ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`).
- **Network access:** Required for Exhibit 3 (FRED and datahub downloads). Exhibits 1 and 2 are purely computational with no external data.

## Paper-code consistency

### Parameters (all match)

| Parameter | Paper | Code | Match |
|-----------|-------|------|-------|
| β | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| γ | 4 | 4 | Yes |
| φ (baseline) | 0.5 | 0.50 | Yes |
| η (baseline) | 0.5 | 0.50 | Yes |
| θ | 0.15 | 0.15 | Yes |
| Δθ | 0.2 | 0.20 | Yes |
| φ (large singularity) | 0.05 | 0.05 | Yes |
| η (large singularity) | 9 | 9.0 | Yes |
| p (extension figure) | 0.5% | 0.005 | Yes |
| ξ (extension figure) | 5% | 0.05 | Yes |
| δ₀ | 0.5 (caption) | 0.50 | Yes |
| α₀ (household share) | Not stated | 0.70 | **Undocumented** |

### Formulas (all match)

- **P/D ratio** (Proposition 1, Eq. 126–131): Code's `compute_pd()` exactly implements K/(1-K) where K = β(1+g)^(1-γ)[(1-p) + p(1-ξ)φ^(-γ)(1+η)^(-γ)Γ^j]. Verified.
- **Dividend growth factors** Γ^AI and Γ^N: Code lines 34–37 match paper definitions exactly.
- **Transfer consumption** (Eq. 249): Code's `consumption_growth()` matches.
- **Transfer ratio** (Eq. 257): Code's `phi_eff` construction is consistent.
- **P/D with transfers**: Code's `compute_pd_with_transfer()` correctly substitutes φ_eff for φ.

### Minor issue: undocumented α₀

The code uses `alpha0 = 0.70` (household's initial consumption share) for the extension figure. This parameter appears in the model as a variable (α_t) but its numerical value for the figure is not stated in the paper text or caption. The caption lists p, ξ, and δ₀ but omits α. This is a documentation gap, not a logical error — the formulas in the paper use α symbolically, and the code's value is reasonable.

### Per-share data (Requirement 5)

Not applicable. Exhibit 3 uses market-level price indices (S&P 500 index, NASDAQ Composite), not per-share stock data. No share count adjustments are involved.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` (P/D table) | **Locally reproducible** — pure computation, no external data |
| `fig-extension-panels.pdf` (extension panels) | **Locally reproducible** — pure computation, no external data |
| `fig-ai-valuations.pdf` (AI valuations) | **Locally reproducible with network** — requires HTTP downloads from FRED and datahub at runtime; no credentials needed |

All three exhibits are regenerated from scratch by the canonical entry point. No precomputed caches or manually prepared files are used. The pipeline satisfies the paper spec's from-scratch execution requirement (III.3.c).
