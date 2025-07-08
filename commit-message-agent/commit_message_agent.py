import os
import sys
import asyncio
from typing import List

from helpers.git import get_full_diff, get_recent_commits
from helpers.llm import get_mcp_client, kill_process, run_mcp_server

def load_prompt() -> str:
    """Load the prompt from the prompt.txt file."""
    prompt_path = os.path.join(os.path.dirname(__file__), 'user_prompt.txt')
    with open(prompt_path, 'r') as f:
        return f.read().strip()

async def generate_commit_message(mcp_agent, git_diff: str, branch_name: str, recent_commits: List[str]) -> str:
    prompt_template = load_prompt()
    prompt = prompt_template.format(git_diff=git_diff, branch_name=branch_name, recent_commits=recent_commits)

    response = await mcp_agent.run(
        prompt,
        max_steps=10,
    )

    return response

async def main(branch_name: str) -> str:
    git_diff = get_full_diff(branch_name)
    recent_commits = get_recent_commits()
    mcp_agent = get_mcp_client()

    message = await generate_commit_message(mcp_agent, git_diff, branch_name, recent_commits)
    await mcp_agent.close()
    return message

if __name__ == "__main__":
    if len(sys.argv) > 1:
        branch_name = sys.argv[1]
        process = run_mcp_server()
        message = asyncio.run(main(branch_name))
        print(message)
        kill_process(process)
    else:
        print("Usage: python commit_message_agent.py <branch_name>")
        sys.exit(1)
