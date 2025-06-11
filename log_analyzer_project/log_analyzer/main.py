import sys
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
