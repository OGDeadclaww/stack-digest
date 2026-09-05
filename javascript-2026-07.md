# JS / Frontend — archive (2026-07)

### 2026-07-03 — Sloth Bytes
- **Tool:** TypeScript 7.0 RC — compiler rewritten in Go, ~10x faster type-checking. Install `npm install -D typescript@rc`; run old+new side by side with the `@typescript/typescript6` compat package. Legacy configs like `target: es5` are now hard errors — audit tsconfig before upgrading. [devblogs.microsoft.com](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0-rc/)
- **Tool:** Vercel AI SDK 7 — WorkflowAgent runs each tool call as a durable step that survives crashes and auto-retries; a tool-approval system lets an agent propose an action for human confirmation; typed tool context scopes API keys per tool. Migrate with `npx @ai-sdk/codemod v7`.
