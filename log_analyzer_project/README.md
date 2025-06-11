# log-analyzer

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
```
