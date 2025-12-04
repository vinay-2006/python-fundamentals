"""
Simple script to read and pretty-print the utility_history.jsonl file.
Requires utility_toolkit.py to have been executed at least once.
"""

import json
from datetime import datetime
import os

HISTORY_FILE = "utility_history.jsonl"


def pretty_print_history(filename: str):
    """Reads a JSONL file and prints each entry in a human-readable format."""
    if not os.path.exists(filename):
        print(f"\nError: History file '{filename}' not found. Run the CLI first.")
        return

    print(f"--- Reading Utility History from {filename} ---")

    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            try:
                entry = json.loads(line)

                timestamp_str = entry.get("ts", "N/A")
                try:
                    dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
                    formatted_ts = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
                except Exception:
                    formatted_ts = timestamp_str

                status = "SUCCESS"
                if "error" in entry:
                    status = f"ERROR: {entry['error']}"

                print(f"\n[{i}] @ {formatted_ts}")
                print(f"  Function #: {entry.get('function_number', 'N/A')}")
                print(f"  Status: {status}")
                print(f"  Output: {entry.get('output', entry.get('error', 'N/A'))}")

            except json.JSONDecodeError:
                print(f"\n[{i}] Invalid JSON entry.")
            except Exception as e:
                print(f"\n[{i}] Unexpected Error: {e}")


if __name__ == "__main__":
    pretty_print_history(HISTORY_FILE)
