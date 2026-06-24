import json

target = "CAND_0000001"

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] == target:
            print(c["profile"])
            print()
            print("Signals:")
            print(c["redrob_signals"])
            break