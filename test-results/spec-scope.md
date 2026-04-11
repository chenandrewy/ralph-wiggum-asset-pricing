# tests/spec-scope.py
Started: 2026-04-11 15:15:58 EDT
Runtime: 36s
[ralph-garage/agent-logs/20260411T151558.200945-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260411T151558.200945-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with limited empirical content, no broad prediction menus, and illustrative rather than calibrated quantitative material.

## Findings

### Empirical content: minimal and illustrative
- One empirical figure (Figure 1): NASDAQ vs S&P 500 normalized prices since 2015, used purely to motivate the question. No regressions, no estimation, no empirical tests.
- The paper explicitly acknowledges the comparison is "imperfect" and uses it only to show the pattern is "consistent with" model predictions (Section 3).

### No broad prediction menu
- The model delivers two focused results: (1) AI stock P/D ratios exceed non-AI stock P/D ratios due to the hedging channel under incomplete markets, and (2) extinction risk attenuates this spread. Extensions add the veto distortion and government transfers, both tightly connected to the core incomplete-markets mechanism.
- There is no laundry list of testable predictions or moment-matching exercises.

### Quantitative material: illustrative, not calibrated
- Table 1 reports model-implied P/D ratios across a grid of singularity probabilities and extinction risks. Parameters are chosen to be "plausible" rather than estimated or calibrated to match specific data moments.
- Figure 2 (extension panels) illustrates how transfers affect P/D ratios and household consumption. Again illustrative, not fitted to data.
- The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."

### Theoretical scope: tight
- Three propositions, all closed-form or analytical.
- Two extensions, both directly motivated by the core incomplete-markets mechanism.
- No production side, no heterogeneous agents, no dynamic portfolio choice, no continuous-time dynamics — all deliberately excluded per the conclusion.
