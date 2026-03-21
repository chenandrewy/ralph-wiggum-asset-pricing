# Bootstrap Implementation and Feedback
**Date:** 2026-03-20, 6:00 PM ET

## Context

This repo (`ralph-wiggum-asset-pricing`) writes an academic asset pricing theory paper using the Ralph loop — an automated plan/improve/test/review cycle driven by Claude agents.

The bootstrap brought over the Ralph architecture from two source repos kept under `dev/`:

- **`dev/HumanxAI-ChenAY/`** — the canonical Ralph implementation. An empirical finance paper with WRDS data, R code, and 19 tests. This is the structural template: its folder layout (`paper/`, `code/`, `data/`, `spec/`, `ralph/tests/`, `ralph/tools/`, `ralph-garage/`), loop script, agent wrapper, test framework, review framework, and config system were all copied from here.

- **`dev/backup-ralph-ap/`** — a prior attempt at this same asset pricing paper using an older, flat Ralph architecture (`ralph.sh` at repo root, `prompts/`, `output/`, `log/`, `tools/`). Its paper spec (`spec/paper_spec.md`), review prompts (`prompts/review_*.md`), literature files (`lit/`), and referee report (`spec/CFR-R1-report.md`) contain the domain-specific content for this project.

The design decision was to use HumanxAI's structure (Option B from the kickoff) and translate the backup's domain content into that structure. The backup's flat structure will be adopted later once stability is confirmed.

## What was done

Implemented steps 2–5 from the kickoff plan (`dev/journal/260320T17-project-kickoff.md`).

### Specifications created (`spec/`)

| File | Source | Notes |
|------|--------|-------|
| `spec/paper-spec.md` | Backup's `spec/paper_spec.md` | Reformatted into HumanxAI numbered-section style (sections I–IV). Content is identical in substance. Key requirements: infinite-horizon model, two agents (AI owners + household), disaster-based consumption growth, AI asset dividend structure, complete vs incomplete markets, extension addressing CFR R1 report. Style: <100 word abstract, <15 pages, <6 exhibits. |
| `spec/asset-pricing-background.md` | Backup's `spec/asset_pricing_background.md` | Copied verbatim. Defines conventions for budget constraints, complete/incomplete markets, hedging, GE vs PE. |
| `spec/CFR-R1-report.md` | Backup's `spec/CFR-R1-report.md` | Copied verbatim. The referee report the paper must address. Key concerns: (1) model subsumed by GKP (2012), (2) should dive deeper into AI singularity per Jones (2024). |
| `spec/ralph-spec.md` | HumanxAI's `spec/ralph-spec.md` | Adapted: removed WRDS credential requirements, removed `code/` and `data/` from commit model staging paths, removed code-spec references. Core loop lifecycle, branch model, commit model, exit conditions are structurally identical. |
| `spec/test-spec.md` | HumanxAI's `spec/test-spec.md` | Adapted: removed `code/` and `data/` from evaluation scope. Test result contract, agent wrapper contract, artifact preparation pipeline are identical. |

### Ralph tools created (`ralph/tools/`, 16 files)

Files copied **as-is** from HumanxAI (no changes needed):
- `agent_wrapper.py` (360 lines) — dispatches to claude/codex, manages logs
- `utils.py` (129 lines) — config parsing, transient dir clearing, staleness checks
- `read-config.py` — CLI config reader
- `run-tests.py` — parallel test orchestrator
- `run-reviews.py` — sequential review orchestrator
- `build-paper.sh` — pdflatex/biber compilation (3-pass)
- `generate-page-images.py` — PDF→PNG + exhibit manifest
- `prune-agent-logs.py` — retention-based log cleanup
- `compile-improvement-plan-history.py` — git-based plan history
- `compile-test-result-history.py` — git-based test history
- `wipe.sh` — removes `ralph-garage/`
- `prompts/commit-message.md` — commit message template

Files **adapted** for this project:
- `ralph-loop.sh` — removed `load_wrds_env_file()` and the WRDS `.env` requirement. Otherwise identical to HumanxAI.
- `author-plan.py` — prompt template reads `spec/paper-spec.md` and `spec/asset-pricing-background.md` instead of `code/` and `data/`.
- `author-improve.py` — same adaptation (no code/data references in prompt).
- `commit-iteration.py` — `DEFAULT_ADD_PATHS` is `["paper", "ralph-garage/improvement-plan.md", "ralph-garage/test-results", "ralph-garage/review-results"]` (removed `"code"`). Everything else identical.
- `check-setup.py` — simplified: removed WRDS credential validation, kept config constraint checks only.
- `init.sh` — copies only from `docs/code-templates/latex/` (no R templates).

### Tests created (`ralph/tests/`, 8 scripts + 1 helper)

The backup repo used **review prompts** (`prompts/review_*.md`) that wrote ACCEPT/REJECT to output files. These were translated into HumanxAI-style **test scripts** that produce VERDICT: PASS/FAIL reports.

| Test file | Source | What it checks |
|-----------|--------|---------------|
| `_runner_helpers.py` | HumanxAI (as-is) | Shared test framework: context builder, agent runner, verdict parser, report writer |
| `build-latex.py` | HumanxAI (as-is) | Pure-Python LaTeX build gate. Checks `paper/paper.pdf` freshness vs `paper/paper.tex`. Used as pre-test gate in the loop. |
| `spec-compliance.py` | HumanxAI (adapted prompt) | Agent reads `spec/paper-spec.md` and `paper/paper.tex`, checks every requirement in sections I and II. |
| `theory-correctness.py` | Backup's `review_theory_correctness.md` | 4-step procedure: (1) notational consistency, (2) consistent assumptions, (3) logical results derivable from assumptions, (4) verbal claims supported by formal theory. |
| `theory-elegance.py` | Backup's `review_theory_elegance.md` | Checks conciseness: every equation must be used downstream, every parameter must matter for conclusions, no redundant notation. |
| `ai-economics.py` | Backup's `review_AI_economics.md` | Checks 4 conditions: (1) singularity grows aggregate output, (2) household displaced, (3) AI owners benefit, (4) complete vs incomplete markets distinguished. |
| `writing-natural.py` | HumanxAI (adapted) | Multi-agent: sub-agents review individual sections for jargon/compression/cringeyness, synthesizer produces verdict. Adapted style description for this paper's spec. |
| `cfr-r1.py` | Backup's `review_CFR_R1.md` | Plays CFR R1 referee. Reads GKP and Jones papers from `docs/lit/`. Checks: (1) meaningful contribution vs GKP, (2) modestly characterized, (3) captures Jones (2024) features. |
| `visual-pages.py` | New | Reads page images, checks page numbers, formatting, length compliance. |

All agent-backed tests use `AGENT = "claude"` and `MODEL = "claude-opus-4-6"`.

### Reviews created (`ralph/reviews/`, 1 script + 1 helper)

| File | Source | Notes |
|------|--------|-------|
| `_review_helpers.py` | HumanxAI (as-is) | Shared review framework. Reviews always exit 0. |
| `top3-referee.py` | HumanxAI (adapted) | Simulates top-journal referee. Reads paper, spec, page images, test results. Produces open-ended feedback (no VERDICT). |

### Config (`config-ralph.yaml`)

```yaml
max-iter: 20
agent: claude
model: opus
test-mode: selected
selected-tests:
  - spec-compliance
  - theory-correctness
  - theory-elegance
  - ai-economics
  - writing-natural
agent-log-mode: verbose
agent-log-retention-days: 1
reviews: false
selected-reviews:
  - top3-referee
```

Note: `cfr-r1` and `visual-pages` exist as test scripts but are NOT in `selected-tests`. They can be enabled later. `cfr-r1` requires the GKP and Jones literature files which are present in `docs/lit/`.

### Other files

- `README.md` — full repo structure documentation, adapted from HumanxAI
- `CLAUDE.md` — updated with asset pricing background references, key files, review folder
- `AGENTS.md` — symlink → `CLAUDE.md`
- `.gitignore` — added Ralph transient artifacts, LaTeX build artifacts, generated PDFs
- `docs/code-templates/latex/paper.tex` — starter template with biblatex/biber/hyperref
- `docs/code-templates/latex/references.bib` — starter bib with Lucas (1978) and Cochrane (2005)
- `docs/lit/` — 7 files copied from backup: GKP-2012-WP.md, GKP-2012-WP-appendix.md, GKP-2012-notes.md, Jones-2024-AERI.md, Jones-2024-AERI-notes.md, Korinek-Suh-2024.md, Koriken-Suh-2024.md
- `ralph-garage/` — directory structure with `.gitkeep` files in test-results, review-results, agent-logs, page-images, history

## Open issues — feedback received

### Issue 1: Bootstrap is incomplete — `paper/` is empty

**Problem:** The canonical paper required by the repo contract is missing. `spec/paper-spec.md`, `README.md`, and the kickoff note all assume `paper/paper.tex` exists, but `paper/` is currently empty. The build gate (`ralph/tests/build-latex.py`), all agent-backed tests, and reviews cannot run.

**Why it matters:** The loop will fail at its very first step. `ralph-loop.sh` line 275 calls `run_latex_build_gate()` which runs `build-paper.sh` and then `build-latex.py`. Both require `paper/paper.tex` to exist.

**Fix:** Run `bash ralph/tools/init.sh` to copy `docs/code-templates/latex/paper.tex` and `docs/code-templates/latex/references.bib` into `paper/`. The starter template has placeholder content — the first Ralph iteration will replace it with the actual paper.

### Issue 2: codex support is advertised but not implemented across the loop

**Problem:** The loop validates `agent: codex` as a valid config value (`ralph/tools/ralph-loop.sh:116`), but downstream components hard-code Claude:
- Every test script: `AGENT = "claude"` (e.g., `ralph/tests/spec-compliance.py:12`)
- Every review script: `AGENT = "claude"` (e.g., `ralph/reviews/top3-referee.py:14`)
- Commit step: `ralph/tools/commit-iteration.py:166` shells out to `claude` CLI directly

If someone sets `agent: codex` in `config-ralph.yaml`, only `author-plan.py` and `author-improve.py` would dispatch through the agent wrapper with codex. Tests, reviews, and commits would still use Claude.

**This is inherited from HumanxAI** — the same inconsistency exists in the source repo. It was copied faithfully.

**Fix options:**
1. **Minimal:** Remove `codex` from the allowed agents in `ralph-loop.sh:116` (change the check to only allow `claude`). Document that codex is not supported.
2. **Full:** Plumb agent choice through an env var or config read in every test/review script and in `commit-iteration.py`. This is more work and may not be needed since we only use Claude.

### Issue 3: Setup check is too weak to catch the broken bootstrap

**Problem:** `ralph/tools/check-setup.py` validates only:
- `config-ralph.yaml` exists
- `continual-improvement: true` requires `reviews: true`
- `selected-reviews` IDs exist in `ralph/reviews/`

It does NOT check for:
- `paper/paper.tex` exists
- `paper/references.bib` exists
- `spec/paper-spec.md` exists
- Any other required artifact

Running `python3 ralph/tools/check-setup.py` currently prints "Setup check passed" despite `paper/` being empty.

**Fix:** Add artifact presence checks to `check-setup.py`. At minimum:
```python
required_files = [
    pathlib.Path("paper/paper.tex"),
    pathlib.Path("spec/paper-spec.md"),
]
for path in required_files:
    if not path.is_file():
        print(f"FAIL: missing required file: {path}", file=sys.stderr)
        return 2
```

## What was NOT done

- Step 1 from kickoff (copy CLAUDE.md from HumanxAI) was already marked done.
- The starter template in `paper/` was NOT populated — `init.sh` was created but not run. This is Issue 1 above.
- No git commit was made for the bootstrap work.
- The `.claude/skills/` directory was not set up (per user instruction: "ignore the backup skills").
