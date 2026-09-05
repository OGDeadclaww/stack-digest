# JS / Frontend — archive (2026-04)

### 2026-04-30 — Sloth Bytes
- **Tool:** Node.js 24.15.0 LTS — `require(esm)` is stable (use ES modules from CommonJS files with no experimental flag), a new `--max-heap-size` flag caps memory without env-var hacks, plus OpenSSL fixes and bundled SQLite/npm updates.

### 2026-04-03 — Sloth Bytes
- **Lesson:** Real npm supply-chain attack on Axios: a compromised maintainer account pushed poisoned `axios@1.14.1`/`0.30.4` plus a malicious helper dependency `plain-crypto-js@4.2.1` that phoned home on install then deleted its own evidence. Check any lockfile for these exact versions; if found, update immediately and rotate credentials used in that project. Malware increasingly hides in an auto-pulled helper package, not the well-known package itself — audit the full dependency tree, not just top-level packages.
