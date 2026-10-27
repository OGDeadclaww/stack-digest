# Universal — archive (2026-07)

### 2026-07-30 — Sloth Bytes
- **Tool:** Better Auth — open-source TypeScript auth library (4.7M weekly downloads), acquired by Vercel but staying free/MIT; adding "Agent Auth" to scope what an agent can access under a user's login instead of inheriting full account access.
- **Lesson:** MCP went stateless — no more init handshake or session-id header, so servers can sit behind a plain round-robin load balancer instead of needing sticky sessions + Redis. Also added MCP Apps and Tasks; Roots/Sampling/Logging/old HTTP+SSE transport deprecated on a 12-month countdown.
- **Lesson:** Cost-control techniques as model prices rose: advisor-executor workflow (strong model plans, cheap model executes), prompt caching (~90% savings), batch API (half price for non-urgent work), tighter prompts, and model routers that auto-pick the cheapest model clearing a quality bar.
- **Tool:** replacements.fyi — paste any npm package name, see if a faster/safer/already-native alternative exists. [replacements.fyi](https://replacements.fyi/)
- **Tool:** Codex Security (OpenAI) — free open-source CLI + TypeScript SDK for finding, validating and fixing vulnerabilities in a codebase; `npm install` and run. [github.com/openai/codex-security](https://github.com/openai/codex-security)

### 2026-07-03 — Sloth Bytes
- **Lesson:** Claude Sonnet 5 specifics: model ID `claude-sonnet-5`, 1M-token context window by default now, manual extended-thinking param removed (adaptive thinking runs automatically — passing it throws a 400), and the same text costs ~30% more tokens than on Sonnet 4.6 — recheck hardcoded `max_tokens` limits so outputs don't get silently clipped.
