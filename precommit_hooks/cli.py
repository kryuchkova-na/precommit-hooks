import sys

import click

from precommit_hooks.commands.check_branch import check_branch
from precommit_hooks.commands.check_codestyle import check_codestyle
from precommit_hooks.commands.check_email import check_email


@click.group(name="precommit-hooks")
@click.version_option()
def cli():
    """precommit-hooks: A collection of pre-commit hooks for code quality."""
    pass


@cli.command(name="check-codestyle")
@click.option("--fix/--no-fix", "fix")
@click.argument("paths", nargs=-1)
def check_codestyle_cmd(fix: bool, paths: tuple[str]):
    """Check code style using black, isort, and ruff."""
    exit_code = check_codestyle(fix, paths)
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


@cli.command(name="check-branch")
@click.option("--allow-main/--no-allow-main", "allow_main")
def check_branch_cmd(allow_main):
    branch_valid, msg = check_branch(allow_main=allow_main)
    click.echo(
        click.style(msg, fg="green" if branch_valid else "red"), err=not branch_valid
    )
    if not branch_valid:
        sys.exit(1)


if __name__ == "__main__":
    cli()
