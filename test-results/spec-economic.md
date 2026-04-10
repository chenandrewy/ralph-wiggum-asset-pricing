# tests/spec-economic.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 1m 44s
[ralph-garage/agent-logs/20260409T203927.591980-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T203927.591980-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usages:**
- Introduction (line 49): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption." Matches "sudden improvement" and "vastly increases productivity."
- Model (line 89–98): Singularity modeled as a discrete event with probability $p$; non-extinction singularity jumps aggregate consumption by $1+\eta$. Matches "vastly increases productivity and output."
- Extension 1 (line 201): Introduces "positive" and "negative" singularities explicitly. The negative singularity has $\alpha_{t+1} = \phi \alpha_t$ (household's share drops), consistent with "devastating for the typical investor."
- Baseline singularity always displaces the household; calibration gives $\phi(1+\eta) = 0.75$, a 25% consumption drop—devastating. Consistent.

**Assessment:** Consistent across all sections.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations."

**Paper usages:**
- Model (line 86): Household gets $\alpha_t C_t$; AI owners get $(1-\alpha_t) C_t$. Shares sum to 1.
- Model (line 106–108): AI stock dividends $\theta_t C_t$ and non-AI stock dividends $(1-\theta_t) C_t$ sum to $C_t$.
- Transfer equation (line 227): Post-transfer consumption accounts for the full AI surplus, with deadweight costs reducing the transferred amount but not creating resources from nothing.

**Assessment:** No budget-constraint violations detected. Consumption shares and dividend shares each sum to their respective totals throughout.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Abstract (line 32): "markets are incomplete---investors cannot trade private AI capital." Focuses on the specific unavailable asset, not Arrow-Debreu.
- Model (line 110–111): "The household cannot trade this private capital. This is the source of market incompleteness." Directly identifies the unavailable asset.
- Model (line 120–121): "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." Consequence of incompleteness, consistent framing.
- Discussion (line 171–172): "If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk, and the valuation spread would collapse." Complete-markets counterfactual focuses on the specific asset.
- Extension 1 (line 215): "Under complete markets, the household can trade claims on private AI capital before the singularity." Again focuses on the specific unavailable asset.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu and always frames (in)completeness in terms of the specific asset the representative investor cannot trade.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Introduction (line 49): "AI stocks serve as a hedge against a risk... the risk that an AI singularity... displaces their labor income and consumption." The risk is displacement; AI stock dividends grow upon singularity ($\Gamma^{AI} > 1+\eta$), so payoff increases when risk materializes.
- Model (line 149): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." "Partial hedge" is consistent with "need not be perfect."
- Discussion (line 170): "growth stocks earn lower expected returns because they hedge displacement risk." Lower expected returns (not negative risk premium overall)—consistent with the spec.
- Abstract (line 32): "investors use AI stocks to hedge against an AI singularity." Same meaning throughout.
- Conclusion (line 260): "investors use AI stocks to partially insure against an AI singularity." "Partially insure" = partial hedge. Consistent.

**Assessment:** Consistent. The paper always uses "hedge" to mean payoff increases when displacement materializes, explicitly notes it is partial (imperfect), and never claims AI stocks earn a negative risk premium overall.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**
- Literature review (line 64): Refers to GKP's "general-equilibrium model." GKP determines prices via equilibrium conditions—correct usage.
- The paper's own model: Prices are determined by the household's Euler equation (line 271–275), an equilibrium condition. Consumption is exogenous (grows at rate $g$ with stochastic singularity shocks). This is general equilibrium per the spec: prices endogenous, consumption exogenous. The paper does not label its own model "general equilibrium" explicitly, but importantly it does not mischaracterize it as partial equilibrium either.
- The paper never equates general equilibrium with endogenous consumption.

**Assessment:** Consistent. The only explicit use of "general-equilibrium" (describing GKP) is correct. The paper's own model fits the spec's GE definition and is never mislabeled.

## Cross-Section Consistency

All five concepts maintain their economic meaning across the introduction, model, quantitative analysis, extensions, conclusion, and appendix. No term drifts in meaning or is used ambiguously in a way that changes its economic content.
