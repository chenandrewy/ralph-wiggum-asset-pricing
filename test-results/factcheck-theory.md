# tests/factcheck-theory.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 8m 25s
[ralph-garage/agent-logs/20260411T161024.950254-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.950254-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical objects trace back to the stated assumptions.

## Requirement 1: Notational Consistency — PASS

Reviewed 30 symbol families. Three minor flags, none constituting a true semantic collision:

1. **$\theta$ subscript convention shift** (moderate): In the body, $\theta_t$ is time-indexed. In Appendix A, $\theta_0, \theta_1, \theta_2, \ldots$ index the chain of post-singularity states. The text at line 316 explicitly defines the chain ("$\theta_0, \theta_1 = \theta_0 + \Delta\theta(1-\theta_0), \theta_2, \ldots$"), which disambiguates. No reader would confuse the two usages.

2. **Implicit time-subscript dropping** (minor): $\alpha_t$ and $\theta_t$ lose their subscripts when the paper moves to stationary-equilibrium expressions. Standard practice for the target audience.

3. **Dual use of $\Delta$** (minor): $\Delta\theta$ is a compound parameter name; $\Delta u(\gamma)$ uses $\Delta$ as a difference operator. Both are conventional and unambiguous in context.

No symbol family is reused for a genuinely different formal object.

## Requirement 2: Assumption Consistency — PASS

Cataloged 24 assumptions across Sections 2.1–4.2 and Appendix A. No contradictions found.

Key checks:
- $\phi(1+\eta) < 1$ (Prop 3 proof) is a tighter restriction than $\phi \in (0,1)$ but is correctly scoped to the veto result and satisfied by all calibrations.
- Existence condition $A^j < 1$ is correctly noted as violated under large-singularity parameters ($\phi = 0.05$, $\eta = 9$); the paper uses this violation as a feature motivating transfers.
- Extinction utility $U_\text{ext} = 0$ with $\gamma > 1$ (negative CRRA utility) is explicitly discussed as making the veto result conservative.
- Extension assumptions augment rather than contradict the baseline.

Minor implicit restrictions (not inconsistencies): $p \in (0,1)$ and $\delta\tau < 1$ are not formally stated but are satisfied in all parameterizations.

## Requirement 3: Traceability — PASS

All mathematical objects trace to the stated assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $\Gamma^{AI}$, $\Gamma^{N}$ (dividend growth factors) | A5 ($\eta$), A8 ($\theta_t$, $\Delta\theta$) |
| P/D ratios, eqs. (4)–(5) | A2 ($g$), A4 ($p$), A5 ($\eta$), A6 ($\phi$), A7 ($\xi$), A8 ($\theta$, $\Delta\theta$), A11 ($\beta$, $\gamma$) via Euler equation |
| $A^j$, eq. (4) | Same as P/D ratios (collects primitives) |
| $B$, $S$ (Prop 2 proof locals) | Subsets of P/D primitives |
| $\Delta u(\gamma)$, eq. (6) | A5, A6, A11, A15 ($q$, $\alpha^+$) |
| $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ | A11, A17 ($\kappa$), A18 ($U_\text{ext}$), model primitives |
| $c^H_{post}$, eq. (7) | A6, A19 ($\tau$), A20 ($\delta$) |
| $\phi_\text{eff}$, eq. (8) | Algebraic rearrangement of eq. (7) |
| Transfer ratio, eq. (9) | Division of eq. (7) by displaced consumption |
| $\bar{\gamma}$ (Prop 3 threshold) | Existence guaranteed by limit argument using A6, A5, A11 |

**Algebraic verification of key derivations:**

- **Proposition 1 (P/D ratios):** Euler equation substitution verified step-by-step. The three consumption-growth states (no singularity, non-extinction singularity, extinction) correctly produce the closed-form $v^j = A^j/(1-A^j)$.
- **Proposition 2 (extinction attenuation):** The ratio $f(A^{AI})/f(A^N)$ decreases in $\xi$ because (i) $\Gamma^{AI}/A^{AI} > \Gamma^N/A^N$ (so proportional decrease in $A^{AI}$ exceeds that in $A^N$), and (ii) the elasticity of $f(A) = A/(1-A)$ is $1/(1-A)$, increasing in $A$. Both effects work in the same direction.
- **Proposition 3 (veto):** The limit $\Delta u(\gamma)/u(\alpha) \to +\infty$ as $\gamma \to \infty$ when $\phi(1+\eta) < 1$ is correct: the negative-singularity utility term $[\phi(1+\eta)]^{1-\gamma}$ dominates as $\gamma \to \infty$.
- **$\phi_\text{eff}$ derivation:** Factoring eq. (7) by $\alpha(1+\eta)(1+g)C_t$ correctly yields eq. (8).
- **Transfer ratio (eq. 9):** $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$, independent of $\eta$. Verified by direct division.

No expression was found that cannot be logically derived from the assumptions.
