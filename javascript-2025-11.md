# JS / Frontend — archive (2025-11)

### 2025-11-26 — Sloth Bytes
- **Lesson:** React Server Components reference: a Server Component (default in Next.js 13+ App Router) runs only on the server and ships zero JS for that component. Add `"use client"` only to the component that actually needs interactivity — everything imported underneath it must also be a Client Component. Context isn't available inside Server Components (they don't re-render) — fetch data directly or pass it down as props.

### 2025-11-20 — Sloth Bytes
- **Tool:** Prisma 7 rewrote its ORM client from Rust to TypeScript — 90% smaller bundle, 3x faster queries, lower CPU/memory. Generated code moved out of node_modules into your own source dir; new `prisma.config.ts`; Prisma Postgres now speaks standard Postgres wire protocol.
- **Tool:** React Grab — click any element in a running app's UI and hand its context straight to Cursor/Claude Code for editing, instead of describing it in words. [github.com/aidenybai/react-grab](https://github.com/aidenybai/react-grab)
