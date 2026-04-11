# tests/factcheck-anaphora.py
Started: 2026-04-11 10:15:04 EDT
Runtime: 1m 36s
[ralph-garage/agent-logs/20260411T101504.818952-0400_factcheck-anaphora_claude_opus.log](../ralph-garage/agent-logs/20260411T101504.818952-0400_factcheck-anaphora_claude_opus.log)

# factcheck-anaphora
VERDICT: FAIL
REASON: Line 196 attributes a claim to Proposition 2(iii) that the proposition does not establish.

## Findings by section

### Introduction (lines 38–72)
No issues found.

### Model (lines 73–184)
No issues found.

### Quantitative Analysis (lines 185–202)

**Line 196** — "extinction risk reduces both valuations and compresses the AI premium, as Proposition~\ref{prop:comp-statics}(iii) predicts"

The sentence attributes two claims to Proposition 2(iii):
1. "reduces both valuations" — Proposition 2(iii) does **not** state this. It says the valuation **spread** ($P^{AI}/D^{AI} - P^N/D^N$) and ratio are decreasing in extinction probability $\xi$; it is silent on the direction of the individual level effects.
2. "compresses the AI premium" — this correctly matches Proposition 2(iii).

The first claim is not what the cited proposition proves. Both P/D ratios could rise while the spread narrows and the proposition would still hold. The prose should either drop "reduces both valuations" from the scope of the citation or provide a separate argument for the level-reduction claim.

### Extensions (lines 203–287)
No issues found.

### Conclusion (lines 288–298)
No issues found.

### Proof of Proposition (lines 299–330)
No issues found.
