import json

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for i in range(20):
        candidate = json.loads(f.readline())

        print("=" * 80)
        print(candidate["candidate_id"])
        print(candidate["profile"]["current_title"])
        print(candidate["profile"]["years_of_experience"])

        print("\nSkills:")
        for s in candidate["skills"][:10]:
            print("-", s["name"])

        print()