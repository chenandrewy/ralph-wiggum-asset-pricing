# tests/factcheck-theory.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 7m 29s
[ralph-garage/agent-logs/20260412T202602.592189-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.592189-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: FAIL
REASON: Proposition 3(i) relies on the condition $\phi(1+\eta) < 1$, which is neither a stated assumption nor implied by the stated assumptions, so the result cannot be logically derived from the paper's formal premises.

## Requirement 1: Notational Consistency — PASS

The paper uses 25 symbol families, all well-defined with non-overlapping meanings. Three minor issues were identified, none constituting genuine ambiguity:

1. **Silent subscript drop for $\theta$**: The paper explicitly announces dropping the time subscript for $\alpha$ (line 202) but does so silently for $\theta$ starting in Proposition 1. Contextually clear in stationary equilibrium.
2. **$V$ vs. $v$ overlap**: $V$ is used for household value functions in the veto analysis (Section 4.1), while $v^{AI}$ is used for P/D ratio shorthand in Appendix A. These appear in completely separate contexts and carry different subscript conventions.
3. **$\alpha^+$ notation**: A one-off superscript convention defined and used in a single line of the Proposition 3 proof.

Full notation report: `ralph-garage/scratch/factcheck-notation.md`.

## Requirement 2: Mutual Consistency of Assumptions — PASS

24 assumptions were cataloged across the baseline model and extensions. All are mutually consistent: no contradictory parameter restrictions, no conflicting functional forms, and no baseline-vs-extension conflicts.

Two minor exposition gaps (not inconsistencies) were identified:

1. **$\phi(1+\eta) < 1$ is used but not formally assumed.** This condition is essential for the negative singularity to cause a household consumption drop, and is required by the Proposition 3 proof. It is not implied by $\phi \in (0,1)$ and $\eta > 0$ (e.g., $\phi = 0.9, \eta = 0.5 \Rightarrow \phi(1+\eta) = 1.35 > 1$). All calibrations satisfy it, but it is not stated as a maintained assumption.
2. **$\delta\tau < 1$ is implicitly needed** for transfers to benefit the household, but is stated only conditionally rather than as an assumption. All calibrations satisfy it.

Full assumptions report: `ralph-garage/scratch/factcheck-assumptions.md`.

## Requirement 3: Traceability to Assumptions — FAIL

### Objects successfully traced

All derived mathematical objects trace back to the stated assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $c_t^H = \alpha_t C_t$ | A3 ($\alpha_t$), A2 ($C_t$) |
| $D_t^{AI} = \theta_t C_t$ | A8 ($\theta_t$), A2 ($C_t$) |
| $D_t^N = (1-\theta_t) C_t$ | A9, A8, A2 |
| $\Gamma^{AI}, \Gamma^N$ | A8 ($\theta$, $\Delta\theta$), A5 ($\eta$) |
| $A^j$ (existence condition) | A12 ($\beta$, $\gamma$), A2 ($g$), A4 ($p$), A7 ($\xi$), A5 ($\eta$), A6 ($\phi$), $\Gamma^j$ |
| P/D ratios (Prop. 1) | Euler equation from A12, all baseline primitives |
| Extinction attenuation (Prop. 2) | $A^j$ decomposition, $\Gamma^{AI} > \Gamma^N$ from A8 |
| $c^H_{post}$ | A6 ($\phi$), A3 ($\alpha$), A5 ($\eta$), A2 ($g$, $C_t$), A21 ($\tau$), A22 ($\delta$) |
| $\phi_\text{eff}$ | A6 ($\phi$), A21 ($\tau$), A22 ($\delta$), A3 ($\alpha$) |
| Transfer ratio (eq. 9) | Derived from $c^H_{post}$ and $c^H_{no\text{-}transfer}$ |
| $V_\text{veto}, V_\text{develop}, V_\text{develop}^{CM}$ | A12, A17 ($\kappa$), A4 ($p$), A7 ($\xi$), A15 ($q$), A5, A6, A3 |

### Expression that cannot be derived from stated assumptions

**Proposition 3(i) — Veto under incomplete markets (line 214–216):**

The proposition states unconditionally: *"there exists a threshold $\bar{\gamma}$ such that for all $\gamma > \bar{\gamma}$, the household vetoes AI development."*

The proof (line 228) establishes this by showing $\Delta u(\gamma) \to -\infty$ as $\gamma \to \infty$, which requires $\phi\alpha(1+\eta) < \alpha$, i.e., $\phi(1+\eta) < 1$. This is the condition that ensures the negative singularity causes a household consumption drop.

**The problem:** $\phi(1+\eta) < 1$ is:
- Not stated as a formal assumption anywhere in the paper.
- Not implied by the stated assumptions ($\phi \in (0,1)$ and $\eta > 0$ do not jointly imply $\phi(1+\eta) < 1$).
- Mentioned only conditionally within the proof text ("when $\phi(1+\eta) < 1$"), not in the proposition statement.
- Used earlier in the paper (line 159) also only conditionally ("$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small").

Without this condition, if $\phi(1+\eta) \geq 1$, the household's consumption rises even in the "negative" singularity, the utility cost $\Delta u(\gamma)$ does not diverge to $-\infty$, and the veto result does not hold. Therefore, Proposition 3(i) as stated cannot be logically derived from the paper's formal premises.

**Fix:** Either add $\phi(1+\eta) < 1$ as a maintained assumption in the model setup, or add it as an explicit condition in Proposition 3(i)'s statement (e.g., "Suppose $\phi(1+\eta) < 1$. Then there exists...").
