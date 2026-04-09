# tests/visual-figures-image-only.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 1m 21s
[ralph-garage/agent-logs/20260409T184838.247508-0400_visual-figures-image-only_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T184838.247508-0400_visual-figures-image-only_claude_claude-opus-4-6.log)

# visual-figures-image-only

VERDICT: FAIL

REASON: Panel (a) of fig-extension-panels has a severe use-of-space problem (curves flatten by ~20% tax rate but x-axis extends to 70%), and fig-ai-valuations has low-contrast gridlines.

---

## fig-ai-valuations

VERDICT: FAIL

REASON: Horizontal gridlines are low-contrast light gray, failing the contrast requirement.

### Full Figure (single panel)

- **Readability: PASS.** Y-axis label ("Price-Earnings Ratio"), x-axis tick labels (2015–2025), y-axis tick labels (20, 40, 60), and legend entries ("AI-Exposed Firms", "S&P 500") are all clearly readable with appropriate font sizes. No overlapping or cut-off text.

- **Distinguishability: PASS.** Two series are clearly distinguishable: solid blue line with filled circles (AI-Exposed Firms) vs. dashed dark red/maroon line with filled circles (S&P 500). Color and line-style contrasts are strong. Legend is in the upper-left and does not obstruct data.

- **Contrast: FAIL.** Horizontal gridlines are very light gray with weak contrast against the white background. Every drawn element must have strong visual contrast; these gridlines are faint. The data lines themselves have excellent contrast.

- **Use of space: PASS.** X-axis spans 2015–2025, matching the data range. Y-axis runs from ~10 to ~75–80; data spans ~18 to ~73 (range ≈ 55). Bottom gap is ~8 (15% of range), within the 20% threshold. Top has only slight headroom above the ~73 peak.

- **Narrative clarity: PASS.** The figure clearly shows AI-exposed firms have dramatically higher and rising P/E ratios compared to the S&P 500, with a sharp divergence beginning around 2019–2020 and accelerating through 2025. The "(Illustrative)" qualifier is noted in the caption.

**Main message:** AI-exposed stocks have seen their price-earnings ratios surge far above the broader market since ~2019, with the gap widening dramatically through 2025, consistent with investors pricing in expectations of transformative AI-driven growth or a hedging premium against displacement risk.

---

## fig-extension-panels

VERDICT: FAIL

REASON: Panel (a) has a severe use-of-space problem — both curves flatten and converge by ~20% tax rate, yet the x-axis extends to 70%, leaving the right half as wasted space.

### Panel (a): AI Stock Valuations

- **Readability: PASS.** Title "(a) AI Stock Valuations", axis labels ("Tax rate tau", "P/D Ratio (AI Stocks)"), legend text, and tick labels are all legible at appropriate font sizes. Nothing is cut off or overlapping.

- **Distinguishability: PASS.** Two series use different colors (salmon/red for Baseline, cyan for Large singularity) and different line types (solid vs. dashed). They are immediately distinguishable.

- **Contrast: PASS.** Both lines are thick and rendered in saturated colors against a white background. No contrast issues.

- **Use of space: FAIL.** The large-singularity (cyan dashed) curve drops sharply from above 40 near tau = 0 to about 10 by tau ≈ 10%, then essentially flattens and merges with the baseline curve by tau ≈ 20%. From 20% to 70% (more than half the x-axis), both curves are flat, overlapping, and carry no additional visual information. The right ~50 percentage points of x-axis range are wasted. The x-max should be reduced to roughly 30–40% to let the interesting region fill the panel.

- **Narrative clarity: PASS.** The message is clear: higher taxes reduce AI stock valuations, and the large-singularity scenario is far more sensitive to low tax rates.

### Panel (b): Household Consumption

- **Readability: PASS.** Title, axis labels, tick marks, and legend are all legible. The "No change" annotation at the y = 1 reference line is readable.

- **Distinguishability: PASS.** Same color/linetype encoding as Panel (a). The two series diverge strongly across the tax-rate range and are easy to tell apart. The "No change" dashed reference line is dark gray and clearly distinct from the data series.

- **Contrast: PASS.** The reference line at y = 1 uses dark gray, providing adequate contrast. All data lines are strongly colored.

- **Use of space: PASS.** The large-singularity curve rises from near 0 to about 7 across the full 0–70% range, using the full extent of both axes. No significant wasted space on any edge.

- **Narrative clarity: PASS.** The message is clear: in a large singularity, even inefficient (high-tau) transfers produce large household consumption gains, whereas in the baseline scenario consumption barely budges above the "no change" line.

**Main message:** The two panels together show that while AI stock valuations are highly sensitive to taxes only at low rates (Panel a), the consumption gains from redistribution are substantial and rise across the full tax range in the large-singularity scenario (Panel b).
