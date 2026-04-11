# tests/factcheck-theory.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 7m 44s
[ralph-garage/agent-logs/20260411T103039.133283-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.133283-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually consistent, and all mathematical objects are traceable to the assumptions.

## Requirement 1: Notational Consistency — PASS

Full audit in `ralph-garage/scratch/factcheck-notation.md`.

17 symbol families identified. No collisions (same symbol for different objects), no unexplained aliases, and no orphan symbols. Superscript/subscript conventions are stable throughout:
- Asset type ($AI$, $N$, $j$) as superscripts
- Time ($t$, $t+1$) as subscripts
- Descriptive labels ($\text{veto}$, $\text{eff}$, $\text{post}$) in text font

One deliberate alias: $v^{AI}$ for $P^{AI}/D^{AI}$ in the Appendix, explicitly defined at introduction.

Minor informality: "$D^{AI} + D^N = C_t$" drops time subscripts on the LHS but retains them on the RHS. Unambiguous in context.

## Requirement 2: Assumption Consistency — PASS

Full audit in `ralph-garage/scratch/factcheck-assumptions.md`.

28 assumptions identified across the baseline model (A1–A17), the veto extension (A18–A24), and the transfers extension (A25–A28). No contradictions found between any pair.

Key verifications:
- **CRRA + extinction normalization (A12 + A21):** $\gamma > 1$ gives negative utility, so $U_\text{ext} = 0$ makes extinction "better" than living. Paper explicitly acknowledges this makes the veto result conservative. Consistent.
- **$\alpha^+ = \min(1, \alpha/\phi)$ (A18 + A6 + A4):** The min-cap correctly handles $\alpha/\phi > 1$. Consistent.
- **Complete markets consumption (A22):** Correctly derived from $\phi_\text{eff} \to 1$, giving $\alpha(1+\eta)(1+g)C_t$. Consistent.
- **$\phi_\text{eff}$ algebra (A28):** Verified by factoring Eq. 11. Correct.
- **Transfer ratio (Eq. 13):** $(1+\eta)(1+g)C_t$ cancels, yielding an $\eta$-independent ratio. Correct.
- **Existence condition (A16):** Baseline calibration gives $A^{AI} \approx 0.94 < 1$. Satisfied.
- **Veto limit $\gamma \to \infty$ (A12 + A23):** When $\phi(1+\eta) < 1$, the negative-singularity CRRA term dominates. Mathematically correct.

Two implicit conditions noted (not errors):
1. $\phi(1+\eta) < 1$ is used in the veto proof and discussion but stated as a condition rather than a formal assumption. Baseline calibration satisfies it ($0.5 \times 1.5 = 0.75$).
2. $\delta\tau < 1$ is needed for positive net transfers but not explicitly stated. All calibrations satisfy it.

## Requirement 3: Traceability — PASS

All derived mathematical objects traced back to assumptions:

| Derived Object | Traced to Assumptions |
|---|---|
| $\Gamma^{AI}$, $\Gamma^N$ (dividend growth factors) | A7 ($\eta$), A10 ($\theta$ dynamics) |
| $A^j$ (existence auxiliary, Eq. 8) | A3, A5, A6, A7, A8, A13, plus $\Gamma^j$ |
| $P^{AI}/D^{AI}$, $P^N/D^N$ (Prop. 1, Eqs. 3–4) | A2 (marginal investor), A3, A5, A6, A7, A8, A9, A12, A13, A14, A15 via Euler equation |
| Comparative statics (Prop. 2) | Derivatives of P/D formulas w.r.t. $\phi$, $p$, $\xi$ |
| $\Delta u(\gamma)$ (Eq. 9) | A6, A7, A12, A18 |
| $\bar{\gamma}$ (veto threshold, Prop. 3) | Existence from limit argument using A12, A23 |
| $V_\text{veto}$, $V_\text{develop}$, $V_\text{develop}^{CM}$ | A5, A12, A13, A20, A21, A22 |
| $c^H_{post}$ (Eq. 11) | A3, A6, A7, A25, A26 |
| $\phi_\text{eff}$ (Eq. 12) | Factoring Eq. 11 |
| Transfer ratio (Eq. 13) | Eqs. 11 / no-transfer baseline |
| $v^{AI}$ (Appendix) | Alias for $P^{AI}/D^{AI}$ |

**Euler equation derivation verified:** The appendix correctly expands the three states (no singularity, non-extinction singularity, extinction), substitutes consumption growth and dividend growth, divides by $D_t^{AI}$, and solves $v = B/(1-B)$ where $B$ is the SDF-weighted expected growth term. The algebra reproduces Eq. 3 exactly.

**No underived expressions found.** Every equation in the paper can be logically derived from the stated assumptions and standard asset pricing theory (Euler equation).

## Minor Notes (not failures)

1. **Prop. 2(iii) proof language:** The proof says the ratio "$A^{AI}/(1-A^{AI})$ falls proportionally more" due to convexity, but the ratio claim is qualified to "the parameterizations considered." The level-spread claim follows from convexity; the ratio claim is empirical. Acceptable as stated.
2. **Stationarity approximation (A17):** Explicitly acknowledged as approximate (exact when $\Delta\theta \to 0$). Numerically exact values provided via backward recursion. Transparently handled.
