# tests/factcheck-exhibits.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 4m 29s
[ralph-garage/agent-logs/20260404T234508.986296-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260404T234508.986296-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: FAIL
REASON: Figure 2 caption misidentifies $V_0$ as the P/D ratio "with no singularity risk" when it actually includes singularity risk (p=0.05).

## Figure 1: AI stock market cap share (fig:opening)

**Description.** Line chart showing the Magnificent 7 stocks' share of total CRSP market capitalization from January 2015 to December 2024. The share rises from under 10% to approximately 33%.

### Suspicious features

1. **End-of-sample label reads "33%" but paper text says "nearly 30%."** The introduction (line 43 of `paper.tex`) states the share grew to "nearly 30%," while the figure labels the endpoint at 33%. These are inconsistent, though "nearly 30%" may loosely refer to a sustained level rather than the year-end peak.

2. **No cached data to verify the 33% figure.** The code queries WRDS/CRSP live (`code/run-all.R:44–64`). No cached data file exists under `data/`. The 33% Mag7 share of total CRSP equity market cap by end-2024 is broadly consistent with public reporting, but the exact value cannot be independently verified from local files.

3. **Permno-to-ticker mapping is hardcoded and unverifiable locally.** The code uses 8 permnos for 7 companies (Alphabet has two share classes). The permnos are standard in the CRSP database, and the resulting figure is plausible, but no local lookup table confirms the mapping.

### Code check

- `code/run-all.R:42`: hardcodes `ai_permnos <- c(14593, 84788, 14542, 90319, 13407, 10107, 86580, 93436)` for AAPL, AMZN, GOOG, GOOGL, META, MSFT, NVDA, TSLA.
- `code/run-all.R:45–61`: SQL query pulls all common stocks (shrcd 10/11) on NYSE/AMEX/NASDAQ with valid prices, 2015–2024.
- `code/run-all.R:73–78`: aggregates monthly market cap shares correctly.
- The code logic is sound. The figure is plausible but locally unverifiable.

**Exhibit verdict: PASS** — No artifact or coding error detected. The text mismatch ("nearly 30%" vs 33%) is in the body text, not the exhibit itself; the exhibit label is self-consistent. Lack of cached data prevents exact verification but the figure is plausible.

## Table 1: Price-dividend ratios and the singularity probability (tab:pd)

**Description.** Two-panel table showing P/D ratios for AI stocks, non-AI stocks, and their spread across five singularity probabilities (p = 0, 0.01, 0.02, 0.05, 0.10). Panel A: moderate displacement (G=5, φ=0.5, Λ=2.5). Panel B: severe displacement (G=2, φ=0.6, Λ=0.8).

### Suspicious features

1. **Panel B AI stocks show P/D ratios rising sharply to 41.6.** At p=0.10 with Λ=0.8, the AI P/D ratio reaches 41.6 — nearly 4× the no-risk benchmark of 11.9.

### Code check

Manual verification of key values confirms the code is correct:

- Parameters: β=0.96, g=0.02, γ=3, α=0.15, α_S=0.50. R = 0.96 × 1.02^(−2) ≈ 0.9227. V_inf = R/(1−R) ≈ 11.94.
- Panel A (Λ=2.5): H_ai = (0.50/0.15) × 2.5^(−2) = 0.5333. At p=0.01: pd = (1−0.5333)×V0(0.01) + 0.5333×11.94 = 0.4667×10.56 + 6.37 ≈ 11.3. ✓
- Panel B (Λ=0.8): H_ai = (0.50/0.15) × 0.8^(−2) = 5.208. At p=0.10: V0(0.10) = 0.90×0.9227/(1−0.90×0.9227) = 0.8304/0.1696 ≈ 4.895. pd = (1−5.208)×4.895 + 5.208×11.94 = −20.60 + 62.18 ≈ 41.6. ✓
- All table entries verified against `code/run-all.R:149–157` and `paper/exhibits/table-pd-ratios.tex`.
- The high P/D in Panel B is a genuine model prediction: with γ=3 and Λ<1, H>1, so the hedging term dominates and P/D rises with p. The economic logic is correct.

**Exhibit verdict: PASS** — All values verified by manual computation. No artifacts or errors.

## Figure 2: P/D ratio vs singularity output growth and deadweight costs (fig:transfers)

**Description.** Four curves showing the P/D ratio of AI stocks as a function of singularity output growth factor G (1.5 to 20), for different deadweight cost parameters (δ = 1, 0.9, 0.5, 0). Two horizontal reference lines mark V_0 and V_∞.

### Suspicious features

1. **Caption misidentifies V_0.** The note states: "$V_0$ marks the P/D ratio with no singularity risk; $V_\infty$ marks the no-singularity-risk benchmark." Both phrases describe the same concept ("no singularity risk"), which is contradictory. Per the paper's own definition (line 167 of `paper.tex`), $V_0 = (1-p)R/[1-(1-p)R]$ includes the singularity probability p=0.05. V_0 is the P/D ratio **with** singularity risk but **without** hedging benefit (H=0) — i.e., the asymptote as G→∞. Only V_∞ = R/(1−R) is the no-singularity-risk benchmark (equivalent to p=0).

2. **All curves converge toward V_0 ≈ 7.1 rather than V_∞ ≈ 11.9 at large G.** This is correct: as G→∞ with γ>1, H→0, so P/D→V_0(p). The reference line placement is correct even though the caption description is wrong.

### Code check

- `code/run-all.R:189–209`: For each δ, Lambda = (1−δφ)G. H = (α_S/α) × Lambda^(1−γ). P/D = (1−H)×V0 + H×V_inf. All formulas match the paper's Proposition.
- `code/run-all.R:229`: V0_fig horizontal line placed at V0(0.05) ≈ 7.10. Correct computation.
- `code/run-all.R:233`: V_inf horizontal line placed at 11.94. Correct.
- `code/run-all.R:230`: Label text says V_0, placed at V0_fig. The line itself is correctly positioned.
- The **curves and reference lines are correctly generated**. The error is solely in the caption note at `paper/paper.tex:261`, which incorrectly describes V_0 as "the P/D ratio with no singularity risk." The correct description would be: "the P/D ratio with singularity risk but no hedging benefit (H=0), i.e., the limit as G→∞."

**Exhibit verdict: FAIL** — Caption labeling error: V_0 is described as "no singularity risk" but it actually incorporates singularity risk with p=0.05. This mischaracterizes the reference line and could mislead readers about its economic interpretation.
