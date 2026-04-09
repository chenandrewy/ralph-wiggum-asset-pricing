# tests/visual-figures-image-only.py
Started: 2026-04-09 19:33:02 EDT
Runtime: 1m 46s
[ralph-garage/agent-logs/20260409T193302.049570-0400_visual-figures-image-only_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T193302.049570-0400_visual-figures-image-only_claude_claude-opus-4-6.log)

# visual-figures-image-only

VERDICT: FAIL

REASON: fig-extension-panels fails on contrast (light salmon baseline line nearly invisible in Panel b) and use-of-space (baseline crushed into bottom 15% of Panel b due to scale compression).

---

## fig-ai-valuations

VERDICT: PASS

REASON: Two clearly distinguishable, high-contrast series with readable labels, good use of space, and a clear narrative message.

### Full Figure (single panel, no sub-panels)

**Readability: PASS.** The y-axis label ("Normalized Price (Jan 2015 = 100)"), x-axis tick labels (2016–2026), y-axis tick labels (100–500), and legend are all clearly readable at appropriate font sizes. Nothing is cut off or overlapping.

**Distinguishability: PASS.** The NASDAQ Composite is rendered as a solid blue line and the S&P 500 as a dashed dark red/maroon line. The two series are immediately distinguishable by both color and line style. The legend does not obscure any meaningful data.

**Contrast: PASS.** Both lines are thick and rendered in dark, saturated colors (blue, dark red) against a white background. No reference lines or markers suffer from low contrast.

**Use of space: PASS.** X-axis runs from roughly Jan 2015 to early 2026; data fills the range. Y-axis spans 100 to 500, matching the data range tightly. No wasted space on any edge.

**Narrative clarity: PASS.** AI/tech-heavy stocks (NASDAQ Composite) have dramatically outpaced the broader market (S&P 500) since 2015, with the gap widening sharply after roughly 2023, motivating the paper's focus on AI-driven displacement risk.

---

## fig-extension-panels

VERDICT: FAIL

REASON: The baseline (salmon) line in Panel (b) has critically poor contrast and is visually crushed by scale compression into the bottom 15% of the plot.

### Panel (a): AI Stock Valuations

**Readability: PASS.** Title, axis labels ("Tax rate tau", "P/D Ratio (AI Stocks)"), tick labels, and legend are all clearly readable. Nothing is cut off or overlapping.

**Distinguishability: PASS.** The two series are encoded with both color (salmon vs. cyan) and linetype (solid vs. dashed), making them easy to tell apart.

**Contrast: FAIL.** The baseline (salmon/coral) solid line is rendered in a light, low-saturation red-pink. In the right half of the panel (tau > 20%), the salmon line becomes quite faint against the white background.

**Use of space: PASS.** The y-axis spans roughly 5 to 45, and the data spans approximately 8 to 45. The x-axis runs 0%–40% and data fills this range. No excessive whitespace.

### Panel (b): Household Consumption

**Readability: PASS.** Title, axis labels, tick labels, legend, and annotations ("Catastrophe: 50% loss", "25% loss", "No change") are all legible.

**Distinguishability: FAIL.** The baseline (salmon) line is extremely difficult to see. It is a light, low-saturation pink that barely rises from about 0.75 to about 1.0 across the full x-range. Against the white plot background it is nearly invisible and fails the "instant read" test.

**Contrast: FAIL.** The baseline salmon line is far too light and low-contrast. In the region where it conveys its most important information (modest gains from transfers), it hovers near the "No change" reference line and is barely distinguishable from the background. The "25% loss" annotation text is also rendered in gray at small size, which is marginal.

**Use of space: FAIL.** The y-axis runs from 0 to approximately 7. The baseline series maxes out at roughly 1.0, occupying only the bottom ~15% of the plot. The large-singularity line drives the y-axis up to ~6.5, compressing the baseline into a nearly flat line at the bottom. The baseline's behavior — the key point that transfers help only modestly without a singularity — is visually lost.

**Narrative clarity: MARGINAL.** The caption's main message (that the large singularity makes transfers dramatically effective while the baseline gains only modestly) is conveyed by the cyan line, but the baseline comparison is visually crushed. A reader cannot easily appreciate the contrast without squinting.

### Summary of Problems

1. **Panel (b) baseline contrast:** The salmon/pink line is too light and thin. It should be a darker, more saturated color (e.g., true red or dark orange).
2. **Panel (b) scale compression:** The two series differ by an order of magnitude (baseline peaks at ~1.0, large singularity at ~6.5), which crushes the baseline into a barely-visible flat line. Consider a log scale, a broken axis, or separate panels to give the baseline adequate visual weight.
3. **Panel (a) baseline contrast (minor):** The salmon line could be darker for improved contrast, though this is less severe than in Panel (b).
