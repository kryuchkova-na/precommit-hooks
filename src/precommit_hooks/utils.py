import subprocess

import click


def run_command(cmd, *options):
    click.echo(f"Running {cmd} with {options}")
    cleaned_options = list(filter(lambda x: x != "", options))
    result = subprocess.run(["poetry", "run", cmd, *cleaned_options])
    return result.returncode