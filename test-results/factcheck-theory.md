# tests/factcheck-theory.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 3m 2s
[ralph-garage/agent-logs/20260402T184535.059909-0400_factcheck-theory_claude_opus.log](../ralph-garage/agent-logs/20260402T184535.059909-0400_factcheck-theory_claude_opus.log)

# factcheck-theory
VERDICT: FAIL
REASON: Two notational ambiguities — an unstated regime-vs-time subscript convention on V, and a variable collision between A(p) and the AI-stock superscript A in the same expression.

## Requirement 1: Notational Consistency — FAIL

### Issue 1 (Medium): V subscripts overload time vs. regime

Throughout the paper, subscripts denote time ($Y_t$, $c_t$, $D_t^A$, $P_t^i$, $n_t^A$, etc.). However, in Proposition 1 and onward, subscripts 0 and 1 on $V$ denote **regimes** (pre-singularity = 0, post-singularity = 1), not time periods. This convention is never explicitly stated. A reader encountering $V_0^A$ will naturally parse the subscript 0 as "at time $t=0$" rather than "in regime 0." The paper introduces $V_0^A$ as "the price-dividend ratio of public AI stocks in the pre-singularity regime" in prose, but the subscript convention itself is left implicit.

This is an ambiguity, not merely a style preference: the subscript 0 on $V$ has a different semantic role than the subscript 0 on $E_0$ (which denotes time-0 conditioning).

**Fix:** Add an explicit statement when $V_0^A$ is first introduced, e.g., "where subscripts 0 and 1 on $V$ denote the pre- and post-singularity regimes, respectively."

### Issue 2 (Medium): A(p) collides with AI-stock superscript A

In the proof of Proposition 3 (Appendix A), the paper writes:

> $V_0^A = A(p)/B(p)$ where $A(p) = (1-p)R + p\Phi^A(1+V_1)$

The letter $A$ appears in two unrelated roles in the same expression: as a superscript on $V_0^A$ (denoting "AI stocks") and as a standalone function $A(p)$ (denoting the numerator). This is a genuine variable collision.

**Fix:** Rename the proof auxiliaries to avoid collision, e.g., $f(p)/h(p)$ or $\mathcal{N}(p)/\mathcal{D}(p)$.

### Issue 3 (Minor): Orphaned symbol $\Delta_0$

Section 4.2 introduces $\Delta_0 = \tilde{\omega}/\omega$ as the no-transfer displacement ratio, which is semantically identical to $\Delta$ defined in Eq. (5). The symbol $\Delta_0$ is used exactly once and never appears in any equation. The paper then reverts to $\Delta$ without formalizing how transfers modify $\Delta$.

### Issue 4 (Minor): $R$ for pricing kernel vs. conventional return notation

$R$ is conventionally used in finance for gross returns. Here it denotes $\beta(1+g)^{1-\gamma}$, a pricing-kernel component. The symbol is explicitly defined, so this is not an error, but it inverts the standard semantic association.

### Issue 5 (Minor): Dual role of $q$

The letter $q$ appears as both a probability parameter ($q \in [0,1)$) and a superscript label on $V_0^{A,q}$. The connection is natural but the superscript is functioning as a label ("the version with extinction risk"), not as the probability itself.

## Requirements 2–3: Not evaluated

Per the test procedure, Requirements 2 and 3 are not evaluated because Requirement 1 failed. Notational consistency must be established before assumption consistency and traceability can be meaningfully assessed.
