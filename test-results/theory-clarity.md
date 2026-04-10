# tests/theory-clarity.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 1m 56s
[ralph-garage/agent-logs/20260409T205235.736479-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T205235.736479-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Nearly all key model assumptions appear in display math or at the start of setup paragraphs; two moderate placement issues do not impede readability.

## Key items identified

**Display math (confirmed present):**
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq (1), line 80
2. Displacement rule $\alpha_{t+1} = \phi\,\alpha_t$ — eq (2), line 92
3. CRRA utility — eq (3), line 113
4. Existence condition $A^j < 1$ — Remark 1, line 142
5. Post-transfer consumption $c^H_{post}$ — eq (4), line 225
6. Transfer ratio $c^H_{post}/c^H_{no\text{-}transfer}$ — eq (5), line 235

**Prose-level assumptions (confirmed at or near paragraph starts):**
- Household share $c_t^H = \alpha_t C_t$ — line 84, immediately after eq (1)
- Singularity probability $p$ — line 87, opens Singularity paragraph
- Productivity boost $1+\eta$ — line 90, inside singularity enumeration
- Extinction probability $\xi$ — lines 90-95, inside singularity enumeration
- AI/non-AI dividend definitions — lines 103-105, Assets paragraph
- AI share evolution $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — line 104, Assets paragraph
- Market incompleteness (no trade in private AI capital) — lines 108-109, end of Assets paragraph
- CRRA parameters $\gamma > 1$, $\beta$ — line 111, opens Preferences paragraph
- Positive singularity rule (Ext 1) — line 199, opens Extension 1 setup
- Social efficiency assumption — line 199, same paragraph
- Veto mechanism — lines 201-202, follows immediately
- Transfer mechanism $\tau$, $\delta$ — lines 222-223, opens Extension 2 setup
- Effective displacement $\phi_\text{eff}$ — line 230, mid-paragraph (minor)

## Findings by section

### Section 2.1 (Setup)
All core assumptions are introduced in clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences). Display math is used for the three most critical expressions: consumption growth, displacement, and utility. No issues.

### Section 2.2 (Equilibrium prices)
Two moderate issues:

1. **$\Gamma^{AI}$ and $\Gamma^{N}$ defined only inside Proposition 1** (line 132). These dividend growth factors are derived mechanically from setup parameters ($\theta$, $\Delta\theta$, $\eta$) and are not results of the proposition itself. Defining them in display math in the Assets paragraph of Section 2.1 would let readers absorb the definitions before encountering the P/D formulas.

2. **$\phi(1+\eta) < 1$ stated only informally** in the discussion paragraph after Proposition 1 (line 147). This inequality is the essential condition for the hedging channel to operate — it ensures household consumption falls in the singularity state despite the productivity boost. Elevating it to a named condition or explicit assumption in Setup would clarify the mechanism.

Neither issue blocks comprehension; the current text is readable. Both are organizational improvements rather than gaps.

### Section 2.3 (Discussion)
No new assumptions. Correctly recalls earlier setup.

### Section 3 (Quantitative Analysis)
No new assumptions. Calibration values clearly stated.

### Section 4.1 (Extension 1: Veto)
New assumptions (positive singularity, social efficiency, veto cost, extinction-utility normalization) are all introduced in setup prose before Proposition 3. The positive-singularity rule $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ is inline rather than display math, but the extension is brief and this does not hinder readability.

### Section 4.2 (Extension 2: Transfers)
Transfer mechanism assumptions open the subsection. Post-transfer consumption and transfer ratio are in display math. The effective displacement parameter $\phi_\text{eff}$ is defined mid-paragraph (line 230) rather than at the start — a minor placement issue. Overall well-organized.
