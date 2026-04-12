# tests/spec-economic.py
Started: 2026-04-11 21:43:22 EDT
Runtime: 2m 4s
[ralph-garage/agent-logs/20260411T214322.784500-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260411T214322.784500-0400_spec-economic_claude_opus.log)

# spec-economic

VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output."

**Paper usages:**

- Abstract: "an AI singularity that displaces their consumption"
- Introduction (line 48): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption."
- Model (line 90–93): "Each period, with probability $p$, an AI singularity occurs... Aggregate consumption jumps by a factor $1 + \eta$ (where $\eta > 0$ captures the productivity boost)"
- Extension 1 (line 204): positive and negative singularity variants, both involving the productivity jump $1 + \eta$.

**Assessment:** Consistent. The paper's singularity is sudden (discrete, single-period), increases productivity ($\eta > 0$), and increases aggregate output. The productivity jump is the definitional core across all sections; displacement and extinction are layered consequences, not redefinitions of the singularity itself.

### 2. Negative AI Singularity

**Spec definition:** "An AI singularity that is devastating for the typical investor."

**Paper usages:**

- Introduction (line 48): "a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption"
- Model (line 96–97): household's share drops to $\phi \alpha_t$ with $\phi \in (0,1)$, so household consumption falls even as aggregate consumption rises.
- Extension 1 (line 204): "negative (probability $1-q$, as in the baseline), with the household's share falling to $\alpha_{t+1} = \phi \alpha_t$"
- Quantitative Analysis (line 188): calibration gives $\phi(1+\eta) = 0.75$, a 25% consumption drop; large singularity gives $\phi(1+\eta) = 0.5$, a 50% drop.

**Assessment:** Consistent. The paper's negative singularity is devastating for the typical investor (household consumption falls 25–50% at baseline/large calibrations). The term keeps the same meaning across model, extensions, and quantitative sections.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor." Complete markets does NOT necessarily refer to Arrow-Debreu securities. Discussions should "focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital"
- Introduction (line 52): "Under complete markets the displacement-driven premium would largely vanish, because the household could trade the restricted AI equity directly; market incompleteness is the key driver."
- Model (line 113): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness."
- Model discussion (line 172): "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged"
- Extension 1 (line 210): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable"
- Extension 2 (line 237): "The ideal solution---broader trading of AI capital---faces the same constraint GKP identify: much of the displacing capital does not yet exist."

**Assessment:** Consistent. Every mention of incomplete markets focuses on specific unavailable assets (restricted equity, founder stakes, pre-IPO shares, future innovators' capital). Complete markets is defined as the household being able to trade these specific assets. Arrow-Debreu securities are never mentioned. The usage matches the spec's instruction to focus on "the important assets that are unavailable to the representative investor."

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract: "investors use AI stocks to hedge against an AI singularity"
- Introduction (line 48): "investors use AI stocks to partially insure against displacement from AI"
- Model (line 107–108): AI dividend share $\theta_t$ increases upon singularity ($\Delta\theta > 0$), so AI stock dividends rise when displacement occurs.
- Model (line 156): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Model discussion (line 115): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement"
- Extension 2 (line 269): "transfers reduce the hedge value of AI stocks"

**Assessment:** Consistent. The paper describes AI stocks as a "partial hedge" throughout, matching the spec's allowance that "the hedge need not be perfect." The payoff mechanism (AI dividends rise when displacement occurs) matches the spec's definition (payoff increases when the risk materializes). The paper never claims AI stocks are a perfect hedge or that they earn negative risk premia.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = "prices are determined by the equilibrium conditions," NOT that consumption is endogenous. Partial equilibrium = "prices are exogenous."

**Paper usages:** The terms "general equilibrium" and "partial equilibrium" do not appear in the paper.

**Assessment:** No inconsistency possible since the terms are not used. The paper's model is general equilibrium by the spec's definition (prices are determined by the Euler equation, not exogenous), and consumption growth is exogenous ($g$ is constant), which is consistent with the spec's clarification that GE does not require endogenous consumption.

### 6. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:** The term "budget constraint" does not appear, but the model's resource accounting is internally consistent:

- Total public dividends equal aggregate consumption: $D^{AI} + D^{N} = C_t$ (line 111).
- The household receives $\alpha_t C_t$; AI owners receive $(1 - \alpha_t) C_t$ (line 87).
- Shares sum to one by construction.
- Transfer equation (line 246–247): transfers are levied on AI owners' surplus and delivered (net of deadweight loss) to the household; total post-transfer consumption is less than or equal to aggregate consumption (the deadweight loss is a resource drain, not a violation).

**Assessment:** No violations detected. The resource accounting is internally consistent across all sections.

## Cross-Section Consistency Check

All five substantive economic concepts maintain the same meaning across:
- Abstract
- Introduction
- Model setup and discussion
- Quantitative analysis
- Extensions (veto and transfers)
- Conclusion
- Appendix (proof)

No term drifts in meaning, acquires an incompatible secondary definition, or contradicts its spec definition in any section.
