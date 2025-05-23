import subprocess


def get_git_config_value(key: str):
    try:
        return subprocess.check_output(["git", "config", key]).decode().strip()
    except subprocess.CalledProcessError:
        return None


def check_email(*, allowed_domain: str) -> (bool, str):
    email = get_git_config_value("user.email")
    if not email:
        return False, "No committer email set (git config user.email)"
    if not email.endswith(f"@{allowed_domain}"):
        return (
            False,
            f"Invalid committer email: {email} (must end with @{allowed_domain})",
        )
    return True, f"Email OK: {email}"
