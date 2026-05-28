
```sh
OpenClaw config is invalid
File: ~/.openclaw/openclaw.json
Problem:
  - channels.telegram.streaming: invalid config: must be object
  - channels.discord.streaming: invalid config: must be object
Legacy config keys detected:
  - channels: channels.<id>.threadBindings.spawnSubagentSessions/spawnAcpSessions were replaced by channels.<id>.threadBindings.spawnSessions. Run "openclaw doctor --fix".
  - channels.telegram: channels.telegram.streamMode, channels.telegram.streaming (scalar), chunkMode, blockStreaming, draftChunk, and blockStreamingCoalesce are legacy; use channels.telegram.streaming.{mode,chunkMode,preview.chunk,block.enabled,block.coalesce}.
```