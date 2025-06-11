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
        # Get the diff of tracked files
        tracked_diff = subprocess.check_output(["git", "diff", "../log_analyzer_project/"], text=True).strip()
        
        # Get list of untracked files
        untracked_files = subprocess.check_output(
            ["git", "ls-files", "--others", "--exclude-standard", "../log_analyzer_project/"],
            text=True
        ).strip().split("\n")
        
        # Get content of untracked files
        untracked_diff = ""
        for file in untracked_files:
            if file:  # Skip empty lines
                try:
                    with open(file, 'r') as f:
                        content = f.read()
                        untracked_diff += f"\n\n--- /dev/null\n+++ {file}\n@@ -0,0 +1 @@\n+{content}"
                except Exception as e:
                    untracked_diff += f"\n\nError reading untracked file {file}: {e}"
        
        return tracked_diff + untracked_diff
    
    except subprocess.CalledProcessError as e:
        return f"Error getting full diff: {e}"

def get_branch_name() -> str:
    try:
        branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True)
        return branch_name.strip()
    except subprocess.CalledProcessError:
        return ""

def get_recent_commits() -> List[str]:
    return """[Example 1 starts]
    chore: Create kanban_mcp package structure
[Example 1 ends]

[Example 2 starts]
    feat: Add initial Kanban MCP files

    - Add DB module
    - Add main application logic
    - Add MCP tools module
    - Add typing models
[Example 2 ends]

[Example 3 starts]
    feat(log_analyzer): Add main log analyzer functionality

    - Create a package structure for the log analyzer
    - Add sample logs to test the log analyzer with
[Example 3 ends]

[Example 4 starts]
    feat(log_analyzer): [Log Analyzer] Add report generation module
[Example 4 ends]

[Example 5 starts]
    feat: Update message generator agent and create judge agent
[Example 5 ends]

[Example 6 starts]
    chore: Extract functions to create git and llm helpers

    - Add README.md
    - Update requirements.txt
[Example 6 ends]
"""
