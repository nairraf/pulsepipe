import typer
from pulsepipe.cli.commands import ingest, embed, search, status
from pulsepipe.core.container import bootstrap_container

app = typer.Typer()

container = bootstrap_container()

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
