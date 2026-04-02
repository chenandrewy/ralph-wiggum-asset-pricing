# tests/factcheck-theory.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 8m 31s
[ralph-garage/agent-logs/20260402T183430.359632-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T183430.359632-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS

REASON: All notation is resolvable from context, all assumptions are mutually consistent, and all mathematical objects trace back to primitives.

---

## Requirement 1: Notational Consistency — PASS (with issues)

The paper's notation is largely clean and internally consistent. The tilde convention (post-singularity values), asset-class superscripts ($A$, $N$, $P$), and CRRA parameters ($\beta$, $\gamma$) are stable throughout. Five substantive issues were identified, none critical:

### Issue 1 (Moderate): $\Delta$ constant vs. function collision

$\Delta \equiv \tilde{\omega}/\omega$ is defined as a constant in Eq. (5) and used throughout Sections 2–3. In Section 4.2, $\Delta(\lambda)$ is introduced as a function, with $\Delta_0 = \tilde{\omega}/\omega$ as the no-transfer case. The paper states "with the earlier definition corresponding to the case of no transfers" and "At $\lambda = 0$, $\Delta = \Delta_0$," which resolves the equivalence informally. However, the formal identity $\Delta \equiv \Delta(0) = \Delta_0$ is never written as an equation.

**Assessment:** The text provides sufficient context to resolve the ambiguity. A reader following the paper sequentially can infer $\Delta = \Delta_0 = \Delta(0)$. Not a true collision, but an explicit equivalence statement would strengthen clarity.

### Issue 2 (Low-to-moderate): Regime vs. time subscripts on $V$

Subscripts 0 and 1 on $V$ denote regimes (pre/post-singularity), while numeric subscripts on $Y_t$, $c_t$, $D_t$ denote time. The convention is never formally declared. However, the paper explicitly defines $V_1$ as "the common post-singularity price-dividend ratio" (line 172), and no symbol carries both time and regime subscripts simultaneously.

**Assessment:** Resolvable from definitions in context. The dual use of numeric subscripts is a notational fragility, not a true ambiguity.

### Issue 3 (Low): $V_0^{A,q}$ vs. $V_0^{A,\mathrm{CM}}$ superscript style

$q$ is a variable name used as a superscript label, while $\mathrm{CM}$ is a descriptive label. Inconsistent decoration style.

### Issue 4 (Low-to-moderate): $R$ convention

$R = \beta(1+g)^{1-\gamma}$ is an SDF-weighted growth factor less than 1, but $R$ conventionally denotes a gross return in finance. Potential clash with reader expectations, though the paper defines $R$ explicitly.

### Issue 5 (Low-to-moderate): $A(p)$ in appendix proof

$A(p)$ is used as an auxiliary function in the proof of Proposition 3, colliding visually with the superscript $A$ for AI stocks in the same equations (e.g., $V_0^A = A(p)/B(p)$). The meaning is locally clear, but a different letter would avoid the visual collision.

---

## Requirement 2: Assumption Consistency — PASS

All formal assumptions (A1–A3) and implicit assumptions are mutually consistent. The parameter space satisfying all constraints is non-empty, confirmed by the numerical example ($\beta=0.96$, $\gamma=3$, $g=0.02$, $\tilde{g}=0.05$, $\theta=0.05$, $\tilde{\theta}=0.15$, $\nu=0.55$, $\tilde{\nu}=0.30$, $p=0.01$).

### Formal assumptions compatibility

- **A1 + A2:** A2 says $\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$. A1 requires $\tilde{\theta}+\tilde{\nu} < \theta+\nu$, meaning the non-AI loss dominates the AI gain. These are compatible; the joint parameter space is non-empty.
- **A3 given A1–A2:** With $\gamma > 1$ and positive growth rates, A3 is automatically satisfied ($R < \beta < 1$).
- **Extensions (Section 4):** Extinction probability $q \in [0,1)$ and transfer fraction $\lambda \in [0,1]$ introduce no conflicts with the base model. At $q=0$ and $\lambda=0$, the extension formulas reduce to the base model.

### Algebraic verification

- Post-singularity P/D ratio $V_1$ is correctly common to all assets (both satisfy the same Euler equation).
- Hedging premium (Eq. 16) is strictly positive under the maintained assumptions (all factors verified positive).
- Proposition 3 proof verified algebraically correct.
- Transition-period consumption growth $\Delta(1+\tilde{g})$ is consistent with share and growth definitions.

### Minor imprecisions (not inconsistencies)

1. The claim that Assumption 3 is "automatically satisfied for $\gamma > 1$" implicitly requires $g \geq 0$. For very negative $g$ with high $\gamma$, the condition can fail. The paper intends positive growth rates but does not state $g \geq 0$ as a maintained assumption.
2. Output shares $\theta, \nu, \tilde{\theta}, \tilde{\nu} \in (0,1)$ with $\theta+\nu < 1$ and $\tilde{\theta}+\tilde{\nu} < 1$ are implicitly required but never stated as a formal assumption.

---

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to the primitive assumptions and definitions.

### Primitive parameters (from assumptions)

$\theta, \tilde{\theta}, \nu, \tilde{\nu}, p, g, \tilde{g}, \gamma, \beta, q, \lambda, F, \tau, Y_t$

### Derived objects and their traceability

| Object | Defined from |
|--------|-------------|
| $\omega, \tilde{\omega}$ | $\theta+\nu$, $\tilde{\theta}+\tilde{\nu}$ (Eq. 5) |
| $\Delta$ | $\tilde{\omega}/\omega$ (Eq. 5) |
| $R$ | $\beta(1+g)^{1-\gamma}$ (Eq. 7) |
| $D_t^A, D_t^N, D_t^P$ | Output shares $\times$ $Y_t$ (Eqs. 3–4) |
| $c_t$ | Market clearing: $\omega Y_t$ or $\tilde{\omega}Y_t$ (Eq. 6) |
| $\Phi^A, \Phi^N$ | $\beta, \gamma, \Delta, \tilde{g}, \tilde{\theta}/\theta, \tilde{\nu}/\nu$ (Eqs. 8–9) |
| $V_1$ | $\beta, \tilde{g}, \gamma$ (Eq. 10) |
| $V_0^A, V_0^N$ | $R, \Phi^{A/N}, V_1, p$ (Eqs. 8–9) |
| $\Phi^{A,\mathrm{CM}}, V_0^{A,\mathrm{CM}}$ | Same as $\Phi^A, V_0^A$ with $\Delta=1$ (Eqs. 15–16) |
| $V_0^{A,q}$ | Base formula + $q$ (Eq. 14) |
| $\Delta(\lambda), \Delta_0$ | $\Delta, \lambda$ (Eq. 17) |
| $T$ | $(\omega-\tilde{\omega})Y$ (Eq. 18) |
| $A(p), B(p)$ | Auxiliary: $R, \Phi^A, V_1$ (Appendix proof) |

No expressions were found that cannot be logically derived from the assumptions and definitions.
