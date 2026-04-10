# tests/theory-clarity.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 1m 52s
[ralph-garage/agent-logs/20260409T213452.252463-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.252463-0400_theory-clarity_claude_opus.log)

# theory-clarity
VERDICT: PASS
REASON: All key model assumptions are introduced in clearly labeled setup paragraphs with the most critical expressions in display math; prose assumptions appear at or near paragraph/bullet starts.

## Key Items Identified

### Display math in main text (all present)
1. Aggregate consumption growth $C_{t+1} = (1+g)C_t$ — Eq. 1
2. Displacement rule $\alpha_{t+1} = \phi\alpha_t$ — Eq. 2
3. CRRA utility — Eq. 3
4. Existence condition $A^j < 1$ — Eq. 5
5. Post-transfer consumption — Eq. 6
6. Effective displacement $\phi_\text{eff}$ — Eq. 7
7. Transfer consumption ratio — Eq. 8

### Prose assumptions (all at paragraph/bullet starts)
A. Household share $c_t^H = \alpha_t C_t$ — opens sentence after Eq. 1
B. AI dividend share $D_t^{AI} = \theta_t C_t$ and expansion rule — opens Assets bullet
C. Singularity probability $p$ and extinction probability $\xi$ — opens Singularity paragraph
D. Market incompleteness (restricted equity) — opens its own paragraph after asset bullets
E. Veto cost and extinction normalization — opens Section 4.1 setup
F. Transfer tax $\tau$ and deadweight cost $\delta\tau$ — opens Section 4.2 setup

### Derived quantities defined inside propositions
G. Dividend growth factors $\Gamma^{AI}$, $\Gamma^{N}$ — defined in the "where" clause of Proposition 1

## Section-Level Findings

**Section 2.1 (Setup):** Well-organized. Four labeled paragraphs (Consumption, Singularity, Assets, Preferences) each introduce their assumptions clearly. The most critical expressions (Eqs. 1–3) are in display math. Prose assumptions (items A–D) all appear at or near the start of their paragraph or bullet. The productivity boost $(1+\eta)$ and AI share expansion $\Delta\theta$ are introduced inline in structured lists, which is appropriate for their role.

**Section 2.2 (Equilibrium prices):** The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined only inside Proposition 1's "where" clause. These are derived quantities (following from $\theta$, $\Delta\theta$, and $\eta$, all previously defined), not new model assumptions, so this is acceptable. The discussion paragraph after Proposition 1 (line 151) effectively explains their economic content.

**Section 2.3 (Discussion):** No new model assumptions introduced; recalls earlier ones appropriately.

**Section 3 (Quantitative Analysis):** Calibration values are stated clearly at the start of the discussion paragraph. No new assumptions.

**Section 4.1 (Extension 1 — Veto):** The positive singularity rule ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$) and the extinction utility normalization are introduced in the opening setup prose before Proposition 3, at or near paragraph starts.

**Section 4.2 (Extension 2 — Transfers):** The transfer mechanism ($\tau$, $\delta\tau$) is introduced in a setup paragraph before the display equations. The post-transfer consumption (Eq. 6), $\phi_\text{eff}$ (Eq. 7), and transfer ratio (Eq. 8) all appear in display math. The progression from setup prose to display equations is clear and well-sequenced.
