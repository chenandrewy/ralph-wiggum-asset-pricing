# Paper Specification

## I. Economic Requirements

1. Academic asset pricing theory paper.
2. The paper uses the following economic ideas:
    - An AI singularity is a sudden improvement in AI that vastly increases productivity and output.
    - A *negative* AI singularity is an AI singularity that is devastating for the typical investor.
    - Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. It does not necessarily refer to Arrow-Debreu securities.
3. The paper makes the following arguments:
    - Main argument: AI stocks may have high valuations, in part, because they help hedge against a negative AI singularity
    - Incomplete markets are key: if markets are complete, the typical investor could buy stocks in private AI assets and benefit from the singularity along with the AI owners.
    - Financial market solutions to AI disaster risk are under-discussed.
    - If the singularity occurs, then market frictions can be overcome due to the abundance of resources.
4. The main model has the following features:
    - Infinite horizon
    - Two agents: A representative household, who is the marginal investor, and AI owners who hold private AI capital and are not marginal investors.        
    - Two publicly traded assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity.
    - The main focus is on the price/dividend ratio of public AI stocks, and how it changes with the probability of a negative AI singularity.
5. An extension of the main model formally incorporates ideas from `spec/lit/Jones-2024-AERI.md`:
    - The singularity may cause extinction.
    - Consumption may become infinite (in our case, only for the AI owners).
    - Data on the value of a statistical life can be used to calibrate the model.
    - Consider how infinite output and consumption affects the assumption that agents cannot make trades despite the mutual benefit (see `spec/lit/GKP-2012-WP.md`).
    - Keep these ideas in an extension, so that the main argument stays simple.
6. The introduction includes a single figure illustrating the valuation of AI stocks compared with the market portfolio.

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
5. Paper length is less than 20 pages, excluding references.
6. Every page has a visible page number.
7. At most 6 exhibits.
8. Lit review focuses on the most relevant papers and is concise.

## IV. Technical Requirements

1. `paper/paper.tex` is the canonical paper and the only LaTeX document intended for review, testing, and referee-style evaluation.
2. `paper/` should contain only assets used by `paper/paper.tex`.
