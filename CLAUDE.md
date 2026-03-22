# CLAUDE.md

The goal of the project is to write an academic asset pricing theory paper. You are either an author or a reviewer.

Always read `spec/paper-spec.md` before doing work.

See `README.md` for the full repo structure and how Ralph (a.k.a. RALF, ralph, the ralph loop) works.

## Asset Pricing Background
- Target audience is readers of top finance journals.
- See `spec/asset-pricing-background.md` for how to use asset pricing terms.

## Prompt Design Guidelines
- Keep prompts general. Do not use examples to patch current holes in the system.

## Key Files
- `spec/paper-spec.md`: paper specification
- `spec/CFR-R1-report.md`: referee report to address
- `spec/lit/`: literature for reference as needed

## Folder Structure (Quick Reference)

### Research Project
- `paper/` — LaTeX source
- `code/` — R scripts and analysis
- `data/` — datasets
- `spec/lit/` — literature for reference
- `dev/` — scratch work, journals

### Specification
- `spec/` — repo intent and source-of-truth specifications

### Tests
- `tests/` — test and referee definitions (referee scripts prefixed `referee-`)
- `test-results/` — test and referee outputs from the latest run

### Ralph (Permanent)
- `ralph/` — loop script, agent wrapper, prompts

### Ralph Garage (Transient)
- `ralph-garage/` — improvement plan, shared page images
- `ralph-garage/page-images/` — uncommitted page images of the paper
- `ralph-garage/history/` — track ralph loop progress here (iteration logs, run summaries)
- `ralph-garage/loop.log` — console output from the ralph loop

### Dev Logs
- `ralph-garage/agent-logs/` — non-canonical agent debug logs

### Disposable Code and Results
Wipe these folders before making disposable code
- `dev/tmp/` — disposable code
- `dev/tmp/results/` — disposable results

## Sync Issues
- The files are synced via Dropbox and may not be available immediately.
- If files are unreadable or corrupt, stop and ask the user rather than trying to work around the issue. The user can trigger a Dropbox sync to fix it.
- If git fails with "Resource deadlock avoided" on a reflog file (e.g. `.git/logs/refs/heads/...`), ask the user to delete that file from the Mac side. It's a stale Dropbox/FUSE lock.

## Worktrees
- Create git worktrees under `/workspace/worktrees/`.

## Coding Guidelines
- Use R for data analysis.
- For the ralph loop, use minimal bash, and lean on Python for most tasks.
- Use kebab-case for file and folder names.
- Top comment in every script: how to run, inputs, outputs.
- Do not create fallback or try-catch statements unless they are strictly necessary.
- if the user says "what do you think?" it means explain and do not modify any files.

## Git Usage
- For commits that update the ralph algorithm, start with "algo update:"
- For commits where the ralph loop updates the paper, start with "rloop" (e.g., `rloop [run-name]: ...`)
- "The beginning of the run" means the commit immediately before the first `rloop` commit on the current branch — not the merge base with main. Use `git log --oneline <branch> | tail` to find it.

## Journal
- When requested, take notes in `dev/journal/`
    - Filename: `YYMMDD[T]HH-[note name].md`
    - Include title, date, and time at the top.

## Time Zone
- Use New York time zone for all timestamps.

## Synonyms
- Other terms that mean "Claude":
    - Claw, clawed
- Other terms that mean "Ralph"
    - Ralf, ralf, ralph
