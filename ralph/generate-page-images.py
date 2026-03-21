#!/usr/bin/env python3
"""
How to run: python ralph/generate-page-images.py [--pdf PATH] [--output-dir PATH] [--force]
Inputs: paper/paper.pdf, paper/paper.aux
Outputs: ralph-garage/page-images/page-*.png, ralph-garage/page-images/exhibit-manifest.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess


DEFAULT_PDF = "paper/paper.pdf"
DEFAULT_OUTPUT_DIR = "ralph-garage/page-images"
DEFAULT_AUX = "paper/paper.aux"
MANIFEST_FILENAME = "exhibit-manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render paper PDF pages to PNG images")
    parser.add_argument(
        "--pdf",
        default=DEFAULT_PDF,
        help=f"Input PDF path (default: {DEFAULT_PDF})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory for page PNG files (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Always regenerate images, even if output appears up to date",
    )
    return parser.parse_args()


def artifacts_up_to_date(pdf_path: pathlib.Path, output_dir: pathlib.Path) -> bool:
    images = sorted(output_dir.glob("page-*.png"))
    if not images:
        return False
    manifest_path = output_dir / MANIFEST_FILENAME
    if not manifest_path.exists():
        return False
    pdf_mtime = pdf_path.stat().st_mtime
    oldest_image_mtime = min(image.stat().st_mtime for image in images)
    return oldest_image_mtime >= pdf_mtime and manifest_path.stat().st_mtime >= pdf_mtime


def page_number_from_image(image_path: pathlib.Path) -> int | None:
    match = re.fullmatch(r"page-(\d+)\.png", image_path.name)
    if not match:
        return None
    return int(match.group(1))


def longtable_labels(tex_dir: pathlib.Path) -> set[str]:
    """Scan .tex files for longtable environments and return their \\label{tab:...} values."""
    labels: set[str] = set()
    for tex_file in tex_dir.rglob("*.tex"):
        content = tex_file.read_text(encoding="utf-8")
        for match in re.finditer(
            r"\\begin\{longtable\}.*?\\end\{longtable\}",
            content,
            re.DOTALL,
        ):
            for label_match in re.finditer(r"\\label\{(tab:[^}]+)\}", match.group()):
                labels.add(label_match.group(1))
    return labels


def exhibits_from_aux(aux_path: pathlib.Path) -> list[dict[str, object]]:
    pattern = re.compile(
        r"\\newlabel\{(?P<label>(?P<prefix>fig|tab):[^}]*)\}"
        r"\{\{(?P<number>[^}]*)\}\{(?P<page>\d+)\}"
    )
    exhibits: list[dict[str, object]] = []

    for line in aux_path.read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)
        if not match:
            continue
        prefix = match.group("prefix")
        number = match.group("number")
        page_number = int(match.group("page"))
        kind = "Figure" if prefix == "fig" else "Table"
        exhibits.append({
            "page": page_number,
            "kind": kind,
            "number": number,
            "exhibit_id": f"{kind} {number}",
            "latex_label": match.group("label"),
        })

    return exhibits


def build_manifest(aux_path: pathlib.Path, output_dir: pathlib.Path, tex_dir: pathlib.Path | None = None) -> dict[str, object]:
    images = sorted(output_dir.glob("page-*.png"))
    exhibits = exhibits_from_aux(aux_path)
    long_labels = longtable_labels(tex_dir) if tex_dir is not None else set()
    page_to_exhibits: dict[int, list[dict[str, object]]] = {}
    figure_pages: set[int] = set()
    table_pages: set[int] = set()

    for exhibit in exhibits:
        page_number = exhibit["page"]
        label = str(exhibit["latex_label"])
        is_long = label in long_labels
        page_range = [page_number, page_number + 1] if is_long else [page_number]
        page_exhibits = page_to_exhibits.setdefault(page_number, [])
        page_exhibits.append({
            "kind": str(exhibit["kind"]),
            "number": str(exhibit["number"]),
            "exhibit_id": str(exhibit["exhibit_id"]),
            "latex_label": label,
            "page_range": page_range,
        })
        if exhibit["kind"] == "Figure":
            figure_pages.add(page_number)
        else:
            for p in page_range:
                table_pages.add(p)

    pages: list[dict[str, object]] = []
    seen_pages: set[int] = set()
    for image_path in images:
        page_number = page_number_from_image(image_path)
        if page_number is None:
            continue
        seen_pages.add(page_number)
        pages.append({
            "page": page_number,
            "image": str(image_path.relative_to(output_dir.parents[1])),
            "has_figures": page_number in figure_pages,
            "has_tables": page_number in table_pages,
            "exhibits": page_to_exhibits.get(page_number, []),
        })

    missing_pages = sorted((figure_pages | table_pages) - seen_pages)
    if missing_pages:
        missing_text = ", ".join(str(page) for page in missing_pages)
        raise ValueError(f"manifest references pages with no rendered image: {missing_text}")

    return {"pages": pages}


def write_manifest(aux_path: pathlib.Path, output_dir: pathlib.Path, tex_dir: pathlib.Path | None = None) -> int:
    manifest_path = output_dir / MANIFEST_FILENAME
    try:
        manifest = build_manifest(aux_path, output_dir, tex_dir)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return 0


def render_images(pdf_path: pathlib.Path, output_dir: pathlib.Path) -> int | None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for old in output_dir.glob("page-*.png"):
        old.unlink()

    result = subprocess.run(
        ["pdftoppm", "-png", "-r", "150", str(pdf_path), str(output_dir / "page")],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: pdftoppm failed: {result.stderr.strip()}")
        return None

    count = len(list(output_dir.glob("page-*.png")))
    if count == 0:
        print("ERROR: no page images generated")
        return None

    return count


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(__file__).resolve().parents[1]

    pdf_path = (repo_root / args.pdf).resolve()
    aux_path = (repo_root / DEFAULT_AUX).resolve()
    output_dir = (repo_root / args.output_dir).resolve()
    tex_dir = aux_path.parent

    if not pdf_path.exists():
        print(f"ERROR: missing PDF: {pdf_path}")
        return 1
    if not aux_path.exists():
        print(f"ERROR: missing AUX: {aux_path}")
        return 1

    if not args.force and artifacts_up_to_date(pdf_path, output_dir):
        count = len(list(output_dir.glob("page-*.png")))
        if write_manifest(aux_path, output_dir, tex_dir) != 0:
            return 1
        print(f"[page-images] {count} images up to date")
        return 0

    count = render_images(pdf_path, output_dir)
    if count is None:
        return 1
    if write_manifest(aux_path, output_dir, tex_dir) != 0:
        return 1
    print(f"[page-images] generated {count} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
