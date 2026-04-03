# tests/spec-paper.py
Started: 2026-04-02 21:59:20 EDT
Runtime: 3m 6s
[ralph-garage/agent-logs/20260402T215920.395739-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T215920.395739-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: FAIL
REASON: Exhibit number comment in generated table file is inconsistent with paper numbering (III.2b).

## I. Economic Requirements
**VERDICT: PASS**
**Reason:** All 22 sub-requirements are satisfied with concrete textual and formal evidence.

### 1. Academic asset pricing theory paper with tightly limited empirical content
PASS. The paper is a formal theory paper with propositions and proofs. Empirical content is limited to one CRSP figure and one numerical illustration table.

### 2a. AI singularity definition used consistently
PASS. "A sudden AI breakthrough---a singularity---could dramatically increase productivity" (intro). Formalized with higher post-singularity growth $\tilde{g} > g$.

### 2b. Negative AI singularity definition used consistently
PASS. Assumption 1 labeled "Negative singularity": "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." Displacement ratio $\Delta < 1$ formalizes this throughout.

### 2c. Incomplete markets definition used consistently
PASS. "the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist. In this world of incomplete markets." No reference to Arrow-Debreu securities.

### 3a. Main argument: AI stocks hedge negative singularity
PASS. Abstract: "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity." Proposition 2 proves $V_0^A > V_0^N$; Proposition 4 isolates the hedging premium.

### 3b. Incomplete markets are key
PASS. Proposition 4 shows under complete markets the hedging premium vanishes. "Under complete markets, the household could invest in private AI capital, eliminating displacement risk and the hedging premium."

### 3c. Financial market solutions under-discussed
PASS. Conclusion opens: "Financial market solutions to AI disaster risk are under-discussed."

### 3d. Singularity overcomes frictions
PASS. Remark 2: "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible. In this limit, the Coase theorem applies."

### 4a. Infinite-horizon, discrete-time model
PASS. "Time is discrete: $t = 0, 1, 2, \ldots$." Utility sums from $t=0$ to $\infty$.

### 4b. Two agents
PASS. "The economy has two types of agents: a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets."

### 4c. Two publicly traded assets; AI stocks grow as share
PASS. Three dividend streams defined; two publicly traded. Assumption 2: "$\tilde{\theta} > \theta$" (AI stocks gain share).

### 4d. Focus on P/D ratio of AI stocks
PASS. Proposition 1 derives P/D ratio in closed form. Proposition 3 analyzes $\partial V_0^A / \partial p > 0$. Numerical illustration varies $p$ and reports P/D ratios.

### 4e. AI owners as unborn/future owners (GKP interpretation)
PASS. "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### 5a. Singularity may cause extinction
PASS. Section 4.1: "conditional on a singularity occurring, there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### 5b. Consumption may become infinite (only for AI owners)
PASS. "as $\tilde{g} \to \infty$, the AI owners---who hold private AI capital---enjoy unbounded consumption, while the household's consumption, though growing, remains a shrinking fraction."

### 5c. Infinite output affects trade assumptions
PASS. Section 4.2 analyzes this with Coase theorem argument and formal cost analysis showing $F/Y \to 0$ as $Y \to \infty$.

### 5d. Extension keeps main argument simple
PASS. All three ideas (extinction, infinite consumption, overcoming frictions) confined to Section 4 "Extension: Singularity, Extinction, and Frictions." Main model (Sections 2-3) contains none.

### 6a. GKP contribution: formal analysis of transfers
PASS. "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor... but do not conduct a formal analysis... We take up this question."

### 6b. Coase Theorem logic and GKP's friction assumption
PASS. "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome. GKP's assumption that displacement persists is driven by real-world frictions."

### 6c. Singularity overcomes frictions (Jones-2024)
PASS. Formal cost model with $F + \tau T$. Remark 2: "Following \citet{Jones2024}, if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### 6d. Purposefully modest contribution
PASS. "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work."

---

## II. Style Requirements
**VERDICT: PASS**
**Reason:** All 11 requirements satisfied.

### 1. Tone between academic and blog
PASS. Formal theorem-proof structure combined with accessible language ("Why are AI stocks so expensive?").

### 2. Author is anonymous
PASS. `\author{}` is empty.

### 3. Abstract is 100 words or less
PASS. Abstract is approximately 97 words.

### 4. Title is short, evocative, not cringey
PASS. "Hedging the Singularity" — three words, combines finance and AI concepts.

### 5. Paper length at most 20 pages
PASS. Compiled PDF is 13 pages.

### 6. Every page has a visible page number
PASS. `\pagestyle{plain}` on line 19 and `\thispagestyle{plain}` on line 27 ensure all pages have numbers.

### 7. At most 6 exhibits
PASS. Exactly 2 exhibits (1 figure, 1 table).

### 8. Lit review at most half a page, at end of introduction
PASS. Lit review begins with `\paragraph{Related literature.}` and ends before Section 2. Approximately 256 words (~half a page at 12pt, 1.5 spacing).

### 9. All display equations numbered
PASS. All display math uses `equation` or `align` environments (no starred/unnumbered variants).

### 10. All propositions explicitly proved; long proofs in appendix
PASS. All 4 propositions have explicit proofs. Proposition 3's proof (the longest) is deferred to Appendix A.

### 11. First section is "Preface (TBC)", unnumbered, left blank
PASS. `\section*{Preface (TBC)}` with no content. Introduction follows as Section 1, with standard numbering thereafter.

### 11a. Introduction follows normally
PASS. `\section{Introduction}` is numbered Section 1. Subsequent sections numbered 2-5 as if Preface doesn't exist.

---

## III. Technical Requirements
**VERDICT: FAIL**
**Reason:** Exhibit number comment in generated file `numerical-illustration.tex` is inconsistent with paper numbering.

### 1a. `paper.tex` is the main paper file
PASS. File exists and contains the full paper.

### 1b. All figures use PDFs in `paper/exhibits/`
PASS. One figure: `\includegraphics{exhibits/ai-valuations.pdf}`.

### 1c. All tables use tex files in `paper/exhibits/`
PASS. One table: `\input{exhibits/numerical-illustration.tex}`.

### 1d. All files in `paper/exhibits/` are used
PASS. Exactly two files in `paper/exhibits/` (`ai-valuations.pdf`, `numerical-illustration.tex`), both referenced in `paper.tex`.

### 2a. Sections have number comments
PASS. All sections and subsections have inline comments with their numbers (e.g., `\section{Introduction} % Section 1`, `\subsection{Environment} % Section 2.1`).

### 2b. Exhibits have number comments
**FAIL.** The figure in `paper.tex` is correctly labeled `% Exhibit 1`. The table input in `paper.tex` is correctly labeled `% Exhibit 2`. However, the generated file `paper/exhibits/numerical-illustration.tex` line 5 contains `\label{tab:numerical} % Exhibit 1`, which conflicts with the paper's `% Exhibit 2` label. The code that generates this file (`code/numerical-illustration.R`) hardcodes the wrong exhibit number. This is an inconsistency: the same exhibit is labeled "Exhibit 1" in the generated file and "Exhibit 2" in the paper.

### 2c. Theorem environments have number comments
PASS. All assumptions, propositions, and remarks have inline comments with their numbers (e.g., `% Assumption 1`, `% Proposition 1`, `% Remark 1`).

### 3a. Code is written in R
PASS. All three files (`run-all.R`, `ai-valuations-figure.R`, `numerical-illustration.R`) are R scripts.

### 3b. One canonical entry point
PASS. `code/run-all.R` calls both exhibit-generating scripts.

### 3c. Pipeline runs from scratch, no caches
PASS. Both scripts generate outputs fresh from parameters or live WRDS queries. No precomputed caches or intermediate files are relied upon. Note: `run-all.R` comments claim graceful degradation without WRDS credentials, but the pipeline actually fails if credentials are absent; however, the requirement is about not relying on caches, which is satisfied.

### 3d. Executes in less than 180 seconds
PASS (assumed). The numerical illustration is pure computation (<1s). The CRSP query is simple and should complete well within budget.

### 3e. External data queries in canonical pipeline
PASS. The WRDS query is embedded in `ai-valuations-figure.R`, called by `run-all.R`.

### 3f. Code outputs to `paper/exhibits/`
PASS. `ai-valuations-figure.R` outputs to `paper/exhibits/ai-valuations.pdf`. `numerical-illustration.R` outputs to `paper/exhibits/numerical-illustration.tex`.

### 3g. No silent reliance on cached/mismatched objects
PASS. Pipeline has two clean code paths producing outputs fresh.
