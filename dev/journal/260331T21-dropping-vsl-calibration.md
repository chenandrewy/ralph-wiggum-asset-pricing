# Dropping the VSL Calibration from the Paper

March 31, 2026 at 9:24 PM EDT

## Decision

We are removing the value-of-statistical-life (VSL) calibration strategy from the paper. The extinction risk extension stays, but the VSL-based reasoning for disciplining the extinction probability parameter $p$ is being dropped.

## Background

The paper spec (item 5c) originally envisioned using VSL data — following Jones (2024, AERI) — to calibrate the extinction risk extension. Jones uses VSL to pin down $\bar{u}$, the level constant in CRRA utility that makes $u(c) > 0$. With $\bar{u}$ pinned down, he can quantify how conservative agents should be about extinction gambles: a life-year is worth roughly 6× annual consumption, so even infinite consumption delivers only finite welfare, making agents very reluctant to accept any extinction probability.

The paper's current draft uses this to derive a threshold $p^* \approx 0.046$ at which an agent would reject doubled consumption paired with extinction risk, and sets the baseline $p = 0.03$ below this threshold.

## Why It Doesn't Work Here

The core issue is that **VSL is a welfare concept, not a pricing concept**, and our paper is about asset prices.

What the VSL really answers is: what's better, living with some level of consumption, or dying? It quantifies the tradeoff between being alive (with utility flow $u(c)$) and being dead (with utility zero). This pins down the **level** of the utility function — specifically $\bar{u}$, the constant that determines where utility sits relative to zero.

Asset prices are determined by the stochastic discount factor, $\Lambda_t = e^{-\rho t} c_t^{-\gamma}$, which depends on **marginal** utility. Marginal utility ($c^{-\gamma}$) is a derivative — it measures how utility changes with a small change in consumption. It does not depend on the level of utility, and so $\bar{u}$ never appears in any pricing equation.

More concretely, in the extinction-adjusted pricing formula:

$$\delta_i^{\text{ext}} = \delta_0 - \lambda\!\left[(1-p)\kappa^{-\gamma}\theta_i - 1\right]$$

the extinction probability $p$ and the singularity arrival rate $\lambda$ enter only through the product $\lambda(1-p)$. From observed asset prices, you can back out this composite — the effective arrival rate of non-extinction singularities — but you cannot separately identify $\lambda$ and $p$. The VSL calibration cannot help break this identification problem, because the object it pins down ($\bar{u}$) never enters the SDF.

In short: the life-vs-death tradeoff that VSL quantifies is not a margin that shows up in asset prices. Since the paper doesn't model agents choosing whether to accept extinction risk (it's not a choice — singularities just happen), and since the pricing kernel only reflects marginal consumption comparisons across states, the VSL adds nothing to the asset pricing analysis.

## What We Keep

The extinction risk extension itself remains valuable. It shows that extinction dampens the hedging motive (Proposition 4) and interacts with the Coase-theorem result. We just won't use VSL to discipline $p$ — instead, $p$ enters as a parameter that investors may have beliefs about, and we show how valuations vary with it.
