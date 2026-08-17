# From Thought to Trailer: Making an AI Video with a Loop and Five Skills

A sixty-second trailer for a personal essay on death in Mexico is a small artifact. The workflow that produced it is not. By the time the trailer was rendered, I had built a chain of five codified skills running inside OpenCode, all steered by one collaboration loop, and I had rewritten parts of it twice after failures that no amount of planning predicted. This essay is about the workflow. The trailer is just its proof.

## The trailer in one paragraph

The video is 59.5 seconds, 480p, 24 frames per second, H.264 video with AAC audio. It opens with a black title card carrying the essay's soul line — 死亡未必是生命的终点, "death need not be the end of life" — then three beats: the streets of Guadalajara and a Día de Muertos mural (现场观察), a ceramic skull and a courtyard (日常化), a church interior (精神), and a closing card with the same soul line. Every beat carries one line of Simplified Chinese subtitles burned into the frame. All of it was made from eight real photographs taken in Mexico, a pile of decisions, and a session model that never once looked at a picture.

## The loop: thought-flow

The workflow is organized around an eight-stage loop I use for every task: INTENT → CONSTRAINTS → PROPOSE → PRESS → PRACTICE → INVESTIGATE → CODIFY → BOUNDARY-CHECK. It is not a checklist; it is an architecture of thought-flow, a loop that converges. The two most expensive stages come first. State the intent and the constraints plainly, because a precise description beats a better model: the trailer had to be under a minute, at 480p, subtitle-only (no TTS available), and the soul line had to appear verbatim in the opening and closing cards. Every proposal came with options and a recommendation, so that disagreeing with me was a meaningful act rather than a refusal. When something failed, I investigated the real system before blaming the tool, and when a procedure worked twice, I codified it into a skill. This whole essay is that loop running in public: each section below is one stage doing real work.

## One source of truth: death-thought-flow

The project's content lives in a master skill named death-thought-flow: the essay's actual subject — Mexican death culture versus Tibetan Buddhist views on death — the verified facts (that La Catrina is a Day of the Dead icon, that Tlaquepaque is Guadalajara's ceramics town), the photo pool, and the guardrails about what must not be invented. Downstream skills reference this file and never duplicate its content. That is the boundary-check in action: the knowledge lives in exactly one place, sized to its worktree, and the video pipeline is a consumer, not a second home for facts. It is also the anti-hallucination layer — when a script describes the skulls, it does so from the master file, not from whatever the model happens to remember about Mexican death culture.

## From content to script: story-telling

The story-telling skill turns the master content and the photo pool into a narration script: a sequence of beats, one voiceover line per beat, per-clip visual prompts for the video engine, a music/audio cue per section, and a table that doubles as the subtitle source. For the trailer I added a trailer mode to the skill itself — target under sixty seconds, roughly three author-chosen beats, photo reuse allowed, the soul line as a fixed bookend — because the pattern repeated and one-off solutions die with the session. The script is the contract between thinking and rendering: it is the only artifact a human reads, and it is the exact input the video pipeline consumes. A single excerpt shows the grain of it:

```
## 段落二 日常化 (0:21-0:38)
**旁白:** "没有肃穆的仪式,也没有回避的目光。桌上的陶艺骷髅、院墙上的十字架,
死亡就这样被安静地请进了日常。"
| Clip | 时长 | 视觉提示 |
| 2.1 | 8s | Slow macro push-in on a hand-painted ceramic Day-of-the-Dead skull on a
wooden table beside blue and green mugs. Warm window light, quiet, contemplative. |
```

## Seeing without eyes: read-image

The session model cannot see images — no image input at all — yet the whole video is driven by eight photographs. The solution was to stop fighting the constraint and orchestrate around it: delegate vision to a separate model, then feed its text back into the pipeline. One command, per photo:

```
opencode run "Describe this photo factually: subjects, objects, colors, composition,
any visible text. Also: does it contain recognizable human faces?"
  --model openrouter/z-ai/glm-4.6v --file=imgs/260816-mexico-01.png
```

Two things came out of those descriptions. First, a narrative-ordering principle that generalizes: arrange a set of images to tell a story with a narrowing-then-widening arc — establish the place, state the theme, zoom to the object, go private, go spiritual, introduce people, end on celebration. Second, the question that reshaped the entire video: "does it contain recognizable human faces?" Every photo of a person — the guitar player, the mother and child, the costumed dancers — was later rejected by the video engine. The vision delegation had found the failure before the render did.

## The render: video-gen

The video-gen skill drives Seedance 2.0 image-to-video through OpenRouter's asynchronous API: submit a job with the frame and a prompt, poll until it completes, download the clip. Per clip it looks roughly like this:

```
payload = {
  "model": "bytedance/seedance-2.0-fast",
  "prompt": clip["prompt"],
  "duration": 8, "resolution": "480p", "aspect_ratio": "16:9",
  "generate_audio": True,
  "frame_images": [{"type": "image_url",
    "image_url": {"url": f"data:image/png;base64,{b64}"},
    "frame_type": "first_frame"}],
}
```

Six clips, about three minutes of generation, then local ffmpeg assembly: a drawtext title card, a concat of the clips, subtitles burned in with the Noto CJK font. This is where plans meet reality, and reality pushed back twice. The first rejection was content policy: a submit returned HTTP 400 with `InputImageSensitiveContentDetected.PrivacyInformation` — Seedance refuses to animate frames containing real people, which is why a picture of a man with a guitar is forever banned from this video while a picture of a ceramic skull is not. The beat was rewritten to use the pedestrian street twice with different camera moves, and the script was updated to match. The second rejection was audio copyright: one clip failed with "the output audio may be related to copyright restrictions," and succeeded untouched on the next try — a transient flag, a reminder that these systems are stochastic, and that a failure message is a clue, not a conclusion.

## The audio lottery, and how I stopped playing it

The biggest problem was never the pictures. Each clip carried its own independently-generated ambient audio, and the lottery produced a mess: the loudest clip averaged -17.7 dB, the quietest -50.7 dB, and two clips — the ones whose prompts said "quiet, contemplative" — were effectively silent, with long stretches of pure silence inside them. The model had over-obeyed the prompt. I verified this with ffmpeg before changing anything, because an error is a clue and a measurement is a verdict:

```
ffmpeg -i clip.mp4 -af volumedetect -f null -
ffmpeg -i clip.mp4 -af silencedetect=noise=-38dB:d=0.6 -f null -
```

I proposed three fixes: regenerate the two silent clips with audible-audio prompts; a free post-only mask of normalized levels plus a synthesized bed; or a full silent re-roll — regenerate every clip with `generate_audio: false` and build one continuous soundtrack in post. We chose the third, for control. The re-roll was six fresh clips at about $2.16, and the soundtrack was synthesized locally in a few seconds of pure-Python: lowpassed wind as room tone, a warm detuned A-drone (A2/E3/A3 with a slow breathing LFO), and sparse A-minor pentatonic plucks that gesture at a marimba without claiming to be music. A fade-in over the title card, a fade-out over the closing card, muxed as one seamless track. The result is a video with zero audio gaps, and a lesson codified: decouple audio from video generation whenever the story matters more than the ambience.

## Lessons learned

- State the constraints first; they are the most expensive stage. The "quiet, contemplative" prompt produced literal silence, and the fix cost a full re-render. A precise sentence about what the audio must be would have cost nothing.
- A plan with one path is a demand, not a proposal. Every decision here — the narrative order, the audio strategy — was offered with options and a recommendation, which made the right choices easy to find and wrong ones cheap to reject.
- Failures are data. The audio "bug" was a 33 dB level span measured in thirty seconds, not a hunch. Investigate before blaming the tool.
- Codify what works twice. read-image and trailer mode exist as skills because the pattern repeated; one-off solutions die with the session, skills survive to be reused and improved.
- Boundary-check everything. Content lives in death-thought-flow, procedures in skills, and the generic technique of delegating vision in a skill of its own — each placed where the work happens, none duplicated.
- The loop converges, but intent lives outside it. I chose the arc, the order, the sound, the words. The machine never decided anything; it made my decisions legible and cheap to revise.

In the end, the trailer is less interesting than the way it was made: eight photos that a blind model orchestrated, a plan that broke twice against content policy and stochastic failure, and a loop that turned both breakages into skills. That is the part worth keeping.

btw, i use arch 
