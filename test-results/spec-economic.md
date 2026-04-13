# tests/spec-economic.py
Started: 2026-04-12 20:26:02 EDT
Runtime: 2m 12s
[ralph-garage/agent-logs/20260412T202602.588995-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T202602.588995-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the background spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usage:**
- Introduction (P2): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Matches spec exactly.
- Model (Section 2.1): "Each period, with probability $p$, an AI singularity occurs." The singularity produces a productivity boost $\eta > 0$ (aggregate consumption jumps by $1+\eta$), consistent with "vastly increases productivity and output."
- The baseline singularity is negative: household share drops to $\phi \alpha_t$ with $\phi(1+\eta) < 1$, so household consumption falls — "devastating for the typical investor."
- Extension 1 introduces a positive singularity (household share increases), using "AI singularity" as the general term and "negative/positive" as qualifiers. Consistent with the spec's neutral base definition.

**Verdict:** Consistent across all sections.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations."

**Paper usage:**
- Model (Section 2.1): "Total public dividends equal aggregate consumption ($D^{AI} + D^{N} = C_t$)." The household receives $\alpha_t C_t$; AI owners receive $(1 - \alpha_t) C_t$. Shares sum to 1.
- Transfer equation (Section 4.2): $c^H_{post} = \phi\alpha(1+\eta)C_t(1+g) + \tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$. Verifying: household consumption + AI owner consumption + deadweight loss = $[\phi\alpha + \tau(1-\delta\tau)(1-\phi\alpha) + (1-\tau)(1-\phi\alpha) + \delta\tau^2(1-\phi\alpha)] \times (1+\eta)C_t(1+g) = (1+\eta)C_t(1+g)$. Budget constraint satisfied.

**Verdict:** No violations found.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = "some assets cannot be bought by the representative investor," e.g., privately-held AI firms. Does NOT necessarily refer to Arrow-Debreu securities. Complete markets should focus on "important assets that are unavailable to the representative investor."

**Paper usage:**
- Abstract: "markets are incomplete---investors cannot trade private AI capital." Matches spec definition precisely.
- Model (Section 2.1): "The household *cannot* purchase these restricted shares. This is the source of market incompleteness: although the household can trade publicly listed AI stocks, it cannot access the full universe of AI equity." Focuses on specific unavailable assets, not Arrow-Debreu.
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$." Consistent.
- Extension 1 (Section 4.1): "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." Defines completeness via availability of specific assets, as spec requires.
- Extension 2 (Section 4.2): "the household's inability to trade restricted AI equity" — same framing throughout.
- No reference to Arrow-Debreu securities anywhere in the paper.

**Verdict:** Consistent across all sections. Correctly avoids Arrow-Debreu framing.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**
- Introduction (P2): "investors use AI stocks to partially insure against displacement from AI." Uses "partially" — consistent with "need not be perfect."
- Model (Section 2.1): "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." Explicitly notes the hedge is imperfect.
- Model (Section 2.2): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." Payoff increases when risk materializes — matches spec definition exactly.
- The paper never claims AI stocks earn a negative risk premium overall; it discusses higher P/D ratios (implying lower expected returns than they would have under complete markets), which is consistent with the spec's note that "the asset need not earn a negative risk premium overall."

**Verdict:** Consistent across all sections.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** GE = "prices determined by equilibrium conditions," NOT "consumption is endogenous." PE = "prices are exogenous."

**Paper usage:**
- The paper does not use the terms "general equilibrium" or "partial equilibrium" anywhere.
- The model's prices are determined endogenously by the household's Euler equation (equilibrium condition), which would make it GE by the spec's definition if the paper chose to label it.
- Consumption growth is exogenous (deterministic $g$ plus stochastic singularity shocks), which is consistent with GE under the spec's definition (GE does not require endogenous consumption).
- No inconsistency arises because the paper avoids GE/PE labeling entirely.

**Verdict:** No usage to evaluate; no inconsistency.

## Cross-Section Consistency Check

All five concepts maintain the same economic meaning across:
- **Abstract** and **Introduction**: Framing language matches formal definitions.
- **Model** (Section 2): Formal definitions established.
- **Discussion** (Section 2.3): Restatements match formal definitions.
- **Quantitative Analysis** (Section 3): Empirical discussion consistent with model definitions.
- **Extensions** (Section 4): Terms carry the same meaning when applied to veto and transfer settings.
- **Conclusion** (Section 5): Summary language matches prior usage.
- **Appendix**: Technical derivations consistent with model setup.

No cross-section drift or ambiguity that changes economic meaning was found.
