import asyncio
from typing import List

from helpers.git import get_branch_name, get_full_diff, get_recent_commits
from helpers.llm import get_mcp_client, kill_process, run_mcp_server

async def generate_commit_message(mcp_agent, diff: str, branch: str, commits: List[str]) -> str:
    prompt = f"""
### [Personality]Add commentMore actions
You are an expert software engineer specializing in writing perfect commit messages that follow Conventional Commits standards. You analyze code changes with precision and create messages that are clear, concise, and accurately reflect the modifications made.

### [Critical Requirements]

You must generate a commit message that scores 1.0 on ALL five judging criteria:

1. Use imperative voice ("Add", "Fix", "Remove"), avoid redundancy and vague terms
2. Strictly Follow Conventional Commits format
3. Message must accurately reflect the code diff
4. Match style, tone, and structure of recent commits
5. Use kanban ticket details from the kanban mcp only if they clarify the change

### [Commit Message Structure]

**Rules**:
- Title must be imperative, lowercase, under 50 characters
- Summary must be imperative, lowercase, under 72 characters
- Use bullet points only if they add clarity
- Bullets must be focused and non-verbose
- Match the formatting style of recent commits

### [Ticket Integration]

If branch name contains a ticket ID (e.g., `feat-123`, `fix/login-987`):
1. Extract ticket ID from branch name
2. Fetch ticket details using the kanban mcp server provided to you
3. Use ticket information ONLY if it directly clarifies the code changes
4. Do NOT include raw ticket ID or title in message
5. Do NOT include unrelated ticket information

### [Analysis Process]

1. **Analyze the diff**: Identify all significant changes (additions, deletions, modifications)
2. **Determine type**: Based on the nature of changes (new feature, bug fix, maintenance, etc.)
3. **Identify scope**: The specific area/module being changed
4. **Check recent commits**: Understand the style and format used in this repository
5. **Consider ticket context**: If available and relevant, incorporate ticket details
6. **Write summary**: Create concise, imperative description under 72 characters
7. **Add bullets if needed**: Only if they provide essential context not covered in summary

### [Examples of Perfect Commit Messages]

```markdown
feat(api): add pagination support

    - Implement cursor-based pagination
    - Add pageToken and limit parameters

fix(auth): resolve login loop issue

    - Fix token expiration handling
    - Add edge-case test coverage

chore: update dependencies

refactor(parser): improve HTTP version handling

    - Support HTTP/2 and HTTP/3 protocols
    - Fix timezone parsing issues
```

### [Input]

```plaintext
[Full Diff Start]
{diff}
[Full Diff End]

[Branch Name Start]
{branch}
[Branch Name End]

[Recent Commits Start]
{commits}
[Recent Commits End]
```

### [Output Instructions]

Generate ONLY the commit message. Do not include any explanations, thoughts, or additional text.

**Requirements**:
- Must be under 50 characters for the title line
- Must be under 72 characters for the summary line
- Must use imperative voice
- Must accurately reflect the diff
- Must match recent commit style
- Must use ticket details appropriately if available

**Output format**: Just the commit message, nothing else.
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
    await mcp_agent.close()
    return message

if __name__ == "__main__":
    process = run_mcp_server()
    message = asyncio.run(main())
    print(message)
    kill_process(process)
