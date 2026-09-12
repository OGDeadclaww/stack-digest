# JS / Frontend
_read only if the project is JS/TS or frontend_

> Entries older than 60 days live in `archive/javascript-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).

### 2026-09-11 — Sloth Bytes
- **Tool:** React 19.3 — View Transitions graduated to stable; also ships Fragment Refs (refs on fragments via a new FragmentInstance object), a `browser` API to mark a component browser-only during server rendering, Trusted Types support (blocks DOM-based XSS), and `<title>` now renderable directly in Server Components. [react.dev/blog](https://react.dev/blog/2026/09/09/react-19-3)
- **Tool:** Expo Modules 2.0 — replaces the old result-builder DSL for native modules with a plain `@ExpoModule` class and `@JS`-annotated methods/properties; sync/async follows Swift's own `async` keyword, 1.0/2.0 coexist so you migrate one function at a time, and the `@JS` path benchmarks 2.5–5.6x faster than 1.0 for sync calls. Live on iOS SDK 57 (experimental)/58 (beta); Android still in progress. [expo.dev/blog](https://expo.dev/blog/an-early-look-at-expo-modules-2-0)
- **Tool:** drawably — hand-drawn-style UI component library with zero dependencies. [drawably.dev](https://www.drawably.dev/)
- **Tool:** Extend UI — React components for viewing PDF, DOCX, XLSX, and CSV files inside your app. [extend.ai/ui](https://www.extend.ai/ui)

### 2026-09-09 — The Code
- **Lesson:** Three ways to build agent-generated UIs (CopilotKit's Tyler Slaton): let agents create dynamic frontends, handle user input, and power interactive workflows like incident-triage apps, instead of only returning text. [tutorial](https://www.youtube.com/watch?v=mGyyTVk8Ggw)


### 2026-09-04 — Sloth Bytes
- **Lesson:** Chrome removed all remaining Manifest V2 extensions from the Web Store (uBlock Origin included) — already-installed copies on Chrome 138 or earlier keep working with no updates and can't be reinstalled. Alternatives: uBO Lite, Brave (which self-hosts uBlock Origin/AdGuard/uMatrix/NoScript), or Firefox. [developer.chrome.com](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline)
- **Tool:** htmx 4.0 — switched internally from XMLHttpRequest to `fetch()`. Breaking for you: attribute inheritance (e.g. `hx-confirm`) is now opt-in via `:inherited`; events renamed (`htmx:beforeRequest` → `htmx:before:request`); history no longer uses localStorage, so the back button re-fetches instead of restoring a stale DOM. npm `latest` stays on 2.x until early 2027; run `npx htmx.org@4.0.0 upgrade-check` before pinning 4.0.0. [four.htmx.org](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)
- **Tool:** Vitest 5.0 — mainly a performance release (biggest wins on vm pools, Browser Mode, monorepos) but with quiet breaking changes: requires Vite ≥6.4.0 and Node ≥22.12.0, `clearMocks` is now on by default, and an unawaited `expect(promise).resolves` now fails instead of just warning. New `vitest doctor` command suggests config changes that would speed up your suite. Read the migration guide before `npm i vitest@5`. [vitest.dev/blog](https://vitest.dev/blog/vitest-5.html)
- **Lesson:** ESLint's autofix can combine two individually-valid fixes into broken code because it batches edits instead of re-analyzing between them (unlike elm-review, which applies one fix and re-checks) — worth knowing before trusting `--fix` on a large batch unreviewed. [jfmengels.net](https://jfmengels.net/concurrent-linter-fixes/)
- **Tool:** Svelte Bits — copy-paste animated Svelte 5 components (text, backgrounds, UI), a port of React Bits; Tailwind + TypeScript. [github.com/DavidHDev/svelte-bits](https://github.com/DavidHDev/svelte-bits)
- **Tool:** Typebase — a type-safe backend written as TypeScript files inside your existing app (oRPC, Drizzle, better-auth), MIT-licensed. [github.com/typebase-io/monorepo](https://github.com/typebase-io/monorepo)
- **Tool:** Schedule-X — a FullCalendar-shaped event calendar for React, Vue, Angular, Svelte and Preact, with drag, resize, and dark mode; MIT core. [github.com/schedule-x/schedule-x](https://github.com/schedule-x/schedule-x)
- **Tool:** Cropper.js — drop-in image cropper with a live playground. [github.com/fengyuanchen/cropperjs](https://github.com/fengyuanchen/cropperjs)
- **Tool:** Rslint — ESLint-compatible JS/TS linter built for speed, ships TypeScript-ESLint rules out of the box (experimental). [rslint.rs/guide](https://rslint.rs/guide/)

### 2026-08-27 — Sloth Bytes
- **Tool:** MicroLighter — ~2KB syntax highlighter using CSS Custom Highlights instead of wrapping every token in a span. [daverupert.com](https://daverupert.com/2026/08/microlighter/)
- **Tool:** Formisch 1.0 — framework-agnostic, schema-based form library with type safety. [formisch.dev/blog](https://formisch.dev/blog/formisch-v1/)

### 2026-08-24 — The Code
- **Tool:** Is Agentic — free site scanner scoring how easily AI agents can navigate/use a website (100+ checks), gives one-click fixes + a CLI. Works for any HTML site incl. server-rendered/Jinja2 output. [is-agentic.com](https://is-agentic.com/)
- **Tool:** anti-slop — plugin that catches low-signal TypeScript/JavaScript patterns before they land in your codebase; vendor the rules into your repo and customize. [github.com/dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop)

### 2026-08-20 — Sloth Bytes
- **Tool:** Oxlint + React Compiler support — 22 new React Compiler lint rules plus a transform ~10x faster than Babel; catches Rules-of-React violations at lint time. [oxc.rs/blog](https://oxc.rs/blog/2026-08-18-react-compiler-support.html)
- **Tool:** Playwright "soak test" pattern for catching SPA memory leaks (listener/timer leaks) before they ship. [denodell.com/blog](https://denodell.com/blog/your-spa-is-leaking-memory-soak-test-it)

### 2026-07-30 — Sloth Bytes
- **Tool:** React Doctor — one `npx` command scans a React codebase and returns a health score out of 100, specifically built to catch sloppy patterns AI coding agents leave behind. [react.doctor](https://www.react.doctor/)
