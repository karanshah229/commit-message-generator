git checkout -b feat-311

SCRIPTS_DIR=$(pwd)

mkdir log_analyzer_project && cd log_analyzer_project/

echo '# log-analyzer

A command-line tool to analyze Apache-style web server logs.  
Useful for quickly extracting insights like the most requested endpoints, status code distribution, and traffic patterns.

---

## 📦 Features

-   Parse standard Apache access log files
-   Count most requested endpoints
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
Most Requested Endpoints:
  /index.html    -> 3 hits
  /dashboard     -> 2 hits
  /login         -> 1 hits

```

### 4. Project Structure

```
log_analyzer/
├── log_parser.py      # Reads and parses log lines
├── analyzer.py        # Aggregates insights from parsed logs
├── report.py          # Pretty-prints the results
├── main.py            # CLI entry point
```
' > README.md

echo '192.168.1.1 - - [04/Jun/2025:06:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - - [04/Jun/2025:06:05:32 +0000] "POST /login HTTP/1.1" 302 512
192.168.1.3 - - [04/Jun/2025:07:10:11 +0000] "GET /dashboard HTTP/1.1" 200 2048
192.168.1.1 - - [04/Jun/2025:07:15:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.4 - - [04/Jun/2025:08:01:00 +0000] "GET /dashboard HTTP/1.1" 500 0
192.168.1.5 - - [04/Jun/2025:08:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
' > sample_access.log

echo '[project]
name = "log-analyzer"
version = "0.1.0"
description = "A CLI tool to analyze web server logs"
authors = [{ name = "John Doe", email = "john.doe@example.com" }]
dependencies = []

[project.scripts]
log-analyzer = "log_analyzer.main:main"

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
packages = ["log_analyzer"]
' > pyproject.toml

mkdir log_analyzer && cd log_analyzer/

echo 'def print_endpoint_stats(stats):
    print("Most Requested Endpoints:")
    for endpoint, count in stats:
        print(f"{endpoint}: {count} requests")
' > report.py

echo 'import sys
from log_analyzer.log_parser import read_log_file
from log_analyzer.analyzer import most_requested_endpoints
from log_analyzer.report import print_endpoint_stats

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: log-analyzer <access_log_file>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = list(read_log_file(log_file_path))

    endpoint_stats = most_requested_endpoints(logs)

    print_endpoint_stats(endpoint_stats)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py access.log")
        sys.exit(1)
    main(sys.argv[1])
' > main.py

echo 'import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] \"(?P<method>\S+) (?P<endpoint>\S+) \S+\" (?P<status>\d{3}) (?P<size>\d+)"
)

def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    data["timestamp"] = datetime.strptime(data["timestamp"], "%d/%b/%Y:%H:%M:%S %z")


    return data

def read_log_file(filepath):
    with open(filepath) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                yield parsed
' > log_parser.py

echo 'from collections import Counter

def most_requested_endpoints(logs, top_n=5):
    endpoints = Counter(log["endpoint"] for log in logs)
    return endpoints.most_common(top_n)
' > analyzer.py

touch __init__.py

cd $SCRIPTS_DIR

git add .
git commit -F- << 'EOF'
feat: Create log analyzer project

- Initial commit of log analyzer project
- Application that analyzes apache web server logs and generates the most requested endpoints
EOF
