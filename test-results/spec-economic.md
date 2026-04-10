# tests/spec-economic.py
Started: 2026-04-09 21:34:52 EDT
Runtime: 1m 38s
[ralph-garage/agent-logs/20260409T213452.252126-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260409T213452.252126-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: The paper uses all economic concepts from the background spec consistently with their definitions throughout every section.

## Concept-by-Concept Analysis

### 1. AI Singularity

**Spec definition:** "An AI singularity is a sudden improvement in AI that vastly increases productivity and output. A negative AI singularity is an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Abstract:** "an AI singularity that displaces their consumption"
- **Introduction (Section 1):** "an AI singularity---a sudden, dramatic improvement in AI productivity---displaces their labor income and consumption"
- **Model (Section 2.1):** "Each period, with probability $p$, an AI singularity occurs." The singularity produces a productivity boost ($\eta > 0$) and displacement ($\phi < 1$), with household consumption falling even as aggregate output rises.
- **Extension 1 (Section 4.1):** Introduces positive vs. negative singularity. The negative singularity has "$\alpha_{t+1} = \phi \alpha_t$" (household share falls), while the positive one has the share rising. Under the baseline calibration ($\phi = 0.5$, $\eta = 0.5$), the household loses 25% of consumption; under the large singularity ($\phi = 0.05$, $\eta = 9$), the paper describes a "catastrophe."

**Assessment:** Consistent. The singularity is always modeled as a sudden, discrete productivity jump (matching "sudden improvement"). The negative singularity is devastating for the household (the typical/representative investor) through displacement. The term is used uniformly across all sections.

---

### 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Model (Section 2.1):** Household receives $\alpha_t C_t$; AI owners receive $(1 - \alpha_t) C_t$. These sum to $C_t$. Dividends: $D_t^{AI} = \theta_t C_t$ and $D_t^{N} = (1 - \theta_t) C_t$, summing to $C_t$.
- **Extension 2 (Section 4.2):** Transfer equation (9) explicitly accounts for the household's displaced consumption plus the net transfer (after deadweight costs). The deadweight cost $\delta\tau$ is a real resource loss, not a budget violation.

**Assessment:** Consistent. All consumption shares sum to the aggregate. Dividend claims exhaust aggregate consumption. Transfer mechanics are resource-consistent. No budget constraint violations.

---

### 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor... Incomplete markets does not necessarily refer to Arrow-Debreu securities... Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Abstract:** "markets are incomplete---investors cannot trade private AI capital"
- **Introduction (Section 1):** "much of this equity is restricted---held by founders, early-stage investors, and firms that may not yet exist. Financial markets could in principle provide hedging instruments, but frictions---illiquidity, restricted ownership, the non-existence of future capital---limit their effectiveness. This market incompleteness forces investors into publicly traded AI stocks as an imperfect substitute."
- **Model (Section 2.1):** "AI owners also hold restricted equity---founder stakes, pre-IPO shares, and other claims on AI firms that are not available for public trading. The household cannot purchase these restricted shares. This is the source of market incompleteness."
- **Equilibrium Prices (Section 2.2):** "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth."
- **Discussion (Section 2.3):** "The market incompleteness in our model---the household's inability to trade restricted AI equity---is central. If the household could buy claims on the full universe of AI shares, it could perfectly hedge displacement risk."
- **Extension 1 (Section 4.1):** "Under complete markets, the household can trade claims on private AI capital before the singularity."

**Assessment:** Consistent. Every usage frames incomplete markets as the representative investor's inability to buy specific important assets (restricted AI equity). Complete markets are framed as the ability to trade those same assets. No reference to Arrow-Debreu securities. The framing focuses precisely on "important assets that are unavailable to the representative investor," as the spec requires.

---

### 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Introduction (Section 1):** "AI stocks serve as a hedge against a risk that most investors cannot diversify away"
- **Introduction (Section 1):** "growth stocks provide a partial hedge" (describing GKP)
- **Equilibrium Prices (Section 2.2):** "AI stocks' payoffs are especially valuable, pushing their P/D ratio above that of non-AI stocks. This is the hedging channel: AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement."
- **Discussion (Section 2.3):** "growth stocks earn lower expected returns because they hedge displacement risk from innovation" (describing GKP)
- **Extension 2 (Section 4.2):** "transfers reduce the hedge value of AI stocks, compressing P/D ratios"
- **Conclusion (Section 5):** "investors use AI stocks to partially insure against an AI singularity"

**Assessment:** Consistent. Every usage defines hedging as the asset paying off when the risk materializes (singularity/displacement), matching the spec exactly. The paper repeatedly qualifies the hedge as "partial" or "imperfect," never requiring perfection. The lower expected returns mentioned for growth stocks (GKP) are consistent with the spec's note that the asset "need not earn a negative risk premium overall"---the paper does not claim AI stocks must earn negative premia.

---

### 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does not mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:**

- **Introduction (Section 1):** Describes GKP2012 as "a general-equilibrium model in which innovation displaces existing agents"
- **Model (Section 2.2):** "The household prices all publicly traded assets via its Euler equation." Prices are determined endogenously through equilibrium conditions (the Euler equation), not assumed exogenously.

**Assessment:** Consistent. The paper's own model determines prices through equilibrium (Euler equation), consistent with general equilibrium per the spec. Consumption growth is partly exogenous (rate $g$) and partly endogenous (singularity shifts shares), but the spec explicitly states that GE does not require endogenous consumption. The reference to GKP as "general-equilibrium" is appropriate since their model also determines prices endogenously. The paper never claims that general equilibrium requires endogenous consumption.

---

## Cross-Section Consistency Check

Each term maintains the same economic meaning across all sections:

| Concept | Abstract | Intro | Model | Extensions | Conclusion | Appendix |
|---------|----------|-------|-------|------------|------------|----------|
| AI singularity | Consistent | Consistent | Consistent | Consistent | Consistent | Consistent |
| Budget constraints | N/A | N/A | Satisfied | Satisfied | N/A | Satisfied |
| Incomplete markets | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| Hedging | Consistent | Consistent | Consistent | Consistent | Consistent | N/A |
| GE/PE | N/A | Consistent | Consistent | N/A | N/A | N/A |

No cross-section drift, definitional ambiguity, or inconsistency detected.
