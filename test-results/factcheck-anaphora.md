# tests/factcheck-anaphora.py
Started: 2026-04-11 15:21:59 EDT
Runtime: 2m 20s
[ralph-garage/agent-logs/20260411T152159.664472-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T152159.664472-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their targets.

## Findings by section

### Introduction (lines 38–72)
No anaphora resolution issues. The one demonstrative near a cross-reference — "As Proposition~\ref{prop:veto} shows" (line 55) — correctly attributes the veto-under-incomplete-markets result to Proposition 3, whose content matches. The prose says "investors' inability to hedge the downside of displacement," which aligns with the proposition's formal mechanism (unhedgeable downside drives the veto).

### Model (lines 73–177)
No anaphora resolution issues. Five demonstrative-plus-cross-reference constructions were checked:
- "this condition" near \ref{sec:ext2} (line 150): resolves to the existence condition $A^j < 1$, consistent with \eqref{eq:existence}.
- "This is exact" near \ref{prop:pd-ratios} (line 153): resolves to the stationarity approximation used in deriving Proposition 1.
- "this common multiplicative scaling" near \eqref{eq:existence} (line 164): resolves to the $(1-\xi)$ factor just described.
- "This condition is satisfied" near \ref{tab:pd-ratios} (line 164): resolves to $A^j > 1/2$, verifiable from the table.
- "This discontinuity" near \ref{rem:existence} (line 173): resolves to the finite-to-infinite hedging demand transition described in Remark 1.

### Quantitative Analysis (lines 178–195)
No anaphora resolution issues. Two cross-references checked:
- "as Proposition~\ref{prop:comp-statics} predicts" (line 189): prose says extinction risk compresses the AI premium; Proposition 2 says the valuation spread is decreasing in $\xi$. Match.
- "As Figure~\ref{fig:ai-valuations} shows" (line 191): prose describes S&P 500 P/D and NASDAQ relative performance; figure contains exactly those two panels. Match.

### Extensions (lines 196–280)
No anaphora resolution issues. Cross-references to \ref{prop:pd-ratios}, \ref{rem:existence}, and \ref{prop:veto} all resolve consistently with their targets. "This follows directly from dividing \eqref{eq:transfer-consumption}" (line 255) correctly refers to the factoring step deriving $\phi_\text{eff}$. Line 231's "Proposition~\ref{prop:veto} implies that calls to slow or halt AI development may partly reflect unhedgeable downside risk from displacement" correctly matches the proposition's formal content about downside-driven veto.

### Conclusion (lines 281–291)
No cross-references appear in this section. No anaphora resolution issues possible.

### Proof of Proposition 1 (lines 292–323)
No anaphora resolution issues. "This can be rewritten as equation~\eqref{eq:pd-ai}" (line 322) correctly refers to the just-derived $v^{AI}$ expression, which is algebraically identical to equation (3).
