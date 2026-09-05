# Universal — archive (2026-04)

### 2026-04-30 — Sloth Bytes
- **Lesson:** Node.js 20 LTS reached end-of-life April 30, 2026 — no more security patches. Upgrade to Node 22 (to Apr 2027) or Node 24 (to Apr 2028) if any project is still pinned to 20.
- **Tool:** Warp terminal open-sourced its client under AGPL v3 (cloud orchestration stays closed) — Rust-built, with direct Claude Code/Codex/Gemini CLI support. [github.com/warpdotdev/warp](https://github.com/warpdotdev/warp)

### 2026-04-23 — Sloth Bytes
- **Lesson:** Vercel security-incident case study: an employee's broad ("Allow All") OAuth grant to an unrelated third-party AI tool from a work account let an attacker pivot into internal systems and reach env vars that weren't flagged "sensitive" (stored plaintext), while properly-flagged sensitive vars stayed encrypted. Takeaways: mark real secrets as sensitive/encrypted wherever your host supports it, and avoid granting broad OAuth scopes to third-party tools from a work account.
- **Lesson:** OpenAI's Agents SDK reference architecture worth modeling regardless of SDK: a "harness" layer managing tool calls/working directory/reasoning state/memory separately from an isolated sandboxed execution environment, so credentials never sit where model-generated code runs, plus automatic state snapshot/rehydrate if a sandbox dies mid-task.

### 2026-04-21 — Sloth Bytes
- **Lesson:** Two habits that eliminate most coding-agent hallucination: give detailed instructions pointing at exact existing files/components/patterns to follow instead of vague requests, and explicitly tell the agent to read the relevant docs before implementing instead of relying on training-data memory of an API.
- **Lesson:** Sloppy patterns to call out in a project rules file: dumping everything into one file, copy-pasting instead of extracting a shared helper, redefining types that already exist elsewhere, and reinventing a battle-tested package from scratch.

### 2026-04-16 — Sloth Bytes
- **Tool:** supabase.sh — browse Supabase's docs over SSH, pipeable straight into Claude Code (`ssh supabase.sh setup | claude`) so an agent gets current docs without hallucinating outdated syntax.
- **Lesson:** `llms.txt` — a proposed standard (like robots.txt, but for LLMs): a site exposes a clean markdown entry point at `/llms.txt` for AI tools to read at inference time instead of scraping human-oriented HTML.
- **Tool:** GitHub Copilot CLI now supports BYOK — point it at Azure OpenAI, Anthropic, any OpenAI-compatible endpoint, or a fully local model via env vars; `COPILOT_OFFLINE=true` stops all telemetry for air-gapped use.
- **Tool:** GitHub Stacked PRs (native, private preview) + `gh stack` CLI — arrange a big change as an ordered stack of small reviewable PRs with one-click cascading rebase; `npx skills add github/gh-stack` teaches an agent to split large diffs into stacks automatically.
- **Lesson:** Anthropic published a practical guide on what changes for defenders once AI makes finding/exploiting vulnerabilities dramatically faster — worth reading before wiring agents up to anything important. [claude.com/blog](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense)
- **Lesson:** Cloudflare published exactly how they rolled MCP out company-wide (security architecture, cost cuts, pitfalls) — a useful reference before connecting agents to internal tools at any scale. [blog.cloudflare.com](https://blog.cloudflare.com/enterprise-mcp/)

### 2026-04-03 — Sloth Bytes
- **Lesson:** Claude Code accidentally shipped its full unredacted source map (~2,000 files, 500k+ lines) in a March 31 npm update — rotate API keys/credentials as a precaution if you updated around that date.
- **Tool:** Stripe Projects (dev preview) — a CLI that provisions an entire stack (hosting, DB, auth, AI services, analytics) across accounts you own with a few commands, dropping credentials into your local env automatically instead of copy-pasting across dashboards.
- **Lesson:** "The Feedback Loop Is All You Need" — a rules file (CLAUDE.md) only states intent; automated checkers that actually enforce those rules are what stops a codebase drifting away from them over time.
- **Lesson:** Vercel's internal warning to their own engineers: a PR from a coding agent can look perfect and pass every test while still silently destroying production infrastructure — passing tests is not proof an agent-authored infra change is safe.
