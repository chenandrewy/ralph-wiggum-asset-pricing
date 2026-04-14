# tests/theory-clarity.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 1m 0s
[ralph-garage/agent-logs/20260414T102326.820712-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.820712-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions and expressions are clearly introduced in dedicated setup paragraphs or display math before they are used in results.

## Key items identified

### Display math in main text (all present)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq (1), line 80
2. Displacement $\alpha_{t+1} = \phi\alpha_t$ — eq (2), line 92
3. AI share update $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ — eq (3), line 106
4. CRRA utility — eq (4), line 123
5. P/D ratio for AI stocks — eq (5), line 134
6. P/D ratio for non-AI stocks — eq (6), line 138
7. Existence condition $A^j < 1$ — eq (7), line 152
8. Veto utility gain $\Delta u(\gamma)$ — eq (8), line 225
9. Transfer consumption $c^H_{post}$ — eq (9), line 248
10. Effective displacement $\phi_\text{eff}$ — eq (10), line 256
11. Transfer ratio — eq (11), line 264

### Prose assumptions (all at or near paragraph starts)
- $c_t^H = \alpha_t C_t$: Consumption paragraph, line 83
- Singularity probability $p$: Singularity paragraph, line 86
- Extinction probability $\xi$: enumerated item within Singularity paragraph, line 94
- Productivity boost $\eta > 0$: enumerated item within Singularity paragraph, line 89
- $D_t^{AI} = \theta_t C_t$ and $D_t^{N} = (1-\theta_t)C_t$: Assets paragraph items, lines 103/110
- $\gamma > 1$, $\beta \in (0,1)$: Preferences paragraph, line 120
- Positive singularity probability $q$, veto cost $\kappa$: Extension 1 setup, lines 206/210
- Tax rate $\tau$, deadweight parameter $\delta$: Extension 2 setup, line 245

## Section-level findings

### Section 2 (Model)
No issues. The Setup subsection (2.1) uses clearly labeled \paragraph blocks (Consumption, Singularity, Assets, Preferences) that each introduce their assumptions at the start. All critical expressions appear in display math. The distinction between $\alpha_t$ (consumption share) and $\theta_t$ (dividend share) is made explicit in the Assets paragraph.

### Section 2.2 (Equilibrium prices)
P/D ratios and growth factors $\Gamma^{AI}$, $\Gamma^{N}$ are in display math within Proposition 1. The existence condition is displayed in Remark 1. The condition $\phi(1+\eta) < 1$ for the hedging channel is introduced in the discussion paragraph following the proposition — appropriate since it is an interpretation of the model rather than a new assumption.

### Section 3 (Quantitative Analysis)
No new model assumptions. Calibration values are stated clearly at the start of the section.

### Section 4.1 (Veto extension)
New assumptions (positive singularity with probability $q$, veto cost $\kappa$, complete-markets benchmark) are introduced in clear setup paragraphs before Proposition 3. The condition $\phi(1+\eta) < 1$ appears as a stated condition within the proposition, which is appropriate.

### Section 4.2 (Transfers extension)
Transfer mechanics ($\tau$, $\delta$, post-transfer consumption) are introduced in a setup paragraph with the key expression in display math (eq 9) before the analysis. The effective displacement parameter $\phi_\text{eff}$ is derived in display math (eq 10) and clearly connected back to Proposition 1.
