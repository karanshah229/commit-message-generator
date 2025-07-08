import os
from typing import List

def get_full_diff(branch_name) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    setup_dir = os.path.join(script_dir, '..', '..', 'setup')
    file_path = os.path.join(setup_dir, f'{branch_name}.txt')
    
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return f"Error: File {file_path} not found"
    except Exception as e:
        return f"Error reading file {file_path}: {e}"

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
