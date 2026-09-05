#!/usr/bin/env python3
"""
Moves day-blocks older than ARCHIVE_DAYS out of each live section file
into archive/<section>-YYYY-MM.md, keeping the live files short.

Run this after inserting today's new day-blocks (as the daily digest job
already does), from the repo root:

    python3 scripts/archive_old_entries.py

Safe to run even when nothing needs archiving (no-op).
"""
import re
import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DAYS = 60
SECTIONS = ["universal", "python", "javascript", "powershell"]  # links.md is manual, not archived here

DATE_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2})")


def parse_blocks(text):
    """Split a live file's body into (header_lines, [ (date_str_or_None, block_text) ]).
    A block starts at a line matching '### ' and runs until the next '### ' or EOF.
    """
    lines = text.splitlines(keepends=True)
    header = []
    blocks = []
    i = 0
    while i < len(lines) and not lines[i].startswith("### "):
        header.append(lines[i])
        i += 1
    while i < len(lines):
        m = DATE_RE.match(lines[i])
        date_str = m.group(1) if m else None
        block_lines = [lines[i]]
        i += 1
        while i < len(lines) and not lines[i].startswith("### "):
            block_lines.append(lines[i])
            i += 1
        blocks.append((date_str, "".join(block_lines)))
    return "".join(header), blocks


def main():
    cutoff = datetime.date.today() - datetime.timedelta(days=ARCHIVE_DAYS)
    archive_dir = REPO_ROOT / "archive"
    archive_dir.mkdir(exist_ok=True)

    for section in SECTIONS:
        live_path = REPO_ROOT / f"{section}.md"
        if not live_path.exists():
            continue
        header, blocks = parse_blocks(live_path.read_text(encoding="utf-8"))

        keep, moved = [], {}
        for date_str, block_text in blocks:
            d = None
            if date_str:
                try:
                    d = datetime.date.fromisoformat(date_str)
                except ValueError:
                    d = None
            if d is not None and d < cutoff:
                key = f"{d.year:04d}-{d.month:02d}"
                moved.setdefault(key, []).append(block_text)
            else:
                # keep unparseable/odd date strings (e.g. multi-date notes) in the live
                # file rather than risk mis-filing them — safe default, not a bug.
                keep.append(block_text)

        if not moved:
            continue

        live_path.write_text(header + "".join(keep), encoding="utf-8")

        for key, block_texts in moved.items():
            arch_path = archive_dir / f"{section}-{key}.md"
            new_content = "".join(block_texts)
            if arch_path.exists():
                old = arch_path.read_text(encoding="utf-8")
                # keep newest-first within the month file
                sep = "\n" if not old.endswith("\n\n") else ""
                arch_path.write_text(new_content + sep + old, encoding="utf-8")
            else:
                title = section.capitalize() if section != "javascript" else "JS / Frontend"
                arch_path.write_text(f"# {title} — archive ({key})\n\n{new_content}", encoding="utf-8")

        print(f"{section}: archived {sum(len(v) for v in moved.values())} block(s) into {list(moved.keys())}")


if __name__ == "__main__":
    main()
