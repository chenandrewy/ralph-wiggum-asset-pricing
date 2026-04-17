# Ralph Run Archive

This folder preserves reader-facing artifacts from the Ralph loop that produced the paper.
It is meant to make the run legible without requiring readers to reconstruct the process from
Git history.

## What to Read First

- `history/improvement-plan-history.md` records the plans Ralph wrote across iterations.
- `history/test-result-history.md` records the test outcomes across iterations.
- `history/001-paper.pdf`, `history/002-paper.pdf`, and so on are paper snapshots from the run.
- `loop.log` records the loop chronology: planning, improvement, build, test, and commit phases.
- `check-direction/` records the candidate starting drafts considered before the run began.

## Folder Contents

`history/` is the main progress archive. The numbered PDFs show the paper changing over time.
The compiled plan and test histories summarize what Ralph tried to do and how the test suite
responded.

`check-direction/` documents the startup direction. Each `run-*` folder contains a candidate
initial paper and supporting code. The top-level candidate PDFs provide quick visual access to
those starting drafts.

`loop.log` is the console log from the Ralph loop. It is useful for checking timing, iteration
boundaries, build failures, test phases, and where the loop stopped.

## Omitted Artifacts

Low-level agent logs, current page images, scratch files, and LaTeX build intermediates are not
part of this archive. They are noisy implementation details rather than a useful reader-facing
record of the run.
