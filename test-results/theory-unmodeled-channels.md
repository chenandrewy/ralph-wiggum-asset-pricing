# tests/theory-unmodeled-channels.py
Started: 2026-04-10 22:15:41 EDT
Runtime: 1m 1s
[ralph-garage/agent-logs/20260410T221541.753871-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260410T221541.753871-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper is consistently cautious about channels it does not explicitly model, clearly flagging approximations, abstracted mechanisms, and scope limitations.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk under incomplete markets** — Core mechanism. Household consumption share drops upon singularity; restricted AI equity cannot be traded.
2. **Extinction risk** — Parameter ξ captures probability of extinction conditional on singularity, following Jones (2024).
3. **Veto / blocking AI development** — Extension 1 models the household's option to block socially efficient AI development under incomplete markets.
4. **Government transfers with deadweight costs** — Extension 2 models tax-and-transfer with quadratic deadweight costs, showing how explosive singularity growth can overcome waste.

### Discussed but Not Explicitly Modeled
5. **Entry dynamics / creative destruction (GKP-style)** — The paper draws an analogy between AI owners and future entrants in GKP (2012) but explicitly disclaims modeling the entry mechanism.
6. **Wealth heterogeneity and attitudes toward AI risk** — Discussed as a "complementary channel" to Jones (2024)'s existential-risk mechanism, but not formally modeled with heterogeneous agents.
7. **Continuous-time dynamics, heterogeneous beliefs, production-side details** — Acknowledged as abstractions in the conclusion.
8. **Technology policy and labor market channels** — Mentioned in the introduction as the focus of other discussions; the paper focuses on financial markets instead.
9. **Financial market frictions beyond restricted ownership** — Illiquidity and other frictions are mentioned as motivation but reduced to a binary: the household either can or cannot trade restricted equity.

## Assessment of Caution

The paper handles unmodeled channels with consistent care:

- **GKP entry dynamics**: The paper says twice that it does not model entry dynamics: "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1) and "we do not model the entry dynamics that are central to their framework; the displacement in our model comes from the singularity's reallocation of consumption shares rather than from creative destruction by new entrants" (Section 2.3).
- **Scope hedging in claims**: The introduction uses careful language — "Part of this premium, we argue" and "AI stocks may have high valuations, in part" — rather than claiming the hedging channel is the sole driver.
- **Explicit abstraction acknowledgment**: The conclusion states "Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features that would enrich the analysis."
- **Modest contribution characterization**: The paper frames its contribution relative to GKP modestly, inheriting their "central economic logic" rather than claiming novelty on the core displacement-risk insight.
- **Closed-form approximation**: The paper flags that Proposition 1's closed form relies on an approximation (post-singularity P/D ≈ pre-singularity P/D), notes when this is exact vs. approximate, and reports numerically exact values in the table.
- **Wealth heterogeneity**: When connecting to Jones (2024)'s observation about wealth and AI attitudes, the paper frames it as a "complementary channel" rather than a modeled result.

No instance was found where the paper claims to model something it does not, or discusses an unmodeled channel without appropriate qualification.
