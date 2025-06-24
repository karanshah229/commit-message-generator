git branch -D feat-452 || true
git checkout -b feat-452

SCRIPTS_DIR=$(pwd)

cd log_analyzer_project/

echo '# log-analyzer

A command-line tool to analyze Apache-style web server logs.  
Useful for quickly extracting insights like the most requested endpoints, status code distribution, traffic patterns, and more.

---

## 📦 Features

-   ✅ Parse standard Apache access log files
-   📊 Count most requested endpoints
-   🧾 Analyze status code distribution (2xx, 3xx, 4xx, 5xx)
-   ⏰ Show hourly traffic trends
-   🔍 Filter by time range
-   ❗ Show only error responses (4xx/5xx)
-   📤 Export results to JSON or CSV
-   🧱 Easily extensible as a Python module

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Usage

**Basic Example**

```bash
log-analyzer sample_access.log
```

**Advanced Examples**

-   Top 5 endpoints and IPs:

```bash
log-analyzer sample_access.log --top 5
```

-   Filter logs between 6 AM and 12 PM:

```bash
log-analyzer sample_access.log --start "2025-06-04T06:00:00" --end "2025-06-04T12:00:00"
```

-   Show only error logs (4xx and 5xx):

```bash
log-analyzer sample_access.log --errors-only
```

-   Export analysis to CSV:

```bash
log-analyzer sample_access.log --export csv
```

### 4. Sample Log Format

```bash
192.168.1.1 - - [04/Jun/2025:06:00:01 +0000] "GET /index.html HTTP/1.1" 200 **1024**
```

### 5. Sample Output

```bash
Top 10 Endpoints:
  /index.html    -> 3 hits
  /dashboard     -> 2 hits
  /login         -> 1 hits

Status Codes:
  200 -> 4
  302 -> 1
  500 -> 1

Traffic per Hour:
  06 -> 2 requests
  07 -> 2 requests
  08 -> 2 requests

Top IP Addresses:
  192.168.1.1     -> 4 hits
  192.168.1.2     -> 2 hits
```
' > README.md

echo '192.168.1.1 - - [04/Jun/2025:06:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - - [04/Jun/2025:06:05:32 +0000] "POST /login HTTP/1.1" 302 512
192.168.1.13 - - [04/Jun/2025:10:30:19 +0000] "POST /api/comments HTTP/1.1" 201 768
192.168.1.3 - - [04/Jun/2025:07:10:11 +0000] "GET /dashboard HTTP/1.1" 200 2048
192.168.1.1 - - [04/Jun/2025:07:15:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.4 - - [04/Jun/2025:08:01:00 +0000] "GET /dashboard HTTP/1.1" 500 0
192.168.1.5 - - [04/Jun/2025:08:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.6 - - [04/Jun/2025:08:45:12 +0000] "GET /api/users HTTP/1.1" 200 1536
192.168.1.7 - - [04/Jun/2025:09:01:33 +0000] "POST /api/auth HTTP/1.1" 401 256
192.168.1.8 - - [04/Jun/2025:09:15:45 +0000] "GET /products HTTP/1.1" 200 3072
192.168.1.9 - - [04/Jun/2025:09:30:22 +0000] "PUT /api/users/123 HTTP/1.1" 204 0
192.168.1.10 - - [04/Jun/2025:09:45:18 +0000] "GET /images/logo.png HTTP/1.1" 200 5120
192.168.1.11 - - [04/Jun/2025:10:00:05 +0000] "DELETE /api/posts/456 HTTP/1.1" 200 0
192.168.1.12 - - [04/Jun/2025:10:15:42 +0000] "GET /api/stats HTTP/1.1" 200 2048
192.168.1.13 - - [04/Jun/2025:10:30:19 +0000] "POST /api/comments HTTP/1.1" 201 768
192.168.1.14 - - [04/Jun/2025:10:45:33 +0000] "GET /settings HTTP/1.1" 403 512
192.168.1.15 - - [04/Jun/2025:11:00:27 +0000] "GET /api/health HTTP/1.1" 200 128
192.168.1.16 - - [04/Jun/2025:11:15:14 +0000] "POST /api/upload HTTP/1.1" 413 256
192.168.1.7 - - [04/Jun/2025:09:01:33 +0000] "POST /api/auth HTTP/1.1" 401 256
192.168.1.17 - - [04/Jun/2025:11:30:45 +0000] "GET /api/notifications HTTP/1.1" 200 1024
192.168.1.18 - - [04/Jun/2025:11:45:22 +0000] "PUT /api/profile HTTP/1.1" 200 512
192.168.1.19 - - [04/Jun/2025:12:00:18 +0000] "GET /api/search?q=test HTTP/1.1" 200 2048
192.168.1.10 - - [04/Jun/2025:09:45:18 +0000] "GET /images/logo.png HTTP/1.1" 200 5120
192.168.1.20 - - [04/Jun/2025:12:15:33 +0000] "POST /api/orders HTTP/1.1" 201 1024
192.168.1.21 - - [04/Jun/2025:12:30:45 +0000] "GET /api/products/789 HTTP/1.1" 404 256
192.168.1.22 - - [04/Jun/2025:12:45:12 +0000] "GET /api/categories HTTP/1.1" 200 1536
192.168.1.23 - - [04/Jun/2025:13:00:28 +0000] "POST /api/reviews HTTP/1.1" 400 512
192.168.1.24 - - [04/Jun/2025:13:15:45 +0000] "GET /api/cart HTTP/1.1" 200 768
192.168.1.25 - - [04/Jun/2025:13:30:33 +0000] "DELETE /api/cart/items/123 HTTP/1.1" 200 0
192.168.1.26 - - [04/Jun/2025:13:45:19 +0000] "GET /api/wishlist HTTP/1.1" 200 1024
192.168.1.27 - - [04/Jun/2025:14:00:45 +0000] "POST /api/checkout HTTP/1.1" 200 1536
192.168.1.28 - - [04/Jun/2025:14:15:22 +0000] "GET /api/orders/456 HTTP/1.1" 200 2048
192.168.1.29 - - [04/Jun/2025:14:30:18 +0000] "PUT /api/orders/456/status HTTP/1.1" 200 512
192.168.1.30 - - [04/Jun/2025:14:45:33 +0000] "GET /api/shipping HTTP/1.1" 200 768
192.168.1.31 - - [04/Jun/2025:15:00:45 +0000] "POST /api/payment HTTP/1.1" 201 1024
192.168.1.32 - - [04/Jun/2025:15:15:12 +0000] "GET /api/invoice/789 HTTP/1.1" 200 3072
192.168.1.33 - - [04/Jun/2025:15:30:28 +0000] "GET /api/analytics HTTP/1.1" 403 256
192.168.1.34 - - [04/Jun/2025:15:45:45 +0000] "POST /api/feedback HTTP/1.1" 201 512
192.168.1.10 - - [04/Jun/2025:09:45:18 +0000] "GET /images/logo.png HTTP/1.1" 200 5120
192.168.1.35 - - [04/Jun/2025:16:00:19 +0000] "GET /api/support HTTP/1.1" 200 1024
192.168.1.36 - - [04/Jun/2025:16:15:33 +0000] "POST /api/tickets HTTP/1.1" 201 768
192.168.1.37 - - [04/Jun/2025:16:30:45 +0000] "GET /api/tickets/123 HTTP/1.1" 200 1536
192.168.1.38 - - [04/Jun/2025:16:45:22 +0000] "PUT /api/tickets/123 HTTP/1.1" 200 512
192.168.1.39 - - [04/Jun/2025:17:00:18 +0000] "GET /api/faq HTTP/1.1" 200 2048
192.168.1.40 - - [04/Jun/2025:17:15:33 +0000] "POST /api/contact HTTP/1.1" 200 512
192.168.1.41 - - [04/Jun/2025:17:30:45 +0000] "GET /api/blog HTTP/1.1" 200 3072
192.168.1.7 - - [04/Jun/2025:09:01:33 +0000] "POST /api/auth HTTP/1.1" 401 256
192.168.1.42 - - [04/Jun/2025:17:45:12 +0000] "GET /api/blog/123 HTTP/1.1" 200 2048
192.168.1.43 - - [04/Jun/2025:18:00:28 +0000] "POST /api/blog/comments HTTP/1.1" 201 768
192.168.1.44 - - [04/Jun/2025:18:15:45 +0000] "GET /api/newsletter HTTP/1.1" 200 512
192.168.1.45 - - [04/Jun/2025:18:30:19 +0000] "POST /api/newsletter/subscribe HTTP/1.1" 200 256
192.168.1.46 - - [04/Jun/2025:18:45:33 +0000] "GET /api/events HTTP/1.1" 200 1536
192.168.1.52 - - [04/Jun/2025:20:15:12 +0000] "POST /api/stream/chat HTTP/1.1" 200 512
192.168.1.53 - - [04/Jun/2025:20:30:28 +0000] "GET /api/chat/history HTTP/1.1" 200 2048
192.168.1.5 - - [04/Jun/2025:08:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.54 - - [04/Jun/2025:20:45:45 +0000] "POST /api/chat/message HTTP/1.1" 200 768
192.168.1.55 - - [04/Jun/2025:21:00:19 +0000] "GET /api/notifications/settings HTTP/1.1" 200 512
192.168.1.56 - - [04/Jun/2025:21:15:33 +0000] "PUT /api/notifications/settings HTTP/1.1" 200 256
192.168.1.57 - - [04/Jun/2025:21:30:45 +0000] "GET /api/activity HTTP/1.1" 200 1536
192.168.1.58 - - [04/Jun/2025:21:45:22 +0000] "GET /api/recommendations HTTP/1.1" 200 2048
192.168.1.59 - - [04/Jun/2025:22:00:18 +0000] "POST /api/recommendations/feedback HTTP/1.1" 200 512
192.168.1.60 - - [04/Jun/2025:22:15:33 +0000] "GET /api/search/suggestions HTTP/1.1" 200 768
192.168.1.61 - - [04/Jun/2025:22:30:45 +0000] "GET /api/trending HTTP/1.1" 200 1024
192.168.1.64 - - [04/Jun/2025:23:15:45 +0000] "GET /api/achievements HTTP/1.1" 200 1024
192.168.1.65 - - [04/Jun/2025:23:30:19 +0000] "POST /api/achievements/claim HTTP/1.1" 200 512
192.168.1.66 - - [04/Jun/2025:23:45:33 +0000] "GET /api/points HTTP/1.1" 200 768
192.168.1.67 - - [05/Jun/2025:00:00:45 +0000] "GET /api/rewards HTTP/1.1" 200 1024
192.168.1.68 - - [05/Jun/2025:00:15:22 +0000] "POST /api/rewards/redeem HTTP/1.1" 200 512
192.168.1.69 - - [05/Jun/2025:00:30:18 +0000] "GET /api/coupons HTTP/1.1" 200 768
192.168.1.70 - - [05/Jun/2025:00:45:33 +0000] "POST /api/coupons/apply HTTP/1.1" 200 256
192.168.1.71 - - [05/Jun/2025:01:00:45 +0000] "GET /api/subscription HTTP/1.1" 200 1024
192.168.1.72 - - [05/Jun/2025:01:15:12 +0000] "POST /api/subscription/upgrade HTTP/1.1" 200 512
192.168.1.73 - - [05/Jun/2025:01:30:28 +0000] "GET /api/billing HTTP/1.1" 200 1536
192.168.1.74 - - [05/Jun/2025:01:45:45 +0000] "POST /api/billing/update HTTP/1.1" 200 768
192.168.1.75 - - [05/Jun/2025:02:00:19 +0000] "GET /api/invoices HTTP/1.1" 200 2048
192.168.1.5 - - [04/Jun/2025:08:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.76 - - [05/Jun/2025:02:15:33 +0000] "GET /api/invoices/123 HTTP/1.1" 200 3072
192.168.1.77 - - [05/Jun/2025:02:30:45 +0000] "POST /api/invoices/pay HTTP/1.1" 200 512
192.168.1.78 - - [05/Jun/2025:02:45:22 +0000] "GET /api/transactions HTTP/1.1" 200 1536
192.168.1.79 - - [05/Jun/2025:03:00:18 +0000] "GET /api/transactions/456 HTTP/1.1" 200 1024
192.168.1.80 - - [05/Jun/2025:03:15:33 +0000] "POST /api/transactions/refund HTTP/1.1" 200 768
192.168.1.81 - - [05/Jun/2025:03:30:45 +0000] "GET /api/wallet HTTP/1.1" 200 512
192.168.1.82 - - [05/Jun/2025:03:45:12 +0000] "POST /api/wallet/add HTTP/1.1" 200 256
192.168.1.13 - - [04/Jun/2025:10:30:19 +0000] "POST /api/comments HTTP/1.1" 201 768
192.168.1.7 - - [04/Jun/2025:09:01:33 +0000] "POST /api/auth HTTP/1.1" 401 256
192.168.1.83 - - [05/Jun/2025:04:00:28 +0000] "GET /api/wallet/balance HTTP/1.1" 200 512
192.168.1.84 - - [05/Jun/2025:04:15:45 +0000] "POST /api/wallet/transfer HTTP/1.1" 200 768
192.168.1.85 - - [05/Jun/2025:04:30:19 +0000] "GET /api/statements HTTP/1.1" 200 2048
192.168.1.13 - - [04/Jun/2025:10:30:19 +0000] "POST /api/comments HTTP/1.1" 201 768
192.168.1.86 - - [05/Jun/2025:04:45:33 +0000] "GET /api/statements/789 HTTP/1.1" 200 3072
192.168.1.87 - - [05/Jun/2025:05:00:45 +0000] "POST /api/statements/download HTTP/1.1" 200 5120
192.168.1.88 - - [05/Jun/2025:05:15:22 +0000] "GET /api/taxes HTTP/1.1" 200 1536
192.168.1.5 - - [04/Jun/2025:08:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.95 - - [05/Jun/2025:07:00:19 +0000] "POST /api/analytics/filter HTTP/1.1" 200 1024
192.168.1.96 - - [05/Jun/2025:07:15:33 +0000] "GET /api/metrics HTTP/1.1" 200 1536
192.168.1.97 - - [05/Jun/2025:07:30:45 +0000] "GET /api/metrics/performance HTTP/1.1" 200 2048
192.168.1.98 - - [05/Jun/2025:07:45:22 +0000] "POST /api/metrics/update HTTP/1.1" 200 512
192.168.1.7 - - [04/Jun/2025:09:01:33 +0000] "POST /api/auth HTTP/1.1" 401 256
192.168.1.99 - - [05/Jun/2025:08:00:18 +0000] "GET /api/audit HTTP/1.1" 200 3072
192.168.1.13 - - [04/Jun/2025:10:30:19 +0000] "POST /api/comments HTTP/1.1" 201 768
' > sample_access.log

cd log_analyzer/

echo 'from collections import Counter, defaultdict
from typing import List

def top_ip_addresses(logs: List[dict], top_n: int = 10) -> dict:
    """
    Returns a dict of top N IPs and their hit counts.
    """
    counter = Counter()
    for log in logs:
        ip = log.get("ip")
        if ip:
            counter[ip] += 1
    return dict(counter.most_common(top_n))

def most_requested_endpoints(logs, top_n=5):
    endpoints = Counter(log["endpoint"] for log in logs)
    return endpoints.most_common(top_n)

def status_code_distribution(logs):
    codes = Counter(log["status"] for log in logs)
    return dict(codes)

def traffic_per_hour(logs):
    hourly = defaultdict(int)
    for log in logs:
        hour = log["timestamp"].strftime("%Y-%m-%d %H:00")
        hourly[hour] += 1
    return dict(hourly)
' > analyzer.py

echo '# Format: 10/Oct/2000:13:55:36 -0700
APACHE_LOG_TIMESTAMP_FORMAT = "%d/%b/%Y:%H:%M:%S %z"
' > constants.py

echo 'import json
import csv
from datetime import datetime
from pathlib import Path

def export_data(data: dict, fmt: str = "json", output_dir: str = "exports") -> None:
    """Export analysis result dictionary to specified format."""
    Path(output_dir).mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if fmt == "json":
        filename = f"{output_dir}/log_report_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[✔] Exported JSON report to {filename}")
    
    elif fmt == "csv":
        filename = f"{output_dir}/log_report_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for key, value in data.items():
                writer.writerow([key])
                if isinstance(value, dict):
                    writer.writerow(["Key", "Value"])
                    for k, v in value.items():
                        writer.writerow([k, v])
                elif isinstance(value, list):
                    for item in value:
                        writer.writerow(item if isinstance(item, (list, tuple)) else [item])
                writer.writerow([])  # blank line between sections
        print(f"[✔] Exported CSV report to {filename}")
' > exporter.py

echo 'from typing import List, Optional
from log_analyzer.utils import parse_timestamp

def filter_by_time_range(
    logs: List[dict], 
    start: Optional[str] = None, 
    end: Optional[str] = None
) -> List[dict]:
    """
    Filters log entries between start and end datetime (inclusive).
    Expects ISO 8601 datetime strings.
    """
    if not start and not end:
        return logs

    start_dt = parse_timestamp(start) if start else None
    end_dt = parse_timestamp(end) if end else None

    filtered = []
    for entry in logs:
        entry_time = entry.get("timestamp")
        if not entry_time:
            continue

        if ((start_dt is None or entry_time >= start_dt) and
            (end_dt is None or entry_time <= end_dt)):
            filtered.append(entry)

    return filtered


def filter_error_logs(logs: List[dict]) -> List[dict]:
    """
    Returns only log entries with status codes 4xx or 5xx.
    """
    return [
        log for log in logs 
        if 400 <= int(log.get("status", 0)) < 600
    ]
' > filters.py

echo 'import re
from datetime import datetime

from log_analyzer.constants import APACHE_LOG_TIMESTAMP_FORMAT

LOG_PATTERN = re.compile(
    r"(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] \"(?P<method>\S+) (?P<endpoint>\S+) \S+\" (?P<status>\d{3}) (?P<size>\d+)"
)
' > log_parser.py

echo 'def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
     # Parse with timezone info but then strip it to make it timezone-naiveAdd commentMore actions
    
    dt = datetime.strptime(data["timestamp"], APACHE_LOG_TIMESTAMP_FORMAT)
    data["timestamp"] = dt.replace(tzinfo=None)


    return data

def read_log_file(filepath):
    with open(filepath) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                yield parsed
' > log_parser.py

echo '
import argparse
from log_analyzer.log_parser import read_log_file
from log_analyzer.analyzer import (
    most_requested_endpoints, 
    status_code_distribution,
    traffic_per_hour,
    top_ip_addresses
)
from log_analyzer.report import (
    print_endpoint_stats, 
    print_status_codes, 
    print_traffic,
    print_ip_stats
)
from log_analyzer.exporter import export_data
from log_analyzer.filters import (
    filter_by_time_range, 
    filter_error_logs
)
from log_analyzer.utils import parse_timestamp
import sys

def main():
    parser = argparse.ArgumentParser(description="Analyze Apache-style log files.")
    parser.add_argument("logfile", help="Path to the access log file")
    parser.add_argument("--top", type=int, default=10, help="Top N entries to display")
    parser.add_argument("--start", type=str, help="Start datetime in ISO format (e.g. 2025-06-04T06:00:00)")
    parser.add_argument("--end", type=str, help="End datetime in ISO format (e.g. 2025-06-04T12:00:00)")
    parser.add_argument("--export", choices=["json", "csv"], help="Export results to JSON or CSV")
    parser.add_argument("--errors-only", action="store_true", help="Include only 4xx and 5xx error logs")

    args = parser.parse_args()
    parse_timestamp(args.start)
    parse_timestamp(args.end)

    try:
        logs = list(read_log_file(args.logfile))
    except FileNotFoundError:
        print(f"Log file not found: {args.logfile}")
        sys.exit(1)

    if args.start or args.end:
        logs = filter_by_time_range(logs, args.start, args.end)

    if args.errors_only:
        logs = filter_error_logs(logs)

    # Analysis
    endpoint_stats = most_requested_endpoints(logs, top_n=args.top)
    code_stats = status_code_distribution(logs)
    hourly_traffic = traffic_per_hour(logs)
    ip_stats = top_ip_addresses(logs, top_n=args.top)

    # Reporting
    print_endpoint_stats(endpoint_stats)
    print_status_codes(code_stats)
    print_traffic(hourly_traffic)
    print_ip_stats(ip_stats)

    # Export if needed
    if args.export:
        export_data(
            {
                "top_endpoints": endpoint_stats,
                "status_codes": code_stats,
                "hourly_traffic": hourly_traffic,
                "top_ips": ip_stats,
            },
            fmt=args.export
        )

if __name__ == "__main__":
    main()
' > main.py

echo 'def print_endpoint_stats(stats):
    print("Most Requested Endpoints:")
    for endpoint, count in stats:
        print(f"{endpoint}: {count} requests")

def print_status_codes(stats):
    print("\nStatus Code Distribution:")
    for code, count in stats.items():
        print(f"{code}: {count}")

def print_traffic(stats):
    print("\nTraffic per Hour:")
    for hour, count in sorted(stats.items()):
        print(f"{hour}: {count} requests")

def print_ip_stats(ip_stats: dict) -> None:
    print("\nTop IP Addresses:")
    for ip, count in ip_stats.items():
        print(f"  {ip:<15} -> {count} hits")
' > report.py

echo 'from datetime import datetime
from typing import Optional

from log_analyzer.constants import APACHE_LOG_TIMESTAMP_FORMAT

def parse_timestamp(dt_str: Optional[str]) -> Optional[datetime]:
    if dt_str is None:
        return None
    try:
        # Parse the datetime and ensure it'\''s timezone-naive
        dt = datetime.fromisoformat(dt_str)
        if dt.tzinfo is not None:
            dt = dt.replace(tzinfo=None)
        return dt
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: '\''{dt_str}'\''. Use ISO format like '\''2025-06-04T06:00:00'\''.") from e

def parse_apache_timestamp(ts: str) -> Optional[datetime]:
    """
    Parses Apache-style timestamp and removes timezone info to make it offset-naive.
    """
    try:
        dt = datetime.strptime(ts, APACHE_LOG_TIMESTAMP_FORMAT)
        return dt.replace(tzinfo=None)  # Strip timezone
    except ValueError:
        return None
' > utils.py

cd $SCRIPTS_DIR

git add .
git commit -F- << 'EOF'
feat: Add more features to log analyzer project

- Show hourly traffic trends
- Filter by time range
- Show only error responses (4xx/5xx)
- Export results to JSON or CSV
EOF

git push -u origin feat-452 -f

git switch master
