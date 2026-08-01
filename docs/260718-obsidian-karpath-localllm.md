# Configure Obsidian using Karpathy LLM Wiki with Ollama's Local LLM

## Background

i have more than 330+ documents/ notes that i've kept for years. 2 years ago, migrated from evernote to obsidian. so to build my own wiki/ knowledge base from my multi-year saved documents, not only technical ones, but any personal interests, such how to fly dcs, riding motorcycles in mountains, and photograph techniques, in both english and chinese lanugages. in theory, i could query and chat with my llm wiki and it would be able to gather and pull all the relted topics in result. amazing, isn't it?

found and got very interested in karpathy llm wiki and decided to try

burned out $10/ day for 3 days, then decided to try local llm via ollama

## it's simpler than your expectation

- obsidian with single plugin
- performance from local llm via ollama is really good

- there are tons of tutorials about how Karpathy LLM Wiki work and describing how its archtecture looks like, i recommend you can read/ view
    - https://datasciencedojo.com/blog/llm-wiki-tutorial/
    - https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki

I won't repeat it. there are some variants that can bring you comprehensive and complex solution of building the same. however, i would skip them and bring up a simplest one, after i tried severals and burned tokens for several days for test

#### 1. install obsidian

through arch linux official repo and obsidian is binded to electron, which is simple and okay

then select a Vault to start with. i would recommend you start a new vault, starting with a few documents, as llm processing docs really takes time and costs money if connecting to external language model on web

do not install any plugin, or you won't really know which is which

- do not need `CLAUDE.md`, nor `AGENT.md` (or `AGENTS.md`), nor `SCHEMA.md`

- if you really want to understand how LLM Wiki works, read `<VAULT>/wiki/schema/config.md`

#### 2. just install karpathy llm wiki plugin through community plugin

## install local llm via ollama

this one could be an option as if hooking to public llm on web would be quite simple as well. 

my intention is

a. as i have a GPD Win4 gamepad, with an internal AMD GPU and an external AMD GPU, i wanted to test out its capability, to push up to the limit see how they can run a local llm model and how the model benchmark could be, in term of speed and analysis/ summarization quality

b. 

by the way, i use arch linux for years and only used microsoft windows for playing pc games. anyway, completely ditched microsoft windows when proton 

