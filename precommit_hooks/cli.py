import click

from precommit_hooks.utils import run_command


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
