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