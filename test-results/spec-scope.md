# tests/spec-scope.py
Started: 2026-04-14 10:23:26 EDT
Runtime: 33s
[ralph-garage/agent-logs/20260414T102326.821261-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260414T102326.821261-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative rather than calibrated quantitative material and no broad prediction menus.

## Findings

**Theoretical core.** The paper develops a single, focused mechanism: hedging against AI-driven displacement under incomplete markets. The model has CRRA preferences, two public assets (AI and non-AI stocks), a discrete singularity shock, and closed-form price-dividend ratios (Proposition 1). This is a tight setup with few moving parts.

**Limited empirical content.** The only empirical material is Figure 1 (S&P 500 P/D ratios and NASDAQ-to-S&P relative prices), which serves purely as motivation. The paper explicitly notes the mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is "imperfect" and describes the magnitudes as "broadly suggestive" rather than calibrated. There are no regressions, GMM estimates, or formal empirical tests.

**Illustrative quantitative analysis.** Table 1 reports P/D ratios across a grid of singularity probabilities and extinction risks using fixed parameters ($\beta = 0.96$, $g = 0.02$, $\gamma = 4$, $\phi = 0.5$, $\eta = 0.5$). This is a numerical illustration of the model's mechanics, not a calibration exercise targeting data moments.

**No broad prediction menus.** The paper delivers three propositions: (1) closed-form P/D ratios with AI premium, (2) extinction attenuation of the spread, (3) veto under incomplete markets. Each is a direct implication of the single hedging-under-incompleteness mechanism. The extensions (veto distortion, government transfers) stay within the same model framework rather than branching into unrelated predictions.

**Deliberately simple.** The conclusion states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features." This self-awareness about scope is consistent with the paper's execution.

**Figure 2 (extension panels).** The government transfers analysis uses two parameterizations (baseline and large singularity) to illustrate how transfers compress P/D ratios and improve household consumption. Again illustrative, not estimated.
