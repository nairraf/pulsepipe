import typer
import time
from pulsepipe.cli.ui.pulsepipeui import PulsepipeUI

app = typer.Typer()


@app.command()
def run(
    source: str = typer.Option("default","--source", help="source to ingest")
):
    ui = PulsepipeUI()
    ui.banner(banner_text="Downloader", simple=True)
    ui.task_start(description="downloader", total=100, bar=True)
    for i in range(100):
        time.sleep(0.1)
        ui.task_bar_update()
    ui.print(f"Download Complete")

@app.command()
def crawl(site: str):
    ui = PulsepipeUI()
    ui.banner(banner_text="Crawler", simple=True)
    ui.task_start(description="Crawler...")

    total_links = 0

    for url in range(50):
        latest_url=f"https://some.site/article/{url}"
        total_links += 1
        ui.task_url_update(latest_url,url)
        time.sleep(0.1)

    ui.print(f"Crawl Complete. Found {total_links} links")