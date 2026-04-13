# tests/factcheck-theory.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 6m 55s
[ralph-garage/agent-logs/20260412T200023.686135-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.686135-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

28 symbol families were identified across the paper. Zero true collisions were found. No symbol family is reused for a different formal object, semantic role, model, or decision problem without explicit renaming.

Two low-severity notes (neither constitutes ambiguity for the target audience):

1. **$\Delta$ prefix dual use.** $\Delta\theta$ is a fixed parameter (jump in AI share), while $\Delta u(\gamma)$ uses $\Delta$ as a difference operator. These are syntactically distinguishable ($\Delta\theta$ takes no argument; $\Delta u(\gamma)$ is applied to a function).

2. **Time-subscript suppression.** The paper uses two conventions: explicit statement for $\alpha$/$\theta$ (Section 4: "we write $\alpha$ for $\alpha_t$") and implicit stationarity for P/D ratios in Proposition 1. Both are clearly communicated. $\Gamma^{AI}$ implicitly depends on $\theta_t$, which is acknowledged in the Appendix.

Full notation audit: `ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Assumption Consistency — PASS

35 assumptions were identified across the baseline model (20), Extension 1/Veto (8), and Extension 2/Transfers (7). No contradictions or inconsistencies were found.

- No contradictory parameter restrictions. Each parameter has a single domain maintained consistently.
- No functional form conflicts. CRRA utility and multiplicative displacement used uniformly.
- No stochastic process conflicts. Baseline and extension singularity processes are clearly delineated.
- No extension-baseline conflicts. Extensions augment rather than contradict.
- No implicit-explicit conflicts. The key implicit condition $\phi(1+\eta) < 1$ is always satisfied in calibrations and stated as sufficient where needed.

Minor notes (not inconsistencies):

1. $\phi(1+\eta) < 1$ is required for the veto result (Prop. 3) but is not given a formal assumption label.
2. $\delta\tau < 1$ (needed for transfers to be net-positive) is not explicitly stated as a maintained assumption, though always satisfied in calibrations.
3. Extensions 1 and 2 are not formally combined into a unified model.
4. The $\min(1, \alpha/\phi)$ cap could push $\alpha_t$ to exactly 1, technically extending the stated domain $(0,1)$ to $(0,1]$.

Full assumptions audit: `ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability — PASS

All mathematical objects not among the primitive assumptions were traced back to those assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $\Gamma^{AI}$, $\Gamma^{N}$ (dividend growth factors) | A6, A9, A10 |
| $A^j$ (existence condition) | A3, A5, A6, A7, A8, A14 + $\Gamma^j$ |
| P/D ratios (Prop. 1) | A2, A3–A11, A14, A16 |
| $B$, $S$, $f$ (Prop. 2 proof auxiliaries) | Defined from primitives |
| $\Delta u(\gamma)$ (Eq. 7) | A4, A6, A7, A14, A21, A22 |
| $\alpha^+ = \min(1, \alpha/\phi)$ | A4, A7, A21 |
| $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ | A14, A24, A25, A27 + singularity process |
| $\bar{\gamma}$ (Prop. 3 threshold) | Derived from full assumption set |
| $c^H_{post}$ (Eq. 8) | A4, A6, A7, A29, A30 |
| $\phi_\text{eff}$ (Eq. 9) | Derived from Eq. 8 |
| Transfer ratio (Eq. 10) | Derived from Eq. 8 |
| Euler equation (Appendix) | A2, A14 |

No expression was found that cannot be logically derived from the assumptions.
