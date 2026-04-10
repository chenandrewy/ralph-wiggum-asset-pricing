# tests/factcheck-anaphora.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 4m 20s
[ralph-garage/agent-logs/20260409T212047.322971-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.322971-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve unambiguously to meanings consistent with their targets.

## Findings by section

### Introduction (lines 38--72)
No errors. The one demonstrative near a cross-reference---"such gains" near `Figure~\ref{fig:ai-valuations}`---refers back to "transformative productivity gains," not to the figure. Resolution is unambiguous.

### Model (lines 73--176)
No errors. Key instance: "this condition" near `Section~\ref{sec:ext2}` correctly resolves to the $A^j < 1$ existence condition stated in the immediately preceding sentence; the `\ref` is a forward pointer to where the discussion continues, not the antecedent of "this."

### Quantitative Analysis (lines 177--194)
No errors. All three cross-references (`Table~\ref{tab:pd-ratios}`, `Proposition~\ref{prop:comp-statics}(iii)`, `Figure~\ref{fig:ai-valuations}`) are introduced with precise noun phrases rather than demonstratives.

### Extensions (lines 195--257)
No errors. Cross-references to `Proposition~\ref{prop:pd-ratios}`, `Remark~\ref{rem:existence}`, and `Figure~\ref{fig:extension-panels}` all use explicit noun phrases. Nearby demonstratives ("This ratio," "This discontinuity") resolve locally and unambiguously to immediately preceding content.

### Conclusion (lines 258--268)
No errors. No `\ref` or `\eqref` commands appear. Demonstratives ("this premium," "this mechanism") resolve to adjacent noun phrases without ambiguity.

### Proof of Proposition 1 (lines 269--298)
No errors. The one demonstrative near a cross-reference---"This can be rewritten as equation~\eqref{eq:pd-ai}"---correctly refers to the just-derived equation \eqref{eq:pd-ai-solve}.
