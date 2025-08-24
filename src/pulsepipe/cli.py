import typer
from pulsepipe.commands import ingest, embed, search, status

app = typer.Typer()

app.add_typer(
    ingest.app, 
    name="ingest", 
    help="Ingest Mode to ingest content"
)

app.add_typer(
    embed.app,
    name="embed",
    help="embed mode to process embeddings"    
)

app.add_typer(
    search.app,
    name="search",
    help="searches stuff"
)

app.add_typer(
    status.app,
    name="status",
    help="returns the current status"
)
