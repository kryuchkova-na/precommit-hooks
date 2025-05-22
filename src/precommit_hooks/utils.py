import subprocess

import click


def run_command(cmd, *options):
    click.echo(f"Running {cmd} ")
    cleaned_options = list(filter(lambda x: x != "", options))
    subprocess.run(["poetry", "run", cmd, *cleaned_options])
