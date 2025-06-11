from collections import Counter

def most_requested_endpoints(logs, top_n=5):
    endpoints = Counter(log["endpoint"] for log in logs)
    return endpoints.most_common(top_n)

def status_code_distribution(logs):
    codes = Counter(log["status"] for log in logs)
    return dict(codes)
