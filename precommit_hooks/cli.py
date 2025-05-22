"""
Command-line interface for precommit-hooks.

This module provides the CLI functionality using Click.
"""

import click
import subprocess


def run_command(cmd, *options):
    subprocess.run(["poetry", "run", cmd, *options])


@click.group()
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command()
@click.option("--fix", "fix")
@click.argument("path", default=".")
def codestyle(fix: bool, path: str):
    click.echo("Running code formatters...")
    run_command("black", path)


if __name__ == "__main__":
    cli()
