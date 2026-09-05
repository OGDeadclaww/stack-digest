# Universal — archive (2026-07)

### 2026-07-03 — Sloth Bytes
- **Lesson:** Claude Sonnet 5 specifics: model ID `claude-sonnet-5`, 1M-token context window by default now, manual extended-thinking param removed (adaptive thinking runs automatically — passing it throws a 400), and the same text costs ~30% more tokens than on Sonnet 4.6 — recheck hardcoded `max_tokens` limits so outputs don't get silently clipped.
