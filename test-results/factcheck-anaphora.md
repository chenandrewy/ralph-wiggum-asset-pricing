# tests/factcheck-anaphora.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 4m 56s
[ralph-garage/agent-logs/20260409T200738.680342-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.680342-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to their intended targets.

## Findings by section

### Introduction (lines 39–81)
No anaphora issues. Demonstratives like "such gains" (line 41, near Figure~\ref{fig:ai-valuations}) resolve to "transformative productivity gains" in the same clause, not to the figure content. No mismatch.

### Model (lines 82–193)
No anaphora issues. References to Proposition~\ref{prop:pd-ratios}, Section~\ref{sec:ext2}, and Appendix~\ref{app:proof-pd} are not preceded by ambiguous demonstratives. Nearby demonstratives ("This is the hedging channel," "This makes the interaction...") resolve to mechanisms described in the immediately preceding text, not to cross-referenced targets.

### Quantitative Analysis (lines 194–211)
No anaphora issues. No demonstratives appear near the cross-references to Table~\ref{tab:pd-ratios}, Proposition~\ref{prop:comp-statics}(iii), or Figure~\ref{fig:ai-valuations}.

### Extensions (lines 212–281)
No anaphora issues. "This ratio" (line 264) correctly resolves to equation~\eqref{eq:transfer-ratio} defined immediately above. "This discontinuity" (line 268) refers to the P/D ratio behavior described in the preceding sentences, consistent with the existence condition in Remark~\ref{rem:existence}. The reference to "The P/D formula from Proposition~\ref{prop:pd-ratios}" (line 256) uses a definite description, not a demonstrative.

### Conclusion (lines 282–292)
No cross-references appear in this section. Demonstratives ("this premium," "This mechanism") resolve to antecedents within the paragraph.

### Proof of Proposition 1 (lines 293–322)
No anaphora issues. "This can be rewritten as equation~\eqref{eq:pd-ai}" (line 321) correctly refers to the solved formula on the preceding line. "this is exact when..." (line 315) refers to the approximation described in the same sentence.
