# Python
_read only if the project is Python_

> Entries older than 60 days live in `archive/python-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).

### 2026-09-24 — Sloth Bytes
- **Tool:** Python Workers are now GA on Cloudflare — FastAPI, Django, and Flask run natively (no Uvicorn/Gunicorn setup); call Cloudflare's own services (D1, R2, Workers AI, Queues) directly from Python without a JavaScript conversion step, connect to Postgres/MySQL through Hyperdrive with normal drivers, and AI libraries like `openai`, `langchain`, and `mcp` just work. Runs compiled to WebAssembly, so multiprocessing/threading don't work. [blog.cloudflare.com](https://blog.cloudflare.com/python-workers-ga/)

