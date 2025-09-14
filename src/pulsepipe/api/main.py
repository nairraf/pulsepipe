from fastapi import FastAPI
#from api.routes import crawler, uploader, manager  # placeholder modules

app = FastAPI(
    title="Pulsepipe API",
    description="Modular RAG pipeline interface for ingestion, retrieval, and embedding",
    version="0.1.0"
)

# Include routers (once defined)
# app.include_router(crawler.router, prefix="/crawl")
# app.include_router(uploader.router, prefix="/upload")
# app.include_router(manager.router, prefix="/manage")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Pulsepipe API is alive"}
