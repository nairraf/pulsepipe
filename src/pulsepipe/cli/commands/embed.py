import typer


app = typer.Typer()

app.command()
def run(source: str):
    typer.echo(f"embed of {source} complete")