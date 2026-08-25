# Ten Rules for Making an AI Video

Making a video with an AI image-to-video engine is not hard; the renderer is the easiest part of the job. It takes your picture and your prompt and returns a clip, and on a good day the clip is exactly what you asked for. The work is everything before that moment: deciding what the video is about, choosing which pictures to use and in what order, writing a script the renderer can obey, and — the part nobody warns you about — deciding what the audience will *hear*. These ten rules are what a sixty-second trailer taught me. They apply to any AI video, whatever the subject, whatever the engine.

## 1. Write the story before the pixels

A narration script is the contract between you and the renderer. It should name the beats of the video, carry one voiceover line per beat, and give every shot its own visual prompt. A script is not a nice-to-have; it is the thing you read to decide whether the video is good before you spend a single dollar rendering it. The most useful trick I learned: write the subtitles first. If the video works on a black screen with only the words, the pictures are decoration; if the words are empty, no amount of rendering will save it.

## 2. Keep one source of truth for the facts

If the video is about something real — a place, a culture, an event — put the verified facts in one file and let the pipeline read only from there. This is the anti-hallucination layer. When your script describes a Day of the Dead symbol, it quotes the master file instead of whatever the model happens to remember that day. One file, one truth, and every downstream skill is a consumer rather than a second home for the facts.

## 3. Borrow eyes if you have none

Session models are often blind: they cannot see images at all, yet they are perfectly capable of directing a video built from photographs. Solve this by delegating vision to a separate vision-capable model, one command per image, then feed the text back into the workflow. While you have the vision model's attention, ask it the question that matters most before a single render: does this image contain recognizable human faces? In my case that single question identified every frame the engine would later refuse on content-policy grounds — before I paid for the refusal.

## 4. Order the images by story, not by capture

Descriptions in hand, the question becomes sequence. Capture order and personal preference are not narrative order. A reliable arc for a set of images: establish the place, state the theme, zoom to the object, go private, go spiritual, introduce people, end on celebration. It narrows from wide to intimate, then widens again toward life. Nobody watching cares what order you shot the pictures; they care that each image motivates the next.

## 5. Constrain early — the engine over-obeys

Image-to-video engines take adjectives literally. I wrote "quiet, contemplative" into a visual prompt, and the engine produced two clips that were, in the strictest sense, silent: long stretches of nothing, at roughly -50 dB. The fix cost a full re-render. State your constraints as directives — resolution, duration, audio policy, whether people may appear, what the subtitles must say — before the prompts, and let the renderer surprise you in motion, never in policy.

## 6. Prove the pipeline on one clip

Before committing to a batch, render one short clip end to end: submit, poll, download, inspect. The first clip costs a few cents and a few minutes, and it will show you the engine's real output resolution, the frame-crop behavior, the pricing, and any API quirks — everything the marketing page got wrong. Every pipeline question that can be answered with one clip should be. A batch of six clips is the wrong time to discover that your frames are the wrong aspect ratio.

## 7. Expect stochastic failure; design for it

Asynchronous video APIs are a submit-poll-download loop, and the loop will break. Killed processes, empty downloads, and the two failure classes I hit: content-policy rejects at submit time (real people in a frame), and transient flags like a copyright warning that vanished on an identical retry. Design the pipeline to be resumable — job state on disk, retry on failure, alternate shots ready for rejected frames. A failure message is a clue, not a conclusion; sometimes the honest answer is "run it again."

## 8. Take the audio out of the lottery

If each clip generates its own audio, you are playing a lottery: six independent ambiences, level jumps of thirty decibels between them, and the "quiet" clip that is actually silent. When the story matters more than serendipitous ambience, decouple audio from video. Render every clip silent, then build one continuous soundtrack in post — one track, no gaps, no jumps. It costs a re-render and turns a montage with holes into something that holds together. Ambience is a layer you control, or it is a problem you have.

## 9. Measure before you fix

When audio sounds broken, or colors look wrong, or a clip feels off, the temptation is to tweak and pray. Measure first. A thirty-second pass with ffmpeg's volume and silence detectors turned "the audio is broken" into "a 33 dB level span and two silent clips" — a diagnosis, not a mood. Know your diagnostic commands before you need them; they are the difference between fixing a symptom and fixing a cause.

## 10. Assemble locally and know your costs

The renderer does not deliver a finished video; it delivers clips. Assembly is a local job, and ffmpeg does it for free: title cards with drawn text, concatenation of clips, burned-in subtitles with any CJK font on your system, loudness normalization. None of it touches the cloud or your budget. And know your per-clip price before you submit, not after: at the fast 480p tier a sixty-second trailer costs roughly two dollars. Cost is a planning input, not a surprise.

---

The one-line version: **decide the story, delegate the eyes, constrain early, prove the pipeline, expect failure, and take the audio out of the lottery.**

None of these rules are about the machine. The engine never decided anything in my project — I chose the arc, the order, the sound, the words. The machine made my decisions legible and cheap to revise. That is the actual service it provides, and it is the reason the rules above all live upstream of the render: the video was made before a single frame was generated.

## The principles, encoded

Principles are cheap; enforcement is the work. After one run, most of these rules were turned into gates inside the pipeline's skills, so the failures this essay describes cannot recur the expensive way:

- **Rule 3 (borrow eyes, scan for faces)** → a mandatory face-scan gate: every frame is checked for real people before any submission, and flagged frames are blocked and swapped for alternates.
- **Rule 4 (order by story)** → a narrative-order gate: the first render must be the story arc, never capture or preference order.
- **Rule 5 (constrain early)** → a prompt style guide: mood adjectives that map to audio are banned, policy constraints are embedded in every prompt.
- **Rule 6 (prove on one clip)** → a risk-POC gate: the proof run deliberately includes a people-frame and a still-life frame.
- **Rule 7 (expect failure)** → a resumable driver with size-verified downloads and transient-vs-permanent retry classification.
- **Rule 8 (audio out of the lottery)** → silent clips plus one synthesized soundtrack is now the default, not a salvage operation.
- **Rules 1, 2, 9, 10** were already practiced; they became verification steps rather than gates.

The loop that made the trailer now guards the trailer's own making.

btw, i use arch
