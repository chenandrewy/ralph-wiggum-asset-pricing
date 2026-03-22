# Improvement Plan

## Status

All tests pass. The referee-top3 review identifies two substantive gaps that limit publishability.

## Key Issues

### From referee-top3

1. **No empirical content beyond Figure 1.** The testable-implications section (3.4) promises an identification strategy (singularity-risk shocks orthogonal to earnings revisions) but provides zero empirical evidence. The referee calls this a "promissory note" and says it makes the hedging channel "unfalsified and unfalsifiable."

2. **The incomplete-markets friction ($\alpha$) is asserted, not measured.** The welfare analysis ($\omega$ up to 3.4%) and the GKP comparison ("reducible in principle") are disconnected from observable data. No proxies for $\alpha$ are discussed, $\psi = 0.15$ is assumed without justification, and the policy discussion is abstract.

### From CFR-R1 referee report (spec file)

The CFR referee's two concerns have been addressed in prior iterations:
- GKP subsumption concern → addressed via the incomplete-markets parameterization ($\alpha$), the hedging/cash-flow decomposition, and explicit GKP comparison prose.
- Jones (2024) integration → addressed in Section 4 (extinction risk, heterogeneous beliefs, infinite output with bilateral-trade microfoundation).

## No overhaul needed

The model section is clean: theory-correctness passes, notation is consistent, all propositions are correctly derived, and the narrative aligns with results. The model structure is sound and does not need reworking.

## Plan: Add empirical content to strengthen the hedging channel

The referee's two comments both point to the same gap: the paper lacks empirical grounding beyond the motivating figure. The plan focuses on closing this gap within the 20-page constraint.

### 1. Add a preliminary event study (addresses referee comment 1)

**What:** A small-sample descriptive analysis showing AI stocks respond abnormally to singularity-risk events, controlling for earnings news. Use 5–8 events: the 2023 executive order on AI safety, publication of Grace et al. (2024) expert survey results, major lab safety announcements (e.g., Anthropic/OpenAI safety publications), EU AI Act milestones.

**Where:** Replace the current testable-implications subsection (Section 3.4) with a short empirical subsection. Present abnormal returns for AI stocks vs. non-AI stocks in a narrow event window (e.g., [-1, +1] days). A simple table of cumulative abnormal returns (CARs) would suffice—this is a theory paper, not an empirical one, so a descriptive pass is adequate.

**Data:** CRSP daily returns for the AI portfolio (NVDA, MSFT, GOOG, META, AMZN) and S&P 500. Market-model residuals using a 120-day estimation window.

**Code:** Write an R script `code/table-event-study.R` that computes CARs and outputs a LaTeX table.

**Constraint:** This adds one exhibit (table). Current count is 5; max is 6.

### 2. Add observable proxies for $\alpha$ and ground $\psi$ in data (addresses referee comment 2)

**What:** Add 2–3 paragraphs to the calibration/sensitivity discussion that:
- Identify observable proxies for $\alpha$: ratio of public-to-total AI market capitalization, household participation rates in venture/PE funds, secondary-market volume for pre-IPO AI shares.
- Calibrate $\psi$ from data rather than assuming it: estimate the size of private AI capital (major private AI labs' valuations) relative to aggregate household consumption.
- Briefly note how $\alpha$ is evolving (secondary markets like Forge/EquityZen, AI-focused ETFs, accredited investor definition changes).

**Where:** Add to the partial-market-access discussion in Section 3.2 (after Table 3).

**Constraint:** No new exhibits needed—this is prose and calibration grounding.

### 3. Tighten the testable-implications prose

**What:** Reframe the section around the event-study evidence rather than the current promissory-note framing. Keep the theoretical identification argument ($\lambda$-shocks orthogonal to earnings) but present it as the motivation for the empirical exercise, not a placeholder for future work. Remove "We leave this empirical test to future work."

### 4. Minor prose adjustments

- In the GKP comparison, add a sentence noting that the $\alpha$-trajectory is observable (tying to the proxies from item 2), strengthening the "reducible in principle" claim.
- In the conclusion, update the testability language to reference the event-study evidence.
