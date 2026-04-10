# tests/factcheck-lit.py
Started: 2026-04-09 21:20:47 EDT
Runtime: 3m 46s
[ralph-garage/agent-logs/20260409T212047.325427-0400_factcheck-lit_claude_opus.log](../ralph-garage/agent-logs/20260409T212047.325427-0400_factcheck-lit_claude_opus.log)

# factcheck-lit
VERDICT: FAIL
REASON: The bibliography entry for KoganPapanikolaouSeruStoffman2020 includes a ghost author (Amit Seru) who is not an author of the cited paper.

## 1. Citation inventory audited

All 9 citation keys appearing in the paper text were audited:

1. GKP2012
2. Jones2024
3. KoganPapanikolaou2014
4. KoganPapanikolaouSeruStoffman2020
5. Knesl2023
6. Barro2006
7. Wachter2013
8. PastorVeronesi2009
9. Nordhaus2021

## 2. External verification coverage

| Key | Status | External sources |
|-----|--------|-----------------|
| GKP2012 | VERIFIED | EconPapers/RePEc, ScienceDirect, SSRN |
| Jones2024 | VERIFIED | AEA publisher page, IDEAS/RePEc, Stanford GSB |
| KoganPapanikolaou2014 | VERIFIED | Wiley/Journal of Finance, EconPapers/RePEc, NBER |
| KoganPapanikolaouSeruStoffman2020 | VERIFIED | Journal of Political Economy, EconPapers/RePEc, MIT DSpace, Kellogg/Northwestern |
| Knesl2023 | VERIFIED | ScienceDirect, EconPapers/RePEc, Oxford ORA |
| Barro2006 | VERIFIED | Oxford Academic/QJE, EconPapers/RePEc, Harvard DASH |
| Wachter2013 | VERIFIED | Wiley/Journal of Finance, EconPapers/RePEc, Wharton/UPenn |
| PastorVeronesi2009 | VERIFIED | AEA publisher page, EconPapers/RePEc, NBER |
| Nordhaus2021 | VERIFIED | AEA publisher page, IDEAS/RePEc, NBER |

**Coverage: 9/9 cited works externally verified (100%).**

## 3. Metadata accuracy findings

| Key | Metadata verdict |
|-----|-----------------|
| GKP2012 | Accurate |
| Jones2024 | Accurate |
| KoganPapanikolaou2014 | Accurate |
| KoganPapanikolaouSeruStoffman2020 | **ERROR — ghost author** |
| Knesl2023 | Accurate |
| Barro2006 | Accurate |
| Wachter2013 | Accurate |
| PastorVeronesi2009 | Accurate |
| Nordhaus2021 | Accurate |

**Detail on the error:** The bibliography lists four authors for "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE, 2020): Kogan, Papanikolaou, Seru, and Stoffman. Multiple authoritative sources (the JPE publisher page, EconPapers, MIT DSpace, Kellogg/Northwestern) consistently list only three authors: **Kogan, Papanikolaou, and Stoffman**. Amit Seru is not an author of this paper. Seru is a coauthor on a different paper by a similar author group: "Technological Innovation, Resource Allocation, and Growth" (QJE, 2017). The bib key, the author field, and any rendered citation are all incorrect.

## 4. In-text description accuracy findings

| Key | In-text claim-support verdict |
|-----|-------------------------------|
| GKP2012 | Supported. The paper accurately describes GKP's general-equilibrium model of displacement risk from innovation under incomplete markets, the overlapping-generations structure, and the hedging role of growth stocks. |
| Jones2024 | Supported. The paper accurately describes the growth-vs-extinction trade-off, bounded utility making agents conservative, and the normalization of extinction utility to zero. |
| KoganPapanikolaou2014 | Supported. The characterization that technology shocks generate cross-sectional return differences through firms' heterogeneous exposures is materially accurate. |
| KoganPapanikolaouSeruStoffman2020 | Supported. Despite the author-list error, the characterization of the paper's content (creative destruction, inequality, cross-sectional return differences) is materially accurate. |
| Knesl2023 | Supported. The claim that Knesl provides direct empirical evidence that automation-driven displacement commands a risk premium is confirmed. |
| Barro2006 | Supported. The characterization as providing a methodological foundation for pricing discrete catastrophic events is accurate. |
| Wachter2013 | Supported. Cited alongside Barro2006 as rare disasters literature; Wachter's time-varying disaster probability model fits this characterization. |
| PastorVeronesi2009 | Supported. The claim that Pastor and Veronesi study how technological revolutions affect stock prices through productivity uncertainty is accurate. |
| Nordhaus2021 | Supported. The phrase "examined critically" accurately characterizes Nordhaus's skeptical, empirical evaluation of the singularity hypothesis. |

## 5. Flagged issues by citation key and severity

### KoganPapanikolaouSeruStoffman2020

- **CRITICAL: Incorrect author list.** The bibliography lists Amit Seru as a fourth author, but the published paper "Left Behind: Creative Destruction, Inequality, and the Stock Market" (JPE, 2020, vol. 128, no. 3, pp. 855–906) has only three authors: Kogan, Papanikolaou, and Stoffman. The bib key itself embeds the error. The correct entry should list only three authors and use a corrected bib key (e.g., `KoganPapanikolaouStoffman2020`). External sources: JPE publisher page, EconPapers/RePEc, MIT DSpace, Kellogg/Northwestern.

### All other keys

- No CRITICAL, IMPORTANT, or MINOR issues found.

## 6. Overall reliability of the paper's citations

The paper cites 9 works. All 9 were externally verified. In-text characterizations of all 9 cited works are materially accurate and supported by the cited sources.

One CRITICAL metadata error was found: the bibliography entry for "Left Behind" (JPE, 2020) incorrectly includes Amit Seru as a coauthor. This is a clear factual error that would produce an incorrect rendered citation and bibliography entry.

All other metadata (authors, titles, journals, volumes, pages, years) is accurate across all 9 citations. The paper's use of citations to support its arguments is careful and well-supported.
