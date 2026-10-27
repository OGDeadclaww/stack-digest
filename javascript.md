# JS / Frontend
_read only if the project is JS/TS or frontend_

> Entries older than 60 days live in `archive/javascript-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).

### 2026-10-23 — The Code
- **Tool:** Reylo (Colin McDonnell, Zod creator) — import .sql files straight into TypeScript with full type inference, no ORM or codegen; checks queries against the real database schema, catches bad columns/parameters in the editor, and keeps agents from leaving stale types. Runs on TypeScript 7.1 content mappers (still beta). [github.com/colinhacks/reylo](https://github.com/colinhacks/reylo)


### 2026-10-22 — The Code
- **Lesson:** Node.js security release: three release lines were patched this week — find your line and upgrade. [nodejs.org](https://nodejs.org)


### 2026-10-20 — The Code
- **Tool:** Pele (kepano) — tiny open-source, zero-dependency alternative to Mermaid.js for rendering diagrams in your app: feed it Mermaid syntax and get themeable SVG, with a much smaller bundle and claimed render speeds up to 500x faster. [pele.run](https://pele.run/)


### 2026-10-19 — The Code
- **Tool:** Handwired (1.8k★) — converts normal JavaScript (if-else logic, loops) into matrix math, i.e. a neural net with the same output without training; use it to experiment with training parts of regular programs, mix hand-written logic with neural nets, or get GPU-style parallelism. [details](https://archive.codenewsletter.ai/2110557373651931267)


### 2026-10-15 — The Code
- **Tool:** Eve (Vercel, open source) — agent framework structured around prompts, tools, skills, and channels (web, Slack, etc.), deployable to Vercel; the tutorial builds a research agent from setup to deployment. [tutorial](https://www.youtube.com/watch?v=MObkrCUCrJw)


### 2026-10-06 — The Code
- **Tool:** Gdp-ts (Vercel) — TypeScript library that catches authorization mistakes at compile time: a sensitive function won't run unless the caller can prove the user has permission, with an agent skill included for applying the pattern across your codebase. [github.com/rauchg/gdp-ts](https://github.com/rauchg/gdp-ts)


### 2026-10-01 — Sloth Bytes
- **Tool:** Vite+ 1.0 — one CLI and one config (`vite.config.ts`) replacing vite, vitest, eslint, prettier, tsup, and turbo; the same commands (`vp dev`, `vp test`, `vp build`, `vp check`) work across React, Vue, Node CLIs, and monorepos, with a cached monorepo task runner. Built in Rust — up to 50-100x faster linting than ESLint and up to 30x faster formatting than Prettier. Free and MIT licensed. [voidzero.dev](https://voidzero.dev/posts/announcing-vite-plus-1-0)

### 2026-09-24 — Sloth Bytes
- **Tool:** Chrome 154 ships responsive iframes — an iframe can now size itself to fit its content: add `frame-sizing: content-height;` to the iframe's CSS on the parent page, opt in from the embedded page, and call `window.requestResize()` if content changes later — no more double scrollbars or manual `postMessage()` size measuring. Not supported in other browsers yet, so keep a fallback. [developer.chrome.com](https://developer.chrome.com/blog/responsive-iframes)
- **Lesson:** "Blurry Before Beautiful" — a proposed built-in HTML attribute that shows a blurry preview of an image while it loads, no JavaScript library required; worth watching as a future zero-JS alternative to current placeholder techniques. [patrickbrosset.com](https://patrickbrosset.com/articles/2026-09-22-blurry-before-beautiful-image-previews-for-the-web/)
- **Tool:** Remotion — make videos with React code. [github.com/remotion-dev/remotion](https://github.com/remotion-dev/remotion)


### 2026-09-21 — The Code
- **Tool:** Emil Kowalski's animation skill pack for Claude Code (12 skills) fixes the easing/timing/motion Claude Code usually gets wrong on its own: install with `npx skills@latest add emilkowalski/skills`, then `/prototype` a component and `/animate` it for proper easing/timing, iterate in plain English, and run `/prep-for-prod` to check performance/accessibility/mobile before shipping. [github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)


### 2026-09-18 — Sloth Bytes
- **Tool:** Google's modern web guidance skills — a set of Claude/agent-ready skills covering modern web-development best practices (UX, performance) straight from the Chrome team. [developer.chrome.com](https://developer.chrome.com/docs/modern-web-guidance)
- **Tool:** neat-annotations — hand-drawn-style CSS arrows and notes for docs/screenshots that need fun callouts, zero JS, one stylesheet. [neat-annotations.syabro.com](https://neat-annotations.syabro.com/)
- **Tool:** pdfcn — customizable PDF-viewing/rendering components for React. [pdfcn.dev](https://www.pdfcn.dev/)

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

