# tests/theory-clarity.py
Started: 2026-04-11 15:15:27 EDT
Runtime: 2m 16s
[ralph-garage/agent-logs/20260411T151527.415857-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260411T151527.415857-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: The model setup is well-structured with labeled paragraphs and display math for the most critical expressions, though a few key items could be more prominent.

## Key Items Identified

### Should appear in display math (Group A)
1. Aggregate consumption growth: $C_{t+1} = (1+g)C_t$
2. Household consumption share: $c_t^H = \alpha_t C_t$
3. Displacement rule: $\alpha_{t+1} = \phi \alpha_t$
4. AI dividend share dynamics: $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$
5. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$
6. CRRA utility
7. Existence condition $A^j < 1$
8. Effective displacement $\phi_\text{eff}$
9. Transfer consumption $c^H_{post}$
10. Veto utility gain $\Delta u(\gamma)$

### May remain in prose but should be prominent (Group B)
11. Market incompleteness (household cannot trade restricted AI equity)
12. Singularity probability $p$ each period
13. Extinction probability $\xi$ conditional on singularity
14. Productivity jump factor $(1+\eta)$
15. Condition $\phi(1+\eta) < 1$
16. $q > 1/2$ (positive singularity more likely)
17. Veto cost $\kappa > 0$
18. Complete-markets counterfactual
19. Extinction utility normalized to zero

## Section-Level Findings

### Section 2.1 (Setup) — Good
The setup uses labeled paragraphs (Consumption, Singularity, Assets, Preferences) that give the section clear structure. Items 1 and 3 appear in display math. Items 12, 13, and 14 are introduced in prose at or near paragraph starts. The CRRA utility is in display math.

Minor notes:
- **Item 2** (household consumption share $c_t^H = \alpha_t C_t$): introduced in prose after the display equation for aggregate growth, not in its own display. This is acceptable since it follows directly from the preceding equation, but it is one of the most-referenced objects in the paper.
- **Item 4** (AI dividend share dynamics $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$): stated only in a bullet-point item within the Assets paragraph with no display equation. This expression is critical — $\Gamma^{AI}$ and $\Gamma^{N}$ depend on it, and those drive the entire valuation spread. Promoting it to display math would help the reader locate it on re-reading.
- **Item 11** (market incompleteness): introduced in a dedicated paragraph after the asset bullets. The emphasis is adequate, though the paragraph begins with "AI owners also hold restricted equity" rather than leading with the incompleteness itself.

### Section 2.2 (Equilibrium Prices) — Good with one note
Proposition 1 presents P/D ratios in display math. The existence condition (item 7) appears in a Remark with its own display equation.

- **Item 5** ($\Gamma^{AI}$ and $\Gamma^{N}$): defined only in the "where" clause at the end of Proposition 1's statement. These are the objects that carry the economic content of the proposition (as the paper itself notes in the discussion). They are not introduced before the proposition and do not have their own display equation outside the proposition. This is standard practice in theory papers, but given how much the subsequent discussion leans on $\Gamma^{AI} > \Gamma^{N}$, a reader benefits from seeing these defined prominently.
- **Item 15** ($\phi(1+\eta) < 1$): first appears as a parenthetical in the post-Proposition 1 discussion (line 155), not in the model setup. This condition is load-bearing for both the hedging channel and the veto result. It would be clearer as a stated condition in Section 2.1 when $\phi$ is introduced.

### Section 2.3 (Discussion) — Good
Recalls and interprets earlier assumptions without introducing new ones. The complete-markets counterfactual ($\phi_\text{eff} \to 1$) is discussed prominently. No issues.

### Section 4.1 (Extension 1: Veto) — Good
New assumptions (positive singularity, $q > 1/2$, veto cost $\kappa$, extinction utility normalization, complete-markets counterfactual) are introduced in prose paragraphs before Proposition 3.

Minor notes:
- **Item 16** ($q > 1/2$): stated at the end of the opening paragraph rather than at or near its start. Moving it earlier or giving it its own sentence at the start of a paragraph would help.
- **Item 19** (extinction utility $= 0$): buried in the same paragraph as the veto cost. Acceptable since it is a normalization rather than a structural assumption.

### Section 4.2 (Extension 2: Transfers) — Good
The transfer mechanism (item 17), transfer consumption (item 9), and $\phi_\text{eff}$ (item 8) all appear in display math with clear prose motivation. The transfer ratio (eq. 9) is also displayed. No issues.

### Appendix A — Not evaluated
Conditions stated inside proofs are excluded per the procedure.
