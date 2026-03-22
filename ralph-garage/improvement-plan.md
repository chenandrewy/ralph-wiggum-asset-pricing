# Improvement Plan

## Current Status

- **spec-compliance**: PASS
- **theory-correctness**: FAIL — Proposition 5 proof error
- **referee-top3**: Two substantive comments

## Priority 1: Fix Proposition 5 (theory-correctness FAIL)

The test identified that the proof of Proposition 5(i) is incorrect. The claim is that $\Delta^{\text{hedge}} \to 0$ as $Y_O \to \infty$, but the proof says "$Y_O = \bar{Y}(1+\theta)$ suffices." With linear $Y_O$, the product $(1-\pi)(\theta+\phi)(J^{-\gamma}-1)$ converges to $-d/\bar{Y}$, not zero.

**Fix:** Replace the linear specification with a super-linear one. Specifically:

1. Change the proof of Part (i) to require $Y_O$ to grow faster than linearly in $\theta$ — e.g., state that $Y_O$ grows at least quadratically (or simply say "provided $Y_O$ grows faster than linearly in $\theta$").
2. In the proof of Part (ii), replace "$Y_O = \bar{Y}(1+\theta)$ suffices" with a correct sufficient condition, e.g., $Y_O = \bar{Y}(1+\theta)^k$ for $k > 1$.
3. Add a brief economic justification: super-linear scaling is natural if AI output exhibits increasing returns — the same accelerating-returns logic that motivates the singularity concept.

**Secondary issue (Part ii):** The test notes that for large $\theta$ (specifically $\theta > \phi(1-s)/s \approx 1.70$), the singularity becomes positive for the household ($J > 1$), so $J^{-\gamma} - 1 < 0$ and the hedging component turns negative. The "hump shape" description is incomplete — it rises, falls through zero, and becomes negative. Fix: acknowledge in the proposition statement or surrounding text that the hedging component eventually turns negative for very large $\theta$ (when the singularity ceases to be negative), reinforcing that hedging amplification is an intermediate-regime phenomenon.

## Priority 2: Referee Comments

### Comment 1 — AI owners as marginal investors in public AI stocks

The referee argues that AI insiders (founders, VCs) are large shareholders of public AI companies and would have low marginal utility in the singularity state, weakening the hedging premium.

**Fix:**
1. Add a paragraph in Section 2.3 (Incomplete Markets) or Section 3.2 explicitly acknowledging this tension.
2. Argue that insiders are primarily constrained sellers (lockups, diversification mandates, board restrictions) who set quantities not prices, and that after lockup expiration their holdings are small relative to total public float.
3. Add a simple robustness check: let a fraction $\eta$ of public AI shares be priced by AI owners (who have $J > 1$). Show the effective hedging amplifier becomes $(1-\eta)J^{-\gamma} + \eta J_O^{-\gamma}$ where $J_O > 1$, degrading the premium in $\eta$. Report a small table or inline calculation showing the premium remains substantial for moderate $\eta$.

### Comment 2 — Non-AI stock valuations rise with singularity risk

Table 1 shows non-AI P/D rises from 11.9 to 13.2 as $\lambda$ goes from 0 to 0.05. The referee notes this is a substantive, counterintuitive prediction the paper ignores.

**Fix:**
1. Add a paragraph in Section 3.2 or 3.4 discussing the level effects on both stock types. Explain: $J^{-\gamma}(1-\phi) > 1$ at baseline, so the marginal-utility surge dominates the dividend drop for non-AI stocks too.
2. Note the condition under which non-AI stocks *fall* with singularity risk: $J^{-\gamma}(1-\phi) < 1$, i.e., when the singularity is severe enough that even the SDF boost cannot overcome the dividend collapse.
3. Frame this as an additional testable implication: all stocks should appreciate when perceived singularity risk rises, but AI stocks more so. Contrast with standard rare-disaster models (Barro, Rietz) where disaster risk depresses all valuations.
4. Note that $v^A/v^N$ understates the absolute valuation effect on AI stocks since both numerator and denominator are moving.
