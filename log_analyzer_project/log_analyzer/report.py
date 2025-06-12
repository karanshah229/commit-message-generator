def print_endpoint_stats(stats):
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
