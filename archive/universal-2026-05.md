# Universal — archive (2026-05)

### 2026-05-27 — Sloth Bytes
- **Lesson:** Always commit the lockfile — it records the exact version, resolved URL, and a SHA-512 integrity hash per package, so a later install fails loudly if a package's published contents were tampered with after the lockfile was created.
- **Lesson:** The 2016 left-pad incident: an author unpublished an 11-line npm package and broke builds at Facebook, Netflix, and Spotify overnight — every dependency is maintained by a human who can vanish or get compromised; npm's current unpublish policy exists because of this.

### 2026-05-13 — Sloth Bytes
- **Lesson:** Five ways to improve as a developer without writing more code: read real production codebases for decisions that surprise you; read company engineering blogs for how real teams handled tradeoffs tutorials never show; review others' code / merged OSS PR threads to see senior reasoning; actually read docs and CS books to build vocabulary; explain your reasoning out loud — increasingly valuable as agents do more of the actual typing.

### 2026-05-07 — Sloth Bytes
- **Lesson:** CVE-2026-31431 ("copy.fail") — a 732-byte script chaining a Linux kernel crypto-layer bug gets root on essentially every Linux distro shipped since 2017, escapes containers, and isn't caught by file-integrity checkers since it writes to memory not disk. A patch is available — update Linux servers/containers now if you haven't.
- **Tool:** GitHub alternatives worth knowing given recent reliability incidents: GitLab, Codeberg, Sourcehut — worth having a backup plan rather than treating GitHub as risk-free.
- **Lesson:** Claude/Claude Code rate limits were substantially raised (5-hour limits doubled for Pro/Max/Team, peak-hour throttling removed) after an Anthropic compute partnership.
