# tests/theory-unmodeled-channels.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 1m 10s
[ralph-garage/agent-logs/20260412T201203.513282-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.513282-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently and explicitly disclaims channels it does not model, including entry dynamics, continuous-time dynamics, heterogeneous beliefs, and production-side details.

## Channels Explicitly Modeled

1. **Hedging channel / displacement risk premium** — AI stocks pay off when household consumption falls (share drops by φ), creating a valuation premium via the SDF. Fully captured in Proposition 1 with closed-form P/D ratios.
2. **Market incompleteness** — Household cannot trade restricted AI equity (founder stakes, pre-IPO shares). Modeled as separation between household consumption share α and AI dividend share θ.
3. **Extinction risk attenuation** — Probability ξ of extinction reduces valuation premium by shrinking the weight on non-extinction singularity states. Modeled and proved in Proposition 2.
4. **Veto / development distortion** — Risk-averse household may block socially efficient AI development under incomplete markets. Modeled in Extension 1 (Proposition 3), with positive singularity probability q and veto cost κ.
5. **Government transfers with deadweight costs** — Tax τ on AI owners with waste parameter δ. Modeled in Extension 2 via effective displacement parameter φ_eff.

## Channels Discussed but NOT Explicitly Modeled

1. **Entry dynamics / creative destruction by new cohorts (GKP 2012)** — The paper discusses the analogy between AI owners and future capital owners who have not yet entered the economy.
   - **Caution check:** Explicitly disclaimed twice. Line 75: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism." Line 169: "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants." Both disclaimers are clear and prominent.

2. **Continuous-time dynamics** — Mentioned in the conclusion as an abstraction.
   - **Caution check:** Conclusion (line 283): "It abstracts from continuous-time dynamics..." Acknowledged openly.

3. **Heterogeneous beliefs** — Mentioned in the conclusion as abstracted away.
   - **Caution check:** Same conclusion sentence. Acknowledged.

4. **Production-side details** — Mentioned in the conclusion.
   - **Caution check:** Same conclusion sentence. Acknowledged.

5. **Bequests and intergenerational gifts** — Mentioned as a GKP mechanism that could attenuate displacement (dynasty with altruistic bequests makes displacement factor equal to one).
   - **Caution check:** Discussed as a GKP observation (line 237), clearly attributed rather than claimed as the paper's own result. Not presented as if modeled.

6. **Broader AI equity trading as ideal solution** — Discussed as the natural market fix for incompleteness.
   - **Caution check:** Explicitly noted as infeasible: "the natural fix—broader trading of AI equity—is blocked by restricted ownership and non-existent future capital" (line 55). The paper does not pretend to model this solution.

7. **Jones (2024) preference channels** — Jones identifies two channels (risk aversion toward existential gambles; high-consumption agents valuing current living standards). The paper discusses these as complementary to its own displacement channel.
   - **Caution check:** Line 231 frames these as "complementary" and clearly attributes them to Jones rather than claiming the paper captures them: "Our model offers a complementary channel through financial markets rather than existential risk."

## Additional Caution Markers

- **Empirical mapping:** The paper explicitly flags the imperfect mapping from NASDAQ/S&P 500 to model AI/non-AI stocks (line 189): "The mapping...is imperfect: the NASDAQ is broader than 'AI stocks,' return differences partly reflect earnings growth rather than valuation multiples, and the S&P 500 itself has substantial AI exposure."
- **Closed-form approximation:** Lines 151 and 314 explicitly note that the closed form relies on an approximation (post-singularity P/D ≈ pre-singularity P/D) and when it becomes less accurate.
- **Transfer approximation:** Line 253 notes φ_eff is computed at α_0 for simplicity.
- **GKP attribution:** The paper is careful and modest about its contribution relative to GKP: "The main insights about displacement risk and incomplete markets originate in their work" (line 64).
- **Scope:** The conclusion states the goal is "not to provide a definitive account of AI stock valuations but to highlight a specific channel" (line 283).

## Summary

Every channel that is discussed but not explicitly modeled is accompanied by a clear disclaimer or attribution. The paper never allows the reader to believe it formally captures something it does not. The two most important disclaimers—about GKP entry dynamics—appear twice each in prominent locations (model setup and discussion). The conclusion provides a blanket acknowledgment of abstractions. The paper's tone throughout is modest and careful about scope.
