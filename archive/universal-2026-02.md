# Universal — archive (2026-02)

### 2026-02-25 — Sloth Bytes
- **Lesson:** A* search improves on Dijkstra for large graphs by adding an admissible heuristic to prioritize nodes closer to the goal — same guaranteed-correct result, far less work.
- **Lesson:** Contraction Hierarchies — the real technique behind Google Maps' speed: pre-process a graph offline into shortcut edges between important nodes so live queries mostly search a small "highway layer." Reported 10–100x faster than raw A* — worth knowing for any repeated shortest-path query over a graph too large to search from scratch each time.

### 2026-02-11 — Sloth Bytes
- **Lesson:** JIT (V8, HotSpot, CLR) optimizes adaptively at runtime but pays a warm-up cost; AOT (C, C++, Rust) front-loads optimization with zero runtime overhead but no adaptivity — why real-time/embedded/security-sensitive systems (iOS blocks JIT outside Safari) stick with AOT, and brief serverless cold starts don't benefit from JIT. Rule of thumb: JIT suits long-running complex apps, AOT suits resource-constrained or latency-critical ones.
