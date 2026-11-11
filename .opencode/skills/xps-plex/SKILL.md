---
name: xps-plex
description: >
  Project a web page fullscreen onto the second laptop (ssh host `xps`) over
  SSH: start the v2rayN proxy if it is down, launch Firefox or Brave on a
  dedicated proxy profile, park the proxy GUI on its own workspace, fullscreen
  the page. Use when the user asks to put a page, a stream, or Plex live TV on
  the other machine's screen, asks whether that machine's proxy is up, or asks
  what is open on it.
---

# xps-plex — project a page onto the other laptop

One script, three subcommands, no server. The logic runs as a bash block on the remote host over `ssh`; this skill is the part that tells you when to run it and what the output means.

The MCP server version of the same job lives at `ai-thoughts/.opencode/mcp/xps-plex/`. They are interchangeable; this one needs no client registration and no restart.

## Commands

Run from anywhere; the script is beside this file.

```sh
scripts/xps-plex.sh status
scripts/xps-plex.sh start-proxy
scripts/xps-plex.sh open [--browser firefox|brave] [--windowed]
```

| Command | Does | Use when |
|---|---|---|
| `status` | proxy state, v2rayN/Firefox/Brave process counts, window titles | before reporting to the user, or to check whether something is already open |
| `start-proxy` | starts v2rayN if the port is down, parks its window | the user asks to prepare the proxy without opening a page |
| `open` | ensures the proxy, reuses or starts the browser, fullscreens the page | the actual request: "put it on the other screen" |

`open` defaults to Firefox and fullscreen. `--windowed` skips the fullscreen step. Both arguments are optional, so the ordinary call is bare `open`.

## Output

One `key: value` line per fact:

```
proxy window: workspace 2
action: reuse
window: Live TV Guide - Plex — Mozilla Firefox
proxy: already listening
fullscreen: mode 2
```

| Key | Values | Meaning |
|---|---|---|
| `action` | `reuse` / `start` / `clean` / `restart` | `reuse` means nothing was touched; the rest launched one browser |
| `window` | window titles, ` ; ` separated | what is actually on screen |
| `fullscreen` | `mode 2` / `mode 1` / `mode 0` | **2 is fullscreen**, 1 is maximize, 0 is neither |
| `proxy` | `already listening` / `was down, v2rayN started` / `v2rayN not found…` / `…never opened` | the last two are honest failures, not errors |
| `proxy window` | `workspace <n>` | where the proxy GUI was parked |
| `warning` | `no page window` | nothing but a dialog or blank tab appeared |

## The four faults this script exists to dodge

These are why it is not a one-line `ssh firefox https://…`. Each one looks like the fault before it when it breaks.

1. **The name resolves to a Facebook address.** `watch.plex.tv` is answered with `157.240.20.18` on this network, so a direct connection loads nothing. Only the proxy path works, and the proxy becomes a prerequisite, not a detail.
2. **Firefox has no `--proxy-server`.** Brave takes it on the command line; Firefox needs it written into a profile. The script writes `~/.mozilla/firefox/plex-proxy/user.js` on every call, which keeps the proxy scoped to one profile and the configuration idempotent. Neither browser can be retrofitted, so a browser on another profile is restarted.
3. **Fullscreen is a compositor dispatch, not a flag.** `--start-fullscreen` is ignored, especially when the launch is forwarded to a running instance. Hyprland 0.56+ takes Lua dispatchers, and `1` means maximize — mode **2** is real fullscreen. The window is focused by address first, because the site sometimes opens a sign-in window that would otherwise take the fullscreen.
4. **v2rayN is X11-only.** Its Avalonia build needs `DISPLAY`, which an SSH session does not have and Hyprland does not export; the `:0` fallback hits a different X server and fails authorization. XWayland's real number is read from its command line each time.

## Rules

- **Never pass a command through.** The script only starts the proxy, launches a page, fullscreens it, or reports. If the user wants something else on that host, say so rather than extending this call.
- **Do not kill the browser yourself.** `open` reuses one good window and clears the rest; a manual `pkill` is what leaves the crash-restore dialog behind.
- **`action: reuse` is the good case.** It means the page was already up and nothing was disturbed — report that rather than implying a fresh launch.
- **A missing proxy is not a failure.** The page still opens without it; say so and do not retry.
- **One window is the target state.** If `window` lists more than one title, something drifted — the next `open` clears it, so run it rather than explaining the mess.

## Configuration

Every machine-specific value is an environment variable with a working default:

| Variable | Default | Changes |
|---|---|---|
| `XPS_SSH_HOST` | `xps` | ssh destination (an alias, not an address) |
| `XPS_URL` | `https://watch.plex.tv/live-tv` | the page opened |
| `XPS_PROXY_URL` | `http://127.0.0.1:10808` | proxy handed to Brave |
| `XPS_PROXY_ADDR` | `127.0.0.1:10808` | address the readiness check polls |
| `XPS_V2RAY_DIR` | `$HOME/pool/Downloads/rog_drive/v2rayN-linux-64` | proxy binary location |
| `XPS_PROXY_WORKSPACE` | `2` | workspace the proxy GUI parks on |

## Verify

```sh
scripts/xps-plex.sh status     # proxy listening, one firefox, one window
scripts/xps-plex.sh open       # action: reuse, fullscreen: mode 2
```

If `status` answers `ssh to xps failed`, the key or the host alias is wrong — that is a setup fault, not a projection fault. Do not try to fix it from inside this skill.

The reasoning behind every branch, and the measurements that found each fault, are in [Projecting a Tab Onto Another Machine](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261110-projecting-a-tab-onto-another-machine.md) and [A Skill or an MCP Server?](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261111-skill-vs-mcp.md).
