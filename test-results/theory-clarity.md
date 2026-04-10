# tests/theory-clarity.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 1m 45s
[ralph-garage/agent-logs/20260409T202148.448641-0400_theory-clarity_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.448641-0400_theory-clarity_claude_opus.log)

# theory-clarity

VERDICT: PASS
REASON: Key model assumptions are introduced in clearly labeled setup paragraphs with display math for the most critical expressions; no essential assumption is buried in a proof or proposition-only context.

## Key items identified

### Should appear in display math (and do)
- **A.** Aggregate consumption growth $C_{t+1}=(1+g)C_t$ — eq. (1), display math ✓
- **B.** Displacement rule $\alpha_{t+1}=\phi\alpha_t$ — eq. (2), display math ✓
- **C.** CRRA utility with $\gamma>1$ — eq. (3), display math ✓
- **D.** Existence condition $A^j<1$ — eq. (6), display math ✓
- **E.** Post-transfer consumption — eq. (5), display math ✓
- **F.** Transfer ratio — eq. (7), display math ✓

### May remain in prose (and are appropriately placed)
- **G.** Singularity probability $p$ — first sentence of "Singularity" paragraph ✓
- **H.** Household share $c_t^H=\alpha_t C_t$ — in "Consumption" paragraph ✓
- **I.** Consumption jump factor $(1+\eta)$ — in enumerated singularity list ✓
- **J.** Extinction probability $\xi$ — in enumerated singularity list ✓
- **K.** AI dividend share jump $\theta_{t+1}=\theta_t+\Delta\theta(1-\theta_t)$ — in "Assets" itemized list ✓
- **L.** Market incompleteness (private AI capital) — start of paragraph after asset list ✓
- **M.** Positive singularity probability $\lambda>1/2$ — Extension 1 setup prose ✓
- **N.** Veto option — Extension 1 setup paragraph ✓
- **O.** Tax rate $\tau$ and deadweight cost $\delta$ — Extension 2 setup paragraph ✓
- **P.** Effective displacement $\phi_\text{eff}$ — Extension 2 prose after eq. (5) ✓
- **Q.** Extinction utility normalization $U_\text{ext}=0$ — Extension 1 setup prose ✓

## Section-level findings

### Section 2.1 (Setup)
Clear and well-organized. Four named `\paragraph{}` blocks (Consumption, Singularity, Assets, Preferences) introduce all baseline assumptions. Display math is used for the three most critical expressions (consumption growth, displacement rule, utility). The singularity event tree and asset definitions use enumerated/itemized lists, which is appropriate for their multi-part structure. One minor note: the AI dividend share jump rule (item K) is important enough that display math could be justified, since it directly determines $\Gamma^{AI}$ and $\Gamma^{N}$, but its current placement at the start of a bullet point is acceptable.

### Section 2.2 (Equilibrium prices)
The dividend growth factors $\Gamma^{AI}$ and $\Gamma^{N}$ are defined in the "where" clause of Proposition 1 rather than in a setup paragraph. This is acceptable: they are derived quantities (functions of $\theta$ and $\Delta\theta$) rather than new model assumptions, and defining them at point of use is standard practice.

### Section 2.3 (Discussion)
No new assumptions introduced. Provides economic interpretation of the mechanism.

### Section 3 (Quantitative Analysis)
Calibration parameters are clearly stated in prose at the start of the section. No new model assumptions.

### Section 4.1 (Extension 1: Veto)
New assumptions ($\lambda$, $\lambda>1/2$, veto option, extinction utility normalization) are introduced in setup prose before Proposition 3. The structure is clear: itemized list for the positive/negative singularity split, then prose paragraphs for the veto and normalization.

### Section 4.2 (Extension 2: Transfers)
Setup prose introduces $\tau$ and $\delta$ before the display-math post-transfer consumption formula. The effective displacement parameter $\phi_\text{eff}$ is introduced inline immediately after, which is appropriate for a derived quantity.
