# tests/factcheck-anaphora.py
Started: 2026-04-04 23:59:28 EDT
Runtime: 4m 29s
[ralph-garage/agent-logs/20260404T235928.980499-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260404T235928.980499-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: No demonstrative near a cross-reference resolves to a meaning that conflicts with the referenced target.

## Findings by section

### Introduction (lines 41–74)
No anaphora resolution errors. The single internal cross-reference (`\ref{fig:opening}`) appears near "these valuations," which correctly resolves to the high market-cap levels the figure depicts.

### Model (lines 75–155)
No anaphora resolution errors. The section defines equation labels (`eq:utility`, `eq:output`, `eq:consumption-jump`, `eq:Lambda`, `eq:euler`, `def:equilibrium`) but does not back-reference them with demonstratives within this section.

### Results (lines 156–237)
No anaphora resolution errors. Cross-references (`\ref{app:proofs}`, `\ref{tab:pd}`) appear without accompanying demonstratives. Anaphoric prose (e.g., "The spread equals…") refers unambiguously to the immediately preceding formula.

### Extensions (lines 238–311)
No anaphora resolution errors. Cross-references (`\ref{fig:transfers}`, `\eqref{eq:Lambda-transfer}`, `\ref{prop:pd}`, `\eqref{eq:pd-extinction}`, `\ref{app:proofs}`) are each paired with neutral noun phrases ("Figure," "equation," "the P/D formula from") that match the target content.

### Conclusion (lines 312–328)
No cross-references appear in this section. No demonstrative + cross-reference pairs to evaluate.

### Proofs appendix (lines 329–368)
No anaphora resolution errors. "The Euler equation \eqref{eq:euler}" correctly identifies the Euler equation being applied. Proof headers (`Proposition~\ref{prop:pd}`, `Proposition~\ref{prop:veto}`) are standard and unambiguous.
