# AI Agent: Automatic Commit Message Generator

## The Challenge

You need to create an AI agent that analyzes code changes and suggests a commit message in the Conventional Commit format.

### Inputs

Your agent will have access to:

-   The `diff` of staged changes.
-   The current Git `branch name`.
-   A list of recent commit messages from the repository.

### Output Requirements

The generated commit messages must be:

-   **Concise and Clear**: Easy to understand at a glance.
-   **Formatted Correctly**: Following the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).
-   **Relevant**: The message should accurately reflect the changes in the diff.
-   **Context-Aware**: If the branch name contains a ticket ID (e.g., `feature/TICKET-123-new-auth-flow`), the agent should use this information to enrich the commit message.

**Example of a great commit message:**

```markdown
feat(api): add support for pagination

-   Enables cursor-based pagination for large datasets
-   Adds `pageToken` and `limit` query params to endpoints
```

## Tools at Your Disposal

We have provided a Kanban MCP server that is already integrated into your project.
You can use it to fetch details about tickets, which can provide valuable context for your commit messages.
The code to create the tools for the kanban MCP server are not written and you have to write those.

## Evaluation

Your solution will be evaluated based on the following criteria:

-   **Correctness**: The agent consistently produces valid Conventional Commit messages.
-   **Relevance**: The messages accurately describe the code changes.
-   **Tool Integration**: The agent correctly fetches and uses information from the Kanban server when a ticket ID is present in the branch name.
-   **Code Quality**: The code is well-structured, readable, and maintainable.
