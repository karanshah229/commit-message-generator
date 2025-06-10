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
        # Fetch files
        unstaged_file_names = subprocess.check_output(["git", "ls-files", "-m"], text=True).splitlines()
        staged_file_names = subprocess.check_output(["git", "diff", "--name-only", "--cached"], text=True).splitlines()
        untracked_files = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], text=True).splitlines()
        
        # Filter files
        exclude_files = ["commit_message_agent.py", "judge.py"]
        filtered_unstaged = [str(f) for f in unstaged_file_names if not is_file_ignore_by_git(f) and f not in exclude_files]
        filtered_staged = [f for f in staged_file_names if not is_file_ignore_by_git(f) and f not in exclude_files]
        filtered_untracked = [f for f in untracked_files if not is_file_ignore_by_git(f) and f not in exclude_files]

        if not (filtered_unstaged or filtered_staged or filtered_untracked):
            return "No relevant file changes detected."

        # Get diff of filtered files
        unstaged_files_diff = subprocess.check_output(["git", "diff"] + filtered_unstaged, text=True).strip() if filtered_unstaged else ""
        staged_files_diff = subprocess.check_output(["git", "diff", "--cached"] + filtered_staged, text=True).strip() if filtered_staged else ""
        
        # For untracked files, compare against /dev/null
        untracked_files_diff = ""
        if filtered_untracked:
            for file in filtered_untracked:
                try:
                    file_diff = subprocess.check_output(["git", "diff", "--no-index", "/dev/null", file], text=True).strip()
                    untracked_files_diff += f"\n\n=== {file} ===\n{file_diff}"
                except subprocess.CalledProcessError as e:
                    # git diff --no-index returns 1 even on success, so we need to check the output
                    if e.output:
                        untracked_files_diff += f"\n\n=== {file} ===\n{e.output}"
        
        diff = (unstaged_files_diff + "\n" + staged_files_diff + untracked_files_diff).strip()

        return diff
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