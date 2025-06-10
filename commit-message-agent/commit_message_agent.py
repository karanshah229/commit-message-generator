import asyncio
from typing import List

from helpers.git import get_branch_name, get_full_diff, get_recent_commits
from helpers.llm import get_mcp_client

async def generate_commit_message(mcp_agent, diff: str, branch: str, commits: List[str]) -> str:
    prompt = f"""
[Personality]
You are an expert software engineer.
You have to generate a semantic commit message in Conventional Commit format.
The commit message should be concise, clear, and follow the Conventional Commits specification.

[Examples Start]
feat(api): add support for pagination

    - Enables cursor-based pagination for large datasets
    - Adds `pageToken` and `limit` query params to endpoints

fix(auth): resolve login loop issue

    - Fixes token expiration not redirecting to login
    - Adds unit tests for edge-case logouts

chore: update dependencies
[Examples End]

You will be provided with the following information to help you generate the commit message:
1. The full diff of the changes.
2. The current branch name.
3. The last few commit messages for reference.
4. Always Use the provided Kanban server to fetch the ticket details from the branch name if ticket ID is present in the branch name.

[Tools]
You also have a Kanban MCP server available. Explore all the tools it provides.
You can use the Kanban MCP server to fetch details about that ticket.

Here is part of the information you need to generate the commit message:
[Full Diff Start]
{diff}
[Full Diff End]

[Branch Name Start]
{branch}
[Branch Name End]

[Recent Commits Start]
{(chr(10) * 2).join(commits)}
[Recent Commits End]

[Output]
Generate a concise and clear commit message based on the above information in the format as specified above.
Do not provide any additional commentary or explanations, just the commit message.
Do not provide the Thought or the Action taken, just the commit message.
"""

    # print(prompt)
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
    return message

if __name__ == "__main__":
    message = asyncio.run(main())
    print("\nSuggested Commit Message:")
    print(message)
