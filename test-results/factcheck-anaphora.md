# tests/factcheck-anaphora.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 1m 33s
[ralph-garage/agent-logs/20260411T103039.129812-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.129812-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve unambiguously to meanings consistent with their referenced targets.

## Findings by Section

### Introduction (lines 38–72)
No issues. Demonstratives ("this market incompleteness," "this mechanism," "this distortion") resolve to clear antecedents. Cross-references to Figure 1, Proposition 2, and section roadmap labels all match their targets.

### Model (lines 73–184)
No issues. Key checks:
- "this condition" (line 150) near `\ref{sec:ext2}` resolves to $A^j \geq 1$ from `\eqref{eq:existence}`, not to the section reference. Correct.
- "This discontinuity" (line 180) near `Remark~\ref{rem:existence}` resolves to the finite-to-infinite hedging demand transition described in the preceding sentences. Correct.
- All `\ref` and `\eqref` targets (Proposition 1, Remark 1, Table 1, Appendix A) contain what the prose claims.

### Quantitative Analysis (lines 185–202)
No issues. "This comparison" (line 198) resolves to the NASDAQ-vs-S&P comparison in the preceding sentence, not to Figure 1 itself. Cross-references to Proposition 2(iii) and Figure 1 match their targets.

### Extensions (lines 203–287)
No issues. Key checks:
- "This follows directly" and "This ratio exceeds one" resolve to immediately preceding equations.
- `Proposition~\ref{prop:pd-ratios}` (line 262) correctly describes substituting $\phi_\text{eff}$ for $\phi$; the formula does contain $\phi^{-\gamma}$.
- `Remark~\ref{rem:existence}` (line 274) correctly references the existence condition $A^j < 1$.
- `Figure~\ref{fig:extension-panels}` (line 272) correctly references a two-panel figure.

### Conclusion (lines 288–298)
No issues. No cross-references appear in this section. Demonstratives ("this premium," "this mechanism") resolve to immediately preceding noun phrases.

### Proof of Proposition 1 (lines 299–330)
No issues. "This" (line 329) near `\eqref{eq:pd-ai}` resolves to the preceding equation (eq:pd-ai-solve), which is indeed identical to eq:pd-ai. "This approximation" (line 323) resolves to the approximation described in the same sentence.
