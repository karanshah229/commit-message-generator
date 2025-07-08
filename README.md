# Automatic Commit Message Generator

## What You'll Build

Your AI agent will analyze code changes and generate commit messages following the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).

## Inputs

Your agent will have access to:

-   **Git diff**: The staged changes in your repository
-   **Branch name**: The current Git branch you're working on
-   **Recent commits**: A list of previous commit messages for context
-   **Kanban integration**: A pre-configured MCP server to fetch ticket details

## Tools You Can Use

-   **Kanban MCP Server**: Already integrated into your project. You can fetch the ticket details using the tools provided by this server.

> Note: You need to write the code that exposes the tools from the MCP server. See kanban/main.py

## Requirements

Your generated commit messages must be:

-   **Concise and Clear**: Easy to understand at a glance
-   **Correctly Formatted**: Follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/)
-   **Accurate**: Reflect the actual changes in your code
-   **Consistent**: Match the tone and style of previous commits
-   **Context-Aware**: Use ticket information when available (e.g., from branch names like `feature/TICKET-123-new-auth-flow`)

## Example

Here's what a good commit message looks like:

```markdown
feat(api): add support for pagination

-   Enables cursor-based pagination for large datasets
-   Adds `pageToken` and `limit` query params to endpoints
```

## Evaluation Criteria

Your solution will be evaluated on:

-   **Correctness**: Produces valid Conventional Commit messages
-   **Relevance**: Messages accurately describe the code changes
-   **Consistency**: Matches the style of previous commits
-   **Tool Integration**: Properly uses Kanban server when ticket IDs are present
-   **Code Quality**: Well-structured, readable, and maintainable code
