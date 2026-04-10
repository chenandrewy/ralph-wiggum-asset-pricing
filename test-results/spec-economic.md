# tests/spec-economic.py
Started: 2026-04-09 21:06:08 EDT
Runtime: 1m 50s
[ralph-garage/agent-logs/20260409T210608.976934-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T210608.976934-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "devastating for the typical investor."

**Paper usages:**

- Abstract: "AI singularity that displaces their consumption"
- Introduction (Section 1): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption"
- Model (Section 2): "Each period, with probability $p$, an AI singularity occurs... Aggregate consumption jumps by a factor $1 + \eta$ (where $\eta > 0$ captures the productivity boost), but the household's share drops"
- Extension 1 (Section 4.1): Introduces a positive singularity where the household's share increases, contrasted with the negative singularity from the baseline.
- Conclusion (Section 5): "an AI singularity that would displace their consumption"

**Assessment:** Consistent. The paper defines the singularity as a sudden event that vastly increases aggregate output (η > 0), matching the spec. The baseline singularity is negative (devastating for the household: consumption falls by 25–50% depending on calibration), matching the spec's "negative AI singularity." Extension 1's positive singularity is an AI singularity that benefits the typical investor, providing a natural complement. The term is used with the same meaning across all sections.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- Model (Section 2): Household consumption is $\alpha_t C_t$, AI owners receive $(1 - \alpha_t) C_t$. These shares sum to 1, satisfying the aggregate resource constraint.
- Assets: AI stocks pay $\theta_t C_t$, non-AI stocks pay $(1 - \theta_t) C_t$. Dividends sum to $C_t$.
- Extension 2 (Section 4.2): Post-transfer consumption: the transfer takes $\tau$ from AI owners' surplus and delivers $\tau(1 - \delta\tau)$ to the household, with $\delta\tau$ lost to deadweight costs. The total post-singularity consumption plus deadweight loss sums correctly.

**Assessment:** Consistent. No budget constraint violations detected. Consumption shares sum to 1 in all states. Dividend shares sum to aggregate consumption. Transfer accounting in Extension 2 is internally consistent with explicit deadweight loss.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- Abstract: "markets are incomplete---investors cannot trade private AI capital---AI stocks command a premium"
- Introduction (Section 1): "If markets were complete, investors could insure against this risk directly by trading claims on AI capital. But much of this capital is private, held by founders and early-stage investors in firms that may not yet exist."
- Model (Section 2): "There is also private AI capital, held by AI owners... The household cannot trade this private capital. This is the source of market incompleteness."
- Discussion (Section 2.3): "The market incompleteness in our model---the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk, and the valuation spread would collapse."
- Extension 1 (Section 4.1): "Under complete markets, the household can trade claims on private AI capital before the singularity."
- Extension 2 (Section 4.2): "the displacing capital may not yet exist---it belongs to future cohorts of innovators---and government transfers offer an alternative"

**Assessment:** Consistent. Every reference to market incompleteness focuses on specific important assets unavailable to the representative investor (private AI capital), exactly as the spec prescribes. No reference to Arrow-Debreu securities. Complete markets is consistently defined as the ability to trade claims on AI capital. This usage is uniform across all sections.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- Abstract: "investors use AI stocks to hedge against an AI singularity that displaces their consumption"
- Introduction (Section 1): "AI stocks serve as a hedge against a risk that most investors cannot diversify away"
- Introduction (Section 1): "AI stocks grow as a share of the economy with each singularity, making them a partial hedge"
- Model (Section 2): "AI stocks' payoffs are especially valuable... This is the hedging channel: AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Discussion (Section 2.3): "growth stocks earn lower expected returns because they hedge displacement risk from innovation" (describing GKP)
- Extension 2 (Section 4.2): "transfers reduce the hedge value of AI stocks"

**Assessment:** Consistent. AI stock dividends grow by $\Gamma^{AI}(1+g)$ upon singularity, exceeding normal-state growth of $(1+g)$—the payoff increases when the displacement risk materializes. The paper consistently calls this a "partial hedge," acknowledging imperfection (extinction states produce zero payoff; private capital is not fully replicated). The paper never claims AI stocks earn a negative risk premium; the high P/D ratio reflects high price, not a claim about the sign of the overall risk premium. All usages match the spec.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- Introduction (Section 1): "general-equilibrium model in which innovation displaces existing agents and creates a systematic risk factor under incomplete markets" (describing GKP2012)
- The paper's own model determines prices endogenously via the household's Euler equation (Proposition 1), making it general equilibrium by the spec's definition.
- Consumption shares ($\alpha_t$, $\theta_t$) are governed by exogenous parameters ($\phi$, $\Delta\theta$) rather than being endogenously determined by production. The paper does not claim this makes the model partial equilibrium.

**Assessment:** Consistent. The paper correctly labels GKP as "general-equilibrium" (prices are determined by equilibrium conditions in their model). The paper's own model has prices determined by the Euler equation, consistent with GE. Importantly, the paper never conflates general equilibrium with endogenous consumption—consumption shares are exogenous parameters, and this is not treated as a deviation from general equilibrium. The paper does not use the term "partial equilibrium" anywhere.

---

## Cross-Section Consistency Check

All five concepts maintain their definitions across:
- **Abstract → Introduction:** Singularity, hedging, and market incompleteness carry the same meaning.
- **Introduction → Model:** Informal descriptions in the introduction are formalized in the model with no drift in meaning.
- **Model → Extensions:** The same definitions of singularity, hedging, and incomplete markets carry through to the veto and transfer analyses.
- **Model → Conclusion:** The conclusion restates the mechanisms using the same terminology with no ambiguity.
- **Main text → Appendix:** The proof uses the same framework without redefining terms.

No inconsistencies, ambiguities that change economic meaning, or cross-section drift detected.
