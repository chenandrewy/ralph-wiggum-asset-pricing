# Paper Specification

## I. Economic Requirements

1. Academic asset pricing theory paper with tightly limited empirical content.
2. The following economic ideas are consistently used throughout the paper
    - a. An AI singularity is a sudden improvement in AI that vastly increases productivity and output.
    - b. A *negative* AI singularity is an AI singularity that is devastating for the typical investor.
    - c. Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. It does not necessarily refer to Arrow-Debreu securities.
3. The paper makes the following arguments:
    - a. Main argument: AI stocks may have high valuations, in part, because they help hedge against a negative AI singularity
    - b. Incomplete markets are key: if markets are complete, the typical investor could buy stocks in private AI assets and benefit from the singularity along with the AI owners.
    - c. Financial market solutions to AI disaster risk are under-discussed.
    - d. If the singularity occurs, then market frictions can be overcome due to the abundance of resources.
4. The main model has the following features:
    - a. Infinite-horizon, discrete-time model.
    - b. Two agents: A representative household, who is the marginal investor, and AI owners who hold private AI capital, including unborn or not-yet-marketable capital, and are not marginal investors in public stocks.
    - c. Two publicly traded assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity.
    - d. The main focus is on the price/dividend ratio of public AI stocks, and how it changes with the probability of a negative AI singularity.
    - e. The private AI capital and AI owners can also be thought of as unborn capital and future owners that do not yet exist, as in `spec/lit/GKP-2012-WP.md`.
5. An extension of the main model addresses the referee's suggestions in `spec/CFR-R1-report.md`:
    - a. The singularity may cause extinction, following `spec/lit/Jones-2024-AERI.md`.
    - b. Consumption may become infinite (in our case, only for the AI owners).
    - c. Government transfer programs attenuate displacement risk, emphasizing the role of heterogeneity at the singularity (cf. `spec/lit/Jones-2024-AERI.md`). Illustrate quantitatively: for a range of plausible singularity growth rates, how large can the deadweight cost of the program be before the attenuation is wiped out?
    - d. Keep these ideas in an extension, so that the main argument stays simple.
6. The paper explains how it contributes relative to `spec/lit/GKP-2012-WP.md`
    - a. GKP note that government transfers would affect the magnitude of the displacement factor but do not conduct further analysis. The paper contributes a formal analysis with a quantitative illustration.
    - b. Without frictions, intergenerational transfers (bequests, gifts, government debt) would allow existing agents to share in the gains of new entrants, eliminating displacement risk — this is the Coase Theorem logic. GKP's modeling assumes, quite reasonably, that such frictions exist and preserve the risk premium.
    - c. A transfer program with deadweight costs can still attenuate displacement if output is large enough. The paper provides a quantitative illustration calibrated to a range of singularity growth rates, showing how much inefficiency the program can absorb.
    - d. The characterization of the contribution is purposefully modest. The main insights about displacement risk and incomplete markets are already in GKP.

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
11. The first section is called "Preface (TBC)", is unnumbered, and left blank
    - a. The traditional "Introduction" follows, and then the rest of the paper is standard, as if the Preface is not there.

## III. Technical Requirements

1. `paper/` has the following structure
    - a. `paper.tex` is the main paper file
    - b. All figures use pdfs in `paper/exhibits/`
    - c. All tables use tex files in `paper/exhibits/`
    - d. All files are `paper/exhibits/` are used in the paper
2. `paper.tex` uses comments that list object numbers for ease of reference.
    - a. Sections come with comments that list the section number
    - b. Exhibits come with comments that list the exhibit number
    - c. Math theorem environments (e.g. propositions) come with comments that list the environment number
3. All analysis code goes in `code/` and satisfies the following:
    - a. Code is written in R
    - b. `code/` provides one canonical entry point that regenerates every exhibit used in `paper/paper.tex`.
    - c. The canonical pipeline runs from scratch. It does not rely on precomputed local caches or manually prepared intermediate files.
    - d. The canonical pipeline executes in less than 180 seconds in routine test execution.
    - e. Any external-data download or WRDS query required by the paper is part of the canonical pipeline and must fit within that time budget.
    - f. The code outputs directly to `paper/exhibits/` in the correct format for use in the paper.
    - g. The canonical pipeline does not silently rely on inconsistent cached objects, manually prepared files, or mismatched code paths.

## IV. Quality Requirements

1. Figures and tables are nicely formatted.
2. Theoretical derivations are correct
3. Each claim is supported by either the paper's results, or by a literature citation
4. Each citation accurately represents the referenced paper(s).
5. The writing is compelling and conversationally, yet rigorous.
    - a. Plain English is favored. Writing is direct and concise.
    - b. The abstract is eye-catching yet rigorous. 
    - c. The introduction is engaging. Each paragraph moves the reader to the next one. 
    - d. The paper uses itself as a demonstration of the AI displacement risk it models, since all analysis and writing is done by AI agents. Discussion of this includes an accurate description of how the work was divided: the human only wrote the paper spec (80 lines) and tests.
6. The paper is sensitive, cautious, and modest in how it cites `spec/lit/GKP-2012-WP.md`. 
7. The lit review is centered on the papers most relevant to the paper's contribution. It emphasizes papers in JF, JFE, RFS, JFQA, RAPS, and MS, as well as top economics journals. 
8. The paper is intentionally limited in scope to a compact theoretical contribution.
    - a. Good theory style is essential. Mathematical formalism is kept to a minimum. Each piece of formalism contributes to the economic claims. The paper avoids pompous or ceremonial formalism, and it avoids auxiliary formal detours that do not advance the main argument.
    - b. The empirical content remains very limited, ideally to a single figure in the introduction illustrating the valuation of publicly traded AI stocks compared with non-AI stocks using CRSP data.
    - c. The paper does not try to generate a broad menu of novel testable predictions beyond the model's main arguments.
    - d. The paper may include rough quantitative parameterizations for illustration, but quantitative material remains illustrative rather than becoming a calibration or estimation exercise.
