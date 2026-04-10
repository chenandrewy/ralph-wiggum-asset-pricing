# tests/factcheck-theory.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 9m 1s
[ralph-garage/agent-logs/20260409T200738.674238-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.674238-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to the assumptions.

## Requirement 1: Notational Consistency — PASS

Every mathematical symbol maps to a unique formal object. No collisions, reuse for different concepts, or meaningful ambiguities were found across 25 symbol families (10 Greek letters, 15 Roman/compound symbols).

**Minor observations** (not failures):
1. **Undefined period utility symbol $u$** (line 237, proof of Proposition 3): The symbol $u$ appears once ("but $u$ is concave") without formal definition. The period felicity $u(c) = c^{1-\gamma}/(1-\gamma)$ is implicit in $U_0^H$ (eq 3) but never introduced as $u$. Meaning is clear from context; standard practice in the field.
2. **Implicit time-subscript dropping**: The setup uses $\alpha_t$, $\theta_t$ with time subscripts, but the equilibrium formulas (Proposition 1, Extension 2) write $\alpha$, $\theta$ without subscripts. The appendix proof explains the stationarity assumption that justifies this, but the convention is never stated as a global rule.

## Requirement 2: Assumption Consistency — PASS

24 formal assumptions were identified across the baseline model (A1–A13), Extension 1 (A14–A18), Extension 2 (A19–A22), and proposition-level conditions (A23–A24). No pair of assumptions imposes contradictory constraints.

**Checks performed:**
- **Contradictory constraints**: None found. Extension 1 explicitly augments the baseline singularity by splitting it into positive/negative sub-types; the negative sub-case reduces to the baseline.
- **Parameter domains**: Compatible across all uses. Two implicit constraints noted:
  - $\phi \leq 1 - \Delta\theta$ (needed for $\alpha_t \leq 1 - \theta_t$ to survive repeated singularities). Not stated; satisfied by all calibrated values ($0.5 \leq 0.8$; $0.05 \leq 0.8$).
  - $\delta\tau < 1$ (needed for net transfers to be positive). Not stated; always satisfied when $\delta < 1$ since $\tau < 1$.
- **Structural equations**: Consistent across baseline and both extensions. Consumption dynamics, dividend dynamics, and the Euler equation pricing framework are coherent.
- **Budget constraint / accounting**: Aggregate consumption $C_t$ is exhausted between household ($\alpha_t C_t$) and AI owners ($(1-\alpha_t)C_t$). Private AI capital dividends $(1-\alpha_t - \theta_t)C_t \geq 0$ by the domain constraint $\alpha_t \leq 1-\theta_t$. The model is reduced-form (consumption-based pricing), so full GE budget balance is outside scope and not claimed.
- **Transfer base**: Tax base $(1-\phi\alpha)(1+\eta)(1+g)C_t$ equals AI owners' post-singularity share. The $\phi_\text{eff}$ derivation and transfer ratio (eq 9) are algebraically verified.
- **Proof algebra** (Appendix A): Euler equation expansion (eq 11) and solved P/D (eq 12) match Proposition 1. Verified step by step.

## Requirement 3: Traceability — PASS

All mathematical objects not appearing directly in the assumptions were traced back:

| Object | Traced to |
|--------|-----------|
| $\Gamma^{AI}$, $\Gamma^{N}$ | A6 (singularity jump), A8–A9 (dividend dynamics) |
| $A^j$ (existence condition) | A2, A5–A7, A12 |
| P/D ratios (eqs 4–5) | Euler equation from A12, A24, A2–A3, A5–A10 |
| $v^{AI}$ (appendix) | Notation for P/D ratio |
| $\phi_\text{eff}$ | Algebraic rearrangement of A21 |
| Transfer ratio (eq 9) | Algebraic manipulation of A21 |
| $c^H_{post}$, $c^H_{no\text{-}transfer}$ | A21, A3, A6 |
| $(\alpha', \theta')$ | Post-singularity values per A6, A9 |
| $u$ (line 237) | Period utility implicit in A12 (symbol not formally introduced) |

No expression was found that cannot be logically derived from the stated assumptions.
