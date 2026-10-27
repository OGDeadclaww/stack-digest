# Universal — archive (2026-08)

### 2026-08-27 — The Code
- **Tool:** GLM-5.3-Flash — open multimodal model tuned for agentic/long-horizon coding, ~1/10 the price of comparable frontier models, near Claude Opus 4.8 on coding benchmarks. Via OpenRouter/Z.ai. [z.ai/blog](https://z.ai/blog/glm-5.3-flash)
- **Lesson:** Andrew Ng's 6 pillars for AI engineering: LLM foundations, grounding models with data/context, building agentic systems (tool choice + bounds), evaluation-driven development (prove changes help, don't trust gut read), operating in production (monitoring/cost/quality), ML foundations.

### 2026-08-27 — Sloth Bytes
- **Tool:** Bun 1.4 — Rust rewrite of the runtime, big perf jump (idle CPU down 5x, memory down up to 35%). `node:http`/`node:fs` pass 97% of Node's tests; Playwright/vitest run. [bun.com/blog](https://bun.com/blog/bun-v1.4)
- **Lesson:** Debian is voting on whether AI-written contributions are allowed at all. Node.js's policy is a good default to borrow: use AI to research/understand a codebase, but never let raw model output be committed as-is without a human owning it.
- **Lesson:** Claude Code only reads CLAUDE.md, not the AGENTS.md standard other agents (Codex, Cursor, Copilot) read — causes a split-brain problem on multi-tool teams. Workaround: reference/import AGENTS.md from inside CLAUDE.md.
- **Tool:** hk — git hook manager that runs linters in parallel without letting overlapping auto-fixes race each other. [github.com/jdx/hk](https://github.com/jdx/hk)
- **Lesson:** Uber's AI software factory: 70%+ of their PRs now come from agents; they had to build dedicated systems so agent-authored PRs don't overwhelm CI.

### 2026-08-26 — The Code
- **Tool:** dzhng/skills — David Zhang's open-sourced skills implementing the "software factory" audit loop below; drops into Claude Code, Cursor, Codex. [github.com/dzhng/skills](https://github.com/dzhng/skills)
- **Tool:** Headlong — alpha open-source microharness giving agents a continuous inner loop (self-set priorities, runs shell commands around the clock, ~$1–2/hr in tokens). [github.com/laude-institute/headlong](https://github.com/laude-institute/headlong)
- **Tool:** codex-plugin-cc — official OpenAI Codex plugin that reviews Claude Code's changes without leaving the terminal (second-opinion reviewer). [github.com/openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)
- **Lesson:** "Software factory" code-review approach for high-volume AI-generated code: treat the codebase as a black box divided into small pieces with clear inputs/outputs; attach sensors and examine outputs instead of reading implementation; keep invariants, traces, attack surface, and spec-silent decisions readable per piece; get a ranked decision ledger each run and read decisions instead of the diff; keep the auditor sub-agent separate from the implementer so audits stay honest.
- **Lesson:** Building your own agent harness needs: tool design, safety gates, sandboxes, context pruning, subagents, human approvals, planning, verification, extensibility — the checklist before rolling a custom harness. [vercel.com/academy](https://vercel.com/academy/build-ai-agent-harness)

### 2026-08-25 — The Code
- **Tool:** AgentSky — "OpenRouter for coding agents": pick a harness + model, swap via config with no lost history, compare cost/results side by side. [agentsky.dev](https://agentsky.dev/)
- **Tool:** session-migrate — carry a coding session between agents (Claude Code, Codex, Pi, OpenCode, Copilot CLI, Cursor) when you hit a usage limit mid-task. [github.com/xhluca/session-migrate](https://github.com/xhluca/session-migrate)
- **Lesson:** Cutting agent token cost 2.7x with an open harness comes from 4 levers: context offloading, subagents, "code mode" (agent writes code to do a task instead of many tool calls), and compaction.
- **Tool:** Claude Code Remote Control: `claude auth login` then `claude remote-control` from your project dir, press spacebar for a QR code — steer a running session from your phone while files/MCP/tools stay local.

### 2026-08-25 — Superhuman
- **Tool:** WorkOS Relay — hosted relay for connecting agents to enterprise SSO/directory data without building the auth plumbing yourself. [workos.com/relay](https://workos.com/relay)
- **Lesson:** Three traits of companies successfully scaling agents in production: scope each agent to one narrow job, instrument agent actions the same way as human-triggered events (failures show up in normal monitoring), and keep a human approval gate on anything irreversible (payments, deletes, external sends).

### 2026-08-24 — The Code
- **Tool:** swarm-forge — Uncle Bob Martin's open-source 5-agent assembly line for feature work. [github.com/unclebob/swarm-forge](https://github.com/unclebob/swarm-forge)
- **Lesson:** 5-agent pipeline pattern beats one agent doing everything: Specifier (spec + manual test checklist) → Coder (feature + unit tests) → Cleaner (simplifies) → Hardener (tries to break tests on purpose) → QA (scripts the checklist against the real app). Splitting keeps each agent's prompt short enough to actually follow.
- **Tool:** Walgit — single-binary Rust git server serving repos as plain static files off cheap cloud storage, no DB, MIT-licensed. Useful as a GitHub-outage-proof or cheap self-hosted git backend. [github.com/tobi/omasnap](https://github.com/tobi/omasnap)
- **Lesson:** Token/cost engineering (Google guide): prune and cache agent context, batch offline work, cap reasoning tokens, route simple tasks to smaller models.

### 2026-08-21 — The Code
- **Lesson:** API design rules that hold up under agent-driven development: get it right the first time, never remove/restructure existing fields, treat versioning as a last resort, a good product covers for a rough API but not vice versa, prefer simple API keys over OAuth for non-professional users, and always plan for the API going down (rate limits + kill switches ready).
- **Lesson:** Long-horizon agent design patterns (Google): checkpointing and resuming work, pausing for human approval — needed once agents run for hours/days so failures don't mean starting over.

### 2026-08-20 — The Code
- **Tool:** Router.com (Ramp) — single endpoint auto-routing each request to the cheapest model clearing your quality bar; OpenAI/Anthropic-compatible, free through 2026 with credits. [docs.router.com](https://docs.router.com/)
- **Tool:** Anthropic Cybersecurity Skills — 817 ready-made security skills across 29 domains for Claude Code, Codex CLI, Cursor. [github.com/mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
- **Tool:** terminal-code — brings a full VS Code-compatible editor into the terminal (diffs, split panes, extensions). [terminal-code.com](https://terminal-code.com/)
- **Lesson:** Canva's AI cost-reduction playbook (cut serving costs ~90%): stop routing every request through a pricey frontier model, use cheap/in-house models for high-volume work, add usage & pricing guardrails so a few heavy users can't run up the bill unchecked.

### 2026-08-06 — Sloth Bytes
- **Tool:** Agent Plugins 1.0 — open, vendor-neutral standard (AWS/GitHub/Microsoft/OpenAI/Vercel-backed) for packaging Agent Skills + MCP servers into one plugin folder instead of a different format per client. [agent-plugins.org](https://agent-plugins.org/)
- **Lesson:** Evil Martians' security checklist for publishing npm packages safely in 2026. [evilmartians.com](https://evilmartians.com/chronicles/the-secure-way-to-release-an-npm-package)
- **Lesson:** Truffle Security scanned 7.6PB of public HuggingFace training datasets and found 221,303 working credentials across 187M files — secrets committed to public repos get baked into models permanently; scan your own repos proactively (gitleaks/trufflehog-style).
- **Tool:** github/gitignore — canonical `.gitignore` templates per language/framework. [github.com/github/gitignore](https://github.com/github/gitignore)

### 2026-08-04 — Sloth Bytes
- **Lesson:** Git undo cheat sheet — uncommitted mistake → `git restore <file>` (or `--staged` to unstage without losing changes); committed but local → `git reset --soft HEAD~1` (keeps staged) or `git reset HEAD~1` (mixed, unstages too) or `--hard` (deletes changes — branch first as a safety net); already pushed/shared → `git revert <commit>` (new commit that reverses it, history intact); `git commit --amend` fixes the most recent unpushed commit.

