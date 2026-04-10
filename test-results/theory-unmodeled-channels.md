# tests/theory-unmodeled-channels.py
Started: 2026-04-09 19:48:38 EDT
Runtime: 56s
[ralph-garage/agent-logs/20260409T194838.519907-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T194838.519907-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, using hedging language and explicit disclaimers throughout.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk** — Core mechanism. Household share drops by factor phi upon singularity.
2. **Market incompleteness** — Household cannot trade private AI capital. Drives the valuation spread.
3. **Extinction risk** — Probability xi of total loss upon singularity. Explicitly parameterized.
4. **Positive vs. negative singularity** — Extension 1 adds probability lambda of a positive singularity.
5. **Veto / blocking AI development** — Extension 1 models household's option to block development at cost kappa.
6. **Government transfers with deadweight costs** — Extension 2 models tax-and-transfer with waste parameter delta_0.

### Discussed but Not Modeled
7. **Entry dynamics / creative destruction by new cohorts (GKP2012)** — The paper explicitly disclaims: "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants" (Section 2.3).
8. **AI owners as future capital owners** — The paper says they "can also be thought of as future capital owners" but immediately adds: "Importantly, we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1).
9. **Continuous-time dynamics** — Acknowledged as abstracted away in conclusion.
10. **Heterogeneous beliefs** — Acknowledged as abstracted away in conclusion.
11. **Production-side details** — Acknowledged as abstracted away in conclusion.
12. **Cross-sectional return dispersion from technology shocks (Kogan & Papanikolaou 2014)** — Referenced in lit review without claiming to replicate.
13. **Creative destruction and inequality (KPSS 2020)** — Referenced in lit review without claiming to replicate.
14. **Empirical labor displacement premium (Knesl 2023)** — Referenced for empirical support, not as a modeled channel.
15. **AI regulation incentives** — Connected to veto result with appropriately soft language: "calls to slow or halt AI development *may partly reflect*..."

## Assessment of Caution

The paper demonstrates consistent caution across several dimensions:

- **Hedging language on main claims**: "Part of this premium, *we argue*, reflects a hedging motive" (Introduction). Uses "partial hedge," never "perfect hedge."
- **Explicit disclaimers for unmodeled features**: The GKP entry dynamics disclaimer appears twice (Sections 2.1 and 2.3), and both times is precise about what is and is not modeled.
- **Scope limitation in conclusion**: "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features... The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Modest contribution framing**: The paper characterizes its contribution relative to GKP as connecting existing insights to AI features, not as generating fundamentally new theory.
- **Quantitative humility**: Magnitudes are described as "broadly consistent" with data, not as calibrated fits.

No instance was found where the paper claims a result that relies on an unmodeled channel without appropriate qualification.
