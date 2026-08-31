import json

input_path = "/app/index.txt"
output_path = "/app/report.json"

with open(input_path, "r", encoding="utf-8") as f:
    non_empty_lines = sum(1 for line in f if line.strip())

with open(output_path, "w", encoding="utf-8") as f:
    json.dump({"non_empty_lines": non_empty_lines}, f)