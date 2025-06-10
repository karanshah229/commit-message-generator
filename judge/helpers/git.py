import subprocess
from typing import List

def is_file_ignore_by_git(filename: str) -> bool:
    try:
        subprocess.check_output(["git", "check-ignore", filename], text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def get_full_diff() -> str:
    try:
        return subprocess.check_output(["git", "diff", "../log_analyzer_project/"], text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error getting full diff: {e}"

def get_branch_name() -> str:
    try:
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True)
        return branch_name.strip()
    except subprocess.CalledProcessError:
        return ""

def get_recent_commits(limit: int = 5) -> List[str]:
    try:
        commits = subprocess.check_output(["git", "log", f"-n{limit}", "--pretty=format:%s"], text=True)
        return commits.strip().split("\n")
    except subprocess.CalledProcessError:
        return []