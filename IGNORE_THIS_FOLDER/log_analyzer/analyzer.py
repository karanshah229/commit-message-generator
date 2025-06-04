from collections import Counter, defaultdict

def most_requested_endpoints(logs, top_n=5):
    endpoints = Counter(log["endpoint"] for log in logs)
    return endpoints.most_common(top_n)

def status_code_distribution(logs):
    codes = Counter(log["status"] for log in logs)
    return dict(codes)

def traffic_per_hour(logs):
    hourly = defaultdict(int)
    for log in logs:
        hour = log["timestamp"].strftime("%Y-%m-%d %H:00")
        hourly[hour] += 1
    return dict(hourly)
