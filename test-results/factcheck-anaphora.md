# tests/factcheck-anaphora.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 1h 8m 31s
[ralph-garage/agent-logs/20260402T225431.388885-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260402T225431.388885-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: FAIL
REASON: Two anaphora resolution issues found where demonstratives near cross-references do not precisely match the referenced target's content.

## Findings

### Issue 1: Line 113 (Model section)

**Text:** `Assumption~\ref{as:neg-sing} states that $\Delta < 1$`

**Problem:** The prose claims Assumption 1 "states that $\Delta < 1$," but Assumption 1 (lines 101–103) actually states the inequality $\tilde{\theta} + \tilde{\nu} < \theta + \nu$. The notation $\Delta < 1$ is a consequence derived via the definition of $\Delta$ in eq:delta (lines 109–112), not what the assumption itself states. The demonstrative claim about what the assumption "states" resolves to a different formal expression than the one the target contains.

### Issue 2: Line 244 (Extension section)

**Text:** `This observation complements \citet{Jones2024}: just as the curvature of utility determines whether infinite AI-driven consumption justifies existential risk, it determines whether extreme AI growth sustains or eliminates the hedging premium.`

**Problem:** "This observation" refers back to Remark 1 (rem:extreme, lines 240–242), which specifically shows that for $\gamma > 1$ the hedging premium *vanishes* as $\tilde{g} \to \infty$. However, the sentence following the demonstrative discusses conditions under which extreme growth "sustains or eliminates" the premium—a broader claim than what Remark 1 actually contains. Remark 1 addresses only the case where the premium is eliminated, not conditions under which it is sustained.

## Sections with no issues

- **Introduction (lines 41–67):** No anaphora issues. "This pattern" near `\ref{fig:ai-valuations}` correctly resolves to the price-dividend ratio comparison described in the figure.
- **Results (lines 153–225):** No anaphora issues. All demonstratives near cross-references ("such a hedge," "this condition" near `\eqref{eq:comp-static}`, Assumption/Proposition references) resolve correctly.
- **Conclusion (lines 267–278):** No cross-references present; no anaphora issues possible.
- **Proofs (lines 279–295):** No anaphora issues. "This" on line 292 correctly refers to the numerator expression; `\eqref{eq:comp-static}` correctly resolves.
