# tests/spec-scope.py
Started: 2026-04-14 10:33:09 EDT
Runtime: 33s
[ralph-garage/agent-logs/20260414T103310.014419-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260414T103310.014419-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative rather than calibrated quantitative material, no empirical estimation, and no broad prediction menus.

## Findings

### Theoretical scope
The paper presents a single discrete-time asset pricing model with CRRA preferences, two public assets (AI and non-AI stocks), and a stochastic singularity event. It derives three propositions:
1. Closed-form price-dividend ratios (Proposition 1)
2. Extinction attenuation of the valuation spread (Proposition 2)
3. Veto under incomplete markets (Proposition 3)

The two extensions (veto distortion and government transfers) flow directly from the core incomplete-markets mechanism rather than expanding into unrelated territory.

### Empirical content — limited and illustrative
- **Figure 1** shows S&P 500 P/D ratios and NASDAQ-to-S&P relative valuations. This is purely descriptive — no regressions, no formal estimation, no hypothesis tests.
- **Table 1** reports P/D ratios across a parameter grid. These are computed from the model's closed-form expressions, not estimated from data. The paper explicitly notes the mapping to real data is "imperfect" and the magnitudes are "broadly suggestive."
- **Figure 2** illustrates the transfer extension with parameterized examples. Again, no estimation.

There is no econometric analysis anywhere in the paper.

### No broad prediction menus
The paper focuses on one mechanism (hedging displacement under incomplete markets) and its direct consequences (valuation spreads, veto distortion, transfer effectiveness). It does not enumerate a long list of testable predictions or attempt to explain a wide range of asset pricing phenomena.

### Quantitative material is illustrative
The conclusion explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis." The numerical examples use round-number parameterizations (φ = 0.5, η = 0.5, γ = 4) chosen to illustrate the mechanism rather than to match moments or calibrate to data.
