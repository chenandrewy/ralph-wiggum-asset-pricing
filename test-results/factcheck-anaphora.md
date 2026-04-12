# tests/factcheck-anaphora.py
Started: 2026-04-12 09:58:42 EDT
Runtime: 5m 38s
[ralph-garage/agent-logs/20260412T095842.925338-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T095842.925338-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to their intended referents.

## Findings by section

### Introduction (lines 38–70)
- "Proposition~\ref{prop:comp-statics} quantifies **this** attenuation": "this attenuation" resolves to the extinction-risk attenuation described in the preceding clause, which matches what Proposition 2 formalizes. **PASS.**
- No other demonstrative+ref pairs found.

### Model (lines 71–175)
- "this condition" near \ref{sec:ext2} (line 148): "this condition" resolves to A^j < 1 defined in the immediately preceding equation; the ref only locates where transfers are discussed. **PASS.**
- "This is exact" after \ref{prop:pd-ratios} (line 151): "This" resolves to the stated approximation (post-singularity P/D treated as equal to pre-singularity P/D), not to Proposition 1 itself. **PASS.**
- No other demonstrative+ref pairs found.

### Quantitative Analysis (lines 176–193)
- No demonstrative+ref pairs found. All cross-references are used as direct noun phrases without adjacent demonstratives. **PASS.**

### Extensions (lines 194–278)
- "This ratio" near \eqref{eq:transfer-ratio}: resolves to the ratio equation immediately above. **PASS.**
- "This connects...Proposition~\ref{prop:veto} implies": "this" refers to the preceding discussion of extinction risk interacting with the veto distortion; the proposition is not the antecedent. **PASS.**
- No other demonstrative+ref pairs found.

### Conclusion (lines 279–289)
- No cross-references in this section. **PASS.**

### Proof of Proposition 1 (lines 290–321)
- "This can be rewritten as equation~\eqref{eq:pd-ai}": "This" points to the immediately preceding displayed equation \eqref{eq:pd-ai-solve}, and the rewrite target is correctly identified. **PASS.**
- No other demonstrative+ref pairs found.
