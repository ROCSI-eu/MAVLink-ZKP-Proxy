#!/usr/bin/env python3
"""Check local Markdown links, anchors, JSON examples, and license-state wording."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]+>|[^\s)]+)")
REFERENCE_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})\s*([^\s`]*)\s*$")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
HTML_ANCHOR_RE = re.compile(r"<(?:a\s+[^>]*(?:id|name)|[^>]+\s+id)=[\"']([^\"']+)", re.I)


def markdown_files() -> list[Path]:
    return [*sorted(ROOT.glob("*.md")), *sorted((ROOT / "docs").rglob("*.md"))]


def slug(text: str) -> str:
    """Approximate GitHub's heading IDs without requiring a Markdown package."""
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"[`*_~]", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    occurrences: dict[str, int] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    fence_char = ""
    fence_len = 0
    for index, line in enumerate(lines):
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence, fence_char, fence_len = True, marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        heading = match.group(1) if match else None
        if heading is None and index + 1 < len(lines) and line.strip():
            if re.match(r"^\s{0,3}(?:=+|-+)\s*$", lines[index + 1]):
                heading = line.strip()
        if heading is not None:
            base = slug(heading)
            count = occurrences.get(base, 0)
            occurrences[base] = count + 1
            anchors.add(base if count == 0 else f"{base}-{count}")
        anchors.update(unquote(value) for value in HTML_ANCHOR_RE.findall(line))
    return anchors


def check_link(source: Path, line_number: int, destination: str, failures: list[str]) -> None:
    destination = destination.strip("<>")
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return
    raw_path, fragment = unquote(parsed.path), unquote(parsed.fragment)
    if not raw_path and not fragment:
        return
    if not raw_path:
        target = source
    else:
        target = (ROOT / raw_path.lstrip("/")) if raw_path.startswith("/") else (source.parent / raw_path)
    try:
        target = target.resolve()
        target.relative_to(ROOT)
    except (OSError, ValueError):
        failures.append(f"{source.relative_to(ROOT)}:{line_number}: link escapes the repository: {destination}")
        return
    if not target.exists():
        failures.append(f"{source.relative_to(ROOT)}:{line_number}: unresolved link: {destination}")
        return
    if fragment:
        anchor_target = target / "README.md" if target.is_dir() else target
        if anchor_target.suffix.lower() != ".md" or fragment not in anchors_for(anchor_target):
            failures.append(f"{source.relative_to(ROOT)}:{line_number}: unresolved anchor: {destination}")


def check_file(path: Path, failures: list[str]) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    fence_marker: str | None = None
    json_start = 0
    json_lines: list[str] = []
    for line_number, line in enumerate(lines, 1):
        fence = FENCE_RE.match(line)
        if fence_marker is not None:
            if fence and fence.group(1)[0] == fence_marker[0] and len(fence.group(1)) >= len(fence_marker):
                if json_start:
                    try:
                        json.loads("\n".join(json_lines))
                    except json.JSONDecodeError as error:
                        failure_line = json_start + error.lineno
                        failures.append(f"{path.relative_to(ROOT)}:{failure_line}: invalid JSON: {error.msg}")
                fence_marker, json_start, json_lines = None, 0, []
            elif json_start:
                json_lines.append(line)
            continue
        if fence:
            fence_marker = fence.group(1)
            if fence.group(2).lower() == "json":
                json_start = line_number
            continue
        destinations = [match.group(1) for match in LINK_RE.finditer(line)]
        reference = REFERENCE_RE.match(line)
        if reference:
            destinations.append(reference.group(1))
        for destination in destinations:
            check_link(path, line_number, destination, failures)
    if json_start:
        failures.append(f"{path.relative_to(ROOT)}:{json_start}: unclosed JSON fence")


def main() -> int:
    failures: list[str] = []
    for path in markdown_files():
        check_file(path, failures)
    required = [
        ROOT / "LICENSE",
        ROOT / "LICENSING.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "docs/adr/0003-layered-licensing-model-for-the-open-proof-path.md",
        ROOT / "docs/dependency-licensing-policy.md",
    ]
    for path in required:
        if not path.is_file():
            failures.append(f"missing required licensing document: {path.relative_to(ROOT)}")

    recognized = {"MIT", "MPL-2.0", "CC-BY-4.0", "CC0-1.0"}
    licensing = (ROOT / "LICENSING.md").read_text(encoding="utf-8")
    mapped = set(re.findall(r"`([A-Za-z0-9.-]+)`", licensing)) & recognized
    if mapped != recognized:
        failures.append(f"licensing policy identifiers differ from expected SPDX set: {sorted(mapped)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    adr = required[3].read_text(encoding="utf-8")
    decisions = (ROOT / "docs/decisions.md").read_text(encoding="utf-8")
    if "MIT License](LICENSE) remains the current effective license" not in readme:
        failures.append("README must state that MIT remains the current effective license")
    if "Status | Proposed;" not in adr or "MIT remains effective" not in decisions:
        failures.append("ADR and decision register must agree that the proposal is not effective")
    forbidden_effective = re.compile(r"(?:project|repository) is (?:now )?(?:MPL|CC-BY|CC0)[ -]licensed", re.I)
    for path in markdown_files():
        if forbidden_effective.search(path.read_text(encoding="utf-8")):
            failures.append(f"{path.relative_to(ROOT)}: layered proposal presented as effective")
    if (ROOT / "LICENSES").exists() or (ROOT / ".reuse/dep5").exists():
        failures.append("proposed transition must not add LICENSES/ or .reuse/dep5 before approval")
    if failures:
        print("Documentation check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Documentation check passed ({len(markdown_files())} Markdown files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
