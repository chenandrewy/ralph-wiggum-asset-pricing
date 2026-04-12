# tests/factcheck-anaphora.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 3m 15s
[ralph-garage/agent-logs/20260412T093252.145088-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.145088-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their referenced targets.

## Findings by section

### Introduction (lines 38–70)
No issues. Key checks:
- "such gains" near `\ref{fig:ai-valuations}`: resolves to "transformative productivity gains" in the same sentence, not to the figure. Correct.
- "this attenuation" near `Proposition~\ref{prop:comp-statics}`: resolves to the extinction-risk attenuation described in the preceding clause. The proposition states the valuation spread decreases in extinction probability. Match.
- "These results" near section roadmap refs (`\ref{sec:model}`, etc.): resolves to the three enumerated results in the same paragraph, not to the section labels. Correct.

### Model (lines 71–175)
No issues. Key checks:
- "this condition" near `Section~\ref{sec:ext2}` in Remark 1: resolves to the existence condition $A^j < 1$ just stated, not to the section. Correct.
- "This discontinuity" in Discussion (line 171): resolves to the finite-to-infinite price transition described in prior sentences. No adjacent cross-reference creates ambiguity.
- All references to `Proposition~\ref{prop:pd-ratios}` use definite descriptions ("The P/D ratios in," "The closed-form expressions in," "The key economic content of") that match the proposition's content.

### Quantitative Analysis and Extensions (lines 176–278)
No issues. Key checks:
- "This connects to debates about AI regulation: Proposition~\ref{prop:veto} implies..." (line 229): "This" resolves to the preceding extinction-risk interaction mechanism, not to the proposition. The proposition is cited as authority for the subsequent claim. Correct.
- "the existence condition in Remark~\ref{rem:existence}" (line 265): definite description matches the remark's content (condition $A^j < 1$ for finite P/D ratios). Correct.
- References to `\eqref{eq:phi-eff}` and `\eqref{eq:transfer-consumption}` use equation-name descriptions without demonstratives. No ambiguity.

### Conclusion and Appendix (lines 279–321)
No issues. Key check:
- "This can be rewritten as equation~\eqref{eq:pd-ai}" (line 320): "This" resolves to the expanded Euler equation just derived. The target is the solved P/D ratio formula. Standard algebraic rewriting claim; no mismatch.
