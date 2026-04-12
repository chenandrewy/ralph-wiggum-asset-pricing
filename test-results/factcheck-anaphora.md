# tests/factcheck-anaphora.py
Started: 2026-04-11 21:15:26 EDT
Runtime: 2m 56s
[ralph-garage/agent-logs/20260411T211526.533006-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T211526.533006-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: One minor over-attribution found but no demonstrative resolves to a meaning that contradicts what the referenced target actually contains.

## Findings by section

### Introduction (lines 38–74)
No problems. All demonstratives near cross-references resolve correctly:
- "this attenuation" before `Proposition~\ref{prop:comp-statics}` correctly refers to the attenuation of the hedging channel by extinction risk, and the proposition's content (valuation spread decreasing in ξ) matches the gloss given in the same sentence.
- "this premium" after discussion of Figure 1 correctly refers to the AI valuation premium shown in the figure.
- References to `\ref{prop:veto}`, `\ref{sec:model}`, `\ref{sec:quant}`, `\ref{sec:extensions}`, `\ref{sec:conclusion}` are all clean nominal references without problematic demonstratives.

### Model (lines 75–179)
No problems. Key checks:
- Line 152: "this condition" near `\ref{sec:ext2}` correctly resolves to the existence condition $A^j < 1$ just defined in `\eqref{eq:existence}`, not to the section reference.
- Line 166: "This condition" near `Table~\ref{tab:pd-ratios}` correctly resolves to the $A^j > 1/2$ condition stated two sentences earlier; the table is cited as supporting evidence.
- All other cross-references use full noun phrases ("The P/D ratios in Proposition...", "the existence condition for finite prices") rather than bare demonstratives.

### Quantitative Analysis (lines 180–197)
One minor issue:
- Line 191: "extinction risk compresses the AI premium, as Proposition~\ref{prop:comp-statics} predicts" followed by "reducing both valuations and narrowing the spread." The proposition only covers the spread narrowing (the valuation spread is decreasing in ξ), not the level reduction in both valuations. The attribution scope is slightly too broad—the level-reduction claim is the authors' own gloss, not the proposition's content. However, this is an over-attribution rather than a demonstrative resolving to a contradictory meaning; the prose and the target describe the same mechanism, just at different scopes.

### Extensions (lines 198–282)
No problems. Key checks:
- Line 265: "This ratio" correctly resolves to the ratio $c^H_{post}/c^H_{no\text{-}transfer}$ displayed in `\eqref{eq:transfer-ratio}` immediately above.
- Line 269: "the existence condition in Remark~\ref{rem:existence}" correctly matches the Remark's content ($A^j < 1$).
- All other cross-references (`\eqref{eq:transfer-consumption}`, `\eqref{eq:phi-eff}`, `\ref{prop:pd-ratios}`, `\ref{fig:extension-panels}`) use clean nominal references without problematic demonstratives.

### Conclusion (lines 283–293)
No problems. No demonstratives appear near cross-references.

### Proof of Proposition 1 (lines 294–325)
No problems. One demonstrative near a cross-reference:
- Line 324: "This can be rewritten as equation~\eqref{eq:pd-ai}" — "This" correctly resolves to the equation just derived in `\eqref{eq:pd-ai-solve}`, and the two equations are algebraically identical.
