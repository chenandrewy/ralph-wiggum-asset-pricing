# tests/theory-clarity.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 17s
[ralph-garage/agent-logs/20260411T101504.815898-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.815898-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with critical expressions in display math; no substantive clarity issues found.

## Key items identified

### Should appear (and do appear) in display math
1. Aggregate consumption growth: $C_{t+1} = (1+g)C_t$ — eq (1)
2. Displacement equation: $\alpha_{t+1} = \phi\,\alpha_t$ — eq (2)
3. CRRA utility — eq (3)
4. P/D ratios for AI and non-AI stocks — eqs (4)-(5)
5. Existence condition $A^j < 1$ — eq (6)
6. Veto one-period utility gain $\Delta u(\gamma)$ — eq (7)
7. Post-transfer household consumption — eq (8)
8. Effective displacement parameter $\phi_\text{eff}$ — eq (9)
9. Transfer ratio — eq (10)

### May remain in prose (introduced at or near paragraph starts)
- Household consumption share $c_t^H = \alpha_t C_t$ (Consumption paragraph)
- Singularity probability $p$ per period (Singularity paragraph)
- Extinction probability $\xi$ (Singularity enumerated list)
- Productivity jump factor $1 + \eta$ (Singularity enumerated list)
- AI dividend share $D_t^{AI} = \theta_t C_t$ and update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ (Assets paragraph, itemize)
- Non-AI dividends $D_t^N = (1-\theta_t)C_t$ (Assets paragraph, itemize)
- Positive singularity probability $q$ and reverse-displacement $\alpha_{t+1} = \min(1, \alpha_t/\phi)$ (Extension 1 opening paragraph)
- Veto cost $\kappa$ (Extension 1 veto paragraph)
- Complete-markets consumption $\alpha(1+\eta)C_t(1+g)$ (own paragraph before Proposition 3)
- Tax rate $\tau$ and deadweight cost $\delta$ (Extension 2 transfer setup paragraph)

## Findings by section

### Section 2.1 (Setup)
All model primitives are introduced in clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences). The two most important structural equations — consumption growth and displacement — appear in display math. Parameters ($p$, $\xi$, $\eta$, $\phi$, $\theta$, $\Delta\theta$, $\gamma$, $\beta$) are introduced at or near the start of their respective paragraphs. The AI dividend update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ is in an itemize block rather than display math; this is acceptable since its role is mediated through $\Gamma^{AI}$ and $\Gamma^{N}$, which are defined in display math within Proposition 1.

### Section 2.2 (Equilibrium prices)
P/D ratios and the existence condition appear in display math within Proposition 1 and Remark 1. The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined inline in the proposition statement. The discussion paragraph after the proposition clearly explains the economic content. No new model assumptions are introduced here — only results derived from the setup.

### Section 2.3 (Discussion)
Introduces the concept of $\phi_\text{eff} \to 1$ under complete markets as an interpretive device. This is discussion, not a new assumption.

### Section 3 (Quantitative Analysis)
No new model assumptions. Calibration values are stated clearly at the start of the section.

### Section 4.1 (Veto extension)
New assumptions (positive singularity probability $q$, reverse-displacement, veto cost $\kappa$, social efficiency definition, complete-markets consumption) are introduced in setup paragraphs before Proposition 3. The one-period utility gain $\Delta u(\gamma)$ appears in display math within the proof, which is appropriate since it is derived, not assumed.

### Section 4.2 (Government transfers)
The transfer mechanism ($\tau$, $\delta$) is introduced in a setup paragraph before the display-math equation for post-transfer consumption. The effective displacement parameter and transfer ratio both appear in display math with clear prose motivation.
