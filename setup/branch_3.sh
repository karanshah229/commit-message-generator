git branch -D fix-359 || true
git checkout -b fix-359

SCRIPTS_DIR=$(pwd)

cd log_analyzer_project/

cd log_analyzer/

echo 'import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r"(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] \"(?P<method>\S+) (?P<endpoint>\S+) HTTP/1.1\" (?P<status>\d{3}) (?P<size>\d+)"
)

def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    try:
        data["timestamp"] = datetime.strptime(data["timestamp"], "%d/%b/%Y:%H:%M:%S %z")
    except ValueError:
        data["timestamp"] = None
    return data

def read_log_file(filepath):
    with open(filepath) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                yield parsed
' > log_parser.py

git add .
git commit -F- << 'EOF'
fix: Update log parsing logic
EOF

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
    try:
        data["timestamp"] = datetime.strptime(data["timestamp"], "%d/%b/%Y:%H:%M:%S %z")
    except ValueError:
        data["timestamp"] = None
    return data

def read_log_file(filepath):
    with open(filepath) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                yield parsed
' > log_parser.py

cd $SCRIPTS_DIR

git add .
git commit -F- << 'EOF'
fix: Log parser logic

- Regex pattern to parse logs with different HTTP versions
- Parse different timezone formats in the log
EOF

git push -u origin fix-359 -f
