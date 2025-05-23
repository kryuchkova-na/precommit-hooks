#!/usr/bin/env python3
"""
Test script for the check_email command.
"""

from unittest.mock import patch

from click.testing import CliRunner
from src.precommit_hooks import cli


def test_check_email_command():
    """Test the check_email command."""
    runner = CliRunner()

    # Mock the git config command to return a valid email
    with patch("subprocess.check_output", return_value=b"test@ulta.team\n"):
        result = runner.invoke(cli, ["check-email"])
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output}")

        # Verify that the output contains the expected message
        assert "Email OK: test@ulta.team" in result.output
        # Note: We can't verify the color in this test environment


if __name__ == "__main__":
    test_check_email_command()
