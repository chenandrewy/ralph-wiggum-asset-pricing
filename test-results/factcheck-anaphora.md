# tests/factcheck-anaphora.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 5m 42s
[ralph-garage/agent-logs/20260409T215056.135332-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.135332-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to meanings that match their referenced targets.

## Findings by section

### Introduction (lines 38–68)
No problems. The only cross-reference is `Figure~\ref{fig:ai-valuations}`; the nearby "such" in "the displacement such gains may bring" resolves to "transformative productivity gains" within the same sentence, not to the figure.

### Model (lines 69–174)
No problems. Key instances checked:
- "this condition" (line 142) near `Section~\ref{sec:ext2}` resolves to the $A^j < 1$ existence condition from `\eqref{eq:existence}`, not to the section reference. Unambiguous.
- "The closed-form expressions in Proposition~\ref{prop:pd-ratios}" uses a definite noun phrase, not a demonstrative.
- "This is the hedging channel" (line 147) has no adjacent cross-reference.

### Quantitative Analysis (lines 175–192)
No problems. Three cross-references (`\ref{tab:pd-ratios}`, `\ref{prop:comp-statics}(iii)`, `\ref{fig:ai-valuations}`) appear with no adjacent demonstratives.

### Extensions (lines 193–261)
No problems. Key instances checked:
- "This follows directly from dividing \eqref{eq:transfer-consumption}" (line 236): "This" resolves to the algebraic derivation of $\phi_\text{eff}$, consistent with the referenced equation.
- "This ratio" (line 244) near `\eqref{eq:transfer-ratio}`: resolves to the ratio just defined by that equation.
- "the existence condition in Remark~\ref{rem:existence}" (line 248): definite noun phrase, not a demonstrative.
- "This discontinuity" (line 248): no adjacent cross-reference.

### Conclusion (lines 262–272)
No problems. No cross-references appear in this section. Demonstratives ("this premium", "This mechanism") resolve to immediately preceding noun phrases.

### Proof of Proposition 1 (lines 273–302)
No problems. Key instances checked:
- "This approximation" (line 295): resolves to the approximation stated in the preceding sentence; no adjacent \ref.
- "This can be rewritten as equation~\eqref{eq:pd-ai}" (line 301): "This" resolves to the displayed equation \eqref{eq:pd-ai-solve} immediately above, which is indeed algebraically equivalent to \eqref{eq:pd-ai}.
