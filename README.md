# ralph-wiggum-asset-pricing

This repo uses [Geoff Huntley's Ralph Wiggum loop](https://ghuntley.com/ralph/) to generate an academic asset pricing theory paper. 

The default setup generates something like ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf).

If you want Ralph to write a different paper, update:
- `spec/paper-spec.md`
- `config-ralph.yaml`

and perhaps
- `tests/*.py`

Then as long as you feel comfortable with agents in Yolo mode and have some Claude or Codex credits,
- `go-ralph-go.sh` 

will have the AIs start working on your paper.


**How "Hedging the Singularity" was actually generated:** the `config-ralph.yaml` and `spec/paper-spec.md` on `main` are a minimal quick-start setup, not what produced the paper. The automated Ralph loop that wrote the paper ran on the [`ralph/run-final`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/ralph/run-final) branch — that's where you'll find the real config, paper-spec, and full `rloop-NN:` commit history. A human-written preface and edits of two sentences were then added on the [`human-preface`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/human-preface) branch, which is where [the final PDF](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf) lives.

## How Ralph Works

Each iteration of the loop:

1. `ralph/author-plan.py` reads the latest test results and `spec/paper-spec.md`, and writes `ralph-garage/improvement-plan.md`.
2. `ralph/author-improve.py` executes that plan against the paper and code.
3. Scripts in `tests/` evaluate the result.
4. If any test fails, go back to step 1.

Ralph is *human on the loop*, not *human out of the loop*. While it runs, watch `ralph-garage/loop.log` and inspect the iteration history (see [Watching a Run](#watching-a-run)), then adjust `config-ralph.yaml` between stretches — turning tests on or off, raising or lowering the iteration budget — based on what you see. The branch model (see [Git Branching](#git-branching)) makes stopping, resuming, and discarding stretches cheap.

For another paper built with this same method, and a different set of tests to crib from, see [HumanxAI-ChenAY](https://github.com/chenandrewy/HumanxAI-ChenAY) (an empirical paper).

## Environment Setup and Safety Model

Ralph runs coding agents in YOLO mode. The agent wrapper invokes Claude with `--dangerously-skip-permissions` and Codex with `--sandbox danger-full-access`. I recommend running Ralph inside the dev container for safety.

The simplest way is to open this repo in VS Code and use "Reopen in Container" (requires [Docker Desktop](https://docs.docker.com/desktop/) and the [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/create-dev-container)). See `.devcontainer/README.md` for container and credential details. I develop on macOS; Windows users (untested) should clone into WSL2 rather than the Windows filesystem (for file I/O, line endings, and symlinks like `AGENTS.md`) and run `Install-Module CredentialManager` in PowerShell so `.credentials/get-credentials.py` can read Windows Credential Manager.

To use WRDS, I recommend saving your WRDS credentials once per machine on the host (not inside the container):

```bash
python .credentials/setup.py
```

Rebuild the container afterward so it picks up the credentials. Verify with:

```bash
python .credentials/check-wrds.py
```

Inside the container, credentials are exposed as environment variables — `WRDS_USERNAME` and `WRDS_PASSWORD`. Read them from your code with `Sys.getenv("WRDS_USERNAME")` in R or `os.environ["WRDS_USERNAME"]` in Python. If you use `ralph/research-template` as your `startup-source`, Ralph inherits `code/query-wrds-example.R` as a working example to adapt.

To add other credentials (e.g. API keys), edit `.credentials/credentials-map.json` — see `.devcontainer/README.md`.

## Selecting Claude vs Codex

Each agent invocation is configured by three module-level constants near the top of a Python script: `AGENT` (`"claude"` or `"codex"`), `MODEL`, and `EFFORT`. Edit them to switch providers or change model tiers.

The scripts fall into two groups:

- `ralph/author-plan.py`, `ralph/author-improve.py`, `ralph/author-fix-build.py` — the three phases of the loop (plan, apply, repair LaTeX build errors)
- `tests/*.py` — each test and referee script runs its own agent invocation, with its own `AGENT` / `MODEL` / `EFFORT`

You'll need credits with whichever provider you choose. See `ralph/agent_wrapper.py` for the full list of supported agents, models, and effort values.


## Key Files

### `spec/paper-spec.md` — Paper Specification

Basically the paper in bullet point form. You can leave it to be open ended, if you have confidence in your tests. As explained in the preface of ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf), I found that I needed to make `paper-spec.md` rather tight. 

But hopefully your agents are more up for your task.

### `config-ralph.yaml` — Ralph Config

The knobs for a particular run. 

The most important knobs are the selected PASS/FAIL tests
```yaml
selected-tests:
  - factcheck-code
  - factcheck-freely
  - factcheck-lit
  - spec-paper
  - visual-figures
  - visual-figures-image-only
```
These defaults are a minimal set so you can hopefully just run with it. ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf) used all 25 tests in `tests/`.

One can also turn on continual improvement and open ended referees
```yaml
continual-improvement: true

referees: true

selected-referees:
  - referee-top3
```
continual improvement means Ralph will keep going even if all tests pass. The referees are not pass/fail: they generate open-ended feedback. I couldn't get this to work well for ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf). But once again, I hope your agents do better.

The last key config is `startup-source`, which tells Ralph where to begin. It takes one of two values:

- `ralph/research-template` — a folder with minimal `code/` and `paper/` templates.
- `ralph-garage/check-direction/run-NN` — a folder with `code/` and `paper/` filled out by `check-ralph-direction.sh` (see below)

### `tests/*.py` — Tests and Referees

Scripts in `tests/` with no prefix are tests; scripts prefixed `referee-` are referees. Test IDs are filenames without `.py` (e.g. `tests/spec-paper.py` → `spec-paper`, `tests/referee-top3.py` → `referee-top3`). Edit these when your paper needs different checks than the template.

### `go-ralph-go.sh` — Running Ralph

The main entry point. Behavior depends on the current branch: `main` starts a fresh stretch using `startup-source`; `ralph/run` resumes the existing stretch.

The full workflow is specified in `spec/ralph-spec.md`.

## Optional Direction Check

Before committing to a long run, you can generate a handful of candidate starting drafts with `check-ralph-direction.sh` and skim them to see which direction looks promising:

```bash
bash check-ralph-direction.sh
```

Candidates land under `ralph-garage/check-direction/run-NN/`. Pick one, then set `startup-source` in `config-ralph.yaml` to that path, e.g.

```yaml
startup-source: ralph-garage/check-direction/run-03
```

## Git Branching

Ralph uses two branches:

- **`main`** — where you live. Edit `paper-spec.md`, `config-ralph.yaml`, `tests/`, and everything else here.
- **`ralph/run`** — where Ralph commits each iteration. Every iteration is one commit with an `rloop-NN:` prefix.

`go-ralph-go.sh` behaves differently depending on which of the two branches you run it from:

- **From `main`** — start a fresh stretch. Ralph installs the startup baseline from `startup-source`, wipes `ralph-garage/agent-logs/`, and creates `ralph/run` (or fast-forwards an existing `ralph/run` from `main`) before looping. Your config-file changes must be committed first.
- **From `ralph/run`** — resume the existing stretch. The loop log is appended rather than wiped.

If `ralph/run` has commits that `main` hasn't seen and you try to start a fresh stretch from `main`, Ralph refuses. Switch to `ralph/run` to continue that stretch, or merge `ralph/run` into `main` first if you want to absorb it and move on.

When you're happy with a stretch, merge `ralph/run` back into `main` (or cherry-pick the pieces you want). To throw it away, delete the branch and start a fresh stretch from `main`.

## Watching a Run

Everything Ralph produces while running lands under `ralph-garage/`. None of it is committed on normal commits — it's all transient scratch space. The durable artifacts are in `paper/`, `code/`, and the `rloop-NN:` commits on `ralph/run`.

Useful entry points:

- **`ralph-garage/loop.log`** — the running console log. `tail -f ralph-garage/loop.log` during a stretch to watch progress.
- **`ralph-garage/improvement-plan.md`** — the current iteration's plan, overwritten each iteration. Peek here to see what Ralph thinks it's doing right now.
- **`ralph-garage/history/`** — per-iteration snapshots (PDFs named `NNN-paper.pdf`, plus plan and test compilations). Diff across iterations here.
- **`ralph-garage/page-images/`** — PNG renders of the current compiled paper, shared across tests. Not usually read directly, but tests reference these.
- **`ralph-garage/agent-logs/`** — raw per-invocation agent logs. For debugging unexpected agent behavior.

## Repo Structure

### Research Project

These are the paper and its supporting materials.

- `paper/` — canonical LaTeX source for the referee-ready paper (`paper.tex`, references, and only exhibits used by that paper)
- `code/` — R scripts and analysis code (if needed)
- `data/` — datasets (if needed)
- `spec/lit/` — literature for reference
- `dev/` — scratch work, journals, experiments

### Specification

`spec/` contains the source-of-truth specifications for the project, including the paper requirements, economic background, referee reports, Ralph loop behavior, and test framework.

### Tests

Test and referee definitions that evaluate the paper.

- `tests/` — PASS/FAIL test scripts (no prefix) and open-ended referee scripts (`referee-` prefix)
- `test-results/` — latest test and referee outputs

### Ralph (Permanent)

Infrastructure that drives the improvement loop.

- `ralph/` — loop script, agent wrapper, prompts, init script

### Ralph Garage (Transient)

Working artifacts generated during a Ralph run.

- `ralph-garage/improvement-plan.md` — the current iteration's plan
- `ralph-garage/page-images/` — uncommitted page renders of the current compiled paper, shared across tests
- `ralph-garage/history/` — iteration history (PDFs, plan/test compilations)
- `ralph-garage/loop.log` — console output from the ralph loop

### Dev Logs

Non-canonical debugging output.

- `ralph-garage/agent-logs/` — logs from agent invocations

