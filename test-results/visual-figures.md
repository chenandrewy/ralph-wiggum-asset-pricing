# tests/visual-figures.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 1m 53s
[ralph-garage/agent-logs/20260412T202602.584894-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260412T202602.584894-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS
REASON: Both figures pass readability, distinguishability, and narrative clarity requirements.

---

## Figure 1 (page 2): AI Stock Valuations — Motivating Evidence

**VERDICT: PASS**
**REASON:** Both panels are readable, series are clearly distinguishable, and the figure's main message — that AI-related valuations have risen to historically elevated levels both in absolute and relative terms — is immediately apparent from the figure and caption.

### Panel (a): S&P 500 P/D Ratio

- **Readability:** PASS. Panel title, y-axis label ("Price / Trailing Dividend"), and x-axis tick labels (2003–2023) are all readable at reasonable font sizes. No text is overlapping or cut off.
- **Distinguishability:** PASS. Single dark line series against a light grid background. Grid lines are subtle enough not to compete with the data series. No legend needed for a single series.

### Panel (b): NASDAQ vs. S&P 500

- **Readability:** PASS. Panel title, y-axis label ("NASDAQ / S&P 500"), and x-axis tick labels are all readable. The dashed horizontal reference line at 100 is labeled. No text overlap or truncation.
- **Distinguishability:** PASS. Single dark line series with a dashed reference line using different line styles (solid vs. dashed), easy to tell apart. Grid is light and does not interfere.

### Narrative clarity

- **From figure and caption alone:** The S&P 500 price-dividend ratio has reached historically elevated levels (Panel a), and the NASDAQ Composite has appreciated substantially relative to the S&P 500 since roughly 2015 (Panel b), indicating that AI and technology firms command growing relative valuations.
- **From figure and paper text:** The figure motivates the paper's central question. AI stocks carry a valuation premium — priced higher relative to dividends than non-AI stocks. The paper builds a model in which this premium arises because investors use publicly traded AI stocks as an imperfect hedge against displacement risk from AI.

---

## Figure 2 (page 15): Extension Panels — Transfers and Singularity

**VERDICT: PASS**
**REASON:** Both panels are readable and distinguishable, and the figure's message about transfers cushioning singularity-driven displacement is clear from the caption alone.

### Panel (a): AI Stock Valuations

- **Readability:** PASS. Panel title "AI Stock Valuations" is legible. Y-axis label "P/D Ratio (AI Stocks)" and x-axis label "Tax rate τ" are readable. Tick labels on both axes are clear. Legend at the bottom is readable, distinguishing "Baseline" and "Large singularity" lines with parameter values. The annotation "P/D = ∞ at τ = 0" is small but legible. X-axis ticks (0%–40%) are well-spaced.
- **Distinguishability:** PASS. Two lines — dashed (Baseline) and solid (Large singularity) — are clearly distinct via line style and spatial separation. Legend encodes them unambiguously.

### Panel (b): Consumption Growth

- **Readability:** PASS. Panel title "Consumption Growth" is legible. Y-axis label "Household Consumption Change in Singularity" is readable. X-axis label "Tax rate τ" is clear. The boxed annotation "Catastrophe: 50% loss" with arrow at τ = 0 is readable and helpful.
- **Distinguishability:** PASS. Two series (Baseline dashed, Large singularity solid) are clearly distinct through line style and large vertical separation. The "Catastrophe" annotation is clearly associated with the large-singularity scenario.

### Narrative clarity

- **From figure and caption alone:** Government transfers (tax rate τ) compress AI stock P/D ratios by reducing hedging demand (Panel a). Absent transfers, households face catastrophic consumption losses under a large singularity, but even modest transfers produce enormous consumption gains because explosive output growth overwhelms deadweight costs (Panel b).
- **From figure and paper text:** The consumption-transfer ratio is independent of the productivity jump η, meaning transfers always improve household welfare when deadweight costs don't consume the entire transfer. Transfers are a "blunt and wasteful tool" in normal times but become transformatively effective under singularity conditions.
