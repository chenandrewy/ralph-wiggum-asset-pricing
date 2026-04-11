# tests/theory-clarity.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 1m 2s
[ralph-garage/agent-logs/20260410T225642.491861-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.491861-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are organized into labeled setup paragraphs with critical expressions in display math; no important assumptions are buried mid-paragraph or confined to proposition/proof statements.

## Key items identified

### Items in display math (main text)
1. Aggregate consumption growth: eq (1), $C_{t+1} = (1+g)C_t$
2. Displacement rule: eq (2), $\alpha_{t+1} = \phi \alpha_t$
3. CRRA utility: eq (3)
4. P/D ratios for AI and non-AI stocks: eqs (4)-(5), Proposition 1
5. Existence condition: eq (6), Remark 1
6. Post-transfer household consumption: eq (8)
7. Effective displacement parameter: eq (9), $\phi_\text{eff}$
8. Transfer ratio: eq (10)

### Items in prose (at or near paragraph starts)
- Household consumption share $c_t^H = \alpha_t C_t$ (line 84, immediately after eq 1)
- Singularity probability $p$ per period (line 87, start of Singularity paragraph)
- Extinction probability $\xi$ vs non-extinction $1-\xi$ (lines 90-96, enumerated under Singularity)
- Productivity jump $\eta$ (line 90, within the singularity enumeration)
- AI dividend share $\theta_t$ and update rule $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ (line 104, start of AI stocks bullet)
- Market incompleteness: household cannot buy restricted AI equity (line 110, own paragraph)
- CRRA parameters $\gamma > 1$, $\beta \in (0,1)$ (line 113, start of Preferences paragraph)
- Positive singularity and 70/30 split (line 203, start of Section 4.1)
- Veto mechanism and cost (line 205, second paragraph of Section 4.1)
- Tax rate $\tau$ and deadweight cost fraction $\delta\tau$ (lines 230-231, setup paragraph of Section 4.2)

## Findings by section

### Section 2.1 (Setup)
Well-organized into four labeled paragraphs (Consumption, Singularity, Assets, Preferences). Each introduces its assumptions at the paragraph start. The displacement rule, consumption growth, and utility all appear in display math. The AI dividend update rule ($\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$) is inline rather than display, but it is simple, clearly placed at the start of its bullet, and the derived quantities $\Gamma^{AI}$, $\Gamma^{N}$ appear in display math in Proposition 1.

### Section 2.2 (Equilibrium prices)
Propositions 1 and 2 state results using parameters already introduced in Section 2.1. No new model assumptions are introduced here; new definitions ($\Gamma^{AI}$, $\Gamma^{N}$, $A^j$) are properly stated in display math within the proposition and remark where they first appear.

### Section 2.3 (Discussion)
No new assumptions. Discusses the model's relationship to GKP (2012).

### Section 3 (Quantitative Analysis)
No new assumptions. Calibration parameters are stated clearly at the start of the section.

### Section 4.1 (Extension 1: Veto)
The positive singularity and veto mechanism are introduced in clear setup paragraphs before Proposition 3. The extinction utility normalization ($U_\text{ext} = 0$) is stated in prose near the start of its paragraph (line 205).

### Section 4.2 (Extension 2: Government transfers)
The tax-and-transfer framework ($\tau$, $\delta$) is introduced in a setup paragraph before the display math equation (8). The effective displacement parameter $\phi_\text{eff}$ and transfer ratio both appear in display math.
