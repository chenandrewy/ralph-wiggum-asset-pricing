Title: VS Code Git Relative Worktrees Fix
Date: 2026-04-08
Time: 19:18:58 EDT

VS Code Source Control showed `Initialize Repository` inside an existing repository and failed repeated `git rev-parse --show-toplevel` calls with:

`fatal: unknown repository extension found: relativeworktrees`

Root cause:
- VS Code was using `/usr/bin/git`, which reported `2.39.5 (Apple Git-154)`.
- The repository uses `[extensions] relativeWorktrees = true` and `[worktree] useRelativePaths = true` in `.git/config`.
- The shell and Codex environment were using `/opt/homebrew/bin/git`, which reported `2.49.0`.
- The older Apple Git could not parse the repository extension, so VS Code treated the folder as if no repository existed.

Fix:
- Added workspace setting `.vscode/settings.json` with `"git.path": "/opt/homebrew/bin/git"`.
- Added the same setting to VS Code user settings at `~/Library/Application Support/Code/User/settings.json`.
- After restarting VS Code, Source Control recognized the repository correctly.

Takeaway:
- If VS Code claims a repository with relative worktrees is uninitialized, first check which Git binary VS Code is using in the Git output panel.
