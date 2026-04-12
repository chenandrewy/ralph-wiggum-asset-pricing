# tests/factcheck-code.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 2m 36s
[ralph-garage/agent-logs/20260412T093252.130492-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.130492-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS

REASON: The canonical analysis path runs from scratch, produces all three exhibits, and all numerical claims in the paper are consistent with the code.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`. Produces three outputs directly to `paper/exhibits/`:

1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 2)
2. `fig-extension-panels.pdf` — two-panel extension figure (Exhibit 3)
3. `fig-ai-valuations.pdf` — S&P 500 P/D and NASDAQ/S&P ratio (Exhibit 1)

Additionally prints veto example computations (Section 4.1) to console.

## Execution status

- **Executed successfully from scratch.** All three exhibits regenerated.
- **Runtime dependencies:** R 4.2.2 with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. All available in this environment.
- **Network access:** Required for two downloads (Shiller S&P 500 data from datahub.io, NASDAQ data from FRED). Both succeeded. This is compatible with the spec, which allows up to 180 seconds including external data downloads (spec III.3.d).
- **No local caches or precomputed intermediates required.** The `data/` directory is empty and unused. Compliant with spec III.3.c.
- **Warnings:** ggplot2 warns about rows removed due to scale limits in the extension figure panels. These are intentional — the code caps y-axis ranges for readability and annotates the out-of-range behavior.

## Paper-code consistency

All verified claims match:

| Paper claim | Code/output | Status |
|---|---|---|
| Parameters: β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 | Lines 18–24 of `generate-exhibits.R` | Match |
| p=0.5%, ξ=0: AI P/D ≈ 15.5, non-AI ≈ 11, ratio ≈ 1.4 | Table row: 15.5, 11.1, 1.4 | Match |
| p=1%, ξ=0: ratio rises to 2 | Table row: 26.5, 13.3, 2.0 | Match |
| Extension: α=0.70, p=0.5%, ξ=5%, δ=0.5 | Lines 138–184 | Match |
| Large singularity: η=9, φ=0.05 (φ(1+η)=0.5) | Line 25, lines 187–196 | Match |
| δ=0.9 illustration: net transfer 0.219 at τ=0.30, consumption multiple 3.5× | Verified numerically: 0.219 and 3.52 (rounds to 3.5) | Match |
| τ=0 catastrophe: consumption halves (large sing.), falls 25% (baseline) | φ(1+η)=0.5 and 0.75 confirmed | Match |
| Veto example: γ=10, p=1%, κ=1%, q=0.70, α=0.70 → veto under incomplete, develop under complete | Console output confirms V_veto > V_develop (incomplete), V_develop > V_veto (complete) | Match |
| AI P/D computed by backward recursion over post-singularity θ chain | `compute_pd_ai_exact` function, lines 51–80 | Match |
| Non-AI closed form is exact (Γ^N is θ-independent) | Paper states this; code uses `compute_pd_approx` for non-AI (no recursion needed) | Consistent |

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | **Locally reproducible** — pure computation, no external data |
| `fig-extension-panels.pdf` | **Locally reproducible** — pure computation, no external data |
| `fig-ai-valuations.pdf` | **Locally reproducible with network access** — requires downloading S&P 500 and NASDAQ data |
| Veto example (Section 4.1) | **Locally reproducible** — console output from same script |
| All theoretical propositions | Not code-dependent — mathematical derivations in the paper |

No per-share data issues arise: the empirical figure uses index-level prices and trailing dividends from the Shiller dataset and a FRED price index. No share counts are combined across sources.

No hidden or unnecessary auxiliary files. The `data/` directory is empty. The code is self-contained in a single script with a clear header documenting how to run it, its inputs, and its outputs.
