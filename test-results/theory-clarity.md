# tests/theory-clarity.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 2m 14s
[ralph-garage/agent-logs/20260412T200023.658860-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.658860-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: Key model assumptions are organized in named setup paragraphs with display math for critical expressions; no major assumption is buried or missing from the model-setup sections.

## Key items identified

**Should appear in display math (and do):**
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — eq. (1), display math
2. Displacement equation $\alpha_{t+1} = \phi\alpha_t$ — eq. (2), display math
3. CRRA utility — eq. (3), display math
4. P/D ratio formulas — eqs. (4)–(5), inside Proposition 1 (appropriate)
5. Existence condition $A^j < 1$ — eq. (6), display math in Remark 1
6. Post-transfer consumption — eq. (7), display math
7. Effective displacement $\phi_\text{eff}$ — eq. (9), display math
8. Transfer ratio — eq. (10), display math

**Prose items (should be near paragraph start):**
9. Household share $c_t^H = \alpha_t C_t$ — inline after eq. (1), acceptable
10. Singularity probabilities $p$, $\xi$ — start of Singularity paragraph
11. AI dividend share $\theta_t$ and update rule — start of Assets bullet
12. Market incompleteness — dedicated paragraph in Assets subsection
13. $\gamma > 1$, $\beta \in (0,1)$ — start of Preferences paragraph
14. Extension 1 parameters ($q > 1/2$, $\kappa > 0$) — mid-paragraph in Extension 1
15. Extension 2 parameters ($\tau$, $\delta$) — mid-paragraph in Extension 2

## Section-level findings

**Section 2.1 (Setup):** Well-organized. Named paragraphs (Consumption, Singularity, Assets, Preferences) each introduce assumptions clearly. Display math for the three foundational equations. The parameters $\phi$, $\eta$, $\Delta\theta$ are introduced in structured list items, which serve an equivalent organizational role to paragraph starts. The household share definition $c_t^H = \alpha_t C_t$ is inline math rather than display, but is simple enough that this is fine.

**Section 2.2 (Equilibrium prices):** The P/D ratios and dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ appear inside Proposition 1. Since these are derived results rather than new assumptions, this placement is appropriate. The existence condition gets its own Remark block with display math. The condition $\phi(1+\eta) < 1$, which is important for the hedging channel, is discussed in the text after Proposition 1 (line 153) rather than stated as a formal assumption; this is acceptable since it is a parametric condition implied by calibration, not a structural assumption.

**Section 2.3 (Discussion):** No new assumptions introduced; recalls and interprets earlier ones. No issues.

**Section 3 (Quantitative Analysis):** Parameter values clearly listed at the start. No new model assumptions.

**Section 4.1 (Extension 1 — Veto):** The positive singularity probability $q > 1/2$, veto cost $\kappa > 0$, and complete-markets consumption are introduced in prose paragraphs. These are mid-paragraph rather than at paragraph starts, but the extension section is compact and the parameters are introduced before they are used. Minor organizational point, not a clarity failure.

**Section 4.2 (Extension 2 — Transfers):** Tax rate $\tau$ and deadweight cost $\delta$ are introduced mid-paragraph (line 239), but immediately followed by the display-math equation for post-transfer consumption. The effective displacement $\phi_\text{eff}$ gets its own display equation. Adequate clarity.
