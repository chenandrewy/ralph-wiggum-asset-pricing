# tests/factcheck-code.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 2m 3s
[ralph-garage/agent-logs/20260411T101504.809757-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.809757-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and all quantitative claims in the paper match the code output.

## Canonical local analysis path

Single entry point: `Rscript code/generate-exhibits.R`. This script generates all three exhibits referenced in `paper/paper.tex`:

1. `paper/exhibits/table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
2. `paper/exhibits/fig-extension-panels.pdf` — Government transfers two-panel figure (Exhibit 2)
3. `paper/exhibits/fig-ai-valuations.pdf` — NASDAQ vs S&P 500 empirical figure (Exhibit 3)

The script also prints veto example computations (Section 4.1) to console.

## Execution status

**Locally reproducible.** The script ran successfully from scratch in this environment with R 4.2.2 and all required packages (`ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`). External data downloads (FRED for NASDAQ, datahub for S&P 500 Shiller data) completed successfully. No precomputed caches or intermediate files are required. No credentials needed. Execution completed well within the 180-second spec limit.

Dependencies: R with `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`. All documented implicitly via `library()` calls.

## Paper-code consistency

**Parameters match.** The paper states (Section 3): $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$. Code lines 18-24 set identical values.

**Extension parameters match.** Paper (Figure 3 caption): $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$. Large singularity: $\eta=9$, $\phi=0.05$. Code lines 138-193 match exactly.

**Veto parameters match.** Paper (Section 4.1): $\gamma=10$, $p=1\%$, $\kappa=1\%$, $\alpha=0.70$, $q=0.70$, $\phi=0.5$, $\eta=0.5$, $\xi=5\%$. Code lines 393-437 match exactly.

**Quantitative claims verified against generated output:**

| Claim (paper) | Generated output | Status |
|---|---|---|
| P/D AI ≈ 15.5 at p=0.5%, ξ=0% | Table: 15.5 | Match |
| P/D Non-AI ≈ 11 at p=0.5%, ξ=0% | Table: 11.1 | Match |
| Ratio ≈ 1.4 at p=0.5%, ξ=0% | Table: 1.4 | Match |
| Ratio rises to 2 at p=1% | Table: 2.0 (ξ=0%) | Match |
| AI P/D ratios 1.3–2× non-AI for p=0.5–1% | Table: 1.3–2.0 | Match |
| φ(1+η)=0.75 baseline → 25% loss | 0.5×1.5=0.75 | Match |
| φ(1+η)=0.5 large sing. → halves | 0.05×10=0.5 | Match |
| φ^{-γ}=160,000 for large sing. | 0.05^{-4}=160,000 | Match |
| Household vetoes under incomplete markets | V_veto > V_develop | Match |
| No veto under complete markets | V_develop^CM > V_veto | Match |

**P/D formulas match.** The approximate closed-form (non-AI) and exact backward recursion (AI) in the code implement the Euler equation derivation in Appendix A. The code correctly handles the chain of post-singularity θ values for AI stocks via backward recursion (60 steps), as noted in the table footnote.

**Transfer formulas match.** The code's `consumption_growth` and `compute_pd_with_transfer` functions implement equations (5)–(7) of the paper, using φ_eff = φ + τ(1−δτ)(1−φα)/α.

**Per-share data (Requirement 5).** The model operates on aggregate dividend claims (D^AI = θC, D^N = (1−θ)C) with no share issuance or splits. The empirical figure uses price index levels (NASDAQ Composite, S&P 500), not per-share quantities. No per-share/share-count mismatch is possible in this setup.

## Reproducibility classification

| Output | Classification |
|---|---|
| `table-pd-ratios.tex` | Locally reproducible |
| `fig-extension-panels.pdf` | Locally reproducible |
| `fig-ai-valuations.pdf` | Locally reproducible (requires network for FRED/datahub download, which is part of the spec-approved canonical path) |
| Veto numerical example | Locally reproducible (console output matches paper claims) |
| All other paper claims (propositions, proofs) | Theoretical; not code-dependent |
