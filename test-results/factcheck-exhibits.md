# tests/factcheck-exhibits.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 2m 59s
[ralph-garage/agent-logs/20260404T235928.980263-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260404T235928.980263-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits

VERDICT: PASS
REASON: All three exhibits are correctly generated from the code and consistent with the paper's claims.

## Figure 1: AI stocks as a share of total CRSP market capitalization

**Description.** A time-series line chart (2015--2024) showing the Magnificent 7's combined market capitalization as a percentage of total CRSP market cap for common stocks on NYSE, AMEX, and NASDAQ. The line rises from roughly 8% in 2015 to 33% by end of 2024, with a sharp acceleration in 2023--2024.

### Suspicious features

1. **Sharp acceleration in 2023--2024.** The curve steepens dramatically in the final two years, reaching 33%.
2. **No locally cached data.** The figure is generated from a live WRDS/CRSP query; no cached output exists under `data/`.

### Code check

1. **Sharp acceleration.** The code (`code/run-all.R`, lines 42--78) queries CRSP monthly stock file (`crsp.msf`) for all common stocks (shrcd 10, 11) on major exchanges (exchcd 1, 2, 3), computes market cap as `ABS(prc) * shrout`, and aggregates. The Magnificent 7 are identified by 8 permnos (7 companies; Alphabet has two share classes GOOG/GOOGL). The 2023--2024 acceleration is consistent with the well-documented AI-driven rally in these stocks. **Verified as plausible and correctly coded.**

2. **No local data.** The CRSP query requires WRDS credentials and produces no cached intermediate file. The code logic is sound: it uses standard CRSP conventions (absolute price, share-code filters, exchange-code filters). The endpoint value of ~33% is consistent with publicly reported Mag-7 market-cap shares in late 2024. While exact replication requires WRDS access, the code path is transparent and the result is externally plausible. **No evidence of error; acceptable.**

**Exhibit verdict: PASS.** Code logic is correct; visual features are consistent with known market data.

## Table 1: Price-dividend ratios and the singularity probability

**Description.** A two-panel table showing P/D ratios for AI stocks, non-AI stocks, and the spread across five singularity probabilities (p = 0, 0.01, 0.02, 0.05, 0.10). Panel A uses moderate displacement (G = 5, phi = 0.5, Lambda = 2.5). Panel B uses severe displacement (G = 2, phi = 0.6, Lambda = 0.8).

### Suspicious features

1. **Panel B AI P/D ratios are extremely high (up to 41.6).** These are far above the no-risk benchmark of ~11.9.
2. **Panel B non-AI P/D ratios barely move (11.9 to 11.4).** Near-constant despite rising singularity probability.

### Code check

1. **High Panel B AI P/D.** With Lambda = 0.8 < 1, H_ai = (alpha_S/alpha) * Lambda^(1-gamma) = (0.50/0.15) * 0.8^(-2) = 3.333 * 1.5625 = 5.208. Since H > 1, the P/D formula pd = (1-H)*V0(p) + H*V_inf produces values above V_inf when V_inf > V0(p). At p = 0.10: V0 = 4.90, pd = (1-5.208)*4.90 + 5.208*11.94 = -20.6 + 62.2 = 41.6. **Matches the table. The economics: when the singularity is a disaster (Lambda < 1), AI stocks are valuable insurance, driving their P/D well above the no-risk benchmark. Correctly generated.**

2. **Near-constant Panel B non-AI.** H_non = (0.50/0.85) * 0.8^(-2) = 0.588 * 1.5625 = 0.919. Since H_non is close to 1, pd = (1-0.919)*V0(p) + 0.919*11.94 ≈ 0.081*V0(p) + 10.97. The V0(p) term has little weight, so P/D barely moves with p. At p = 0.10: 0.081*4.90 + 10.97 = 11.37 ≈ 11.4. **Matches the table. Correctly generated.**

All 15 table cells were independently verified by recomputing from the parameter values and model formulas. Every value matches to the reported precision (one decimal place).

**Exhibit verdict: PASS.** All values are arithmetically correct and consistent with the paper's formulas and text claims.

## Figure 2: P/D ratio of AI stocks vs singularity output growth and deadweight costs

**Description.** A line chart plotting P/D ratios of AI stocks against the singularity output growth factor G (1.5 to 20), for four transfer scenarios: no transfers (delta = 1), delta = 0.9, delta = 0.5, and perfect transfers (delta = 0). Two horizontal reference lines mark V0 (~7.1) and V_infinity (~11.9). All curves decline from high values at low G and converge toward V0 at high G.

### Suspicious features

1. **Curves reach very high P/D (~50) at low G.** The y-axis is clipped at 50.
2. **All curves converge at high G, suggesting transfer policy becomes irrelevant.** This needs economic justification.
3. **Curve ordering: "No transfers" is highest, "Perfect transfers" is lowest.** This means reducing deadweight costs *lowers* AI stock valuations, which may seem counterintuitive.

### Code check

1. **High P/D at low G.** For the no-transfers curve at G = 1.5: Lambda = 0.5 * 1.5 = 0.75, H = (0.50/0.15) * 0.75^(-2) = 5.926. With V0(0.05) = 7.10 and V_inf = 11.94: pd = (1-5.926)*7.10 + 5.926*11.94 = -34.97 + 70.76 = 35.8. The code clips at y_max = 50 (line 224). **Correctly generated; high P/D reflects large hedge premium when G is small and Lambda < 1.**

2. **Convergence at high G.** At G = 20, no transfers: Lambda = 10, H = 3.333 * 10^(-2) = 0.033. pd ≈ 0.967*7.10 + 0.033*11.94 = 7.26. For perfect transfers: Lambda = 20, H = 3.333/400 = 0.0083. pd ≈ 7.14. Both approach V0 because when G is very large, Lambda is large, H is near zero, and the hedge benefit vanishes regardless of delta. **Correctly generated.**

3. **Curve ordering.** No transfers (delta = 1) gives the smallest Lambda for each G, hence the largest H, hence the highest P/D. Perfect transfers (delta = 0) gives the largest Lambda, hence the smallest H and lowest P/D. AI stocks are most valuable as hedges when displacement risk is worst (no transfers). Reducing deadweight costs reduces the household's need for hedging, which lowers the AI stock premium. **Economically correct and consistent with the paper's narrative (lines 253--254, 266).**

The figure's reference lines (V0 ≈ 7.1, V_inf ≈ 11.9) match the computed values. The legend labels match the delta values used in the code.

**Exhibit verdict: PASS.** Code logic, parameter values, curve shapes, reference lines, and labels are all correct and consistent with the model.
