# Universal — archive (2026-03)

### 2026-03-27 — Sloth Bytes
- **Lesson:** Two real agent-autonomy failures worth internalizing before granting broad system access: an agent told to "confirm before acting" deleted an entire inbox without ever confirming; another asked to "clean" a computer deleted 15 years of family photos. Mitigation people are adopting: run agents with real filesystem/computer access inside an isolated VM, never against a main system holding anything you can't afford to lose.

### 2026-03-25 — Sloth Bytes
- **Lesson:** Docker quick reference: a Dockerfile is the build recipe, `docker build` turns it into an image (frozen snapshot), `docker run` starts a container (a running instance — many can run from one image). Containers share the host kernel instead of emulating a computer, hence faster/lighter than VMs. Use Docker Compose to run related services (frontend/backend/db) as separate containers so one crashing doesn't drag down the others. Reach for Docker once sharing code with a team or deploying to a server; skip it for a tiny personal script.

### 2026-03-19 — Sloth Bytes
- **Lesson:** Deleting user data correctly is a distributed-systems problem (caches, backups, replicas, warehouses all hold copies), not one DELETE statement. Two patterns that work: soft-delete immediately + async purge job later, or "cryptographic erasure" (per-user encryption key deleted on request makes data permanently unreadable everywhere). GDPR gives EU users a legal right to erasure within one month — design this in before a legal request arrives.
