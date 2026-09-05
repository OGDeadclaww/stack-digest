# JS / Frontend — archive (2026-01)

### 2026-01-27 — Sloth Bytes
- **Lesson:** Server state (API data — needs caching, background refetching, staleness tracking) is fundamentally different from client state (pure UI — simple, component-scoped). Use TanStack Query or SWR for server state from day one instead of hand-rolling it in `useEffect` or dumping API responses into Redux/Context; wrap each API resource in its own hook (`useUser()`) so swapping the data source later only touches the hook.
