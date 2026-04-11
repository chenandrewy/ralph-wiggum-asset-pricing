# tests/spec-scope.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 36s
[ralph-garage/agent-logs/20260410T225642.524914-0400_spec-scope_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.524914-0400_spec-scope_claude_opus.log)

# spec-scope
VERDICT: PASS
REASON: The paper maintains a compact theoretical scope with illustrative rather than calibrated quantitative material and no broad prediction menus.

## Findings

**Theoretical scope.** The model is tightly focused: a representative household with CRRA preferences, two public assets (AI and non-AI stocks), a discrete singularity shock, and market incompleteness from restricted AI equity. The entire framework delivers closed-form P/D ratios (Proposition 1) and clean comparative statics (Proposition 2). There are exactly two extensions—veto under incomplete markets and government transfers—both directly connected to the core displacement/hedging mechanism.

**Empirical content is minimal and illustrative.** The paper contains:
- One motivating figure (Figure 1: NASDAQ vs S&P 500 since 2015), used to establish a stylized fact rather than to test the model.
- One calibration table (Table 1: P/D ratios across a grid of singularity probabilities and extinction risks), explicitly described as "broadly suggestive" rather than moment-matched.
- One extension figure (Figure 2: transfers and valuations), illustrating the transfer mechanism with two parameter scenarios.

The paper explicitly disclaims empirical ambition: "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel" (Section 5).

**No broad prediction menus.** The model generates exactly one observable prediction—AI stocks should have higher P/D ratios than non-AI stocks—plus comparative statics on how displacement severity, singularity probability, and extinction risk affect the spread. There is no attempt to match return moments, cross-sectional sorts, or time-series dynamics.

**Quantitative material is illustrative.** Parameters ($\phi = 0.5$, $\eta = 0.5$, $\gamma = 4$, etc.) are chosen for transparency rather than estimation. The paper notes that the NASDAQ/S&P comparison is "imperfect" and that the model's magnitudes are only "consistent with" observed patterns.
