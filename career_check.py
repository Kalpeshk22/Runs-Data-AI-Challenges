import json

TARGET_IDS = [
    "CAND_0000021",
    "CAND_0000083",
    "CAND_0000121"
]

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] in TARGET_IDS:
            print("\n" + "="*80)
            print(c["candidate_id"])

            for job in c["career_history"]:
                print(job["title"], "|", job["industry"])