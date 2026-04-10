# tests/factcheck-freely.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 6m 38s
[ralph-garage/agent-logs/20260409T205235.719819-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T205235.719819-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The proof of Proposition 1 contains a self-contradictory stationarity claim, and Proposition 2(iii) lacks a rigorous proof for the ratio result.

## Detailed Findings

### Logical Inconsistency 1: Self-contradictory stationarity claim (Appendix A, line 289)

The proof of Proposition 1 states: "we focus on the pre-singularity valuation, treating the post-singularity P/D ratio as approximately $v^{AI}$ (this is exact when the economy is stationary conditional on the new share)."

This parenthetical exactness claim contradicts the model's own structure. After a non-extinction singularity, $\theta$ changes to $\theta + \Delta\theta(1-\theta)$, which changes $\Gamma^{AI}$ and $\Gamma^N$. A subsequent singularity from the new state would therefore have different dividend growth factors, so the post-singularity P/D ratio differs from the pre-singularity one. The economy is never truly stationary conditional on the new share (unless $\Delta\theta = 0$, which would eliminate the model's mechanism). The claim that the approximation is "exact" under a condition that never holds within the model is a logical inconsistency.

### Logical Inconsistency 2: Incomplete proof for Proposition 2(iii) ratio claim

Proposition 2(iii) states without qualification: "The *ratio* $(P^{AI}/D^{AI}) / (P^N/D^N)$ also decreases in $\xi$."

The proof argues by intuition that "higher $\xi$ uniformly shrinks the weight on non-extinction singularity states, which are the only states where AI and non-AI dividends diverge. Both the spread and the ratio narrow." However, the P/D ratio has the form $A/(1-A)$, which is convex in $A$. The ratio of two such convex functions is not guaranteed to be monotonic in $\xi$ for all parameter values. Unlike part (ii), which includes the qualifier "when $\gamma$ is sufficiently large," part (iii) is stated as holding universally. The proof does not establish this.

### Borderline Issue: "Surplus" terminology mismatch (Section 4.2, line 222)

The text says the government taxes "AI owners' surplus," but the formula (equation 5) taxes $(1-\phi\alpha)(1+\eta)(1+g)C_t$, which is AI owners' total post-singularity consumption, not their surplus (gain relative to pre-singularity level). This is a text-math mismatch, though "surplus" could be charitably interpreted as "their share of output."
