import csv
from pathlib import Path
from matcher import calculate_match_score


def load_jobs():
    jobs = []

    with open(Path("data/jobs.csv"), "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            jobs.append(row)

    return jobs


def recommend_jobs(resume_text):
    jobs = load_jobs()

    for job in jobs:
        job["match_score"] = calculate_match_score(
            resume_text,
            job["description"]
        )

    jobs.sort(key=lambda item: item["match_score"], reverse=True)

    return jobs
