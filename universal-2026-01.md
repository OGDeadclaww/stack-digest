# Universal — archive (2026-01)

### 2026-01-31 — Sloth Bytes
- **Lesson:** curl shut down its 7-year, $100k bug bounty program after a flood of AI-generated ("slop") reports crashed the confirmation rate from 15% to under 5% — plan for this if you run or rely on a bug bounty program.
- **Lesson:** Anthropic's own research: junior engineers who just had AI complete tasks scored 17% lower on a follow-up concept quiz than those who used AI to ask follow-up questions and build understanding while coding. When learning a new library, ask the AI to explain as you go instead of just finishing the task.
- **Lesson:** DHH argues AI-generated code quality is often worse than a junior's and inconsistent; his company still has humans write 95% of the code on their latest product — agent output still needs the same or more scrutiny as a junior's PR.
- **Lesson:** Google Gemini 3 "Agentic Vision" pattern worth borrowing for any vision task needing precision: instead of one static look, have the model write code to crop/zoom/annotate the image, then re-examine (a Think-Act-Observe loop) — reported 5–10% accuracy boost over a single pass.

### 2026-01-08 — Sloth Bytes
- **Lesson:** Five production-readiness features tutorials skip, roughly by value-for-effort: analytics (Plausible/PostHog/Mixpanel), error tracking (Sentry/Rollbar), uptime monitoring (UptimeRobot/Pingdom), rate limiting/DDoS protection (Cloudflare/Upstash — one unprotected static site ate a $104,500 bandwidth bill from a single-day DDoS), and automated testing (Stripe runs 1.4M automated tests per change). Analytics + error tracking + rate limiting cover most of the value if you only add three.
