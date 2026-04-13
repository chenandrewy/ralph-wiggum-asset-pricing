# tests/visual-figures.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 1m 43s
[ralph-garage/agent-logs/20260412T200023.660628-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T200023.660628-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures pass readability, distinguishability, and narrative clarity checks with no issues found.

---

## Figure 1 (page 2): AI Valuations

VERDICT: PASS

REASON: Both panels are readable and distinguishable, and the figure's message—historically elevated S&P 500 valuations and a widening NASDAQ-vs-S&P 500 gap since ~2015—is immediately clear from the figure and caption.

### Panel (a): S&P 500 P/D Ratio

- **Readability:** Panel title "(a) S&P 500 P/D Ratio" is legible. Y-axis label "Price / Trailing Dividend" is readable. X-axis tick labels (2003, 2008, 2013, 2018, 2022) are readable. Font sizes are adequate throughout.
- **Distinguishability:** Single dark line series with a light shaded region (confidence band or recession shading). The line is clearly visible and easy to follow. No ambiguity.
- **Assessment:** PASS. No issues.

### Panel (b): NASDAQ vs. S&P 500

- **Readability:** Panel title "(b) NASDAQ vs. S&P 500" is legible. Y-axis label "NASDAQ / S&P 500, Jan 2015 = 100" is readable, though slightly small—but still legible. X-axis tick labels (2003, 2008, 2013, 2018, 2022) are readable. Y-axis tick values (80, 100, 120, 140) are readable.
- **Distinguishability:** Single dark line series with a light shaded region. The line is clearly visible. No ambiguity or confusion between elements.
- **Assessment:** PASS. No issues.

### Narrative Clarity

- **From figure and caption alone:** The caption explains that Panel (a) shows the S&P 500 price-dividend ratio at historically elevated levels, and Panel (b) shows NASDAQ relative to the S&P 500, normalized to Jan 2015 = 100, with a rising ratio indicating growing relative valuations of AI/tech firms. The visual clearly conveys both points: Panel (a) shows a ratio climbing to ~80 by the end of the sample, and Panel (b) shows a ratio rising sharply from ~100 in 2015 to ~140+, with acceleration after ~2023.
- **From figure and paper text:** The opening paragraph uses this figure to motivate the paper's central question—why AI-exposed stocks have reached remarkable valuations. The paper argues this reflects a hedging motive under incomplete markets, where investors use publicly traded AI stocks to partially insure against displacement. The figure serves as the empirical anchor for this argument.

---

## Figure 2 (page 15): Extension Panels

VERDICT: PASS

REASON: Both panels are readable, series are clearly distinguishable, and the figure's main message is understandable from the figure and caption alone.

### Panel (a): AI Stock Valuations

- **Readability:** Title "(a) AI Stock Valuations" is readable. Y-axis label "P/D Ratio (AI Stocks)" is readable. X-axis label "Tax rate tau" is readable. Tick labels on both axes are clearly legible. The annotation "P/D → ∞ as τ → 0" is readable, rendered in bold blue with a white label background. Legend text at the bottom is readable with Greek letters for parameters. No text overlap or truncation issues.
- **Distinguishability:** The Baseline series (solid red line) and Large singularity series (dashed blue line) are clearly distinguishable via both color and linetype. The annotation arrow/label for the divergence does not obscure either line. Grid lines are visible but do not interfere with the data.
- **Assessment:** PASS. No issues.

### Panel (b): Consumption Growth

- **Readability:** Title "(b) Consumption Growth" is readable. Y-axis label "Household Consumption Growth in Singularity" is readable. X-axis label "Tax rate tau" is readable. Tick labels are legible on both axes. The y-axis uses a log scale with labeled breaks (0.50, 0.75, 1.00, 1.50, 2.00, 5.00). The "Catastrophe: 95% loss" annotation in blue is readable. The "50% loss" annotation in red is readable. Baseline trajectory annotations (0.7x, 0.8x) at specific tax rates are readable with white label fills. The "No change" label at y=1 is readable. The dashed black horizontal reference line at y=1 is clear.
- **Distinguishability:** The two series (solid red Baseline, dashed blue Large singularity) are clearly distinguishable by both color and linetype. The catastrophe dots at τ=0 use matching colors, making their association with each series clear. Annotations do not obscure either series line. The reference line (dashed black) is visually distinct from both data series.
- **Assessment:** PASS. No issues.

### Narrative Clarity

- **From figure and caption alone:** The figure shows that government transfers (funded by a tax rate τ on AI output) have two effects. Panel (a): transfers compress AI stock P/D ratios by reducing hedging demand; under a large-singularity scenario, the P/D ratio diverges at low tax rates, and transfers restore finite valuations. Panel (b): transfers dramatically improve household consumption in the singularity state; without transfers the household faces catastrophic losses (95% under large singularity, 50% under baseline), but even modest tax rates produce enormous consumption gains under the large-singularity parameterization.
- **From figure and paper text:** The paper adds the policy implication: in normal times, transfers are a "blunt and wasteful tool," but if an AI singularity produces explosive output growth, even inefficient redistribution becomes effective because the abundance of resources overwhelms the deadweight costs. The figure illustrates the sharp contrast between parameterizations—the large-singularity scenario has both more extreme problems and more dramatic benefits from transfers.
