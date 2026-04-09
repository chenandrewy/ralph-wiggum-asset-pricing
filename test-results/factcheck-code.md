# tests/factcheck-code.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 2m 47s
[ralph-garage/agent-logs/20260409T193301.999820-0400_factcheck-code_claude_opus.log](../ralph-garage/agent-logs/20260409T193301.999820-0400_factcheck-code_claude_opus.log)

# factcheck-code
VERDICT: PASS
REASON: The canonical analysis path runs from scratch, produces all exhibits, and is consistent with the paper's formulas and claims.

## Canonical local analysis path

- **Entry point**: `code/generate-exhibits.R` (single canonical script, run via `Rscript code/generate-exhibits.R`)
- **Outputs**: Three exhibits written to `paper/exhibits/`:
  1. `table-pd-ratios.tex` — P/D ratio table (Exhibit 1)
  2. `fig-extension-panels.pdf` — two-panel extension figure (Exhibit 2)
  3. `fig-ai-valuations.pdf` — empirical AI valuations vs. market (Exhibit 3)
- **Data sources**: Downloads S&P 500 data from datahub.io (Shiller dataset) and NASDAQ from FRED. No local data files are required; `data/` is empty.
- **Dependencies**: R packages `ggplot2`, `dplyr`, `tidyr`, `gridExtra`, `scales`.

## Execution status

| Check | Status |
|-------|--------|
| Runs from scratch | PASS — no precomputed caches or intermediate files |
| Completes under 180s | PASS — ~2.5 seconds |
| All outputs generated | PASS — all 3 exhibits produced |
| All exhibits used in paper | PASS — all files in `paper/exhibits/` are referenced in `paper.tex` |
| No hidden auxiliary files | PASS — `data/` is empty; no undocumented inputs |

## Paper-code consistency

### Table (P/D ratios)
- Code's `compute_pd` function matches the paper's Proposition 1, equations (4)–(5): $K/(1-K)$ where $K = \beta(1+g)^{1-\gamma}[(1-p) + p(1-\xi)(1+\eta)^{-\gamma}\phi^{-\gamma}\Gamma^j]$.
- Parameters match paper text: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.
- Dividend growth factors $\Gamma^{AI}=3.2$ and $\Gamma^{N}=1.2$ match the paper's definitions.
- Independently verified: P/D values (e.g., 17.5 AI at p=0.5%/xi=0; 76.4 AI at p=1%/xi=0) match the output table to rounding.
- Paper claim "up to roughly six times higher" corresponds to ratio 5.8 at p=1%, xi=0. Accurate.

### Extension figure (transfers)
- Code's transfer consumption formula matches paper equation (10).
- Code's transfer ratio matches paper equation (11): $1 + \tau(1-\delta_0\tau)(1-\phi\alpha)/(\phi\alpha)$, confirmed independent of $\eta$.
- Effective-phi construction for P/D with transfers is consistent with the paper's SDF logic.
- Paper claims verified: $\phi(1+\eta)=0.75$ (baseline, 25% loss), $\phi(1+\eta)=0.5$ (large, 50% loss), $\phi^{-\gamma}=160{,}000$ (large singularity).
- Large-singularity P/D is NA at $\tau=0$ (existence condition violated), consistent with paper discussion.

### Empirical figure (AI valuations)
- Downloads NASDAQ and S&P 500 index data, normalizes to Jan 2015 = 100. Straightforward index comparison.
- No per-share data combination issues — uses index-level prices throughout.
- Paper describes this as "illustrative" empirical content, consistent with spec requirement IV.8.b.

### Minor note
- The extension figure caption lists $p=0.5\%$, $\xi=5\%$, $\delta_0=0.5$ but does not document $\alpha_0=0.70$ (household's initial consumption share), which is used in the code. This parameter appears in the paper model as generic $\alpha$ but its numerical value is not stated in the figure caption or surrounding text.

## Reproducibility classification

| Object | Classification |
|--------|---------------|
| Table: P/D ratios | Locally reproducible |
| Figure: Extension panels | Locally reproducible |
| Figure: AI valuations | Locally reproducible (requires network for FRED/datahub downloads) |
| All theoretical propositions | Not code-generated; verified that code implements the stated formulas correctly |
