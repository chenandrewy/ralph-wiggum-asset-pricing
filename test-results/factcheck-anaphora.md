# tests/factcheck-anaphora.py
Started: 2026-04-11 10:02:08 EDT
Runtime: 1m 27s
[ralph-garage/agent-logs/20260411T100208.983372-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T100208.983372-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to their intended targets.

## Findings by section

### Introduction (lines 38–74)
No anaphora resolution issues found. Cross-references checked:
- Line 40: "Figure~\ref{fig:ai-valuations} illustrates" — no demonstrative; figure content matches description.
- Line 57: "as Proposition~\ref{prop:veto} shows, calls to slow or halt AI development may partly reflect investors' inability to share in its upside" — Proposition 3 is indeed about veto under incomplete markets and supports this claim.
- Line 61: Section references (\ref{sec:model}, \ref{sec:quant}, \ref{sec:extensions}, \ref{sec:conclusion}) — all accurate roadmap references.

### Model (lines 75–186)
No anaphora resolution issues found. Cross-references checked:
- Line 148: "The P/D ratios in Proposition~\ref{prop:pd-ratios} are well-defined" — correctly refers to the P/D formulas in Proposition 1.
- Line 152: "this condition" near "Section~\ref{sec:ext2}" — "this condition" resolves to the existence condition $A^j < 1$ defined in the same remark, not to the section reference. The sentence correctly states that Section 4.2 discusses how displacement can violate the existence condition, which it does.
- Line 155: "The closed-form expressions in Proposition~\ref{prop:pd-ratios}" — correctly refers to the P/D ratio formulas.
- Line 157: "The key economic content of Proposition~\ref{prop:pd-ratios}" — correctly refers to Proposition 1.
- Line 182: "the existence condition for finite prices (Remark~\ref{rem:existence})" — Remark 1 is indeed about the existence condition $A^j < 1$.

### Quantitative Analysis (lines 187–204)
No anaphora resolution issues found. Cross-references checked:
- Line 198: "as Proposition~\ref{prop:comp-statics}(iii) predicts" — the surrounding text says extinction risk compresses the AI premium; Proposition 2(iii) states the valuation spread is decreasing in $\xi$. These match.
- Line 200: "As Figure~\ref{fig:ai-valuations} shows, the AI-heavy NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" — Figure 1 plots NASDAQ vs S&P 500 normalized to Jan 2015, which supports this claim.

### Extensions (lines 205–289)
No anaphora resolution issues found. Cross-references checked:
- Line 240: "This connects to debates about AI regulation: Proposition~\ref{prop:veto} implies..." — "This" resolves to the preceding discussion of extinction risk interacting with the veto distortion. Proposition 3 is about veto under incomplete markets; the claim that it implies calls to slow AI reflect inability to share upside is an accurate reading.
- Line 264: "This follows directly from dividing \eqref{eq:transfer-consumption}" — "This" resolves to the derivation of $\phi_\text{eff}$. Equation (7) is the post-transfer consumption formula; dividing it by $\alpha(1+\eta)(1+g)C_t$ does yield $\phi_\text{eff}$. Correct.
- Line 264: "the P/D formula from Proposition~\ref{prop:pd-ratios} applies with $\phi$ replaced by $\phi_\text{eff}$" — Proposition 1 gives the P/D formula parameterized by $\phi$; substituting $\phi_\text{eff}$ is valid since it enters the SDF identically.
- Line 276: "the existence condition in Remark~\ref{rem:existence} is violated" — Remark 1 defines the existence condition as $A^j < 1$; the text correctly states it is violated when marginal utility is extreme enough for the pricing sum to diverge.

### Conclusion (lines 290–300)
No cross-references with demonstratives. No issues found.

### Proof of Proposition 1 (lines 301–332)
No anaphora resolution issues found. Cross-references checked:
- Line 325: "Table~\ref{tab:pd-ratios}" — correctly refers to the P/D ratio table.
- Line 331: "equation~\eqref{eq:pd-ai}" — correctly refers to the AI P/D ratio formula.
