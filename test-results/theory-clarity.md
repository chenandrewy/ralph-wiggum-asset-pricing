# tests/theory-clarity.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 1m 59s
[ralph-garage/agent-logs/20260409T203927.594081-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.594081-0400_theory-clarity_claude_opus.log)

# theory-clarity

VERDICT: PASS

REASON: Key model assumptions are introduced in clearly labeled setup paragraphs before the results that use them; the most critical expressions appear in display math, with a few minor candidates for promotion.

## Key Items Identified

### Should appear in display math (most critical)
1. **[Agg-growth]** $C_{t+1} = (1+g)C_t$ — baseline consumption growth
2. **[Household-share]** $c_t^H = \alpha_t C_t$ — household consumption level
3. **[Displacement]** $\alpha_{t+1} = \phi \alpha_t$ — share dynamics upon singularity
4. **[Utility]** CRRA utility $U_0^H$
5. **[AI-div]** $D_t^{AI} = \theta_t C_t$ — AI stock dividends
6. **[NonAI-div]** $D_t^{N} = (1-\theta_t) C_t$ — non-AI stock dividends
7. **[Theta-jump]** $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — AI share expansion
8. **[Gamma-factors]** $\Gamma^{AI}$, $\Gamma^N$ — conditional dividend growth factors
9. **[PD-ratios]** P/D ratio formulas (Proposition 1)
10. **[Transfer-consumption]** Post-transfer household consumption
11. **[Transfer-ratio]** Transfer consumption ratio

### May remain in prose (at paragraph start)
1. Time is discrete and infinite
2. Representative household is marginal investor
3. AI owners hold private capital
4. Singularity probability $p$
5. Extinction probability $\xi$
6. Productivity boost $\eta$
7. $\phi \in (0,1)$ displacement severity
8. Market incompleteness (cannot trade private AI capital)
9. Deadweight cost $\delta$, tax rate $\tau$
10. Positive singularity $\alpha_{t+1} = \min(1, \alpha_t/\phi)$
11. Veto mechanism and cost

## Findings by Section

### Section 2.1 (Setup) — Good
- The section uses clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences) that each open with the relevant assumption.
- **[Agg-growth]**, **[Displacement]**, **[Utility]** all appear in display math. Good.
- **[Household-share]** ($c_t^H = \alpha_t C_t$) is inline on line 86. This is the central object of displacement and the direct argument of the utility function; promoting it to display math would make it easier to locate on re-reading. Minor issue.
- **[AI-div]**, **[NonAI-div]**, **[Theta-jump]** are inline math inside bullet items (lines 106–107). These are clearly presented in a dedicated Assets paragraph, but the theta-jump expression is a key input to $\Gamma^{AI}$ and could benefit from display math. Minor issue.
- All prose-level assumptions (singularity probability, extinction, productivity boost, incompleteness) are stated at or near the start of their respective paragraphs or enumerated list items. Good.

### Section 2.2 (Equilibrium Prices) — Good
- Opens with the key statement that the SDF reflects the household's own consumption growth. Good.
- P/D formulas appear in display math inside Proposition 1. Good.
- **[Gamma-factors]** are defined in the "where" clause of Proposition 1 rather than in a standalone display equation. Since these are the linchpin of the valuation spread ($\Gamma^{AI} > \Gamma^N$ is the entire hedging channel), a reader looking for them must scan the proposition statement. This is acceptable since the proposition is the natural home, but a standalone equation would improve navigability. Minor issue.

### Section 2.3 (Discussion) — Good
- No new assumptions introduced; discusses existing ones. No issues.

### Section 3 (Quantitative Analysis) — Good
- Calibration values are stated clearly in prose at the start of the section. No new model assumptions. Good.

### Section 4.1 (Extension 1: Veto) — Good
- Positive singularity ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$) is introduced in setup prose before Proposition 3. Good.
- Veto mechanism and cost are introduced in a setup paragraph before the proposition. Good.
- Extinction utility normalization is stated in prose before the proposition. Good.

### Section 4.2 (Extension 2: Transfers) — Good
- Tax rate $\tau$ and deadweight cost $\delta$ are introduced in setup prose before the display equations. Good.
- **[Transfer-consumption]** and **[Transfer-ratio]** are in display math. Good.
- $\phi_{\text{eff}}$ (effective displacement parameter) is defined inline in prose (line 232). This is a useful sufficient statistic linking transfers to Proposition 1, and could be promoted to display math. Minor issue.

## Summary

The paper's model presentation is well-structured. All key assumptions appear in dedicated setup paragraphs or formal blocks before the results that depend on them. The most critical expressions are in display math. A few expressions — $c_t^H = \alpha_t C_t$, the $\theta$-jump law, $\Gamma$ factors, and $\phi_{\text{eff}}$ — are currently inline and could be promoted to display math for easier navigation, but none are buried or hard to find. No assumption is introduced only inside a proposition or proof and then relied upon later without prior setup.
