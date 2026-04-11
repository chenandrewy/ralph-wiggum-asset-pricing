# tests/visual-figures.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260411T103039.162885-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T103039.162885-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures are readable, distinguishable, and narratively clear.

---

## Figure 1 (page 2)

VERDICT: PASS

REASON: The single-panel figure is readable, the two series are clearly distinguishable, and the main message—that AI-exposed stocks have dramatically outpaced the broader market since roughly 2020—is immediately apparent from the figure and caption alone.

### Per-panel findings (single panel)

**Readability**
- The title/caption is rendered as text above the figure and is fully legible.
- The y-axis label ("Normalized Price (Jan 2015 = 100)") is readable and correctly oriented.
- The x-axis tick labels (2016, 2018, 2020, 2022, 2024, 2026) are clearly spaced and legible.
- The y-axis tick labels (100, 200, 300, 400, 500) are legible.
- The legend ("NASDAQ Composite (AITech-Heavy)" and "S&P 500") is rendered in a readable font size in the upper-left area of the plot, and its placement does not obscure any data.
- Assessment: **No problems.**

**Distinguishability**
- The two series use different line styles: a solid line for NASDAQ and a dashed line for the S&P 500. This encoding matches what the caption describes.
- The two lines are spatially close in the early part of the sample (2015–2019) but remain visually separable because of the solid-vs-dashed distinction.
- From 2020 onward the lines diverge substantially, making them trivially distinguishable.
- The legend does not obscure any meaningful portion of the plotted data.
- Assessment: **No problems.**

**Narrative clarity**
- *From figure and caption alone:* The figure shows that AI-and-tech-heavy NASDAQ has risen far more steeply than the broad S&P 500 since around 2020, with both indices normalized to the same starting point in January 2015. The divergence accelerates sharply after 2022–2023, consistent with the AI boom. A reader immediately grasps that AI-exposed stocks carry a large valuation premium relative to the broader market.
- *From figure and paper text:* The paper argues this valuation gap reflects a hedging motive under incomplete markets—investors cannot trade restricted AI equity, so publicly traded AI stocks serve as the only available partial hedge against labor-income displacement, pushing their prices above non-AI stocks. The figure motivates the entire paper by documenting the empirical pattern the model seeks to explain.
- Assessment: **No problems.**

---

## Figure 2 (page 14)

VERDICT: PASS

REASON: Both panels are readable and distinguishable, and the caption conveys the main message clearly.

### Panel identification

The figure has two panels:
- **(a) AI Stock Valuations** (left) — P/D ratio versus tax rate
- **(b) Household Consumption** (right) — consumption change (%) versus tax rate

### Panel (a): AI Stock Valuations

**Readability**
- The panel title "(a) AI Stock Valuations" is legible. The y-axis label "P/D of AI Stocks" and x-axis label "Tax Rate τ" are clear and appropriately sized. Tick labels on both axes (0% to 60% on x, 0 to 16 on y) are readable. The legend at the bottom is legible.
- Assessment: **No problems.**

**Distinguishability**
- Two series are plotted: a solid line (Baseline) and a dashed line (Large singularity). They are clearly separated in both line style and vertical position. The dashed line starts from a higher P/D value and drops steeply; the solid line is flatter and lower. Both are easily distinguishable. The vertical dashed marker near 20–30% tax rate is visible and does not obscure the main series.
- Assessment: **No problems.**

### Panel (b): Household Consumption

**Readability**
- The panel title "(b) Household Consumption" is legible. The y-axis label "Household Consumption Growth" and x-axis label "Tax Rate τ" are clear. Tick labels are readable. The annotation text inside the panel (marking the catastrophe point at τ = 0) is small but still legible.
- Assessment: **No problems.**

**Distinguishability**
- Two series are again shown with the same solid/dashed encoding. They are clearly separated. The dashed line (Large singularity) shows dramatic growth from negative values at τ = 0 to very large positive values, while the solid Baseline line shows only modest improvement. A shared legend at the bottom clearly maps line styles to parameter sets.
- Assessment: **No problems.**

### Narrative clarity
- *From figure and caption alone:* The figure communicates that (a) government transfers (higher τ) compress AI stock P/D ratios by reducing hedging demand, and (b) under a large singularity, even modest transfers produce enormous consumption gains because explosive output growth overwhelms deadweight costs, while absent transfers the household faces a consumption catastrophe. The two parameter regimes (baseline vs. large singularity) show strikingly different magnitudes of response.
- *From figure and paper text:* The paper text adds that the P/D ratio is undefined at τ = 0 under the large singularity because the existence condition is violated. The vertical dashed line in Panel (a) marks where finite P/D ratios emerge. The text also explains the policy implication: contingent transfers triggered by a singularity may be worth designing in advance, since the abundance of resources from explosive growth makes even inefficient redistribution effective.
- Assessment: **No problems.**
