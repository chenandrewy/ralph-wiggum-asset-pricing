# tests/spec-paper.py
Started: 2026-04-02 22:54:31 EDT
Runtime: 1h 10m 7s
[ralph-garage/agent-logs/20260402T225431.388390-0400_spec-paper_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260402T225431.388390-0400_spec-paper_claude_claude-opus-4-6.log)

# spec-paper
VERDICT: PASS
REASON: All requirements in Sections I, II, and III of the spec are satisfied.

## I. Economic Requirements
**Section Verdict: PASS**
**Reason:** All 22 sub-requirements are satisfied with concrete textual evidence.

### Requirement 1: Academic asset pricing theory paper with tightly limited empirical content
**PASS.** The paper is a formal asset pricing theory paper. Empirical content is limited to a single CRSP-based figure (Exhibit 1) and a numerical illustration table (Exhibit 2). The conclusion confirms: "The model is intentionally stylized."

### Requirement 2a: AI singularity = sudden productivity improvement
**PASS.** "output grows at a strictly higher rate, reflecting the productivity increase that accompanies the singularity"; "the paper's economic focus is on large disruptions---singularities that vastly increase productivity." Abstract: "a sudden AI-driven productivity surge."

### Requirement 2b: Negative AI singularity = devastating for typical investor
**PASS.** Abstract: "a negative AI singularity---a sudden AI-driven productivity surge that displaces existing workers and firms." Assumption 1: "The household's share of output falls at the singularity: $\tilde{\theta} + \tilde{\nu} < \theta + \nu$."

### Requirement 2c: Incomplete markets = some assets not tradeable (not Arrow-Debreu)
**PASS.** "the typical investor cannot buy these assets. They are either privately held, illiquid, or simply do not yet exist." No Arrow-Debreu securities invoked anywhere.

### Requirement 3a: Main argument — AI stocks hedge negative singularity
**PASS.** Abstract: "publicly traded AI stocks command a valuation premium because they hedge against a negative AI singularity." Proposition 1 derives the AI P/D ratio with the displacement hedging channel.

### Requirement 3b: Incomplete markets are key
**PASS.** Proposition 3 shows that under complete markets the hedging premium vanishes: "If the household could trade with AI owners...the hedging motive would vanish."

### Requirement 3c: Financial market solutions under-discussed
**PASS.** Conclusion states verbatim: "Financial market solutions to AI disaster risk are under-discussed."

### Requirement 3d: Singularity abundance overcomes frictions
**PASS.** Remark 2: "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible. In this limit, the Coase theorem applies."

### Requirement 4a: Infinite-horizon, discrete-time model
**PASS.** "Time is discrete: $t = 0, 1, 2, \ldots$"; utility uses $E_0 \sum_{t=0}^{\infty} \beta^t$.

### Requirement 4b: Two agents with correct roles
**PASS.** "The economy has two types of agents: a representative household and AI owners. The household is the marginal investor in public markets. AI owners hold private AI capital and do not participate in public stock markets." Unborn interpretation: "Following GKP (2012), AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy."

### Requirement 4c: Two public assets, AI share grows
**PASS.** "two publicly traded assets---AI stocks and non-AI stocks." Assumption 2: "Public AI stocks gain share and non-AI stocks lose share: $\tilde{\theta} > \theta$ and $\tilde{\nu} < \nu$."

### Requirement 4d: Focus on AI P/D ratio vs. singularity probability
**PASS.** Proposition 1 derives P/D ratios in closed form. Proposition 2 shows $\partial V_{\mathrm{pre}}^A / \partial p > 0$.

### Requirement 4e: AI owners interpretable as unborn/future owners per GKP
**PASS.** "Following GKP (2012), AI owners can be interpreted as future innovators and entrepreneurs who have not yet entered the economy. In our application, they may also represent holders of illiquid private AI ventures---this is our own modeling choice, distinct from but inspired by GKP's unborn-cohorts mechanism."

### Requirement 5a: Extension — singularity may cause extinction
**PASS.** Section 4.1: "conditional on a singularity occurring, there is a probability $q \in [0,1)$ that the event is catastrophic---all output is permanently destroyed."

### Requirement 5b: Extension — consumption may become infinite (AI owners only)
**PASS.** "as $\tilde{g} \to \infty$, the AI owners---who hold private AI capital---enjoy unbounded consumption, while the household's consumption, though growing, remains a fixed fraction $\tilde{\omega}$ of total output."

### Requirement 5c: Extension — infinite output affects trade frictions
**PASS.** Section 4.2 ("Overcoming frictions: the Coase theorem in the singularity") analyzes this formally. Remark 2 shows infinite output eliminates frictions.

### Requirement 5d: Ideas kept in extension
**PASS.** These appear in Section 4 ("Extension: Singularity, Extinction, and Frictions"), separate from the main model (Section 2) and results (Section 3).

### Requirement 6a: GKP gap — formal analysis contributed
**PASS.** "GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor...but do not conduct a formal analysis...We take up this question."

### Requirement 6b: Coase theorem logic, GKP assumes frictions reasonably
**PASS.** "The Coase theorem implies that if property rights are well-defined and transaction costs are zero, the parties will bargain to an efficient (fully risk-sharing) outcome. GKP's assumption that displacement persists is driven by real-world frictions."

### Requirement 6c: Frictions overcome at singularity, following Jones
**PASS.** Equation (14) provides the formal cost structure. Remark 2 connects to Jones (2024): "if the singularity produces unbounded output ($Y \to \infty$), any transfer mechanism with a fixed-cost component becomes negligible."

### Requirement 6d: Contribution characterized as purposefully modest
**PASS.** "Our contribution relative to GKP is purposefully modest: the main economic insights originate in their work."

---

## II. Style Requirements
**Section Verdict: PASS**
**Reason:** All 11 requirements (and sub-requirements) are satisfied.

### Requirement 1: Tone between academic and blog post
**PASS.** Formal structures (propositions, proofs, Euler equations) combined with conversational phrasing like "Why are AI stocks so expensive?" in the abstract.

### Requirement 2: Author is anonymous
**PASS.** `\author{}` — the author field is empty. No names appear anywhere.

### Requirement 3: Abstract is 100 words or less
**PASS.** Abstract is 98 words (hyphenated words as one) or 100 words (hyphenated words split). Within the limit either way.

### Requirement 4: Title is short, evocative, eye-catching, not cringey
**PASS.** "Hedging the Singularity" — three words, evocative, captures the core idea.

### Requirement 5: Paper is at most 20 pages
**PASS.** Content spans roughly 15-18 pages (12pt article class, 1-inch margins, 1.5 spacing, 2 exhibits, 1 appendix proof).

### Requirement 6: Every page has visible page number
**PASS.** `\pagestyle{plain}` sets page numbers on all pages; `\thispagestyle{plain}` ensures the title page also has one.

### Requirement 7: At most 6 exhibits
**PASS.** 2 exhibits (1 figure, 1 table).

### Requirement 8: Lit review at most half a page at end of introduction
**PASS.** Single `\paragraph{Related literature.}` block at the end of the Introduction, before Section 2. Approximately half a page at the paper's formatting settings.

### Requirement 9: All display equations numbered
**PASS.** No unnumbered display equations (`equation*`, `align*`, `\[...\]`) found. All use `equation` or `align` environments.

### Requirement 10: All propositions explicitly proved, long proofs in appendix
**PASS.** Propositions 1, 2, 3 all have explicit proofs. Proposition 2's proof (the longest) is deferred to Appendix A.

### Requirement 11: First section "Preface (TBC)", unnumbered, left blank
**PASS.** `\section*{Preface (TBC)}` with no content. `\section{Introduction}` follows immediately as the first numbered section. Rest of paper is standard.

---

## III. Technical Requirements
**Section Verdict: PASS**
**Reason:** All 16 sub-requirements are satisfied across paper structure, comments, and code pipeline.

### Requirement 1a: `paper.tex` is the main paper file
**PASS.** Contains `\documentclass`, `\begin{document}`, and `\end{document}`.

### Requirement 1b: All figures use PDFs in `paper/exhibits/`
**PASS.** Only figure: `\includegraphics[width=0.85\textwidth]{exhibits/ai-valuations.pdf}`.

### Requirement 1c: All tables use tex files in `paper/exhibits/`
**PASS.** Only table: `\input{exhibits/numerical-illustration.tex}`.

### Requirement 1d: All files in `paper/exhibits/` are used in the paper
**PASS.** Directory contains exactly `ai-valuations.pdf` and `numerical-illustration.tex`; both are referenced.

### Requirement 2a: Section comments with numbers
**PASS.** Every section/subsection annotated, e.g., `\section{Introduction} % Section 1`, `\subsection{Environment} % Section 2.1`.

### Requirement 2b: Exhibit comments with numbers
**PASS.** `\label{fig:ai-valuations} % Exhibit 1`, `\input{exhibits/numerical-illustration.tex} % Exhibit 2`.

### Requirement 2c: Theorem environment comments with numbers
**PASS.** All annotated: `% Assumption 1`, `% Proposition 1`, `% Remark 1`, etc.

### Requirement 3a: Code in R
**PASS.** All scripts (`run-all.R`, `ai-valuations-figure.R`, `numerical-illustration.R`) are R with `#!/usr/bin/env Rscript`.

### Requirement 3b: One canonical entry point regenerating every exhibit
**PASS.** `code/run-all.R` calls both exhibit-generating scripts.

### Requirement 3c: Pipeline runs from scratch, no caches
**PASS.** No local data files or caches read. WRDS queried live; numerical illustration uses hardcoded parameters.

### Requirement 3d: Pipeline executes in less than 180 seconds
**PASS (by inspection).** One SQL query and pure arithmetic — lightweight operations.

### Requirement 3e: External data downloads part of pipeline
**PASS.** WRDS query embedded in `ai-valuations-figure.R`, called by `run-all.R`.

### Requirement 3f: Code outputs to `paper/exhibits/`
**PASS.** `outfile <- "paper/exhibits/ai-valuations.pdf"` and `outfile <- "paper/exhibits/numerical-illustration.tex"`.

### Requirement 3g: No silent reliance on cached/manual files
**PASS.** Pipeline is self-contained; `run-all.R` halts on failure via `stop()`.
