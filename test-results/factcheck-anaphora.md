# tests/factcheck-anaphora.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 3m 50s
[ralph-garage/agent-logs/20260412T201203.496956-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.496956-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their referenced targets.

## Findings by section

### Introduction (lines 38–70)
No errors. Four cross-references checked (`\ref{fig:ai-valuations}`, `\ref{prop:comp-statics}`, `\ref{sec:model}`/`\ref{sec:quant}`/`\ref{sec:extensions}`). The one nearby demonstrative ("such gains" near `\ref{fig:ai-valuations}`) correctly resolves to "transformative productivity gains" in the same clause, not to the figure.

### Model (lines 71–175)
No errors. Two demonstratives near cross-references checked:
- "this condition" near `Section~\ref{sec:ext2}` (line 148): resolves to the existence condition $A^j < 1$ from the surrounding remark; the `\ref` points forward to where the violation is discussed. Distinct roles, no conflict.
- "This discontinuity" two sentences after `Remark~\ref{rem:existence}` (line 171): resolves to the finite-to-infinite hedging demand phenomenon described in the intervening prose, which is precisely the content of the remark. Substantively correct.

### Quantitative Analysis (lines 176–193)
No errors. Three cross-references (`\ref{tab:pd-ratios}`, `\ref{prop:comp-statics}`, `\ref{fig:ai-valuations}`) all introduced with bare noun phrases ("Table~\ref{...}", "Proposition~\ref{...}", "Figure~\ref{...}"). No demonstratives adjacent to any cross-reference.

### Extensions (lines 194–278)
No errors. Four demonstratives near cross-references checked:
- "this distortion" near `Proposition~\ref{prop:veto}` (line 229): correctly resolves to the veto distortion from Proposition 3.
- "This connects" before `Proposition~\ref{prop:veto}` (line 229): resolves to the preceding extinction-risk observation, not to the proposition itself.
- "This approximation" after `\eqref{eq:phi-eff}` (line 253): resolves to the stated approximation of computing $\phi_\text{eff}$ at $\alpha_0$.
- "This ratio" after `\eqref{eq:transfer-ratio}` (line 261): resolves to the displayed equation immediately above.

### Conclusion (lines 279–289)
No cross-references appear in this section. No demonstrative-reference interactions to check.

### Proof of Proposition 1 (lines 290–321)
No errors. One demonstrative near a cross-reference: "This can be rewritten as equation~\eqref{eq:pd-ai}" correctly resolves "This" to the immediately preceding display equation \eqref{eq:pd-ai-solve}.
