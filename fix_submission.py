import pandas as pd

df = pd.read_csv("submission.csv")

df = df.sort_values(
    by=["score", "candidate_id"],
    ascending=[False, True]
)

df["rank"] = range(1, len(df) + 1)

df.to_csv("submission_fixed.csv", index=False)

print("Done")