# tests/factcheck-exhibits.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 4m 55s
[ralph-garage/agent-logs/20260409T184838.243845-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T184838.243845-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code; no artifacts, labeling errors, or unsupported features found.

## Figure 1: Valuations of AI Stocks vs. the Broader Market (Illustrative)

**Description:** Time-series plot (2015–2025) of price-earnings ratios for AI-exposed firms vs. the S&P 500. AI-exposed firms show a dramatic divergence starting around 2023, reaching ~75 by 2025.

### Suspicious features

1. **Hardcoded data with no external data file.** The P/E series (`pe_ai`, `pe_market`) are defined as literal vectors in `code/generate-exhibits.R:189–190` with no external CSV or API call. No local data files exist under `/workspace/data/`.

2. **Steep AI P/E spike (42 → 62 → 75 from 2023–2025).** The trajectory implies ~80% P/E growth over two years.

3. **Y-axis does not start at zero.** The default ggplot range (~18–76) visually amplifies the gap.

### Code check

1. The caption explicitly says "(Illustrative)" and the paper text (line 39) says "based on approximate values from public sources." The hardcoded values are within plausible ranges for the period: S&P 500 trailing P/E was 18–28 over 2015–2025; mega-cap AI firms (NVIDIA, Microsoft, Alphabet) saw P/Es in the 40–75 range post-2023. The illustrative label makes exact verification unnecessary; directional correctness suffices.

2. The steep AI spike reflects the post-ChatGPT AI boom. NVIDIA's P/E alone exceeded 60 in this period. A basket of AI-exposed firms at 75 in 2025 is aggressive but not implausible for an illustrative figure.

3. Not starting the y-axis at zero is standard practice for ratio plots and does not misrepresent the data.

**Exhibit verdict: PASS** — Illustrative data is transparently labeled and directionally plausible.

---

## Table 1: Price-Dividend Ratios: AI Stocks vs. Non-AI Stocks

**Description:** Grid of model-implied P/D ratios across singularity probability $p$ (0.1%–1.0%) and extinction probability $\xi$ (0%–20%). Shows AI stocks, non-AI stocks, and their ratio.

### Suspicious features

1. **Extreme P/D at high $p$.** At $p = 1\%$, $\xi = 0\%$, AI P/D = 76.4 — roughly 7× the non-AI value (13.3). This explodes because $K \to 1$.

2. **Non-AI P/D increases with $p$ despite non-AI stocks losing share.** Non-AI P/D rises from 9.8 ($p = 0.1\%$) to 13.3 ($p = 1.0\%$) at $\xi = 0\%$.

### Code check

1. **Verified numerically.** At $p = 1\%$, $\xi = 0\%$: $K_{AI} = 0.9871$, giving $P/D = 0.9871 / 0.0129 = 76.4$. The near-unit $K$ arises because the SDF-weighted singularity payoff ($\phi^{-\gamma} (1+\eta)^{-\gamma} \gamma_{AI} = 10.11$) is large: severe household displacement ($\phi = 0.5$) raises marginal utility, amplifying the value of AI dividends. This is the core hedging mechanism of the paper and is mathematically correct.

2. **Non-AI P/D increase is correct.** Non-AI dividend growth in singularity is $\gamma_{non} = 0.8 \times 1.5 = 1.2$, but the SDF factor $\phi^{-\gamma}(1+\eta)^{-\gamma} = 3.16$ means the SDF-weighted singularity payoff is $3.16 \times 1.2 = 3.79 > 1$. Since the singularity state has high marginal utility, even non-AI stocks (which lose share but benefit from aggregate growth) carry a premium. Higher $p$ amplifies this, raising non-AI P/D. Economically sound: non-AI stocks still pay something in the high-marginal-utility singularity state.

3. **Spot-checked five rows** against independent R computation: $p = 0.5\%/\xi = 0\%$ (AI = 17.5, Non = 11.1), $p = 1.0\%/\xi = 0\%$ (AI = 76.4, Non = 13.3), $p = 0.5\%/\xi = 5\%$ (AI = 16.7, Non = 11.0), $p = 0.8\%/\xi = 20\%$ (AI = 21.7, Non = 11.4). All match the table to the displayed precision.

4. **Parameter footnote matches code:** $\beta = 0.96$, $g = 0.02$, $\gamma = 4$, $\phi = 0.5$, $\eta = 0.5$, $\theta = 0.15$, $\Delta\theta = 0.2$ — all verified at `code/generate-exhibits.R:18–24`.

**Exhibit verdict: PASS** — All values verified; extreme P/D at high $p$ is a correct model property.

---

## Figure 2: Government Transfers and the Singularity

**Description:** Two-panel figure. Panel (a) shows AI stock P/D ratio vs. tax rate $\tau$ for baseline ($\eta = 0.5, \phi = 0.5$) and large singularity ($\eta = 9, \phi = 0.05$). Panel (b) shows household consumption growth in the singularity state vs. $\tau$.

### Suspicious features

1. **Large singularity line in Panel (a) starts partway through the $\tau$ range** — it does not appear at low $\tau$, unlike the baseline which spans the full range.

2. **Large singularity consumption growth in Panel (b) reaches very high values (~7×)** while baseline stays modest (~1.4×).

3. **"No change" annotation positioned at $y = 1.3$** rather than at the reference line $y = 1$.

### Code check

1. **Truncated large-singularity line is correct.** At $\tau = 0$, $\phi_{eff} = 0.05$, giving $K = 2.37 > 1$ (verified numerically). The code returns `NA` when $K \geq 1$ (`generate-exhibits.R:46`), and Panel (a) filters NAs (`filter(!is.na(pd_ai))` at line 155). The line only appears once $\phi_{eff}$ grows large enough (via transfers) to bring $K < 1$. This is economically correct: without transfers, the SDF diverges because extreme displacement ($\phi = 0.05$) creates enormous marginal utility in the singularity state.

2. **High consumption growth verified.** At $\tau = 0.7$: consumption\_growth for large singularity = $0.05 \times 10 + 0.7 \times (1 - 0.35) \times \frac{1 - 0.035}{0.70} \times 10 = 0.5 + 0.7 \times 0.65 \times 1.379 \times 10 = 0.5 + 6.27 = 6.77$. The enormous transfer base (10× aggregate growth) swamps the deadweight costs, exactly as the paper argues (line 280: "the enormous output growth swamps the deadweight costs").

3. **"No change" annotation is a label, not a data point.** The text at $(0.55, 1.3)$ labels the dashed reference line at $y = 1$ (`code/generate-exhibits.R:168–169`). Placing annotation text slightly above its reference line is standard practice. The dashed line itself is correctly at $y = 1$.

4. **Transfer formula matches paper.** Equation (8) in the paper: $c^H_{post} = \phi \alpha (1+\eta) C_t (1+g) + \tau(1-\delta_0 \tau)(1-\phi\alpha)(1+\eta) C_t (1+g)$. The code's `consumption_growth` function (`generate-exhibits.R:112–113`) divides by $\alpha C_t (1+g)$ to get the ratio, yielding $\phi(1+\eta) + \tau(1-\delta_0\tau)(1-\phi\alpha)/\alpha \cdot (1+\eta)$. Verified consistent.

5. **Paper's inline claims match the figure.** The text states "consumption halves under the large singularity ($\phi(1+\eta) = 0.5$)" — $0.05 \times 10 = 0.5$ ✓ — and "falls by 25% under the baseline ($\phi(1+\eta) = 0.75$)" — $0.5 \times 1.5 = 0.75$ ✓.

**Exhibit verdict: PASS** — All features traced to correct code logic and consistent with the paper's economic arguments.
