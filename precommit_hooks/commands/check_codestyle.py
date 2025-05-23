import subprocess

import click


def run_command(cmd, *options):
    """Run a command with the given options."""
    click.echo("==========")
    click.secho(f"Running {cmd}", fg="cyan", bold=True)
    cleaned_options = list(filter(lambda x: x != "", options))
    result = subprocess.run([cmd, *cleaned_options])
    return result.returncode


def check_codestyle(fix: bool, paths: tuple[str]):
    """Check code style using black, isort, and ruff."""
    click.echo("Running code formatters...")
    exit_code = run_command("black", *paths, "" if fix else "--check")
    exit_code |= run_command("isort", *paths, "" if fix else "--check-only")
    exit_code |= run_command("ruff", "check", *paths, "--fix" if fix else "")

    return exit_code
