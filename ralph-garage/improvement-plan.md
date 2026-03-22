# Improvement Plan

## Status

All tests pass. Referee-top3 review completed with two substantive comments. No section needs an overhaul — the model is correct, well-structured, and spec-compliant. Focus is on addressing referee feedback.

## Key Issues

### From referee-top3

1. **Singularity parameters lack empirical grounding.** The calibration varies $\lambda$, $\theta$, $\phi$ freely but offers no external evidence. The paper repeatedly compares model output to data (2-2.7x ratio) yet treats parameters as illustrative. Either anchor them or soften quantitative claims.

2. **Market incompleteness is exogenous and unexplained.** A 29% premium implies large gains from trade — why don't intermediaries securitize private AI capital pre-singularity? Section 4.3 microfounds friction resolution post-singularity, but the pre-singularity persistence is unaddressed. The referee notes GKP's friction (unborn innovators) is structurally irreducible, while ours (private capital held by existing agents) is exactly what financial markets resolve.

### From CFR-R1 (already largely addressed)

- GKP subsumption concern: addressed via three-point differentiation in intro and continuous $\alpha$ parameter.
- Jones (2024) integration: addressed via Section 4 extensions.

## Planned Changes

### 1. Anchor calibration parameters empirically (referee comment 1)

**Where:** Section 3.1 (Calibration), before Table 1.

Add a paragraph grounding each singularity parameter in external evidence:
- **$\lambda$ (singularity probability):** Cite AI researcher surveys (e.g., Grace et al. 2024) on probability of transformative AI within N years. Convert to an annual hazard rate. The 1-5% range in the paper should be shown to bracket survey-based estimates.
- **$\theta = 0.50$ (AI dividend jump):** Relate to the private-vs-public split in AI capital. If private AI capital is roughly equal to public AI market cap, then a singularity that doubles total AI value implies $\theta \approx 0.50$ for the public component. Cite industry estimates of private AI valuations.
- **$\phi = 0.30$ (non-AI dividend drop):** Relate to labor share displacement estimates. If AI automates 30-40% of tasks (cite Eloundou et al. 2023 or similar), a 30% drop in non-AI dividends is consistent.

Also soften language in the growth-hedging decomposition: frame the 2-2.7x comparison as "consistent with" rather than "accounts for."

### 2. Explain why the friction persists pre-singularity (referee comment 2)

**Where:** Section 2.3 (Incomplete Markets), after the paragraph on parameterizing $\alpha$.

Add a paragraph explaining why the friction is not arbitraged away despite large gains from trade:
- **Information asymmetry:** Private AI firms' value depends on proprietary technology that outsiders cannot evaluate — classic adverse selection.
- **Control and incentives:** AI owners retain private capital to preserve control over strategic technology; selling equity dilutes governance rights and may reduce innovation incentives.
- **Regulatory barriers:** Private placements, accredited investor requirements, and securities regulation limit household access to pre-IPO AI capital.
- **Contrast with GKP:** Acknowledge that GKP's friction is structurally permanent while ours is reducible — this is a feature, not a bug, because it generates the policy lever ($\alpha$) that GKP lacks.

### 3. Add references

Add bibliography entries for:
- Grace et al. (2024) — AI researcher surveys
- Eloundou et al. (2023) or similar — AI labor displacement estimates
- Any private AI capital valuation source used
