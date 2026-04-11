# tests/theory-deadweight.py
Started: 2026-04-11 15:15:58 EDT
Runtime: 2m 19s
[ralph-garage/agent-logs/20260411T151558.933513-0400_theory-deadweight_claude_opus.log](../ralph-garage/agent-logs/20260411T151558.933513-0400_theory-deadweight_claude_opus.log)

# theory-deadweight
VERDICT: PASS
REASON: Every formal object in the paper contributes to an economic claim, calibration, or quantitative result; no formalism is introduced and abandoned, ceremonial, or replaceable by plain English without weakening the argument.

## Detailed Audit

### Parameters and Variables

All 15 parameters ($C_t, g, \alpha_t, p, \xi, \eta, \phi, \theta_t, \Delta\theta, \gamma, \beta, q, \kappa, \tau, \delta$) are used in at least one proposition, calibration (Table 1), or figure. None are introduced and dropped.

- $C_t, g, \alpha_t, \phi, \eta, \theta_t, \Delta\theta, \gamma, \beta, p, \xi$: appear in the P/D formulas (Prop 1), calibration table, or Prop 2.
- $q, \kappa$: introduced in Extension 1 and used in Prop 3 (veto).
- $\tau, \delta$: introduced in Extension 2 and used in the transfer consumption equation, $\phi_\text{eff}$, and Figure 2.

### Propositions

- **Proposition 1 (P/D ratios):** Central result. Closed-form expressions enable the $\Gamma^{AI}$ vs. $\Gamma^{N}$ comparison and the quantitative table. Cannot be stated in English.
- **Proposition 2 (Extinction attenuation):** Qualitative takeaway ("extinction attenuates the spread") could be stated in English, but the formal proof adds the non-obvious result about the *ratio* also decreasing via a convexity argument. This is a genuine comparative static, not decoration.
- **Proposition 3 (Veto):** The interplay of risk aversion $\gamma$, displacement $\phi$, and positive-singularity probability $q$ is inherently quantitative. The complete-markets comparison in part (ii) is essential to the incomplete-markets argument.

### Remark 1 (Existence condition)

Introduced in Section 2 and used substantively in Extension 2, where the "infinite price" discontinuity under severe displacement motivates government transfers. Not abandoned.

### Equations

- **Eq. (1)** (consumption growth): Establishes $(1+g)$ notation used in all P/D formulas. One line.
- **Eq. (2)** (displacement): Defines $\phi$, central to the paper.
- **Eq. (3)** (utility): Standard CRRA. Could arguably be inline, but establishes notation for the SDF and is conventional in asset pricing theory papers. One line.
- **Eqs. (4)-(5)** (P/D ratios): Central results.
- **Eq. (6)** (existence condition): Used in Remark 1 and Extension 2.
- **Eq. (7)** (veto delta utility): Used in Prop 3 proof.
- **Eq. (8)** (transfer consumption): Foundation for Extension 2.
- **Eq. (9)** ($\phi_\text{eff}$): Cleanly connects transfers to the P/D formula without re-derivation.
- **Eq. (10)** (transfer ratio): Shows non-obvious result that the ratio is independent of $\eta$.
- **Eqs. (11)-(13)** (appendix proof): Required for Prop 1 proof.

### Auxiliary Concepts

- **Kaldor-Hicks efficiency** (Extension 1): Invoked in two sentences to clarify the welfare criterion. Standard economics terminology for the target audience; immediately resolved ($\eta > 0$ implies it holds). Not ceremonial — it distinguishes Kaldor-Hicks from Pareto efficiency, which matters since the household is harmed in the negative singularity.
- **$\Gamma^{AI}$ and $\Gamma^{N}$** (dividend growth factors): Carry the key economic comparison. Used in Prop 1, Prop 2, and the discussion. Not auxiliary.
- **$A^j$** (Remark 1 / Prop 2 proof): Compact notation for a quantity used in two places.

### What Was NOT Found

- No variable or parameter introduced and unused in any result.
- No proposition whose content is purely ceremonial or could be fully replaced by plain English.
- No auxiliary formal detour that fails to advance the hedging/incompleteness argument.
- No formalism introduced in one section and abandoned in subsequent analysis.
- No "pompous" machinery — the model is a single discrete-time setup with CRRA preferences and three states per period.
