# tests/factcheck-anaphora.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 2m 34s
[ralph-garage/agent-logs/20260412T202602.579973-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.579973-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their referenced targets.

## Findings by section

### Introduction (lines 38–70)
No demonstrative+cross-reference pairs found. The two propositions cited parenthetically (prop:comp-statics, prop:veto) use definite noun phrases, not demonstratives, and the prose claims match the targets.

### Model (lines 71–181)
One pair found. Line 154: "violate this condition" near `Section~\ref{sec:ext2}`. The demonstrative "this condition" correctly resolves to the existence condition $A^j < 1$ defined two lines earlier, not to sec:ext2. The section reference is locative ("as we discuss in..."). No mismatch.

### Quantitative Analysis (lines 182–199)
No demonstrative+cross-reference pairs found. All three cross-references use explicit noun labels ("Table", "Proposition", "Figure").

### Extensions (lines 200–284)
No demonstrative+cross-reference mismatches. Cross-references use definite descriptions ("the existence condition," "the P/D formula"). The one demonstrative near a cross-reference (line 235: "This connects to...Proposition~\ref{prop:veto}") correctly refers to the surrounding argument, with the proposition cited as support.

### Conclusion (lines 285–295)
No cross-references present in this section.

### Proof of Proposition 1 (lines 296–327)
One pair found. Line 326: "This can be rewritten as equation~\eqref{eq:pd-ai}." The demonstrative "This" correctly resolves to the solved P/D ratio in eq:pd-ai-solve (line 323), and eq:pd-ai is algebraically the same formula. No mismatch.
