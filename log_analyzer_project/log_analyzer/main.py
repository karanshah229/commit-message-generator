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