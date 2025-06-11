from datetime import datetime
from typing import Optional

from log_analyzer.constants import APACHE_LOG_TIMESTAMP_FORMAT

def parse_timestamp(dt_str: Optional[str]) -> Optional[datetime]:
    if dt_str is None:
        return None
    try:
        # Parse the datetime and ensure it's timezone-naive
        dt = datetime.fromisoformat(dt_str)
        if dt.tzinfo is not None:
            dt = dt.replace(tzinfo=None)
        return dt
    except ValueError as e:
        raise ValueError(f"Invalid datetime format: '{dt_str}'. Use ISO format like '2025-06-04T06:00:00'.") from e

def parse_apache_timestamp(ts: str) -> Optional[datetime]:
    """
    Parses Apache-style timestamp and removes timezone info to make it offset-naive.
    """
    try:
        dt = datetime.strptime(ts, APACHE_LOG_TIMESTAMP_FORMAT)
        return dt.replace(tzinfo=None)  # Strip timezone
    except ValueError:
        return None
