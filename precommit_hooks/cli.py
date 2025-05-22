"""
Command-line interface for precommit-hooks.

This module provides the CLI functionality using Click.
"""

import subprocess

import click

# if $FIX_MODE; then
#   echo "Fixing formatting..."
#   poetry run black ./
#   poetry run isort ./
#   poetry run ruff check --fix
# else
#   echo "Checking formatting..."
#   black --check .
#   isort --check-only .
#   ruff check .
# fi
#


def run_command(cmd, *options):
    click.echo(f"Running {cmd} ")
    cleaned_options = list(filter(lambda x: x != "", options))
    # click.echo(["poetry", "run", cmd, *options])
    subprocess.run(["poetry", "run", cmd, *cleaned_options])


@click.group()
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command()
@click.option("--fix/--no-fix", "fix")
@click.argument("path", default=".")
def codestyle(fix: bool, path: str):
    click.echo("Running code formatters...")
    run_command("black", path, "" if fix else "--check")
    run_command("isort", path, "" if fix else "--check-only")
    run_command("ruff", "check", path, "--fix" if fix else "")


if __name__ == "__main__":
    cli()
