# tests/theory-intro-payoff.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 51s
[ralph-garage/agent-logs/20260409T212047.313691-0400_theory-intro-payoff_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.313691-0400_theory-intro-payoff_claude_opus.log)

# theory-intro-payoff
VERDICT: PASS
REASON: Every modeling feature in the paper connects to an economic result that is discussed in the introduction.

## Detailed Findings

### Modeling features and their introduction payoff

1. **Singularity with displacement (probability p, displacement φ)** → AI stocks serve as a hedge against displacement, commanding higher P/D ratios. **Intro ¶2** discusses this hedging motive explicitly.

2. **Market incompleteness (restricted AI equity)** → Investors cannot fully hedge displacement, forcing them into public AI stocks as an imperfect substitute. **Intro ¶2** explains this channel and the nature of the frictions (illiquidity, restricted ownership, non-existence of future capital).

3. **Two public assets (AI vs non-AI stocks with different dividend dynamics)** → Valuation spread between AI and non-AI stocks. **Intro ¶3** reports the quantitative P/D ratio predictions (roughly 6× at plausible parameters).

4. **Extinction risk (probability ξ)** → Attenuates the valuation gap by reducing the weight on non-extinction singularity states. **Intro ¶3** discusses this countervailing force explicitly, citing Jones (2024).

5. **Positive singularity and veto mechanism (Extension 1)** → Market incompleteness distorts the efficient development of AI; risk-averse households may block socially efficient AI. **Intro ¶4** discusses the veto distortion and connects it to AI regulation debates.

6. **Government transfers with deadweight costs (Extension 2)** → Transfers become compelling when singularity-driven explosive growth overwhelms deadweight costs. **Intro ¶5** explains this mechanism and its distinctive feature (same growth that makes displacement catastrophic makes transfers effective).

7. **CRRA preferences with γ > 1** → Standard modeling ingredient that drives the hedging demand and risk-aversion effects. Implicitly covered throughout the introduction's discussion of hedging and risk aversion.

### Conclusion

All modeling features serve a clear economic purpose and each corresponding economic result appears in the introduction. There is no "orphan" modeling feature that lacks an introduction payoff, and no introduction claim that lacks a modeling counterpart.
