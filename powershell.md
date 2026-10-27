# PowerShell / Windows
_read only if the project targets Windows/PowerShell_

> Entries older than 60 days live in `archive/powershell-YYYY-MM.md`. Coding agents should read only this file (plus `universal.md` if this is not already Universal).


### 2026-10-01 — Sloth Bytes
- **Tool:** WSL containers (GA) — run Linux containers on Windows without a separate container engine: `wsl --update`, then Docker-style commands (`wslc run`, `wslc build`, `wslc container list`); up to 2x faster when Linux reads your Windows files; works as the driver for VS Code dev containers; a `Microsoft.WSL.Containers` NuGet package lets Windows apps spin up Linux containers themselves. No Compose support yet, so it's not a Docker Desktop replacement. [blogs.windows.com](https://blogs.windows.com/windowsdeveloper/2026/09/29/wsl-containers-now-generally-available/)

