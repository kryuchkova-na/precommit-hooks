import sys
import subprocess

import click

from precommit_hooks.commands.check_email import check_email


def run_command(cmd, *options):
    click.echo(f"Running {cmd}")
    cleaned_options = list(filter(lambda x: x != "", options))
    return subprocess.run(["poetry", "run", cmd, *cleaned_options])


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
    click.echo(f"Paths passed: {paths}")
    result = run_command("black", *paths, "" if fix else "--check")
    exit_code = result.returncode
    # exit_code |= run_command("isort", *paths, "" if fix else "--check-only")
    # exit_code |= run_command("ruff", "check", *paths, "--fix" if fix else "")

    if exit_code == 1:
        sys.exit(1)


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
