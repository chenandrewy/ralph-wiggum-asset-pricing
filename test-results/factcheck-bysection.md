# tests/factcheck-bysection.py
Started: 2026-04-09 20:21:48 EDT
Runtime: 6m 39s
[ralph-garage/agent-logs/20260409T202148.451019-0400_factcheck-bysection_claude_opus.log](../ralph-garage/agent-logs/20260409T202148.451019-0400_factcheck-bysection_claude_opus.log)

# factcheck-bysection
VERDICT: PASS
REASON: All arithmetic is correct, all verbal claims are supported, and no claim is materially wrong; two minor prose imprecisions noted but neither constitutes an error.

## Introduction (lines 39–73)

- **Line 39** — Section header
- **Line 41** [FIGURE/TABLE] OK — Figure confirms NASDAQ (solid) above S&P 500 (dashed) from 2015 onward with sharp post-2023 divergence
- **Line 41** [VERBAL] OK — "AI- and technology-heavy NASDAQ Composite" is an accurate characterization
- **Lines 43–48** [FIGURE/TABLE] OK — Caption matches R code: both series normalized to Jan 2015 = 100; sources (NASDAQ from FRED, S&P 500 from Shiller dataset) confirmed in code
- **Line 50** [DEFINITION] OK — "AI singularity—a sudden, dramatic improvement in AI productivity" matches spec §I.2.a
- **Line 50** [VERBAL] OK — Market incompleteness / hedging mechanism accurately described; consistent with spec §I.3.b
- **Line 52** [VERBAL] OK — Descriptive claim about under-discussed financial market solutions; no specific empirical assertion requiring a reference
- **Line 54** [REFERENCE] OK — GKP2012 attribution ("rents from new technologies accrue to agents that current investors cannot trade with") matches GKP2012 p.492 verbatim
- **Line 54** [REFERENCE] OK — "displacement risk is distinct from aggregate consumption risk" matches GKP2012 p.493
- **Line 54** [REFERENCE] OK — "growth stocks provide a partial hedge" matches GKP2012 p.493
- **Line 54** [VERBAL] OK — "Our model simplifies their overlapping-generations structure" — GKP2012 is explicitly OLG; our model uses representative household
- **Line 54** [ARITHMETIC] OK — "P/D ratios for AI stocks can reach roughly six times those of non-AI stocks" — table maximum is ratio 5.8 at p=1.0%, ξ=0%; "roughly six" is appropriate
- **Line 54** [REFERENCE] OK — "Extinction risk \citep{Jones2024} attenuates this gap" — table confirms ratio drops 5.8→4.3 as ξ goes 0%→5% at p=1.0%
- **Line 56** [VERBAL] OK — Veto extension claims match spec §I.5.c.i–v
- **Line 58** [REFERENCE] OK — GKP2012 ("capital belongs to future innovators") confirmed; Jones2024 ("explosive output growth") appropriate
- **Line 58** [VERBAL] OK — Transfer extension logic (abundance overcomes deadweight costs) matches spec §I.5.d.iii
- **Line 60** [VERBAL] OK — Footnote describing AI/human division of labor matches spec §IV.4.c accurately
- **Line 65** [REFERENCE] OK — GKP2012 lit review characterization ("general-equilibrium model… innovation displaces existing agents… systematic risk factor under incomplete markets") matches GKP2012 abstract
- **Line 67** [REFERENCE] OK — Jones2024 ("bounded utility functions make agents conservative about extinction") matches Jones2024 Section A discussion of CRRA upper bound
- **Line 67** [VERBAL] OK — "attenuating rather than amplifying the valuation premium" confirmed by table (ratio decreases with ξ)
- **Line 69** [REFERENCE] OK — KoganPapanikolaou2014 (JF), KoganPapanikolaouStoffman2020 (JPE), Knesl2023 (JFE), Barro2006 (QJE), Wachter2013 (JF), PastorVeronesi2009 (AER), KorinekSuh2024 (NBER WP) — all bib keys correct and characterizations accurate

## Model (lines 74–185)

- **Line 74** — Section header "Model"
- **Line 78** [REFERENCE] OK — GKP2012 analogy to future capital owners matches GKP2012 p.492; caveat that entry dynamics are not modeled is present (per spec §I.4.d)
- **Lines 81–85** [DEFINITION] OK — Aggregate consumption growth $C_{t+1} = (1+g)C_t$ is standard
- **Line 87** [DEFINITION] OK — Household share $\alpha_t \in (0, 1-\theta_t]$; ensures private AI capital dividend is non-negative
- **Lines 90–101** [DEFINITION] OK — Singularity structure internally consistent; probabilities sum to 1
- **Line 98** [REFERENCE] OK — Jones2024 extinction characterization matches source: "precisely the state of the world in which AI is sufficiently powerful…seems most likely to pose existential risk"
- **Lines 107–108** [DEFINITION] OK — AI dividend $D_t^{AI} = \theta_t C_t$; share evolution $\theta_{t+1} = \theta_t + \Delta\theta(1-\theta_t)$ keeps θ ∈ (0,1)
- **Line 111** [DEFINITION] OK — Private AI capital dividend $(1-\alpha_t)C_t - D_t^{AI} = (1-\alpha_t-\theta_t)C_t \geq 0$ by constraint on α
- **Line 114** [ASSUMPTION] OK — CRRA with $\gamma > 1$ and $\beta \in (0,1)$; baseline $\gamma=4$ satisfies $\gamma>1$
- **Lines 116–118** [DEFINITION] OK — Standard CRRA infinite-horizon utility
- **Lines 125–136** [ARITHMETIC] OK — P/D formula structure $A/(1-A)$ is correct closed-form for geometric pricing sum
- **Line 135** [ARITHMETIC] OK — $\Gamma^{AI} = [0.15 + 0.2 \times 0.85]/0.15 \times 1.5 = 0.32/0.15 \times 1.5 = 3.2$; $\Gamma^N = [0.85-0.17]/0.85 \times 1.5 = 0.8 \times 1.5 = 1.2$. Confirms $\Gamma^{AI} > 1+\eta > \Gamma^N$
- **Lines 142–148** [ARITHMETIC] OK — Existence condition $A^j < 1$ is necessary and sufficient for positive, finite P/D; "if and only if" is correct
- **Line 150** [VERBAL] OK — "$\phi(1+\eta) < 1$ when $\phi$ is sufficiently small" — baseline: $0.5 \times 1.5 = 0.75 < 1$; household consumption falls in singularity, raising marginal utility, making AI stocks hedges
- **Lines 152–158** [ARITHMETIC] OK — Corollary 1 proof: P/D increasing in $\Gamma^j$ (since $d/dA[A/(1-A)] > 0$); $\Delta\theta > 0 \Rightarrow \Gamma^{AI} - \Gamma^N = (1+\eta)\Delta\theta/\theta > 0$
- **Lines 160–167** [VERBAL] OK — Proposition 2 comparative statics: (i) spread increasing in displacement severity ✓; (ii) increasing in p for large γ ✓; (iii) decreasing in ξ ✓
- **Lines 169–175** [ARITHMETIC] OK — All three proof arguments are valid: (i) $\phi^{-\gamma}$ amplification differential; (ii) weight-shifting to singularity states; (iii) uniform shrinkage of non-extinction weight
- **Line 179** [REFERENCE] OK — GKP2012 Discussion characterization ("growth stocks earn lower expected returns… new cohorts of firms") matches GKP2012 abstract and OLG structure
- **Line 181** [REFERENCE] OK — "future innovators' rents cannot be traded" matches GKP2012 Introduction; disclaimer about not modeling entry dynamics present

## Quantitative Analysis (lines 186–203)

- **Lines 188–193** — Table exhibit (table-pd-ratios.tex)
- **Line 195** [ASSUMPTION] OK — Parameters $\beta=0.96$, $g=0.02$, $\gamma=4$, $\phi=0.5$, $\eta=0.5$, $\theta=0.15$, $\Delta\theta=0.2$ match table footnote and R code
- **Line 195** [ARITHMETIC] OK — $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$; household consumption falls by 25%. Correct
- **Line 195** [ARITHMETIC] OK — $\eta=0.5$ means 50% aggregate consumption rise. Correct
- **Line 195** [ARITHMETIC] OK — Independent recomputation of P/D at $p=0.5\%$, $\xi=0$: base $= 0.96 \times 1.02^{-3} = 0.9046$; $\phi^{-\gamma}(1+\eta)^{-\gamma}\Gamma^{AI} = 16 \times 0.1975 \times 3.2 = 10.114$; $K^{AI} = 0.9046 \times (0.995 + 0.005 \times 10.114) = 0.9459$; $P/D^{AI} = 0.9459/0.0541 = 17.5$ ✓
- **Line 195** [ARITHMETIC] OK — At $p=0.5\%$, $\xi=0$: $P/D^N = 11.1$ ✓; Ratio $= 1.6$ ✓
- **Line 195** [ARITHMETIC] OK — At $p=1\%$, $\xi=0$: $P/D^{AI} = 76.4$ ✓; $P/D^N = 13.3$ ✓; Ratio $= 5.8$ ✓
- **Line 197** [VERBAL] OK — "AI stocks trade at a P/D of roughly 18" (table: 17.5); "non-AI stocks trade near 11" (table: 11.1); "ratio of about 1.6" (table: 1.6). The "roughly 18" is a slight overstatement of 17.5 but not materially wrong
- **Line 197** [VERBAL] OK — "At $p=1\%$, the ratio rises to nearly 6 to 1" — table shows 5.8; "nearly 6" is appropriate
- **Line 197** [VERBAL] OK — "Extinction risk reduces both valuations and compresses the AI premium, as Proposition 2(iii) predicts" — table confirms: at $p=1\%$, ratio falls from 5.8 (ξ=0%) to 4.3 (ξ=5%) to 2.6 (ξ=20%)
- **Line 199** [VERBAL] OK — "P/D ratios for AI stocks that are 1.5 to 6 times higher… across annual singularity probabilities in the 0.5–1% range" — actual range at ξ=0% is 1.58 to 5.76; "1.5 to 6" is a round-number characterization, not materially wrong
- **Line 199** [VERBAL] OK — "NASDAQ has appreciated roughly 50% more than the S&P 500 since 2015" — figure shows NASDAQ at ~500 vs S&P 500 at ~340 by recent data, consistent with substantial outperformance; exact ratio depends on data download date but claim is broadly supported

## Extensions: Market Incompleteness and the Singularity (lines 204–273)

- **Line 204** — Section header
- **Line 206** [VERBAL] OK — Accurate framing: baseline takes incompleteness as given; extensions examine further consequences

### Extension 1: Veto and Efficient Development (lines 208–234)

- **Line 210** [DEFINITION] OK — Augmented model adds positive singularity (prob λ) alongside baseline negative singularity (prob 1−λ)
- **Line 213** [DEFINITION] OK — Positive singularity: household share increases and aggregate consumption jumps by 1+η
- **Line 214** [DEFINITION] OK — Negative singularity remains as baseline: $\alpha_{t+1} = \phi\alpha_t$
- **Line 217** [ASSUMPTION] OK — $\lambda > 1/2$: positive singularity is modal outcome; "socially efficient" qualified with "in the sense that the expected welfare gain…is positive"
- **Line 219** [REFERENCE] OK — Jones2024 extinction utility normalization: "we normalized the utility when dead to zero; this is a free normalization" (Jones 2024 p.575–576)
- **Line 219** [ARITHMETIC] OK — CRRA utility negative for all $c>0$ when $\gamma>1$: $c^{1-\gamma}/(1-\gamma)$ with $1-\gamma<0$ gives $u(c)<0$. Correct
- **Line 219** [VERBAL] OK — Normalization "makes the veto result conservative" — with $U_{ext}=0 > u(c)$, extinction is weakly preferred, making the household less inclined to veto; finding the veto survives this is indeed conservative
- **Lines 221–226** [VERBAL] OK — Proposition 3: (i) incomplete markets + large γ → veto even when socially efficient ✓; (ii) complete markets → never veto ✓
- **Lines 228–232** [VERBAL] OK — Proof logic: (i) concavity and high γ make downside loom larger than upside under incomplete markets; (ii) complete markets allow hedging, so household reflects social surplus
- **Line 234** [VERBAL] OK — Discussion of extinction risk interaction with veto is directionally correct

### Extension 2: Government Transfers (lines 236–269)

- **Line 238** [REFERENCE] OK — GKP2012: "Such extensions [including intergenerational transfers] would not change the functional form of Eq. (25) and would only affect the magnitude of the displacement factor" (GKP2012 p.496–497). Citation accurate
- **Line 243** [ARITHMETIC] OK — Post-transfer consumption equation: first term $\phi\alpha(1+\eta)C_t(1+g)$ is displaced household consumption; second term $\tau(1-\delta\tau)(1-\phi\alpha)(1+\eta)C_t(1+g)$ is net transfer. Both terms verified
- **Line 248** [ARITHMETIC] OK — $\phi_{eff} = \phi + \tau(1-\delta\tau)(1-\phi\alpha)/\alpha$ derived correctly by factoring $c^H_{post} = \phi_{eff} \cdot \alpha \cdot (1+\eta)(1+g)C_t$
- **Line 253** [ARITHMETIC] OK — Transfer ratio $c^H_{post}/c^H_{no\text{-}transfer} = 1 + \tau(1-\delta\tau)(1-\phi\alpha)/(\phi\alpha)$; $(1+\eta)$ and other common factors cancel, confirming η-independence
- **Line 258** [ASSUMPTION] OK — Parameters $\alpha=0.70$, $p=0.5\%$, $\xi=5\%$; baseline ($\eta=0.5$, $\phi=0.5$); large singularity ($\eta=9$, $\phi=0.05$) — all confirmed in R code
- **Line 258** [ARITHMETIC] OK — Large singularity: $\phi(1+\eta) = 0.05 \times 10 = 0.5$, consumption halves. Correct
- **Line 258** [ARITHMETIC] OK — Baseline: $\phi(1+\eta) = 0.5 \times 1.5 = 0.75$, falls by 25%. Correct
- **Line 260** [ARITHMETIC] OK — $\phi^{-\gamma} = 0.05^{-4} = 20^4 = 160{,}000$. Exact
- **Line 260** [ARITHMETIC] OK — Existence condition violated at $\tau=0$ for large singularity: $K \approx 2.37 \gg 1$, so pricing sum diverges. Confirmed numerically
- **Line 260** [VERBAL] OK — "hedge value of AI stocks becomes infinite—no finite price can compensate" — correct economic interpretation of $A^j \geq 1$
- **Line 264** [ASSUMPTION] OK — Figure caption parameters ($\alpha=0.70$, $p=0.5\%$, $\xi=5\%$, $\delta=0.5$) match R code
- **Line 269** [REFERENCE] OK — Jones2024 and Nordhaus2021 bib keys correct; citations appropriate for explosive output growth and economic singularity discussions

## Conclusion (lines 274–284)

- **Line 276** [VERBAL] OK — "AI stocks trade at high valuations… hedging motive" — supported by Proposition 1 and empirical figure
- **Line 276** [VERBAL] OK — "requires market incompleteness" — supported by model setup (Section 2.1) and discussion (Section 2.3)
- **Line 276** [VERBAL] OK — "attenuated by extinction risk" — supported by Proposition 2(iii) and table
- **Line 276** [VERBAL] OK — "households may inefficiently block AI development" — supported by Extension 1 (Proposition 3)
- **Line 276** [VERBAL] OK — "government transfers… can become effective if singularity-driven growth is large enough" — supported by Extension 2 and figure
- **Line 278** [VERBAL] OK — Limitations paragraph ("abstracts from continuous-time dynamics, heterogeneous beliefs, production-side details") accurately describes model scope; no new claims introduced

## Proof of Proposition 1 (lines 285–314)

- **Line 290** [ARITHMETIC] OK — Standard CRRA Euler equation with household's own consumption growth as SDF kernel; correct under incomplete markets
- **Line 296** [ARITHMETIC] OK — No-singularity case: $c_{t+1}^H/c_t^H = 1+g$, $D_{t+1}^{AI}/D_t^{AI} = 1+g$. Verified from model primitives
- **Line 297** [ARITHMETIC] OK — Non-extinction singularity: $c_{t+1}^H/c_t^H = \phi(1+g)(1+\eta)$, $D_{t+1}^{AI}/D_t^{AI} = \Gamma^{AI}(1+g)$. Verified
- **Line 298** [ARITHMETIC] OK — Extinction: payoff zero. Standard treatment under Jones2024 convention
- **Lines 302–305** [ARITHMETIC] OK — Expanded Euler equation verified term by term: no-singularity term $= \beta(1+g)^{1-\gamma}(1-p)(v^{AI}+1)D_t^{AI}$; non-extinction term $= \beta(1+g)^{1-\gamma}p(1-\xi)[\phi(1+\eta)]^{-\gamma}\Gamma^{AI}(v^{AI}+1)D_t^{AI}$. Both correct
- **Line 310** [ARITHMETIC] OK — Solving $v = A(v+1)$ gives $v = A/(1-A)$. Matches eq:pd-ai exactly
- **Line 313** [VERBAL] OK — "derivation for non-AI stocks is identical, replacing $\Gamma^{AI}$ with $\Gamma^N$" — correct by symmetry
