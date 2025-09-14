"""
This module contains the PulsepipeUI class, which provides a user interface
for displaying banners, progress bars, and messages in the terminal using
the rich library and art for ASCII art generation.
"""

from art import text2art
from rich.console import Console
from rich.panel import Panel
from rich.progress import (Progress, SpinnerColumn, TextColumn,
                           TimeElapsedColumn)
from rich.text import Text

class PulsepipeUI:
    """
    PulsepipeUI class provides methods to display banners, progress bars,
    and messages in the terminal using rich library and art for ASCII art generation.
    """

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
        """Displays a banner with ASCII art in the terminal.

        Args:
            title (str, optional): _description_. Defaults to "MODE".
            banner_text (str, optional): _description_. Defaults to "".
            simple (bool, optional): _description_. Defaults to False.
        """
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
        """Starts a progress task with optional progress bar.

        Args:
            description (str): Description of the task.
            total (int, optional): Total number of steps for the task. Defaults to None.
            bar (bool, optional): Whether to show a progress bar. Defaults to False.
        """
        if bar:
            self.progress = Progress()
            self.progress_bar = True

        self.progress.start()
        self.task = self.progress.add_task(description, total=total)

    def task_url_update(self, latest_url: str, count):
        """Updates the progress task with the latest URL and count.

        Args:
            latest_url (str): The latest URL being processed.
            count (int): The count of URLs processed.
        """
        self.progress.update(self.task, description=f"URLs: {count} Last URL: {latest_url}")

    def task_bar_update(self):
        """Advances the progress bar by one step."""
        self.progress.update(self.task, advance=1)

    def task_stop(self):
        """Stops the progress task."""
        self.progress.stop()

    def print(self, message, color="green"):
        """Prints a message to the console with the specified color.

        Args:
            message (str): The message to print.
            color (str, optional): The color of the message. Defaults to "green".
        """
        self.console.print(f"\n[{color}]{message}")
