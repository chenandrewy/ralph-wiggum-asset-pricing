# tests/factcheck-freely.py
Started: 2026-04-09 18:48:38 EDT
Runtime: 6m 40s
[ralph-garage/agent-logs/20260409T184838.245391-0400_factcheck-freely_claude_claude-opus-4-6.log](../ralph-garage/agent-logs/20260409T184838.245391-0400_factcheck-freely_claude_claude-opus-4-6.log)

# factcheck-freely
VERDICT: FAIL
REASON: The paper misattributes the authorship of Kogan, Papanikolaou, Schmidt, and Song (2020) and contains an internal terminological inconsistency in the transfer model.

## Factual Errors

### 1. Wrong authors for "Left Behind" (JPE 2020)
**Location:** `references.bib` lines 134–142; cited on line 67 of `paper.tex`.

The bibliography entry attributes "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE, Vol 128, No 3, 2020, pp. 855–906) to Kogan, Papanikolaou, and **Stoffman**. The actual paper is by Kogan, Papanikolaou, **Schmidt**, and **Song** (four authors, not three). Noah Stoffman is not an author of this paper. The citation key `KoganPapanikolaouStoffman2020`, the author list, and the in-text citation are all incorrect.

### 2. Mischaracterization of Kogan and Papanikolaou (2014)
**Location:** Line 67 of `paper.tex`.

The paper states KP2014 "show that technology shocks create a displacement risk factor that is priced in the cross-section." KP2014 is about investment-specific technology shocks and growth opportunities, not "displacement risk" per se. The term "displacement risk" as a named concept originates in GKP (2012). KP2014's mechanism involves differential exposure to IST shocks across firms with different growth-opportunity ratios. Calling their factor a "displacement risk factor" conflates two related but distinct concepts.

## Logical Inconsistencies

### 3. "Income" vs. "surplus" in the transfer model
**Location:** Lines 264 and 270 of `paper.tex`.

Line 264 defines the tax as levied on "AI owners' income." Line 270 then refers to the same tax base as "AI owners' surplus." These are different economic concepts: income is the total amount received; surplus is the gain relative to a baseline. The formula in equation (11) taxes the full post-displacement income share $(1 - \phi\alpha)$, not the surplus from the singularity. The text should use one term consistently.

## Additional Issues (Not Determinative)

### 4. Explosive P/D in extension figure (undiscussed)
For the "Large singularity" scenario ($\eta = 9$, $\phi = 0.05$), the P/D formula yields $K > 1$ at low tax rates, meaning valuations are infinite. The code silently drops these points. The paper text discusses the figure without noting that the large-singularity P/D curve starts at a positive $\tau$, which could mislead readers.

### 5. Post-singularity stationarity approximation
The proof of Proposition 1 assumes the post-singularity P/D ratio equals the pre-singularity one, but acknowledges this is approximate. Since $\theta$ increases and $\alpha$ decreases after each singularity, the actual post-singularity $\Gamma^{AI}$ would differ, potentially affecting the quantitative results.

### 6. Informal veto proof (Proposition 3)
The proof argues qualitatively that "for $\gamma$ sufficiently large" the household vetoes, but does not establish formal conditions on the parameters. Part (ii) asserts that complete markets let the household share the social surplus without demonstrating this within the model.

## Items Verified as Correct
- Euler equation derivation and P/D formulas (Proposition 1)
- Corollary 1 (valuation spread)
- Proposition 2 comparative statics
- GKP (2012) and Jones (2024) characterizations
- Transfer ratio formula (equation 12), correctly independent of $\eta$
- Code output matches formulas and table values
- Parameter constraints satisfied across singularity transitions
