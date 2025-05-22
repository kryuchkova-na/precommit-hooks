"""
Entry point for direct execution of the package.

This allows running the package with `python -m precommit_hooks`.
"""

from precommit_hooks.cli import cli

if __name__ == "__main__":
    cli()
