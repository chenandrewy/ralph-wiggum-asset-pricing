# tests/visual-figures.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 1m 3s
[ralph-garage/agent-logs/20260409T182005.683836-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T182005.683836-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures have readable labels, distinguishable series, and clear narrative messages.

---

## Figure 1: Valuations of AI Stocks vs. the Broader Market (Illustrative)

**VERDICT: PASS**

**REASON:** The single-panel figure is readable, distinguishable, and clearly conveys the valuation gap between AI-exposed firms and the S&P 500.

**Panel identification:** Single panel (no sub-panels).

### Readability — PASS
- Title at top is clearly legible.
- Y-axis label ("Price / earnings ratio") is readable.
- X-axis year tick labels (2015, 2017, 2019, 2021, 2023, 2025) are legible.
- Y-axis tick labels (15, 20, 25, 30, 35) are legible.
- Legend ("AI-Exposed Firms" in red, "S&P 500" in blue) is placed in the upper-left and is readable.
- Font sizes are adequate throughout; no text is cut off or overlapping.

### Distinguishability — PASS
- Two series use distinct colors: red for AI-exposed firms and blue for the S&P 500; clearly separable.
- Lines are thick enough to follow easily.
- Legend does not obscure any important data.
- The two series diverge substantially after ~2023, making the key pattern visually immediate. Before 2023 the lines are close but still distinguishable by color.

### Narrative clarity — PASS
- **From figure and caption alone:** AI-exposed firms trade at much higher P/E ratios than the broad market, with a dramatic widening since ~2023.
- **From figure and paper text:** The paper states the figure "illustrates the pattern of price-to-earnings ratios for AI-exposed firms versus the broader market since 2015" and that "the gap has widened dramatically since 2023, as advances in generative AI have accelerated expectations of transformative productivity gains." The figure supports the paper's motivating observation that AI stocks carry a valuation premium, which the theoretical model explains through a displacement-risk hedging channel.

---

## Figure 2: Government Transfers and the Singularity

**VERDICT: PASS**

**REASON:** Both panels have readable labels, clearly distinguishable series with large vertical separation, and the figure's main message is immediately apparent from the figure and caption alone.

**Panel identification:** Two panels — (a) AI Stock Valuations, (b) Household Consumption.

### Panel (a): AI Stock Valuations — PASS

#### Readability
- Axis labels ("Tax rate" on x, "P/D ratio (AI Stock)" on y) are legible.
- Tick labels are readable.
- Panel title "(a) AI Stock Valuations" is clear.
- Legend at the bottom is small but legible.

#### Distinguishability
- Two lines ("Baseline (eta = 0.5)" and "Large singularity (eta = 9)") are clearly separated vertically.
- Both lines use different dash patterns and are easy to tell apart spatially.
- No overlapping text, no cut-off text, no legend covering data.

### Panel (b): Household Consumption — PASS

#### Readability
- Axis labels ("Tax rate" on x, "Household Consumption Growth (% change)" on y) are legible.
- Tick labels are readable.
- Panel title "(b) Household Consumption" is clear.

#### Distinguishability
- Two lines are well separated — the large-singularity line rises steeply to very high values (thousands of percent), while the baseline line stays near zero.
- Legend at the bottom matches Panel (a). Lines are easy to tell apart.
- No overlapping text, no cut-off text, no legend covering data.

### Narrative clarity — PASS
- **From figure and caption alone:** Panel (a) shows that AI stock valuations (P/D ratios) decrease with higher tax rates and are much higher under a large singularity. Panel (b) shows household consumption growth increases with the tax rate, dramatically so under a large singularity. Government transfers funded by taxing AI owners can materially boost household consumption when singularity-driven output growth is large.
- **From figure and paper text:** Without transfers (tau = 0), a singularity actually reduces household consumption (displacement). Increasing tau under a large singularity produces substantial household consumption gains because enormous output growth swamps deadweight costs. The figure confirms this and reinforces the paper's argument that contingent transfer policies triggered by a singularity are worth designing in advance.
