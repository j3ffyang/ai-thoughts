# 2nd Brain: AI-Powered Knowledge Assistant

[toc]

## 1. Overview

An AI-powered knowledge assistant built on Obsidian that allows users to query their personal knowledge base and receive grounded, context-aware responses in both Chinese and English.

**Problem:** 300+ notes in Obsidian are hard to navigate and synthesize. Current tools lack intelligent Q&A that retrieves from the full vault.

## 2. Goals

- Build a 2nd brain: users ask questions, get answers grounded in their existing knowledge base
- Support bilingual input/output: auto-detect language, respond in kind (zh-hans/zh-hant/en)
- Demo-ready PoC on Linux or Mac for potential customer conversations

## 3. Designer Profile

This section provides context for AI-assisted development.

- Power Linux user (Arch)
- Python and bash preferred
- Comfortable with command line
- Sole builder: develop, operate, and maintain this project

## 4. Design Philosophy

- Design first before writing code
- Think and build standards and strategy first
- Linux and open source stack
- Documentation: all docs in markdown, document everything
- Use plantuml or mindmap for architecture diagrams and workflow logic
- Start simple with PoC, iterate in 2-3 milestones

## 5. Environment & Constraints

- Platform: Linux only
- AI model: ChatGPT for M1 (PoC), local LLM after M1
- Bilingual support: auto-detect input language, respond in same language

## 6. Current State

- Obsidian installed and configured
- Plugins installed: dataview, smart connections
- 300+ notes created over past years
- Embedding: use Obsidian's default embedding model for PoC (Smart Connections plugin default)

## 7. Architecture

*To be added: system overview diagram in plantuml*

```
[ Obsidian Vault ] --> [ Smart Connections (embedding) ] --> [ ChatGPT API (M1) / Local LLM (M2) ]
```

## 8. Tech Stack

| Component | M1 (PoC) | M2 (Post-PoC) |
|---|---|---|
| Knowledge base | Obsidian vault | Obsidian vault |
| Embedding | Smart Connections default | TBD |
| Retrieval | Smart Connections plugin | TBD |
| LLM | ChatGPT API | Local LLM |
| Interface | Smart Connections chat | TBD |
| Storage | None | Persistent conversation log |

## 9. Milestones

### M1: PoC
- Configure Smart Connections plugin with default embedding model
- Configure Smart Connections ChatGPT integration
- Bilingual support: auto-detect, respond in kind
- Demo on Linux or Mac

### M2: Post-PoC
- Swap ChatGPT API for local LLM
- Conversation logging and summarization
- Mindmap generation from summaries
- Persistent conversation storage

## 10. Open Questions

- Which local LLM to use for M2?
- How to persist conversations? (SQLite vs markdown files)
- Smart Connections config specifics for bilingual support
