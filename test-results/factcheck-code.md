# tests/factcheck-code.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260409T184838.247359-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.247359-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and its outputs are consistent with the paper's quantitative claims.

## Canonical local analysis path

- **Entry point:** `Rscript code/generate-exhibits.R` (single canonical script, documented in header comment).
- **Inputs:** None external. All parameters are defined inline; the illustrative empirical figure uses hardcoded approximate data.
- **Outputs:** Three exhibit files written directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — Government transfers two-panel figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — Illustrative AI valuations figure (Exhibit 3)
- **Dependencies:** R with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.
- **No WRDS queries, no credentials, no network access, no precomputed caches.**

The structure satisfies spec III.3: single canonical entry point in `code/`, written in R, runs from scratch, outputs directly to `paper/exhibits/`. All files in `paper/exhibits/` are used in the paper, and vice versa.

## Execution status

- **Locally reproducible.** The script ran successfully from scratch in this environment in under 10 seconds. All three output files were regenerated.
- No execution blockers (R and all required packages are available).
- No credentials or downloads required.

## Paper-code consistency

### Exhibit 1: P/D ratio table

- **Formula verification:** The code's `compute_pd` implements $K/(1-K)$ where $K = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^j]$. This matches the paper's equations (5)-(6) exactly.
- **Dividend growth factors:** $\Gamma^{AI} = [\theta + \Delta\theta(1-\theta)]/\theta \cdot (1+\eta) = 3.2$ and $\Gamma^N = [1-\theta-\Delta\theta(1-\theta)]/(1-\theta) \cdot (1+\eta) = 1.2$. Matches the paper's definition.
- **Parameter values:** Code uses $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$. All match the paper's stated parameterization (Section 3).
- **Paper claims vs. table output:**
  - "P/D of roughly 18" at $p=0.5\%$, $\xi=0$: table shows 17.5. Consistent.
  - "non-AI stocks trade near 11": table shows 11.1. Consistent.
  - "ratio of about 1.6": table shows 1.6. Consistent.
  - "At $p=1\%$, the ratio rises to nearly 6 to 1": table shows 5.8. Consistent.
  - "up to roughly six times higher": max ratio in table is 5.8 at $p=1\%$, $\xi=0$. Consistent with "roughly six."
- **Comparative statics:** Extinction risk compresses the spread (decreasing ratio with increasing $\xi$) — visible in table. Consistent with Proposition 2(iii).

### Exhibit 2: Extension panels

- **Consumption growth formula:** Code computes $\phi(1+\eta) + \tau(1-\delta_0\tau)(1-\phi\alpha_0)/\alpha_0 \cdot (1+\eta)$, which equals $c^H_{post}/c^H_{pre}$. Derived correctly from paper equation (8).
- **P/D with transfers:** Code computes an effective $\phi_{eff}$ and substitutes into the P/D formula. This correctly captures how transfers change the household's singularity consumption and hence the SDF.
- **Parameters:** Baseline ($\eta=0.5$, $\phi=0.5$) and large singularity ($\eta=9$, $\phi=0.05$) with $p=0.5\%$, $\xi=5\%$, $\alpha_0=0.70$, $\delta_0=0.50$.
- **Paper claims:**
  - "consumption halves under the large singularity ($\phi(1+\eta)=0.5$)": $0.05 \times 10 = 0.5$. Correct.
  - "falls by 25% under the baseline ($\phi(1+\eta)=0.75$)": $0.5 \times 1.5 = 0.75$. Correct.
  - "transfers reduce the hedge value of AI stocks, compressing P/D ratios": left panel shows declining P/D with $\tau$. Consistent.

### Exhibit 3: AI valuations figure

- **Data source:** Hardcoded illustrative P/E ratios, not from any external dataset.
- **Labeling:** Figure caption says "(Illustrative)"; paper text says "based on approximate values from public sources." Properly labeled as non-canonical empirical content.

### Per-share data handling (Requirement 5)

Not applicable. The code uses no per-share market data. All quantities are model-derived parameters or illustrative hardcoded values.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` | Locally reproducible |
| `fig-extension-panels.pdf` | Locally reproducible |
| `fig-ai-valuations.pdf` | Locally reproducible (illustrative data, properly labeled) |
| Paper's theoretical propositions | Not code-dependent (analytical proofs) |
| Paper's quantitative claims (Section 3) | Locally reproducible, consistent with code output |

No violations found.
