import re
from datetime import datetime

from log_analyzer_project.log_analyzer.constants import APACHE_LOG_TIMESTAMP_FORMAT

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)'
)

def parse_line(line):
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    # Parse with timezone info but then strip it to make it timezone-naive
    dt = datetime.strptime(data["timestamp"], APACHE_LOG_TIMESTAMP_FORMAT)
    data["timestamp"] = dt.replace(tzinfo=None)
    return data

def read_log_file(filepath):
    with open(filepath) as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                yield parsed
