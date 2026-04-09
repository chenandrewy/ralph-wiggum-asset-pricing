# tests/theory-clarity.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 1m 35s
[ralph-garage/agent-logs/20260409T184838.239656-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T184838.239656-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly structured setup paragraphs before the results that use them; the most critical expressions appear in display math, with two minor gaps that do not impair readability.

## Key items identified

**Display math (critical expressions):**
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ (eq 1)
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ (eq 2)
3. CRRA utility (eq 3)
4. AI share jump $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — currently inline prose
5. $\Gamma^{AI}$, $\Gamma^N$ definitions — currently inside Proposition 1 only
6. P/D ratio formulas (eqs 4–5, inside Proposition 1)
7. Veto gain $\Delta U^H$ (eq 8, inside Proposition 3)
8. Post-transfer consumption (eq 9)
9. Transfer ratio (eq 10)

**Prose assumptions:**
10. Household consumption share $c_t^H = \alpha_t C_t$
11. Singularity probability $p$, extinction probability $\xi$, productivity boost $\eta$
12. $\gamma > 1$, $\beta \in (0,1)$, $\Delta\theta \in (0,1)$
13. Market incompleteness (cannot trade private AI capital)
14. $\lambda > 1/2$ (positive singularity most likely)
15. Veto cost $\kappa > 0$, deadweight cost $\delta_0 > 0$, tax rate $\tau$

## Findings by section

### Section 2 (Model)
- **Setup paragraphs (2.1):** Well-organized with named paragraph headers (Consumption, Singularity, Assets, Preferences). Each introduces assumptions at the top of its paragraph. Satisfies criteria A and C.
- **Display math:** The most critical structural expressions — consumption growth (eq 1), displacement (eq 2), utility (eq 3) — are all in display math. Satisfies criterion B for these items.
- **Minor gap (item 4):** The AI share jump rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ is stated inline in a bullet list (line 105) rather than in display math. This expression directly drives the valuation spread (Corollary 1) and all comparative statics. Promoting it to display math would make it easier for the reader to locate. This is a suggestion, not a failure — the bullet list is clearly structured and the expression is easy to find.
- **Minor gap (item 5):** $\Gamma^{AI}$ and $\Gamma^N$ are defined only inside Proposition 1 (line 133). Since these are the pivot of every comparative static and the hedging interpretation discussed in the text after Proposition 1, defining them in a display equation before the proposition would improve navigability. Again a suggestion, not a failure — defining notation inside a proposition statement is standard practice.
- **Market incompleteness (item 13):** Clearly stated at the end of the Assets paragraph (line 109) with emphasis ("cannot"). Well-placed.

### Section 2.2 (Equilibrium prices)
- P/D ratios and $\Gamma$ factors appear inside Proposition 1, which is standard for formal results. The discussion paragraph after the proof (line 166) effectively recaps the hedging channel. No issues.

### Section 3 (Quantitative Analysis)
- References parameterization clearly. No new assumptions introduced. No issues.

### Section 4.1 (Veto and efficient development)
- New assumptions ($\lambda > 1/2$, $\phi^+ > 1$, veto cost $\kappa$) are introduced in a setup paragraph and bullet list before Proposition 3. Well-structured.
- The veto gain $\Delta U^H$ (eq 8) appears inside Proposition 3. This is appropriate — it is a derived quantity used to state the result, not a new primitive assumption.

### Section 4.2 (Government transfers)
- New assumptions ($\tau$, $\delta_0$) are introduced in prose at the start of the subsection (line 264), before the display equations. Well-structured.
- Post-transfer consumption (eq 9) and transfer ratio (eq 10) are in display math in the main text. Satisfies criterion B.
