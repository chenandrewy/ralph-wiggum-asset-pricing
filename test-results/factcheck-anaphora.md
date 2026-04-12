# tests/factcheck-anaphora.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 4m 51s
[ralph-garage/agent-logs/20260411T214322.792186-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.792186-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: FAIL
REASON: One demonstrative near a cross-reference has ambiguous resolution between an empirical and a theoretical comparison.

## Findings

### Section: Introduction (lines 38–74)
**PASS.** All demonstratives near cross-references resolve correctly:
- "such gains" near `Figure~\ref{fig:ai-valuations}` — refers to "transformative productivity gains" in the same sentence; the figure shows valuation data consistent with that context.
- "this attenuation" near `Proposition~\ref{prop:comp-statics}` — refers to the extinction-risk attenuation just described; the proposition states the valuation spread decreases in extinction probability. Match.
- "the downside" near `Proposition~\ref{prop:veto}` — refers to displacement downside; the proposition addresses the household's veto under incomplete markets driven by unhedgeable downside. Match.

### Section: Model (lines 75–179)
**PASS.** All demonstratives near cross-references resolve correctly:
- "this condition" (line 152) near `Section~\ref{sec:ext2}` — refers to the existence condition $A^j < 1$ stated in the same remark. Match.
- "This is the hedging channel" (line 157) near `Proposition~\ref{prop:pd-ratios}` — refers to the mechanism just described (AI stocks pay off when household consumption falls). Match.
- "This condition" (line 166) near `Table~\ref{tab:pd-ratios}` — refers to the $A^j > 1/2$ condition stated two sentences prior. Match.

### Section: Quantitative Analysis (lines 180–197)
**FAIL.** One ambiguous demonstrative found:
- **Line 193**: "This comparison is imperfect" appears after a sentence referencing `Figure~\ref{fig:ai-valuations}`. The demonstrative "This comparison" could resolve to (a) the empirical comparison between NASDAQ and S&P 500 shown in the figure, or (b) the theoretical comparison between AI and non-AI stock valuations from the model (discussed via `Table~\ref{tab:pd-ratios}` in the preceding paragraph). The subsequent qualifications ("the NASDAQ is broader than 'AI stocks'...") clarify the intended referent is the empirical-to-theoretical mapping, but the demonstrative itself is ambiguous between the figure's empirical content and the table's theoretical content.

### Section: Extensions (lines 198–282)
**PASS.** All demonstratives near cross-references resolve correctly. Key instances:
- "This connects to debates about AI regulation: Proposition~\ref{prop:veto} implies..." — "This" refers to the preceding discussion of extinction risk interacting with the veto distortion. The proposition addresses the veto mechanism. Match.
- No other demonstratives appear immediately before cross-references in this section.

### Section: Conclusion (lines 283–293)
**PASS.** No cross-references appear in this section. All demonstratives ("this mechanism", "this premium") have clear, unambiguous antecedents within the local text.

### Section: Proof of Proposition (lines 294–325)
**PASS.** One demonstrative near a cross-reference:
- "This can be rewritten as equation~\eqref{eq:pd-ai}" — "This" refers to the formula in `eq:pd-ai-solve` derived immediately above. The target `eq:pd-ai` is the equivalent P/D ratio formula from Proposition 1. Match.
