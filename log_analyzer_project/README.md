# log-analyzer

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
