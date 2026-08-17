---
name: video-gen
description: >
  Generate a video from a story-telling narration script plus the author's
  photos, using Seedance 2.0 image-to-video via OpenRouter's asynchronous
  video API: pre-render gates (face-scan, narrative order, risk-POC), then
  per-clip submit -> poll -> download, then ffmpeg assembly. Multi-clip
  projects default to silent clips plus one continuous soundtrack (synthesized
  or royalty-free/PD); subtitle voiceover is the fallback (no OpenRouter TTS). Verified working
  2026-08-15 (POC: 4s 480p clip, $0.28, ~3 min). Use when the user asks to
  render a narration script into a video, generate a 视频, or run the
  death-in-Mexico project's video pipeline. Related terms: Seedance,
  视频生成, OpenRouter, image-to-video.
---

# Video Generation (Seedance 2.0 via OpenRouter)

Render a story-telling narration script plus the author's photos into a finished MP4. The engine is Seedance 2.0 through OpenRouter's dedicated asynchronous video endpoint.

## Engine status (verified 2026-08-15)

- OpenRouter video generation is **live and working**. The models are **not** in the standard `/api/v1/models` list — discover them via the dedicated endpoint `GET https://openrouter.ai/api/v1/videos/models` (23 video models listed, including `bytedance/seedance-2.0`, `-fast`, `-mini`, `-2.5`, plus Veo 3.1, Kling, Hailuo).
- `bytedance/seedance-2.0` (verified from the live catalog): durations 4–15 s, resolutions 480p/720p/1080p/4K, aspect ratios 16:9/9:16/1:1/4:3/3:4/21:9/9:21, image-to-video with `first_frame`/`last_frame` control, native audio (`generate_audio`), deterministic `seed`. Token cost: `(H*W*duration*24)/1024` tokens; `video_tokens` SKU at $0.000007/token, 1080p SKU at $0.0000077/token.
- Measured POC (this setup, 2026-08-15): 4 s, 480p, 16:9, data-URL first frame, audio on → **$0.284, completed in ~190 s**, output H.264+AAC MP4 (864×496).
- **No TTS model exists on OpenRouter** — the video carries Seedance's native audio (ambience/sound) only. Voiceover must come from a separate TTS engine or fall back to on-screen subtitles.
- Re-verify the model catalog immediately before a run; model availability and pricing change.

## Inputs

- `script` — the narration script from `story-telling` (Markdown with sections, voiceover, clip grid, timing). Required.
- `photos` — the author's own photos referenced by the script (first frames for image-to-video). At least 5. Required.
- `model` — default `bytedance/seedance-2.0`; swap to `bytedance/seedance-2.0-fast` or `-mini` to cut cost and wait time.
- `duration` — per-clip seconds (4–15). Use short clips (4–8 s) for a POC, longer only after review.
- `resolution` / `aspect_ratio` — default `1080p` / `16:9` for the final cut; use `480p` for POCs.
- `voiceover` — TTS engine (none on OpenRouter yet) or `subtitles` fallback. Optional.
- `slug` — the video's slug; combined with today's date into the output filename. Optional (default: derived from the script's name).

## Output location

- Final MP4 → `ai-thoughts/videos/<YYMMDD>-<slug>.mp4`, parallel to `imgs/` and `docs/`, following the repo's `YYMMDD-slug` filename convention (6-digit date, hyphen, lowercase slug). Example: `videos/260815-death-mexico.mp4`.
- Intermediates (clips, concat manifest, subtitles, preprocessed frames) are regenerable — keep them in a scratch folder (e.g. `videos/.work-<YYMMDD>-<slug>/`), not alongside the final file.

## Prerequisites

- `OPENROUTER_API_KEY` in the environment (present in this setup).
- Python 3 (stdlib only — no pip packages needed) or curl for the API calls.
- `ffmpeg` / `ffprobe` and ImageMagick (`magick`/`convert`) for preprocessing and assembly.

## Pre-render gates (run before any submission)

Three gates come before the first API call. They exist because this pipeline once paid for failures these gates catch for free: real people in frames were rejected at submit time (costing a beat rewrite), preference-order clips had to be re-rendered in narrative order, and "quiet, contemplative" prompts produced literally silent clips.

1. **Face-scan gate.** Every frame passes a people check before it may be submitted. Delegate to a vision model via the `read-image` skill's technique (`opencode run "Describe this photo factually... Also: does it contain recognizable human faces?" --model openrouter/z-ai/glm-4.6v --file=<frame>`). Any frame flagged with faces is **blocked** — never submit it. Seedance refuses frames containing real people with HTTP 400 `InputImageSensitiveContentDetected.PrivacyInformation`, so a flagged frame is a permanent no, not a retry; pull an alternate photo or ask the user.
2. **Narrative-order gate.** Order the clips by story, not by capture or preference. Apply the `read-image` skill's narrowing-then-widening arc (establish → theme → object → private → spiritual → people → celebration) to the photo pool, and render in that order on the very first run. The first render must be the narrative version.
3. **Risk-POC gate.** Before the full batch, run a short proof-of-concept (a few 4 s clips) that deliberately samples the risky cases: one frame containing people (expect the content-policy refusal and confirm the fallback path) and one still-life frame (check for near-silent audio or audio flags). Surfacing these landmines costs cents; discovering them mid-batch costs re-renders.

## Prompt style guide

The engine over-obeys mood adjectives. Prompts are the only lever you control after the frame is chosen, so write them as policy, not poetry:

- **No mood adjectives that map to audio** — "quiet", "calm", "contemplative", "peaceful", "serene" tend to produce near-silent clips (measured -48 to -51 dB mean on two clips). The voiceover and the soundtrack carry the mood; the prompt carries motion and light.
- **Embed policy constraints in every prompt** — end each prompt with explicit directives: `no people`, `no text`, `no music`, `neutral ambient audio`, as the scene requires. Do not assume the engine will infer them.
- **Name the camera move** — `slow push-in`, `gentle lateral pan`, `slow pull-back` — so the same frame can serve two clips with different motion.
- **Stay factual and visual** — subject, lighting, atmosphere grounded in the photo's actual content (from the `read-image` descriptions), not invented props.

Canonical template:

```
<Camera move> <subject in the actual frame, from the read-image description>.
<Lighting and atmosphere grounded in the photo>. Cinematic documentary style.
No people. No text. No music. Neutral ambient audio.
```

## Procedure (verified flow)

The steps below assume the pre-render gates above have passed.

1. **Verify the engine.** `curl -s https://openrouter.ai/api/v1/videos/models` and confirm the chosen model id, its `supported_durations`, `supported_resolutions`, and `supported_aspect_ratios`. Absent → stop and report.
2. **Preprocess photos.** Resize and pad each photo to the target `size` (e.g. 1920×1080 for 1080p 16:9): `magick input.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 out.png`. Never overwrite the originals.
3. **Submit a job per clip.** `POST https://openrouter.ai/api/v1/videos` with `model`, `prompt` (from the prompt style guide), `duration`, `resolution`, `aspect_ratio`, and `frame_images` carrying the photo as a base64 **data URL** (`data:image/png;base64,...`) with `frame_type: "first_frame"`. **Audio default:** multi-clip projects submit `generate_audio: false` (see Audio strategy); `generate_audio: true` is opt-in for single-clip artifacts only. Response: `id`, `polling_url`, `status: pending` (HTTP 202).
4. **Poll.** `GET /api/v1/videos/{id}` every ~15–30 s until `status` is `completed` or `failed`. A 4 s 480p clip takes ~3 min.
5. **Download.** On `completed`, download `unsigned_urls[0]` (auth header still required). **Verify the file is non-empty** — a 0-byte download has been observed from a polling race; re-download before treating the clip as done. Record `usage.cost` per clip.
6. **Audio.** Multi-clip: build one continuous soundtrack per the Audio strategy and mux it in at assembly. Single-clip opt-in audio needs no post work.
7. **Voiceover.** No OpenRouter TTS — either generate narration with a separate TTS engine and mux it in, or render the script's voiceover as subtitles (`.srt`).
8. **Assemble.** Concat the clips in script order with ffmpeg; mux the soundtrack; burn subtitles; export the final MP4 to `ai-thoughts/videos/<YYMMDD>-<slug>.mp4`. Keep the concat manifest and every clip in the scratch folder so only failed clips get regenerated.
9. **QC.** Play through: order, pacing, audio continuity, cultural sensitivity. Run `ffprobe` + `volumedetect`/`silencedetect` on the final if audio matters. Report the final path and total cost (sum of per-clip `usage.cost`).

## Audio strategy (anti-lottery)

Per-clip native audio is a lottery: six independent ambiences, level jumps of 30+ dB between clips, and the "quiet" clip that is actually silent. When the story matters, take audio out of the generation and control it in post:

- **Default for multi-clip projects:** `generate_audio: false` on every clip, then build ONE continuous soundtrack and mux it at assembly — one track, no gaps, no level jumps. Fade in over the opening card, fade out over the closing card.
- **Synthesizing the soundtrack (stdlib Python + ffmpeg):** layer a lowpassed-noise wind/room tone, a warm detuned pad drone (e.g. A2/E3/A3 sines with a slow breathing LFO), and sparse pentatonic plucks as a light rhythmic gesture. Target ~-20 dB mean, gentle peaks. The track is generated locally for free and can be re-tuned (loudness, timbre, density) without any re-render.
- **Measure before fixing.** Diagnose audio complaints with `ffmpeg -i clip.mp4 -af volumedetect -f null -` and `ffmpeg -i clip.mp4 -af silencedetect=noise=-38dB:d=0.6 -f null -`. A 33 dB span across clips is a diagnosis, not a mood.
- **Synthesized soundtracks were rejected in practice** (2026-08-16: both a generated piano piece and an adagio strings pad); the user preferred a real royalty-free recording. Prefer offering a real PD/royalty-free track from the start.
- `generate_audio: true` remains the right choice only for a single-clip artifact with no soundtrack, where the engine's ambience is the whole point.

## Royalty-free / public-domain music (worked recipe)

- **incompetech (Kevin MacLeod)** is a reliable direct-download source: track metadata (title, filename, ISRC, length, instruments) lives in `https://incompetech.com/music/royalty-free/pieces.json`; the MP3 is at `https://incompetech.com/music/royalty-free/mp3-royaltyfree/<filename>.mp3` (URL-encoded). Example: *Erik Satie: Gymnopedie No 1* (ISRC `USUAN1100787`, filename `Gymnopedie No 1.mp3`, piano, 3:07).
- **License honesty.** All incompetech tracks are CC-BY (3.0 or 4.0): free for commercial use but **attribution is required** — carry the credit line in the description (e.g. `"Gymnopedie No 1" Kevin MacLeod (incompetech.com) / Licensed under Creative Commons: By Attribution 3.0 License`). If the user wants no attribution, point them at YouTube Audio Library's no-attribution filter (they must download it themselves — it needs their login).
- **Pick the segment, don't ship the whole track.** Cut a continuous ~60 s section matching the video: `ffmpeg -ss 0 -t 60 -i track.mp3 -af "afade=t=in:st=0:d=1.5,afade=t=out:st=58.5:d=1.5" -c:a pcm_s16le soundtrack.wav`.
- **Match the loudness reference** (e.g. a previously accepted soundtrack's `mean_volume`), not just the peaks. Measure with `volumedetect`; then boost with a limiter so the raise can't clip: `volume=4.5dB,alimiter=limit=0.9` (measured result: mean −17.7 dB, max −0.4 dB, no clipping).
- **Do not overwrite the previously accepted video** when swapping music — write a new filename (`...-<variant>.mp4`) and let the user compare.

## Assembly gotchas

- `-c:v copy` cannot be combined with `-vf subtitles=...` (filtergraph requires a re-encode) — drop `-c:v copy` and use `-c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p`.
- `-vf` is an output option: it must come after every input (`-i list.txt -i soundtrack.wav -vf subtitles=...`), otherwise ffmpeg errors with "Option vf ... cannot be applied to input url".

## Reference implementation (tested 2026-08-15, stdlib only)

```python
#!/usr/bin/env python3
"""Seedance 2.0 via OpenRouter — submit -> poll -> download. Usage: script.py <image> <prompt> [model] [duration] [resolution] [aspect_ratio]"""
import base64, json, os, sys, time, urllib.request

API = "https://openrouter.ai/api/v1/videos"
KEY = os.getenv("OPENROUTER_API_KEY")
AUDIO = False  # multi-clip default per the audio strategy; opt-in True for single-clip

image, prompt = sys.argv[1], sys.argv[2]
model = sys.argv[3] if len(sys.argv) > 3 else "bytedance/seedance-2.0"
duration = int(sys.argv[4]) if len(sys.argv) > 4 else 4
resolution = sys.argv[5] if len(sys.argv) > 5 else "480p"
aspect = sys.argv[6] if len(sys.argv) > 6 else "16:9"

with open(image, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

payload = {
    "model": model,
    "prompt": prompt,
    "duration": duration,
    "resolution": resolution,
    "aspect_ratio": aspect,
    "generate_audio": AUDIO,
    "frame_images": [
        {"type": "image_url",
         "image_url": {"url": f"data:image/png;base64,{b64}"},
         "frame_type": "first_frame"}
    ],
}

def call(url, body=None):
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {KEY}")
    req.add_header("Content-Type", "application/json")
    data = json.dumps(body).encode() if body is not None else None
    with urllib.request.urlopen(req, data=data, timeout=120) as resp:
        return resp.status, json.loads(resp.read().decode())

status, result = call(API, payload)
if status != 202:
    sys.exit(f"submit failed: {result}")
job_id = result["id"]
print(f"job {job_id} {result['status']}")

def download(job_id, pr):
    for url in pr.get("unsigned_urls", []):
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {KEY}")
        with urllib.request.urlopen(req, timeout=120) as vr:
            data = vr.read()
        if data:  # reject 0-byte downloads from polling races
            out = f"clip-{job_id}.mp4"
            with open(out, "wb") as fh:
                fh.write(data)
            print(f"saved {out} ({len(data)} bytes) cost=${pr.get('usage', {}).get('cost')}")
            return True
    print(f"{job_id}: completed but no usable url / empty body")
    return False

t0 = time.time()
while True:
    time.sleep(15)
    _, pr = call(result["polling_url"])
    st = pr["status"]
    print(f"[{int(time.time()-t0)}s] {st}")
    if st == "completed":
        if download(job_id, pr):
            break
        continue  # transient empty body — keep polling/retrying
    if st == "failed":
        err = pr.get("error", "")
        if "copyright" in err.lower() or "timeout" in err.lower():
            print(f"transient failure ({err[:120]}), retrying identical job")
            time.sleep(20)
            status, result = call(API, payload)  # re-submit identical
            if status != 202:
                sys.exit(f"resubmit failed: {result}")
            job_id = result["id"]
            continue
        sys.exit(f"permanent failure: {err}")
```

## Cost notes

- Billed per generated second with a resolution multiplier; the measured POC was **$0.284 for 4 s @ 480p with audio** (~$0.07/s). 1080p is roughly an order of magnitude more per second; `-mini`/`-fast` models and 480p/720p cuts are the cheap path.
- Always run the risk-POC gate (a few 4 s clips, deliberately including a people-frame and a still-life frame) before the full cut, and regenerate only failed clips — never the whole video.

## Error handling

- **Engine absent from the catalog** → stop and report; do not guess the API.
- **Content policy (`InputImageSensitiveContentDetected.*`)** → permanent for that frame; the face-scan gate should have caught it. Never retry the same frame — swap an alternate photo or ask the user.
- **Transient flags (audio copyright, timeout, rate limit)** → retry the identical job after a short backoff; verified to succeed on retry. A failure message is a clue, not a conclusion.
- **0-byte download** → re-download with size verification before counting the clip as done.
- **Data URL rejected** → host the frame image at an HTTPS URL and pass that instead.
- **No TTS engine** → offer the subtitle fallback; never silently drop narration.

## Verification

- Engine was re-checked against `GET /api/v1/videos/models` immediately before the run.
- The three pre-render gates ran: every frame passed the face-scan (no people in submitted frames), clips were ordered by the narrative arc, and the risk-POC was run before the batch.
- Photos were preprocessed without touching the originals; each clip row maps to exactly one downloaded clip.
- Audio policy applied: multi-clip projects have a single continuous soundtrack (no per-clip lottery); subtitles or TTS present as planned.
- Final MP4 is at `ai-thoughts/videos/<YYMMDD>-<slug>.mp4`; intermediates live only in the scratch folder.
- Total cost (sum of `usage.cost`) and the final file path were reported to the user.
