# tests/spec-compliance.py
Started: 2026-03-21 22:34:54 EDT
Runtime: 1m 20s
[ralph-garage/agent-logs/20260322T023454.042030Z_spec-compliance_claude_opus.log](../ralph-garage/agent-logs/20260322T023454.042030Z_spec-compliance_claude_opus.log)

# spec-compliance

VERDICT: FAIL
REASON: The introduction figure compares AI stocks to non-AI stocks, not to the market portfolio as required by spec I.6.

## I. Economic Requirements

### I.1 Academic asset pricing theory paper
PASS. The paper is a formal asset pricing theory paper with propositions, proofs, and calibration.

### I.2 Economic ideas
PASS.
- **AI singularity**: Defined in Section 2.2 (lines 113–115): "with probability λ, an AI singularity occurs."
- **Negative AI singularity**: Defined at line 139: "We say the singularity is *negative* if J(s) < 1, which holds when s < φ/(θ+φ)."
- **Incomplete markets as asset inaccessibility**: Section 2.3 (line 145): "the household cannot buy equity in privately held AI firms, data assets, or proprietary algorithms." Explicitly distinguished from Arrow-Debreu framing.

### I.3 Arguments
PASS.
- **Main argument (hedging demand)**: Line 38–39: "We argue that hedging demand is part of the explanation."
- **Incomplete markets are key**: Line 72: "Incomplete markets are the key friction. If the household could invest in private AI capital, it could perfectly hedge the singularity risk, and the valuation premium would vanish."
- **Financial market solutions under-discussed**: Line 39: "Financial market solutions to AI disaster risk have received surprisingly little attention."
- **Singularity overcomes frictions via abundance**: Section 4.2, line 305: "Any finite barrier to trade... can be overcome when the resources to overcome it are unlimited."

### I.4 Model features
PASS.
- **Infinite horizon**: Line 90: "Time is discrete and infinite: t = 0, 1, 2, …"
- **Two agents**: Line 90: "representative household" and "AI owners." Household is marginal investor (line 91). AI owners hold private capital and are not marginal (line 91).
- **Two publicly traded assets**: Line 99: "AI stock" and "non-AI stock."
- **Focus on P/D ratio of public AI stocks**: Proposition 1 (line 188) derives closed-form P/D ratios; Proposition 2 gives comparative statics on the premium w.r.t. singularity probability.

### I.5 Extension incorporating Jones (2024)
PASS.
- **Extinction**: Section 4.1, Proposition 3 (line 282).
- **Infinite consumption for AI owners**: Section 4.2 (line 303): "the owners of that technology could, in principle, produce unlimited goods and services."
- **VSL calibration**: Line 298: "calibrates the value of a statistical life (VSL) to assess the trade-off between AI-driven growth and existential risk."
- **Infinite output overcoming incomplete markets (connecting to GKP)**: Section 4.2, line 309: explicitly connects to Garleanu et al. and discusses how infinite output resolves the friction.
- **Kept in extension**: Yes, all of this is in Section 4 ("Extension: Existential Risk and Infinite Output"), separate from the main model.

### I.6 Introduction includes a single figure illustrating AI stock valuation vs. market portfolio
**FAIL.** Figure 1 (line 45–70) compares AI stocks to *non-AI stocks* (labeled "Non-AI stocks (v^N)"). The spec requires comparison to the *market portfolio*, which is the value-weighted combination of AI and non-AI stocks, not non-AI stocks alone. Non-AI stocks and the market portfolio are distinct objects.

## II. Quality Requirements

### II.1 Narrative consistent with results
PASS. The narrative (hedging demand drives AI premium) matches the formal results (Propositions 1–3) and calibration (Table 1).

### II.2 Figures and tables nicely formatted
PASS. Uses booktabs for tables, pgfplots for figures, with gridlines, legends, and clear labels.

### II.3 Clear, unified, concise story
PASS. The paper follows a tight arc: motivation → model → results → extension → conclusion.

### II.4 Remove text and math that do not add value
PASS. No extraneous sections or unused equations detected.

## III. Style Requirements

### III.1 Writing style (between academic and blog, catchy, not cringey)
PASS. The writing is direct and conversational while maintaining rigor. Examples: "Why are AI stocks so expensive?" (line 37), "their elevated valuations are not a bubble—they are the price of insurance" (line 321).

### III.2 Author is anonymous
PASS. `\author{}` on line 21.

### III.3 Abstract is 100 words or less
PASS. Abstract is 89 words.

### III.4 Title is short, evocative, eye-catching, not cringey
PASS. "Hedging the Singularity" — three words, evocative, not cringey.

### III.5 Paper length < 20 pages excluding references
PASS. The paper is approximately 330 lines of LaTeX with standard 12pt/1.5-spacing formatting, well under 20 pages.

### III.6 Every page has a visible page number
PASS. `\pagestyle{plain}` (line 15) and `\thispagestyle{plain}` (line 26) ensure page numbers on all pages including the title page.

### III.7 At most 6 exhibits
PASS. 2 exhibits total: 1 figure (Figure 1) and 1 table (Table 1).

### III.8 Lit review focuses on most relevant papers, concise
PASS. The lit review covers three targeted strands: Garleanu et al. (2012) on displacement risk (most closely related), Jones (2024) on existential risk, and the rare disaster literature (Rietz, Barro, Wachter). All directly relevant, no padding.
