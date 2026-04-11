# tests/factcheck-theory.py
Started: 2026-04-11 15:10:18 EDT
Runtime: 8m 17s
[ralph-garage/agent-logs/20260411T151018.396290-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260411T151018.396290-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

Inventoried 40+ mathematical objects across 8 symbol families. No symbol collisions, no missing definitions, no ambiguous notation.

Two minor stylistic observations (neither constitutes ambiguity):

1. **Subscript convention shift on $c^H$:** In Sections 2-3, subscripts denote time ($c_t^H$). In Extension 2, subscripts denote state/scenario ($c^H_{post}$, $c^H_{no\text{-}transfer}$). The two conventions never co-occur, so no formal ambiguity arises.

2. **$U$ subscript semantics:** $U_0^H$ uses time+agent indexing while $U_\text{ext}$ uses a state label. These appear in different contexts and are never confused.

Full notation inventory and analysis: `ralph-garage/scratch/factcheck-notation.md`

## Requirement 2: Assumption Consistency — PASS

Catalogued 16 explicit parameter restrictions, 10 derived/implicit assumptions, and 5 numerical parameterizations. All are mutually consistent.

Key verifications:
- $\phi(1+\eta) < 1$ satisfied in all parameterizations: $0.75 < 1$ (baseline), $0.5 < 1$ (large singularity)
- Existence condition $A^j < 1$ satisfied for all baseline parameterizations; correctly reported as violated for large-singularity at $\tau = 0$
- Prop 2 convexity condition ($A^j > 1/2$, equiv. $P^j/D^j > 1$) verified against all table entries (smallest P/D is 9.7)
- Prop 3 limit argument mathematically correct under $\phi(1+\eta) < 1$
- All numerical parameterizations satisfy all applicable restrictions
- Non-AI closed-form P/D verified against table: $13.3$ at $p=1\%$, $\xi=0\%$ (exact match, since $\Gamma^N$ is $\theta$-independent)

One minor boundary observation: the positive singularity in Extension 1 can push $\alpha_t$ to exactly 1 via $\min(1, \alpha/\phi)$, touching the boundary of the stated open interval $(0,1)$. This does not break any result or create a logical contradiction.

Full assumptions analysis: `ralph-garage/scratch/factcheck-assumptions.md`

## Requirement 3: Traceability — PASS

All mathematical objects in the paper are either primitive parameters defined in the assumptions or derived quantities with explicit definitions traceable to those primitives:

- **Primitive parameters** (16): $t$, $g$, $\alpha_t$, $\phi$, $\eta$, $\Delta\theta$, $\gamma$, $\beta$, $p$, $\xi$, $\theta_t$, $\kappa$, $q$, $\tau$, $\delta$, $\bar{\gamma}$
- **Defined consumption objects**: $C_t$ (Eq 1), $c_t^H = \alpha_t C_t$, $c^H_{post}$ (Eq 8), $c^H_{no\text{-}transfer}$
- **Defined dividend objects**: $D_t^{AI} = \theta_t C_t$, $D_t^{N} = (1-\theta_t) C_t$
- **Derived pricing quantities**: $\Gamma^{AI}$, $\Gamma^N$ (from $\theta$, $\Delta\theta$, $\eta$); $A^j$ (Eq 5); P/D ratios (Prop 1, from Euler equation)
- **Proof auxiliaries**: $B$, $S$, $f(A)$, $v^{AI}$ (all defined at point of use)
- **Extension objects**: $\alpha^+$ (from $\alpha$, $\phi$); $\phi_\text{eff}$ (Eq 9, from $\phi$, $\tau$, $\delta$, $\alpha$); $\Delta u(\gamma)$ (Eq 7); $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ (Bellman equation); $u(c)$ (CRRA period utility); $U_0^H$ (Eq 3); $U_\text{ext}$ (normalized to 0)

Derivation chain verified: Euler equation (Eq 11) → substitute three consumption-growth scenarios → divide by $D_t^j$ → solve for $v^j = A^j/(1-A^j)$ → yields Prop 1 formulas. All steps use only defined objects and stated assumptions.

**No expression in the paper fails to trace back to the stated assumptions.**
