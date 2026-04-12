# tests/spec-scope.py
Started: 2026-04-12 15:47:40 EDT
Runtime: 42s
[ralph-garage/agent-logs/20260412T154740.736799-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260412T154740.736799-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative quantitative material and no empirical estimation or broad prediction menus.

## Findings

**Theoretical core.** The paper develops a single model with three propositions (closed-form P/D ratios, extinction attenuation, veto under incomplete markets) and two focused extensions (veto/efficient development, government transfers). All results are analytical with closed-form or semi-closed-form expressions.

**Quantitative material is illustrative, not calibrated.** Section 3 ("Quantitative Analysis") reports P/D ratios across a parameter grid (Table 1) but does not calibrate to match moments, estimate parameters from data, or run regressions. The language is explicitly hedged: "The magnitudes are broadly suggestive" and "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect." Figure 2 uses chosen parameterizations to illustrate the transfers mechanism, not to fit data.

**Empirical content is minimal.** The only empirical exhibit is Figure 1 (Shiller P/D ratio and NASDAQ/S&P 500 relative price), which serves as motivation rather than as a test of the model. There is no econometric analysis, no moment-matching, and no out-of-sample prediction.

**No broad prediction menus.** The paper focuses on a single mechanism (hedging displacement under incomplete markets) and derives a narrow set of implications: (1) AI stocks trade at higher P/D ratios, (2) extinction risk attenuates the spread, (3) incomplete markets can cause inefficient vetoes, (4) transfers become effective under explosive growth. The conclusion explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features."

**Scope discipline.** The paper does not attempt to explain cross-sectional return patterns, estimate risk premia, or provide a comprehensive account of AI valuations. It highlights one channel and explores its implications analytically.
