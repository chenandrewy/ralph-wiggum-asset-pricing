# tests/spec-economic.py
Started: 2026-04-12 20:12:03 EDT
Runtime: 2m 17s
[ralph-garage/agent-logs/20260412T201203.494318-0400_spec-economic_claude_opus.log](../ralph-garage/agent-logs/20260412T201203.494318-0400_spec-economic_claude_opus.log)

# spec-economic
VERDICT: PASS
REASON: All five economic concepts from the spec are used consistently with their definitions throughout the paper.

## Concepts Evaluated

The economic background spec defines five concepts with definitional constraints: (1) AI Singularity / Negative AI Singularity, (2) Budget Constraints, (3) Complete vs. Incomplete Markets, (4) Hedging, (5) General Equilibrium vs. Partial Equilibrium.

---

## 1. AI Singularity

**Spec definition:** "A sudden improvement in AI that vastly increases productivity and output." A negative AI singularity is "an AI singularity that is devastating for the typical investor."

**Paper usages:**

- **Introduction (line 49):** "We define a *negative* AI singularity as a sudden, dramatic improvement in AI productivity that displaces the typical investor's labor income and consumption." — Consistent with both parts of the spec definition.
- **Model Setup (line 87):** "Each period, with probability $p$, an AI singularity occurs." The non-extinction branch has "Aggregate consumption jumps by a factor $1 + \eta$" (sudden productivity increase) with displacement via $\phi$ (devastating for the household). — Consistent.
- **Extension 1 (line 200):** Introduces a "positive singularity" where the household's share increases, vs. "negative" (as in the baseline). The positive singularity still involves a productivity boost ($1+\eta$) but is not devastating for the household. — Consistent distinction.
- **Extinction sub-event (line 95):** The singularity triggers extinction with probability $\xi$: "$C_{t+1} = 0$." This is framed not as a separate concept but as a consequence of the same AI improvement event, following Jones (2024): "the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest." The AI improvement occurs; extinction is a possible outcome of it. — Consistent with the spec's intent; the "sudden improvement in AI" is the triggering event, and the paper is clear about what happens next.

**Cross-section consistency:** The term "singularity" carries the same meaning (sudden AI-driven productivity jump) across abstract, introduction, model, quantitative analysis, extensions, and conclusion. No drift.

---

## 2. Budget Constraints

**Spec definition:** "Budget constraints are satisfied. We instinctively look for violations of budget constraints, and treat violations as fundamental flaws."

**Paper usages:**

- **Assets (line 108):** "$D^{AI} + D^{N} = C_t$" — total public dividends equal aggregate consumption. Satisfied.
- **Consumption split (line 84):** Household gets $\alpha_t C_t$; AI owners get $(1 - \alpha_t) C_t$. These sum to $C_t$. Satisfied.
- **Government transfers (line 242):** The transfer equation taxes AI owners at rate $\tau$ on their surplus $(1 - \phi\alpha)(1+\eta)C_t(1+g)$, with deadweight loss $\delta\tau$ consuming part of the transfer. The household receives the net amount. The deadweight cost is explicitly accounted for as real resource loss. — Budget constraint satisfied; resources are conserved (output = household consumption + AI owner consumption + deadweight loss).

**Cross-section consistency:** No budget constraint violations identified anywhere in the paper.

---

## 3. Complete vs. Incomplete Markets

**Spec definition:** "Incomplete markets refers to the idea that some assets cannot be bought by the representative investor." Complete markets "does not necessarily refer to Arrow-Debreu securities. Discussions of complete markets should instead focus on the important assets that are unavailable to the representative investor."

**Paper usages:**

- **Abstract (line 32):** "markets are incomplete---investors cannot trade private AI capital" — Exactly the spec's framing: specific assets unavailable to the representative investor.
- **Model (line 110):** "The household *cannot* purchase these restricted shares. This is the source of market incompleteness: although the household can trade publicly listed AI stocks, it cannot access the full universe of AI equity." — Identifies the specific assets that are unavailable. Consistent.
- **Equilibrium (line 123):** "Because markets are incomplete, the household's stochastic discount factor (SDF) reflects its own consumption growth, not aggregate consumption growth." — Uses incompleteness to derive pricing implications. Consistent.
- **Extension 1 (line 206):** "Under complete markets, the household can trade the restricted AI equity---founder stakes, pre-IPO shares, and other claims currently unavailable---so that it fully hedges displacement risk." — Complete markets defined as the household gaining access to the specific assets it was previously excluded from. Consistent with spec's instruction to focus on "the important assets that are unavailable."
- **Discussion (line 169):** "If the household could trade the restricted equity, its effective displacement parameter would become $\phi_\text{eff} \to 1$: displacement is fully hedged." — Same framing.

**Arrow-Debreu:** The paper never mentions Arrow-Debreu securities anywhere. Consistent with spec's instruction.

**Cross-section consistency:** The meaning of incomplete markets (inability to trade restricted AI equity) is identical across abstract, model, discussion, extensions, and conclusion.

---

## 4. Hedging

**Spec definition:** "An asset 'hedges' a risk if its payoff tends to increase when that risk materializes. The hedge need not be perfect, and the asset need not earn a negative risk premium overall."

**Paper usages:**

- **Introduction (line 49):** "investors use AI stocks to partially insure against displacement from AI" — "partially" is consistent with "the hedge need not be perfect."
- **Model (line 153):** "AI stocks pay off precisely when the household's consumption falls, making them a partial hedge against displacement." — Payoff increases when risk materializes (displacement). Explicitly partial. Consistent.
- **Model (line 112):** "Holding AI stocks allows the household to smooth marginal utility across states---this is the hedging channel that inflates AI stock valuations---but does not eliminate displacement." — Acknowledges the hedge is imperfect. Consistent.
- **Abstract (line 32):** "investors use AI stocks to hedge against an AI singularity that displaces their consumption" — Uses "hedge" without "partial," but in context of the full abstract where "Markets are incomplete" is stated, this is not misleading.
- **Extension 2 (line 265):** "the hedge value of AI stocks becomes infinite---no finite price can compensate for the catastrophic displacement" — Uses "hedge value" to describe the extreme case. This still refers to payoffs increasing when risk materializes; the infinite price reflects extreme marginal utility, not a claim of perfect hedging. Consistent.

**Cross-section consistency:** Hedging consistently means "AI stocks' payoffs increase when displacement occurs" throughout. Never claimed to be perfect; never claimed to require negative risk premia.

---

## 5. General Equilibrium vs. Partial Equilibrium

**Spec definition:** "General equilibrium means that prices are determined by the equilibrium conditions. It does *not* mean that consumption is endogenous. Partial equilibrium means that prices are exogenous."

**Paper usages:** The paper never explicitly uses the terms "general equilibrium" or "partial equilibrium." The model determines prices through the Euler equation (equilibrium conditions), which is general equilibrium by the spec's definition. Consumption growth is exogenous ($g$ is a constant), which the spec explicitly says is compatible with general equilibrium. No inconsistency is possible since the terms are not invoked.

---

## Summary

All five concepts from the economic background spec are used consistently with their definitions. The paper's treatment of incomplete markets is particularly well-aligned with the spec's emphasis on specific unavailable assets rather than Arrow-Debreu framing. Hedging is always described as partial and payoff-based. Budget constraints are satisfied in every equation. The AI singularity definition is stable across all sections.
