# tests/factcheck-theory.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 7m 31s
[ralph-garage/agent-logs/20260402T214942.823272-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.823272-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: PASS
REASON: All notation is consistent, all assumptions are mutually compatible, and all mathematical objects trace back to assumptions.

---

## Requirement 1: Notational Consistency — PASS

Every mathematical symbol was cataloged across 16 symbol families. The paper maintains a clean notational system with:

- **Tilde convention** (post-singularity values: $\tilde{g}$, $\tilde{\theta}$, $\tilde{\nu}$, $\tilde{\omega}$) applied uniformly.
- **Superscript convention** (asset type $A/N/P/i$, model variant $\mathrm{CM}/q$) applied uniformly.
- **Regime subscript on $V$** ($0$ = pre-singularity, $1$ = post-singularity) explicitly declared and consistently applied.

No symbol serves double duty for genuinely different formal objects. No formal object is denoted by two unrelated symbols.

**Minor observations (none rising to true inconsistency):**

1. $\Delta$ used for a ratio rather than a difference — unconventional but explicitly defined (Eq. 5).
2. $R$ used for a pricing kernel, not a return — unconventional in finance but explicitly defined (Eq. 11).
3. Letter $P$ appears as both the base symbol for price ($P_t^i$) and the superscript for "private" ($D_t^P$) — context disambiguates.
4. $V_1$ lacks an asset superscript; justified because the PD ratio is common post-singularity, but could be stated more explicitly.
5. Visual similarity between $n$ (holdings) and $\nu$ (non-AI share) — negligible.

Full notation audit: `ralph-garage/scratch/factcheck-notation.md`.

---

## Requirement 2: Assumption Consistency — PASS

### Formal assumptions

| ID | Statement |
|----|-----------|
| A1 (Negative singularity) | $\tilde{\theta} + \tilde{\nu} < \theta + \nu$ |
| A2 (AI share growth) | $\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$ |
| A3 (Existence) | $(1-p)\beta(1+g)^{1-\gamma} < 1$ and $\beta(1+\tilde{g})^{1-\gamma} < 1$ |

### Findings

- **No contradictory inequalities.** A1 and A2 are compatible: A2 requires AI share to increase and non-AI share to decrease; A1 requires the net effect to be negative for the household. The numerical parameterization ($\theta=0.05, \tilde{\theta}=0.15, \nu=0.55, \tilde{\nu}=0.30$) confirms feasibility.
- **A3 is both necessary and sufficient** for finite, positive price-dividend ratios. The claim "automatically satisfied for $\gamma > 1$" is correct (under the implicit and economically natural assumption $g \geq 0$).
- **No conflicts between Section 4 and baseline.** The extinction-risk extension ($q$) and friction-cost parameters ($F, \tau$) nest the baseline as special cases ($q=0$, $F=0$).
- **Output shares sum to 1** by construction in both regimes.
- **Market clearing is consistent** with the budget constraint and consumption expression.

**Minor observations:**

1. Positivity of output shares ($\theta, \nu, \tilde{\theta}, \tilde{\nu} > 0$) and existence of positive private AI share ($\theta + \nu < 1$) are implicit but never formally stated. Standard and obvious from context.
2. The "automatically satisfied for $\gamma > 1$" claim implicitly assumes $g \geq 0$, which is economically natural.

Full assumptions audit: `ralph-garage/scratch/factcheck-assumptions.md`.

---

## Requirement 3: Traceability — PASS

All mathematical objects in the paper trace back to the primitive parameters constrained by the assumptions.

| Object | Derived From |
|--------|-------------|
| $Y_t$ | Primitive; growth via $g$ (pre) and $\tilde{g}$ (post) |
| $D_t^A, D_t^N, D_t^P$ | $\theta, \nu, Y_t$ (Eqs. 3–4) |
| $\omega, \tilde{\omega}, \Delta$ | $\theta, \nu, \tilde{\theta}, \tilde{\nu}$ (definitions) |
| $c_t$ | $\omega Y_t$ from market clearing and dividend structure |
| $R$ | $\beta, g, \gamma$ (Eq. 11) |
| $\Phi^A, \Phi^N$ | $\beta, \Delta, \tilde{g}, \gamma, \tilde{\theta}/\theta, \tilde{\nu}/\nu$ (Eqs. 12–13) |
| $V_1$ | $\beta, \tilde{g}, \gamma$ (Eq. 14) |
| $V_0^A, V_0^N$ | $R, \Phi^{A/N}, V_1, p$ (Prop. 1) |
| $V_0^A - V_0^N$ | Subtraction of PD ratios (Prop. 2) |
| $\partial V_0^A / \partial p$ | Derivative of Prop. 1 formula (Prop. 3) |
| $V_0^{A,\mathrm{CM}}, \Phi^{A,\mathrm{CM}}$ | Same primitives with $\Delta^{-\gamma} \to 1$ (Prop. 4) |
| $V_0^{A,q}$ | Adds $q$ to baseline (Sec. 4.1) |
| $F, \tau, T$ | Extension primitives for friction-cost analysis (Sec. 4.2) |
| $\mathcal{N}(p), \mathcal{D}(p)$ | Proof auxiliaries from $V_0^A$ (Appendix) |

**No expression fails to trace back to the assumptions.** Every derived quantity follows from the primitives $(\beta, \gamma, g, \tilde{g}, p, \theta, \tilde{\theta}, \nu, \tilde{\nu})$ plus the extension parameters $(q, F, \tau)$.
