import json

KEYWORDS = [
    "Recommendation Systems",
    "Retrieval",
    "FAISS",
    "Qdrant",
    "Milvus",
    "Weaviate",
    "OpenSearch",
    "Elasticsearch",
    "Vector Database",
    "LLM",
    "Fine-tuning LLMs",
    "PyTorch",
    "Hugging Face Transformers",
    "LoRA",
    "LangChain"
]

count = 0

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        skills = [s["name"] for s in candidate["skills"]]

        matches = [k for k in KEYWORDS if k in skills]

        if len(matches) >= 3:
            count += 1

            print("\n", "=" * 80)
            print(candidate["candidate_id"])
            print(candidate["profile"]["current_title"])
            print("Experience:", candidate["profile"]["years_of_experience"])
            print("Matched:", matches)

            if count == 20:
                break