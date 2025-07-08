import asyncio
from typing import List
import os

from helpers.git import get_branch_name, get_full_diff, get_recent_commits
from helpers.llm import get_mcp_client, kill_process, run_mcp_server

def load_prompt() -> str:
    """Load the prompt from the prompt.txt file."""
    prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.txt')
    with open(prompt_path, 'r') as f:
        return f.read().strip()

async def generate_commit_message(mcp_agent, diff: str, branch: str, commits: List[str]) -> str:
    prompt_template = load_prompt()
    prompt = prompt_template.format(diff=diff, branch=branch, commits=commits)

    response = await mcp_agent.run(
        prompt,
        max_steps=10,
    )

    return response

async def main():
    diff = get_full_diff()
    branch = get_branch_name()
    commits = get_recent_commits()
    mcp_agent = get_mcp_client()

    message = await generate_commit_message(mcp_agent, diff, branch, commits)
    await mcp_agent.close()
    return message

if __name__ == "__main__":
    process = run_mcp_server()
    message = asyncio.run(main())
    print(message)
    kill_process(process)
