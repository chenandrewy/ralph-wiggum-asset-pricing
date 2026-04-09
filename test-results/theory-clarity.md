# tests/theory-clarity.py
Started: 2026-04-09 19:33:01 EDT
Runtime: 2m 9s
[ralph-garage/agent-logs/20260409T193302.001234-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T193302.001234-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly structured setup paragraphs with named headers; the most critical expressions appear in display math; no assumptions are introduced only inside propositions or proofs.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq (1), display math in Consumption paragraph
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — eq (2), display math in Singularity paragraph
3. CRRA utility $U_0$ — eq (3), display math in Preferences paragraph
4. P/D ratios for AI and non-AI stocks — eqs (4)-(5), display math in Proposition 1
5. Existence condition $A^j < 1$ — eq in Remark 1, display math
6. Post-transfer consumption $c^H_{post}$ — eq (6), display math in Extension 2
7. Transfer ratio — eq (7), display math in Extension 2

### Remain in prose, acceptably placed
- Household share $c_t^H = \alpha_t C_t$: inline in Consumption paragraph, close to paragraph start
- Singularity probability $p$: opens the Singularity paragraph
- Productivity jump $(1+\eta)$: inside enumerated singularity description
- Extinction probability $\xi$: inside enumerated singularity description
- Private AI capital non-tradeability: clearly stated after Assets itemize
- $\gamma > 1$: opens Preferences paragraph
- Extension 1 parameters ($\lambda$, $\phi^+$, $\kappa$): clearly introduced in Extension 1 setup prose
- Extension 2 parameters ($\tau$, $\delta_0$): clearly introduced in Extension 2 setup paragraph

### Minor observations (not failures)
- $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$: inline in a bullet list rather than display math. Could be promoted, but the Assets bullet list is clearly structured and easy to locate.
- $\Gamma^{AI}$, $\Gamma^N$: defined in the "where" clause of Proposition 1 rather than as standalone display math. This is standard practice in economics papers and the definitions are easy to find.

## Section-level findings

**Section 2.1 (Setup):** Well-organized with four named `\paragraph{}` blocks. All primitives ($g$, $\alpha_t$, $p$, $\phi$, $\eta$, $\xi$, $\theta_t$, $\Delta\theta$, $\gamma$, $\beta$) are introduced before any results. The θ evolution rule is the only expression that might benefit from promotion to display math.

**Section 2.2 (Equilibrium prices):** Proposition 1 states the P/D ratios in display math. The Γ definitions appear in a "where" clause, which is standard. Remark 1 gives the existence condition in display math. No assumptions are introduced for the first time inside propositions.

**Section 2.3 (Discussion):** Recalls earlier assumptions; no new model assumptions introduced.

**Section 3 (Quantitative Analysis):** Calibration parameters are clearly listed in prose. No new model assumptions.

**Section 4.1 (Extension 1 — Veto):** New parameters ($\lambda$, $\phi^+$, $\kappa$) are introduced in setup prose before Proposition 3. The assumption $\lambda > 1/2$ is stated in a `\noindent` sentence immediately after the bullet list, which is acceptable.

**Section 4.2 (Extension 2 — Transfers):** Tax rate $\tau$ and deadweight parameter $\delta_0$ are introduced in clear setup prose, followed immediately by the transfer consumption formula in display math.
