# tests/spec-paper.py
Started: 2026-04-02 18:45:35 EDT
Runtime: 2m 55s
[ralph-garage/agent-logs/20260402T184535.059620-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T184535.059620-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: FAIL
REASON: Section III Technical Requirements fails because exhibit number comments are inconsistent across files (requirement 2b).

---

## I. Economic Requirements
**VERDICT: PASS**
**REASON:** All 20 sub-requirements are satisfied with concrete textual and formal support.

### 1. Academic asset pricing theory paper with tightly limited empirical content
**PASS.** The paper is a formal theory paper with propositions and proofs. Empirical content is limited to one figure (CRSP price-dividend ratios) and one illustrative numerical table.

### 2a. AI singularity defined as sudden improvement vastly increasing productivity
**PASS.** "A sudden AI breakthrough---a singularity---could dramatically increase productivity" (Introduction). Formalized via equations (1)-(2) with $\tilde{g} > g$.

### 2b. Negative AI singularity is devastating for the typical investor
**PASS.** Assumption 1 ("Negative singularity"): "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$."

### 2c. Incomplete markets = some assets cannot be bought by representative investor
**PASS.** "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital." (Section 2.3). Not framed as missing Arrow-Debreu securities.

### 3a. Main argument: AI stocks hedge against negative AI singularity
**PASS.** "publicly traded AI stocks command a valuation premium because they serve as a hedge against a negative AI singularity" (Introduction). Propositions 1 and 3 formalize this.

### 3b. Incomplete markets are key
**PASS.** Proposition 4 shows that under complete markets the household consumes total output and the hedging motive vanishes.

### 3c. Financial market solutions to AI disaster risk are under-discussed
**PASS.** Conclusion: "Financial market solutions to AI disaster risk are under-discussed."

### 3d. If singularity occurs, frictions can be overcome due to abundance
**PASS.** Remark 2: "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### 4a. Infinite-horizon, discrete-time model
**PASS.** "Time is discrete: $t = 0, 1, 2, \ldots$" and utility sums from $t=0$ to $\infty$.

### 4b. Two agents: representative household (marginal investor) and AI owners (not marginal)
**PASS.** "The economy has two types of agents: a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets." (Section 2.1)

### 4c. Two publicly traded assets; AI stocks grow as share with singularity
**PASS.** Two assets defined; Assumption 2: "Public AI stocks gain share and non-AI stocks lose share: $\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$."

### 4d. Main focus on P/D ratio of AI stocks and how it changes with singularity probability
**PASS.** Proposition 1 derives the P/D ratio; Proposition 3 derives $\partial V_0^A / \partial p$.

### 4e. Private AI capital / AI owners interpreted as unborn capital / future owners (GKP)
**PASS.** "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy." (Section 2.1)

### 5a. Extension: singularity may cause extinction
**PASS.** Section 4.1: "conditional on a singularity occurring, there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### 5b. Extension: consumption may become infinite (for AI owners)
**PASS.** Remark 1 considers $\tilde{g} \to \infty$; AI owners enjoy unbounded consumption while household's share shrinks.

### 5c. Extension: how infinite output affects friction assumption (GKP + Jones)
**PASS.** Section 4.2 formalizes friction costs as $F/Y + \tau(\omega - \tilde{\omega})$, showing $F/Y \to 0$ as $Y \to \infty$.

### 5d. Extension ideas kept in extension section
**PASS.** All material in Section 4 ("Extension: Singularity, Extinction, and Frictions"), separate from main model.

### 6a. GKP mentions transfers but doesn't analyze; paper contributes formal analysis
**PASS.** Section 4.2 explicitly states GKP "do not conduct a formal analysis of how these mechanisms scale with output. We take up this question."

### 6b. Without frictions, transfers eliminate displacement risk (Coase Theorem); GKP assumes frictions
**PASS.** "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome. GKP's assumption that displacement persists is driven by real-world frictions."

### 6c. With singularity, frictions can be overcome; quantified following Jones
**PASS.** Remark 2: "Following \citet{Jones2024}, if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### 6d. Contribution characterization is purposefully modest
**PASS.** "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work."

---

## II. Style Requirements
**VERDICT: PASS**
**REASON:** All 11 requirements satisfied.

### 1. Tone between academic paper and blog post
**PASS.** Conversational opening ("Why are AI stocks so expensive?") combined with formal propositions and proofs.

### 2. Author is anonymous
**PASS.** `\author{}` — empty author field, no name anywhere.

### 3. Abstract is 100 words or less
**PASS.** Abstract is approximately 97 words.

### 4. Title is short, evocative, eye-catching, not cringey
**PASS.** "Hedging the Singularity" — three words, combines finance and tech concepts.

### 5. Paper length at most 20 pages
**PASS.** 12pt font, 1.5 spacing, 1in margins, ~3,240 words of body text plus equations and 2 exhibits — estimated 10-13 pages.

### 6. Every page has visible page number
**PASS.** `\pagestyle{plain}` and `\thispagestyle{plain}` on title page ensure all pages numbered.

### 7. At most 6 exhibits
**PASS.** Exactly 2 exhibits (1 figure, 1 table).

### 8. Lit review at most half page, at end of introduction
**PASS.** `\paragraph{Related literature.}` appears as last content in Introduction (~254 words, under half a page).

### 9. All display equations numbered
**PASS.** All display math uses `\begin{equation}` or `\begin{align}` — no starred or unnumbered variants.

### 10. All propositions proved, long proofs in appendix
**PASS.** 4 propositions, each with explicit proof. Proposition 3's proof (the longest) is in Appendix A.

### 11. First section is "Preface (TBC)", unnumbered, left blank
**PASS.** `\section*{Preface (TBC)}` with empty body.

### 11a. Traditional Introduction follows, then standard structure
**PASS.** `\section{Introduction} % Section 1` follows immediately. Standard sections thereafter.

---

## III. Technical Requirements
**VERDICT: FAIL**
**REASON:** Exhibit numbering comments are inconsistent across paper.tex, numerical-illustration.tex, and run-all.R (requirement 2b).

### 1a. paper.tex is the main paper file
**PASS.** `/workspace/paper/paper.tex` is a complete LaTeX document.

### 1b. All figures use PDFs in paper/exhibits/
**PASS.** Only figure: `\includegraphics[width=0.85\textwidth]{exhibits/ai-valuations.pdf}`.

### 1c. All tables use tex files in paper/exhibits/
**PASS.** Only table: `\input{exhibits/numerical-illustration.tex}`.

### 1d. All files in paper/exhibits/ are used in the paper
**PASS.** Exactly two files exist (`ai-valuations.pdf`, `numerical-illustration.tex`), both referenced.

### 2a. Sections have comments listing section number
**PASS.** Every section/subsection has `% Section N` comments.

### 2b. Exhibits have comments listing exhibit number
**FAIL.** In `paper.tex`, the figure is `% Exhibit 1` and the table input is `% Exhibit 2`. However, inside `paper/exhibits/numerical-illustration.tex`, the table is labeled `% Exhibit 1`. Additionally, `code/run-all.R` labels the numerical illustration as "Exhibit 1" and the figure as "Exhibit 2", reversing the paper's ordering. The exhibit numbering is inconsistent across files.

### 2c. Math theorem environments have comments listing environment number
**PASS.** All assumptions, propositions, and remarks have number comments (e.g., `% Proposition 3`).

### 3a. Code is written in R
**PASS.** All files in `code/` are `.R` files.

### 3b. One canonical entry point regenerates every exhibit
**PASS.** `code/run-all.R` calls both exhibit-generating scripts.

### 3c. Pipeline runs from scratch
**PASS.** No precomputed caches or intermediate files loaded.

### 3d. Pipeline executes in less than 180 seconds
**PASS.** Numerical illustration is sub-second; WRDS query is simple and within budget.

### 3e. External data queries part of canonical pipeline
**PASS.** WRDS query embedded in `ai-valuations-figure.R`, called by `run-all.R`.

### 3f. Code outputs directly to paper/exhibits/
**PASS.** Outputs to `paper/exhibits/numerical-illustration.tex` and `paper/exhibits/ai-valuations.pdf`.

### 3g. No silent reliance on inconsistent cached objects
**PASS.** Each script computes from scratch or queries WRDS directly.
