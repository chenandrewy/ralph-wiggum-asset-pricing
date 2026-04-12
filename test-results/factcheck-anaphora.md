# tests/factcheck-anaphora.py
Started: 2026-04-12 14:18:19 EDT
Runtime: 4m 50s
[ralph-garage/agent-logs/20260412T141819.073930-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T141819.073930-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their referenced targets.

## Findings by section

### Introduction (lines 38–70)
No anaphora resolution errors. Demonstratives ("this premium," "these distortions," "these frictions," "these three linked results") all resolve to antecedents in the immediately preceding prose rather than to the cross-referenced targets, and where they appear near a `\ref` the prose description matches what the target contains (e.g., "narrowing the valuation spread" for Proposition 2, which states the spread is decreasing in extinction probability).

### Model (lines 71–175)
No anaphora resolution errors. Demonstratives near cross-references ("this condition" referring to Remark 1's existence condition $A^j < 1$; "this discontinuity" referring to the finite-to-infinite price transition near Remark 1) all resolve correctly to what the referenced targets contain.

### Quantitative Analysis (lines 176–193)
No anaphora resolution errors. No demonstratives appear adjacent to any cross-reference in this section.

### Extensions (lines 194–278)
No anaphora resolution errors. Key checks: "Proposition~\ref{prop:veto} implies that calls to slow or halt AI development may partly reflect unhedgeable downside risk" correctly characterizes Proposition 3's veto result; "the existence condition in Remark~\ref{rem:existence} is violated" correctly describes the $A^j < 1$ condition; equation references (\eqref{eq:transfer-consumption}, \eqref{eq:phi-eff}, \eqref{eq:transfer-ratio}) are all described accurately in surrounding prose.

### Conclusion (lines 279–289)
No anaphora resolution errors. No demonstratives appear near cross-references.

### Proof of Proposition 1 (lines 290–321)
No anaphora resolution errors. "This can be rewritten as equation~\eqref{eq:pd-ai}" correctly refers to the immediately preceding derived expression, and the target equation is indeed the same formula.
