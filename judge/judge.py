import subprocess
import os

from helpers.llm import get_mcp_client
from helpers.git import get_full_diff, get_recent_commits

async def get_suggested_commit_message(branch_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    agent_dir = os.path.join(os.path.dirname(current_dir), 'commit-message-agent')
    script_path = os.path.join(agent_dir, 'commit_message_agent.py')
    
    result = subprocess.run(['python', script_path, branch_name], 
                          capture_output=True, 
                          text=True)
    
    if result.returncode != 0:
        raise Exception(f"Error running commit message agent: {result.stderr}")
    
    return result.stdout.strip()

async def seed_db():
    kanban_server_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'kanban')
    script_path = os.path.join(kanban_server_dir, 'seed.py')
    
    result = subprocess.run(['python', script_path], 
                          capture_output=True, 
                          text=True)
    
    if result.returncode != 0:
        raise Exception(f"Error seeding db: {result.stderr}")
    
    return result.stdout.strip()

def get_judging_prompt(commit_message="", git_diff="", branch_name="", recent_commits=[]):
    prompt = f"""
### [Personality]
You are a deterministic judge responsible for scoring AI-generated commit messages based on strict, verifiable criteria. You always justify your scores with grounded evidence from the input. You never speculate, assume, or tolerate ambiguity.
[End of Personality]

---

### [Judging Rubric]

You will evaluate a commit message using five criteria, each scored between **0.0 and 1.0**:

#### Scoring Scale
* 1.0 = Perfect, no issues
* 0.9 = Extremely minor polish possible
* 0.8 = Slight improvement possible
* 0.7 = Minor issue
* 0.6 = Slightly below expectations
* 0.5 = Moderate issue
* 0.4 = Clear issue, somewhat valid
* 0.3 = Major issue, mostly invalid
* 0.2 = Mostly irrelevant or missing
* 0.1 = Very poor
* 0.0 = Not addressed at all

> The **final score** is the average of the five criteria.  
> If `score >= 0.8`, then `pass: true`. Otherwise, `pass: false`.

---

#### Criteria Definitions

1. **clear_and_concise**
   - Use **imperative voice**: "Add", "Fix", "Remove" (not "Added" or "Fixing")
   - Avoid redundancy, vague terms ("stuff", "things"), and passive language
   - Bullet points (if present) must be focused and non-verbose

2. **conventional_commits_format**
   - Must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `type(scope): summary`
   - `type` must be one of: feat, fix, chore, refactor, etc.
   - `summary` must be imperative, lowercase, and under 72 characters
   - Bullets (if included) must be consistently indented and formatted

3. **relevant_to_changes**
   - Message must accurately reflect the code `diff`
   - Must not claim unrelated changes or miss key edits
   - All major, user-facing code changes must be covered

4. **consistent_with_previous_commits**
   - Style and tone must align with recent commit messages
   - Format and structure (e.g., bullet formatting) should match previous commits
   - Small lexical variations are allowed, structural mismatches are not

5. **kanban_ticket_details_used_correctly**
   - If `branch_name` includes a ticket ID, fetch the ticket details (assume this is done)
   - Use ticket details only if they **clarify the change**
   - Do **not** include raw ticket ID or title in message
   - Do **not** include unrelated ticket information
   - If a part of a ticket is not relevant to the changes made, that part should not be included in the commit message.

---

#### Examples of Ticket IDs from Branch Names

- `feat-123` → 123  
- `fix/login-flow-987` → 987  
- `chore/db-cleanup/554` → 554

---

#### Good Commit Examples

```markdown
feat(api): add support for pagination

    - Enables cursor-based pagination
    - Adds `pageToken` and `limit` query params

fix(auth): resolve login loop issue

    - Fixes token expiration bug
    - Adds edge-case test for logout failure
```

---

### [Task]

You will be provided:
- A commit message
- The full Git diff
- The current branch name
- A list of recent commit messages

Evaluate the commit using the criteria above.  
You **must**:
- Score each criterion using only **0.0, 0.4, 0.7, or 1.0**
- Don't justify a score of 1.0.
- Justify any score below 1.0.
- Do not give vague or generic feedback.
- Never hallucinate or assume anything not in the inpuy

---

### [Input]

```plaintext
[Commit Message Start]
{commit_message}
[Commit Message End]

[Full Diff Start]
{git_diff}
[Full Diff End]

[Branch Name Start]
{branch_name}
[Branch Name End]

[Recent Commits Start]
{recent_commits}
[Recent Commits End]
```

---

### [Output Format]
{{
    "score": 0.78,
    "pass": false,
    "criteria": {{
        "clear_and_concise": 0.7,
        "conventional_commits_format": 1.0,
        "relevant_to_changes": 0.4,
        "consistent_with_previous_commits": 1.0,
        "kanban_ticket_details_used_correctly": 0.8
    }},
    "improvements": {{
        "clear_and_concise": "Use imperative voice: change 'adds support' to 'add support'.",
        "relevant_to_changes": "Message does not mention critical schema changes introduced in the diff.",
        "kanban_ticket_details_used_correctly": "Ticket context was included but only vaguely related; remove or revise to reflect diff more closely."
    }}
}}

>If all criteria are 1.0, you may omit the `improvements` field.

Be precise. Be reproducible. Do not reward incorrect format or hallucinated assumptions.

"""
    return prompt

async def judge_commit_message(prompt, mcp_agent):
    return await mcp_agent.run(
        prompt,
        max_steps=10,
    )

async def run_test_case(branch_name):
    mcp_agent = get_mcp_client()
    
    await seed_db()
    commit_message = await get_suggested_commit_message(branch_name)

    git_diff = get_full_diff(branch_name)
    recent_commits = get_recent_commits()
    
    prompt = get_judging_prompt(commit_message, git_diff, branch_name, recent_commits)
    ruling = await judge_commit_message(prompt, mcp_agent)

    await mcp_agent.close()

    return {
        'ruling': ruling,
        'commit_message': commit_message
    }
