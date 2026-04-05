# tests/factcheck-anaphora.py
Started: 2026-04-04 23:25:45 EDT
Runtime: 4m 47s
[ralph-garage/agent-logs/20260404T232545.922375-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260404T232545.922375-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: No demonstrative near a cross-reference resolves to a meaning that conflicts with the referenced target.

## Findings by section

### Introduction (lines 41–62)
No `\ref` or `\eqref` cross-references appear in this section. All demonstratives refer to concepts introduced in surrounding prose. No issues.

### Model (lines 63–141)
No demonstrative appears adjacent to a `\ref` or `\eqref`. Demonstratives such as "This capital" (line 88) and "This is the key friction" (line 125) resolve to immediately preceding noun phrases, not to cross-referenced targets. No issues.

### Results (lines 142–223)
Cross-references include `\ref{app:proofs}`, `\ref{prop:pd}`, and `\eqref` uses in proofs. The one demonstrative near a formal result—"This result quantifies the role of market incompleteness" (line 199)—correctly resolves to Proposition 3 (incomplete markets amplify the premium), which is the immediately preceding proposition. No issues.

### Extensions (lines 224–297)
Cross-references include `\ref{prop:pd}`, `\eqref{eq:Lambda-transfer}`, `\ref{fig:transfers}`, `\ref{app:proofs}`, and `\eqref{eq:pd-extinction}`. No demonstrative appears adjacent to any of these. "This result connects to Extension 1" (line 270) correctly resolves to the preceding Proposition (veto and market completeness). No issues.

### Conclusion (lines 298–314)
No `\ref` or `\eqref` cross-references appear. Demonstratives ("This paper") refer to the paper itself. No issues.

### Proofs (lines 315–352)
Cross-references include `\ref{prop:pd}`, `\ref{prop:veto}`, and `\eqref{eq:euler}`. No demonstrative appears near any cross-reference. All references are introduced with definite articles or noun phrases ("The Euler equation", "Proof of Proposition"). No issues.
