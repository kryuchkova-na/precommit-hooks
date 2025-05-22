"""
Command-line interface for precommit-hooks.

This module provides the CLI functionality using Click.
"""

import click


@click.group()
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command()
@click.option('--fix', 'fix')
def check_codestyle(fix):
    """Run code formatters (black, isort)."""
    click.echo("Running code formatters...")
    # Implementation will go here


if __name__ == "__main__":
    cli()