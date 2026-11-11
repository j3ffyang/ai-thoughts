#!/usr/bin/env python3
"""MCP server: open a web page on a remote Wayland host over SSH.

Built for one job — projecting Plex live TV onto a second machine — but the
moving parts are general. It starts a v2rayN proxy if the port is down, launches
a browser with that proxy, and fullscreens the window through the compositor.

Why each piece exists:

* **The proxy.** `watch.plex.tv` is unreachable on the target network without
  it: the resolver answers with 157.240.20.18, a Facebook address. Both browsers
  need the proxy, but differently — Brave takes `--proxy-server`, Firefox has no
  such flag and needs it in a profile's prefs.
* **The restart rule.** Neither browser can be retrofitted with a proxy once
  running, so a browser started without it is restarted.
* **The compositor.** `--start-fullscreen` is ignored when the launch is
  forwarded to a running instance, so fullscreen is applied through Hyprland.
  Hyprland 0.56+ takes Lua dispatchers (`hl.dsp.*`); fullscreen mode 2 is real
  fullscreen and mode 1 is maximize.
* **The display.** v2rayN is an Avalonia build with an X11 backend only, so it
  needs DISPLAY. An SSH session has none, Hyprland does not export it, and
  XWayland's number is not stable — it is read from the Xwayland command line.

Configuration is by environment variable, so nothing machine-specific is
committed. See README.md.

Run with: uv run --with mcp server.py
"""

from __future__ import annotations

import os
import subprocess

from mcp.server.mcpserver import MCPServer

HOST = os.environ.get("XPS_SSH_HOST", "xps")
URL = os.environ.get("XPS_URL", "https://watch.plex.tv/live-tv")
PROXY = os.environ.get("XPS_PROXY_URL", "http://127.0.0.1:10808")
PROXY_ADDR = os.environ.get("XPS_PROXY_ADDR", "127.0.0.1:10808")
V2RAY_DIR = os.environ.get("XPS_V2RAY_DIR", "$HOME/pool/Downloads/rog_drive/v2rayN-linux-64")
# Where the proxy GUI parks so the browser gets a workspace to itself.
PROXY_WORKSPACE = os.environ.get("XPS_PROXY_WORKSPACE", "2")

SSH_TIMEOUT = 25
LAUNCH_TIMEOUT = 150

mcp = MCPServer("xps-plex")


def _fill(template: str) -> str:
    """Substitute the placeholders. Plain replacement, so bash stays readable."""
    return (
        template.replace("@PROXY_ADDR@", PROXY_ADDR)
        .replace("@V2RAY_DIR@", V2RAY_DIR)
        .replace("@URL@", URL)
        .replace("@PROXY@", PROXY)
        .replace("@PROXY_WS@", PROXY_WORKSPACE)
    )


def _ssh(script: str, timeout: int = SSH_TIMEOUT) -> str:
    """Run a bash script on the remote host over SSH and return its stdout."""
    try:
        proc = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", HOST, "bash -s"],
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"{HOST} did not answer within {timeout}s") from None
    except FileNotFoundError:
        raise RuntimeError("ssh is not installed locally") from None
    if proc.returncode != 0 and not proc.stdout.strip():
        detail = proc.stderr.strip() or f"exit {proc.returncode}"
        raise RuntimeError(f"ssh to {HOST} failed: {detail}")
    return proc.stdout


def _fields(stdout: str) -> dict[str, str]:
    """Parse the `key<TAB>value` lines the remote scripts print."""
    out: dict[str, str] = {}
    for line in stdout.splitlines():
        if "\t" in line:
            key, value = line.split("\t", 1)
            out[key] = value
    return out


# Discovered rather than assumed. The Wayland socket, the Hyprland signature and
# the XWayland display number all change across reboots.
PRELUDE = r"""
RUNDIR="/run/user/$(id -u)"
WD=$(ls "$RUNDIR" 2>/dev/null | grep -m1 '^wayland-[0-9]*$')
HIS=$(ls "$RUNDIR/hypr" 2>/dev/null | head -1)
export XDG_RUNTIME_DIR="$RUNDIR"
export WAYLAND_DISPLAY="${WD:-wayland-1}"
export DBUS_SESSION_BUS_ADDRESS="unix:path=$RUNDIR/bus"
export HYPRLAND_INSTANCE_SIGNATURE="$HIS"
export MOZ_ENABLE_WAYLAND=1
export XDG_SESSION_TYPE=wayland

# v2rayN is X11-only, so it needs DISPLAY. Hyprland does not export DISPLAY into
# its own environ, so read it from the Xwayland command line.
XDISP=$(pgrep -a Xwayland 2>/dev/null | awk '{for(i=1;i<=NF;i++) if ($i ~ /^:[0-9]+$/) {print $i; exit}}')
export DISPLAY="${XDISP:-:0}"

# Terminate every process with this exact name ($1 = name, $2 = seconds to
# wait). SIGTERM first, SIGKILL after. Used to clear what a previous failed
# launch left behind: a second v2rayN never binds the port, and a browser that
# crashed on start leaves windows that count as "already running".
kill_stale() {
  pids=$(pgrep -x "$1" 2>/dev/null)
  [ -z "$pids" ] && return 0
  kill $pids 2>/dev/null
  for _ in $(seq 1 $(( $2 * 2 ))); do
    pgrep -x "$1" >/dev/null 2>&1 || return 0
    sleep 0.5
  done
  kill -9 $(pgrep -x "$1" 2>/dev/null) 2>/dev/null
  return 0
}

# Best-effort proxy: up, started, missing (no binary), or failed to come up.
# Never fatal — the browser still launches without it.
proxy_state=up
ensure_proxy() {
  proxy_state=up
  if ss -ltn 2>/dev/null | grep -q '@PROXY_ADDR@'; then
    # The listener can outlive its GUI: v2rayN hands the port to an `xray` core,
    # and a killed GUI leaves that core orphaned (ppid 1) still holding it. A
    # port with no v2rayN behind it is a leftover, not a working proxy.
    pgrep -x v2rayN >/dev/null 2>&1 && return 0
    kill_stale xray 4
  fi
  proxy_state=down
  V2RAY_DIR="@V2RAY_DIR@"
  if [ ! -x "$V2RAY_DIR/v2rayN" ]; then
    proxy_state=missing
    return 0
  fi
  # A v2rayN left over from a failed start still holds its singleton and never
  # opens the port, so a second copy would sit there doing nothing too. Its core
  # has to go as well, or the new GUI cannot bind.
  kill_stale v2rayN 5
  kill_stale xray 4
  # cwd matters: v2rayN resolves bin/ and guiConfigs/ relative to it.
  setsid sh -c "cd '$V2RAY_DIR' && exec ./v2rayN" >/tmp/v2rayN.log 2>&1 < /dev/null &
  for _ in $(seq 1 25); do
    sleep 1
    ss -ltn 2>/dev/null | grep -q '@PROXY_ADDR@' && { proxy_state=started; return 0; }
  done
  proxy_state=failed
  return 0
}

# Fullscreen the window matching title regex $2 in class regex $1, falling back
# to the most recently used window of that class. Acts only when not already 2.
zoom_window() {
  cls=$1; ttl=$2
  fs=$(hyprctl clients -j 2>/dev/null | jq -r --arg c "$cls" '[.[] | select(.class|test($c)) | .fullscreen] | max // 0')
  [ "${fs:-0}" = "2" ] && { printf 'fullscreen\t2\n'; return; }
  addr=$(hyprctl clients -j 2>/dev/null | jq -r --arg c "$cls" --arg t "$ttl" \
    '([.[] | select(.class|test($c)) | select(.title|test($t))] | sort_by(.focusHistoryID) | .[0].address)
     // ([.[] | select(.class|test($c))] | sort_by(.focusHistoryID) | .[0].address)')
  if [ -n "${addr:-}" ] && [ "$addr" != "null" ]; then
    hyprctl dispatch "hl.dsp.focus({ window = \"address:$addr\" })" >/dev/null 2>&1
    hyprctl dispatch 'hl.dsp.window.fullscreen()' >/dev/null 2>&1
  fi
  printf 'fullscreen\t%s\n' "$(hyprctl clients -j 2>/dev/null | jq -r --arg c "$cls" '[.[] | select(.class|test($c)) | .fullscreen] | max // 0')"
}

# Park the proxy GUI on its own workspace so the browser owns the visible one.
# The window appears a beat after the port opens, so wait for it rather than
# racing. Silent: the user keeps looking at whatever they were looking at.
move_proxy_window() {
  [ "$proxy_state" = "missing" ] && return 0
  addr=""
  for _ in $(seq 1 15); do
    addr=$(hyprctl clients -j 2>/dev/null \
      | jq -r '[.[] | select(.class|test("v2rayN"))] | sort_by(.focusHistoryID) | .[0].address // empty')
    [ -n "$addr" ] && break
    sleep 0.5
  done
  [ -z "$addr" ] && return 0
  ws=$(hyprctl clients -j 2>/dev/null | jq -r --arg a "$addr" '.[] | select(.address==$a) | .workspace.name')
  [ "$ws" = "@PROXY_WS@" ] || \
    hyprctl dispatch "hl.dsp.window.move({ window = \"address:$addr\", workspace = \"@PROXY_WS@\" })" >/dev/null 2>&1
  printf 'proxy_window\t%s\n' "$(hyprctl clients -j 2>/dev/null | jq -r --arg a "$addr" '.[] | select(.address==$a) | .workspace.name')"
}

wait_title() {
  # Ready when at least one window carries a real page title. Blank tabs, the
  # crash-restore dialog and the placeholder titles are all "not ready yet".
  cls=$1; title=""; ready=""
  for _ in $(seq 1 45); do
    title=$(hyprctl clients -j 2>/dev/null | jq -r --arg c "$cls" '[.[] | select(.class|test($c)) | .title] | join(" ; ")')
    ready=$(printf '%s' "$title" | tr ';' '\n' | sed 's/^ *//;s/ *$//' \
      | grep -vE '^(|Mozilla Firefox|Untitled.*|New Tab.*|New Window.*|Restore Session.*)$' | head -1)
    [ -n "$ready" ] && break
    sleep 2
  done
  [ -z "$ready" ] && printf 'blocked\tno page window\n'
  printf 'title\t%s\n' "$title"
}
"""

PROXY_NOTES = {
    "up": "proxy: already listening",
    "started": "proxy: was down, v2rayN started",
    "missing": "proxy: v2rayN not found, launched without it",
    "failed": "proxy: v2rayN started but the port never opened",
}


@mcp.tool()
def xps_status() -> str:
    """Report the proxy, the browsers running remotely, and the window titles."""
    out = _fields(_ssh(_fill(PRELUDE + r"""
printf 'proxy\t%s\n' "$(ss -ltn 2>/dev/null | grep -q '@PROXY_ADDR@' && echo listening || echo down)"
printf 'firefox\t%s\n' "$(pgrep -x firefox | wc -l)"
printf 'brave\t%s\n' "$(pgrep -x brave | wc -l)"
printf 'windows\t%s\n' "$(hyprctl clients -j 2>/dev/null | jq -r '[.[] | select(.class|test("firefox|brave")) | .title] | join(" ; ")')"
""")))
    return (
        f"host: {HOST}\n"
        f"proxy: {out.get('proxy')}\n"
        f"firefox: {out.get('firefox', '0')} process(es)\n"
        f"brave: {out.get('brave', '0')} process(es)\n"
        f"windows: {out.get('windows') or 'none'}"
    )


@mcp.tool()
def xps_start_proxy() -> str:
    """Start the v2rayN proxy on the remote host if it is not already listening."""
    out = _fields(_ssh(_fill(PRELUDE + r"""
ensure_proxy
printf 'state\t%s\n' "$proxy_state"
printf 'log\t%s\n' "$(tail -1 /tmp/v2rayN.log 2>/dev/null | cut -c1-120)"
"""), timeout=60))
    state = out.get("state", "unknown")
    note = PROXY_NOTES.get(state, f"proxy: {state}")
    log = out.get("log")
    return note + (f"\nlog: {log}" if log and state == "failed" else "")


@mcp.tool()
def open_page(browser: str = "firefox", fullscreen: bool = True) -> str:
    """Open the configured URL on the remote host in Firefox (default) or Brave.

    Starts the proxy first when the port is down and a v2rayN binary exists; if
    no binary is found the browser still launches. A browser already running
    without the proxy setting is restarted, because neither can be retrofitted.
    """
    if browser not in ("firefox", "brave"):
        return f"Unknown browser {browser!r}. Use 'firefox' or 'brave'."

    if browser == "firefox":
        launch = r"""
ensure_proxy
move_proxy_window
PROF="$HOME/.mozilla/firefox/plex-proxy"
mkdir -p "$PROF"
cat > "$PROF/user.js" <<'JS'
user_pref("network.proxy.type", 1);
user_pref("network.proxy.http", "127.0.0.1");
user_pref("network.proxy.http_port", 10808);
user_pref("network.proxy.ssl", "127.0.0.1");
user_pref("network.proxy.ssl_port", 10808);
user_pref("network.proxy.share_proxy_settings", true);
user_pref("network.proxy.no_proxies_on", "localhost, 127.0.0.1");
user_pref("browser.startup.page", 1);
user_pref("browser.startup.homepage", "@URL@");
user_pref("browser.sessionstore.resume_from_crash", false);
user_pref("browser.startup.homepage_override.mstone", "ignore");
user_pref("startup.homepage_welcome_url", "");
user_pref("startup.homepage_welcome_url.additional", "");
user_pref("trailhead.firstrun.didSeeAboutWelcome", true);
user_pref("browser.aboutwelcome.enabled", false);
user_pref("browser.shell.checkDefaultBrowser", false);
user_pref("datareporting.policy.dataSubmissionEnabled", false);
user_pref("toolkit.telemetry.reportingpolicy.firstRun", false);
JS

# A profile whose last session ended abruptly (the restart path kills the
# browser) boots into the restore dialog instead of the homepage. Clear it
# first: the dialog is the only window and the page never loads.
rm -f "$PROF/sessionstore.jsonlz4" "$PROF"/sessionstore-backups/*

# Two questions decide the action: is a firefox running on the proxy profile,
# and is it exactly one window showing the page? Anything else — no browser, the
# wrong profile, a restore dialog, a blank tab, two windows opened by earlier
# calls — is cleared before a single fresh instance starts.
ff_windows() {
  hyprctl clients -j 2>/dev/null | jq '[.[] | select(.class|test("firefox"))] | length'
}
page_windows() {
  hyprctl clients -j 2>/dev/null \
    | jq '[.[] | select(.class|test("firefox")) | select(.title|test("Plex"))] | length'
}

pid=$(pgrep -x firefox | head -1)
on_profile=""
if [ -n "${pid:-}" ] && tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null | grep -q 'plex-proxy'; then
  on_profile=1
fi

if [ -n "$on_profile" ] && [ "$(ff_windows)" = "1" ] && [ "$(page_windows)" -ge 1 ]; then
  action=reuse
else
  if [ -z "${pid:-}" ]; then
    action=start
  elif [ -n "$on_profile" ]; then
    action=clean
  else
    action=restart
  fi
  kill_stale firefox 8
  setsid firefox --profile "$PROF" --new-instance >/tmp/firefox-plex.log 2>&1 < /dev/null &
fi
printf 'action\t%s\n' "$action"
wait_title firefox
@ZOOM@
printf 'proxy\t%s\n' "$proxy_state"
printf 'log\t%s\n' "$(tail -1 /tmp/firefox-plex.log 2>/dev/null | cut -c1-120)"
"""
        notes = {
            "start": "Firefox was not running; started on the proxy profile",
            "clean": "cleared the windows earlier launches left behind; started one fresh",
            "restart": "Firefox was running on another profile; restarted on the proxy profile",
            "reuse": "Firefox already showed the page; reused the window",
        }
    else:
        launch = r"""
ensure_proxy
move_proxy_window
pid=$(pgrep -x brave | head -1)
if [ -n "${pid:-}" ]; then
  if tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null | grep -q -- '--proxy-server='; then
    action=tab
    setsid brave --ozone-platform=wayland --new-window '@URL@' >/tmp/brave-plex.log 2>&1 < /dev/null &
  else
    action=restart
    kill $(pgrep -x brave) 2>/dev/null
    sleep 3
    setsid brave --ozone-platform=wayland --proxy-server='@PROXY@' \
      --no-first-run --no-default-browser-check --new-window '@URL@' \
      >/tmp/brave-plex.log 2>&1 < /dev/null &
  fi
else
  action=start
  setsid brave --ozone-platform=wayland --proxy-server='@PROXY@' \
    --no-first-run --no-default-browser-check --new-window '@URL@' \
    >/tmp/brave-plex.log 2>&1 < /dev/null &
fi
printf 'action\t%s\n' "$action"
wait_title brave
@ZOOM@
printf 'proxy\t%s\n' "$proxy_state"
printf 'log\t%s\n' "$(tail -1 /tmp/brave-plex.log 2>/dev/null | cut -c1-120)"
"""
        notes = {
            "start": "Brave was not running; started with the proxy",
            "restart": "Brave was running without the proxy; restarted with it",
            "tab": "Brave already had the proxy; opened a new window",
        }

    zoom = f"zoom_window {browser if browser == 'brave' else 'firefox'} Plex" if fullscreen else ""
    script = _fill(PRELUDE + launch.replace("@ZOOM@", zoom))

    out = _fields(_ssh(script, timeout=LAUNCH_TIMEOUT))
    action = out.get("action", "?")
    title = out.get("title") or "no window"
    fs = out.get("fullscreen")
    parts = [notes.get(action, action), f"window: {title}"]
    if out.get("blocked"):
        parts.append(f"warning: {out['blocked']} — the page did not load")
    if fs:
        parts.append(f"fullscreen: mode {fs}")
    parts.append(PROXY_NOTES.get(out.get("proxy", ""), "proxy: unknown"))
    if out.get("proxy_window"):
        parts.append(f"proxy window: workspace {out['proxy_window']}")
    return "\n".join(parts)


if __name__ == "__main__":
    mcp.run()
