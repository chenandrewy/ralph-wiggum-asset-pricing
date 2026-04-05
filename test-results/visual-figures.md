# tests/visual-figures.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260404T235928.981113-0400_visual-figures_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260404T235928.981113-0400_visual-figures_claude_claude-opus-4-6.log)

# visual-figures

VERDICT: PASS

REASON: Both figures are readable, distinguishable, and convey their messages clearly.

---

## Figure 1 (page 2) — Magnificent 7 Market Cap Share

VERDICT: PASS

REASON: The single-panel figure is readable, distinguishable, and clearly conveys its message.

### Panel identification
Figure 1 is a single-panel time-series line chart showing "AI stocks [Magnificent 7]" market capitalization as a share of total CRSP market capitalization, from roughly 2016 to 2024.

### Readability: PASS
- The title/header "AI stocks [Magnificent 7]" is clearly legible at the top of the plot.
- The y-axis label ("Share of total CRSP market capitalization (%)") is readable.
- Tick labels on both axes are legible with adequate font size.
- The annotation "30%" at the terminal data point is clear and well-placed.
- The caption and notes beneath the figure are readable.
- No text is overlapping, cut off, or too small.

### Distinguishability: PASS
- There is only a single plotted series (a dark line with light blue/gray shading beneath it), so there is no issue of confusing multiple series.
- The shaded area clearly corresponds to the single line.
- No legend is needed or present, and nothing obscures the plot area.

### Narrative clarity
- **From figure and caption alone:** The figure shows that the Magnificent 7 stocks (Apple, Amazon, Alphabet, Meta, Microsoft, Nvidia, Tesla) grew from under 10% to approximately 30% of total U.S. equity market capitalization between 2015 and 2024, with particularly sharp growth after roughly 2022. The message is immediately clear: AI-related mega-cap stocks have dramatically increased their share of the market.
- **From figure and paper text:** The figure motivates the central research question. The introductory paragraph asks whether these extraordinary valuations are rational, and the paper proposes that displacement risk—the risk that an AI singularity devastates the typical investor's wealth—partially explains why AI stocks command high prices as a hedge. The figure serves as the empirical hook establishing that AI stock valuations are remarkable and worthy of theoretical explanation.

---

## Figure 2 (page 11) — P/D Ratio of AI Stocks vs. Singularity Growth Factor

VERDICT: PASS

REASON: The figure is a single-panel plot with clearly readable labels, well-distinguished curves, and a caption that conveys the main message without ambiguity.

### Panel identification
Figure 2 is a single-panel plot showing the P/D ratio of AI stocks as a function of the singularity output growth factor (G) and deadweight costs of transfers.

### Readability: PASS
- The y-axis label ("P/D ratio of AI stocks") is readable.
- The x-axis label ("Singularity output growth factor (G)") is readable.
- Tick labels on both axes are readable; x-axis shows values 1, 5, 10, 15, 20, 25 and y-axis shows values from roughly 20 to 50.
- The legend in the upper-right corner is readable, listing four series: "No transfers," δ = 0, δ = 0.5, and "Perfect transfers (δ = 0)."
- The two horizontal reference lines are labeled V₀ and V∞ on the right margin, both readable though small—still legible.
- Font sizes are adequate throughout. No text is cut off or overlapping.

### Distinguishability: PASS
- There are four curves plus two horizontal dashed reference lines.
- The "No transfers" line is a solid dark line that is clearly separate from the others.
- The three transfer-related curves (δ = 0, δ = 0.5, and "Perfect transfers") use distinct line styles (solid vs dashed) and are visually separable.
- The horizontal reference lines V₀ and V∞ are thin dashed lines clearly distinct from the main curves.
- The legend does not obscure any important part of the plot—it sits in the upper-right where the curves have already flattened and converged.
- All curves are clearly separable across the full range of G.

### Narrative clarity
- **From figure and caption alone:** As the singularity output growth factor G increases, the P/D ratio of AI stocks declines from high levels and converges toward the no-singularity benchmark (V∞). Without transfers, the P/D ratio starts highest and converges slowest. With perfect transfers (δ = 0), it drops fastest toward V∞. Even transfers with substantial deadweight losses (δ = 0.5) bring the P/D ratio down significantly, illustrating that redistribution can reduce the hedging premium on AI stocks even when it is very costly.
- **From figure and paper text:** The paper argues that in a singularity scenario with explosive output growth, government transfers can reduce displacement risk and thus the hedging premium on AI stocks, even if those transfers are extremely inefficient. The figure illustrates this quantitatively: for large G, even transfers that destroy half their value (δ = 0.5) bring AI stock valuations close to the complete-markets benchmark. This supports the paper's broader point that the sheer scale of post-singularity output can make even very wasteful redistribution effective at closing the valuation gap caused by market incompleteness.
