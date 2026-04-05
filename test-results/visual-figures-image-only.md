# tests/visual-figures-image-only.py
Started: 2026-04-05 10:18:54 EDT
Runtime: 1m 4s
[ralph-garage/agent-logs/20260405T101854.581728-0400_visual-figures-image-only_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260405T101854.581728-0400_visual-figures-image-only_claude_claude-opus-4-6.log)

# visual-figures-image-only

VERDICT: FAIL

REASON: fig-transfers fails the contrast requirement due to light gray reference lines for $V_0$ and $V_\infty$.

---

## fig-opening

VERDICT: PASS

REASON: The single-panel figure is readable, clearly distinguishable, uses space well, and communicates its message effectively.

### Full figure — AI stocks as a share of total CRSP market capitalization

- **Readability: PASS** — Title, axis labels, tick labels, and the "30%" endpoint annotation are all clearly rendered and legible. No text is overlapping, cut off, or too small.
- **Distinguishability: PASS** — Only one series is plotted (dark blue line with light blue shaded area beneath). No ambiguity possible.
- **Contrast: PASS** — The main line is dark blue and thick enough to be immediately visible. No reference lines or auxiliary elements raise contrast concerns.
- **Use of space: PASS** — The y-axis runs from 0 to just above 30%, appropriate for a share-of-total metric. The x-axis spans 2015–2024, tightly fitted to the data. No wasted space.
- **Narrative clarity: PASS** — The Magnificent 7 AI stocks grew from about 8% of total US equity market capitalization in 2015 to approximately 30% by end of 2024. The caption provides all needed context.

---

## fig-transfers

VERDICT: FAIL

REASON: The two horizontal reference lines ($V_0$ and $V_\infty$) are rendered in light gray with thin dotted strokes, failing the contrast requirement.

### Full figure — P/D ratio of AI stocks vs. singularity output growth factor

- **Readability: PASS** — Axis labels, tick labels, and legend entries are all clearly readable at appropriate font sizes. The $V_0$ and $V_\infty$ annotations are legible though rendered in light gray.
- **Distinguishability: PASS** — Four curves use distinct visual encodings (solid black, orange long-dash, blue dash-dot, teal/green dashes). All are clearly distinguishable. The legend does not obscure data.
- **Contrast: FAIL** — The two horizontal reference lines for $V_0$ and $V_\infty$ are drawn as thin, light gray dotted lines that are difficult to see against the white background. Every plotted element — including reference lines — must be dark and high-contrast. These should be rendered in a darker color and/or with a heavier stroke weight.
- **Use of space: PASS** — The x-axis range (1–20) is justified since curves carry meaningful information across the full range. The y-axis (0–50) has modest headroom above the data but is not excessive.
- **Narrative clarity: PASS** — The figure clearly communicates that as the singularity output growth factor $G$ increases, the P/D ratio falls toward the no-hedge-benefit benchmark. Higher deadweight costs leave more hedge value in AI stocks, while perfect transfers eliminate nearly all hedge value.
