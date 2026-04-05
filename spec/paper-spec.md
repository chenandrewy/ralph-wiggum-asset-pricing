# Paper Specification

## I. Economic Requirements

1. Academic asset pricing theory paper.
2. The following economic ideas are consistently used throughout
    - a. An AI singularity is a sudden improvement in AI that vastly increases productivity and output.
    - b. A *negative* AI singularity is an AI singularity that is devastating for the typical investor.
    - c. Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. It does not necessarily refer to Arrow-Debreu securities.
3. The paper makes the following arguments:
    - a. Main argument: AI stocks may have high valuations, **in part**, because they help hedge against a negative AI singularity
    - b. Incomplete markets are key: if markets are complete, there would be no need to hedge
    - c. Financial market solutions to AI disaster risk are under-discussed, though frictions can limit their effectiveness.
    - d. If the singularity occurs, then market frictions can be overcome due to the abundance of resources.
    - e. Incomplete markets may distort not only valuations, but also the implementation of AI deployment.
4. The main model has the following features:
    - a. Infinite-horizon, discrete-time model.
    - b. Two agents: A representative household, who is the marginal investor, and AI owners who hold private AI capital, including unborn or not-yet-marketable capital, and are not marginal investors in public stocks.
    - c. Two publicly traded assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity.
    - d. The private AI capital and AI owners can also be thought of as unborn capital and future owners that do not yet exist, as in `spec/lit/GKP-2012.md`.
    - e. The relationship between price/dividend ratios and the singularity probability is studied quantitatively in a table with compelling magnitudes.    
5. An extension section examines multiple simple extensions of the main model that capture essential features of the singularity, following the advice in `spec/CFR-R1-report.md`. Each extension branches directly off the baseline model rather than building on the others, so the paper avoids a single sprawling model even as it studies several margins.
    - a. Extension 1: Government transfers could help attenuate the incomplete markets problem.
        - i. The ideal way to resolve the market incompleteness is to allow broader trading of AI capital. But as pointed out by `spec/lit/GKP-2012.md`, this capital may not yet exist, and thus sufficiently broad trading may be impossible.
        - ii. Government transfers help resolve this problem, as mentioned in `spec/lit/GKP-2012.md`. But they incur sizeable deadweight costs that make the solution ineffective for a setting without the singularity (as in `spec/lit/GKP-2012.md`).
        - iii. In a singularity, with potentially infinite output growth (`spec/lit/Jones-2024-AERI.md`), the government solution is worth considering, even in the face of immense deadweight costs.
        - iv. A figure illustrates how the price/dividend ratio of AI stocks depends on the output growth in the singularity, as well as the deadweight costs
    - b. Extension 2: Market incompleteness is closely related to efficient deployment of AI. 
        - i. The household can block ("veto") the singularity at a cost to its consumption. This includes preventing unborn AI capital from ever coming into existence.
        - ii. If markets were complete, the household would never veto.
        - iii. Informally, based on Extension 1, if output growth in the singularity is sufficiently large, then government transfers, even with huge deadweight costs, can lead to an efficient AI deployment.
    - c. Extension 3: Extinction risk (as in `spec/lit/Jones-2024-AERI.md`) can affect the price/dividend ratio of AI stocks, and its relationship with the singularity probability.
6. The paper explains how it contributes relative to `spec/lit/GKP-2012.md`
    - a. It connects GKP's ideas to the AI singularity.
    - b. It takes a closer look at how government transfers can affect displacement risk. GKP mention this phenomenon briefly.
    - c. The characterization of the contribution is purposefully modest. The main insights about displacement risk and incomplete markets are already in GKP.

## II. Style Requirements

1. Tone is between an academic paper and a blog post.
2. The author is anonymous.
3. The abstract is 100 words or less.
4. The title is short, evocative and eye-catching, but not cringey.
5. Paper length is at most 20 pages.
6. Every page has a visible page number.
7. At most 6 exhibits.
8. Lit review is at most half a page and appears at the end of the introduction.
9. All display equations should be numbered
10. All propositions are explicitly proved, with long proofs in the appendix.
11. The first section is called "Preface (TBC)", is unnumbered, and left blank. The traditional "Introduction" follows, and then the rest of the paper is standard, as if the Preface is not there.

## III. Technical Requirements

1. `paper/` has the following structure
    - a. `paper.tex` is the main paper file
    - b. All figures and tables are sourced from `paper/exhibits/`
    - d. All files are `paper/exhibits/` are used in the paper
2. `paper.tex` uses comments that list object numbers for ease of reference.
    - a. Sections come with comments that list the section number
    - b. Exhibits come with comments that list the exhibit number
    - c. Math theorem environments (e.g. propositions) come with comments that list the environment number
3. All analysis code goes in `code/` and satisfies the following:
    - a. Code is written in R
    - b. `code/` provides one canonical entry point that regenerates every exhibit used in `paper/paper.tex`.
    - c. The canonical pipeline runs from scratch. It does not rely on precomputed local caches or manually prepared intermediate files.
    - d. The canonical pipeline executes in less than 180 seconds, including any external data download.
    - e. The code outputs directly to `paper/exhibits/` in the correct format for use in the paper.

## IV. Quality Requirements

1. Figures and tables are nicely formatted.
2. Theoretical derivations are correct
3. Each claim is supported by either the paper's results, or by a literature citation
4. Each citation accurately represents the referenced paper(s).
5. The writing is compelling and conversationally, yet rigorous.
    - a. Plain English is favored. Writing is direct and concise.
    - b. The abstract is eye-catching yet rigorous. 
    - c. The introduction is engaging. Each paragraph moves the reader to the next one. 
    - d. The paper uses itself as a demonstration of the AI displacement risk it models, since all analysis and writing is done by AI agents. Discussion of this includes an accurate description of how the work was divided: the human only wrote the "economic specification" of the paper (600 words) and test scripts. This device is used in the abstract and introduction.
    - e. The extension section features a compelling and eye-catching figure.
6. The paper is sensitive, cautious, and modest in how it cites `spec/lit/GKP-2012.md`. 
7. The lit review is centered on the papers most relevant to the paper's contribution. It emphasizes papers in JF, JFE, RFS, JFQA, RAPS, and MS, as well as top economics journals. 
8. The paper is intentionally limited in scope to a compact but richer theoretical contribution.
    - a. Good theory style is essential. Mathematical formalism is kept to a minimum. Each piece of formalism contributes to the economic claims. The paper avoids pompous or ceremonial formalism, and it avoids auxiliary formal detours that do not advance the main argument.
    - b. The empirical content remains very limited, ideally to a single figure in the introduction illustrating the valuation of publicly traded AI stocks compared with non-AI stocks using CRSP data.
    - c. The paper does not try to generate a broad menu of novel testable predictions beyond the model's main arguments.
    - d. The paper may include rough quantitative parameterizations for illustration, but quantitative material remains illustrative rather than becoming a calibration or estimation exercise.
