import sys

import click

from precommit_hooks.commands.check_email import check_email
from precommit_hooks.utils import run_command


@click.group()
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command()
@click.option("--fix/--no-fix", "fix")
@click.argument("paths", nargs=-1)
def check_codestyle(fix: bool, paths: tuple[str]):
    click.echo("Running code formatters...")
    sys.exit(1)
    exit_code = 0
    exit_code |= run_command("black", *paths, "" if fix else "--check")
    exit_code |= run_command("isort", *paths, "" if fix else "--check-only")
    exit_code |= run_command("ruff", "check", *paths, "--fix" if fix else "")



@cli.command(name="check-email")
@click.argument("paths", nargs=-1)
def check_email_cmd(paths):
    """Check if the git committer email is valid."""
    click.echo("Checking if git committer email is valid.")
    email_valid, msg = check_email()
    click.echo(
        click.style(msg, fg="green" if email_valid else "red"), err=not email_valid
    )
    if not email_valid:
        sys.exit(1)


if __name__ == "__main__":
    cli()
