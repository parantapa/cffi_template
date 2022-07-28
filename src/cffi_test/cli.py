"""Hello world command."""

import click
from click import secho

from ._pi import lib

@click.command()
def cli():
    """Print "Hello, world!"."""
    approx_pi = lib.pi_approx(1000)
    secho(f"pi = {approx_pi}", fg="green")

if __name__ == "__main__":
    cli()
