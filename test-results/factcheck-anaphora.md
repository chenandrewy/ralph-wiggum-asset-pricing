# tests/factcheck-anaphora.py
Started: 2026-04-04 23:45:08 EDT
Runtime: 4m 29s
[ralph-garage/agent-logs/20260404T234508.979897-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260404T234508.979897-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve unambiguously to meanings consistent with their targets.

## Findings by section

**Introduction (lines 41--74):** No issues. Demonstratives ("these magnitudes", "this logic", "this displacement") all resolve clearly to their intended antecedents. The single \ref (Figure~\ref{fig:opening}) has no nearby demonstrative.

**Model (lines 75--153):** No issues. Demonstratives ("This capital", "This is the displacement scenario", "This is the key friction", "such trade") are either not adjacent to cross-references or resolve unambiguously.

**Results (lines 154--235):** No issues. "This result" after Proposition 4 correctly refers to the preceding proposition. Table and proposition references (Proposition~\ref{prop:pd}, Table~\ref{tab:pd}) have no ambiguous demonstratives nearby.

**Extensions (lines 236--309):** No issues. "This result connects to Extension~1" correctly refers to Proposition 5. References to Proposition~\ref{prop:pd} and equation~\eqref{eq:Lambda-transfer} in figure notes have no nearby demonstratives. "equation~\eqref{eq:pd-extinction}" in the extinction proof is used without demonstrative ambiguity.

**Conclusion (lines 310--326):** No issues. "This paper" is a clear self-reference. No \ref or \eqref commands appear.

**Proofs (lines 327--364):** No issues. Cross-references to \eqref{eq:euler}, Proposition~\ref{prop:pd}, and Proposition~\ref{prop:veto} have no nearby demonstratives with ambiguous resolution.
