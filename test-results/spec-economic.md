# tests/spec-economic.py
Started: 2026-04-10 22:56:42 EDT
Runtime: 1m 59s
[ralph-garage/agent-logs/20260410T225642.498454-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260410T225642.498454-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all five concepts from the economic background spec consistently with their definitions throughout every section.

## Concept-by-Concept Analysis

### 1. AI Singularity / Negative AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**
- Abstract: "an AI singularity that displaces their consumption" — consistent; displacement of consumption is devastating for the typical investor.
- Section 1 (Introduction): "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — consistent with spec; combines the singularity definition (sudden improvement in productivity) with the negative qualifier (devastating for the typical investor via displacement).
- Section 2 (Model): Singularity modeled as aggregate consumption jumping by factor $1+\eta$ (productivity boost) with household share falling via $\phi$ — consistent; productivity rises vastly while the typical investor is displaced.
- Section 4.1 (Extension 1): Introduces a "positive singularity" where the household's share increases and a "negative" one as in the baseline. The positive singularity is still an AI singularity (productivity jumps by $1+\eta$) but is not devastating for the typical investor. The negative singularity retains its baseline meaning. — consistent; the positive/negative distinction turns on the effect on the typical investor, exactly as the spec implies.
- Section 5 (Conclusion): "an AI singularity that would displace their consumption" — consistent restatement.

**Cross-section consistency:** The term maintains the same economic meaning across all sections. The baseline model assumes all singularities are negative; Extension 1 introduces the positive case explicitly. No drift.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**
- Section 2.1: "Total public dividends equal aggregate consumption ($D^{AI} + D^N = C_t$)" — resource constraint is satisfied.
- Section 2.1: "The household receives a share $\alpha_t \in (0,1)$ of aggregate consumption... AI owners receive the remainder, $(1-\alpha_t)C_t$." — consumption shares sum to one.
- Section 2.1: AI dividend share $\theta_t$ and non-AI share $(1-\theta_t)$ sum to one.
- Section 4.2 (Transfers): Equation (6) shows household post-transfer consumption as displaced consumption plus net transfer (taxed from AI owners minus deadweight loss). The deadweight cost $\delta\tau$ is a real resource loss, not a budget violation. Total post-singularity resources: $(1+\eta)(1+g)C_t$, allocated to household consumption + AI owner consumption + deadweight loss. Budget satisfied.

**Cross-section consistency:** No violations detected. All resource and consumption allocations sum correctly throughout.

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**
- Abstract: "Because markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium." — defines incompleteness as inability to trade specific assets, consistent with spec.
- Section 1: "If markets were complete, investors could insure against this risk directly by trading the full universe of AI equity. But much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist." — focuses on specific unavailable assets, not Arrow-Debreu.
- Section 2.1: "The household *cannot* purchase these restricted shares. This is the source of market incompleteness." — explicitly identifies which assets are unavailable.
- Section 2.2: "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — consequence of incompleteness, consistent.
- Section 2.3: "the household's inability to trade restricted AI equity---is central. If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk." — complete markets defined by access to specific assets, not Arrow-Debreu.
- Section 4.1, Proposition 3(ii): "Under complete markets, the household can trade claims on private AI capital before the singularity." — complete markets means access to the specific important assets, exactly as the spec requires.

**Cross-section consistency:** The paper never invokes Arrow-Debreu securities. Every reference to complete/incomplete markets focuses on the representative investor's ability to trade specific AI equity. Fully consistent across all sections.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**
- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption" — AI stock payoffs increase when the singularity risk materializes (dividends grow via $\Gamma^{AI}$). Consistent.
- Section 1: "investors use AI stocks to partially insure against an AI singularity" — "partially" acknowledges imperfect hedge. Consistent.
- Section 2.2: "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — payoff increases when risk materializes; explicitly "partial." Consistent.
- Section 2.3: "growth stocks earn lower expected returns because they hedge displacement risk" — lower expected returns, not negative risk premiums. Consistent with spec's note that the asset need not earn a negative risk premium overall.
- Section 4.2: "transfers reduce the hedge value of AI stocks, compressing P/D ratios" — hedging demand drives valuations. Consistent.

**Cross-section consistency:** The paper consistently uses "hedge" and "partial hedge" to mean that AI stocks' payoffs tend to increase when displacement risk materializes. It never claims the hedge is perfect and never claims AI stocks earn negative risk premiums. Fully consistent.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**
- Section 1: "general-equilibrium model" used to describe \citet{GKP2012}. GKP2012 determines prices via equilibrium conditions, consistent with spec.
- The paper's own model determines prices via the household's Euler equation (an equilibrium condition). Consumption growth is exogenous (constant rate $g$ with stochastic singularity jumps). The paper does not explicitly label its own model as general or partial equilibrium, which avoids any potential confusion. Per the spec, the model could be called general equilibrium (prices are endogenous via equilibrium conditions) despite exogenous consumption—but the paper simply does not make a claim either way.

**Cross-section consistency:** The only use of "general equilibrium" is the correct reference to GKP2012. No misuse of the term to imply endogenous consumption. No conflation of partial equilibrium with the paper's own framework. Consistent.

## Summary

All five concepts from the economic background spec are used consistently with their definitions in every section of the paper. No inconsistencies, ambiguities that change economic meaning, or cross-section drift were found.
