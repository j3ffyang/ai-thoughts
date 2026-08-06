# Pushing the Limits of My Local LLM: Switching from Ollama to llama.cpp

I'm running a local LLM on my Arch Linux + Hyprland setup, and already have `qwen2.5:7b` with Ollama.

I want to maximize the usage of my hardware.

Therefore I decided to download a slightly bigger model to cover my daily document writing and Python coding work, and switch from Ollama to llama.cpp.

## The Reason of Switching to `llama.cpp` from `ollama`

The quality and efficiency would be tremendously increased. There is more detailed explanation on the web; I'll just summarize the main points here

- Granular Hardware Control: llama.cpp lets you manually offload the exact number of model layers to maximize your shared AMD APU VRAM without playing it "too safe" like Ollama's automatic engine.
- Peak Resource Efficiency: It eliminates background daemon overhead by running as a single, lightweight C++ binary that exits completely, saving battery and memory on your GPD device.
- Unix-Centric Minimalism: It integrates natively into Linux (and macOS) environment, allowing you to easily adjust memory context windows, flags, and script pipes on the fly.

## Determine How Much vRAM

```sh
[jeff@gpd blobs]$ free -h
               total        used        free      shared  buff/cache   available
Mem:            23Gi       9.7Gi       2.3Gi       503Mi        11Gi        13Gi
Swap:           11Gi          0B        11Gi
[jeff@gpd blobs]$ glxinfo | grep -i "video memory"
    Video memory: 8192MB
    Dedicated video memory: 8192 MB
    Currently available dedicated video memory: 7079 MB
```

## Download LLM using Ollama
Download `qwen2.5:14b`

Find out where it is located

```sh
[jeff@gpd blobs]$ pwd
/var/lib/ollama/.ollama/models/blobs
[jeff@gpd blobs]$ find . -size +8G -size -10G
./sha256-2049f5674b1e92b4464e5729975c9689fcfbf0b0e4443ccf10b5339f370f9a54
```

After the download finishes, Ollama won't be needed and can be stopped

```sh
sudo systemctl stop ollama
```

## Configure llama.cpp to use LLM

Create a symlink to the model downloaded via `ollama`. First create a local directory to hold the symlink

```sh
mkdir -p ~/llama.cpp/

ln -s /var/lib/ollama/.ollama/models/blobs/./sha256-2049f5674b1e92b4464e5729975c9689fcfbf0b0e4443ccf10b5339f370f9a54 \
  ~/llama.cpp/qwen2.5-14b.gguf
```

Change the `sha256` hash to yours

Start the server (no `sudo` needed — it runs as your user and stays reachable at localhost)

```sh
[jeff@gpd ~]$ llama-server -m ~/llama.cpp/qwen2.5-14b.gguf -ngl 32 -c 8192 --flash-attn on -np 1 --port 8080
```

You'd see something like
```sh
...
0.02.762.489 I srv  llama_server: model loaded
0.02.762.494 I srv  llama_server: listening on http://127.0.0.1:8080
```

## Configure Obsidian using `llama.cpp`

`llama-server` already exposes an OpenAI-compatible API at `http://127.0.0.1:8080/v1`, so any Obsidian plugin that accepts a custom OpenAI-compatible endpoint can talk to it. Using the **Karpathy LLM Wiki** plugin (same one as the previous article):

1. Start `llama-server` first (see above).
2. Obsidian > Settings > Karpathy LLM Wiki.
3. Pick provider: **OpenAI** (or "custom endpoint"/OpenAI-compatible if your version lists it).
4. Set **Base URL** to `http://127.0.0.1:8080/v1`.
5. Set **Model** to `qwen2.5-14b` (type it manually or fetch from `/v1/models`).
6. Leave the **API key empty** — it's a local server, no auth needed.
7. Click **Test Connection**, then **Save Settings**.

That's it — your notes now query the local 14B model. The same endpoint also works with any other OpenAI-compatible Obsidian plugin (Copilot, Smart Connections, Text Generator, ...) for document writing and Python coding assistance.

## Tuning

To maximize local LLM capability through `llama.cpp`, the parameters can vary depending on your GPU or hardware spec, so it's important to tune them.

One strong reason to run everything through the command line is that any error (or warning) message is printed clearly, which helps debugging. If you get an error, check Google or similar first. Here's my printed log

```sh
...
0.00.038.015 I cmn  common_param: common_params_print_info: verbosity = 3 (adjust with the `-lv N` CLI arg)
0.00.038.358 W srv  llama_server: -----------------
0.00.038.360 W srv  llama_server: CORS is set to allow all origins ('*') and no API key is set
0.00.038.360 W srv  llama_server: this can be a security risk (cross-origin attacks)
0.00.038.360 W srv  llama_server: more info: https://github.com/ggml-org/llama.cpp/pull/25655
0.00.038.360 W srv  llama_server: -----------------
0.00.039.555 I srv    load_model: loading model '/home/jeff/llama.cpp/qwen2.5-14b.gguf'
0.00.268.690 W load: control-looking token: 128247 '</s>' was not control-type; this is probably a bug in the model. its type will be overridden
0.02.757.937 I srv    load_model: initializing, n_slots = 1, n_ctx_slot = 8192, kv_unified = 'false'
0.02.762.489 I srv  llama_server: model loaded
0.02.762.494 I srv  llama_server: listening on http://127.0.0.1:8080
1.07.002.103 I slot get_availabl: id  0 | task -1 | selected slot by LRU, t_last = -1
1.07.002.163 I slot launch_slot_: id  0 | task 0 | processing task, is_child = 0
1.22.014.086 I slot print_timing: id  0 | task 0 | prompt processing, n_tokens =   2048, progress = 0.42, t =  15.01 s / 136.43 tokens per second
1.41.426.409 I slot print_timing: id  0 | task 0 | prompt processing, n_tokens =   4096, progress = 0.84, t =  34.42 s / 118.99 tokens per second
2.08.679.214 I slot print_timing: id  0 | task 0 | n_decoded =    100, tg =   5.88 t/s, tg_3s =   5.88 t/s
2.11.798.583 I slot print_timing: id  0 | task 0 | n_decoded =    118, tg =   5.86 t/s, tg_3s =   5.77 t/s
```

We can see the local LLM handles roughly 5~6 tokens/second, which seems low, but it maintains better output quality than `qwen2.5:7b`. Certainly, if you prioritize faster processing — often a few times faster — you could try `qwen2.5:7b` for similar use cases like knowledge management with Karpathy LLM Wiki.

## 14B is Better than 7B in Terms of Output Quality

Why the 14B Model Delivers Better Quality
- Sharper Reasoning & Logic: The 14B model has a much deeper understanding of nuanced logic. It is far less likely to make logical leaps, misunderstand complex prompts, or hallucinate false information compared to the 7B model.
- Superior Coding & Syntax: For text editing, scripting, or note organization, the 14B version has a much tighter grasp on programming syntax and structured formatting (like markdown or JSON). It can handle multi-step instructions without forgetting constraints.
- Broader Knowledge Base: It retains significantly more factual information and context from its training data, making its answers more comprehensive, detailed, and accurate.