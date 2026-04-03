# tests/factcheck-anaphora.py
Started: 2026-04-02 22:13:44 EDT
Runtime: 1m 17s
[ralph-garage/agent-logs/20260402T221344.373516-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260402T221344.373516-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: FAIL
REASON: One demonstrative near a cross-reference resolves to a meaning not contained in the referenced target.

## Findings by section

### Introduction (lines 41–68)
No issues found.

### Model (lines 72–153)
No issues found.

### Results (lines 157–226)

**Line 202 — "this" + `\eqref{eq:comp-static}`**

> Condition~\eqref{eq:comp-static} requires that the singularity-state contribution to the AI stock's value, $\Phi^A(1 + V_1)$, exceeds the no-singularity price-dividend ratio. When **this** holds, adding singularity risk increases the AI stock's price **because the hedging benefit outweighs the direct effect of the regime change on discount rates**.

The demonstrative "this" points to Condition (13), which is the inequality $\Phi^A(1+V_1) > R/(1-R)$. The referenced equation is a threshold inequality only — it contains no decomposition into a "hedging benefit" component versus a "direct discount-rate effect" component. The two-force framing is introduced by the prose but is not grounded in the target equation, making the causal claim appear to follow from the referenced condition when the condition itself says nothing about competing forces.

### Extension (lines 230–267)
No issues found. No `\ref` or `\eqref` cross-references appear in this section.

### Conclusion (lines 271–276)
No issues found. No cross-references appear in this section.

### Proofs (lines 283–297)
No issues found.
