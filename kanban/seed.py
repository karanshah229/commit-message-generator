from db import get_db_connection, init_db


def seed_db():
    try:
        init_db()
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM tickets WHERE id IN (311,317,359,452)")

            tickets = [
                (
                    311,
                    "Create log analyzer project",
                    """**Task:**
Design and implement a command-line tool to analyze Apache-style web server logs.
Useful for quickly extracting insights like the most requested endpoints, status code distribution, and traffic patterns.

**Technical Details:**  
- Use Python 3.8+ with type hints for better code maintainability
- Implement as a modular package with clear separation of concerns:
  - Log parser module for different log formats
  - Analysis module for various metrics
  - CLI interface module
- Include proper error handling and logging

**Features:**
- Parse Apache HTTP server logs
- Calculate most requested endpoints (top N)

**Acceptance Criteria:**  
- Successfully parse Apache HTTP server logs in both Common and Combined formats
- Generate accurate statistics for all specified metrics
- CLI tool accepts standard input and file input
- Documentation includes:
  - Installation instructions
  - Usage examples
  - API reference
  - Contributing guidelines
""",
                    "in_progress",
                ),
                (
                    317,
                    "Add status code distribution feature",
                    """**Task:**  
Add a feature to Analyze the status code distribution (2xx, 3xx, 4xx, 5xx).

**Features:**
- Calculate status code distribution:
  - Count occurrences of each HTTP status code
  - Group status codes by category (2xx, 3xx, 4xx, 5xx)
  - Display distribution as percentage of total requests

**Acceptance Criteria:**  
- Status code distribution is calculated correctly
- Print the status code distribution
""",
                    "in_progress",
                ),
                (
                    359,
                    "Bug: Log parser logic",
                    """**Bug:**  
1. Only HTTP/1.1 logs are being parsed currently. Other HTTP versions (like HTTP/2) are not handled correctly.
2. Different timezone formats are not being parsed correctly, leading to incorrect timestamps in the output.

**Acceptance Criteria:**  
- Log parser should handle all HTTP versions correctly.
- Timezone formats should be parsed correctly, ensuring timestamps are accurate in the output.
""",
                    "in_progress",
                ),
                (
                    452,
                    "Add support for advanced traffic filtering and export",
                    """**Task:**  
Add support for analyzing hourly traffic trends, filtering logs by time range, displaying only error responses, and exporting results.

**Features:**
- Show hourly traffic trends:
  - Aggregate requests by hour
- Filter logs by time range:
  - Allow start and end time as parameters
  - Validate time range input
  - Exclude logs outside range
- Show only error responses:
  - Filter logs to include only 4xx and 5xx responses
- Export results:
  - Allow export to JSON or CSV formats
  - User can choose output format via CLI flag

**Acceptance Criteria:**  
- Hourly trends are displayed correctly
- Filters for time range and error responses work independently and together
- JSON and CSV exports include filtered results in correct format
""",
    "todo",
),
            ]

            for id, title, description, status in tickets:
                cursor.execute(
                    "INSERT INTO tickets (id, title, description, status) VALUES (?, ?, ?, ?)",
                    (id, title, description, status),
                )

            conn.commit()
            print("Database seeded successfully with 4 detailed developer tickets.")

        except Exception as e:
            conn.rollback()
            print(f"Error while seeding database: {str(e)}")
            raise

        finally:
            conn.close()

    except Exception as e:
        print(f"Failed to initialize database or establish connection: {str(e)}")
        raise


if __name__ == "__main__":
    try:
        seed_db()
    except Exception as e:
        print(f"Failed to seed database: {str(e)}")
        exit(1)
