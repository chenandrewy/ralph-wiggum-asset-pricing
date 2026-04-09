# Paper Specification

## I. Economic Requirements

1. Unconventional academic asset pricing theory paper.
2. The following economic ideas are consistently used throughout
    - a. An AI singularity is a sudden improvement in AI that vastly increases productivity and output.
    - b. A *negative* AI singularity is an AI singularity that is devastating for the typical investor.
    - c. Incomplete markets refers to the idea that some assets cannot be bought by the representative investor. It does not necessarily refer to Arrow-Debreu securities.
3. The paper makes the following arguments:
    - a. Main argument: AI stocks may have high valuations, **in part**, because they help hedge against a negative AI singularity
    - b. Incomplete markets are key: if markets are complete, there would be no need to hedge
    - c. Financial market solutions to AI disaster risk are under-discussed, though frictions can limit their effectiveness.
    - d. If the singularity occurs, then market frictions can be overcome due to the abundance of resources.
    - e. Incomplete markets may distort not only valuations, but also the development of AI.
4. Main model: singularity with displacement risk.
    - a. Infinite-horizon, discrete-time model.
    - b. Two agents: A representative household, who is the marginal investor, and AI owners who own private AI capital, and are not marginal investors in public stocks. 
    - c. Two publicly traded assets: AI stocks and non-AI stocks. AI stocks grow as a share of the economy with each singularity.
    - d. The private AI capital and AI owners can also be thought of as future capital and future owners that do not yet exist, as in `spec/lit/GKP-2012.md`. But this is just an analogy. **Importantly, we do not explicitly model this entry dynamic and should not allow the reader to think that we do.**. 
    - e. The singularity may cause extinction, as in `spec/lit/Jones-2024-AERI.md`.
    - f. The relationship between price/dividend ratios and the singularity probability is studied quantitatively in a table with compelling magnitudes. The interaction with extinction risk is examined too.
5. Extension section: closer look at market incompleteness and the singularity.
    - a. This section aims to address the referee report `spec/CFR-R1-report.md`. 
    - b. Each extension branches directly off the baseline model rather than building on the others, to keep the modeling simple.
    - c. Extension 1: Market incompleteness is closely related to efficient development of AI. 
        - i. There is a chance of a *positive* singularity, in which the household also benefits. The positive singularity is the most likely outcome. 
        - ii. AI development is socially efficient in the sense that the positive singularity outweighs the negative singularity in a welfare calculation.
        - iii. The household can block ("veto") development of AI at a significant cost. The cost is significant because it requires intense government intervention and associated deadweight costs. 
        - iv. There is a base case, in which the household vetoes development of AI, due to the disaster risk and risk aversion. 
        - v. But if markets are complete, the household would never veto.
    - d. Extension 2: Government transfers could attenuate the incomplete markets problem, despite their deadweight costs.
        - i. The ideal resolution of market incompleteness is to allow broader trading of AI capital. But as pointed out by `spec/lit/GKP-2012.md`, this capital may not yet exist, and thus this ideal solution has limits.
        - ii. Government transfers may help resolve this deeper incompleteness problem, as mentioned in `spec/lit/GKP-2012.md`. But they incur sizeable deadweight costs (waste, fraud, abuse) that scale with the size of the transfers, making this solution ineffective and unattractive in standard settings. 
        - iii. But in a singularity, with potentially infinite output growth (`spec/lit/Jones-2024-AERI.md`), the government solution is worth considering, even in the face of immense deadweight costs. This possibility is analyzed quantitatively.         
        - iv. A two-panel figure illustrates how price/div of AI stocks and the household's consumption growth in the singularity depend on the tax rate. It illustrates the baseline case where the deadweight costs make transfers ineffective, as well as a case where the singularity growth overcomes the deadweight costs. It must show that the singularity is catastrophic for the household absent transfers.
6. The paper explains how it contributes relative to `spec/lit/GKP-2012.md`
    - a. It connects GKP's ideas to the AI singularity.
    - b. It takes a closer look at how government transfers can affect displacement risk, as discussed in GKP.
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
    - d. The paper uses itself as a demonstration of the AI displacement risk it models, since all analysis and writing is done by AI agents. Discussion of this includes an accurate description of how the work was divided: the human only wrote the "economic specification" of the paper (700 words) and test scripts. This device is used in the abstract and introduction.
    - e. The extension section features a compelling and eye-catching figure.
6. The paper is sensitive, cautious, and modest in how it cites `spec/lit/GKP-2012.md`. 
7. The lit review is centered on the papers most relevant to the paper's contribution. It emphasizes papers in JF, JFE, RFS, JFQA, RAPS, and MS, as well as top economics journals. 
8. The paper is intentionally limited in scope to a compact but richer theoretical contribution.
    - a. Good theory style is essential. Mathematical formalism is kept to a minimum. Each piece of formalism contributes to the economic claims. The paper avoids pompous or ceremonial formalism, and it avoids auxiliary formal detours that do not advance the main argument.
    - b. The empirical content remains very limited, ideally to a single figure in the introduction illustrating the valuation of publicly traded AI stocks compared with non-AI stocks using CRSP data.
    - c. The paper does not try to generate a broad menu of novel testable predictions beyond the model's main arguments.
    - d. The paper may include rough quantitative parameterizations for illustration, but quantitative material remains illustrative rather than becoming a calibration or estimation exercise.
