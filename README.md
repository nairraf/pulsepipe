# Pulsepipe

**Pulsepipe** is a lean, developer-grade Retrieval-Augmented Generation (RAG) pipeline built for speed, modularity, and precision. Designed to ingest, embed, and retrieve markdown and code-based knowledge at scale, Pulsepipe gives you full control over your assistant's brain — from crawling to context injection.

## 🚀 Features

- ⚡ High-performance vector search with Qdrant
- 🧠 Local embeddings via `nomic-embed-text-v1.5`
- 🕸️ Smart web crawler with URL normalization and version filtering
- 🗃️ SQLite-backed corpus tracking with delta detection
- 🔍 FastAPI-powered retrieval API
- 💬 OpenWebUI integration for chat-based querying
- 🔄 Modular architecture for easy swapping of LLMs, embedders, and stores

## 🧱 Stack

- Python 3.11+
- Docker + Docker Compose
- Qdrant (vector store)
- OpenWebUI (chat front-end)
- LM Studio or Ollama (local LLM host)
- FastAPI (retrieval backend)
- SQLite (corpus management)

## 📦 Getting Started

```bash
git clone https://github.com/nairraf/pulsepipe.git
cd pulsepipe
docker compose up -d
