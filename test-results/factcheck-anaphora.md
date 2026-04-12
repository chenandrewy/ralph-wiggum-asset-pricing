# tests/factcheck-anaphora.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 2m 8s
[ralph-garage/agent-logs/20260412T154740.749503-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.749503-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve to meanings consistent with their referenced targets.

## Findings by section

### Introduction (lines 38--70)
No issues. Cross-references to `fig:ai-valuations`, `prop:comp-statics`, `prop:veto`, `sec:model`, `sec:quant`, and `sec:extensions` all use bare noun phrases without demonstratives, or have demonstratives that resolve to prior noun phrases rather than to the cross-reference target.

### Model (lines 71--175)
No issues. The potentially tricky case is "This discontinuity" (line 171) following "(Remark~\ref{rem:existence})": it refers to the finite-to-infinite price jump, which is precisely what Remark 1's existence condition describes. References to `prop:pd-ratios`, `eq:existence`, `sec:ext2`, and `rem:existence` all resolve correctly.

### Quantitative Analysis (lines 176--193)
No issues. Cross-references to `tab:pd-ratios`, `prop:comp-statics`, and `fig:ai-valuations` appear without adjacent demonstratives.

### Extensions (lines 194--278)
No issues. References to `prop:veto`, `eq:transfer-consumption`, `eq:phi-eff`, `prop:pd-ratios`, and `rem:existence` all use definite articles or bare labels rather than demonstratives, and the prose accurately describes each target's content.

### Conclusion (lines 279--289)
No cross-references appear in this section, so no anaphora resolution errors are possible.

### Proof of Proposition 1 (lines 290--321)
No issues. "This can be rewritten as equation~\eqref{eq:pd-ai}" (line 320): "This" refers to the solved formula on line 317, which is the same mathematical object as `eq:pd-ai`. References to `tab:pd-ratios` and `prop:pd-ratios` have no adjacent demonstratives.
