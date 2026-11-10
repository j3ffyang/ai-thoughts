# Ten Tools Over a Pipe: OpenCode on a Remote ⚕ Hermes Agent

*2026-11-09*

**Thesis:** `hermes mcp-serve` turns the agent into an MCP server that speaks over stdin and stdout. Point OpenCode at it through SSH and your editor becomes a client of your messaging bot — ten tools by default, seventeen with one flag, and no terminal in either list.

**Status:** verified end to end. OpenCode v2.2.5 against a Debian VPS: the handshake, both tool lists, the SSH transport, and `opencode mcp list` reporting `✓ hermes connected`.

## The shape of it

```
┌──────────────────────────────────────────────────────┐
│ OpenCode (laptop)                                    │
│   │  ssh -T <vps> · stdio JSON-RPC                   │
│   ▼                                                  │
│ hermes mcp-serve (VPS)                               │
│   ├─ state.db    read every message                  │
│   ├─ adapters    send as you                         │
│   └─ --tools     web · vision · image · skills · TTS │
│   ✗  terminal · file · kanban — never exposed        │
└──────────────────────────────────────────────────────┘
```

One process spawns a command, the command is an SSH session, and the SSH session runs a stdio server. Nothing listens on a port, so there is no endpoint to expose and no token to leak — the SSH key is the authentication.

## What the command is

```
usage: hermes mcp-serve [-h] [-v] [--tools] [--accept-hooks]
```

The help text names its own client config: `{"command": "hermes", "args": ["mcp-serve"]}`. That is the whole protocol — a command that reads JSON-RPC on stdin and writes it on stdout. No port, no listener, no token.

`--tools` adds "web, browser, vision, image generation, skills and TTS tools" and states the limit plainly: **never terminal, file or kanban**.

## What it announces

One `initialize` line in, one object out:

```json
{"jsonrpc":"2.0","id":1,"result":{
  "protocolVersion":"2024-11-05",
  "serverInfo":{"name":"hermes","version":""},
  "capabilities":{"prompts":{},"resources":{},"tools":{}},
  "instructions":"Hermes Agent messaging bridge. Use these tools to interact with
   conversations across Telegram, Discord, Slack, WhatsApp, Signal, Matrix, and
   other connected platforms."
}}
```

Calling itself a *messaging bridge* is accurate. What it is not is a shell.

## The ten tools

| Group | Tools | What it does |
|---|---|---|
| Read | `conversations_list`, `conversation_get`, `messages_read`, `attachments_fetch`, `channels_list` | walk your history, open a conversation, pull attachments |
| Watch | `events_poll`, `events_wait` | ask for new events, or block until one arrives |
| Write | `messages_send` | post as your connected accounts |
| Approvals | `permissions_list_open`, `permissions_respond` | see and answer Hermes' pending approvals |

Seven more with `--tools`: `web_search`, `web_extract`, `vision_analyze`, `image_generate`, `skill_view`, `skills_list`, `text_to_speech`.

Two things in that list are worth reading twice.

**Skills are read-only.** `--tools` exposes `skill_view` and `skills_list`, not `skill_manage`. An editor can read the library and cannot write to it — the same separation the write gate enforces on Discord.

**There is no browser tool**, despite the help text naming one. The flag description says "web, browser, vision, image generation, skills and TTS"; the actual list has web search and extract, with no `browser_exec`. Either the help string lags the code or the browser toolset is gated behind something else in this profile. Do not plan around it.

## Wiring OpenCode

OpenCode v2 nests servers under `mcp.servers`. The CLI writes the file for you:

```bash
opencode mcp add --global hermes -- ssh -T <vps> /home/jeff/.local/bin/hermes mcp-serve
```

Which produces:

```json
{
  "mcp": {
    "servers": {
      "hermes": {
        "type": "local",
        "command": ["ssh", "-T", "<vps>", "/home/jeff/.local/bin/hermes", "mcp-serve"]
      }
    }
  }
}
```

Then:

```
$ opencode mcp list
✓ hermes  connected
```

Without `--global` the CLI writes a project `opencode.json` instead, and the check above still answers *No MCP servers configured* — this command reads the global config, so a project file looks ignored when it is only out of scope.

Add `--tools` after `mcp-serve` if you want the seven extras.

## Using it

Prompts go to the model in OpenCode; the model chooses the tools. What decides whether it works is naming the place.

| Ask | Reaches for |
|---|---|
| "Summarise `#hermes` today and name three open questions" | `conversations_list` → `messages_read` |
| "Post in `#hermes`: down 14:00–14:10 UTC" | `messages_read` → `messages_send` |
| "Wait for the next message in `#hermes` and quote it" | `events_wait` — blocks until one arrives |
| "Anything new since the last turn?" | `events_poll` — returns immediately |
| "List pending approvals; deny anything destructive and quote it first" | `permissions_list_open` → `permissions_respond` |
| "Read my `simplified-to-traditional` skill, then apply it" | `skills_list` → `skill_view`, with `--tools` |
| "Generate a 16:9 banner for this title and post it" | `image_generate` → `messages_send`, with `--tools`; spends credits |

Two habits make it reliable. **Name the platform and the channel** — the server sees Telegram, Discord, Slack and DMs at once, so "the conversation" is ambiguous and "the Discord `#hermes` channel" is not. **Read before you write** — ask for the last twenty messages before asking for a draft, so you can check the context the model is about to reply into.

What will not work, in either mode: "run `df -h`", "write a new skill", "edit the config". No terminal, no `skill_manage`, no file tool. That is the design, not a gap.

## Two footguns, both measured

**PATH.** `ssh <vps> hermes mcp-serve` fails:

```
bash: line 1: hermes: command not found
```

Non-interactive SSH runs a non-login shell, so `~/.local/bin` is not on `PATH`. Two fixes, both verified: the absolute path, or `bash -lc "hermes mcp-serve"`. The absolute path is more robust, because it avoids a second layer of quoting.

**Scope.** A project-level `opencode.json` is not what `opencode mcp list` reads. Hand-written `.jsonc` or `.json`, inside a git repo or with `--standalone`, all four answer *No MCP servers configured*; the same server added with `--global` shows `✓ hermes connected`. The file name is not the variable — the scope is. Whether a *session* started in that directory picks the project file up is a different question, and one this check cannot see.

## What you have handed the editor

The bridge is not read-only, and the plugin says so:

- it reads `~/.hermes/state.db` — every DM and channel message in the active profile;
- it can send as your connected accounts;
- it can answer pending approval prompts;
- with `--tools`, it runs tools under your provider credentials and can spend credits;
- with `--accept-hooks` plus `--tools`, it runs the shell hooks in `config.yaml` without the first-use consent check.

That last flag is the one to leave alone. Everything else is a scope decision: a personal laptop talking to your own bot is one thing, a shared workstation is another.

## When not to

- **Not with `--tools` on a metered account** you share with anything else.
- **Not on a machine you do not control** — the client is the security boundary here, not the server.
- **Not as a substitute for the gateway's own approvals.** `permissions_respond` lets the editor answer prompts that were raised somewhere else; that is a convenience, and it moves the decision off the surface where it was asked.

## What I ran

```bash
# one JSON-RPC message per line: initialize, initialized, tools/list
INIT='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"0"}}}'
printf '%s\n' "$INIT" '{"jsonrpc":"2.0","method":"notifications/initialized"}' '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
  | timeout 20 hermes mcp-serve | jq -r 'select(.id==2) | .result.tools[].name'
printf '%s\n' "$INIT" | timeout 25 ssh -T <vps> /home/jeff/.local/bin/hermes mcp-serve
opencode mcp add --global hermes -- ssh -T <vps> /home/jeff/.local/bin/hermes mcp-serve
opencode mcp list
```

The first two produce the tool lists above. The third and fourth confirm the transport, not just the server.

btw, i use arch
