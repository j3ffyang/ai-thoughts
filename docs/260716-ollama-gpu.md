# Ollama on Arch Linux using AMD GPU

## Objective

- arch linux + hyprland on gpd win4 handheld (powerful beyond my initial expectation) with amd gpu + an external amd gpu. so 2 gpu
- install ollama in order to use local llm for obsidian with karpathy llm wiki (i'll write another blog abour llm wiki)

## hardware and operating system spec

- arch linux + hyprland

## what has been taken at the beginning

## Problem 

- none of 2 gpus' usage is higher than 30% consistently, which indicates ollama
- cpu running at almost 100% all the time

## command to dianose

ollama ps

## resolution

- clean-up existing downloaded model

cd /var/lib/ollama/.ollama/blobs/; rm -fr *     # make sure you know what you're doing

- grant permission to `ollama:ollama` user to own /var/lib/ollama

#### install from ollama.com

remove ollama and its dependencies for amd gpu which came from arch official repo. instead, install from ollama.com official site and it will install `ollama-rocm` utility

#### install utilities

nvtop glxinfo


