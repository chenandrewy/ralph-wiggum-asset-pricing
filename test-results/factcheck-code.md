# tests/factcheck-code.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 2m 27s
[ralph-garage/agent-logs/20260411T100209.008000-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T100209.008000-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path is a single R script that regenerates all exhibits from scratch, and its outputs and logic are consistent with the paper's quantitative claims.

## Canonical local analysis path

- **Entry point:** `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`)
- **Outputs:** `paper/exhibits/table-pd-ratios.tex`, `paper/exhibits/fig-extension-panels.pdf`, `paper/exhibits/fig-ai-valuations.pdf`
- **All three outputs are referenced in `paper/paper.tex`** (lines 46, 193, 282), and no unused exhibits exist in `paper/exhibits/`.
- **No intermediate files or local caches:** The `data/` directory is empty and unused. The script downloads empirical data (S&P 500 from Shiller/datahub, NASDAQ from FRED) at runtime and computes all theoretical exhibits from parameters defined in the script.

## Execution status

- **Classification: Locally reproducible.**
- R is available in this environment. The script executed successfully in under 30 seconds, well within the 180-second spec requirement (III.3.d).
- All three exhibits were regenerated from scratch.
- External data downloads (FRED, datahub.io) completed successfully. The spec explicitly permits external downloads as part of the canonical path (III.3.d: "including any external data download").
- R packages used: `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales` (implicit ggplot2 dependency). All are standard CRAN packages.

## Paper-code consistency

### Parameters

All parameters in the code match the paper's stated values:

| Parameter | Paper (line) | Code | Match |
|-----------|-------------|------|-------|
| beta = 0.96 | 196 | 0.96 | Yes |
| g = 0.02 | 196 | 0.02 | Yes |
| gamma = 4 | 196 | 4 | Yes |
| phi = 0.5 | 196 | 0.50 | Yes |
| eta = 0.5 | 196 | 0.50 | Yes |
| theta = 0.15 | 196 | 0.15 | Yes |
| Delta theta = 0.2 | 196 | 0.20 | Yes |
| phi_large = 0.05 | 274 | 0.05 | Yes |
| alpha = 0.70 | 274 | 0.70 | Yes |
| delta = 0.50 | 280 | 0.50 | Yes |
| Veto: gamma = 10 | 238 | 10 | Yes |
| Veto: p = 1% | 238 | 0.01 | Yes |
| Veto: kappa = 1% | 238 | 0.01 | Yes |
| Veto: q = 0.70 | 238 | 0.70 | Yes |

### Numerical claims vs. code output

1. **Table (Exhibit 1):** Paper states (line 198) "P/D of about 15.5 [AI] ... near 11 [non-AI] ... ratio of about 1.4" at p=0.5%, xi=0. Generated table: AI=15.5, Non-AI=11.1, Ratio=1.4. **Consistent.**
2. **Table (Exhibit 1):** Paper states "At p=1%, the ratio rises to 2." Table: AI=26.5, Non-AI=13.3, Ratio=2.0. **Consistent.**
3. **Paper states phi(1+eta)=0.75** (line 196). Code: 0.5 * 1.5 = 0.75. **Consistent.**
4. **Large singularity phi(1+eta)=0.5** (line 274). Code: 0.05 * 10 = 0.5. **Consistent.**
5. **phi^{-gamma} = 160,000** (line 276). 0.05^{-4} = 160,000. **Consistent.**
6. **Veto result** (line 238): household vetoes under incomplete markets, does not veto under complete markets. Code output: V_develop=-15.5327 < V_veto=-15.3222 (VETO); V_develop_CM=-13.4615 > V_veto (develop). **Consistent.**

### Formula verification

- **P/D closed form (Prop 1):** Code's `compute_pd_approx` implements K/(1-K) where K = beta*(1+g)^{1-gamma} * [(1-p) + p*(1-xi)*phi^{-gamma}*(1+eta)^{-gamma}*Gamma^j]. Matches equations (3)-(4) in the paper. **Consistent.**
- **Exact AI P/D:** Code's `compute_pd_ai_exact` uses backward recursion over the chain of theta values, as described in the paper (line 155) and table footnote. **Consistent.**
- **Non-AI P/D approximate = exact:** The non-AI dividend growth factor Gamma^N = (1-Delta_theta)*(1+eta) is independent of theta, so the "approximate" formula is exact for non-AI stocks. The paper's claim that the table reports exact P/D ratios (line 155) is correct. **Consistent.**
- **Transfer consumption (eq 9):** Code's `consumption_growth` function matches the paper's equation. **Consistent.**
- **Effective displacement (eq 11):** Code's `phi_eff` matches the paper's formula. **Consistent.**

### Data sourcing

- Paper figure caption (line 44): "Sources: NASDAQ from FRED; S&P 500 from the Shiller dataset." Code downloads NASDAQ from FRED and S&P 500 from datahub (Shiller dataset). **Consistent.**

### Per-share data (Requirement 5)

The empirical figure uses index-level price data (NASDAQ Composite, S&P 500), not per-share stock prices. No share count reconciliation is needed. **Not applicable.**

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| table-pd-ratios.tex | Locally reproducible |
| fig-extension-panels.pdf | Locally reproducible |
| fig-ai-valuations.pdf | Locally reproducible (requires network for FRED/datahub downloads) |
| Veto numerical example (console) | Locally reproducible |

## Violations

None found.
