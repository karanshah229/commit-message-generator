from typing import List, Optional
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
