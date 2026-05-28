# Backup Hermes Agent

## Background

- Backup before it crashes
- Migrate to a new installation
- Rollback for whatever reason

## Step 1: Back Up Your Current Hermes Data

Hermes spreads its core memory, persona, and configurations across the `~/.hermes/` directory.

Native Backup Command: If your installation supports it, you can create a complete, timestamped archive with the built-in backup CLI

```bash
hermes backup --now
```

Manual/ Scripted Backup: If you need to bundle it manually, back up these critical components: 

- `~/.hermes/SOUL.md`: Your agent’s core persona and identity constraints.
- `~/.hermes/memories/MEMORY.md` & `~/.hermes/memories/USER.md`: The persistent long-term knowledge base.
- `~/.hermes/skills/`: Your custom skills and auto-learned capabilities.
- `~/.env`: Your sensitive API keys and bot tokens.

    Note: For the SQLite session database (state.db), always use SQLite's online backup API rather than a direct file copy to ensure database consistency.