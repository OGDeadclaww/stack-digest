#!/usr/bin/env python3
"""
Idempotently inserts new day-blocks at the top of a live digest section file
(universal.md / python.md / javascript.md / powershell.md), skipping any
block whose (date, source) key already exists in the file.

Usage:
    python3 scripts/insert_new_entries.py <section>.md < new_blocks.md

<new_blocks.md> on stdin is one or more blocks in the same format already
used in the live files, back to back, e.g.:

    ### 2026-09-10 — The Code
    - **Tool:** Example — description. <a href="https://example.com">link</a>
    - **Lesson:** Another one.

    ### 2026-09-10 — Sloth Bytes
    - **Tool:** ...

Blocks whose "### DATE — SRC" key already appears in the target file are
silently skipped (safe to re-run / retry a partially-failed sync).
"""
import re
import sys
from pathlib import Path

HEADER_RE = re.compile(r"^### (\d{4}-\d{2}-\d{2}) — (.+?)\s*$")


def split_into_blocks(text):
    """Split stdin text into (key, block_text) pairs. key = (date, src)."""
    lines = text.splitlines(keepends=True)
    blocks = []
    i = 0
    while i < len(lines) and not lines[i].startswith("### "):
        i += 1
    while i < len(lines):
        m = HEADER_RE.match(lines[i].rstrip("\n"))
        key = (m.group(1), m.group(2)) if m else None
        block_lines = [lines[i]]
        i += 1
        while i < len(lines) and not lines[i].startswith("### "):
            block_lines.append(lines[i])
            i += 1
        blocks.append((key, "".join(block_lines)))
    return blocks


def existing_keys(text):
    keys = set()
    for line in text.splitlines():
        m = HEADER_RE.match(line.strip())
        if m:
            keys.add((m.group(1), m.group(2)))
    return keys


def archived_keys(target):
    """Keys already moved to archive/<section>-YYYY-MM.md for this section."""
    section = target.stem
    archive_dir = target.parent / "archive"
    keys = set()
    if not archive_dir.is_dir():
        return keys
    for arch_path in archive_dir.glob(f"{section}-*.md"):
        keys |= existing_keys(arch_path.read_text(encoding="utf-8"))
    return keys


def main():
    if len(sys.argv) != 2:
        print("usage: insert_new_entries.py <section>.md < new_blocks.md", file=sys.stderr)
        sys.exit(1)

    target = Path(sys.argv[1])
    new_text = sys.stdin.read()
    new_blocks = split_into_blocks(new_text)
    if not new_blocks:
        print("no blocks found on stdin — nothing to do")
        return

    live_text = target.read_text(encoding="utf-8") if target.exists() else ""
    already = existing_keys(live_text) | archived_keys(target)

    to_insert = []
    skipped = []
    for key, block_text in new_blocks:
        if key is None:
            print(f"WARNING: skipping malformed block (no '### DATE — SRC' header):\n{block_text[:80]!r}", file=sys.stderr)
            continue
        if key in already:
            skipped.append(key)
            continue
        to_insert.append((key, block_text))
        already.add(key)

    if not to_insert:
        print(f"nothing new — all {len(skipped)} block(s) already present, skipped")
        return

    lines = live_text.splitlines(keepends=True)
    insert_at = len(lines)
    for idx, line in enumerate(lines):
        if line.startswith("### "):
            insert_at = idx
            break

    new_content_block = "\n".join(b for _, b in to_insert)
    if not new_content_block.endswith("\n"):
        new_content_block += "\n"
    if to_insert and not new_content_block.endswith("\n\n"):
        new_content_block += "\n"

    result = "".join(lines[:insert_at]) + new_content_block + "".join(lines[insert_at:])
    target.write_text(result, encoding="utf-8")

    print(f"inserted {len(to_insert)} new block(s) into {target}, skipped {len(skipped)} already-present")


if __name__ == "__main__":
    main()
