from unittest.mock import patch

from click.testing import CliRunner

from precommit_hooks.cli import cli


def test_check_email_command():
    runner = CliRunner()

    with patch("subprocess.check_output", return_value=b"test@ulta.team\n"):
        result = runner.invoke(cli, ["check-email", "--allowed-domain", "ulta.team"])
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output}")
        assert "Email OK: test@ulta.team" in result.output
