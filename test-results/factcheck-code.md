# tests/factcheck-code.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 1m 49s
[ralph-garage/agent-logs/20260411T214322.773879-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.773879-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all three exhibits, and every quantitative claim in the paper is consistent with the code.

## Canonical local analysis path

- **Single entry point:** `code/generate-exhibits.R` (run via `Rscript code/generate-exhibits.R`).
- **Outputs:** Three files written to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 2)
  2. `fig-extension-panels.pdf` — Extension two-panel figure (Exhibit 3)
  3. `fig-ai-valuations.pdf` — S&P 500 P/D and NASDAQ/S&P ratio figure (Exhibit 1)
- **External data:** Downloads S&P 500 data from datahub.io (Shiller dataset) and NASDAQ composite from FRED. No WRDS credentials or local caches required.
- **Dependencies:** R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.
- **No intermediate files or precomputed caches.** All model computations (table, extension figure, veto example) are performed from parameters defined at the top of the script.

## Execution status

| Item | Status |
|------|--------|
| R available in environment | Yes |
| Script runs from scratch | Yes, completed successfully |
| All three exhibits generated | Yes |
| Runtime | Well under 180 seconds |
| External downloads | Succeeded (datahub.io, FRED) |
| Warnings | Minor ggplot warnings about rows outside scale range (cosmetic, expected for capped axes) |

**Classification: Locally reproducible** (all three exhibits). Requires network access for the empirical figure data download, which is consistent with spec III.3.d ("including any external data download").

## Paper-code consistency

### Parameters
All parameters in the code match the paper's stated values:

| Parameter | Code | Paper (line 189, 231, 267) | Match |
|-----------|------|----------------------------|-------|
| beta | 0.96 | 0.96 | Yes |
| g | 0.02 | 0.02 | Yes |
| gamma | 4 | 4 | Yes |
| phi | 0.50 | 0.5 | Yes |
| eta | 0.50 | 0.5 | Yes |
| theta | 0.15 | 0.15 | Yes |
| dtheta | 0.20 | 0.2 | Yes |
| alpha0 | 0.70 | 0.70 | Yes |
| delta | 0.50 | 0.5 | Yes |
| phi_large | 0.05 | 0.05 | Yes |
| gamma_veto | 10 | 10 | Yes |
| p_veto | 0.01 | 1% | Yes |
| kappa_veto | 0.01 | 1% | Yes |
| q (prob_pos_v) | 0.70 | 0.70 | Yes |
| xi_ext | 0.05 | 5% | Yes |

### Quantitative claims verified

1. **Table values (line 191):** "p=0.5%, xi=0%: AI P/D about 15.5, non-AI near 11, ratio about 1.4." Table output: 15.5, 11.1, 1.4. Consistent.
2. **Table values (line 191):** "At p=1%, the ratio rises to 2." Table output: ratio = 2.0. Consistent.
3. **Veto example (line 231):** "household vetoes under incomplete markets." Code output: V_veto (-15.32) > V_develop (-15.53). Consistent.
4. **Veto example (line 231):** "Under complete markets... does not veto." Code output: V_develop_CM (-13.46) > V_veto (-15.32). Consistent.
5. **phi(1+eta) = 0.75 (line 189):** 0.5 * 1.5 = 0.75. Consistent.
6. **Large singularity phi(1+eta) = 0.5 (line 267):** 0.05 * 10 = 0.5. Consistent.
7. **phi^(-gamma) = 160,000 (line 269):** 0.05^(-4) = 160,000. Consistent.
8. **delta=0.9, tau=0.30 gives 3.5x consumption (line 265):** Computed 3.52. Consistent with "3.5x."

### Per-share data (Requirement 5)

Not applicable. The code uses aggregate price indices (S&P 500, NASDAQ composite) and trailing dividend yields from the Shiller dataset. No per-share quantities are combined with share counts from different sources.

### Exhibit coverage

All files in `paper/exhibits/` are referenced in the paper:
- `fig-ai-valuations.pdf` at line 46
- `table-pd-ratios.tex` at line 186
- `fig-extension-panels.pdf` at line 275

No orphaned or missing exhibit files.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| `table-pd-ratios.tex` | Locally reproducible |
| `fig-extension-panels.pdf` | Locally reproducible |
| `fig-ai-valuations.pdf` | Locally reproducible (requires network for data download, permitted by spec) |
| Veto example (console output, referenced in-text) | Locally reproducible |
| All in-text quantitative claims checked | Consistent with code |

No violations found.
