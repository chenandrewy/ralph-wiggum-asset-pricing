# tests/spec-economic.py
Started: 2026-04-09 20:07:38 EDT
Runtime: 2m 1s
[ralph-garage/agent-logs/20260409T200738.682299-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T200738.682299-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper, with only minor observations that do not change economic meaning.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- Abstract: "an AI singularity that displaces their consumption" -- shorthand that describes the consequence rather than re-stating the definition, but does not contradict it.
- Introduction (Section 1): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption" -- directly consistent with the spec definition.
- Model (Section 2.1): "Each period, with probability $p$, an AI singularity occurs." The non-extinction branch has "Aggregate consumption jumps by a factor $1 + \eta$ (where $\eta > 0$ captures the productivity boost)" -- consistent: the singularity produces a sudden productivity improvement.
- Extension 1 (Section 4.1): Introduces "positive singularity" (household's share increases) and "negative singularity" (household's share falls, $\phi < 1$). The negative singularity is devastating for the typical investor (the household), matching the spec.
- Extinction branch: The singularity event can lead to extinction ($C_{t+1} = 0$). The paper frames this as: "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest." The singularity is still about AI becoming suddenly powerful (consistent with spec); extinction is a conditional outcome of that power. This is a reasonable modeling extension of the spec's definition rather than a contradiction.

**Assessment:** Consistent. The paper's core definition aligns with the spec. The extinction branch extends the concept but is clearly motivated and does not redefine the singularity itself.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (Section 2.1): Household receives $\alpha_t C_t$, AI owners receive $(1 - \alpha_t) C_t$. These sum to $C_t$. Dividends: AI stocks pay $\theta_t C_t$, non-AI stocks pay $(1 - \theta_t) C_t$, private AI capital pays $(1 - \alpha_t) C_t - \theta_t C_t$. The constraint $\alpha_t \in (0, 1 - \theta_t]$ ensures the household share plus public AI dividend share does not exceed one. All shares sum correctly.
- Extension 2 (Section 4.2): Transfer consumption equation (eq. 6) adds the displaced household consumption and the net transfer (taxed AI surplus minus deadweight). The AI surplus is $(1 - \phi\alpha)(1+\eta)(1+g)C_t$, which is the AI owners' share after displacement. The transfer takes $\tau$ of this and delivers $(1 - \delta\tau)$ of what's taken. Budget arithmetic is consistent.

**Assessment:** Consistent. No budget constraint violations detected.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities. Complete markets also does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital" -- directly matches the spec: identifies the specific asset the representative investor cannot buy.
- Introduction: "If markets were complete, investors could insure against this risk directly by trading claims on AI capital. But much of this capital is private, held by founders and early-stage investors in firms that may not yet exist." -- focuses on the specific unavailable asset, not Arrow-Debreu.
- Model (Section 2.1): "The household cannot trade this private capital. This is the source of market incompleteness: the household cannot directly hedge displacement by buying claims on the full AI surplus." -- identifies the specific asset.
- Discussion (Section 2.3): "If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk, and the valuation spread would collapse." -- frames completeness in terms of the specific missing asset.
- Extension 1 (Section 4.1): "Under complete markets, the household can trade claims on private AI capital before the singularity." -- again, specific asset, no Arrow-Debreu.
- Conclusion: "the inability to trade private AI capital" -- consistent.

**Assessment:** Consistent. The paper never invokes Arrow-Debreu securities and consistently frames market (in)completeness in terms of the specific asset unavailable to the representative investor, exactly as the spec requires.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Introduction: "AI stocks serve as a hedge against a risk that most investors cannot diversify away" -- consistent.
- Introduction: "publicly traded AI stocks as an imperfect substitute" -- consistent with "need not be perfect."
- Model (Section 2.2): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." The mechanism: $\Gamma^{AI} > 1 + \eta$, so AI stocks' dividends grow faster than aggregate consumption in the singularity state, which is when the household's consumption falls. Payoff increases when the risk materializes. Consistent.
- Introduction: "a discrete singularity with severe displacement, which sharpens the hedging channel" -- refers to the mechanism by which AI stocks hedge, consistent.
- Quantitative Analysis (Section 3): "the household values the hedge more as the risk it hedges against becomes more likely" -- consistent usage.
- Extension 2 (Section 4.2): "transfers reduce the hedge value of AI stocks, compressing P/D ratios" -- transfers reduce displacement, so the hedging motive weakens. Logically consistent.
- Conclusion: "investors use AI stocks to partially insure against an AI singularity" -- "partially insure" is consistent with "need not be perfect."

**Assessment:** Consistent. The paper uses "hedge" and "partial hedge" throughout in a manner that matches the spec definition. AI stocks' payoffs increase when displacement risk materializes, and the paper never claims the hedge is perfect or that AI stocks earn a negative risk premium.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Literature review: "general-equilibrium model" referring to GKP2012 -- GKP2012 determines prices via equilibrium conditions, consistent with the spec definition.
- The paper's own model determines prices via the household's Euler equation (an equilibrium condition). The paper does not explicitly label itself as general or partial equilibrium. Consumption is exogenous (determined by share $\alpha_t$ and exogenous growth $g$), and prices are endogenous (determined by the Euler equation). Under the spec's definition, this would qualify as general equilibrium. The paper's choice not to label itself avoids any potential confusion.

**Assessment:** Consistent. The one explicit use of "general equilibrium" (referring to GKP2012) matches the spec. The paper does not misapply the GE/PE distinction.

---

## Cross-Section Consistency Check

The key terms -- singularity, hedging, market incompleteness, displacement -- maintain the same economic meaning across the abstract, introduction, model, quantitative analysis, extensions, and conclusion. No drift in definitions detected.

## Summary

All five concepts from the economic background spec are used consistently with their definitions in every section of the paper. The paper avoids the specific pitfalls flagged in the spec (Arrow-Debreu framing of market completeness, conflating GE with endogenous consumption). Terminology is stable across sections and rhetorical contexts.
