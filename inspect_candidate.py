import json

target = "CAND_0075574"

with open("candidates.jsonl", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] == target:
            print(json.dumps(c, indent=2)[:5000])
            break