# tests/factcheck-lit.py
Started: 2026-04-02 22:39:49 EDT
Runtime: 3m 33s
[ralph-garage/agent-logs/20260402T223949.805760-0400_factcheck-lit_claude_opus.log](../ralph-garage/agent-logs/20260402T223949.805760-0400_factcheck-lit_claude_opus.log)

# factcheck-lit
VERDICT: FAIL
REASON: The Zhang2019 bibliography entry misattributes authorship to Lu Zhang instead of Miao Ben Zhang, a CRITICAL metadata error.

## 1. Citation inventory audited

All 13 citation keys used in the paper text were audited:

| # | Citation key | In-text location |
|---|---|---|
| 1 | GKP2012 | Introduction, Model, Extension (multiple) |
| 2 | Jones2024 | Introduction, Extension (multiple) |
| 3 | GarleanuPanageas2015 | Related literature |
| 4 | KoganPapanikolaouStoffman2020 | Related literature |
| 5 | KoganPapanikolaou2014 | Related literature |
| 6 | Knesl2023 | Related literature |
| 7 | Zhang2019 | Related literature |
| 8 | Rietz1988 | Related literature |
| 9 | Barro2006 | Related literature |
| 10 | Wachter2013 | Related literature |
| 11 | BabinaEtAl2024 | Related literature |
| 12 | PastorVeronesi2009 | Related literature |
| 13 | HobijnJovanovic2001 | Related literature |

Two bibliography entries are never cited and were excluded: KorinekSuh2024, AcemogluRestrepo2018.

## 2. External verification coverage

| Citation key | Status | External sources |
|---|---|---|
| GKP2012 | VERIFIED | EconPapers/RePEc, MIT DSpace, ScienceDirect |
| Jones2024 | VERIFIED | AEA website, RePEc/IDEAS, Stanford GSB |
| GarleanuPanageas2015 | VERIFIED | U Chicago Press / JPE, EconPapers, RePEc/IDEAS |
| KoganPapanikolaouStoffman2020 | VERIFIED | U Chicago Press / JPE, RePEc/IDEAS, MIT DSpace |
| KoganPapanikolaou2014 | VERIFIED | Wiley / Journal of Finance, NBER, EconPapers |
| Knesl2023 | VERIFIED | ScienceDirect, EconPapers, SSRN |
| Zhang2019 | VERIFIED | Wiley / Journal of Finance, SSRN, RePEc/IDEAS, author website (miaobenzhang.com) |
| Rietz1988 | VERIFIED | RePEc/IDEAS, ScienceDirect, Semantic Scholar |
| Barro2006 | VERIFIED | Oxford Academic / QJE, EconPapers/RePEc, Harvard author page |
| Wachter2013 | VERIFIED | EconPapers/RePEc, Wharton faculty page, UPenn repository |
| BabinaEtAl2024 | VERIFIED | IDEAS/RePEc, SSRN, Semantic Scholar |
| PastorVeronesi2009 | VERIFIED | AEA / AER, SSRN, EconPapers/RePEc |
| HobijnJovanovic2001 | VERIFIED | AEA / AER, IDEAS/RePEc, NYU Scholars |

**Coverage: 13/13 cited works externally verified (100%).**

## 3. Metadata accuracy findings

12 of 13 citations have materially accurate metadata (authors, year, title, journal, volume, number, pages).

**One CRITICAL metadata error:**

- **Zhang2019:** The bibliography entry lists `author = {Zhang, Lu}`. The actual author of "Labor-Technology Substitution: Implications for Asset Pricing" (Journal of Finance, 2019, 74(4), 1793--1839) is **Miao Ben Zhang** (USC Marshall School of Business). Lu Zhang is a different finance professor at Ohio State University, known for the investment CAPM / q-factor model. This is a misattribution to a different scholar. All other metadata fields (title, journal, volume, number, pages, year) are correct.

## 4. In-text description accuracy findings

All 13 in-text descriptions are materially accurate and supported by the cited works:

- **GKP2012:** Correctly described as introducing displacement risk in an OLG economy with innovation and incomplete intergenerational risk-sharing. The paper's use of GKP's framework is appropriately attributed and distinguished from its own extensions.
- **Jones2024:** Correctly described as analyzing the trade-off between AI-driven growth and existential risk, with the curvature of utility playing a critical role.
- **GarleanuPanageas2015:** Fairly characterized as developing OLG asset pricing with incomplete risk-sharing (the OLG/finite-lives framework inherently involves limited intergenerational risk-sharing).
- **KoganPapanikolaouStoffman2020:** Correctly characterized as OLG asset pricing with incomplete risk-sharing; the paper's abstract explicitly describes innovators who cannot sell claims on future ideas.
- **KoganPapanikolaou2014:** Correctly described as analyzing technology shocks and growth opportunities.
- **Knesl2023:** Correctly described as modeling automation-driven displacement risk premia in the cross section.
- **Zhang2019:** Setting aside the author error, the in-text description of modeling "automation-driven displacement risk premia in the cross section of stock returns" is a reasonable characterization of a paper about labor-technology substitution and cross-sectional return differences, though Zhang frames it as a "replacement option" mechanism rather than "displacement risk" per se.
- **Rietz1988:** Correctly cited as foundational rare disasters literature.
- **Barro2006:** Correctly cited as rare disasters literature.
- **Wachter2013:** Correctly cited as rare disasters literature (time-varying disaster probability).
- **BabinaEtAl2024:** Correctly described as providing evidence that AI adoption drives firm growth.
- **PastorVeronesi2009:** Correctly described as studying how technological revolutions affect stock prices.
- **HobijnJovanovic2001:** Correctly described as documenting the negative impact of IT innovation on incumbent firms.

## 5. Flagged issues by citation key and severity

### Zhang2019 — CRITICAL

**Author misattribution.** The `references.bib` entry (line 131) has `author = {Zhang, Lu}`. The actual author is Miao Ben Zhang (USC Marshall). Lu Zhang (Ohio State) is a different scholar. The rendered paper would cite "Lu Zhang (2019)", misattributing the work.

- **External evidence:** Wiley/Journal of Finance listing, SSRN page, RePEc/IDEAS, author website (miaobenzhang.com) all confirm the author is Miao Ben Zhang.
- **Recommended fix:** Change `author = {Zhang, Lu}` to `author = {Zhang, Miao Ben}` in `references.bib`.

### All other keys — NONE

No CRITICAL, IMPORTANT, or MINOR issues for the remaining 12 citation keys.

## 6. Overall reliability of the paper's citations

The paper's citation practices are strong overall. All 13 cited works were externally verified. In-text descriptions are materially accurate and fairly represent the cited works. The one CRITICAL error — misattributing Zhang (2019) to Lu Zhang instead of Miao Ben Zhang — is a consequential metadata mistake that attributes a published paper to the wrong scholar and must be corrected. With that fix, the citation inventory would be fully accurate.
