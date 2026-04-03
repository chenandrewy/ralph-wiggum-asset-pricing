# tests/quality-writing.py
Started: 2026-04-02 21:49:42 EDT
Runtime: 3m 30s
[ralph-garage/agent-logs/20260402T214942.812357-0400_quality-writing_claude_opus.log](../ralph-garage/agent-logs/20260402T214942.812357-0400_quality-writing_claude_opus.log)

# quality-writing
VERDICT: FAIL
REASON: The conclusion lapses into mechanical recap prose that a reader would skim, failing the "compelling throughout" standard.

---

## Requirement 1: Abstract
**Sub-verdict: PASS**

The abstract opens with "Why are AI stocks so expensive?" — a direct, attention-grabbing question that would stand out in a JF table of contents. It immediately states the main mechanism (hedging against a negative AI singularity under incomplete markets), delivers the key result (price-dividend ratio increases with singularity probability), and previews the complete-markets benchmark and the abundance extension. The abstract is specific to this paper — no other paper could be described by this text. It is not boilerplate, does not bury the insight, and makes no unsupported claims.

---

## Requirement 2: Introduction flow
**Sub-verdict: PASS**

Paragraph-by-paragraph evaluation:

1. **"The recent surge in AI stock valuations has drawn widespread attention."** Establishes the empirical puzzle (AI stocks are expensive) and proposes the paper's channel (hedging against a negative AI singularity). Forward link: what is a negative AI singularity, and why would it generate a hedge?

2. **"Consider a representative investor whose wealth is largely tied to existing firms and human capital."** Delivers the economic intuition: displacement, incomplete markets, public AI stocks as the only tradeable claim on AI upside. Forward link: the reader wants to see this formalized.

3. **"We formalize this argument in an infinite-horizon, discrete-time asset pricing model."** Describes the model setup and its connection to GKP. Forward link: what does the model deliver?

4. **"We derive the price-dividend ratio of AI stocks in closed form."** States the main results: closed-form solution, comparative statics, complete-markets benchmark. Forward link: are there extensions?

5. **"In an extension, we connect to Jones (2024) on the trade-off between AI-driven growth and existential risk."** Previews the extension: extreme singularity, extinction risk, Coase theorem logic. Forward link: the self-demonstration.

6. **"This paper itself illustrates the displacement risk it models."** Self-demonstration paragraph. Forward link: related literature.

7. **"Related literature."** Lit review, positioned at the end of the introduction per the spec.

Each paragraph advances the argument. No dead ends, no redundancy, no laundry lists. The lit review is compact (under half a page) and placed correctly.

---

## Requirement 3: Plain English and conciseness
**Sub-verdict: PASS**

The writing is generally direct and concise. Five passages worth noting (none rise to the level of failure):

1. *"GKP discuss how mechanisms such as bequests, government debt, and intergenerational transfers would affect the magnitude of the displacement factor---noting, for instance, that in a representative dynasty with perfect altruism the displacement factor equals one---but do not conduct a formal analysis of how these mechanisms scale with output."* (Section 4.2) — A 45-word sentence with an embedded parenthetical clause. This could be two sentences without loss of precision.

2. *"This is consistent with the elevated valuations of AI-related firms observed in recent years, though we emphasize that the model is deliberately stylized and not designed to match specific valuation levels."* (Conclusion, para 2) — The "though we emphasize" hedge is defensive rather than scientifically cautious. The word "deliberately" is redundant with "stylized."

3. *"The model allows for any magnitude of productivity increase; the extension explores the limit $\tilde{g} \to \infty$, corresponding to a singularity that vastly increases output."* (Section 2.1) — The semicolon-joined clauses would be clearer as two sentences. "Corresponding to a singularity that vastly increases output" restates what $\tilde{g} \to \infty$ means, which the reader already knows.

4. *"These ensure that price-dividend ratios are finite."* (Section 2.4, after Assumption 3) — Minor: "These" is a vague pronoun referring to the parameter restrictions. Fine in context but the next sentence ("They are automatically satisfied...") chains another pronoun, making the passage slightly harder to parse than necessary.

5. *"The household is displaced---its consumption share falls."* (Intro, para 3) — This is actually a good example of the paper's style at its best: the dash explains the jargon immediately. Included here to note that the paper generally does this well.

No passage uses genuinely unnecessary jargon or complex syntax. Technical terms (SDF, CRRA, Arrow-Debreu) are standard in asset pricing. The writing clears this bar.

---

## Requirement 4: Self-demonstration
**Sub-verdict: PASS**

The self-demonstration appears in the sixth paragraph of the introduction — prominently placed, not buried in a footnote:

> "This paper itself illustrates the displacement risk it models. All analysis and writing were performed by AI agents working from a human-written specification. The human author contributed only the paper specification---approximately 80 lines---and the test suite. The AI performed all economic modeling, derivations, writing, and typesetting."

This satisfies all three sub-criteria:
- It explicitly acknowledges AI production.
- It is in the introduction, used as a demonstration of the thesis (not an afterthought).
- It accurately describes the division of labor: human wrote the spec (~80 lines) and tests; AI did the rest.

The footnote adds operational detail (Claude, automated loop) without being the primary acknowledgment.

---

## Requirement 5: Compelling and conversational throughout
**Sub-verdict: FAIL**

The introduction, results section, and extension maintain a conversational yet rigorous tone. The results section is particularly effective — each proposition is followed by clear economic interpretation ("The key object... is $\Delta^{-\gamma}$"; "The economic interpretation is direct"; "Proposition 4 is the central result"). The extension's Coase theorem discussion is genuinely engaging.

However, two sections lapse into prose that a reader would skim:

**The conclusion (Section 5)** is the primary failure. Its first two paragraphs are mechanical recap:

> "We show that publicly traded AI stocks command a hedging premium under incomplete markets. The representative household, unable to invest in private AI capital, values public AI stocks for their insurance properties: they pay relatively more in singularity states when the household's marginal utility is high."

This restates the abstract almost verbatim. The second paragraph adds an empirical connection but immediately retreats into hedging ("though we emphasize that the model is deliberately stylized"). The third paragraph summarizes the extension. Only the final paragraph ("Financial market solutions to AI disaster risk are under-discussed") adds genuine forward-looking content. Three out of four conclusion paragraphs are recap — a reader scanning a JF issue would stop reading here.

**The model section (Section 2)** opens with textbook-style exposition: "Time is discrete: $t = 0, 1, 2, \ldots$ The economy produces aggregate output $Y_t$, which grows over time." The subsections proceed mechanically through environment, assets, household problem, equilibrium, with minimal narrative connecting the formalism to the economic story that made the introduction compelling. This is somewhat standard for theory papers, and the section's brevity (~1.5 pages) mitigates the issue, but it contrasts sharply with the paper's own stated tone target ("between an academic paper and a blog post").

The conclusion is the more serious problem. A paper that aspires to be compelling throughout should not end with three paragraphs of summary the reader already knows. The final policy sentence is strong but arrives too late to salvage the section.
