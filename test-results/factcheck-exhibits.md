# tests/factcheck-exhibits.py
Started: 2026-04-09 20:39:27 EDT
Runtime: 3m 23s
[ralph-garage/agent-logs/20260409T203927.592417-0400_factcheck-exhibits_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T203927.592417-0400_factcheck-exhibits_claude_claude-opus-4-6.log)

# factcheck-exhibits
VERDICT: PASS
REASON: All three exhibits are correctly generated and consistent with the code and model parameters.

## Figure 1: AI Valuations vs. the Broader Market

**Description:** Time-series plot of NASDAQ Composite and S&P 500 monthly closing prices, each normalized to January 2015 = 100. NASDAQ is labeled "AI/Tech-Heavy" and plotted as a solid blue line; S&P 500 as a dashed red line.

### Suspicious features

1. **Label "AI/Tech-Heavy" for NASDAQ Composite.** The NASDAQ Composite is a broad index, not an AI-specific portfolio. This could overstate the AI exposure implied by the figure title ("Valuations of AI-Exposed Stocks").
2. **Sharp divergence post-2023.** The NASDAQ pulls dramatically ahead of the S&P 500 starting around 2023.

### Code check

1. The caption explicitly states "NASDAQ Composite (solid), which is heavily weighted toward AI and technology firms." This is a defensible characterization for a finance audience, not a mislabel. The code comments acknowledge FRED lacks individual stock prices and uses NASDAQ as a proxy. **Verified — editorial choice, not an error.**
2. The post-2023 divergence is consistent with observed market history (generative AI boom driving tech valuations). Data is downloaded from FRED (NASDAQ) and datahub Shiller dataset (S&P 500), processed with straightforward normalization (first common month = 100). No transformations that could introduce artifacts. **Verified — reflects real market data.**

**Exhibit verdict: PASS** — Data sources are standard, processing is straightforward, labels and caption are consistent.

## Table 1: Price-Dividend Ratios

**Description:** Grid of model-implied P/D ratios for AI and non-AI stocks across singularity probabilities ($p$ = 0.1%–1.0%) and extinction probabilities ($\xi$ = 0%–20%). Parameters: $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$.

### Suspicious features

1. **AI P/D of 76.4 at $p=1.0\%$, $\xi=0\%$.** This is extremely high relative to other values in the table (next highest is 56.1).
2. **Non-AI P/D barely moves across $p$ values** (9.7–13.3), while AI P/D is highly sensitive (10.5–76.4).

### Code check

1. Independent recomputation of all 20 table cells matches the output exactly (verified via Python reimplementation of the `compute_pd` function). At $p=1\%$, $\xi=0\%$, the kernel $K = 0.9871$, so $P/D = K/(1-K) = 76.4$. The high value reflects $K$ approaching 1 — the model's intended mechanism where high singularity probability with large AI dividend growth pushes valuations toward infinity. **Verified — correct and expected from the model.**
2. The asymmetry between AI and non-AI sensitivity is driven by the dividend growth factors: $\gamma^{AI} = 3.2$ vs $\gamma^N = 1.2$. The AI SDF-weighted singularity term is much larger, making the AI kernel more sensitive to $p$. **Verified — correct model behavior.**

**Exhibit verdict: PASS** — All 20 cells independently verified; extreme values are a correct consequence of the model's Euler-equation pricing.

## Figure 2: Extension Panels

**Description:** Two-panel figure. Panel (a) plots AI stock P/D ratio vs. tax rate $\tau$ (0–40%) for baseline ($\eta=0.5$, $\phi=0.5$) and large singularity ($\eta=9$, $\phi=0.05$) scenarios. Panel (b) plots household consumption growth in the singularity state vs. $\tau$ (0–70%) on a log scale, with annotations for catastrophic losses at $\tau=0$.

### Suspicious features

1. **Panel (a): Large-singularity line starts off-chart high and drops rapidly.** An annotation reads "$P/D \to \infty$ as $\tau \to 0$."
2. **Panel (a): Y-axis capped at 25.** Could hide important behavior above the cap.
3. **Panel (b): "Catastrophe: 50% loss" annotation** at $\tau=0$ for the large singularity scenario.
4. **Panel (b): "25% loss" annotation** at $\tau=0$ for the baseline scenario.

### Code check

1. At $\tau=0$ for the large singularity ($\eta=9$, $\phi=0.05$): the kernel $K=2.37 > 1$, confirming $P/D$ is undefined (diverges). The `compute_pd_with_transfer` function correctly returns NA when $K \geq 1$. As $\tau$ increases, $\phi_{eff}$ rises, reducing the SDF and bringing $K$ below 1. The annotation is mathematically correct. **Verified.**
2. The cap at $y=25$ is set in code (`y_cap_a <- 25`) with an explicit annotation explaining the off-chart behavior. The baseline line stays well within range (~17 at $\tau=0$, declining). The large-singularity line enters the visible range at a small positive $\tau$. This is a reasonable visualization choice. **Verified — not hiding errors.**
3. Consumption growth at $\tau=0$, large singularity: $\phi \cdot (1+\eta) = 0.05 \times 10 = 0.50$, confirming a 50% loss. **Verified.**
4. Consumption growth at $\tau=0$, baseline: $\phi \cdot (1+\eta) = 0.50 \times 1.5 = 0.75$, confirming a 25% loss. **Verified.**

**Exhibit verdict: PASS** — All annotations verified numerically; panel behavior is consistent with the model equations and code logic.
