# tests/factcheck-code.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 1m 58s
[ralph-garage/agent-logs/20260412T094631.077100-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.077100-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical Local Analysis Path

- **Entry point**: `code/generate-exhibits.R` (single canonical script, as required by spec III.3.b).
- **Language**: R, with libraries `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.
- **Outputs**: Three exhibits written directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 2 in paper)
  2. `fig-extension-panels.pdf` — Two-panel extension figure (Exhibit 3 in paper)
  3. `fig-ai-valuations.pdf` — Two-panel empirical valuation figure (Exhibit 1 in paper)
- **Data downloads**: S&P 500 data from datahub.io (Shiller dataset) and NASDAQ from FRED. No local caches or precomputed intermediates.
- **Veto computation**: Printed to console for cross-checking; not an exhibit but supports the numerical example in Section 4.1.
- All files in `paper/exhibits/` are referenced in `paper/paper.tex`; no orphan outputs.

## Execution Status

| Item | Status |
|------|--------|
| From-scratch execution | **Passed** — no precomputed caches or intermediate files required |
| Runtime | ~2.5 seconds (well under the 180-second spec limit) |
| Network downloads | S&P 500 (datahub.io) and NASDAQ (FRED) — successful |
| R packages | All five packages available and loaded |
| Warnings | Minor ggplot2 warnings about rows removed outside scale range (cosmetic, expected from axis clamping) |

## Paper-Code Consistency

| Paper Claim | Code | Match |
|---|---|---|
| Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 | Lines 18–24 | ✓ |
| φ(1+η)=0.75, household consumption falls 25% | 0.5×1.5=0.75 | ✓ |
| AI P/D ratios computed by backward recursion over post-singularity θ chain | `compute_pd_ai_exact()` lines 51–80 | ✓ |
| Non-AI P/D uses closed-form (θ-independent Γ^N) | `compute_pd_approx()` lines 40–46 | ✓ |
| Table P/D ratios 1.3–2× in 0.5–1% range | Table output: p=0.5% ratio 1.3–1.4; p=1% ratio 1.7–2.0 | ✓ |
| Extension: p=0.5%, ξ=5%, δ=0.50, α=0.70 | Lines 140, 183–184 | ✓ |
| Large singularity: η=9, φ=0.05, so φ(1+η)=0.5 | Line 25; 0.05×10=0.5 | ✓ |
| Veto: γ=10, p=1%, κ=1%, q=70%, α=0.70 → VETO under incomplete, develop under complete | Console output confirms | ✓ |
| φ_eff formula: φ + τ(1−δτ)(1−φα)/α | `compute_pd_with_transfer()` line 152 | ✓ |
| Consumption growth formula in singularity with transfers | `consumption_growth()` lines 145–147 | ✓ |

## Reproducibility Classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | **Locally reproducible** — pure computation, no external data |
| `fig-extension-panels.pdf` | **Locally reproducible** — pure computation, no external data |
| `fig-ai-valuations.pdf` | **Reproducible with network access** — requires live download from datahub.io and FRED |
| Veto numerical example (Section 4.1) | **Locally reproducible** — pure computation, printed to console |

No per-share data issues arise: the empirical exhibit uses index-level price and dividend data (Shiller S&P 500 P/D) and index-level price ratios (NASDAQ/S&P 500). No per-share quantities are combined with share counts from different sources.
