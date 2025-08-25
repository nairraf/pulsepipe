from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.console import Console
from rich.panel import Panel
from art import text2art
from rich.text import Text

class PulsepipeUI:
    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TimeElapsedColumn(),
            TextColumn("[progress.description]{task.description}")
        )
        self.progress_bar = False
        self.console = Console()
        self.task = None

    def banner(self, title="MODE", banner_text="", simple=False):
        if simple:
            ascii_art = text2art(text=banner_text, font="fancy102")
            self.console.print(f"[green]{title.upper()}: {ascii_art}")
        else:
            ascii_art = text2art(
                text=banner_text,
                font="graceful" # ogre standard small serifcap graceful fancy12,102,109,136,143,144,146  black_square 
            )
            art_text = Text(ascii_art, style="green")
            self.console.print(Panel(art_text, title=f"{title.upper()}", border_style="dim green"), justify="left")
    
    def task_start(self, description, total=None, bar=False):
        if bar:
            self.progress = Progress()
            self.progress_bar = True
        
        self.progress.start()
        self.task = self.progress.add_task(description, total=total)

    def task_url_update(self, latest_url: str, count):
        self.progress.update(self.task, description=f"URLs: {count} Last URL: {latest_url}")

    def task_bar_update(self):
        self.progress.update(self.task, advance=1)

    def task_stop(self):
        self.progress.stop()

    def print(self, message, color="green"):
        self.console.print(f"\n[{color}]{message}")