# tests/factcheck-lit.py
Started: 2026-04-09 18:20:05 EDT
Runtime: 4m 48s
[ralph-garage/agent-logs/20260409T182005.673677-0400_factcheck-lit_claude_opus.log](../ralph-garage/agent-logs/20260409T182005.673677-0400_factcheck-lit_claude_opus.log)

# factcheck-lit
VERDICT: PASS
REASON: All 11 cited works are externally verified with accurate metadata and materially supported in-text claims; only minor issues found.

## 1. Citation inventory audited

The following 11 citation keys are actually cited in the paper text (including footnotes):

1. GKP2012
2. Jones2024
3. KoganPapanikolaou2014
4. KoganPapanikolaouStoffman2020
5. Barro2006
6. Wachter2013
7. PastorVeronesi2009
8. GarleanuPanageas2015
9. KorinekSuh2024
10. Acemoglu2024
11. Nordhaus2021

The following 4 bibliography entries are never cited in the paper and were not audited:
- MehraPrescott1985
- CampbellCochrane1999
- BabinaMotta2024
- FamaFrench1993
- AghionJonesJones2019

## 2. External verification coverage

| Key | Status | External sources |
|-----|--------|-----------------|
| GKP2012 | VERIFIED | EconPapers/RePEc, ScienceDirect, SSRN, Semantic Scholar |
| Jones2024 | VERIFIED | AEA (doi:10.1257/aeri.20230570), RePEc, Stanford GSB |
| KoganPapanikolaou2014 | VERIFIED | Wiley/JoF, RePEc, NBER WP 17795 |
| KoganPapanikolaouStoffman2020 | VERIFIED | U Chicago Press/JPE (doi:10.1086/704619), MIT DSpace, RePEc, Kellogg |
| Barro2006 | VERIFIED | Oxford Academic/QJE, Harvard DASH, EconPapers |
| Wachter2013 | VERIFIED | Wiley/JoF, Wharton author page, EconPapers, NBER WP 14386 |
| PastorVeronesi2009 | VERIFIED | AEA (doi:10.1257/aer.99.4.1451), EconPapers, NBER WP 11876, SSRN |
| GarleanuPanageas2015 | VERIFIED | U Chicago Press/JPE (doi:10.1086/680996), EconPapers, SSRN, ResearchGate |
| KorinekSuh2024 | VERIFIED | NBER WP 32255, SSRN, arXiv:2403.12107 |
| Acemoglu2024 | VERIFIED | NBER WP 32487, Oxford Academic/Economic Policy (published version), MIT author page |
| Nordhaus2021 | VERIFIED | AEA (doi:10.1257/mac.20170105), NBER WP 21547, Nordhaus author page |

**Coverage: 11/11 cited works verified (100%).**

## 3. Metadata accuracy findings

All 11 cited works have materially accurate bibliographic metadata (authors, year, title, journal/outlet, volume, number, pages). No CRITICAL or IMPORTANT metadata errors.

One minor currency note: Acemoglu2024 is cited as NBER Working Paper No. 32487, but has since been published in *Economic Policy* (vol. 40, issue 121, pp. 13--58, 2025). The working paper citation is not wrong but could be updated.

## 4. In-text description accuracy findings

All 11 in-text characterizations are materially accurate and supported by the cited works. Two minor imprecisions were identified:

- **Jones2024**: The claim that Jones "emphasizes that the states in which AI is powerful enough to produce enormous growth are precisely those in which existential risk is highest" (line 95--96) is a plausible but imprecise paraphrase; Jones frames the AI dilemma as a trade-off between growth and existential risk, not necessarily that the same states produce both. The normalization of extinction utility to zero is the paper's own convention, attributed loosely to Jones.

- **KoganPapanikolaou2014**: Characterizing KP2014's investment-specific technology shock factor as a "displacement risk factor" slightly conflates their growth-opportunities mechanism with GKP2012's displacement risk concept. KP2014 studies differential firm exposure to embodied technology shocks via growth opportunities, which is related to but distinct from the labor/agent displacement in GKP2012.

## 5. Flagged issues by citation key and severity

| Key | Severity | Issue |
|-----|----------|-------|
| Jones2024 | MINOR | Imprecise paraphrase of the growth-extinction linkage; extinction utility normalization attributed loosely to Jones |
| KoganPapanikolaou2014 | MINOR | IST shock mechanism labeled as "displacement risk factor," conflating with GKP2012's concept |
| Acemoglu2024 | MINOR | Bib entry cites working paper; published version now available in *Economic Policy* (2025) |
| GKP2012 | NONE | -- |
| KoganPapanikolaouStoffman2020 | NONE | -- |
| Barro2006 | NONE | -- |
| Wachter2013 | NONE | -- |
| PastorVeronesi2009 | NONE | -- |
| GarleanuPanageas2015 | NONE | -- |
| KorinekSuh2024 | NONE | -- |
| Nordhaus2021 | NONE | -- |

**No CRITICAL or IMPORTANT issues found.**

## 6. Overall reliability of the paper's citations

The paper's citations are reliable. All 11 cited works were externally verified with multiple independent sources. Bibliographic metadata is accurate across all entries. In-text characterizations are materially supported, with only minor imprecisions in the literature review descriptions of Jones (2024) and Kogan and Papanikolaou (2014). The one actionable improvement is updating the Acemoglu (2024) entry to its published version.
