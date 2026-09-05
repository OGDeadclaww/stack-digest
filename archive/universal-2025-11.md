# Universal — archive (2025-11)

### 2025-11-20 — Sloth Bytes
- **Lesson:** Cloudflare's worst outage since 2019 cascaded from one local error (a config file exceeding a hard-coded row limit) through their whole proxy network. Their own fix, worth generalizing: treat internal config as untrusted input (validate/bound-check it), add kill switches, and audit how a small local error could cascade into a total outage.

### 2025-11-18 — Sloth Bytes
- **Lesson:** Core mental model for an "agent": an LLM (non-deterministic, good at language) combined with tools — deterministic functions/APIs — it calls when a task needs precision it can't reliably produce itself.
- **Lesson:** What actually determines whether an agent calls the right tool at the right time: a clear, specific tool description + parameter schema; a clear system prompt stating who it is and what it's trying to do; and the underlying model's own tool-calling strength.
- **Lesson:** Minimal tool-calling pattern (Vercel AI SDK, shape generalizes): define a tool with a Zod schema to validate arguments before your code runs on them, pass a step-count cap to prevent runaway loops/cost, and inspect the returned step trace rather than trusting the model's final prose.
- **Lesson:** Keep temperature low (~0–0.5) for agents doing tool-calling or other deterministic-style tasks — high temperature adds unwanted randomness to tool selection and reasoning, not just wording.

### 2025-11-14 / 11-15 / 11-21 — Sloth Bytes
- **Note:** Subscriber welcome/survey emails — no technical content.
