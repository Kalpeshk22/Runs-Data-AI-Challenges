# Redrob AI Hackathon Submission

## Overview

This solution ranks candidates for the Senior AI Engineer role using a weighted scoring approach based on:

* AI/ML skill relevance
* Current job title relevance
* Experience alignment (5–9 years preferred)
* Behavioral signals
* Recruiter response rate
* Candidate activity indicators

## Ranking Logic

The scoring model prioritizes candidates with demonstrated experience in:

* Retrieval Systems
* Recommendation Systems
* Ranking Systems
* Embedding-based Search
* Vector Databases
* LLM Infrastructure

Additional weight is given to candidates whose profiles indicate production deployment experience and strong recruiter engagement signals.

## Output

The script generates a ranked list of the top 100 candidates in the required submission format.

## Run

python rank_candidates.py
