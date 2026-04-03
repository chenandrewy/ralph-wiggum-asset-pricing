# tests/factcheck-theory.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 4m 12s
[ralph-garage/agent-logs/20260402T221344.384242-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.384242-0400_factcheck-theory_claude_opus.log)

# factcheck-theory

VERDICT: FAIL
REASON: Numeric subscripts 0 and 1 are overloaded to mean both "time" and "regime" on different symbols, creating a notational ambiguity.

## Requirement 1: Notational Consistency — FAIL

### Issue: Subscript overload (time vs. regime)

The paper uses numeric subscripts for two distinct semantic roles:

- **Time indexing:** $E_0$ (Eq. 6) is the time-0 conditional expectation. $E_t$ (Eq. 8, 9) is the time-$t$ expectation. Throughout the paper, subscripts on $Y_t$, $D_t^A$, $c_t$, $P_t^A$, $n_t^A$ denote time.
- **Regime indexing:** $V_0^A$ (Eq. 5) is the *pre-singularity* price-dividend ratio. $V_1$ (Eq. 8) is the *post-singularity* price-dividend ratio. Here 0 and 1 are regime labels, not time periods.

The paper discloses this in Proposition 1: "where subscripts 0 and 1 on $V$ denote pre- and post-singularity regimes, not time." However, acknowledging the problem does not resolve it. In the same paper, subscript 0 on $E_0$ means time zero, while subscript 0 on $V_0^A$ means the pre-singularity regime. This is a genuine overload of the same numeral across symbol families.

**Fix:** Use regime labels such as $V_{\text{pre}}^A$, $V_{\text{post}}$ or drop the time subscript from the expectation operator (write $E[\cdot]$ instead of $E_0[\cdot]$).

### Other notation: clean

The remaining notation is well-organized:

- **Tilde convention** ($\tilde{g}$, $\tilde{\theta}$, $\tilde{\nu}$, $\tilde{\omega}$) consistently denotes post-singularity counterparts throughout.
- **Superscript convention** ($A$, $N$, $P$, $\mathrm{CM}$, $q$) is stable across all asset-related variables.
- **All 17 symbol families** are individually consistent, with explicit definitions and no reuse for unrelated quantities (beyond the subscript overload above).
- $R \equiv \beta(1+g)^{1-\gamma}$ clashes with the standard finance convention of $R$ for gross return, but is defined explicitly and used consistently within the paper. This is an external convention issue, not an internal collision.

## Requirements 2 and 3: Not evaluated

Per procedure, evaluation stops at the first failing requirement.
