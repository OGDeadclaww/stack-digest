# Python
_read only if the project is Python_

> Entries older than 60 days live in `archive/python-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).

### 2026-09-24 — Sloth Bytes
- **Tool:** Python Workers are now GA on Cloudflare — FastAPI, Django, and Flask run natively (no Uvicorn/Gunicorn setup); call Cloudflare's own services (D1, R2, Workers AI, Queues) directly from Python without a JavaScript conversion step, connect to Postgres/MySQL through Hyperdrive with normal drivers, and AI libraries like `openai`, `langchain`, and `mcp` just work. Runs compiled to WebAssembly, so multiprocessing/threading don't work. [blog.cloudflare.com](https://blog.cloudflare.com/python-workers-ga/)

### 2026-08-27 — Sloth Bytes
- **Lesson:** "When `str.lower()` is a security vulnerability" — locale/Unicode-dependent string normalization can hide real security edge cases; worth auditing string comparisons in security-sensitive Python code. [sethmlarson.dev](https://sethmlarson.dev/when-str-lower-is-a-security-vulnerability)

### 2026-08-20 — The Code
- **Tool:** RouteLLM — pip-installable router that drops into the OpenAI client and automatically shifts simpler queries to cheaper models. [github.com/lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM)
