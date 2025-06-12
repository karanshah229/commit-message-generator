import json
import csv
from datetime import datetime
from pathlib import Path

def export_data(data: dict, fmt: str = "json", output_dir: str = "exports") -> None:
    """Export analysis result dictionary to specified format."""
    Path(output_dir).mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if fmt == "json":
        filename = f"{output_dir}/log_report_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"[✔] Exported JSON report to {filename}")
    
    elif fmt == "csv":
        filename = f"{output_dir}/log_report_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for key, value in data.items():
                writer.writerow([key])
                if isinstance(value, dict):
                    writer.writerow(["Key", "Value"])
                    for k, v in value.items():
                        writer.writerow([k, v])
                elif isinstance(value, list):
                    for item in value:
                        writer.writerow(item if isinstance(item, (list, tuple)) else [item])
                writer.writerow([])  # blank line between sections
        print(f"[✔] Exported CSV report to {filename}")
