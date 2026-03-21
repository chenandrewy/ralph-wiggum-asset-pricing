# Gârleanu, Kogan & Panageas (2012) — "Displacement Risk and Asset Returns"

**Working paper version. Published in _JFE_ 2012.**

---

## Core Idea

Innovation displaces older firms and erodes older workers' human capital. Because future innovators cannot trade with current agents (they don't exist yet), this **displacement risk** cannot be insured away. It is a systematic, priced risk factor distinct from aggregate consumption risk.

---

## Model Setup

- Discrete, infinite-time OLG economy; population normalized to 1; birth/death rate $\lambda$
- Two agent types: **workers** (fraction $1-\phi$) and **entrepreneurs** (fraction $\phi$)
- Two shocks: TFP shock $\varepsilon_t \sim N(0,\sigma^2)$ and innovation shock $u_t \sim \text{Gamma}(k,\nu)$

### Preferences (Abel 1990 "keeping-up-with-the-Joneses")

$$E_s \sum_{t=s}^{\infty} \left[(1-\lambda)\beta\right]^{t-s} \frac{\left(c_{t,s}^\psi \left(\frac{c_{t,s}}{C_t}\right)^{1-\psi}\right)^{1-\gamma}}{1-\gamma} \tag{2}$$

When $\psi=1$: standard CRRA. Parameter $\psi \in [0,1]$ controls weight on own vs. relative consumption.

### Production

Final good firm uses labor and a continuum of intermediates:

$$Y_t = Z_t \left(L_t^F\right)^{1-\alpha} \left[\int_0^{A_t} \omega_{j,t} (x_{j,t})^\alpha \, dj\right] \tag{3}$$

where $\omega_{j,t} = (j/A_t)^{\chi(1-\alpha)}$ gives newer goods higher weight ($\chi \geq 0$).

**TFP process:**

$$\log Z_{t+1} = \log Z_t + \mu + \varepsilon_{t+1} \tag{4}$$

**Innovation (variety expansion):**

$$\log A_{t+1} = \log A_t + u_{t+1} \tag{9}$$

### Gamma-Distributed Innovation Shocks

The innovation increment $u_{t+1}$ is i.i.d. **Gamma distributed** with shape parameter $k$ and scale parameter $\nu$, so that $f(x) \propto x^{k-1} e^{-x/\nu}$ (footnote 4 in the paper). The Gamma assumption serves several purposes:

1. **Positivity.** Innovation only expands the variety set ($u_{t+1} > 0$), so the shock must have non-negative support — ruling out the normal distribution.
2. **Flexible skewness and tail weight.** The Gamma family nests thin-tailed (large $k$, small $\nu$) and heavy-tailed / right-skewed (small $k$, large $\nu$) specifications. By choosing $k$ and $\nu$, the model can generate occasional large bursts of innovation — episodes in which many new varieties arrive simultaneously and a large fraction of incumbent firms' profits is destroyed.
3. **Tail risk as disaster risk.** Large realizations of $u_{t+1}$ act like *displacement disasters* for existing agents: they sharply erode the value of assets in place (eq. 34, $\partial R^a/\partial u < 0$) and depreciate older workers' human capital (eq. 10, $\log q$ falls by $\rho u$). Because the displacement factor $\upsilon(u_{t+1})$ in the SDF (eq. 25) is a non-linear, decreasing function of $u_{t+1}$, these rare large shocks receive disproportionate pricing weight — exactly the mechanism emphasized in the disaster-risk literature (Rietz 1988; Barro 2006). The Gamma's ability to put meaningful probability mass on extreme innovation episodes is therefore what allows the model to generate a sizeable equity premium and value premium without requiring implausibly high risk aversion.

### Displacement of Workers

A worker born at $s$ has efficiency units that depreciate with innovation:

$$\log q_{t+1,s} = \log q_{t,s} - \rho u_{t+1} \tag{10}$$

Parameter $\rho \geq 0$ controls the severity of skill obsolescence.

---

## Key Equilibrium Results

### Proposition 1 — Output, Profits, Wages

Aggregate output:
$$Y_t = \frac{(\alpha^2)^\alpha \left(\frac{1-\alpha}{1+\chi}\right)^{1-\alpha}}{\alpha^2 + 1 - \alpha} (1-\phi) Z_t A_t^{1-\alpha} \tag{19}$$

Profits of intermediate good $j$:
$$\pi^I_{j,t} = (1+\chi)\left(\frac{j}{A_t}\right)^\chi \frac{Y_t}{A_t} \alpha(1-\alpha) \tag{20}$$

Key implication: $\pi^I_{j,t}/Y_t \to 0$ as $t \to \infty$ (individual firm profits not cointegrated with output).

---

## The Stochastic Discount Factor

### Equation (24) — The Core Result

$$\frac{\xi_{t+1}}{\xi_t} = \beta \left(\frac{Y_{t+1}}{Y_t}\right)^{-1+\psi(1-\gamma)} \left[\frac{1}{1-\lambda}\left(1 - \lambda\sum_{i\in\{w,e\}} \phi^i \frac{c^i_{t+1,t+1}}{Y_{t+1}}\right)\right]^{-\gamma} \tag{24}$$

The second bracketed term is the **displacement factor** $\upsilon(u_{t+1})/(1-\lambda)$: it captures existing agents' consumption growth net of the share claimed by the newly born generation.

This can be written explicitly as:

$$\upsilon(u_{t+1}) \equiv 1 - \theta^e \alpha(1-\alpha)\left[\kappa\left(1 - e^{-(1+\chi)u_{t+1}}\right) + (1-\varpi)\theta^g\right] - \theta^w(\alpha^2+1-\alpha)\left[1-(1-\lambda)(1+\delta)e^{-\rho u_{t+1}}\right] \tag{25}$$

**Why the CCAPM fails:** The SDF depends on *existing* agents' consumption growth, not aggregate consumption growth. The wedge is stochastic and driven by $u_{t+1}$.

---

## Value vs. Growth Stock Returns (Lemma 2)

Any stock's gross return decomposes as:

$$R_{t+1} = (1 - w^o_t) R^a_{t+1} + w^o_t R^o_{t+1} \tag{33}$$

where:
- $R^a_{t+1}$ = return on **assets in place** (value stock return)
- $R^o_{t+1}$ = return on **growth opportunities**
- $w^o_t = 0$ for value firms; $w^o_t \in (0,1)$ for growth firms

Crucially:
$$\frac{\partial R^a_{t+1}}{\partial u_{t+1}} < 0, \qquad \frac{\partial R^o_{t+1}}{\partial u_{t+1}} > 0 \tag{34}$$

Innovation shocks hurt assets in place but benefit growth options. Since the displacement factor commands a **positive price of risk**, value stocks earn higher average returns than growth stocks.

---

## Three Empirical Implications

### 1. Value Premium
Growth firms hedge displacement risk → lower required returns. Value–growth return spread = compensation for displacement risk exposure.

### 2. High Equity Premium
Existing firms' dividends have high exposure to $u_t$ (not cointegrated with consumption), amplifying risk beyond what aggregate consumption volatility alone implies.

Back-of-envelope (eq. 41):
$$\Delta\log\xi_{t+1} + \text{const} = \underbrace{(\psi(1-\gamma)-1)\varepsilon_{t+1}}_{\text{std dev: } 0.18} + \underbrace{(\psi(1-\gamma)-1)(1-\alpha)u_{t+1} - \gamma\log\upsilon(u_{t+1})}_{\text{std dev: } 0.24}$$

Dividend vol $\approx \sqrt{0.032^2 + 0.095^2} = 0.10$ vs. consumption vol $= 0.032$.

### 3. Low Risk-Free Rate
Individual agents' consumption grows slower and is riskier than aggregate consumption (standard OLG property, Blanchard 1985).

---

## Cohort Effects as Empirical Measure (Lemma 3)

From equation (39), inter-cohort consumption differences evolve as:

$$a_{s+T} - a_s = -\sum_{i=1}^{T} \log\left(\frac{\upsilon(u_{s+i})}{1-\lambda}\right) + z_{s+T} - z_s \tag{39}$$

The **permanent component** of consumption cohort effects = cumulative log displacement factor.

**Testable prediction:** Permanent shocks to cohort effects should be positively correlated with the **growth-minus-value** return differential.

---


## Key Takeaways

1. **Novel risk factor**: Displacement risk arises from *inter-generational* incomplete markets, not intra-generational frictions. Future generations cannot trade before they are born.

2. **HML as mimicking portfolio**: The value-minus-growth return differential isolates realizations of the displacement factor — rationalizing Fama-French (1993) from first principles.

3. **Identification**: Cohort effects in CEX data provide a long (~80 year) time series for measuring the displacement factor, overcoming the short time dimension of consumption surveys.

4. **Portfolio implication**: Agents with high financial wealth relative to total wealth should tilt toward growth stocks (hedging displacement); those with high human capital should tilt toward value.
