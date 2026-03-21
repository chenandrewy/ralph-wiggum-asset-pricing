#!/usr/bin/env python3
"""
How to run: python tests/writing-natural.py
Inputs: paper/paper.tex, spec/paper-spec.md
Outputs: test-results/writing-natural.md and process exit code (0=PASS, 1=FAIL)

Design: Sub-agents assess individual sections of the paper in an open-ended way,
commenting freely on whether the writing reads naturally. A main agent synthesizes
their commentary into a verdict and report.
"""

from __future__ import annotations

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from _test_helpers import build_test_context, fail_test, load_agent_model, require_paths, run_test

SUB_AGENT_MODEL = "sonnet"


def extract_sections(tex: str) -> list[dict]:
    """Split LaTeX body into section-level chunks with titles."""
    body_match = re.search(r"\\begin\{document\}", tex)
    if body_match:
        tex = tex[body_match.end():]

    end_match = re.search(r"\\end\{document\}", tex)
    if end_match:
        tex = tex[:end_match.start()]

    pattern = r"(?=\\(?:section|subsection)\{)"
    raw_chunks = re.split(pattern, tex)

    sections = []

    for chunk in raw_chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        title_match = re.match(r"\\(?:section|subsection)\{([^}]+)\}", chunk)
        if title_match:
            title = title_match.group(1)
        elif "\\begin{abstract}" in chunk:
            title = "Abstract and Front Matter"
        else:
            title = "Preamble"

        prose = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", chunk, flags=re.DOTALL)
        prose = re.sub(r"\\begin\{table\}.*?\\end\{table\}", "", prose, flags=re.DOTALL)
        prose = re.sub(r"\\input\{[^}]+\}", "", prose)
        prose = re.sub(r"%[^\n]*", "", prose)
        prose = prose.strip()
        if len(prose) < 80:
            continue

        sections.append({"title": title, "text": chunk})

    return sections


def run_sub_agent(
    section: dict,
    section_index: int,
    repo_root: Path,
    spec_path: Path,
    test_id: str,
) -> dict:
    """Run a sub-agent on one section. Returns {"title": ..., "commentary": ...}."""

    prompt = f"""You are a writing reviewer for an academic asset pricing theory paper. The paper's spec says:
"Writing is between an academic paper and a blog post. Catchy and conversational, yet rigorous. Favor plain english. Be direct and concise. Not cringey."

You are reviewing one section of the paper. Evaluate whether the writing fits the paper spec. Look out for the following problems:
- Telegram-style results: findings stated as stat fragments without verbs or context
- Cold jargon: technical terms or notation introduced before the reader has context
- Stat-stuffed sentences: multiple parenthetical statistics crammed into one sentence
- Compressed math: formulas or Greek letters dropped inline without explaining what they
  mean economically or intuitively
- Clause overload: single sentences carrying three or more distinct ideas separated by
  semicolons or em-dashes
- Missing intuition: results stated without helping the reader understand why they matter
  or what they mean in plain terms
- Dense paragraphs that try to do too much at once
- Cringey or overly dramatic language

Also consider what the section does well—natural, clear passages should be noted too.

For full context on the paper's goals, read the spec at: {spec_path}

Here is the section to review:

--- SECTION: {section['title']} ---
{section['text']}
--- END SECTION ---
"""

    cmd = [
        sys.executable,
        str(repo_root / "ralph/agent_wrapper.py"),
        "--agent", AGENT,
        "--model", SUB_AGENT_MODEL,
        "--log-mode", "off",
        "--failure-log-mode", "off",
        "--step-label", f"{test_id}-sub{section_index}",
        prompt,
    ]

    result = subprocess.run(
        cmd, cwd=repo_root, capture_output=True, text=True, timeout=300,
    )

    commentary = result.stdout.strip() if result.returncode == 0 else f"[sub-agent failed: exit {result.returncode}]"
    return {"title": section["title"], "commentary": commentary}


def main() -> int:
    context = build_test_context(__file__)
    AGENT, MODEL = load_agent_model()

    paper_path = context.repo_root / "paper/paper.tex"
    spec_path = context.repo_root / "spec/paper-spec.md"
    preflight = require_paths(context, paper_path, spec_path)
    if preflight is not None:
        return preflight

    tex = paper_path.read_text(encoding="utf-8")
    sections = extract_sections(tex)
    if not sections:
        return fail_test(context, "could not parse any sections from paper.tex")

    sub_results = []
    with ThreadPoolExecutor(max_workers=min(len(sections), 6)) as pool:
        futures = {
            pool.submit(
                run_sub_agent, section, i, context.repo_root, spec_path, context.test_id
            ): i
            for i, section in enumerate(sections)
        }
        for future in as_completed(futures):
            sub_results.append(future.result())

    title_order = {s["title"]: i for i, s in enumerate(sections)}
    sub_results.sort(key=lambda r: title_order.get(r["title"], 999))

    digest_parts = []
    for r in sub_results:
        digest_parts.append(f"### {r['title']}\n\n{r['commentary']}\n")
    digest = "\n".join(digest_parts)

    synth_prompt = f"""You are a strict test agent evaluating whether an academic asset pricing theory paper meets its
writing-quality standard. The paper's spec requires: "Writing is between an academic paper and
a blog post. Catchy and conversational, yet rigorous. Favor plain english. Be direct and concise.
Not cringey."

Read the paper as a finance PhD student encountering it for the first time—someone who
knows finance but has not read this paper before. Evaluate whether the writing lets
this reader follow the argument without stopping to decode compressed notation,
telegram-style stat fragments, or jargon that was never introduced.

Multiple reviewers have each assessed one section of the paper. Here is their commentary:

--- REVIEWER COMMENTARY ---
{digest}
--- END REVIEWER COMMENTARY ---

Requirements:
1. A first-time reader can follow each paragraph without re-reading sentences to decode them.
2. Technical concepts are introduced before they are used.
3. Results are presented in a way that conveys meaning, not just numbers.
4. The tone is conversational and not cringey.

For the paper to PASS, ALL of the requirements must be met. Otherwise, FAIL.

Write your report to: {context.report_path}
The report must be a clean, human-readable markdown file with this format:
- Line 1: # {context.test_id}
- Next line: VERDICT: PASS or VERDICT: FAIL
- Next line: REASON: one short sentence summarizing the main finding
- Then your analysis with specific quotes as evidence.
"""

    return run_test(
        context=context,
        prompt=synth_prompt,
        agent=AGENT,
        model=MODEL,
        default_agent_log_mode="verbose",
    )


if __name__ == "__main__":
    raise SystemExit(main())
