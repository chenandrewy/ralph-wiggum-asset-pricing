# Paper Specification

## I. Economic Requirements

1. Academic asset pricing theory paper.
2. The following economic ideas are consistently used, throughout the paper
    - a. An AI singularity is a sudden improvement in AI that vastly increases productivity and output.
    - b. A *negative* AI singularity is an AI singularity that is devastating for the typical investor.
    - c. Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. It does not necessarily refer to Arrow-Debreu securities.
3. The paper makes the following arguments:
    - a. Main argument: AI stocks may have high valuations, in part, because they help hedge against a negative AI singularity
    - b. Incomplete markets are key: if markets are complete, the typical investor could buy stocks in private AI assets and benefit from the singularity along with the AI owners.
    - c. Financial market solutions to AI disaster risk are under-discussed.
    - d. If the singularity occurs, then market frictions can be overcome due to the abundance of resources.
4. The main model has the following features:
    - a. Infinite horizon
    - b. Two agents: A representative household, who is the marginal investor, and AI owners who hold private AI capital and are not marginal investors in public stocks.
    - c. Two publicly traded assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity.
    - d. The main focus is on the price/dividend ratio of public AI stocks, and how it changes with the probability of a negative AI singularity.
    - e. The private AI capital and AI owners can also be thought of as capital and owners that do not yet exist, as in `spec/lit/GKP-2012-WP.md`.
5. An extension of the main model formally incorporates ideas from `spec/lit/Jones-2024-AERI.md`:
    - a. The singularity may cause extinction.
    - b. Consumption may become infinite (in our case, only for the AI owners).
    - c. Data on the value of a statistical life can be used to calibrate the model.
    - d. Consider how infinite output and consumption affects the assumption that agents cannot make trades despite the mutual benefit (see `spec/lit/GKP-2012-WP.md`).
    - e. Keep these ideas in an extension, so that the main argument stays simple.
6. The paper explains how it contributes relative to `spec/lit/GKP-2012-WP.md`
    - a. In GKP, there is a footnote mentioning how government debt or intergenerational transfers would affect the magnitude of the displacement factor, but no further analysis. The paper contributes with a formal analysis.
    - b. Without frictions, intergenerational transfers (bequests, gifts, government debt) would allow existing agents to share in the gains of new entrants, eliminating displacement risk — this is the Coase Theorem logic. GKP's modeling assumes, quite reasonably, that such frictions exist and preserve the risk premium.
    - c. In the case of a singularity, perhaps these frictions can be overcome. Following the modeling in `spec/lit/Jones-2024-AERI.md`, we can quantify the size of frictions that can be overcome, given infinite output.
    - d. The characterization of the contribution is purposefully modest. The main insights about displacement risk and incomplete markets are already in GKP.
7. The introduction includes a single figure illustrating the valuation of publicly traded AI stocks compared with the market portfolio using CRSP and Compustat data.
    - a. This figure uses daily data from 2010 to present.

## II. Style Requirements

1. Tone is between an academic paper and a blog post.
2. The author is anonymous.
3. The abstract is 100 words or less.
4. The title is short, evocative and eye-catching, but not cringey.
5. Paper length is at most 20 pages.
6. Every page has a visible page number.
7. At most 6 exhibits.
8. Lit review focuses on the most relevant papers and is concise.
9. All display equations should be numbered

## III. Technical Requirements

1. `paper/` contains only assets used by `paper/paper.tex`. It has no extraneous objects.
2. All sections in `paper.tex` come with comments that list the section number, for ease of reference.
3. All exhibits in `paper.tex` come with comments that list the exhibit number, for ease of reference.
4. All math theorem environments (e.g. propositions) in `paper.tex` come with comments that list the environment number.
5. If the paper relies on local analysis code, `code/` must provide one canonical local analysis path that supports the paper's claims. The canonical local analysis path should be fast enough for routine test execution. Slow or optional steps should either be outside the canonical path or skipped when their outputs already exist, with an explicit way to force regeneration when needed.

## IV. Quality Requirements

1. Figures and tables are nicely formatted.
2. Theoretical derivations are correct
3. Each claim is supported by either the paper's results, or by a literature citation
4. Each citation accurately represents the referenced paper(s).
5. Mathematical formalism is kept to a minimum. Each piece of formalism contributes to the economic claims.
6. Writing catchy and conversational, yet rigorous. Plain English is favored. Writing is direct and concise.