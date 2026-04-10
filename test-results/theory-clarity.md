# tests/theory-clarity.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 1m 55s
[ralph-garage/agent-logs/20260409T210608.988482-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.988482-0400_theory-clarity_claude_opus.log)

# theory-clarity

VERDICT: PASS

REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with the most critical expressions in display math; minor issues do not impede a careful reader.

## Key Items Identified

**Display math (most critical):**
- A1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ (eq. 1)
- A2. Displacement rule $\alpha_{t+1} = \phi\,\alpha_t$ (eq. 2)
- A3. CRRA utility with $\gamma > 1$ (eq. 3)
- A4. P/D ratio closed forms for AI and non-AI stocks (eqs. 4–5)
- A5. Existence condition $A^j < 1$ (eq. 5, Remark 1)
- A6. Post-transfer consumption (eq. 7)
- A7. Transfer ratio independence from $\eta$ (eq. 8)

**Prose (should be at/near paragraph start):**
- B1. Household share $c_t^H = \alpha_t C_t$
- B2. Singularity probability $p$
- B3. Extinction probability $\xi$ and $C_{t+1}=0$
- B4. Productivity boost factor $1+\eta$
- B5. AI dividend share dynamics $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
- B6. Market incompleteness (cannot trade private AI capital)
- B7. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$
- B8. Effective displacement $\phi_\text{eff}$
- B9. Positive singularity and veto option (Extension 1)
- B10. Transfer mechanism: tax $\tau$, deadweight cost $\delta\tau$ (Extension 2)

## Findings by Section

### Section 2.1 (Setup)

**A. Setup paragraphs:** The model setup uses clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences) that serve as distinct model-setup blocks. Assumptions are well-organized within this structure.

**B. Display math:** All of the most critical expressions — consumption growth (eq. 1), displacement (eq. 2), and preferences (eq. 3) — appear in display math. The singularity structure, including $p$, $\xi$, $\eta$, and the enumerated cases, is presented in a numbered list that is functionally equivalent to a formal assumption block.

**C. Prose placement:** The household share $c_t^H = \alpha_t C_t$ (B1) is introduced mid-paragraph immediately after eq. 1, which is acceptable given that it follows directly from the display equation it augments. The productivity boost $1+\eta$ (B4) and extinction $\xi$ (B3) appear inside the enumerated singularity list, which provides clear structure. The AI dividend dynamics (B5) appear in a bullet list under the Assets paragraph. Market incompleteness (B6) is clearly stated at the end of the Assets paragraph with an explicit sentence identifying it as the source of incompleteness.

No issues in this section.

### Section 2.2 (Equilibrium Prices)

**B. Display math:** The P/D ratios (A4) are in display math inside Proposition 1. The existence condition (A5) is in display math inside Remark 1.

**C. Prose placement:** The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ (B7) are defined in the where-clause of Proposition 1 rather than in standalone display math. This is standard practice for auxiliary definitions within a proposition and does not impair readability. The key inequality $\Gamma^{AI} > \Gamma^{N}$ is discussed in the paragraph immediately following Proposition 1.

No issues in this section.

### Section 4.1 (Extension 1: Veto)

**C. Prose placement:** The positive singularity rule (B9) and veto option are introduced in the opening setup paragraph of Section 4.1, at or near the start. The extinction normalization $U_\text{ext} = 0$ is introduced in the second paragraph, clearly stated. Proposition 3 relies on conditions introduced in these setup paragraphs, not on new assumptions stated only within the proposition.

No issues in this section.

### Section 4.2 (Extension 2: Transfers)

**B. Display math:** The post-transfer consumption (A6) and transfer ratio (A7) are both in display math. The effective displacement parameter $\phi_\text{eff}$ (B8) is introduced in prose rather than display math. This is a minor point — $\phi_\text{eff}$ is a derived connecting device rather than a new primitive assumption, and its formula is short enough for inline math.

**C. Prose placement:** The transfer mechanism (B10) — tax rate $\tau$ and deadweight cost $\delta\tau$ — is introduced at the start of a setup paragraph beginning "We model this as follows." The $\phi_\text{eff}$ definition appears mid-paragraph, but since it is a derived quantity linking back to Proposition 1, this placement is adequate.

No issues in this section.
