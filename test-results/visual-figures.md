# tests/visual-figures.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 2s
[ralph-garage/agent-logs/20260411T101504.846489-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260411T101504.846489-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures have readable labels, distinguishable series, and clear narrative messages.

---

## Figure 1 (page 2)

VERDICT: PASS

REASON: The figure clearly shows two distinguishable time series with readable labels, and the divergence between NASDAQ and S&P 500 is immediately apparent.

### Panel assessment (single panel, no sub-panels)

**Readability:**
- The title/caption is rendered above the figure and is fully legible.
- The y-axis label ("Normalized Price (Jan 2015 = 100)") is readable.
- The x-axis tick labels (2016, 2018, 2020, 2022, 2024, 2026) are readable.
- The y-axis tick labels (100, 200, 300, 400, 500) are readable.
- The legend in the upper-left corner is readable, with clear labels: "NASDAQ Composite (AITech-Heavy)" and "S&P 500."
- Font sizes are adequate throughout.
- No text is overlapping, cut off, or too small.

**Distinguishability:**
- The two series use distinct line styles: solid for NASDAQ and dashed for S&P 500. They are immediately separable.
- The legend does not obscure any meaningful portion of the plotted data.
- The visual separation between the two series grows over time, making the divergence instantly visible.
- No ambiguity in color or encoding.

**Narrative clarity (figure and caption alone):**
The figure shows that since 2015, the NASDAQ Composite (AI/tech-heavy) has appreciated far more than the S&P 500, with the gap widening dramatically after roughly 2020. A reader can immediately grasp that AI-exposed stocks carry a large valuation premium relative to the broader market.

**Narrative clarity (figure and paper text):**
The paper argues this valuation gap reflects a hedging motive under incomplete markets: investors cannot trade restricted AI equity, so publicly traded AI stocks serve as the only partial hedge against labor displacement, pushing their prices above broader-market levels. The figure provides the motivating empirical fact for the theoretical model that follows.

---

## Figure 2 (page 14)

VERDICT: PASS

REASON: Both panels are clearly readable with distinguishable series and a self-explanatory caption.

### Panel (a): AI Stock Valuations

**Readability:** PASS. The panel title "AI Stock Valuations" is clear. The y-axis label ("P/D ratio (AI Stock)") and x-axis label ("Tax Rate τ") are legible. Tick labels on both axes are readable. The legend at the bottom is clearly printed. Font sizes are adequate throughout.

**Distinguishability:** PASS. Two line series are plotted: a solid line for the baseline (η = 0.5, φ = 0.5) and a dashed line for the large singularity (η = 9, φ = 0.05). The two lines are well-separated spatially and use distinct line styles (solid vs. dashed). The large-singularity line starts from around τ = 10% (reflecting the existence condition discussed in the text) and both lines are easy to track. No legend or inset occludes the data.

### Panel (b): Household Consumption

**Readability:** PASS. The panel title "Household Consumption" is clear. The y-axis label ("Household Consumption Growth") and x-axis label ("Tax Rate τ") are legible. Tick labels are readable. The legend is shared with Panel (a) and placed below both panels, clearly printed.

**Distinguishability:** PASS. The two series again use solid vs. dashed lines and are well-separated. The baseline curve is nearly flat (modest gains), while the large-singularity curve rises steeply, making them easy to distinguish both by line style and by shape. Catastrophe markers at τ = 0 are visible. No overlapping or occluded elements.

### Narrative clarity

**From figure and caption alone:** The caption explains that Panel (a) shows how government transfers compress AI stock P/D ratios by reducing hedging demand, and Panel (b) shows how transfers affect household consumption in the singularity state. The key message is clear: under a large singularity, even modest tax rates produce enormous consumption gains (Panel b) while reducing the extreme hedge valuations (Panel a). The baseline case shows much more muted effects.

**From figure and paper text:** The paper text adds that the large-singularity P/D ratio is undefined at τ = 0 because the existence condition is violated (marginal utility diverges), explaining why that line only begins at positive τ. The text also clarifies the parameter choices and the policy implication that contingent transfer policies triggered by a singularity may be worth designing in advance.
