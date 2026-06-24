import json

with open("candidates.jsonl", encoding="utf-8") as f:
    first = json.loads(next(f))

print(first.keys())