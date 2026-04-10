# tests/theory-unmodeled-channels.py
Started: 2026-04-09 21:50:56 EDT
Runtime: 56s
[ralph-garage/agent-logs/20260409T215056.127691-0400_theory-unmodeled-channels_claude_opus.log](../ralph-garage/agent-logs/20260409T215056.127691-0400_theory-unmodeled-channels_claude_opus.log)

# theory-unmodeled-channels
VERDICT: PASS
REASON: The paper consistently uses cautious language ("in part," "may partly," "we do not explicitly model") when discussing channels it does not formally capture.

## Channels and Modeling Status

### Explicitly Modeled
1. **Hedging motive / displacement risk**: Core model. Household share drops by phi upon singularity; AI stocks provide partial hedge. Fully formalized in Propositions 1-2.
2. **Market incompleteness (restricted AI equity)**: Household cannot trade private AI capital. Modeled as a constraint on the household's asset menu.
3. **Extinction risk**: Probability xi of extinction conditional on singularity. Formally incorporated in the pricing equations.
4. **Veto / blocking AI development**: Extension 1. Household can block socially efficient AI development under incomplete markets. Proposition 3.
5. **Government transfers with deadweight costs**: Extension 2. Tax rate tau on AI owners, deadweight fraction delta*tau. Closed-form effective displacement parameter phi_eff.
6. **Positive singularity**: Extension 1. Household share can increase, making development socially efficient.

### Discussed but Not Modeled
1. **Entry dynamics / new cohorts of firms (GKP)**: The paper draws an analogy to GKP's overlapping-generations entry dynamics but explicitly disclaims modeling them: "we do not explicitly model the entry of new cohorts of firms or workers; AI owners are a static group whose share changes only through the singularity mechanism" (Section 2.1) and "we do not model the entry dynamics that are central to their framework" (Section 2.3).
2. **Creative destruction**: Referenced as GKP's mechanism but clearly distinguished: "GKP model continuous displacement from expanding technological variety, while we model a sudden, severe shift" (Section 2.3).
3. **Financial market hedging instruments**: Mentioned as a potential but friction-limited channel ("Financial markets could in principle provide hedging instruments, but frictions---illiquidity, restricted ownership, the non-existence of future capital---limit their effectiveness"). Stated as background motivation, not as a model result.
4. **Heterogeneous beliefs, continuous-time dynamics, production-side details**: Acknowledged in the conclusion as abstractions ("Our model is deliberately simple. It abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details, and many other features").
5. **Technology policy and labor market channels**: Mentioned in the introduction as the focus of other discussions, not claimed as part of this paper's contribution.

## Caution Assessment

The paper is consistently cautious about unmodeled channels:

- **Hedging language for the main claim**: "Part of this premium, we argue, reflects a hedging motive" -- does not overclaim that hedging explains all of the valuation gap.
- **Explicit disclaimers on entry dynamics**: Two separate passages (Sections 2.1 and 2.3) warn the reader that GKP-style entry is not modeled, directly following the spec's instruction not to let the reader think entry is modeled.
- **Policy conclusions hedged**: "calls to slow or halt AI development may partly reflect investors' inability to share in its upside" (uses "may partly"); "contingent transfer policies ... may be worth designing in advance" (uses "may be worth").
- **Conclusion is forthright about scope**: Explicitly lists what the model abstracts from and states "The goal is not to provide a definitive account of AI stock valuations but to highlight a specific channel."
- **Modest characterization of GKP contribution**: The paper credits GKP for the central economic logic and frames its own contribution as applying and extending GKP's insight to the AI singularity setting.

No instance was found where the paper discusses an unmodeled channel as though it were a formal result of the model.
