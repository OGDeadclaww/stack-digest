# Stack Digest

Actionable tools and lessons distilled daily from three coding newsletters (The Code, Superhuman, Sloth Bytes), sorted by stack so a coding agent reads only what applies to its project. This repo is **public** — it contains only aggregated, publicly-sourced newsletter content, nothing about any client, employer, or internal system.

## How a coding agent should read this

Fetch two raw files at the start of a project, once — not on every turn:

- `https://raw.githubusercontent.com/OGDeadclaww/stack-digest/main/universal.md` — always
- `https://raw.githubusercontent.com/OGDeadclaww/stack-digest/main/<stack>.md` — whichever of `python.md`, `javascript.md`, `powershell.md` matches the project

Example line for `CLAUDE.md` / `AGENTS.md`:

```
Before starting, fetch https://raw.githubusercontent.com/OGDeadclaww/stack-digest/main/universal.md
and https://raw.githubusercontent.com/OGDeadclaww/stack-digest/main/javascript.md (or your stack's
file) for current tool/lesson notes. Skip archive/ unless asked for history.
```

Entries run newest → oldest inside each file. Entries older than 60 days move to `archive/<section>-YYYY-MM.md` (see `scripts/archive_old_entries.py`) so the live files stay short — read archive/ only if you explicitly need history.

## Structure

```
universal.md      — applies regardless of language
python.md         — Python-specific
javascript.md     — JS/TS/frontend-specific
powershell.md     — PowerShell/Windows-specific
links.md          — manually-curated bookmarks (not part of the automated daily run)
archive/          — day-blocks older than 60 days, one file per section per month
scripts/archive_old_entries.py — moves aged-out entries from the live files into archive/
```

## ⚠️ What never goes in this repo

This repo is **public**. The daily job that populates it must never commit anything related to:

- clients, or any employer/internal systems
- any internal observation, decision, or lesson learned from non-public work

If newsletter content or a lesson ever touches on that kind of thing, **split it out**: keep the generic/public part (tool name, link, general technique) in the appropriate file here, and route anything client- or employer-specific to a separate private note instead of this repo. When in doubt, leave it out of the public file and flag it to the user rather than guessing.

## Provenance

Populated by a daily scheduled Claude Cowork task that reads three newsletter senders from Gmail, extracts concretely actionable content (installable tools with links, durable engineering lessons), and inserts new day-blocks at the top of the matching section file. Source threads are labeled `DevNews/Digested` in Gmail once processed, so each run only looks at unprocessed mail.
