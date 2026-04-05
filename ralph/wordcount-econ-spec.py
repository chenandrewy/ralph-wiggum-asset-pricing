# Usage: python ralph/wordcount-econ-spec.py
# Input: spec/paper-spec.md
# Output: word count of the Economic Requirements section (stdout)

import re
from pathlib import Path

spec = Path(__file__).resolve().parents[1] / "spec" / "paper-spec.md"
text = spec.read_text()

# Extract content between the Economic Requirements heading and the next ## heading
match = re.search(
    r"^## I\.\s+Economic Requirements\n(.+?)(?=^## |\Z)",
    text,
    re.MULTILINE | re.DOTALL,
)
if not match:
    raise SystemExit("Could not find Economic Requirements section")

section = match.group(1)
# Strip markdown list numbering (e.g. "1.", "- a.", "- i.", "- ii.")
section = re.sub(r"^\s*[-*]\s+[a-z]+\.\s?", " ", section, flags=re.MULTILINE)
section = re.sub(r"^\s*\d+\.\s?", " ", section, flags=re.MULTILINE)
words = len(section.split())
print(f"{words} words in Economic Requirements section")
