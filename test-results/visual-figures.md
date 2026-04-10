# tests/visual-figures.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260409T194838.518416-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T194838.518416-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures are readable, distinguishable, and narratively clear.

---

## Figure 1 — Valuations of AI-Exposed Stocks vs. the Broader Market

VERDICT: PASS

REASON: The single-panel figure is readable, the two series are clearly distinguishable, and the caption conveys the main message without ambiguity.

### Panel: Full figure (single panel)

**Readability: PASS**
- The title/caption is fully legible and informative.
- The y-axis label ("Normalized Price (Jan 2015 = 100)") is readable.
- The x-axis shows year tick labels (2016, 2018, 2020, 2022, 2024, 2026) which are clearly readable.
- The legend in the upper-left is readable with adequate font size.
- Tick labels on both axes are legible.
- No text is overlapping, cut off, or too small.

**Distinguishability: PASS**
- The two series use distinct visual encodings: the NASDAQ Composite is a solid line and the S&P 500 is a dashed line.
- The lines are well separated for the majority of the plot, especially in the later years where the NASDAQ pulls sharply above the S&P 500.
- The legend is positioned in the upper-left corner and does not obscure any meaningful part of the data.

**Narrative clarity: PASS**
- From figure and caption alone: AI-exposed stocks (proxied by the NASDAQ Composite) have dramatically outpaced the broader market (S&P 500) in recent years, particularly from around 2023 onward. The normalization to January 2015 = 100 makes the comparison straightforward.
- From figure and paper text: The elevated valuations partly reflect a hedging motive — AI stocks serve as a partial hedge against AI singularity risk for investors who cannot diversify away displacement risk due to market incompleteness.

---

## Figure 2 — Extension Panels (AI Stock Valuations and Household Consumption)

VERDICT: PASS

REASON: Both panels are readable with clearly distinguishable series, and the caption provides sufficient context to understand the figure's message.

### Panel (a): AI Stock Valuations

**Readability: PASS**
- The panel title "AI Stock Valuations" is clearly readable.
- The y-axis label ("P/D Ratio (AI Stock)") and x-axis label ("Tax rate τ") are legible.
- Tick labels on both axes are readable.
- The legend is legible, showing two series: "Baseline (η=0.5, φ=0.5)" and "Large singularity (η=9, φ=0.05)."

**Distinguishability: PASS**
- The two series use different line styles (solid vs. dashed) and different colors, making them easy to distinguish.
- The baseline series is a gently declining curve across the full range of τ, while the large-singularity series appears only for higher τ values, creating clear visual separation.
- The legend does not obscure any plotted data.

### Panel (b): Household Consumption

**Readability: PASS**
- The panel title "Household Consumption" is clearly readable.
- The y-axis label ("Consumption Change (Singularity State)") and x-axis label ("Tax rate τ") are legible.
- Tick labels are readable. The y-axis uses percentage formatting.
- The legend is legible with the same two-series encoding.

**Distinguishability: PASS**
- The two series are clearly distinguishable via different line styles and colors, consistent with Panel (a).
- The dramatic upward sweep of the large-singularity line versus the modest rise of the baseline line makes the contrast visually immediate.
- No overlap or occlusion issues.

**Narrative clarity: PASS**
- From figure and caption alone: Government transfers (taxing output and redistributing) compress AI stock P/D ratios by reducing hedging demand, and dramatically improve household consumption in the singularity state when the singularity is large.
- From figure and paper text: The P/D ratio is undefined at τ = 0 under the large-singularity calibration because marginal utility becomes extreme enough that the pricing sum diverges, illustrating the severity of the incomplete-markets problem.
