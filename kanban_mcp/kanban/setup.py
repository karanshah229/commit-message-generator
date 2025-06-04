import subprocess
import os
import sys

def main():
    print("📦 Running DB seed...")
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "seed.py")], check=True)

    print("🚀 Starting FastAPI server on http://127.0.0.1:5000")
    subprocess.run([
        "uvicorn", "kanban.main:app", "--reload", "--port", "5000"
    ])
