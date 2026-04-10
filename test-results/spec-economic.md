# tests/spec-economic.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 1m 49s
[ralph-garage/agent-logs/20260409T212047.313513-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.313513-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the spec consistently with their definitions across all sections.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usage:**
- Abstract: "AI singularity that displaces their consumption"
- Introduction (line 49): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption"
- Model (Section 2, para "Singularity"): probability $p$ event where "aggregate consumption jumps by a factor $1 + \eta$" but "the household's share drops" — a sudden improvement in output that is devastating for the household
- Extension 1 (Section 4.1): distinguishes "positive" singularity (household's share increases) from "negative" (household's share falls, as in baseline), consistent with the spec's "negative AI singularity" being devastating for the typical investor

**Assessment:** Consistent. The singularity is always defined as a sudden productivity/output improvement. The baseline singularity is negative for the typical investor (household) through displacement. The extension explicitly labels positive vs. negative cases, matching the spec's definitions.

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usage:**
- The model's consumption accounting is $c_t^H = \alpha_t C_t$ for the household and $(1-\alpha_t) C_t$ for AI owners — these sum to $C_t$, satisfying the aggregate budget constraint.
- Dividends: $D_t^{AI} = \theta_t C_t$ and $D_t^{N} = (1-\theta_t) C_t$ — sum to $C_t$, consistent.
- Transfer equation (Section 4.2): household receives $\tau(1-\delta\tau)$ of the AI surplus, with deadweight loss $\delta\tau$ explicitly accounted for — no resources appear from nowhere.

**Assessment:** Consistent. Budget constraints are satisfied throughout; consumption shares and dividend shares each sum to their respective aggregates.

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets means "some assets cannot be bought by the representative investor" — focus on important unavailable assets, not Arrow-Debreu securities. Complete markets similarly should focus on unavailable assets, not Arrow-Debreu.

**Paper usage:**
- Abstract: "markets are incomplete---investors cannot trade private AI capital"
- Introduction: "much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist"
- Model (Section 2.1): "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household *cannot* purchase these restricted shares. This is the source of market incompleteness"
- Discussion (Section 2.3): "If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk, and the valuation spread would collapse"
- Extension 1: "Under complete markets, the household can trade claims on private AI capital before the singularity"

**Assessment:** Consistent. Every discussion of market completeness/incompleteness focuses on specific unavailable assets (restricted AI equity), never on Arrow-Debreu securities. The framing matches the spec precisely.

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usage:**
- Introduction: "AI stocks serve as a *hedge* against a risk that most investors cannot diversify away"
- Model (Section 2.2): "AI stocks' payoffs are especially valuable [in singularity states], pushing their P/D ratio above that of non-AI stocks. This is the hedging channel: AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- Discussion (Section 2.3): "growth stocks earn lower expected returns because they hedge displacement risk from innovation"
- Extension 2 (Section 4.2): "transfers reduce the hedge value of AI stocks"
- Conclusion: "investors use AI stocks to partially insure against an AI singularity"

**Assessment:** Consistent. AI stock dividends literally increase upon singularity ($\Gamma^{AI} > 1+\eta$), so their payoffs increase when displacement risk materializes — matching the spec's definition. The paper consistently describes the hedge as "partial" or "imperfect," consistent with "need not be perfect." No passage claims or implies a negative risk premium is required for hedging.

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium means prices are determined by equilibrium conditions, **not** that consumption is endogenous. Partial equilibrium means prices are exogenous.

**Paper usage:**
- Literature review: "general-equilibrium model" referring to GKP2012, "who develop a general-equilibrium model in which innovation displaces existing agents"
- The paper's own model determines prices endogenously through the household's Euler equation (Proposition 1, Appendix A) — prices are equilibrium outcomes, making it general equilibrium by the spec's definition
- Consumption in the model is exogenous: aggregate consumption grows at rate $g$, and shares are determined by the singularity mechanism. The paper never conflates general equilibrium with endogenous consumption.

**Assessment:** Consistent. The paper treats general equilibrium as price determination through equilibrium conditions (Euler equation), never as requiring endogenous consumption. Consumption is explicitly exogenous (fixed growth rate $g$, mechanistic share displacement), and this is not presented as undermining the equilibrium nature of the model.

## Cross-Section Consistency Check

All five concepts maintain stable meanings across:
- **Abstract → Introduction → Model → Extensions → Conclusion:** No definitional drift detected.
- **Formal model vs. rhetorical/intuitive discussions:** The informal language in the introduction and discussion sections matches the formal definitions in the model section.
- **Literature review references:** When citing GKP2012 and Jones2024, the paper uses the spec-defined terms consistently with how they are used in the paper's own framework.
