# pulsepipe

```python
python -m pulsepipe <commands> <subcommand> <options>
```

## main CLI commands /  pulsepipe "modes"

### ingest
ingest *source* *subcommand*

```mermaid
flowchart TD
    subgraph CLI Layer
        A["pulsepipe ingest web download"] --> B["IngestManager.run()"]
        C["pulsepipe ingest local scan"] --> B
    end

    subgraph Internal Layer
        B --> D[WebIngestor]
        B --> E[LocalIngestor]

        D --> F[SiteConfig]
        D --> G[Page]
        E --> G
    end
```

### embed

embed *source* *subcommands

```mermaid
flowchart TD
    subgraph CLI Layer
        A["pulsepipe embed web"] --> B["EmbedManager.run()"]
        A2["pulsepipe embed local"] --> B
    end

    subgraph Internal Layer
        B --> C[ContentLoader]
        C --> D[SmartChunker]
        D --> E[Embedder]
        E --> F[VectorStore]
    end

    C --> G[FileTypeDetector]
    D --> H[ChunkStrategy]
```

## IngestManager

```mermaid
---
title: pulsepipe.ingest class diagram
---
classDiagram

    class IngestManager {
        +run(source: str, subcommand: str, options: dict)
    }

    class WebIngestor {
        +sitelist()
        +addsite(config: SiteConfig)
        +urldiscover(url: str)
        +download()
    }

    class LocalIngestor {
        +scan(path: str)
        +index(file: str)
    }

    class SiteConfig {
        +base_url: str
        +selectors: dict
    }

    class Page {
        +title: str
        +url: str
        +hash: str
        +content: str
    }
    
    IngestManager --> WebIngestor : if source == "web"
    IngestManager --> LocalIngestor : if source == "local"
    WebIngestor --> SiteConfig
    WebIngestor --> Page
    LocalIngestor --> Page


```

## new architecture

### Project Structure

```
src/
├── pulsepipe/                      # Root package
│   ├── __init__.py
│   │
│   ├── cli/                        # Typer CLI app
│   │   ├── __init__.py
│   │   ├── main.py                 # CLI entry point
│   │   ├── ingest/                 # CLI subcommand module
│   │   │   ├── __init__.py
│   │   │   ├── commands.py
│   │   │   └── helpers.py
│   │   ├── memory/
│   │   ├── model/
│   │   └── design/
│   │
│   ├── api/                        # FastAPI app
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── dependencies.py         # Wired adapters for FastAPI
│   │   ├── ingest/                 # API route module
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   └── schemas.py
│   │   ├── memory/
│   │   ├── model/
│   │   └── design/
│   │
│   ├── core/                       # Shared logic (used by CLI + API)
│   │   ├── __init__.py
│   │   ├── ingest.py
│   │   ├── memory.py
│   │   ├── model.py
│   │   ├── design.py
│   │   ├── config.py               # Central config loader
│   │   └── container.py            # Wired DI container bootstrap
│   │
│   ├── crawler/                    # Pulsepipe ingestion tools
│   │   ├── __init__.py
│   │   ├── pulsepipe.py            # Entry point for crawling workflows
│   │   ├── page.py                 # Page object: HTML, markdown, image URLs
│   │   ├── extractor.py            # HTML → Markdown + image URL extraction 
│   │   ├── storage.py              # SQLite interface
│   │   ├── transformers.py
│   │   └── filetypes/
│   │       ├── markdown.py
│   │       ├── code.py
│   │       └── pdf.py
│   │
│   ├── db/                         # Memory + vector store layer
│   │   ├── __init__.py
│   │   ├── qdrant.py
│   │   ├── mem0.py
│   │   ├── schema.py
│   │   └── cache.py
│   │
│   ├── agents/                     # Optional: agent personas or plugins
│   │   ├── __init__.py
│   │   ├── planner.py
│   │   ├── executor.py
│   │   └── persona/
│   │       ├── designer.py
│   │       ├── researcher.py
│   │       └── coder.py
│   │
│   ├── tests/                      # Test suite
│   │   ├── __init__.py
│   │   ├── conftest.py             # Pytest fixtures
│   │   ├── test_core/
│   │   │   ├── test_memory.py
│   │   │   ├── test_ingest.py
│   │   ├── test_cli/
│   │   │   ├── test_commands.py
│   │   ├── test_api/
│   │   │   ├── test_routes.py
│   │   └── mocks/
│   │       ├── mock_qdrant.py
│   │       └── mock_embedder.py
│   │
│   └── __main__.py                 # Entry point for `python -m pulsepipe`
```

### Class Graph

```mermaid
classDiagram
  %% Core Services
  class MemoryService {
    - QdrantClient qdrant
    - Embedder embedder
    + search(query, session_id) dict
    + format_results(results) dict
    <<service>>
  }

  class ModelRunner {
    - runner_type
    + run(prompt) str
    + get_available_models() list
    <<service>>
  }

  class IngestPipeline {
    - transformers
    + ingest_file(path) dict
    + extract_chunks(text) list
    <<service>>
  }

  class Embedder {
    + embed(text) list
    + normalize(text) str
    <<static>>
  }

  %% CLI Layer
  class CLI_Main {
    + Typer app
    <<entrypoint>>
  }

  class CLI_MemoryCommands {
    + search_memory(query, session_id)
    <<cli>>
  }

  %% API Layer
  class API_Main {
    + FastAPI app
    <<entrypoint>>
  }

  class API_MemoryRoutes {
    + POST /search
    <<api>>
  }

  class APIDependencies {
    + get_memory_service() MemoryService
    <<adapter>>
  }

  %% DI Container
  class WiredContainer {
    + register_factory(service, factory)
    + get(service) instance
    <<container>>
  }

  %% Relationships
  CLI_MemoryCommands --> MemoryService
  API_MemoryRoutes --> APIDependencies
  APIDependencies --> WiredContainer
  WiredContainer --> MemoryService
  WiredContainer --> ModelRunner
  WiredContainer --> IngestPipeline
  MemoryService --> QdrantClient
  MemoryService --> Embedder
  IngestPipeline --> transformers


```