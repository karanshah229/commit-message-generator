def print_endpoint_stats(stats):
    print("Most Requested Endpoints:")
    for endpoint, count in stats:
        print(f"{endpoint}: {count} requests")
