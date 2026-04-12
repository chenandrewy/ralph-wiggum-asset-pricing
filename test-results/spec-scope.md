# tests/spec-scope.py
Started: 2026-04-12 09:32:52 EDT
Runtime: 41s
[ralph-garage/agent-logs/20260412T093252.137513-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260412T093252.137513-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative rather than calibrated quantitative material and no empirical estimation.

## Findings

### Theoretical scope
The paper develops a single, parsimonious model (CRRA household, discrete singularity, two public assets, incomplete markets) and derives all results from it. The three main results — hedging-based valuation premium (Proposition 1–2), veto distortion (Proposition 3), and government transfers — are tightly linked consequences of one mechanism (market incompleteness under AI singularity). There is no broad prediction menu; each result flows directly from the core model.

### Empirical content
Empirical content is limited to one motivating figure (Figure 1) showing S&P 500 P/D ratios and NASDAQ-to-S&P relative performance. This figure is purely descriptive — no regressions, no moment matching, no formal empirical tests. The paper explicitly hedges the data mapping: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect" (line 189).

### Quantitative material
- Table 1 reports P/D ratios across a parameter grid. This is illustrative exploration of model implications, not a formal calibration exercise. The paper describes the magnitudes as "broadly suggestive" rather than claiming to match specific empirical moments.
- Figure 2 shows how government transfers affect P/D ratios and consumption under two parameterizations. Again illustrative — demonstrating the mechanism's logic under different assumptions, not fitting data.
- A single numerical example for the veto proposition (line 227) uses round parameters to sharpen intuition.

### Self-awareness of scope
The conclusion explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis. The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."

### Summary
The paper stays firmly within the boundaries of a compact theory paper: one model, three linked propositions, illustrative quantitative exercises, and minimal empirical content used only for motivation.
