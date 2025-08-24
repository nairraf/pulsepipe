import typer
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.live import Live
from rich.spinner import Spinner
from rich.panel import Panel
from rich.console import Console
import time

from pulsepipe.ui.crawlerui import CrawlerUI

app = typer.Typer()


@app.command()
def run(
    source: str = typer.Option("default","--source", help="source to ingest")
):
    with Progress() as progress:
        task = progress.add_task("[green]Downloading...", total=100)

        for i in range(100):
            time.sleep(0.1)
            progress.update(task, advance=1)
    
    typer.echo(f"Ingestion of {source} complete")

@app.command()
def crawl(site: str):
    ui = CrawlerUI()
    ui.start()

    total_links = 0

    for url in range(50):
        latest_url=f"https://some.site/article/{url}"
        total_links += 1
        ui.update(latest_url,url)
        time.sleep(0.1)

    ui.print(f"Crawl Complete. Found {total_links} links")