# tests/factcheck-code.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 1m 57s
[ralph-garage/agent-logs/20260414T102326.814486-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.814486-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path is coherent, runs from scratch, and all paper claims are consistent with the code.

## Canonical local analysis path

- **Single entry point:** `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`.
- **Outputs:** Three files written to `paper/exhibits/`:
  - `table-pd-ratios.tex` (Exhibit 2: P/D ratio table)
  - `fig-extension-panels.pdf` (Exhibit 3: government transfers figure)
  - `fig-ai-valuations.pdf` (Exhibit 1: valuation ratios figure)
- **All three outputs are used in `paper/paper.tex`** (lines 46, 188, 277). No unused exhibit files.
- **No precomputed caches or intermediate files required.** The model outputs are computed from parameters; the empirical figure downloads data from datahub.io (Shiller S&P 500) and FRED (NASDAQ Composite) at runtime.
- **No per-share data issues.** Empirical data uses index-level prices and trailing dividends from Shiller; the NASDAQ/S&P ratio is a simple index-level price ratio. Model calculations are purely theoretical.

## Execution status

- **Successfully executed from scratch** in this environment. R and all required packages (`ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`) are available.
- **Data downloads completed** (Shiller dataset from datahub.io, NASDAQ from FRED).
- **Runtime:** Well under the 180-second spec requirement.
- **Warnings:** R emitted warnings about rows removed due to scale limits in the extension figure plots. These are cosmetic (data points outside the chosen axis bounds are clipped) and do not affect correctness.

## Paper-code consistency

All checked quantitative claims in the paper match the code:

| Claim (paper location) | Paper says | Code produces | Match |
|---|---|---|---|
| Parameters (§3, line 191) | β=0.96, g=0.02, γ=4, φ=0.5, η=0.5, θ=0.15, Δθ=0.2 | `beta=0.96, g=0.02, gamma=4, phi=0.50, eta=0.50, theta=0.15, dtheta=0.20` | ✓ |
| P/D at p=0.5%, ξ=0% (§3, line 193) | AI ≈ 15.5, Non-AI ≈ 11, ratio ≈ 1.4 | AI=15.5, Non-AI=11.1, Ratio=1.4 | ✓ |
| Ratio at p=1% (§3, line 193) | Ratio rises to 2 | Ratio=2.0 at p=1%, ξ=0% | ✓ |
| AI P/D computation method (table footnote) | "numerically exact, computed by iterating the Euler equation" | `compute_pd_ai_exact()` uses backward recursion over 60 θ-steps | ✓ |
| Non-AI closed form (Appendix A, line 320) | "Γ^N is θ-independent, so the non-AI closed form is exact" | `compute_pd_approx()` used for non-AI; Γ^N = (1−Δθ)(1+η) | ✓ |
| Veto example (§4.1, line 233) | φ=0.5, η=0.5, ξ=5%, p=1%, γ=10, α=0.70, q=0.70, κ=1%; household vetoes under incomplete markets, develops under complete markets | Code output: V_veto > V_develop (VETO); V_develop^CM > V_veto (develop) | ✓ |
| Extension parameters (§4.2, line 269) | γ=4, α=0.70, p=0.5%, ξ=5%, δ=0.5; baseline η=0.5/φ=0.5; large η=9/φ=0.05 | `gamma=4, alpha0=0.70, p_ext=0.005, xi_ext=0.05, delta=0.50`; baseline/large match | ✓ |
| Large singularity displacement (line 269) | φ(1+η)=0.5 (halves) | 0.05×10=0.5 | ✓ |
| Baseline displacement (line 269) | φ(1+η)=0.75 (−25%) | 0.5×1.5=0.75 | ✓ |
| φ^{−γ} for large singularity (line 271) | 160,000 | 0.05^(−4)=160,000 | ✓ |
| Robustness check δ=0.9 (line 267) | "still yields a consumption multiple of 3.5× at τ=0.30" | Manual calc: 0.5 + 0.30×0.73×0.965×10/0.70 ≈ 3.52× | ✓ |
| Transfer formula (eq 8 vs code) | c^H_post = φα(1+η)C(1+g) + τ(1−δτ)(1−φα)(1+η)C(1+g) | `consumption_growth()` returns c^H_post / [α·C·(1+g)] matching the formula | ✓ |
| φ_eff formula (eq 10 vs code) | φ_eff = φ + τ(1−δτ)(1−φα)/α | `compute_pd_with_transfer()` line 152 implements exactly this | ✓ |
| Extension P/D uses exact recursion | Table footnote and Appendix A describe backward recursion | `compute_pd_with_transfer()` uses same 60-step backward recursion as `compute_pd_ai_exact()` | ✓ |

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | **Locally reproducible** — computed from parameters, no external data |
| `fig-extension-panels.pdf` | **Locally reproducible** — computed from parameters, no external data |
| `fig-ai-valuations.pdf` | **Locally reproducible** — requires network access to download Shiller and FRED data, but this is part of the canonical from-scratch pipeline per the spec |
| Veto example (§4.1 in-text) | **Locally reproducible** — computed and printed to console by the same script |
| All theoretical propositions | **Not code-dependent** — analytical results proved in the paper |
