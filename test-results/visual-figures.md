# tests/visual-figures.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 1m 9s
[ralph-garage/agent-logs/20260410T225642.526995-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260410T225642.526995-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures have readable labels, clearly distinguishable series, and self-evident narrative messages.

---

## Figure 1: Valuations of AI-Exposed Stocks vs. the Broader Market (page 2)

**VERDICT: PASS**

**REASON:** The figure is clean, with readable labels and legend, clearly distinguishable solid vs. dashed lines, and a self-evident message that AI-exposed stocks have dramatically outperformed the broader market since approximately 2023.

### Full Figure (Single Panel)

**Readability:**
- The y-axis label ("Normalized Price (Jan 2015 = 100)") is readable.
- The x-axis tick labels (2016, 2018, 2020, 2022, 2024, 2026) are readable.
- The legend is placed in the upper-left area and is readable. The text "NASDAQ Composite (AITech-Heavy)" and "S&P 500" are legible.
- Font sizes are adequate throughout.
- No text is cut off or overlapping.
- **Assessment: PASS**

**Distinguishability:**
- Two series are plotted: one solid line (NASDAQ Composite) and one dashed line (S&P 500), both in dark colors.
- The solid vs. dashed distinction is clearly visible along the entire length of both lines.
- The two lines diverge substantially after roughly 2023, making them easy to track individually. In the earlier period (2015–2022) they are closer together but the line-style difference keeps them separable.
- The legend does not obscure any meaningful portion of the plotted data.
- **Assessment: PASS**

**Narrative Clarity:**
- From caption alone: AI-exposed stocks (NASDAQ) have risen dramatically relative to the broader market (S&P 500) since roughly 2023, with both normalized to January 2015 = 100. The NASDAQ reaches roughly 500 while the S&P 500 reaches roughly 300.
- From paper text: The paper argues this premium reflects a hedging motive — investors use AI stocks to partially insure against an AI singularity that displaces their consumption.
- **Assessment: PASS**

---

## Figure 2: AI Valuations and Consumption under Transfers (page 13)

**VERDICT: PASS**

**REASON:** Both panels are readable, series are clearly distinguishable, and the figure's main message is understandable from the caption alone.

### Panel (a): AI Stock Valuations

**Readability:**
- Panel title "(a) AI Stock Valuations" is clearly readable.
- Y-axis label "P/D Ratio (AI Stock)" and x-axis label "Tax rate tau" are legible.
- Tick labels on both axes are readable. Legend at the bottom is clearly printed.
- **Assessment: PASS**

**Distinguishability:**
- Two series: solid line ("Baseline") and dashed line ("Large singularity"), clearly distinguishable by line style.
- The dashed line begins partway across the x-axis (around τ = 10%), corresponding to P/D being undefined at low τ for the large singularity case.
- Both lines are well separated vertically for most of the domain.
- **Assessment: PASS**

### Panel (b): Household Consumption

**Readability:**
- Panel title "(b) Household Consumption" is clearly readable.
- Y-axis label "Household Consumption Growth" and x-axis label "Tax rate tau" are legible.
- Tick labels are readable. Shared legend at the bottom is clear.
- **Assessment: PASS**

**Distinguishability:**
- Same two series (solid baseline, dashed large singularity), easy to tell apart.
- The dashed line rises steeply from about −0.5 to roughly 3.5, while the solid baseline rises gently from about −0.25 to roughly 0.1. The dramatic scale difference visually reinforces the paper's message.
- **Assessment: PASS**

**Narrative Clarity:**
- From caption alone: Panel (a) shows transfers compressing AI P/D ratios by reducing hedging demand; Panel (b) shows household consumption change in the singularity state, with a catastrophe at τ = 0 but large gains as τ increases under the large singularity.
- From paper text: The baseline uses η = 0.5, φ = 0.5 while the large singularity uses η = 9, φ = 0.05. Transfers are especially effective under the large singularity because explosive output growth swamps deadweight costs.
- **Assessment: PASS**
