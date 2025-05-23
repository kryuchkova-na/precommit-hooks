import sys

import click

from .commands.check_codestyle import check_codestyle as run_codestyle_check
from .commands.check_email import check_email


@click.group()
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command()
@click.option("--fix/--no-fix", "fix")
@click.argument("paths", nargs=-1)
def check_codestyle(fix: bool, paths: tuple[str]):
    """Check code style using black, isort, and ruff."""
    exit_code = run_codestyle_check(fix, paths)
    sys.exit(exit_code)


@cli.command(name="check-email")
@click.option("--allowed-domain", "-d", "allowed_domain")
def check_email_cmd(allowed_domain):
    """Check if the git committer email is valid."""
    click.echo("Checking if git committer email is valid.")
    email_valid, msg = check_email(allowed_domain=allowed_domain)
    click.echo(
        click.style(msg, fg="green" if email_valid else "red"), err=not email_valid
    )
    if not email_valid:
        sys.exit(1)


if __name__ == "__main__":
    cli()
