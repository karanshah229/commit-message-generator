git branch -D feat-317
git checkout -b feat-317

SCRIPTS_DIR=$(pwd)

cd log_analyzer_project/

echo '# log-analyzer

A command-line tool to analyze Apache-style web server logs.  
Useful for quickly extracting insights like the most requested endpoints, status code distribution, and traffic patterns.

---

## 📦 Features

-   Parse standard Apache access log files
-   Count most requested endpoints
-   Analyze status code distribution (2xx, 3xx, 4xx, 5xx)
-   Easily extensible as a Python module

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer
```

### 2. Create virtual environment and install dependencies

python3 -m venv .venv
source .venv/bin/activate
pip install -e .

### 3. Usage

log-analyzer <path_to_access_log_file>

Example

> log-analyzer sample_access.log

#### Sample Log Format

> 192.168.1.1 - - [04/Jun/2025:06:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024

#### Sample Output

```
Top 10 Endpoints:
  /index.html    -> 3 hits
  /dashboard     -> 2 hits
  /login         -> 1 hits

Status Codes:
  200 -> 4
  302 -> 1
  500 -> 1

```

### 4. Project Structure

```
log_analyzer/
├── log_parser.py      # Reads and parses log lines
├── analyzer.py        # Aggregates insights from parsed logs
├── report.py          # Pretty-prints the results
├── main.py            # CLI entry point
```' > README.md

cd log_analyzer/

echo '
from collections import Counter

def most_requested_endpoints(logs, top_n=5):
    endpoints = Counter(log["endpoint"] for log in logs)
    return endpoints.most_common(top_n)

def status_code_distribution(logs):
    codes = Counter(log["status"] for log in logs)
    return dict(codes)
' > analyzer.py

echo 'import sys
from log_analyzer.log_parser import read_log_file
from log_analyzer.analyzer import most_requested_endpoints, status_code_distribution
from log_analyzer.report import print_endpoint_stats, print_status_codes

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: log-analyzer <access_log_file>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = list(read_log_file(log_file_path))

    endpoint_stats = most_requested_endpoints(logs)
    status_codes = status_code_distribution(logs)

    print_endpoint_stats(endpoint_stats)
    print_status_codes(status_codes)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py access.log")
        sys.exit(1)
    main(sys.argv[1])
' > main.py

echo 'def print_endpoint_stats(stats):
    print("Most Requested Endpoints:")
    for endpoint, count in stats:
        print(f"{endpoint}: {count} requests")

def print_status_codes(stats):
    print("\nStatus Code Distribution:")
    for code, count in stats.items():
        print(f"{code}: {count}")
' > report.py

cd $SCRIPTS_DIR

git add .
git commit -F- << 'EOF'
feat: Add status code distribution feature

- Analyzer module updated to include a method for calculating the distribution of HTTP status codes.
- Report module updated to print the status code distribution.
EOF

git push -d origin feat-317 || true
git push -u origin feat-317 -f