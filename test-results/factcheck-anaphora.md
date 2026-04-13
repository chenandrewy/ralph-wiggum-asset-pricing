# tests/factcheck-anaphora.py
Started: 2026-04-12 20:00:23 EDT
Runtime: 1m 6s
[ralph-garage/agent-logs/20260412T200023.677241-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260412T200023.677241-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: PASS
REASON: All demonstratives near cross-references resolve correctly to their referenced targets.

## Findings by section

### Introduction (lines 38–70)
No issues. Proposition refs (`prop:comp-statics`, `prop:veto`) and section refs (`sec:model`, `sec:quant`, `sec:extensions`) all match their surrounding prose accurately.

### Model (lines 71–175)
No issues. References to `prop:pd-ratios`, `rem:existence`, `sec:ext2`, `tab:pd-ratios`, and `eq:existence` all resolve correctly. Demonstratives like "this condition" (line 148) refer to the immediately preceding existence condition, not to the cross-reference target.

### Quantitative Analysis (lines 176–193)
No issues. References to `tab:pd-ratios`, `prop:comp-statics`, and `fig:ai-valuations` use nominal descriptions without ambiguous demonstratives.

### Extensions (lines 194–278)
No issues. References to `prop:pd-ratios`, `eq:transfer-consumption`, `eq:phi-eff`, `rem:existence`, `prop:veto`, and `fig:extension-panels` all match their prose context. Panel references ("left panel" = P/D ratios = Panel a; "right panel" = consumption = Panel b) are consistent with the figure caption.

### Conclusion (lines 279–289)
No issues. No cross-references appear in this section.

### Proof of Proposition 1 (lines 290–321)
No issues. "This can be rewritten as equation (eq:pd-ai)" on line 320 correctly refers to the immediately preceding derived equation, which matches the referenced target.
