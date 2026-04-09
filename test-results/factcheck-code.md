# tests/factcheck-code.py
Started: 2026-04-09 19:03:08 EDT
Runtime: 2m 4s
[ralph-garage/agent-logs/20260409T190308.206652-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T190308.206652-0400_factcheck-code_claude_opus.log)

# factcheck-code

VERDICT: PASS
REASON: The canonical analysis path runs from scratch, generates all exhibits, and paper claims are consistent with the code.

## Canonical local analysis path

- Single entry point: `code/generate-exhibits.R`
- Run command: `Rscript code/generate-exhibits.R`
- No external data, no network access, no credentials required
- All parameters defined inline; illustrative empirical data hardcoded
- Outputs three exhibits directly to `paper/exhibits/`:
  1. `table-pd-ratios.tex` (Exhibit 1: P/D ratio table)
  2. `fig-extension-panels.pdf` (Exhibit 2: government transfers two-panel figure)
  3. `fig-ai-valuations.pdf` (Exhibit 3: illustrative AI valuations vs market)
- These are the exact three exhibits referenced in `paper/paper.tex`

## Execution status

- **Executed successfully from scratch.** Runtime: under 5 seconds.
- R 4.2.2 with packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales` -- all available.
- Regenerated table is byte-identical to the committed version.
- Regenerated PDFs differ only in minor rendering metadata (expected for plot regeneration).
- Spec requirement III.3.c (from-scratch, no precomputed caches): satisfied.
- Spec requirement III.3.d (under 180 seconds): satisfied.

## Paper-code consistency

**Table (Exhibit 1):**
- Paper states p=0.5%, xi=0 yields AI P/D "roughly 18", non-AI "near 11", ratio "about 1.6". Code produces 17.5, 11.1, 1.6. Consistent.
- Paper states p=1% ratio "nearly 6 to 1". Code produces 5.8. Consistent.
- Paper states parameters: beta=0.96, g=0.02, gamma=4, phi=0.5, eta=0.5, theta=0.15, dtheta=0.2. Code matches exactly.

**Extension figure (Exhibit 2):**
- Paper states phi*(1+eta)=0.75 for baseline (25% consumption loss). Code: 0.5*1.5=0.75. Correct.
- Paper states phi_large=0.05, eta=9 giving phi*(1+eta)=0.5 (consumption halves). Code: 0.05*10=0.5. Correct.
- Paper states p=0.5%, xi=5% for extension. Code uses p_ext=0.005, xi_ext=0.05. Matches.
- Transfer consumption formula (eq. 7) correctly independent of eta in both paper and code.
- P/D computation with transfers uses effective phi_eff consistent with the paper's equation (6).

**Illustrative valuations figure (Exhibit 3):**
- Paper caption labels it "Illustrative". Text says "approximate values from public sources." Appropriately flagged as non-canonical/illustrative data.
- Data is hardcoded in the script (no external download), consistent with illustrative intent.

**Model formulas:**
- P/D formula in code (K/(1-K) structure) matches Proposition 1 equations (4)-(5).
- Dividend growth factors Gamma^AI and Gamma^N computed correctly from theta/dtheta.
- SDF term phi^(-gamma)*(1+eta)^(-gamma) matches the Euler equation derivation in Appendix A.

## Reproducibility classification

| Output | Classification |
|--------|---------------|
| Table 1 (P/D ratios) | Locally reproducible |
| Figure 2 (extension panels) | Locally reproducible |
| Figure 1 (AI valuations) | Locally reproducible (illustrative data hardcoded; appropriately labeled) |

**Requirement 5 (per-share data):** Not applicable. The code computes theoretical model quantities only; no per-share market data is combined with share counts.

**Requirement 6 (non-reproducible outputs labeled):** The only empirical content (Figure 1) is clearly labeled "Illustrative" in the caption and described as "approximate values from public sources" in the text.

**Requirement 7 (no hidden auxiliary files):** No external files, caches, or undocumented dependencies. The `data/` directory is empty.
