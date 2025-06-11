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

def switch_branch(branch_name: str) -> bool:
    try:
        subprocess.check_output(["git", "switch", branch_name], text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error switching to branch {branch_name}: {e}")
        return False

def reset_head_by_commits(num_commits: int) -> bool:
    try:
        subprocess.check_output(["git", "reset", "--soft", f"HEAD~{num_commits}"], text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error resetting HEAD by {num_commits} commits: {e}")
        return False

def unstage_all_files() -> bool:
    try:
        subprocess.check_output(["git", "reset", "HEAD"], text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error unstaging all files: {e}")
        return False

def stage_all_files() -> bool:
    try:
        subprocess.check_output(["git", "add", "."], text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error staging all files: {e}")
        return False

def create_commit(message: str) -> bool:
    try:
        status = subprocess.check_output(["git", "status", "--porcelain"], text=True)
        if not status.strip():
            print("No changes to commit")
            return False
            
        # Use -F- to read commit message from stdin
        process = subprocess.Popen(
            ["git", "commit", "-F-"],
            stdin=subprocess.PIPE,
            text=True
        )
        process.communicate(input=message)
        
        if process.returncode == 0:
            return True
        else:
            print(f"Error creating commit: Command failed with return code {process.returncode}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error creating commit: {e}")
        return False
