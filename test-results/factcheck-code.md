# tests/factcheck-code.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 2m 4s
[ralph-garage/agent-logs/20260411T103039.124925-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.124925-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The single canonical entry point runs from scratch, produces all exhibits, and its outputs are consistent with every quantitative claim in the paper.

## Canonical local analysis path

- **Entry point**: `code/generate-exhibits.R` (the only file in `code/`).
- **Outputs**: `paper/exhibits/table-pd-ratios.tex`, `paper/exhibits/fig-extension-panels.pdf`, `paper/exhibits/fig-ai-valuations.pdf`.
- All three outputs are referenced in `paper/paper.tex` and no other exhibit files exist in `paper/exhibits/`.
- The spec (III.3.b) requires one canonical entry point that regenerates every exhibit. Satisfied.

## Execution status

| Check | Result |
|---|---|
| Runs from scratch (spec III.3.c) | **Pass.** No precomputed caches or manual intermediates. Theoretical exhibits are computed in-memory; empirical figure downloads data from FRED and datahub at runtime. |
| Completes within 180 seconds (spec III.3.d) | **Pass.** Completed successfully within the timeout. |
| Outputs to `paper/exhibits/` (spec III.3.e) | **Pass.** |
| Written in R (spec III.3.a) | **Pass.** |
| Required packages documented | **Pass.** All dependencies (`ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`) are standard CRAN packages loaded at the top of the script. |
| Network access | The empirical figure (Exhibit 3) downloads S&P 500 data from datahub and NASDAQ data from FRED. This is consistent with the spec, which allows external data downloads (III.3.d: "including any external data download"). |

All three exhibits were regenerated without errors. Warnings about removed rows in the extension figure are cosmetic (data points outside the capped y-axis range are intentionally excluded by `scale_y_continuous(limits = ...)`).

## Paper-code consistency

### Parameters

| Parameter | Paper (Section 3 / Table note) | Code | Match |
|---|---|---|---|
| β = 0.96 | ✓ | `beta <- 0.96` | Yes |
| g = 0.02 | ✓ | `g <- 0.02` | Yes |
| γ = 4 | ✓ | `gamma <- 4` | Yes |
| φ = 0.5 | ✓ | `phi <- 0.50` | Yes |
| η = 0.5 | ✓ | `eta <- 0.50` | Yes |
| θ = 0.15 | ✓ | `theta <- 0.15` | Yes |
| Δθ = 0.2 | ✓ | `dtheta <- 0.20` | Yes |

### Table (Exhibit 1) numerical claims

- Paper: "p = 0.5%, no extinction: AI P/D about 15.5, non-AI near 11, ratio about 1.4." Table output: 15.5, 11.1, 1.4. **Match.**
- Paper: "At p = 1%, the ratio rises to 2." Table output: p=1.0%, ξ=0% → ratio 2.0. **Match.**
- Paper: "AI stock P/D ratios are 1.3 to 2 times those of non-AI stocks across annual singularity probabilities in the 0.5–1% range." Table confirms ratios of 1.3–2.0 in that range. **Match.**

### Extension figure (Exhibit 2) parameters and claims

- Paper: "γ = 4, α = 0.70, p = 0.5%, ξ = 5%, δ = 0.5." Code: `gamma=4`, `alpha0=0.70`, `p_ext=0.005`, `xi_ext=0.05`, `delta=0.50`. **Match.**
- Paper: "Baseline: η = 0.5, φ = 0.5; large singularity: η = 9, φ = 0.05." Code: baseline `eta_val=0.5, phi_val=phi=0.5`; large `eta_val=9.0, phi_val=phi_large=0.05`. **Match.**
- Paper: "consumption halves under the large singularity (φ(1+η) = 0.5)." 0.05 × 10 = 0.5. **Match.**
- Paper: "falls by 25% under the baseline (φ(1+η) = 0.75)." 0.5 × 1.5 = 0.75. **Match.**
- Paper: "φ^{-γ} = 160,000." 0.05^(−4) = 160,000. **Match.**
- Paper: "P/D ratio is undefined at τ = 0 [for large singularity]." Code returns NA when existence condition violated; the 3 removed rows in the warning correspond to this. **Match.**

### Veto example (Section 4.1)

- Paper: "φ = 0.5, η = 0.5, ξ = 5%, p = 1%, γ = 10, α = 0.70, q = 0.70, κ = 1%."
- Code: `gamma_veto=10, p_veto=0.01, prob_pos_v=0.70, prob_neg_v=0.30, kappa_veto=0.01, alpha_veto=0.70`, uses global `phi=0.5, eta=0.5, xi_ext=0.05`. **Match.**
- Paper claims: household vetoes under incomplete markets, does not veto under complete markets.
- Code output: `V_veto > V_develop` (VETO) for incomplete; `V_develop^CM > V_veto` (develop) for complete. **Match.**

### Empirical figure (Exhibit 3)

- Paper caption: "NASDAQ from FRED; S&P 500 from the Shiller dataset." Code downloads NASDAQ via `download_fred("NASDAQCOM")` and S&P 500 from `datahub.io/core/s-and-p-500`. **Match.**
- Paper: "each normalized to January 2015 = 100." Code normalizes to first common month = 100 with start date 2015-01-01. **Match.**

### Dividend growth factors

- Code: `share_ratio_ai = (θ + Δθ(1−θ))/θ`, `gamma_ai = share_ratio_ai × (1+η)`. Paper equation: Γ^AI = [θ + Δθ(1−θ)]/θ × (1+η). **Match.**
- Non-AI growth factor Γ^N = (1−Δθ)(1+η) is θ-independent, making the closed-form P/D exact for non-AI stocks. The code correctly uses exact backward recursion for AI stocks and the closed form for non-AI stocks.

### Per-share data handling (Requirement 5)

The empirical figure uses index-level prices (S&P 500 index, NASDAQ Composite index), not per-share quantities. The code normalizes indices to a common base. No per-share / share-count combination issues arise. The theoretical exhibits are pure model computations with no market microstructure data. **No issues.**

## Reproducibility classification

| Output | Classification |
|---|---|
| Table of P/D ratios (Exhibit 1) | **Locally reproducible.** Pure computation, no external data. |
| Extension figure (Exhibit 2) | **Locally reproducible.** Pure computation, no external data. |
| AI valuations figure (Exhibit 3) | **Locally reproducible with network access.** Requires downloading from FRED and datahub. Successfully executed in this environment. |
| Veto numerical example (Section 4.1) | **Locally reproducible.** Printed to console; values match paper's qualitative claims. |
| All theoretical propositions and proofs | **Not code-generated.** These are mathematical derivations in the paper, not outputs of the analysis code. Consistent with the code's parameterizations. |
