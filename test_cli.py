#!/usr/bin/env python3
"""
Test script for the precommit-hooks CLI.
"""

from unittest.mock import patch

from click.testing import CliRunner

from src.precommit_hooks import cli


class MockCompletedProcess:
    """Mock for subprocess.CompletedProcess."""

    def __init__(self, returncode=0):
        self.returncode = returncode


def test_codestyle_command():
    """Test the codestyle command with and without the --fix flag."""
    runner = CliRunner()

    # Create a mock for subprocess.run that returns success
    mock_result = MockCompletedProcess(returncode=0)

    # Test without --fix flag
    with patch("subprocess.run", return_value=mock_result):
        result = runner.invoke(cli, ["codestyle"])
        print("Without --fix flag:")
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output}")

        # Verify that the output contains the expected messages
        assert "Running code linters..." in result.output
        assert "Running ruff..." in result.output
        assert "Running black..." in result.output
        assert "Running isort..." in result.output
        assert "All code style checks passed!" in result.output

    # Test with --fix flag
    with patch("subprocess.run", return_value=mock_result):
        result = runner.invoke(cli, ["codestyle", "--fix"])
        print("\nWith --fix flag:")
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output}")

        # Verify that the output contains the expected messages
        assert "Running code linters with auto-fix enabled..." in result.output
        assert "Running ruff..." in result.output
        assert "Running black..." in result.output
        assert "Running isort..." in result.output
        assert "All code style checks passed!" in result.output


if __name__ == "__main__":
    test_codestyle_command()
