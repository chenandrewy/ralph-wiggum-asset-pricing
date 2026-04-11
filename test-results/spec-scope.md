# tests/spec-scope.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 43s
[ralph-garage/agent-logs/20260411T161024.930264-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.930264-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative quantitative material, no empirical estimation, and no broad prediction menu.

## Findings

### Empirical content: minimal and illustrative
- **Figure 1** shows descriptive time series (S&P 500 P/D ratio and NASDAQ/S&P relative price) to motivate the hedging story. No regressions, no moment-matching, no empirical tests.
- **Table 1** reports model-implied P/D ratios across a parameter grid. The paper explicitly describes the magnitudes as "broadly suggestive" and notes the comparison with data is "imperfect" (Section 3).
- **Figure 2** illustrates the government-transfer extension. Again purely model-based.

### No broad prediction menu
The paper delivers exactly three linked results:
1. AI stocks command a hedging-driven valuation premium under incomplete markets (Proposition 1).
2. Extinction risk attenuates the premium (Proposition 2).
3. Market incompleteness can cause inefficient veto of AI development; government transfers can restore efficiency when singularity growth is large (Proposition 3).

There is no laundry list of testable predictions, cross-sectional implications, or auxiliary results beyond these three propositions.

### Illustrative rather than calibrated quantitative material
- Parameters are chosen to be "plausible" rather than estimated or calibrated to match specific data moments.
- The quantitative section (Section 3) spans one page and one table; its purpose is to show the mechanism produces reasonable magnitudes, not to fit the data.
- The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features."

### Compact theoretical scope
- Two assets (AI stocks, non-AI stocks), one representative household, one shock (singularity), CRRA preferences.
- Two extensions, both tightly connected to the core incomplete-markets mechanism (veto distortion and transfers).
- No production side, no heterogeneous agents, no continuous-time dynamics, no calibration exercise.
