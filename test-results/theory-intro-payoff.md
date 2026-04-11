# tests/theory-intro-payoff.py
Started: 2026-04-11 16:10:24 EDT
Runtime: 1m 5s
[ralph-garage/agent-logs/20260411T161024.924237-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260411T161024.924237-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature leads to an economic result that is discussed in the introduction.

## Detailed Mapping

### Modeling Features → Introduction Payoffs

1. **Singularity probability $p$, displacement $\phi$, productivity boost $\eta$**: The introduction explains that investors use AI stocks to hedge against displacement from an AI singularity, and that P/D ratios for AI stocks can reach roughly twice those of non-AI stocks (paragraphs 2–3). These parameters drive the hedging channel and the closed-form P/D ratios of Proposition 1.

2. **Market incompleteness (restricted AI equity, AI owners)**: The introduction identifies market incompleteness as "the key driver" — investors cannot trade restricted equity (founder stakes, pre-IPO shares, future innovators' capital), forcing them into public AI stocks as a partial hedge. It notes that under complete markets the premium would largely vanish (paragraph 4).

3. **Extinction probability $\xi$**: The introduction discusses extinction risk as a force that "attenuates the hedging channel," because states powerful enough for enormous growth also carry existential risk, reducing the weight on non-extinction states where hedging demand operates (paragraph 4, referencing Proposition 2).

4. **Positive singularity probability $q$ and veto cost $\kappa$**: The introduction explains that a risk-averse household unable to hedge displacement may rationally block AI development even when the positive singularity is more likely, and that complete markets would eliminate this distortion (paragraph 5, referencing Proposition 3).

5. **Government transfers $\tau$ and deadweight cost $\delta$**: The introduction argues that fiscal policy can substitute for missing markets when singularity-driven growth is large enough to overwhelm deadweight costs (paragraph 7).

6. **CRRA preferences with risk aversion $\gamma > 1$**: Risk aversion is embedded throughout the introduction's discussion — it is what makes the household's marginal utility high in displacement states, driving the hedging channel, and what makes sufficiently risk-averse households prefer the veto.

7. **AI dividend share $\theta$ and expansion $\Delta\theta$**: The introduction discusses AI stocks growing "as a share of the economy with each singularity, making them a partial hedge" (paragraph 3), which is the role of $\theta$ and $\Delta\theta$.

8. **Two public assets (AI stocks vs. non-AI stocks)**: The valuation spread between these two asset classes is the paper's central empirical prediction, discussed prominently in the introduction (paragraphs 2–3).

### Summary

The introduction presents three linked results — (1) hedging-based AI valuation premia, (2) resistance to AI development from market incompleteness, and (3) government transfers enabled by explosive growth — and every model parameter contributes to at least one of these results. No modeling feature is introduced without a corresponding economic payoff in the introduction.
