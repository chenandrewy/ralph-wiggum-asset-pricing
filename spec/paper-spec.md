# Paper Specification

## I. Economic Requirements

1. Academic asset pricing theory paper.
2. A secondary goal is to illustrate the threat of a negative AI singularity by demonstration. The very paper is a demonstration.
3. The paper answers the following question:
    - Why might AI stocks have high valuations?
    - The main argument: AI stocks may have high valuations because they help hedge against a negative AI singularity---an explosion of AI development that is devastating for the typical investor.
    - This is not the only reason for high valuations, but the paper highlights this one.
4. The model is purposefully simple and captures the essence of the main argument.
    - Infinite horizon.
    - Characterizes the price/dividend ratios of AI stocks as the probability of the singularity increases.
    - Keep mathematical notation to a minimum. The goal is to make the main argument elegantly.
5. Two agents:
    - AI owners.
        - Owns all of the AI capital.
        - Fully invested in AI, not marginal investors in stock market.
    - Representative household.
        - Marginal investor in stocks: only their consumption matters for this analysis.
        - CRRA = \gamma, time preference = \beta.
6. Consumption growth:
    - \log \Delta C_{t+1} = 0 if no disaster.
    - \log \Delta C_{t+1} = -b if disaster (probability p).
    - A disaster is a sudden improvement in AI that is devastating for the household.
    - Think of as a worst-case scenario for AI progress.
    - Economy booms, but the value of AI is captured by the AI owners.
    - For household, labor is replaced by AI, so labor income plummets, as does consumption.
        - Also, way of life, meaning, is lost. Consumption fall can be thought of as a stand-in for these losses.
    - At t=0, no disasters have happened (singularity has not occurred).
    - Multiple disasters may happen, capturing ongoing uncertainty if a singularity occurs.
7. Publicly traded AI asset:
    - Captures *publicly traded* AI stocks.
    - Dividend D_t = a e^{h N_t} C_t.
    - Interpretation (discuss in prose):
        - a > 0 is small, AI stocks are currently a minor share of the economy.
        - N_t is the number of disasters that have occurred up to and including time t.
        - h > 0: each time a disaster occurs, the AI asset grows as a share of the economy.
        - Intuitively, firms that provide semiconductors, data, AI models, etc. at least partially benefit from a sudden improvement in AI.
8. Non-AI assets:
    - All other assets held by the representative household.
    - Dividend: D_t^{\text{old}} = C_t - D_t.
        - For tractability, we model their dividends as the residual of the household's consumption and the AI asset's dividends.
        - This simply closes the model. It is not essential for the main argument.
9. Incomplete markets are key:
    - If markets are complete, the typical investor could buy stocks in private AI assets and benefit from the singularity along with the AI owners.
    - The paper should characterize both the complete and incomplete market cases.
    - The theory should emphasize this point, as well as its policy implications.
10. Extension section addressing the CFR R1 report:
    - Incorporate key ideas from `spec/lit/Jones-2024-AERI.md`:
        - The singularity may cause extinction.
        - Consumption may become infinite (in our case, for the AI owners).
        - Data on the value of a statistical life can be used to calibrate the model.
    - Consider how infinite output and consumption affects the assumption that agents cannot make trades despite the mutual benefit (see `spec/lit/GKP-2012-WP.md`).
    - Keep these ideas in an extension, so that the main argument stays simple.
    - Ensure the extension sections are meaningful for the main argument. The entire paper should tie together.

## II. Quality Requirements

1. The narrative is consistent with the results.
2. Figures and tables are nicely formatted.
3. The paper tells a clear, unified, and concise story.
4. Remove text and math that do not add value.

## III. Style Requirements

1. Writing is between an academic paper and a blog post. Catchy and conversational, yet rigorous. Favor plain english. Be direct and concise. Not cringey.
2. The author is anonymous.
3. The abstract is 100 words or less.
4. The title is short, evocative and eye-catching, but not cringey.
5. Paper length is less than 15 pages, excluding references.
6. Every page has a visible page number.
7. At most 6 exhibits.
8. Lit review focuses on the most relevant papers and is concise.

## IV. Technical Requirements

1. `paper/paper.tex` is the canonical paper and the only LaTeX document intended for review, testing, and referee-style evaluation.
2. `paper/` should contain only assets used by `paper/paper.tex`.
