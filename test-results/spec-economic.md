# tests/spec-economic.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 1m 41s
[ralph-garage/agent-logs/20260409T202148.491513-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.491513-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concepts Evaluated

### 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." Negative AI singularity: "devastating for the typical investor."

**Paper usages (consistent throughout):**

- Abstract: "an AI singularity that displaces their consumption"
- Introduction (line 50): "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption"
- Model (line 90): "Each period, with probability $p$, an AI singularity occurs." Defined with productivity boost $\eta > 0$ and displacement $\phi < 1$.
- Extension 1 (line 213--214): Positive singularity = household share increases; negative singularity = "the household's share falls, $\alpha_{t+1} = \phi \alpha_t$ with $\phi < 1$" --- labeled "negative (as in the baseline)."
- Extension 2 (line 258): Large singularity with $\eta = 9$ and $\phi = 0.05$ described as "catastrophe" for the household.

**Assessment:** The paper consistently defines the singularity as a sudden productivity event ($\eta > 0$) with displacement consequences. The negative singularity is consistently framed as harmful to the household (consumption drops), matching the spec's "devastating for the typical investor." The positive singularity in Extension 1 is a natural complement (household benefits) and does not contradict the spec. No cross-section drift.

---

### 2. Budget Constraints

**Spec definition:** Budget constraints must be satisfied; violations are fundamental flaws.

**Paper usages:**

- Model (line 87--88): Household receives $\alpha_t C_t$; AI owners receive $(1 - \alpha_t) C_t$. Shares sum to 1.
- Model (line 107--109): AI stock dividends $\theta_t C_t$ plus non-AI stock dividends $(1 - \theta_t) C_t$ sum to $C_t$.
- Model (line 111): Private AI capital dividends are the residual $(1 - \alpha_t) C_t - D_t^{AI}$, ensuring all consumption is accounted for.
- Extension 2 (line 243--244): Transfer equation accounts for displaced consumption plus net transfer minus deadweight costs.

**Assessment:** All consumption shares and dividend shares sum correctly. No budget-constraint violations detected anywhere in the paper.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** Incomplete markets = some assets cannot be bought by the representative investor (e.g., privately-held AI firms). Does NOT necessarily refer to Arrow-Debreu securities. Complete markets should focus on important assets unavailable to the representative investor.

**Paper usages (consistent throughout):**

- Abstract (line 33): "markets are incomplete---investors cannot trade private AI capital"
- Introduction (line 50--51): "If markets were complete, investors could insure against this risk directly by trading claims on AI capital. But much of this capital is private"
- Model (line 111): "The household cannot trade this private capital. This is the source of market incompleteness"
- Discussion (line 181): "The market incompleteness in our model---the household's inability to trade private AI capital---is central. If the household could buy claims on the full AI surplus, it could perfectly hedge displacement risk"
- Extension 1 (line 224--225): "Under incomplete markets and for $\gamma$ sufficiently large, the household vetoes AI development"
- Extension 1 (line 231): "Under complete markets, the household can trade claims on private AI capital before the singularity"
- Conclusion (line 276): "the inability to trade private AI capital"

**Assessment:** Every instance defines incomplete markets as the inability to trade private AI capital, and complete markets as the ability to trade those claims. No reference to Arrow-Debreu securities anywhere. Fully consistent with the spec's framing across all sections.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages (consistent throughout):**

- Introduction (line 50): "AI stocks serve as a hedge against a risk that most investors cannot diversify away"
- Introduction (line 54): "AI stocks grow as a share of the economy with each singularity, making them a partial hedge"
- Model (line 150): "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement"
- Model discussion (line 150): AI stocks' payoffs increase in singularity states ($\Gamma^{AI} > 1 + \eta$), which is when the risk materializes.
- Lit review (line 65): "growth stocks provide a partial hedge" (describing GKP2012)
- Extension 2 (line 260): "transfers reduce the hedge value of AI stocks"
- Conclusion (line 276): "investors use AI stocks to partially insure against an AI singularity"

**Assessment:** The paper consistently uses "hedge" and "partial hedge" to describe an asset whose payoff increases when the hedged risk materializes (singularity displaces household consumption, AI dividends rise). The paper never claims AI stocks are a perfect hedge or earn negative risk premiums. The usage matches the spec definition exactly.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** General equilibrium = prices determined by equilibrium conditions (NOT that consumption is endogenous). Partial equilibrium = prices exogenous.

**Paper usages:**

- Lit review (line 65): GKP2012 described as having a "general-equilibrium model in which innovation displaces existing agents and creates a systematic risk factor under incomplete markets."
- Model (line 122): "The household prices all publicly traded assets via its Euler equation." Prices are endogenous, determined by the household's optimization.
- Appendix (line 287--291): Euler equation derivation shows prices determined by equilibrium conditions.

**Assessment:** The paper's own model has prices determined endogenously through the Euler equation (general equilibrium per the spec). The paper does not claim consumption is endogenous as a feature of general equilibrium. The reference to GKP2012 as "general-equilibrium" is appropriate. No misuse of general vs. partial equilibrium terminology.

---

## Summary

All five concepts from the economic background spec are used consistently across every section of the paper (Abstract, Introduction, Model, Quantitative Analysis, Extensions, Conclusion, Appendix). No definitional drift, no ambiguity that changes economic meaning, and no inconsistencies detected.
