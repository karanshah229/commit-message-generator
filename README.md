## Problem Statement

### **Objective**

Build an AI Agent that automatically generates semantic commit messages in the Conventional Commit format based on:

-   The diff of changes made
-   The current Git branch name
-   A list of recent commit messages
-   Optional ticket details fetched via a Kanban MCP server

### Output

The commit messages must be:

-   Concise, clear, and meaningful
-   In Conventional Commit format (e.g., feat:, fix:, chore:)
-   Relevance to the diff content
-   Augmented with ticket details if available (based on the branch name)

**Example Output**

```markdown
feat(api): add support for pagination

    - Enables cursor-based pagination for large datasets
    - Adds `pageToken` and `limit` query params to endpoints

fix(auth): resolve login loop issue

    - Fixes token expiration not redirecting to login
    - Adds unit tests for edge-case logouts
```

### **Inputs**

-   diff: Full Git diff of the current working changes.
-   branch_name: Name of the current Git branch.
-   recent_commits: List of recent commit messages in the repository.

You are provided with a **Kanban MCP Server** that’s already set up and integrated into your project. It includes functionality to fetch ticket details and potentially other useful actions related to your workflow.

> _Hint:_ **discover and invoke these capabilities**
