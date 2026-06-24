import json
import csv

TARGET_SKILLS = {
    "FAISS",
    "Qdrant",
    "Milvus",
    "Weaviate",
    "OpenSearch",
    "Elasticsearch",
    "Recommendation Systems",
    "Hugging Face Transformers",
    "Fine-tuning LLMs",
    "LoRA"
}

GOOD_TITLES = {
    "AI Engineer",
    "ML Engineer",
    "Machine Learning Engineer",
    "Senior Machine Learning Engineer",
    "Data Scientist",
    "Backend Engineer",
    "Software Engineer",
    "Data Engineer"
}

BAD_TITLES = {
    "Marketing Manager",
    "Graphic Designer",
    "Customer Support",
    "HR Manager",
    "Accountant",
    "Sales Executive"
}


def score_candidate(c):

    score = 0.0

    # ------------------
    # Skills Score (40)
    # ------------------
    skills = {s["name"] for s in c.get("skills", [])}

    matched = skills.intersection(TARGET_SKILLS)

    skills_score = (len(matched) / len(TARGET_SKILLS)) * 40

    score += skills_score

    # ------------------
    # Career Score (30)
    # ------------------
    title = c["profile"]["current_title"]

    career_score = 0

    if title in GOOD_TITLES:
        career_score += 20

    if title in BAD_TITLES:
        career_score -= 10

    for job in c.get("career_history", []):

        jt = job.get("title", "")

        if jt in GOOD_TITLES:
            career_score += 2

    career_score = max(0, min(career_score, 30))

    score += career_score

    # ------------------
    # Behavioral Score (20)
    # ------------------
    signals = c["redrob_signals"]

    behavior = 0

    if signals.get("open_to_work_flag"):
        behavior += 5

    behavior += signals.get("recruiter_response_rate", 0) * 5

    behavior += (
        min(signals.get("github_activity_score", 0), 100)
        / 100
    ) * 5

    behavior += (
        signals.get("interview_completion_rate", 0)
    ) * 5

    if signals.get("notice_period_days", 999) <= 30:
        behavior += 2

    behavior = min(behavior, 20)

    score += behavior

    # ------------------
    # Experience Score (10)
    # ------------------
    exp = c["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 10
    elif 4 <= exp <= 12:
        score += 5

    reasoning = (
        f"{title} with {exp:.1f} yrs; "
        f"{len(matched)} AI core skills; "
        f"response rate {signals.get('recruiter_response_rate',0):.2f}"
    )

    return score, reasoning


results = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        c = json.loads(line)

        score, reasoning = score_candidate(c)

        results.append({
            "candidate_id": c["candidate_id"],
            "score": score,
            "reasoning": reasoning,
            "title": c["profile"]["current_title"]
        })


results.sort(
    key=lambda x: x["score"],
    reverse=True
)

top100 = results[:100]

with open(
    "submission.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, row in enumerate(top100, start=1):

        writer.writerow([
            row["candidate_id"],
            rank,
            round(row["score"] / 100, 4),
            row["reasoning"]
        ])

print("submission.csv created successfully")