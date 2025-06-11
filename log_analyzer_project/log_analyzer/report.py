def print_endpoint_stats(stats):
    print("Most Requested Endpoints:")
    for endpoint, count in stats:
        print(f"{endpoint}: {count} requests")

def print_status_codes(stats):
    print("\nStatus Code Distribution:")
    for code, count in stats.items():
        print(f"{code}: {count}")
