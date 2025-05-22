import subprocess


ALLOWED_EMAIL_DOMAIN = "ulta.team"


def get_git_config_value(key: str):
    try:
        return subprocess.check_output(["git", "config", key]).decode().strip()
    except subprocess.CalledProcessError:
        return None


def check_email() -> (bool, str):
    email = get_git_config_value("user.email")
    if not email:
        return False, "No committer email set (git config user.email)"
    if not email.endswith(f"@{ALLOWED_EMAIL_DOMAIN}"):
        return False, f"Invalid committer email: {email} (must end with @{ALLOWED_EMAIL_DOMAIN})"
    return True, f"Email OK: {email}"
