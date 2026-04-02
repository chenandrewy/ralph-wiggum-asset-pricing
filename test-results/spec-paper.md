# tests/spec-paper.py
Started: 2026-04-02 18:34:30 EDT
Runtime: 3m 27s
[ralph-garage/agent-logs/20260402T183430.355625-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T183430.355625-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: FAIL
REASON: Style Req 9 (display equation numbering) and Technical Req 2b (exhibit numbering comments) have strict violations.

---

## I. Economic Requirements
**SECTION VERDICT: PASS**
**Reason:** All 22 requirements and sub-requirements are satisfied with concrete formal content.

### Requirement 1: Academic asset pricing theory paper with tightly limited empirical content
**SATISFIED.** The paper is a formal asset pricing theory paper with CRRA preferences, Euler equations, four propositions with proofs. Empirical content is limited to one CRSP figure and one numerical illustration table.

### Requirement 2a: AI singularity defined as sudden productivity improvement
**SATISFIED.** Line 84: "The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output." Introduction (line 43): "a sudden AI breakthrough---a singularity---could dramatically increase productivity."

### Requirement 2b: Negative AI singularity is devastating for the typical investor
**SATISFIED.** Assumption 1 (line 103): "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$." Displacement ratio $\Delta < 1$ is defined.

### Requirement 2c: Incomplete markets means some assets cannot be bought by the representative investor
**SATISFIED.** Lines 123-128: "The household trades in two publicly available assets---AI stocks and non-AI stocks---but cannot invest in private AI capital." Framed as inability to invest in private capital, not missing Arrow-Debreu securities. Proposition 4 contrasts incomplete vs. complete markets in these terms.

### Requirement 3a: Main argument — AI stocks hedge against negative singularity
**SATISFIED.** Proposition 1 gives P/D ratio. Proposition 2 proves AI stocks trade at a premium. Proposition 4 isolates the hedging premium. Abstract: "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity."

### Requirement 3b: Incomplete markets are key
**SATISFIED.** Proposition 4 (lines 214-230) proves that under complete markets the hedging premium vanishes. Line 230: "If the household could trade with AI owners...the household's consumption would not fall at the singularity, and the hedging motive would vanish."

### Requirement 3c: Financial market solutions to AI disaster risk are under-discussed
**SATISFIED.** Lines 295-296: "Financial market solutions to AI disaster risk are under-discussed. Our analysis suggests that expanding the set of tradeable AI-related assets...could reduce the displacement premium and improve welfare by completing markets."

### Requirement 3d: Singularity allows frictions to be overcome
**SATISFIED.** Section 4.2 (lines 260-282). Remark 2 (line 278): "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### Requirement 4a: Infinite-horizon, discrete-time model
**SATISFIED.** Line 76: "Time is discrete: $t = 0, 1, 2, \ldots$" Line 121: household maximizes $E_0 \sum_{t=0}^{\infty} \beta^t \frac{c_t^{1-\gamma}}{1-\gamma}$.

### Requirement 4b: Two agents (household as marginal investor, AI owners with private capital)
**SATISFIED.** Lines 86-87: "The economy has two types of agents: a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets. Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### Requirement 4c: Two publicly traded assets, AI stocks grow share with singularity
**SATISFIED.** Lines 90-94 define public AI stocks and non-AI stocks. Assumption 2 (line 107): "Public AI stocks gain share and non-AI stocks lose share: $\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$."

### Requirement 4d: Main focus on P/D ratio and how it changes with singularity probability
**SATISFIED.** Proposition 1 derives P/D ratio. Proposition 3 (line 200) shows $\partial V_0^A / \partial p > 0$. Numerical illustration reports P/D ratios for several values of $p$.

### Requirement 4e: Private AI capital as unborn capital, following GKP
**SATISFIED.** Lines 86-87: "Following \citet{GKP2012}, AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### Requirement 5a: Singularity may cause extinction
**SATISFIED.** Section 4.1 (line 246): "Suppose that, conditional on a singularity occurring, there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### Requirement 5b: Consumption may become infinite (only for AI owners)
**SATISFIED.** Remark 1 (lines 254-256): "as $\tilde{g} \to \infty$, the AI owners---who hold private AI capital---enjoy unbounded consumption, while the household's consumption, though growing, remains a shrinking fraction $\tilde{\omega}$ of total output."

### Requirement 5c: How infinite output affects the assumption agents cannot trade
**SATISFIED.** Section 4.2 (lines 260-282) formalizes how infinite output makes fixed friction costs negligible (eq. 17), enabling Coasean risk-sharing. Remark 2 states the result formally.

### Requirement 5d: Keep these ideas in an extension
**SATISFIED.** All of 5a-5c appear in Section 4 ("Extension"), clearly separated from the main model (Section 2) and results (Section 3).

### Requirement 6a: Formal analysis of displacement factor magnitude (GKP gap)
**SATISFIED.** Line 262: "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor...but do not conduct a formal analysis." Equations (15) and (17) plus Remark 2 provide the formal analysis.

### Requirement 6b: Coase theorem logic and GKP's friction assumption
**SATISFIED.** Lines 268-270: "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome. GKP's assumption that $\lambda < 1$ is driven by real-world frictions."

### Requirement 6c: Jones-2024 modeling of friction quantification
**SATISFIED.** Lines 272-279: "Following \citet{Jones2024}, if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible." Friction cost formula shows $F/Y \to 0$ as $Y \to \infty$.

### Requirement 6d: Purposefully modest characterization of contribution
**SATISFIED.** Line 63: "Our contribution relative to GKP is purposefully modest: the main economic insights about displacement risk and incomplete markets originate in their work."

---

## II. Style Requirements
**SECTION VERDICT: FAIL**
**Reason:** Requirement 9 violated — two display lines in the appendix use `\notag` and are unnumbered.

### Requirement 1: Tone between academic paper and blog post
**SATISFIED.** Formal proposition-proof structure (academic) combined with conversational phrasing like "Why are AI stocks so expensive?" (line 30). The tone is accessible without being informal.

### Requirement 2: Author is anonymous
**SATISFIED.** Line 22: `\author{}` — the author field is empty.

### Requirement 3: Abstract is 100 words or less
**SATISFIED.** Abstract is approximately 98 words, within the limit.

### Requirement 4: Title is short, evocative, eye-catching, not cringey
**SATISFIED.** Line 21: `\title{Hedging the Singularity}` — three words, evocative, not cringey.

### Requirement 5: Paper length at most 20 pages
**SATISFIED.** 12pt article class, 1-inch margins, 1.5 spacing, with 5 sections plus short appendix. Estimated 15-18 pages.

### Requirement 6: Every page has a visible page number
**SATISFIED.** Line 19: `\pagestyle{plain}` sets page numbers on every page. Line 27: `\thispagestyle{plain}` ensures the title page also has one.

### Requirement 7: At most 6 exhibits
**SATISFIED.** Two exhibits total (one figure, one table). Well within limit.

### Requirement 8: Lit review at most half a page, at end of introduction
**SATISFIED.** Literature review begins at line 62 with `\paragraph{Related literature.}` and is the final content of Section 1 before Section 2 begins. Approximately 2 paragraphs (~half a page at 1.5 spacing).

### Requirement 9: All display equations numbered
**NOT SATISFIED.** Lines 312-313 in the appendix proof use `\notag` on two intermediate lines within an `\begin{align}...\end{align}` environment. Under strict reading, these are unnumbered display equation lines. The spec states "all display equations should be numbered" without exception.

Evidence:
```latex
\begin{align}
&\bigl[-R + \Phi^A(1+V_1)\bigr]\bigl[1-(1-p)R\bigr] - ... \notag \\
&= -R + \Phi^A(1+V_1) - R\,\Phi^A(1+V_1) \notag \\
&= \Phi^A(1+V_1)(1 - R) - R. \label{eq:numerator}
\end{align}
```

### Requirement 10: All propositions explicitly proved, long proofs in appendix
**SATISFIED.** Propositions 1, 2, and 4 have inline proofs. Proposition 3's proof is deferred to Appendix A (line 209: "See Appendix~\ref{app:proofs}"). All four propositions are proved.

### Requirement 11: First section "Preface (TBC)", unnumbered, left blank
**SATISFIED.** Line 36: `\section*{Preface (TBC)}` — unnumbered, body is empty.

### Requirement 11a: Traditional Introduction follows
**SATISFIED.** Line 41: `\section{Introduction} % Section 1` — numbered Section 1 immediately follows the Preface.

---

## III. Technical Requirements
**SECTION VERDICT: FAIL**
**Reason:** Requirement 2b violated — exhibit numbering comments are inconsistent (both exhibits labeled "Exhibit 1").

### Requirement 1a: paper.tex is the main paper file
**SATISFIED.** `/workspace/paper/paper.tex` exists and is the sole LaTeX source file.

### Requirement 1b: All figures use PDFs in paper/exhibits/
**SATISFIED.** The only figure uses `exhibits/ai-valuations.pdf` (line 47). File exists at `/workspace/paper/exhibits/ai-valuations.pdf`.

### Requirement 1c: All tables use tex files in paper/exhibits/
**SATISFIED.** The only table uses `\input{exhibits/numerical-illustration.tex}` (line 235). File exists.

### Requirement 1d: All files in paper/exhibits/ are used in the paper
**SATISFIED.** `paper/exhibits/` contains exactly `ai-valuations.pdf` and `numerical-illustration.tex`. Both are referenced in paper.tex.

### Requirement 2a: Section comments with section numbers
**SATISFIED.** All sections and subsections have comments listing their number (e.g., `% Section 1`, `% Section 2.1`, `% Appendix A`).

### Requirement 2b: Exhibit comments with exhibit numbers
**NOT SATISFIED.** Both exhibits are labeled "Exhibit 1":
- Figure (line 49 of paper.tex): `\label{fig:ai-valuations} % Exhibit 1`
- Table (line 5 of numerical-illustration.tex): `\label{tab:numerical} % Exhibit 1`

The table should be labeled "Exhibit 2". Additionally, the `\input` line for the table in paper.tex (line 235) has no exhibit comment — the comment only exists inside the included file.

### Requirement 2c: Math theorem environment comments with numbers
**SATISFIED.** All assumptions (1-3), propositions (1-4), and remarks (1-2) have comments listing their number.

### Requirement 3a: Code written in R
**SATISFIED.** All files in `code/` are R scripts: `run-all.R`, `numerical-illustration.R`, `ai-valuations-figure.R`.

### Requirement 3b: One canonical entry point regenerating every exhibit
**SATISFIED.** `code/run-all.R` sources both exhibit-generating scripts.

### Requirement 3c: Pipeline runs from scratch
**SATISFIED.** No precomputed caches or intermediate files. Parameters are hardcoded; WRDS query runs live.

### Requirement 3d: Pipeline executes in less than 180 seconds
**NOT VERIFIED.** Cannot execute in test environment. Structurally plausible (one WRDS query + simple computation).

### Requirement 3e: External data queries part of pipeline
**SATISFIED.** WRDS query is embedded directly in `ai-valuations-figure.R`, called by `run-all.R`.

### Requirement 3f: Code outputs to paper/exhibits/
**SATISFIED.** `numerical-illustration.R` writes to `paper/exhibits/numerical-illustration.tex`. `ai-valuations-figure.R` writes to `paper/exhibits/ai-valuations.pdf`.

### Requirement 3g: No silent reliance on cached objects
**SATISFIED.** No caching mechanisms present. Each run regenerates from scratch.
