# tests/factcheck-code.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260409T213452.260353-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.260353-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis pipeline runs from scratch, produces all three exhibits, and its logic is consistent with the paper's formulas and quantitative claims.

## Canonical local analysis path

- **Entry point:** `code/generate-exhibits.R` (single script, run via `Rscript code/generate-exhibits.R`)
- **Outputs:** Three exhibits written directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1 in paper)
  2. `fig-extension-panels.pdf` — Extension two-panel figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — AI valuations vs. market figure (Exhibit 3)
- **External data:** Downloads S&P 500 data from datahub (Shiller dataset) and NASDAQ Composite from FRED. No local data files or caches required.
- **Dependencies:** R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.
- **No precomputed intermediate files.** The `data/` directory is empty; everything is computed or downloaded at runtime.

This satisfies the spec requirement of "one canonical entry point that regenerates every exhibit" and "runs from scratch without precomputed local caches."

## Execution status

| Item | Status |
|------|--------|
| R available | Yes (`/usr/bin/Rscript`) |
| All packages available | Yes |
| Pipeline runs from scratch | Yes, completed successfully |
| Network downloads (FRED, datahub) | Succeeded |
| All three exhibits produced | Yes |
| Runtime | Well under 180-second spec limit |

No execution blockers encountered.

## Paper-code consistency

### Parameters
All parameters in the code match those stated in the paper (Section 3 and Figure 2 caption):
- $\beta = 0.96$, $g = 0.02$, $\gamma = 4$, $\phi = 0.5$, $\eta = 0.5$, $\theta = 0.15$, $\Delta\theta = 0.2$ — all match.
- Extension parameters: $\alpha = 0.70$, $p = 0.5\%$, $\xi = 5\%$, $\delta = 0.5$, large singularity $\eta = 9$, $\phi = 0.05$ — all match.

### Formula verification
- **P/D formula (Proposition 1, eqs. 4–5):** Code's `compute_pd` correctly implements $K/(1-K)$ where $K = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^j]$. Verified against paper.
- **Dividend growth factors:** $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)]/\theta \cdot (1+\eta) = 3.2$ and $\Gamma^N = [1-\theta-\Delta\theta(1-\theta)]/(1-\theta) \cdot (1+\eta) = 1.2$. Correct.
- **Effective displacement (eq. 7):** Code's `phi_eff` formula matches the paper's $\phi_{\text{eff}} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$. Verified numerically.
- **Consumption growth in singularity:** Code computes the singularity-specific multiplier $\phi(1+\eta) + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha \cdot (1+\eta)$, consistent with eq. (6) divided by $\alpha C_t$.
- **Transfer ratio (eq. 10):** The ratio $c^H_{\text{post}}/c^H_{\text{no-transfer}}$ is independent of $\eta$ as the paper claims. Verified.

### Quantitative claims
- Paper: "AI stocks trade at P/D of roughly 18, non-AI near 11, ratio about 1.6" at $p=0.5\%$, $\xi=0$. Code: AI P/D = 17.5, Non-AI P/D = 11.1, ratio = 1.6. **Consistent.**
- Paper: "At $p=1\%$, the ratio rises to nearly 6 to 1." Code: ratio = 5.8. **Consistent.**
- Paper: "$\phi^{-\gamma} = 160{,}000$" for the large singularity. Code: $0.05^{-4} = 160{,}000$. **Exact match.**
- Paper: "consumption halves under the large singularity ($\phi(1+\eta)=0.5$) and falls by 25% under the baseline ($\phi(1+\eta)=0.75$)." Code: 0.5 and 0.75. **Exact match.**
- Paper: "P/D ratio is undefined at $\tau=0$" for the large singularity. Code: $K = 2.37 \geq 1$, returns NA. **Consistent.**

### Existence condition
The code correctly returns `NA` when $K \geq 1$, matching Remark 1's existence condition. The large-singularity scenario violates the condition at $\tau=0$ as the paper describes.

## Reproducibility classification

| Paper output | Classification |
|---|---|
| Table 1 (P/D ratios) | **Locally reproducible** — generated from model parameters, no external data |
| Figure 2 (extension panels) | **Locally reproducible** — generated from model parameters, no external data |
| Figure 1 (AI valuations) | **Locally reproducible** — downloads data from FRED/datahub at runtime; requires network access but this is part of the canonical pipeline |
| Proposition 1 formulas | **Consistent with code** — code implements the exact formulas |
| Proposition 2 comparative statics | **Consistent with code** — table exhibits all three comparative statics patterns |
| Section 4.1 (veto extension) | **No code component** — purely theoretical; no code needed |
| Section 4.2 (transfers) | **Locally reproducible** — Figure 2 covers this |

### Per-share data handling (Requirement 5)
Not applicable. The code uses only index-level data (NASDAQ Composite, S&P 500) for the empirical figure and model parameters for all other exhibits. No per-share quantities are combined with share counts.

### Auxiliary files
No hidden or unnecessary auxiliary files. The `data/` directory is empty. All inputs are either model parameters hard-coded in the script or downloaded at runtime.
