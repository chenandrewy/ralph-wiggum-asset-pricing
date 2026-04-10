# tests/factcheck-theory.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 7m 13s
[ralph-garage/agent-logs/20260409T213452.272417-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.272417-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects trace back to stated assumptions.

## Requirement 1: Notational Consistency — PASS

No symbol collisions or reuse of symbols for different formal objects. Twenty-three symbol families were identified; none collide across families.

**Minor observations** (standard conventions, not ambiguities):
- $\alpha_t$ (state variable in Section 2) appears as unsubscripted $\alpha$ in Extension 2 and P/D formulas. This is standard stationary-equilibrium notation; the paper explicitly states "stationary equilibrium" (Proposition 1, Appendix A), which licenses dropping time subscripts.
- $\theta_t$ follows the same pattern. Same convention applies.
- $u$ (period utility) is used once informally in the proof of Proposition 3 ("$u$ is concave") without a displayed definition. The meaning is unambiguous from context ($u(c) = c^{1-\gamma}/(1-\gamma)$ per eq. 3).
- $U_\text{ext} = 0$ is stated in prose but not in a displayed equation. This is adequate for a normalization.
- Uppercase $C$ vs. lowercase $c^H$ for aggregate vs. household consumption is explicitly defined and maintained throughout.

## Requirement 2: Assumption Consistency — PASS

Twenty-seven assumptions were identified across the baseline model, two extensions, calibrations, and proofs. All are mutually consistent.

**Key consistency checks performed:**
1. **Parameter domains**: All constraints ($\phi \in (0,1)$, $\gamma > 1$, $\beta \in (0,1)$, $\Delta\theta \in (0,1)$, etc.) are compatible with each other and with stated calibration values.
2. **Probability structure**: Singularity probabilities sum to 1: $(1-p) + p(1-\xi) + p\xi = 1$.
3. **Baseline vs. Extension 1**: Positive singularity ($\alpha_{t+1} = \min(1, \alpha_t/\phi)$) is a consistent augmentation of the baseline singularity structure.
4. **Baseline vs. Extension 2**: Transfer mechanism modifies only the post-singularity consumption allocation; P/D formula reuse with $\phi_\text{eff}$ is algebraically valid.
5. **Existence condition violation**: The large-singularity calibration ($\eta = 9$, $\phi = 0.05$) deliberately violates $A^j < 1$ at $\tau = 0$; the paper states this explicitly and uses it as an economic feature.
6. **Proof assumptions**: All proofs derive from stated model assumptions. The stationarity approximation (A13) is explicitly acknowledged and its accuracy discussed.
7. **Numerical claims verified**: $\phi(1+\eta) = 0.75$ ✓; $\phi^{-\gamma} = 160{,}000$ ✓; transfer ratio independent of $\eta$ ✓.

**Minor observations** (not inconsistencies):
- The "25% consumption fall" and "consumption halves" claims refer to share displacement ($\phi(1+\eta)$) and omit the $(1+g)$ trend growth factor. This is approximately correct for $g = 0.02$ and refers to displacement-driven change.
- The implicit constraint $\delta\tau < 1$ (for positive net transfers) is satisfied for all parameterizations but not explicitly stated.
- Extension 1 leaves positive/negative singularity probabilities unspecified, appropriate for the qualitative nature of Proposition 3.

## Requirement 3: Traceability of Mathematical Objects — PASS

All derived mathematical objects trace back to stated assumptions:

| Derived Object | Source Assumptions |
|---|---|
| $\Gamma^{AI}$, $\Gamma^{N}$ (dividend growth factors) | A6, A9, A10 |
| $A^j$ (existence condition) | A2, A4–A7, A9, A12 |
| P/D ratios (Proposition 1) | A2, A4–A12 via Euler equation |
| Comparative statics (Proposition 2) | Consequences of P/D formulas |
| Veto result (Proposition 3) | A12, A15–A18 |
| $c^H_{post}$ (post-transfer consumption) | A3, A6, A7, A19, A20 |
| $\phi_\text{eff}$ (effective displacement) | A3, A7, A19, A20 |
| Transfer ratio (eq. 7) | A21 (algebraic rearrangement) |
| Euler equation (eq. 10) | A12 (CRRA first-order condition) |

No expression in the paper fails to trace back to stated assumptions.
