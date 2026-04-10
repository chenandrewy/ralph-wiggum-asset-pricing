# tests/theory-clarity.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260409T194838.517967-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.517967-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in labeled setup paragraphs with the most critical expressions in display math; two moderate-priority items (household consumption formula, AI dividend share dynamics) remain inline but are clearly placed at the start of their respective paragraphs.

## Key items identified

### Should appear in display math (and do)
1. Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq (1), Section 2.1 Consumption paragraph
2. Displacement rule $\alpha_{t+1}=\phi\alpha_t$ — eq (2), Section 2.1 Singularity paragraph
3. CRRA utility — eq (3), Section 2.1 Preferences paragraph
4. P/D ratio formulas — eqs (4)–(5), Proposition 1
5. Existence condition $A^j<1$ — eq (6), Remark 1
6. Veto gain $\Delta U^H$ — eq (7), Proposition 3
7. Post-transfer consumption — eq (8), Section 4.2
8. Transfer ratio — eq (9), Section 4.2

### Could benefit from display math but acceptable inline
9. Household consumption $c_t^H = \alpha_t C_t$ — inline at line 85, start of Consumption paragraph
10. AI dividend share dynamics $\theta_{t+1}=\theta_t+\Delta\theta(1-\theta_t)$ — inline in Assets bullet, line 105

### Appropriately remain in prose
11. Singularity probability $p$ — start of Singularity paragraph
12. Productivity jump $(1+\eta)$ — enumerated item in Singularity paragraph
13. Extinction probability $\xi$ — enumerated item in Singularity paragraph
14. Market incompleteness (private AI capital untradeable) — Assets paragraph, line 109
15. Extension 1 parameters ($\lambda$, $\phi^+$, $\kappa$, $\lambda>1/2$) — start of Section 4.1 setup
16. Extension 2 parameters ($\tau$, $\delta_0$) — start of Section 4.2 setup

## Section-level findings

**Section 2.1 (Setup):** Well-organized with labeled paragraphs. All foundational assumptions appear in dedicated model-setup blocks. Minor observation: the AI dividend share law of motion (item 10) is the most important inline expression and would benefit from display math, since it directly determines the $\Gamma$ factors that drive the valuation spread. The household consumption formula (item 9) is also inline but is a simple definition at the paragraph start and does not cause confusion.

**Section 2.2 (Equilibrium prices):** P/D formulas and $\Gamma$ definitions appear in display math inside Proposition 1. The existence condition is properly highlighted in Remark 1 with its own displayed equation. No new model assumptions are introduced here — only results derived from the setup.

**Section 2.3 (Discussion):** No new assumptions. Properly references prior setup.

**Section 3 (Quantitative Analysis):** Calibration values stated clearly at the start of the discussion paragraph (line 193). No new model assumptions.

**Section 4.1 (Extension 1 — Veto):** New parameters ($\lambda$, $\phi^+$, $\kappa$) introduced in clear setup prose with bullet items before the proposition. The social efficiency assumption $\lambda>1/2$ is stated at the start of its own sentence. The veto gain expression is in display math inside Proposition 3, which is acceptable since it is both a definition and a result.

**Section 4.2 (Extension 2 — Transfers):** Tax rate $\tau$ and deadweight cost $\delta_0$ introduced in setup prose before any formal result. Post-transfer consumption and the transfer ratio both appear in display math. Clear and well-sequenced.

**Appendix A:** Contains only the proof of Proposition 1. The stationarity approximation (post-singularity P/D ≈ pre-singularity P/D, line 311) is stated here but is a technical simplification for the proof, not a new model assumption that the reader needs to evaluate the main results.
