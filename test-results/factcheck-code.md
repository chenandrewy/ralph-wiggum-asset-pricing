# tests/factcheck-code.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 1m 50s
[ralph-garage/agent-logs/20260409T205235.719682-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.719682-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims and formulas.

## Canonical local analysis path

- **Entry point**: `code/generate-exhibits.R` (single canonical script, as required by spec III.3.b)
- **Run command**: `Rscript code/generate-exhibits.R`
- **Outputs**: Three exhibits written to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — Government transfers two-panel figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — NASDAQ vs S&P 500 empirical figure (Exhibit 3)
- **Dependencies**: R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`
- **External data**: Downloads S&P 500 (datahub/Shiller) and NASDAQ (FRED) at runtime; no precomputed local caches or manually prepared intermediate files
- The script produces all exhibits referenced in `paper/paper.tex` and no others

## Execution status

| Step | Status |
|------|--------|
| Run `Rscript code/generate-exhibits.R` from scratch | **Succeeded** |
| All three exhibits regenerated | **Succeeded** |
| Execution time | Well under 180 seconds |
| External data downloads (FRED, datahub) | **Succeeded** |

No execution blockers encountered. R 4.2.2 and all required packages were available.

## Paper-code consistency

### Parameters
The code uses: β=0.96, g=0.02, γ=4, ϕ=0.5, η=0.5, θ=0.15, Δθ=0.2. These match the paper's stated parameterization in Section 3 exactly.

### P/D formula (Proposition 1, equations 4–5)
- Code's `compute_pd` implements: K = β(1+g)^(1−γ) [(1−p) + p(1−ξ)(1+η)^(−γ) ϕ^(−γ) Γʲ], P/D = K/(1−K)
- This matches equations (4) and (5) in the paper exactly.
- Γ^AI = (θ + Δθ(1−θ))/θ · (1+η) = 3.2, Γ^N = (1−θ−Δθ(1−θ))/(1−θ) · (1+η) = 1.2 — matches paper definition.

### Table claims (Section 3)
- Paper: "p=0.5%, ξ=0: AI stocks ~18, non-AI ~11, ratio ~1.6" → Table: 17.5, 11.1, 1.6 ✓
- Paper: "At p=1%, the ratio rises to nearly 6 to 1" → Table: 76.4, 13.3, 5.8 ✓

### Extension figure claims (Section 4.2)
- Paper: "consumption halves under the large singularity (ϕ(1+η)=0.5)" → Code: 0.05×10=0.5 ✓
- Paper: "falls by 25% under the baseline (ϕ(1+η)=0.75)" → Code: 0.5×1.5=0.75 ✓
- Paper: "ϕ^(−γ) = 160,000" → 0.05^(−4) = 160,000 ✓
- Extension parameters α=0.70, p=0.5%, ξ=5%, δ=0.5 match paper caption ✓
- Code correctly recalculates Γ^AI for the large-singularity scenario with η=9 ✓
- Code's `phi_eff` formula matches the paper's effective displacement parameter ✓

### Empirical figure (Figure 1)
- Downloads NASDAQ Composite and S&P 500, normalizes to Jan 2015 = 100
- Matches the paper's caption: "Monthly closing prices... normalized to January 2015 = 100. Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset."

### Per-share data consistency (Requirement 5)
- Not applicable. The code uses only index-level prices; no per-share quantities are combined with share counts from different sources.

## Reproducibility classification

| Paper output | Classification |
|---|---|
| Table 1 (P/D ratios) | **Locally reproducible** — pure computation from parameters |
| Figure 2 (extension panels) | **Locally reproducible** — pure computation from parameters |
| Figure 1 (AI valuations) | **Locally reproducible** — requires network access to FRED/datahub, which is part of the canonical from-scratch path per spec III.3.d |
| Proposition 1 formulas | **Consistent** — code implements the exact formulas |
| Proposition 2 comparative statics | **Consistent** — table values confirm the stated directional patterns |
| Section 4.2 quantitative claims | **Consistent** — all specific numbers verified against code |
