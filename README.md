# ralph-wiggum-asset-pricing

This repo uses Geoff Huntley's [Ralph Wiggum loop](https://ghuntley.com/ralph/) to generate an academic asset pricing paper. 

The default starting point is the checked-in blank template in `paper/` and `code/`. The checked-in paper specification is a worked example modeled on my asset pricing theory paper, ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf).

If you want Ralph to write a different paper, update:
- `spec/paper-spec.md`
- `spec/economic-background.md`
- `config-ralph.yaml`

and perhaps
- `tests/*.py`

Before running, use the dev container or install the tools below, authenticate with Claude and/or Codex (default uses Claude only), start from `main`, and commit your setup (including `config-ralph.yaml`, `paper/`, `code/`, and any edits to `spec/` or `tests/`). The default live `paper/` and `code/` are already a blank template; see [Initializing `paper/` and `code/`](#initializing-paper-and-code) if you want to replace them with a check-direction candidate. Ralph refuses to start from `main` if `paper/` or `code/` are untracked, staged, or dirty. Then, as long as you feel comfortable with agents in Yolo mode and have credits for the configured agent (Claude by default),
```bash 
bash go-ralph-go.sh
```

will have the AIs start working on your paper.


**How "Hedging the Singularity" was actually generated:** the files on `main` are a lightweight setup. The heavier setup used for the paper included literature and a referee report specific to "Hedging the Singularity". See the [`ralph/run-final`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/ralph/run-final) branch for the full setup. The human-written preface was added on the [`human-preface`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/human-preface) branch, which is where [the final PDF](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf) lives.

## How Ralph Works

Each iteration of the loop:

1. `ralph/author-plan.py` reads the latest test results and `spec/paper-spec.md`, and writes `ralph-garage/improvement-plan.md`.
2. `ralph/author-improve.py` executes that plan against the paper and code.
3. Scripts in `tests/` evaluate the result.
4. If any test fails, go back to step 1.

Huntley's Ralph is *human on the loop*. The human is not *in* the loop, but they stay *on* it by watching `ralph-garage/loop.log` and checking `test-results/*.md` (see [Watching a Run](#watching-a-run)). They then adjust `paper-spec.md`, `config-ralph.yaml`, etc., to steer the AIs in the right direction. The branch model (see [Git Branching](#git-branching)) makes stopping, resuming, and discarding stretches cheap.

On the [`ralph/run-final`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/ralph/run-final) branch, I attempted *human as Clockmaker* instead. It didn't work out — see the preface of [the final PDF](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf).


## Environment Setup and Safety Model

Ralph runs coding agents in YOLO mode. The agent wrapper invokes Claude with `--dangerously-skip-permissions` and Codex with `--sandbox danger-full-access`.

Docker is not required, but I recommend running Ralph inside the dev container because it isolates YOLO agents and installs the expected toolchain: bash, git, Python 3, R, LaTeX (`pdflatex` and `biber`), Poppler page-rendering tools, the configured agent CLI, and common Python/R data packages.

The simplest setup is to open this repo in VS Code and use "Reopen in Container" (requires [Docker Desktop](https://docs.docker.com/desktop/) and the [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/create-dev-container)). See `.devcontainer/README.md` for container and credential details. I develop on macOS; Windows users (untested) should clone into WSL2 rather than the Windows filesystem (for file I/O, line endings, and symlinks like `AGENTS.md`) and run `Install-Module CredentialManager` in PowerShell so `.credentials/get-credentials.py` can read Windows Credential Manager.

If you skip Docker, Ralph can still work on a properly provisioned macOS/Linux/WSL2 machine, but you are responsible for installing the same tools and authenticating whichever agent CLI you configure.

If your spec or code uses WRDS, I recommend saving your WRDS credentials once per machine on the host (not inside the container):

```bash
python .credentials/setup.py
```

Rebuild the container afterward so it picks up the credentials. Verify with:

```bash
python .credentials/check-wrds.py
```

Inside the container, credentials are exposed as environment variables — `WRDS_USERNAME` and `WRDS_PASSWORD`. Read them from your code with `Sys.getenv("WRDS_USERNAME")` in R or `os.environ["WRDS_USERNAME"]` in Python. The checked-in blank template includes `code/query-wrds-example.R` as a working example to adapt.

To add other credentials (e.g. API keys), edit `.credentials/credentials-map.json` — see `.devcontainer/README.md`.

## Selecting Claude vs Codex

Each agent invocation is configured by three module-level constants near the top of a Python script: `AGENT` (`"claude"` or `"codex"`), `MODEL`, and `EFFORT`. The checked-in scripts default to Claude; edit these constants to switch providers or change model tiers.

The scripts fall into two groups:

- `ralph/author-plan.py`, `ralph/author-improve.py`, `ralph/author-fix-build.py` — the three phases of the loop (plan, apply, repair LaTeX build errors)
- `tests/*.py` — each test and referee script runs its own agent invocation, with its own `AGENT` / `MODEL` / `EFFORT`

You'll need credits with whichever provider you choose. See `ralph/agent_wrapper.py` for the full list of supported agents, models, and effort values.


## Key Files

### `spec/paper-spec.md` — Paper Specification

Basically the paper in bullet point form. On `main`, this file ships with the Hedging paper-spec as a worked example — **replace it with your own paper's spec** before running Ralph. `spec/economic-background.md` follows the same pattern: it holds shared vocabulary (key terms and conventions the paper depends on) and ships pre-filled with Hedging terms like AI singularity and incomplete markets, so edit it to match your paper.

You can leave `paper-spec.md` open-ended if you have confidence in your tests. As explained in the preface of ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf), I found that I needed to make it rather tight. But hopefully your agents are more up for your task.

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

One can also turn on continual improvement and open-ended referees
```yaml
continual-improvement: true

referees: true

selected-referees:
  - referee-top3
```
Continual improvement means Ralph will keep going even if all tests pass. The referees are not pass/fail: they generate open-ended feedback. I couldn't get this to work well for ["Hedging the Singularity"](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/blob/human-preface/finalization/output-named/paper.pdf). But once again, I hope your agents do better.

Paper/code initialization is intentionally outside `config-ralph.yaml`. Ralph starts from the committed live `paper/` and `code/` directories on `main`; the default checked-in versions are a blank template. The old `startup-source` key is deprecated and now causes setup to fail.

### `tests/*.py` — Tests and Referees

Scripts in `tests/` with no prefix are tests; scripts prefixed `referee-` are referees. Test IDs are filenames without `.py` (e.g. `tests/spec-paper.py` → `spec-paper`, `tests/referee-top3.py` → `referee-top3`). Edit these when your paper needs different checks than the template.

### `go-ralph-go.sh` — Running Ralph

The main entry point. See [Git Branching](#git-branching) for how it behaves on each branch.

## Initializing `paper/` and `code/`

Ralph always starts from committed live `paper/` and `code/`. On a fresh clone, these are very minimal templates. You can, alternatively, copy in your own `paper/` and `code/` before the first run. Commit whichever baseline you choose on `main` before starting Ralph.

Another option is to have the AIs generate candidate starting points based on the spec by running

```bash
bash check-ralph-direction.sh
```
The candidates land under `ralph-garage/check-direction/run-NN/`, with preview PDFs copied to `ralph-garage/check-direction/paper-NN.pdf`. Pick the one you prefer, and copy over the `paper/` and `code/` folders.

`check-ralph-direction.sh` also runs from committed inputs. It creates isolated worktrees from `HEAD` by default, so uncommitted edits to `paper/`, `code/`, `spec/`, `config-ralph.yaml`, `tests/`, agent instructions, or Ralph author tooling are not included and will cause the preflight to fail.

## Git Branching

Ralph is *human on the loop*: the human works freely on `main`, and Ralph works only on `ralph/run`. That split keeps cleanup cheap — you can always throw `ralph/run` away without touching your own edits.

- **`main`** — the human's branch. Edit anything: `paper/`, `code/`, `spec/`, `config-ralph.yaml`, `tests/`, `ralph/`. Commit at your own pace. Ralph never commits here.
- **`ralph/run`** — Ralph's working branch. Every iteration is one commit prefixed `rloop-NN:`. This is a reusable label, not a one-time run identifier.

`go-ralph-go.sh` behaves differently depending on which branch you run it from:

- **From `main`** — start (or extend) a Ralph stretch. Ralph requires committed, clean `paper/` and `code/` on `main`; if either is missing, untracked, staged, or dirty, Ralph exits with an error. Otherwise Ralph wipes `ralph-garage/agent-logs/`, creates `ralph/run` off `main` (or fast-forwards an existing `ralph/run` to `main`), records the current paper/code baseline, and begins looping.
- **From `ralph/run`** — resume the existing stretch. The loop log is appended rather than wiped.

If `ralph/run` has commits that `main` hasn't seen and you try to start from `main`, Ralph refuses. Switch to `ralph/run` to continue that stretch, or merge `ralph/run` into `main` first if you want to absorb it and move on.

Typical lifecycle:

1. Set up on `main`: edit `paper-spec.md`, `config-ralph.yaml`, `tests/`, and prepare `paper/` and `code/` (see [Initializing `paper/` and `code/`](#initializing-paper-and-code)). Commit everything needed for the baseline.
2. Run `bash go-ralph-go.sh`. Ralph creates `ralph/run` and iterates.
3. Watch the run. To intervene, stop Ralph, hand-edit where needed, and restart — Ralph tolerates a dirty tree when it resumes.
4. When you're happy with a stretch, merge `ralph/run` back into `main` (or cherry-pick). `paper/` and `code/` now live on `main`.
5. To start the next stretch, just run `go-ralph-go.sh` from `main` again. Ralph picks up the current `paper/` and `code/` as the new baseline. To throw a stretch away, delete `ralph/run` and restart.

## Watching a Run

Everything Ralph produces while running lands under `ralph-garage/`. None of it is committed on normal commits — it's all transient scratch space. The durable artifacts are in `paper/`, `code/`, and the `rloop-NN:` commits on `ralph/run`.

If you're impatient, watch:

- **`ralph-garage/agent-logs/`** — raw per-invocation agent logs. For debugging unexpected agent behavior. Or being antsy about whether the agents are working.

Human-friendly entry points:

- **`ralph-garage/loop.log`** — the running console log. `tail -f ralph-garage/loop.log` during a stretch to watch progress.
- **`ralph-garage/improvement-plan.md`** — the current iteration's plan, overwritten each iteration. Peek here to see what Ralph thinks it's doing right now.
- **`ralph-garage/history/`** — per-iteration snapshots (PDFs named `NNN-paper.pdf`, plus plan and test compilations). Diff across iterations here.
- **`ralph-garage/page-images/`** — PNG renders of the current compiled paper, shared across tests. Not usually read directly, but tests reference these.


## Test Suite

This repo's `tests/` folder is the test suite for the asset-pricing theory example in this repo. The fuller 25-test version used for "Hedging the Singularity" lives on the [`ralph/run-final`](https://github.com/chenandrewy/ralph-wiggum-asset-pricing/tree/ralph/run-final/tests) branch and groups into six families:

- **`element-*`** (5) — required elements exist in the paper (specific figures, citations, meta-rhetoric).
- **`factcheck-*`** (8) — claims match code output, literature, and each other.
- **`spec-*`** (3) — paper matches `spec/paper-spec.md`, economic background, and stated scope.
- **`theory-*`** (4) — theory-paper quality: clarity, no deadweight content, intro pay-off, cautious treatment of unmodeled channels.
- **`visual-*`** (3) — figures and page-level visuals render well.
- **`writing-*`** (2) — introduction and intuition sections read well.

Plus a `build-latex` infrastructure check that the paper compiles.

"Hedging the Singularity" burned through two $200/month Claude Code subscriptions end-to-end with all 25 tests running. The default test set in `config-ralph.yaml` on `main` is a small subset of these, so a quick-start run will be much lighter.

For empirical papers, you probably want a different mix. See [`ralph/tests/`](https://github.com/chenandrewy/HumanxAI-ChenAY/tree/main/ralph/tests) in [HumanxAI-ChenAY](https://github.com/chenandrewy/HumanxAI-ChenAY), which was built for an empirical finance paper. Those tests are not part of this repo's current `tests/` folder, and their paths/helper imports differ, so treat them as source material to port rather than files to copy blindly. Claude or Codex can usually port them quickly if you ask it to adapt the paths, helper imports, and report locations to this repo.

Tests from HumanxAI-ChenAY that are especially worth considering:

- **`factcheck-econ`** — checks whether the abstract, introduction, and central claims are actually supported by the empirical evidence; useful for catching causal or mechanism overreach.
- **`story-narrative`** — checks whether every section contributes to one clear main story, rather than accumulating disconnected robustness checks or side arguments.
- **`story-exhibit-coherence`** — reviews exhibit-bearing pages and asks whether the figures and tables tell a coherent empirical story with consistent visual logic.
- **`story-exhibit-structure`** — checks whether exhibits are numbered, ordered, nonredundant, and tied to a primary empirical metric.
- **`transparency-calibration`** — checks whether calibration inputs, assumptions, fitted quantities, and imposed quantities are transparent to a careful reader.
- **`writing-natural`** — reviews section-level prose for compressed, jargon-heavy, or stat-stuffed writing; useful but relatively expensive because it uses section-level subreviews.
- **`visual-tables`** — checks table formatting, readability, page fit, and row ordering from rendered page images.

The point is not to turn on every possible test. Pick the tests that match the paper's failure modes, run Ralph for a stretch, inspect what the tests catch and miss, then revise the test mix.

## Repo Structure

### Research Project

These are the paper and its supporting materials.

- `paper/` — canonical LaTeX source for the referee-ready paper (`paper.tex`, references, and only exhibits used by that paper); checked in as the default blank template
- `code/` — R scripts and analysis code (if needed); checked in as the default blank template
- `data/` — datasets (if needed)
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
