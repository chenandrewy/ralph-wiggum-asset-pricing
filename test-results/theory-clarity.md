# tests/theory-clarity.py
Started: 2026-04-12 09:46:31 EDT
Runtime: 2m 26s
[ralph-garage/agent-logs/20260412T094631.065141-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T094631.065141-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Nearly all key model assumptions appear in display math or at the start of setup paragraphs; two minor presentation gaps do not impede reader comprehension.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq:agg-consumption-growth (line 80)
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq:displacement (line 92)
3. CRRA utility $U_0^H$ — eq:utility (line 118)
4. P/D ratios for AI and non-AI stocks — eq:pd-ai, eq:pd-nonai (lines 129, 133)
5. Existence condition $A^j < 1$ — eq:existence (line 146)
6. Post-transfer consumption — eq:transfer-consumption (line 242)
7. Effective displacement $\phi_\text{eff}$ — eq:phi-eff (line 250)
8. Transfer consumption ratio — eq:transfer-ratio (line 258)

### May remain in prose (properly placed)
9. Household share $c_t^H = \alpha_t C_t$ — first sentence after eq 1 (line 84)
10. Singularity probability $p$ — first sentence of Singularity paragraph (line 87)
11. Extinction probability $\xi$ — enumerated list item (line 95)
12. Productivity jump $\eta$ — enumerated list item (line 90)
13. AI/non-AI dividend definitions and $\theta$ update rule — bulleted list (lines 103-105)
14. Market incompleteness — Assets paragraph prose (line 110)
15. Positive singularity $q > 1/2$ — Extension 1 setup prose (line 200)
16. Veto cost $\kappa$ — Extension 1 setup prose (line 204)
17. Tax rate $\tau$ and deadweight $\delta\tau$ — Extension 2 setup prose (line 239)

### Borderline items
18. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined in the "where" clause of Proposition 1 (line 136), not a standalone display equation
19. Condition $\phi(1+\eta) < 1$ — first appears parenthetically mid-sentence (line 153), never stated as a named assumption

## Findings by section

### Section 2.1 (Setup)
All parameters ($g$, $\alpha_t$, $p$, $\phi$, $\xi$, $\eta$, $\theta_t$, $\Delta\theta$, $\gamma$, $\beta$) are introduced in clearly labeled paragraphs (Consumption, Singularity, Assets, Preferences) with display math for the three most critical expressions. Market incompleteness is stated clearly in the Assets paragraph. No issues.

### Section 2.2 (Equilibrium prices)
P/D ratios are in display math within Proposition 1. The definitions of $\Gamma^{AI}$ and $\Gamma^{N}$ appear only in the "where" clause after the P/D equations rather than as a standalone display equation before or after the proposition. These are the key objects that drive the valuation spread and are discussed extensively afterward. Elevating them to their own display equation would improve scannability, but the current placement inside Proposition 1's display math is acceptable.

The existence condition $A^j < 1$ is properly displayed in Remark 1.

The condition $\phi(1+\eta) < 1$ — which ensures household consumption actually falls upon singularity and is load-bearing for the veto result and infinite-hedging-demand discussion — first appears parenthetically at line 153. It would benefit from explicit statement as an assumption or labeled condition near eq:displacement, but its omission does not block comprehension because the calibration ($\phi = 0.5$, $\eta = 0.5$) makes it obvious.

### Section 2.3 (Discussion)
Recalls earlier assumptions; no new assumptions introduced. No issues.

### Section 3 (Quantitative Analysis)
Calibration values stated clearly in prose. No new model assumptions. No issues.

### Section 4.1 (Extension 1: Veto)
New assumptions ($q$, $\kappa$, complete-markets consumption) are introduced in setup paragraphs before Proposition 3. The condition $\phi(1+\eta) < 1$ is used formally in the proof (line 222) but was introduced earlier in Section 2.2 prose. No issues specific to this section.

### Section 4.2 (Extension 2: Transfers)
Transfer mechanism ($\tau$, $\delta$) introduced in setup prose, followed immediately by display math for post-transfer consumption, $\phi_\text{eff}$, and the transfer ratio. Well organized. No issues.
