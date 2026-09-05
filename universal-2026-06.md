# Universal — archive (2026-06)

### 2026-06-19 — Sloth Bytes
- **Tool:** MDN MCP server — hooks a coding agent directly into MDN's live docs instead of relying on stale training-data browser-support knowledge. [developer.mozilla.org](https://developer.mozilla.org/en-US/blog/introducing-mdn-mcp-server/)
- **Lesson:** Dropbox built an agent that uses MCP to flag gaps between a design spec and the code actually shipped — a concrete production use of MCP beyond autocomplete, worth modeling for spec-drift checks. [dropbox.tech](https://dropbox.tech/security/dropbox-mcp-dash-design-code-security)
- **Tool:** eve (Vercel) — open-source agent framework where the whole agent lives in one directory: markdown instructions + TypeScript tools. [vercel.com/blog](https://vercel.com/blog/introducing-eve)
- **Lesson:** Vercel Connect gives agents temporary scoped credentials instead of long-lived API keys sitting in env vars — a pattern worth copying for any agent you give real API access to.

### 2026-06-17 — Sloth Bytes
- **Tool:** Free system-design resources worth bookmarking: ByteByteGo (real-system breakdowns), [system-design-primer](https://github.com/donnemartin/system-design-primer) (fundamentals + Q&A + diagrams), "Jordan Has No Life" (distributed-systems case studies), [awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) (real engineering postmortems), hellointerview.com (ex-Meta staff engineer articles/problems).

### 2026-06-05 — Sloth Bytes
- **Lesson:** Companies are pulling back on unmetered agent token spend after runaway bills (one reportedly spent $500M in a month after forgetting a usage cap) — set explicit usage caps on any agent tooling you run.
- **Lesson:** Docker's "Coding Agent Horror Stories: the rm -rf ~/ Incident" documents an agent deleting an entire home directory with one command — a concrete case for sandboxing/guardrails before letting an agent run unsupervised destructive shell commands.

### 2026-06-02 — Sloth Bytes
- **Lesson:** Binary-search pattern recognition: sorted/sortable data to search → binary search; "find the first index where X becomes true" → boundary search; "find the min/max value satisfying condition X" → search a range of possible answers, not an array; a rotated sorted array still has at least one sorted half at every step. If an O(n) solution works and you're asked to optimize, think O(log n) first.
- **Tool:** `git bisect` — binary-searches commit history to find which commit introduced a bug (`git bisect start` / `bad` / `good <ref>`, then answer at each checkout). Especially useful when a long run of agent-authored commits makes manual bisection impractical.
- **Lesson:** Database indexes are effectively binary search under the hood (B-trees) — sorted data lets a query eliminate half the remaining rows per step, why an index makes lookups fast at any table size.
