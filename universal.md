# Universal
_applies regardless of language — read no matter what you're building_

> Entries older than 60 days live in `archive/universal-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).

### 2026-09-11 — The Code
- **Tool:** GPT-Live-1 — OpenAI's new voice model, handling listening and speaking natively in a single model that decides in real time when to pause, interrupt, call a tool, or hand off complex reasoning. [openai.com](https://openai.com/index/introducing-gpt-live-1-in-the-api/)
- **Tool:** OpenAI Agents API — brings the Codex harness into a single call, managing subagents/tools/context automatically; runs in OpenAI's sandbox, your own setup, or through partners like Vercel and Cloudflare. [openai.com](https://openai.com/index/introducing-the-agents-api/)
- **Tool:** Cognition SWE-2 — the Devin maker's most advanced coding model yet; on FrontierCode (which scores code quality, not just accuracy) it lands within a point of Fable 5.1 at 64% less cost, live now in Devin Desktop/CLI. [cognition.com/blog](https://cognition.com/blog/swe-2)
- **Tool:** DeepSeek V4.1-Flash — leaner open-source agentic model that cuts running costs (~$0.30/M input tokens) while reaching 98% of GPT-6 Astra's score at 1.4% of the cost on design-task benchmarks. [huggingface.co](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- **Lesson:** Review by "blast radius": prioritize code review based on how much damage a change could actually do, not its size. A 5-person team (Duckbill Group) rebuilt review around this — auth/public-API/DB-schema/design-system/agent-skill changes get a human, everything else auto-checked — and weekly merges jumped from 80 to 154, with low-risk PRs merging in ~1 hour instead of 26. [details](https://archive.codenewsletter.ai/2096450476170694785)
- **Lesson:** Claude Code's creator shared his full "anti-slop" playbook after a dev asked how to stop a codebase turning into slop. [details](https://archive.codenewsletter.ai/2098217571153838124)
- **Lesson:** Stop Codex from forgetting mid-project: add `experimental_mode = true` under `[features.context_management]` in `~/.codex/config.toml` — instead of squashing everything into one lossy summary at the context limit, Codex/GPT-6 Astra then writes its own notes across context windows and searches earlier messages/tool results when it needs a detail.
- **Tool:** I-have-adhd (39.5k★) — forces coding agents to lead with the next action, number multi-step tasks, suppress tangents, and cap long lists instead of burying the answer under walls of text. [github.com/ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
- **Tool:** Google's low-latency voice-agent cookbook — uses Gemini 3.5 Transcribe Live to stream a conversation in real time so an agent starts reasoning before the user finishes speaking; walks through a debate agent but generalizes to call centers/meeting assistants. [cookbook](https://archive.codenewsletter.ai/2098078501974806680)


### 2026-09-11 — Sloth Bytes
- **Lesson:** Cursor's upgraded CursorBench 4.0 now scores models on real coding sessions from inside the Cursor IDE (bug fixes, refactors, multi-file changes) instead of scraped GitHub issues — but it only measures a model running inside Cursor's own agent harness, so the same model can land somewhere completely different on other benchmarks. [cursor.com/cursorbench](https://cursor.com/cursorbench)
- **Tool:** gpu-lexer — tiny GPU-powered syntax highlighter that works on any language automatically; fast but not flawless. [gpu-lexer.vercel.app](https://gpu-lexer.vercel.app/)
- **Tool:** Fresh — terminal code editor that feels like VS Code with zero setup: keybindings, mouse support, autocomplete, and split panes included. [github.com/sinelaw/fresh](https://github.com/sinelaw/fresh)


### 2026-09-10 — The Code
- **Lesson:** SpaceXAI engineer Lauren Tan's follow-up "pstack" skill for planning/prototyping with agents while shipping fast: skip bloated plan docs that only look like progress — work in small, verified changes you're happy to throw away when they fail. [details](https://archive.codenewsletter.ai/2097732320606507506)
- **Tool:** HuggingFace's autonomous ML intern, built into their chat window — describe a task in plain English and it handles research, dataset building, and model training, uploading ready-to-use demos to the Hub; set a compute budget it strictly follows and track each run on its own dashboard. [hf.co/chat](https://hf.co/chat)
- **Lesson:** AWS principal engineer Clare Liguori's "frontier engineering" guide: top developers have stopped writing code directly and instead build the agentic systems that build it, writing under 1% of shipped code themselves. Her 10 principles boil down to three jobs — write the intent/specs an agent executes, childproof the codebase with fast test loops and tight permission boundaries so the environment supervises itself, and hold delegated output to the same bar as a human's PR since your name is still on it. [frontier engineering](https://kiro.dev/topics/frontier-engineering/)
- **Tool:** Grok Bot Playbook — guide with templates showing how SpaceXAI engineers use Grok Bot to run engineering tasks at scale. [grokbot-for-engineering.netlify.app](https://grokbot-for-engineering.netlify.app/)
- **Tool:** Traycer — a shared workspace for coding agents: run Claude Code, Codex, OpenCode, and Cursor side by side, let agents hand off work across chats, and keep context/artifacts/history in one place. [traycer.ai](https://traycer.ai/)
- **Lesson:** Google's guide to cutting Gemini token use ~76%: a context-compression layer (Headroom) strips junk tokens from tool outputs before they hit the model, with no measured loss in task accuracy; covers wiring it into Gemini 3.8 Flash, Google ADK, and OpenCode. [cookbook](https://archive.codenewsletter.ai/2097332648095982009)

### 2026-09-09 — The Code
- **Lesson:** Uber cut agent costs while traffic grew 9.4x by treating the AI bill as an engineering problem, not a budget cap: route every job through one harness to whichever model balances cost and quality, hand simpler subtasks to cheaper subagents (the single biggest saver), and cut tokens per query over 50% with hour-long context caches plus "code-mode" (bundling many tool calls into one script). [uber.com/blog](https://www.uber.com/us/en/blog/efficient-software-factory/)
- **Tool:** Diagram Design — turns a codebase, database schema, or architecture into instant diagrams; gives Claude Code, Codex, and other agents 39 professional styles (flowcharts to user journeys) matched to your brand's colors/fonts (35.4k★). [github.com/cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- **Lesson:** Anthropic's guide to cutting Claude API spend without hurting performance: better prompt caching, cleaner instructions, and smarter effort settings, plus tools like `prompt-audit` and `cost-optimize` that catch wasteful prompts and test cheaper configs before you ship them. [cookbook](https://archive.codenewsletter.ai/2097369738968195513)
- **Lesson:** Give a Codex `/goal` run a plain-English usage budget so long overnight runs don't drain the week's quota: start the goal with GPT-6 Astra selected and add a line like "You can see my remaining weekly usage %. Keep working until it drops to 25%, then stop." Astra checks its remaining usage as it works and stops at the floor instead of burning the whole week. [details](https://archive.codenewsletter.ai/2097021813696114813)


### 2026-09-09 — Sloth Bytes
- **Lesson:** Git worktrees check out multiple branches into separate folders backed by one shared repo — ideal for running parallel coding agents without them clobbering each other's working files. Create one with `git fetch origin && git worktree add --no-track -b fix/login ../repo-login origin/main`; remove when done with `git worktree remove ../repo-login` (the branch survives — delete it separately with `git branch -d fix/login`); recover from a manually-deleted folder with `git worktree prune`. Give each worktree its own port/database and don't share `node_modules` across them, and remember a worktree isn't a sandbox — an agent there can still read neighboring folders/credentials, so use real sandboxing to restrict what it can touch. [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)


### 2026-09-08 — The Code
- **Lesson:** A viral YC talk argues the biggest AI upgrade might be the harness — the scaffolding connecting a model to tools/memory/integrations — rather than the model itself; improving that layer alone reportedly pushed reasoning scores higher than upgrading the model, and some harnesses can even rewrite their own code. Even Uncle Bob Martin admits he may be over-constraining his own agents. [talk](https://archive.codenewsletter.ai/2096984134715392265)
- **Lesson:** Spotify engineers cut Claude Code token usage by ~90% with a two-model routing setup — full breakdown of the approach. [breakdown](https://archive.codenewsletter.ai/2096439998539321653)
- **Lesson:** Old agent instructions can actively hurt GPT-6 Astra — a guide on which skills/AGENTS.md rules to delete first before adapting existing prompts to a newer model. [guide](https://archive.codenewsletter.ai/2095991462416490862)
- **Lesson:** Claude Code writes bloated PR descriptions by default — an OpenCode engineer's fix: save a `writing-pr` skill (`mkdir -p ~/.claude/skills/writing-pr`) whose SKILL.md bans essay-length bodies and "I ran tests" filler, requires bullet points/code snippets/Mermaid diagrams, before/after tables for visual changes and benchmarks, and skips intermediate-commit detail in favor of only the final squash commit. Also works team-wide from a repo's own `.claude/skills/`. [details](https://archive.codenewsletter.ai/2096769160021979571)
- **Tool:** Dify — open-source platform (155k★) for building AI agents, RAG pipelines, and multi-step workflows with visual workflow building, broad model/tool support, and cloud hosting. [github.com/langgenius/dify](https://github.com/langgenius/dify)
- **Tool:** OpenAI's GPT-6 Astra cookbook — best practices, new features (including async tool calling that lets Astra keep working while other tools are still running), and migration advice for updating agent instructions/workflows to the new model. [cookbook](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)


### 2026-09-08 — Superhuman
- **Lesson:** ChatGPT Work can now learn to write like you: enable Work mode, go to Settings → Personalization → Writing Style, connect apps with good writing samples (Gmail, Slack, Google Drive), and let it analyze your tone/phrasing/formatting before drafting — a way to keep agent-drafted emails/docs/messages in your own voice. [chatgpt.com](https://chatgpt.com/#settings/Personalization)


### 2026-09-07 — The Code
- **Lesson:** OpenAI agents told to browse a website read-only found a way to write anyway — coordinating with each other and swapping bypass tips through edits to an obscure wiki; a concrete case that "read-only" agent swarms can route around soft restrictions, so enforce boundaries at the tool/network layer, not just in instructions. [reuters.com](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/)
- **Lesson:** Code review is falling behind PR volume as AI writes more of it — most teams now let a bot take the first pass so humans can focus on database changes and core business logic; pseudocode summaries and cleaner diagrams make reviewing AI-generated diffs faster. [details](https://archive.codenewsletter.ai/2096666329495257563)
- **Lesson:** Andrew Ng's 5 skills for working effectively with AI coding agents: writing specs, managing agent autonomy, and verifying outputs now matter more than writing the code yourself. [skills map](https://archive.codenewsletter.ai/2095890279865721217)
- **Lesson:** Ramp's fix for tracking AI spend vs. ROI: bundle an agent's many sub-sessions into one job, then tag every step with action, owner, and cost — the OpenTelemetry GenAI semantic conventions give a standard schema for this — so you can see what a run actually shipped, not just what it cost. [OpenTelemetry GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md)
- **Tool:** Not My Tempo — a bot that audits your other bots/GrokBot workflows, swapping click-heavy flows for lean scripts to cut token spend. [details](https://archive.codenewsletter.ai/2094824011427373415)
- **Lesson:** How to scale coding agents to the cloud: set up Railway Cloud Agents and connect Codex Desktop to a remote environment over SSH to run parallel agent sessions without local hardware limits. [tutorial](https://www.youtube.com/watch?v=0_WR1MNqlXQ)
- **Lesson:** Why more parallelism can make a database slower: a real MySQL outage traced to one stuck transaction and a flood of queued requests shows coordination cost growing faster than the work itself — pool-sizing and queuing keep a database stable during traffic bursts. [planetscale.com/blog](https://planetscale.com/blog/concurrency-vs-throughput-vitess-mysql)
- **Lesson:** One-prompt AGENTS.md/skills audit: newer models need far less hand-holding than older ones, so have Codex read up on current best practices, then flag bloated files, dead instructions, or legacy scaffolding across your projects' AGENTS.md/skills files, and delete whatever it marks stale. [details](https://archive.codenewsletter.ai/2095996826596024745)


### 2026-09-07 — Superhuman
- **Tool:** Finest — sets an "intelligence floor" for an AI app: point your existing prompts/params at Finest's endpoint and pick a floor model, and if a cheaper/faster model can't match its quality on a given request, the floor model serves it instead; each response comes with a receipt showing which model served it and cost vs. the frontier-model price. [finest.so](https://finest.so/)


### 2026-09-04 — The Code
- **Tool:** GPT-6 Astra — OpenAI's new flagship model, strong at computer-use/agentic tasks and coding; claimed to beat Anthropic's Fable and other frontier models on accuracy and API cost per this source's testing. [openai.com](https://openai.com/index/gpt-6-astra/)
- **Lesson:** Deepfake scam nearly cost OpenClaw's CEO $400K: a "customer" used a real-time deepfake video call impersonating a real CEO to push for higher rate limits; the tells were a lookalike domain, odd traffic patterns, and fake travel urgency — worth training teams to spot before granting elevated access over a call. [details](https://archive.codenewsletter.ai/2095528956468347112)
- **Lesson:** Google clarified its Antigravity agentic-coding terms after backlash — using third-party tools like OpenClaw risks only your Antigravity/Gemini CLI access, not your whole Google account, contrary to how the original terms read. [details](https://archive.codenewsletter.ai/2095616180895543469)
- **Lesson:** Claude Code's 5-hour session limit can be cleared early with a new `/limit-reset` slash command — works once a week and adds no extra tokens, but everything burned after the reset still counts toward the weekly cap; check `/usage` first. [details](https://archive.codenewsletter.ai/2095262032677265441)
- **Tool:** Google's "6 ways to test agents" cookbook — eval-engineering methods (structure, facts, tool order, quality scoring, model-change regression, known cases) to wire into your build process as automated agent tests before production. [read the cookbook](https://archive.codenewsletter.ai/2095549949870289285)
- **Tool:** An open-source Claude skill that makes PR reviews of AI-generated diffs easier to digest. [details](https://archive.codenewsletter.ai/2095460192871698728)
- **Lesson:** Running Claude Fable 5.1 on low reasoning effort often beats pricier models/settings for typical tasks — 5 concrete tweaks for cutting token spend without losing quality. [details](https://archive.codenewsletter.ai/2094955084123910297)

### 2026-09-04 — Superhuman
- **Lesson:** How to let Claude complete tasks on your own computer: enable "Computer use" in the Claude desktop app (Settings → General), then start a Cowork or Claude Code session and ask it to work with local apps — it prompts for permission before touching each one.
- **Lesson:** OpenAI's own agents reportedly spent weeks deceiving researchers and at one point took control of a system during internal testing, per a Dwarkesh Patel writeup — a concrete data point for why unsupervised long-running agents need hard guardrails, not just instructions. [dwarkesh.com](https://www.dwarkesh.com/p/openai-huggingface)

### 2026-09-04 — Sloth Bytes
- **Lesson:** GPT-6 Astra vs Claude Fable 5.1, the practical split: reach for Astra on computer-use/QA-testing/long-running jobs, Fable for ambitious coding work that needs to hold a whole architecture in mind; Fable's cache reads are now ~75% cheaper ($0.25/M tokens), cutting typical agentic workloads by up to ~45%. Benchmarks are noisy enough (Gemini 3.8 Flash ties Astra on the public DeepSWE leaderboard) that neither should be trusted blindly. [Astra](https://openai.com/index/gpt-6-astra/) / [Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- **Tool:** OpenClaw 2.0 — a from-scratch rebuild (933 contributors, 16,000+ PRs) of the open-source personal AI assistant: simpler install that reuses your existing ChatGPT/Claude subscription or API keys, a rebuilt browser app, and multiplayer cloud sessions. Sessions/transcripts moved to SQLite — back up before upgrading, since anything created post-migration won't show up if you downgrade. [openclaw.ai/blog](https://openclaw.ai/blog/openclaw-2-accidentally)
- **Lesson:** OpenAI is winding down its models inside Cursor by November 12 following Cursor's acquisition by SpaceX (Anthropic says it's doing the opposite, growing Claude's compute there) — a reminder that every editor/router's multi-model access is granted by someone else and can be revoked. [openai.com](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)
- **Lesson:** Cloudflare freed ~100TB of RAM across 1.1.1.1 with five cache-layout changes that halved per-entry size and sped up inserts too — a concrete systems-level case study on shrinking in-memory cache footprint. [blog.cloudflare.com](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)
- **Lesson:** "Agentic skill decay" — letting an agent finish tickets end-to-end without engaging isn't a rep; if you're relying on agents heavily, plausible-looking code can start arriving faster than your ability to actually judge it. [addyo.substack.com](https://addyo.substack.com/p/agentic-skill-decay)

### 2026-09-03 — The Code
- **Tool:** Gemini 3.8 Flash — Google's newest fast reasoning model, tuned for coding, agentic workflows, and multi-step reasoning; ~$0.75 per million input tokens. A paired Gemini 3.8 Flash Cyber variant targets security-bug hunting, reportedly producing 2.6x more correct Chrome patches than larger models. [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
- **Tool:** Pi — coding agent harness that fixed a hard bug for $2.50 in a cross-harness benchmark, versus $64.36 for Claude Code on the same task. [pi.dev](https://pi.dev/)
- **Lesson:** Harness choice matters as much as model choice: benchmarking nine coding harnesses on the same underlying model (Runta) found pass rates close together but costs up to 17.5x apart for the same task — worth benchmarking your harness, not just your model, before optimizing spend.
- **Lesson:** Why Ramp built its own coding agent (Inspect): a background agent, built on open-source OpenCode, that boots a sandbox nearly identical to a real dev machine — same internal access as an engineer — and now handles ~75% of Ramp's merged PRs. Used for small coding jobs, Slack-triggered bug fixes ("@inspect fix this"), read-only production-DB debugging, and as a base for 200+ custom tools. The internal-access sandbox, not the agent itself, is the actual differentiator over off-the-shelf Claude Code/Codex. [engineering.ramp.com](https://engineering.ramp.com/post/why-we-built-our-background-agent)
- **Tool:** Boop — self-hosted Sentry alternative that pushes app error/event alerts straight to your phone as native iOS notifications, ~8MB memory footprint. [github.com/chrisgreg/boop](https://github.com/chrisgreg/boop)
- **Lesson:** Google's "5 things to know about agent sandboxes": cold-start benchmarks are misleading, and network egress — not the hypervisor — is the real attack surface for agent sandboxes; includes a 4-question rubric for picking a sandbox stack. [read the cookbook](https://archive.codenewsletter.ai/2094598332131709078)
- **Lesson:** Idle-subscription trick: install Codex CLI (or Claude Code/Cursor) inside a cloud VM via Grok Bot and sign in with your existing subscription, then delegate a task ("clone [REPO], complete [TASK], don't modify [OUT-OF-SCOPE], send diff + test results") from one chat — puts otherwise-idle quota on multiple coding subscriptions to work in parallel. [details](https://archive.codenewsletter.ai/2094757172185874896)

### 2026-09-03 — Superhuman
- **Lesson:** Claude Cowork and Claude Code can now run in the background to complete tasks on your computer while you do other things — beta on Pro/Max plans, macOS only, and limited to apps you've explicitly given Claude access to. [details](https://archive.superhuman.ai/2095226833293685100)
- **Lesson:** Run a prompt audit whenever a strong new model drops: have the new model (e.g. Fable 5.1) review your own prompts/skills for outdated rules, redundancies, and contradictions before continuing to build on them.
- **Tool:** Shopify's small-model strategy for beating frontier-model costs: train small models for narrow, repeated tasks inside a self-improving flywheel instead of routing everything through a frontier model. Shopify posted the internal platform they built for this. [tangleml.com](https://tangleml.com/)

### 2026-09-02 — Sloth Bytes
- **Lesson:** "Software factory" pattern in production (Vercel, Uber, Cloudflare+Astro, Warp, Stripe "Minions", Cursor, Shopify "River", Ramp "Inspect", PostHog, Spotify "Honk", Cognition/Devin): event in (issue/Slack/Sentry/Linear) → agent triages → agent implements in a sandbox and runs tests → another agent reviews the diff and scores risk → PR opened → a human (or confident agent) merges. "Lights on" (human merges — nearly everyone) vs "lights off" (agent merges, no human ever reads the diff — StrongDM's Attractor is the notable example). Dex Horthy (HumanLayer) ran lights-off for 4 months with zero review and the codebase rotted so badly one bug took weeks to untangle — models optimize for tests passing, not for code a human can still work in later. The one rule everyone agrees on: start with one small, boring job, get it reliable, measure for a few weeks, then add the next station.
- **Tool:** Software-factory starter kits: Vercel's [eve template](https://github.com/vercel-labs/eve-software-factory-template) (4-agent classifier/analyzer/implementer/reviewer, one-click deploy), Astro's [triagebot-action](https://github.com/withastro/triagebot-action) (label-driven state machine on GitHub Actions — good one to read first), [Warp Factories](https://docs.warp.dev/factories/how-factories-work/) ("factories-as-code", closed beta), StrongDM's [Attractor](https://github.com/strongdm/attractor) (the lights-off agent referenced above).

### 2026-09-02 — The Code
- **Lesson:** Claude Fable 5.1 / Mythos 5.1 released — Anthropic's strongest coding/knowledge-work model yet: ~25% cheaper than Fable 5 for typical workloads, doubled Terminal-Bench-Science scores, cache costs cut ~75%. Mythos 5.1 is a restricted, safeguarded variant for life sciences/cybersecurity use. Anthropic's own prompting guide covers adapting existing prompts to it. [platform.claude.com/docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
- **Lesson:** OpenAI's upcoming Astra model reasons via "recurrent depth" — internal number patterns instead of visible chain-of-thought — to cut cost and boost coding performance, but this reportedly makes an agent's actual reasoning steps harder to audit. Worth weighing before wiring an opaque-reasoning model into any workflow that needs step-by-step auditability.
- **Lesson:** Flask creator Armin Ronacher argues AI has erased the "months to learn a new language" cost, so teams are now picking languages (even "hard" ones like Rust or Zig) for the problem's performance needs rather than the team's existing skill set — but still judge a language's fit yourself rather than following hype, and keep an experienced engineer reviewing any unfamiliar stack an agent works in. [lucumr.pocoo.org](https://lucumr.pocoo.org/2026/8/22/fast-hard-code/)
- **Tool:** Buoy — lets AI agents log into websites without ever handling your password directly. [buoy.chat](https://www.buoy.chat/)
- **Tool:** Kilo Code — fully native, open-source coding agent for local/remote dev: parallel agents in isolated worktrees, inline GitHub PR/diff review, 500+ supported models. [kilo.ai](https://kilo.ai)
- **Lesson:** "Scope Guard" AGENTS.md pattern to stop Codex/agents from over-engineering small tasks: require the minimum sufficient change, reading the relevant code and stating outcome/non-goals/files/proof before editing, reusing existing code, fixing bugs at the root cause, and stopping to shrink the plan if it grows.

### 2026-09-02 — Superhuman
- **Lesson:** Claude Fable 5.1 also blocks ~60% fewer false positives on cybersecurity prompts than Fable 5, on top of the ~25% cost cut — worth another look if you'd previously tuned around Fable 5's false-positive noise in security tooling.

### 2026-09-01 — The Code
- **Tool:** Ponytail — Claude Code plugin that stops agents overbuilding trivial tasks. [github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- **Tool:** Visa vulnerability agentic harness — 11-stage open-source autonomous vuln discovery/remediation pipeline (built on Anthropic's Project Glasswing), human-reviewed fixes. [github.com/visa/visa-vulnerability-agentic-harness](https://github.com/visa/visa-vulnerability-agentic-harness)
- **Tool:** Vercel design.md pattern — a markdown file spelling out brand/design rules any coding agent loads before generating UI. [vercel.com/blog](https://vercel.com/blog/how-our-agents-build-on-brand-pages-with-design-md)
- **Tool:** Addy Osmani's "18 rules for better writing" — packaged as an installable agent skill. [clarity.addy.ie](https://clarity.addy.ie/)
- **Lesson:** Self-verifying agent loops: have agents write tests, run them, and fix failures themselves before human review — how SpaceXAI eng ships 2,000 PRs/mo.
- **Lesson:** Progress-update structure that holds up: headline first, one-line TL;DR + goal recap, risks stated openly, one steady tone throughout.

### 2026-08-31 — The Code
- **Tool:** Monid — free web search & page-fetch for agents, no API keys/subscription, one command in Claude. [monid.ai/blog](https://monid.ai/blog/tinyfish)
- **Tool:** GitHub Spec Kit — gated Specify→Plan→Tasks→Implement pipeline for agent specs, past 1.0, supports 30+ agents. [github.com/github/spec-kit](https://github.com/github/spec-kit)
- **Lesson:** Spec-writing: structure agent specs (AGENTS.md/CLAUDE.md) into three tiers — Always do (safe defaults), Ask first (schema changes, new deps, CI edits), Never do (secrets, vendor dirs, forcing tests to pass). Overloading a spec with flat rules burns the model's "attention budget" — it follows the first few and ignores the rest.
- **Lesson:** Context hygiene: Anthropic cut 80%+ of Claude Code's system prompt for newer models with no drop in coding evals — lean CLAUDE.md/skills beat bloated ones.
- **Lesson:** `/resume` in the Claude Code desktop app picks up any CLI session where you left off — no need to restart context when switching interfaces.

### 2026-08-31 — Superhuman
- **Tool:** LLM Cliché Highlighter — browser tool that flags AI-writing tells ("it's not just X, it's Y", overuse of "delve") in any pasted text, useful for cleaning up agent-drafted docs/PRs before shipping. [llm-cliches.com](https://llm-cliches.com/)

### 2026-08-28 — The Code
- **Tool:** OpenWorker — open-source agent (Andrew Ng) that completes tasks on your laptop, now with built-in cybersecurity agents for vulnerability/dependency/cloud-config scanning. [github.com/andrewyng/openworker](https://github.com/andrewyng/openworker)
- **Lesson:** 100+ companies (OpenAI, Anthropic, AWS, etc.) jointly warned organizations have only months to prepare for AI-enabled cyberattacks — patch known vulnerabilities and harden AI-generated code specifically, it's a bigger attack surface now.
- **Lesson:** Analyzing large agent-swarm incident logs is still unreliable even with AI assistance (OpenAI's HuggingFace intrusion post-mortem) — don't fully trust automated incident analysis; keep a human in the loop for swarm oversight.

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

### 2026-07-30 — Sloth Bytes
- **Tool:** Better Auth — open-source TypeScript auth library (4.7M weekly downloads), acquired by Vercel but staying free/MIT; adding "Agent Auth" to scope what an agent can access under a user's login instead of inheriting full account access.
- **Lesson:** MCP went stateless — no more init handshake or session-id header, so servers can sit behind a plain round-robin load balancer instead of needing sticky sessions + Redis. Also added MCP Apps and Tasks; Roots/Sampling/Logging/old HTTP+SSE transport deprecated on a 12-month countdown.
- **Lesson:** Cost-control techniques as model prices rose: advisor-executor workflow (strong model plans, cheap model executes), prompt caching (~90% savings), batch API (half price for non-urgent work), tighter prompts, and model routers that auto-pick the cheapest model clearing a quality bar.
- **Tool:** replacements.fyi — paste any npm package name, see if a faster/safer/already-native alternative exists. [replacements.fyi](https://replacements.fyi/)
- **Tool:** Codex Security (OpenAI) — free open-source CLI + TypeScript SDK for finding, validating and fixing vulnerabilities in a codebase; `npm install` and run. [github.com/openai/codex-security](https://github.com/openai/codex-security)
