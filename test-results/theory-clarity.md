# tests/theory-clarity.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 2m 7s
[ralph-garage/agent-logs/20260411T211526.521713-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.521713-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with most critical expressions in display math; the main gap is that the dividend growth factors are defined only inside a proposition's where-clause rather than in the model setup.

## Key Items Identified

### Should appear in display math (and do)
- A1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — display math, line 84 (eq:agg-consumption-growth)
- A2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — display math, line 96 (eq:displacement)
- A3. CRRA utility — display math, line 121 (eq:utility)
- A4. P/D ratio formulas — display math inside Proposition 1, lines 132-138
- A5. Existence condition $A^j < 1$ — display math in Remark 1, line 149 (eq:existence)
- A6. Post-transfer consumption — display math, line 246 (eq:transfer-consumption)
- A7. Effective displacement $\phi_\text{eff}$ — display math, line 253 (eq:phi-eff)

### Should appear in display math but currently do not
- A8. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined only inline in Proposition 1's where-clause (line 140). These are the core objects driving the valuation spread ($\Gamma^{AI} > \Gamma^{N}$) and are referenced repeatedly in Propositions 1-2, the discussion, and Extension 2. A labeled display equation in the setup or before the proposition would help readers locate them.

### Prose items (correctly placed near paragraph starts)
- B1. Household share $c_t^H = \alpha_t C_t$ — line 88, in "Consumption" paragraph (second sentence; acceptable since the paragraph opens with aggregate consumption)
- B2. Singularity probability structure ($p$, $\xi$) — lines 91-100, opening the "Singularity" paragraph
- B3. AI dividend share $D_t^{AI} = \theta_t C_t$ and update rule — line 108, lead of the AI-stock bullet in "Assets"
- B4. Market incompleteness — line 114, opens its own paragraph in the Assets subsection
- B5. $\gamma > 1$ — line 119, opening sentence of "Preferences" paragraph
- B6. Positive singularity $q > 1/2$ — line 204, setup paragraph of Extension 1
- B7. Veto cost $\kappa > 0$ — line 208, setup paragraph of Extension 1
- B8. Deadweight cost $\delta > 0$ — line 243, setup paragraph of Extension 2
- B9. $\phi(1+\eta) < 1$ condition — first appears line 157 in a parenthetical mid-discussion; not a new assumption but an implication of the calibration

## Section-Level Findings

### Section 2.1 (Setup)
Well-organized. Four labeled paragraphs (Consumption, Singularity, Assets, Preferences) introduce all baseline assumptions clearly. Key equations are in display math. The market incompleteness statement is clearly presented in its own paragraph (line 114). Minor: the household consumption share definition $c_t^H = \alpha_t C_t$ is inline rather than displayed, but this is a simple identity and acceptable.

### Section 2.2 (Equilibrium Prices)
The P/D formulas appear in display math within Proposition 1. **Main gap**: The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are the economic heart of the hedging mechanism but appear only in an inline where-clause of the proposition. They warrant a standalone labeled display equation, either in the setup or immediately before Proposition 1, since they are referenced in Proposition 2, the discussion (Section 2.3), and Extension 2.

The existence condition (Remark 1) and the approximation discussion (lines 155-156) are well-placed immediately after the proposition.

### Section 2.3 (Discussion)
The condition $\phi(1+\eta) < 1$ first appears parenthetically on line 157. This is not a new model assumption but an implication of the parameter choices; its parenthetical placement is acceptable since the discussion paragraph opens with the economic intuition it supports.

### Section 3 (Quantitative Analysis)
No new model assumptions introduced. Calibration values are stated clearly at the paragraph start (line 189).

### Section 4.1 (Extension 1: Veto)
New assumptions (positive singularity with probability $q$, $q > 1/2$, veto cost $\kappa$, complete-markets benchmark) are introduced in setup paragraphs before Proposition 3. Well-structured.

### Section 4.2 (Extension 2: Government Transfers)
New assumptions (tax rate $\tau$, deadweight cost $\delta$) are introduced in a setup paragraph. The post-transfer consumption equation and $\phi_\text{eff}$ both get labeled display equations. Well-structured.
