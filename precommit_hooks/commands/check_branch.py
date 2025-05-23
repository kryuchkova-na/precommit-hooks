import subprocess


def get_current_branch():
    """Get the current git branch name."""
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .decode()
            .strip()
        )
    except subprocess.CalledProcessError:
        return None


def check_branch(*, allowed_prefixes=None, allow_main=False) -> (bool, str):
    """Check if the branch name starts with one of the allowed prefixes."""
    if allowed_prefixes is None:
        allowed_prefixes = ["hotfix/", "fix/", "feature/", "inf/", "test", "main"]

    prefixes_str = ", ".join(f"'{prefix}'" for prefix in allowed_prefixes)

    branch = get_current_branch()

    if branch == "main" and not allow_main:
        return False, (
            "Direct commits to 'main' are not allowed by default.\n"
            f"Allowed branch prefixes: {prefixes_str}\n"
            "If you know what you're doing, remove or disable this check explicitly in .pre-commit-config.yaml."
        )

    if not branch:
        return False, "Failed to get current branch name"

    for prefix in allowed_prefixes:
        if branch.startswith(prefix):
            return True, f"Branch name OK: {branch}"

    return (
        False,
        f"Invalid branch name: {branch} (must start with one of: {prefixes_str})",
    )
