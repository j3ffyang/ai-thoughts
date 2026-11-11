# xps-plex MCP

A local [Model Context Protocol](https://modelcontextprotocol.io) server that opens a web page on a second machine over SSH, starts the proxy it needs, and fullscreens the window on that machine's compositor.

It was written to project Plex live TV from a handheld onto a laptop across the LAN, and the parts are general enough to open any page on any Wayland host reachable over SSH.

## What it does

Three tools, all narrow by design. None of them accepts a command to run remotely.

| Tool | Does |
|---|---|
| `open_page(browser="firefox", fullscreen=True)` | ensures the proxy, launches the browser on the configured URL, fullscreens the window |
| `xps_start_proxy()` | starts the v2rayN proxy if its port is not already listening |
| `xps_status()` | reports the proxy, the browser process counts, and the window titles |

## Requirements

Locally: `uv`, `ssh`, and a working key for the remote host.

On the remote host:

| Need | Why |
|---|---|
| `Hyprland` + `hyprctl` + `jq` | fullscreen and window discovery |
| `firefox` and/or `brave` | the browser |
| `iproute2` (`ss`) | proxy port check |
| `v2rayN` | optional. Started when the proxy port is down; if absent the browser still launches |

## Configuration

Everything machine-specific comes from the environment, so the committed file stays portable. Defaults are in `server.py`.

| Variable | Default | Meaning |
|---|---|---|
| `XPS_SSH_HOST` | `xps` | ssh destination, normally an alias from `~/.ssh/config` |
| `XPS_URL` | `https://watch.plex.tv/live-tv` | page to open |
| `XPS_PROXY_ADDR` | `127.0.0.1:10808` | where `ss` looks for the proxy |
| `XPS_PROXY_URL` | `http://127.0.0.1:10808` | what Brave is given as `--proxy-server` |
| `XPS_V2RAY_DIR` | `$HOME/pool/Downloads/rog_drive/v2rayN-linux-64` | directory holding the `v2rayN` binary |

The host is an SSH alias on purpose: the remote address is usually a DHCP lease, and an alias keeps that fact in `~/.ssh/config` where it belongs, instead of in the server.

```
Host xps
    HostName 10.0.0.42
    User you
    IdentityFile ~/.ssh/your_key
```

## Registering it

In `opencode.jsonc`:

```jsonc
"mcp": {
  "xps-plex": {
    "type": "local",
    "command": [
      "uv", "run", "--with", "mcp",
      "/path/to/xps-plex/server.py"
    ],
    "enabled": true
  }
}
```

`uv run --with mcp` keeps the SDK out of the system Python; nothing is installed globally. MCP servers load at startup, so restart the client after editing the config.

Override any variable with an `environment` block:

```jsonc
"environment": {
  "XPS_SSH_HOST": "xps",
  "XPS_V2RAY_DIR": "/opt/v2rayN-linux-64"
}
```

## How it works, and why each piece is there

**The proxy is not optional on a censored network.** On the network this was built for, `watch.plex.tv` resolves to `157.240.20.18`, a Facebook address. Direct connections hang or reach nothing. Only the proxy path works, so a browser without it renders an error page rather than the site.

**The two browsers take the proxy differently.** Brave accepts `--proxy-server` on the command line. Firefox has no such flag: the proxy lives in the profile's `prefs`, so the server writes a dedicated profile's `user.js` on every call. The profile is what makes the setting stick, and it is also where the site login persists.

**Neither can be retrofitted.** A browser already running without the proxy ignores the flag — a second invocation only forwards the URL to the running process. The server therefore restarts a browser that lacks the setting, and opens a new window in one that has it.

**Fullscreen needs the compositor.** `--start-fullscreen` is ignored when the launch is forwarded, and under a tiling compositor it often does not apply even on a fresh start. Hyprland 0.56 and later take Lua dispatchers (`hl.dsp.*`); the server focuses the target window by address and calls `hl.dsp.window.fullscreen()`. Mode 2 is fullscreen; mode 1 is only maximize.

**v2rayN needs an X display.** The Avalonia build has an X11 backend only, so it fails with `XOpenDisplay failed` unless `DISPLAY` is set. An SSH session has no display, Hyprland does not export one, and XWayland's number changes across boots, so the server reads it from the Xwayland command line. It also starts the binary from its own directory, because `bin/` and `guiConfigs/` are resolved relative to it.

## Troubleshooting

| Symptom | Cause |
|---|---|
| `XOpenDisplay failed` | no `DISPLAY`; v2rayN is X11-only |
| `Authorization required, but no authorization protocol specified` | `DISPLAY` points at the wrong X server |
| Browser opens an error page | proxy down and no v2rayN binary found |
| Window is tiled, not fullscreen | dispatched `fullscreen` mode 1 instead of 2 |
| `pkill -f brave` kills your SSH session | the pattern matches the shell's own command line; match exact process names instead |
| Two windows appear | the site opens its own popup, usually a sign-in step |

## Security notes

The server holds no credentials. The site login happens in the browser, on the remote machine, and stays in that browser profile.

It exposes no generic remote-execution tool. The host, the URL and the browser are fixed by configuration, and the only commands run remotely are the ones implementing these three tools.
