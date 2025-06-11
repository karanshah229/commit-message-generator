import asyncio
from typing import List

from helpers.git import get_branch_name, get_full_diff, get_recent_commits
from helpers.llm import get_mcp_client

async def generate_commit_message(mcp_agent, diff: str, branch: str, commits: List[str]) -> str:
    prompt = f"""
[Personality]
You are an expert software engineer.
You have to generate a semantic commit message in the Conventional Commits format.

Commit message structure should follow these rules:
1. Be concise, clear, and in plain English.
2. Strictly follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
3. Use verbs like Add instead of Adds, Update instead of Updates, etc.
3. Be strictly relevant to the changes made in the code (i.e., based on the provided diff).
4. Be stylistically and semantically consistent with recent commit messages from the same repository.
5. Do Not include ticket IDs or irrelevant ticket details in the commit message.
6. Use the Kanban MCP server to fetch ticket details if the branch name includes a ticket ID.
   - Include ticket information in the commit message if it directly relates to the code changes.
7. In case the full diff and ticket details are both relevant ensure to give both equal weightage and include them in the commit message.
   
[Branch name including Ticket ID Examples]
    - feat-265
    Here the ticket ID is 265, and the branch name is `feat-265`.

    - chore/999
    Here the ticket ID is 999, and the branch name is `chore/999`.

    - log_analyzer-1310
    Here the ticket ID is 1310, and the branch name is `log_analyzer-1310`.
[Branch name including Ticket ID Examples ends]

[Examples Start]
feat(api): add support for pagination

    - Enables cursor-based pagination for large datasets
    - Adds `pageToken` and `limit` query params to endpoints

fix(auth): resolve login loop issue

    - Fixes token expiration not redirecting to login
    - Adds unit tests for edge-case logouts

chore: update dependencies
[Examples End]

[Input]
    [Full Diff Start]
    {diff}
    [Full Diff End]

    [Branch Name Start]
    {branch}
    [Branch Name End]

    [Recent Commits Start]
    {(chr(10) * 2).join(commits)}
    [Recent Commits End]
[End of Input]

[Output]
Your task is to output a single semantic commit message** that satisfies all the judging criteria above.

Do:
- Output only the final commit message.
- Make sure it is aligned with the code diff and recent commits.
- Use the appropriate `type(scope):` prefix.
- Use a short, meaningful description.

Do Not:
- Output any additional text or explanation.
- Include the Thought or Action taken.

[End of Output]
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
    print(message)
