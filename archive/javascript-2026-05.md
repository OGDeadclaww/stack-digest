# JS / Frontend — archive (2026-05)

### 2026-05-27 — Sloth Bytes
- **Lesson:** npm semver symbols: `^5.2.1` allows minor+patch updates, `~5.2.1` allows patch only, no symbol pins the exact version, `*` always installs latest (avoid). Use `npm install <pkg>@<version> --save-exact` to pin precisely.
- **Lesson:** Supply-chain hygiene checklist: use `npm ci` (not `install`) in CI — deletes node_modules first, installs exactly what the lockfile says, fails hard on mismatch; add `--ignore-scripts` in automated environments; run `npm audit` but remember it only catches known vulnerabilities; consider Socket.dev to flag malicious packages before install.
