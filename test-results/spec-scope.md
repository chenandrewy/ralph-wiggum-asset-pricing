# tests/spec-scope.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 35s
[ralph-garage/agent-logs/20260412T202602.576114-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.576114-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative quantitative material and no empirical estimation or broad prediction menus.

## Findings

**Theoretical core.** The paper develops a single, deliberately simple discrete-time asset pricing model with three propositions (P/D ratios, extinction attenuation, veto under incomplete markets). All results are derived in closed form or via straightforward Bellman equation solutions. There are no ancillary models, no alternative specifications, and no broad menus of testable predictions.

**Empirical content is minimal and illustrative.** The only data-facing exhibit is Figure 1 (S&P 500 P/D ratio and NASDAQ/S&P relative price), used to motivate the paper rather than to test it. The text explicitly hedges the data mapping: "The mapping from NASDAQ vs. S&P 500 to the model's AI vs. non-AI distinction is imperfect." There is no regression analysis, no GMM estimation, no calibration to match moments, and no empirical hypothesis testing.

**Quantitative analysis is illustrative, not calibrated.** Table 1 reports P/D ratios across a parameter grid (singularity probability x extinction risk) using round-number parameters ($\beta=0.96$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$). The text describes the magnitudes as "broadly suggestive" rather than claiming precise calibration. Figure 2 similarly illustrates comparative statics (transfers vs. P/D ratios and consumption) rather than fitting data.

**No broad prediction menus.** The paper derives a focused set of qualitative predictions: (1) AI stocks trade at a premium under incomplete markets, (2) extinction risk attenuates the premium, (3) risk-averse households may inefficiently veto AI development, (4) transfers become effective when singularity growth overwhelms deadweight costs. These are tightly connected to the model's mechanism rather than constituting a sprawling list of testable implications.

**Extensions stay within scope.** The two extensions (veto, government transfers) are theoretical analyses that build directly on the baseline model's incomplete-markets mechanism. They add no new asset classes, no production-side modeling, and no empirical work. The conclusion explicitly acknowledges the model's simplicity as intentional.
