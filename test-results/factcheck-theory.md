# tests/factcheck-theory.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 9m 9s
[ralph-garage/agent-logs/20260409T194838.528159-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.528159-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: FAIL
REASON: Notational inconsistencies in the utility family ($U_0$ vs. $\Delta U^H$ superscript; $u_\text{ext}$ case ambiguity) and an undisclosed parameter ($\alpha_0 = 0.70$) used in the Extension 2 figure violate the consistency and traceability requirements.

---

## Requirement 1: Notational Consistency — FAIL (minor)

**No symbol collisions found.** No symbol is reused for a genuinely different formal object. The paper is clean in this regard.

**Ambiguities found:**

1. **$U_0$ vs. $\Delta U^H$ superscript inconsistency (MEDIUM).** $U_0$ (Eq. 3) denotes the household's lifetime utility but lacks the $H$ superscript. $\Delta U^H$ (Eq. 5) denotes the household's one-period utility gain and carries the $H$ superscript. Both refer to the same household. The inconsistency does not create genuine confusion (there is only one household), but it is a notational inconsistency.

2. **$u_\text{ext}$ case ambiguity (MEDIUM).** The prose refers to "normalizing extinction utility to zero" using $u_\text{ext}$. Lowercase $u$ denotes period utility throughout the paper, but extinction utility is a continuation (lifetime) value, which should be $U_\text{ext}$ by the paper's own uppercase/lowercase convention.

3. **$\delta_0$ subscript unexplained (LOW-MEDIUM).** The subscript "0" has no companion ($\delta_1$, etc.) and clashes with the paper's convention where subscript 0 means "at date 0" ($U_0$, $\mathbb{E}_0$). Should be $\delta$ or the subscript should be explained.

4. **Time-subscript dropping convention unstated (MINOR).** Both $\alpha_t$ and $\theta_t$ are introduced as time-varying, but appear without subscripts in Propositions 1 and 3 and Extension 2. The convention (bare = current/pre-singularity) is standard but never declared.

5. **$\Gamma^j$ naming ambiguity (MINOR).** Called "dividend growth factor" but actual dividend growth in a singularity is $\Gamma^j(1+g)$, not $\Gamma^j$ alone.

6. **$\Delta\theta$ naming (MINOR).** The $\Delta$ prefix conventionally suggests a first difference, but $\Delta\theta$ is a rate parameter; the actual change in $\theta$ is $\Delta\theta(1-\theta_t)$.

7. **$\phi(1+\eta) < 1$ is an implicit assumption (MINOR).** Used in the economic narrative but never formally stated as a maintained assumption. Both calibrations satisfy it.

8. **$\alpha_t \leq 1-\theta_t$ not verified under dynamics (MINOR).** Stated once in Setup but the implicit requirement $\phi \leq 1-\Delta\theta$ for preservation under singularity transitions is never stated (naturally satisfied by all calibrations).

---

## Requirement 2: Mutual Consistency of Assumptions — PASS

All formally stated assumptions are mutually consistent. Detailed checks confirmed:

- **Parameter domains compatible** across all sections and calibrations, including after repeated singularities.
- **Probability weights sum to 1** in both the baseline and Extension 1 probability trees.
- **CRRA functional form and SDF specification consistent** across all sections.
- **Budget/resource constraints hold exactly**, including with government transfers (household + AI owners + deadweight loss = aggregate output).
- **Existence condition** $A^j < 1$ satisfied for baseline calibration ($A^{AI} = 0.987$ at $p = 1\%$, $\xi = 0$) and correctly identified as violated for large-singularity case ($A^{AI} = 2.37$ at $\tau = 0$), matching the paper's narrative.
- **Extensions branch independently** off the baseline with no cross-contamination.
- **Code parameters match paper parameters** exactly for all 12 disclosed values.

No pair of assumptions contradicts another.

---

## Requirement 3: Traceability — FAIL (minor)

**One undisclosed parameter:**

- **$\alpha_0 = 0.70$**: Used in the R code (`alpha0 <- 0.70`) for the Extension 2 figure (Panel (a): P/D ratios as a function of $\tau$; Panel (b): consumption change). The paper never states this value. The transfer ratio (Eq. 7) and post-transfer consumption (Eq. 6) depend on $\alpha$, so the figure implicitly assumes $\alpha = 0.70$ without disclosing this to the reader. This parameter is not traceable to any stated assumption in the paper.

**One unstated derivation:**

- **Effective $\phi$ for P/D with transfers.** The code computes $\phi_\text{eff} = \phi + \tau(1-\delta_0\tau)(1-\phi\alpha)/\alpha$ to generate Panel (a) of Figure 2. This formula is not derived or stated in the paper. It follows directly from Eq. 6 by expressing post-transfer consumption as $\phi_\text{eff} \cdot \alpha \cdot (1+\eta)(1+g)C_t$ and substituting into the P/D formula from Proposition 1. The derivation is correct but unstated.

**All other objects are traceable.** Every parameter, state variable, dividend, price, and derived quantity can be traced back through explicit definitions to the stated assumptions.

---

## Summary of Issues Requiring Fixes

| # | Issue | Requirement | Severity |
|---|-------|-------------|----------|
| 1 | $U_0$ should be $U_0^H$ for consistency with $\Delta U^H$ | Req. 1 | Medium |
| 2 | $u_\text{ext}$ should be $U_\text{ext}$ (lifetime, not period utility) | Req. 1 | Medium |
| 3 | $\delta_0$ subscript unexplained or should be plain $\delta$ | Req. 1 | Low-Medium |
| 4 | $\alpha_0 = 0.70$ used in figure code but not stated in paper | Req. 3 | Low-Medium |
| 5 | Effective-$\phi$ formula for P/D with transfers not derived in paper | Req. 3 | Low-Medium |
| 6 | Time-subscript dropping convention should be stated | Req. 1 | Minor |
| 7 | $\phi(1+\eta) < 1$ should be stated as maintained assumption | Req. 1 | Minor |
