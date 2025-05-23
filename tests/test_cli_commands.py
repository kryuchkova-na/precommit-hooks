#!/usr/bin/env python3
"""
Test script to list all available commands in the CLI.
"""

from click.testing import CliRunner

from precommit_hooks.cli import cli


def test_cli_commands():
    """Test that all expected commands are available in the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    print(f"Exit code: {result.exit_code}")
    print(f"Output: {result.output}")

    # Check if the check_email command is listed
    assert "check-email" in result.output or "check_email" in result.output
