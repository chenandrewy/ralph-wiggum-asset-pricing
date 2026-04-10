# tests/theory-clarity.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 2m 11s
[ralph-garage/agent-logs/20260409T215056.128229-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.128229-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in dedicated setup paragraphs with display math for the most critical expressions; minor presentation gaps do not impede a careful reader.

## Key items identified

### Should appear in display math (and do)
1. **Aggregate consumption growth** $C_{t+1} = (1+g)C_t$ -- eq. (1), displayed at start of Consumption paragraph
2. **Displacement rule** $\alpha_{t+1} = \phi\,\alpha_t$ -- eq. (2), displayed inside Singularity enumerated list
3. **CRRA utility** -- eq. (3), displayed at start of Preferences paragraph
4. **P/D ratios** -- eqs. (4)-(5), displayed in Proposition 1
5. **Transfer consumption** -- eq. (5/transfer), displayed in Extension 2
6. **Effective displacement** $\phi_\text{eff}$ -- eq. (6), displayed in Extension 2

### Should appear in display math but currently do not
7. **Dividend growth factors** $\Gamma^{AI}$, $\Gamma^{N}$ -- defined inline within Proposition 1's "where" clause; the entire valuation-spread argument and comparative statics depend on $\Gamma^{AI} > \Gamma^{N}$
8. **Household consumption growth in singularity** $\phi(1+\eta)(1+g)$ -- appears only as a bullet in the Appendix A proof; however, this is a derived quantity from displayed eqs. (1)-(2) rather than a new assumption

### May remain in prose (at or near paragraph start)
9. **Household consumption share** $c_t^H = \alpha_t C_t$ -- introduced mid-paragraph (line 82) after eq. (1); natural continuation
10. **Singularity probability** $p$ -- at start of Singularity paragraph (line 85)
11. **Productivity jump** $(1+\eta)$ -- inline in enumerated list item (line 88)
12. **Extinction probability** $\xi$ -- inline in enumerated list items (lines 88, 93)
13. **AI dividend share and dynamics** $\theta_t$, $\Delta\theta$ -- inline in bulleted list (line 102)
14. **Market incompleteness** -- end of Assets paragraph (lines 106-107)
15. **Positive singularity / veto** -- start of Section 4.1 paragraph (lines 199-202)
16. **Extinction utility normalization** $U_\text{ext} = 0$ -- mid-paragraph (line 201)

## Findings by section

### Section 2.1 (Setup)
- **Question A (setup paragraphs):** Yes. The model is organized into four dedicated `\paragraph{}` blocks (Consumption, Singularity, Assets, Preferences), each introducing a distinct group of assumptions. Market incompleteness (item 14) appears at the end of the Assets paragraph rather than in its own block, but follows logically from the asset descriptions and is clearly flagged with emphasis ("The household *cannot* purchase these restricted shares").
- **Question B (display math):** The three most critical setup equations -- consumption growth, displacement, and utility -- all appear in display math. The productivity jump $(1+\eta)$ and extinction probability $\xi$ remain inline, which is acceptable since they are scalar parameters introduced alongside the displacement equation.
- **Question C (paragraph starts):** Singularity probability $p$ opens its paragraph. Household share $\alpha_t$ appears mid-paragraph but immediately after eq. (1), which is natural. No key assumption is buried deep within a paragraph.

### Section 2.2 (Equilibrium prices)
- **Question A:** The section opens with a clear statement that market incompleteness means the SDF uses household consumption, not aggregate -- the key pricing consequence. Proposition 1 is a formal block.
- **Question B:** P/D ratio equations are displayed. The $\Gamma^{AI}$, $\Gamma^{N}$ factors (item 7) are defined in the "where" clause of Proposition 1 rather than as a standalone displayed equation. Since the entire discussion of hedging channel and all comparative statics turn on $\Gamma^{AI} > \Gamma^{N}$, a standalone display equation would improve scanability, but the current placement inside a clearly labeled proposition is adequate.
- **Question C:** The post-proposition discussion paragraph (line 147) opens by directing the reader to the key comparison ($\Gamma^{AI}$ vs. $\Gamma^{N}$).

### Section 2.3 (Discussion)
- No new assumptions introduced. Recaps and contextualizes prior assumptions. No issues.

### Section 3 (Quantitative Analysis)
- No new assumptions. Calibration values are stated clearly in a single sentence (line 184). No issues.

### Section 4.1 (Extension 1: Veto)
- **Question A:** The positive singularity and veto mechanism are introduced in setup prose paragraphs before Proposition 3. The extinction utility normalization $U_\text{ext} = 0$ (item 16) appears mid-paragraph (line 201) rather than at paragraph start; a reader could miss it, but it is flagged with "Following Jones (2024), we normalize..."
- **Question B:** No new display equations are needed here; the assumptions are qualitative augmentations to the baseline.
- **Question C:** The positive singularity is introduced at the start of the subsection's opening paragraph.

### Section 4.2 (Extension 2: Transfers)
- **Question A:** The transfer mechanism is introduced in a clear "We model this as follows" paragraph before the display equation.
- **Question B:** Both the transfer consumption formula and $\phi_\text{eff}$ appear in display math. The transfer ratio (eq. 7) is also displayed. Well done.
- **Question C:** The tax rate $\tau$ and deadweight $\delta$ are introduced at the start of their paragraph.

### Appendix A
- The household consumption growth expression $\phi(1+\eta)(1+g)$ appears only here as a proof bullet (line 285). This is a derived quantity rather than a new assumption, and the condition $\phi(1+\eta) < 1$ is stated in the main text discussion (line 147: "the household's high marginal utility in singularity states (due to displacement, $\phi(1+\eta) < 1$ when $\phi$ is sufficiently small)"). Not a clarity failure.
