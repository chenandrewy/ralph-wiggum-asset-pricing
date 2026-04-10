# tests/factcheck-anaphora.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 5m 48s
[ralph-garage/agent-logs/20260409T202148.436207-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.436207-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to their intended targets.

## Findings by section

### Introduction (lines 39–73)
One marginal observation: on line 41, "such gains" appears in the same sentence as `Figure~\ref{fig:ai-valuations}`. The demonstrative "such" resolves to "transformative productivity gains" in the same clause, which is future-oriented, while the figure shows historical valuation data. However, "such" is not pointing at the figure — it refers to the noun phrase in the same clause — so this is not a true anaphora-reference mismatch.

### Model (lines 74–185)
No issues found. All demonstratives near `Proposition~\ref{prop:pd-ratios}`, `Remark~\ref{rem:existence}`, `Section~\ref{sec:ext2}`, and `Appendix~\ref{app:proof-pd}` resolve correctly.

### Quantitative Analysis (lines 186–203)
No issues found. References to `Table~\ref{tab:pd-ratios}`, `Proposition~\ref{prop:comp-statics}(iii)`, and `Figure~\ref{fig:ai-valuations}` all match their targets.

### Extensions (lines 204–273)
No issues found. References to `Proposition~\ref{prop:pd-ratios}`, `Remark~\ref{rem:existence}`, and `Figure~\ref{fig:extension-panels}` all resolve correctly.

### Conclusion (lines 274–284)
No issues found. No cross-references appear in this section.

### Proof of Proposition 1 (lines 285–314)
No issues found. References to `\eqref{eq:pd-ai}` and `\ref{prop:pd-ratios}` resolve correctly.
