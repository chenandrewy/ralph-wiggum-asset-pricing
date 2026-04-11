# tests/spec-scope.py
Started: 2026-04-11 10:30:39 EDT
Runtime: 39s
[ralph-garage/agent-logs/20260411T103039.126874-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260411T103039.126874-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with one core model, illustrative (not calibrated) quantitative analysis, and two tightly scoped extensions.

## Findings

### Theoretical scope
The paper develops a single consumption-based asset pricing model with a discrete AI singularity, market incompleteness, and extinction risk. The model delivers closed-form price-dividend ratios (Proposition 1) and comparative statics (Proposition 2). The two extensions — veto/efficient development (Proposition 3) and government transfers — are direct consequences of the core mechanism, not separate models. The conclusion explicitly states: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."

### Empirical content
Empirical content is minimal and illustrative:
- **Figure 1**: NASDAQ vs. S&P 500 since 2015, used only to motivate the valuation spread. The paper explicitly notes this comparison is "imperfect" and "broadly suggestive."
- **Table 1**: Model-generated P/D ratios across a parameter grid. This is quantitative analysis of the model, not empirical estimation.
- No regressions, no calibration to match empirical moments, no estimation.

### Prediction menu
The paper does not offer a broad menu of testable predictions. The comparative statics (Proposition 2) are limited to three results about the valuation spread's response to displacement severity, singularity probability, and extinction probability — all direct implications of the single mechanism.

### Quantitative material
Section 3 ("Quantitative Analysis") is illustrative rather than calibrated. Parameters are chosen for transparency ($\phi = 0.5$, $\eta = 0.5$, etc.) and the paper reports that "magnitudes are broadly suggestive" rather than claiming precise empirical fit. The extension figures use round-number parameters to illustrate how transfers interact with singularity severity.
