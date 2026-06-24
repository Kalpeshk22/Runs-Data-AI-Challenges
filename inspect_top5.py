import json

targets = [
    "CAND_0075574",
    "CAND_0099806",
    "CAND_0044222",
    "CAND_0006418",
    "CAND_0050454"
]

with open("candidates.jsonl", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        if c["candidate_id"] in targets:

            print("\n" + "="*80)
            print(c["candidate_id"])

            print(
                c["profile"]["current_title"],
                "|",
                c["profile"]["years_of_experience"]
            )

            print(
                c["profile"]["current_company"]
            )

            print(
                c["profile"]["headline"]
            )

            print("\nSUMMARY:")
            print(c["profile"]["summary"][:500])

            print("\nCAREER:")
            for job in c["career_history"][:2]:
                print("-", job["title"])
                print(job["description"][:300])