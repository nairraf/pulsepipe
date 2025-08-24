from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.console import Console

class CrawlerUI:
    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TimeElapsedColumn(),
            TextColumn("[progress.description]{task.description}")
        )
        self.console = Console()
        self.console.print("\n\n[green]Crawler Mode\n")
        self.task = None

    def start(self, description="Crawling site...."):
        self.progress.start()
        self.task = self.progress.add_task(description, total=None)

    def update(self, latest_url: str, count):
        self.progress.update(self.task, description=f"URLs: {count} Last URL: {latest_url}")

    def stop(self):
        self.progress.stop()

    def print(self, message, color="green"):
        self.console.print(f"\n[{color}]{message}")