# Notes: Jones (2024) — "The AI Dilemma: Growth versus Existential Risk"

**Citation:** Jones, Charles I. 2024. "The AI Dilemma: Growth versus Existential Risk." *AER: Insights* 6(4): 575–590. https://doi.org/10.1257/aeri.20230570

---

## Core Question

When is it optimal to continue advancing AI vs. shut it down, given that AI simultaneously raises living standards and poses existential risk?

---

## Simple Model (Section II)

The simple model is essentially static. AI use of intensity $T$ raises consumption to $c = c_0 e^{gT}$ but humanity survives only with probability $S(T) = e^{-\delta T}$. All growth and risk are realized immediately; if humanity survives, people consume the constant $c$ forever after.

The planner chooses $T$ to maximize:
$$EU = e^{-\delta T} \cdot \frac{1}{\rho} N u(c_0 e^{gT})$$

The FOC says: use AI as long as the marginal benefit (growth $g$) exceeds the marginal cost (flow extinction probability $\delta$ times the value of life):
$$\delta \cdot v(c) \le g, \quad \text{where} \quad v(c) \equiv \frac{u(c)}{u'(c)c}$$

At the optimum:
$$v(c^*) = \frac{g}{\delta}$$

The function $v(c)$ is the value of a year of life measured as a multiple of consumption. Using VSL $\approx$ \$10M for a 40-year-old with 40 years to live, and consumption $\approx$ \$40K, Jones calibrates $v(c_\text{US,today}) \approx 6$.

### CRRA utility and the role of $\gamma$

With $u(c) = \bar{u} + \frac{c^{1-\gamma}}{1-\gamma}$:
$$v(c) = \bar{u} c^{\gamma-1} + \frac{1}{1-\gamma}$$

- **Log utility ($\gamma = 1$):** $v(c) = \bar{u} + \log c$ rises slowly. With $\delta = 1\%$, optimal to run AI for $T^* = 40$ years, accepting a 1-in-3 extinction probability, for a 55x consumption increase. But at $\delta = 2\%$, optimal use is zero immediately — very sensitive.
- **$\gamma = 2$:** $v(c)$ rises linearly in $c$. With $\delta = 1\%$: only 4.5 years, 4% extinction risk, 57% consumption increase.
- **$\gamma = 3$:** Roughly halves these values again.

The key economic force: when $\gamma > 1$, utility is bounded above at $\bar{u}$, so the marginal value of extra consumption falls rapidly and life becomes increasingly valuable relative to more consumption.

### Heterogeneity

Poor people have lower $v(c)$ and would be more willing to accept existential risk for higher growth. The same applies to people with low $\gamma$ (perhaps tech entrepreneurs).

---

## Richer Model (Section III): Singularities and Mortality

The richer model differs from the simple model in several important ways:
1. **Dynamic structure:** Overlapping generations with social discounting $\rho_s$, private discounting $\rho$, population growth $b$, and mortality $m$.
2. **One-shot existential risk:** Instead of a flow hazard $\delta$ over $T$ periods, the planner faces a single probability $\delta$ of extinction at the moment AI is adopted — no interior choice of intensity.
3. **Singularity:** Consumption can be *infinite* (not just high growth). With $\gamma > 1$, utility is bounded, so even infinite consumption delivers only finite utility $\bar{u}$.
4. **Mortality improvements:** AI may also reduce the mortality rate $m$.
5. **The decision variable is different:** Rather than choosing $T^*$, the planner simply adopts or does not adopt AI. The key output is $\delta^*$, the maximum tolerable one-time existential risk.

### Setup

Social welfare:
$$W = \int_0^\infty e^{-\rho_s t} N_t U_t \, dt$$

where $N_t = N_0 e^{bt}$ and expected lifetime utility of a cohort-$t$ individual is:
$$U_t = \int_0^\infty e^{-(\rho + m)a} u(c_{t+a}) \, da$$

Substituting CRRA utility with $\gamma > 1$ and constant consumption growth:
$$W(g, m) = \frac{N_0 \bar{u}}{(\rho + m)(\rho_s - b)} + \frac{N_0 c_0^{1-\gamma}}{1-\gamma} \cdot \frac{1}{(\rho + m + (\gamma-1)g)(\rho_s - b + (\gamma-1)g)}$$

Adopt AI iff $W(g_0, m_0) < (1 - \delta) W(g_\text{ai}, m_\text{ai})$. The cutoff:
$$\delta^* = \frac{W(g_\text{ai}, m_\text{ai}) - W(g_0, m_0)}{W(g_\text{ai}, m_\text{ai})}$$

### Key results

**Singularity without mortality improvement.** When $g_\text{ai} = \infty$ and $m_\text{ai} = m_0$:
- $\gamma \le 1$: $\delta^* = 1$ — any risk short of certain extinction is acceptable. (Jones finds this unappealing.)
- $\gamma = 2$: $\delta^* = 2.4\%$ — barely higher than the 2.2% cutoff with $g_\text{ai} = 10\%$. Infinite consumption adds almost nothing because utility is bounded.
- $\gamma = 3$: $\delta^* = 0.5\%$.

**Mortality improvements are the key exception.** If AI also halves mortality ($m_\text{ai} = 0.5\%$ vs. $m_0 = 1\%$, i.e., life expectancy doubles from 100 to 200 years):
- $\gamma = 2$: $\delta^*$ jumps from 2.2% to **26.7%**.
- $\gamma = 3$: $\delta^*$ jumps from 0.5% to **25.4%**.

The economic intuition: mortality reductions are "in the same units" as existential risk. Consumption must pass through a bounded utility function and faces severe diminishing returns. But living longer directly offsets the risk of dying, without diminishing returns of the same kind.

**Near-zero social discounting ($\rho_s \to 0$).** Without mortality gains, $\delta^* \to 0$ (infinite undiscounted future at stake). But *with* mortality improvements, the cutoff stays around 25%, because future generations also benefit from longer lives. Closed-form in the limit:
$$\delta^* = \frac{1/2}{\rho \cdot LE + 1}$$
With $\rho = 0.01$, $LE = 100$: $\delta^* = 1/4$.

---

## Key Assumptions: Valuing Life

### Individual level

The value of life $v(c)$ is calibrated from the VSL, which is estimated from compensating differentials in the labor market (e.g., how much extra wage a construction worker demands for higher mortality risk). This tells us how an individual values marginal changes in mortality risk given their consumption level.

Jones argues that this marginal VSL is exactly the right object for the simple model: all $N$ identical people face the same trade-off between existential risk and higher consumption, so the representative person's marginal willingness to trade mortality risk for consumption is directly informative.

One caveat Jones raises: the VSL may *overstate* existential risk costs. Standard VSLs embed the suffering of surviving family members, but with extinction no one remains to suffer. This suggests the effective value-of-life number for existential risk could be lower, making the risk more worth bearing.

### Aggregate level: total utilitarianism

At the aggregate level, social welfare simply adds up lifetime utilities across all people who might live:
$$W = \int_0^\infty e^{-\rho_s t} N_t U_t \, dt$$

This total utilitarian approach has two important features:
1. **Linearity in lives:** The planner treats "10% of the population dies each period" as equivalent to "there is a 10% chance of human extinction," because only total utils matter. Jones acknowledges that many people's instincts reject this equivalence, which would push toward more conservative cutoffs.
2. **Future people count:** The framework captures the logic that trillions of future people might not get to live. It values them precisely as they would value living their own lives. Jones cites Kuruc, Budolfson, and Spears (2022) for axiomatic justification of this additive structure.

### What the framework cannot capture

Jones acknowledges that ending all human life may not be properly measured by extrapolating from the value of ending a single person's life. The total utilitarian perspective is a natural starting point, but there may be something beyond the sum of individual losses — an additional moral weight to extinction itself — that this framework misses. The modeling also does not capture potential non-utilitarian concerns (e.g., that the *irreversibility* of extinction makes it categorically different from ordinary mortality risk).

---

## Summary of the Two Pivotal Forces

1. **Risk aversion $\gamma$:** Log utility is too permissive; $\gamma \ge 2$ makes the planner very conservative about existential risk because utility is bounded and consumption gains have sharply diminishing value.
2. **Mortality improvements:** The one force that can justify large existential risk even with high $\gamma$ and low discounting, because longer life and extinction risk trade off directly without passing through diminishing marginal utility of consumption.

---

## Relation to Our Paper

- Jones assumes a representative agent who uniformly benefits from AI-driven consumption growth. Our paper considers the case where AI owners gain dramatically while the representative household may suffer — incomplete markets prevent sharing the gains.
- Jones's singularity: everyone gets infinite consumption. Our singularity: AI owners get enormous gains but the representative investor cannot access AI equity, so the gains are unshared.
- If AI owners have infinite consumption, it seems obviously optimal to share it. Even with frictions preventing that sharing, infinite consumption could be spent to overcome the friction. This is a useful point to make in passing.
- Jones does not consider that a portion of the population can suffer greatly from the singularity. One could enrich Jones with such modeling, but the result is very different from our hedging paper.
- The paper is better positioned as connecting GKP to Korinek and Suh, with Jones as context for the existential-risk literature rather than as the primary comparison.
