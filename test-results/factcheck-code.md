# tests/factcheck-code.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 2m 13s
[ralph-garage/agent-logs/20260412T202602.576170-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.576170-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path is coherent, runs from scratch, and all paper claims are consistent with the code.

## Canonical local analysis path

Single entry point: `code/generate-exhibits.R`, run via `Rscript code/generate-exhibits.R`. Produces all three exhibits used in the paper:

| Exhibit | Output file | Paper reference |
|---------|-------------|-----------------|
| Table 1 (P/D ratios) | `paper/exhibits/table-pd-ratios.tex` | `\input{exhibits/table-pd-ratios.tex}` |
| Figure 1 (AI valuations) | `paper/exhibits/fig-ai-valuations.pdf` | `\includegraphics{exhibits/fig-ai-valuations.pdf}` |
| Figure 2 (Extension panels) | `paper/exhibits/fig-extension-panels.pdf` | `\includegraphics{exhibits/fig-extension-panels.pdf}` |

No other files in `code/` or `data/`. The code also prints the veto-example computation (Section 4.1) to the console for verification; this is not an exhibit.

## Execution status

- **Locally reproducible.** The script ran from scratch in this environment and completed successfully.
- R 4.2.2 with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales` -- all present.
- External data downloads (Shiller dataset from datahub.io, NASDAQ from FRED) succeeded. These are public, no credentials needed.
- No precomputed caches or manually prepared intermediate files were relied on.
- The spec requires execution under 180 seconds including downloads; the script completed within that window.
- Warnings about removed rows in `geom_line()` are expected: Panel (a) of the extension figure intentionally clips the large-singularity P/D series at the axis limits for readability.

## Paper-code consistency

**Parameters.** All parameters in the code match the paper's stated values exactly:

| Parameter | Code | Paper |
|-----------|------|-------|
| beta | 0.96 | 0.96 |
| g | 0.02 | 0.02 |
| gamma | 4 | 4 |
| phi | 0.50 | 0.5 |
| eta | 0.50 | 0.5 |
| theta | 0.15 | 0.15 |
| dtheta | 0.20 | 0.2 |
| phi_large | 0.05 | 0.05 |
| alpha0 | 0.70 | 0.70 |
| delta | 0.50 | 0.5 |
| p_ext | 0.005 | 0.5% |
| xi_ext | 0.05 | 5% |

**Formulas.** The code's implementations match the paper's equations:

- P/D closed-form (Proposition 1, eq. 5-6): `compute_pd_approx` implements $A^j/(1-A^j)$ with correct SDF and dividend growth factors. Verified.
- Exact AI P/D via backward recursion (Appendix A): `compute_pd_ai_exact` iterates the theta chain $\theta_{k+1} = \theta_k + \Delta\theta(1-\theta_k)$ over 60 steps, consistent with the paper's description. Verified.
- Non-AI P/D uses the closed form, which the paper notes is exact since $\Gamma^N$ is theta-independent. Verified.
- Consumption growth with transfers (eq. 8): code formula matches $\phi(1+\eta) + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha \cdot (1+\eta)$. Verified.
- Effective displacement (eq. 10): code computes $\phi_\text{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$. Verified.

**In-text quantitative claims vs. generated output:**

- "P/D of about 15.5 [AI] ... near 11 [non-AI] ... ratio of about 1.4" at p=0.5%, xi=0%: Table shows 15.5, 11.1, 1.4. Consistent.
- "At p=1%, the ratio rises to 2": Table shows ratio 2.0. Consistent.
- Extinction risk compresses the AI premium: ratios decrease monotonically with xi at every p level. Consistent.
- $\phi^{-\gamma} = 160{,}000$ (large singularity): $0.05^{-4} = 160{,}000$. Consistent.
- Robustness claim at delta=0.9, tau=0.30: $\tau(1-\delta\tau) = 0.30 \times 0.73 = 0.219$; consumption multiple $\approx 3.5\times$. Both match manual calculation from the code's formula. Consistent.
- Veto example: code confirms V_veto > V_develop under incomplete markets and V_develop > V_veto under complete markets, matching the paper's stated result. Consistent.

**Per-share data handling (Requirement 5).** The empirical exhibit uses index-level data only (S&P 500 index from Shiller, NASDAQ Composite index from FRED). No per-share quantities or share counts are combined. Not applicable / no issue.

## Reproducibility classification

| Object | Classification |
|--------|---------------|
| Table 1 (P/D ratios) | Locally reproducible |
| Figure 1 (AI valuations) | Locally reproducible (requires network for FRED/datahub download) |
| Figure 2 (Extension panels) | Locally reproducible |
| Veto example (Section 4.1) | Locally reproducible (console output, not an exhibit) |
| All in-text quantitative claims | Consistent with code |
