# tests/factcheck-exhibits.py
Started: 2026-04-09 20:52:35 EDT
Runtime: 3m 1s
[ralph-garage/agent-logs/20260409T205235.728203-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T205235.728203-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated from the code, with table values, figure logic, and annotations matching the model equations and stated parameters.

## Figure 1 (fig:ai-valuations)

Monthly closing prices for the NASDAQ Composite (solid) and S&P 500 (dashed), normalized to January 2015 = 100. Data sourced from FRED (NASDAQ) and the Shiller/datahub dataset (S&P 500).

### Suspicious features

1. **Sharp post-2023 divergence.** The NASDAQ pulls away dramatically from the S&P 500 starting around 2023, with the gap appearing larger than at any prior point.
2. **COVID-era dip and recovery (2020).** Both series show a sharp drawdown and rapid rebound.

### Code check

1. **Post-2023 divergence.** This reflects real market data. The code downloads live monthly data from FRED (NASDAQCOM) and datahub (S&P 500), normalizes each to 100, and plots directly. No transformation beyond normalization is applied (`code/generate-exhibits.R:284-292`). The divergence corresponds to the AI/tech rally of 2023-2025 and is well-documented in financial markets. **Verified: real feature.**
2. **COVID dip.** Same logic: the code plots raw normalized data. The 2020 dip corresponds to the March 2020 COVID crash. **Verified: real feature.**

No data caching is present locally (the `data/` directory is empty), so exact values cannot be independently reproduced without network access. However, the code logic is straightforward normalization of externally sourced price data with no suspicious filtering, subsetting, or transformation.

**Exhibit verdict: PASS** -- No artifacts or errors detected; visible features reflect real market data.

## Table 1 (tab:pd-ratios)

Price-dividend ratios for AI stocks and non-AI stocks across a grid of singularity probabilities (p = 0.1% to 1.0%) and extinction probabilities (xi = 0% to 20%), using the closed-form P/D formula from Proposition 1.

### Suspicious features

1. **Explosive AI P/D at p = 1%.** The AI stock P/D jumps from 33.0 (at p = 0.8%, xi = 0%) to 76.4 (at p = 1.0%, xi = 0%), a more-than-doubling. This could suggest a coding error or numerical instability.
2. **Non-AI P/D relatively stable.** Non-AI P/D only moves from 9.8 to 13.3 across the entire grid, while AI P/D ranges from 10.5 to 76.4.

### Code check

1. **Explosive AI P/D.** Independent numerical verification confirms: at p = 1%, xi = 0%, K_AI = 0.9871, so P/D = K/(1-K) = 76.4. The formula K/(1-K) is hyperbolic near K = 1, producing rapid growth. This is the correct mathematical behavior of the Gordon-growth-style formula, and the paper explicitly discusses this via the existence condition in Remark 1 (`paper.tex:139-145`). The code at `generate-exhibits.R:42-48` implements the formula correctly: `K = base * ((1-p) + p*(1-xi)*sdf_sing)` with `sdf_sing = phi^(-gamma) * (1+eta)^(-gamma) * gamma_j`. **Verified: correct behavior, not an error.**
2. **Non-AI stability.** The non-AI SDF singularity term (sdf_sing_non = 3.79) is much smaller than the AI term (sdf_sing_ai = 10.11) because Gamma_N = 1.2 vs Gamma_AI = 3.2. This means K_N stays farther from 1 across the grid, producing moderate P/D values. **Verified: correct.**

All 20 table cells were independently recomputed and match the output to one decimal place.

**Exhibit verdict: PASS** -- All values verified against the model formula; no computational errors.

## Figure 2 (fig:extension-panels)

Two-panel figure. Panel (a): AI stock P/D ratio vs. tax rate tau for baseline (eta = 0.5, phi = 0.5) and large singularity (eta = 9, phi = 0.05). Panel (b): household consumption change in the singularity state vs. tau (log-scale y-axis), with catastrophe markers at tau = 0.

### Suspicious features

1. **Panel (a): Large-singularity P/D appears to start at the y-axis cap (~25) and drops steeply.** The annotation says "P/D -> infinity as tau -> 0." This could be an artifact of capping.
2. **Panel (b): Large-singularity consumption growth rises dramatically with tau, appearing almost linear on a log scale.** The baseline shows much more modest gains.
3. **Panel (b): Annotations claim "50% loss" and "25% loss" at tau = 0.** These specific numbers need verification.

### Code check

1. **Panel (a) asymptote.** At tau = 0 with large-singularity parameters (phi = 0.05, eta = 9), the existence condition K < 1 is violated (K = 2.37), producing NA. The code correctly returns NA (`generate-exhibits.R:123`), and the plot caps y at 25 (`generate-exhibits.R:171`). The annotation at `generate-exhibits.R:185-187` correctly indicates the asymptote. As tau increases, phi_eff rises, K falls below 1, and finite P/D values emerge. **Verified: correct handling of the divergence.**
2. **Panel (b) steep rise.** The consumption growth function (`generate-exhibits.R:113-115`) computes `phi_val*(1+eta_val) + tau*(1-delta*tau)*(1-phi_val*alpha0)/alpha0*(1+eta_val)`. For the large singularity, the transfer base `(1-phi_val*alpha0)/alpha0 * (1+eta_val)` = `(1-0.035)/0.70 * 10` = 13.79, so each unit of tau adds ~13.8 to consumption growth (before deadweight costs). The steep rise is a direct consequence of the enormous output growth (eta = 9). On the log scale this appears approximately linear, which is mathematically expected. **Verified: correct.**
3. **Annotations.** Baseline at tau = 0: phi*(1+eta) = 0.5*1.5 = 0.75, i.e., 25% loss. Large singularity at tau = 0: phi_large*(1+eta_large) = 0.05*10 = 0.5, i.e., 50% loss. Both independently confirmed. **Verified: correct.**

The `gamma_j_val` correctly varies with scenario (`share_ratio_ai * (1+eta_val)`), matching the formula Gamma^AI = (share_ratio_ai) * (1+eta) from the paper. The phi_eff formula in the code matches Equation (7) of the paper.

**Exhibit verdict: PASS** -- All features trace correctly to the generating code and model equations.
