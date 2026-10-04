import re

SKILLS = [
    "python", "java", "c++", "c", "javascript", "typescript",
    "html", "css", "react", "node", "nodejs", "express",
    "mongodb", "mysql", "sql", "postgresql",
    "machine learning", "deep learning", "nlp",
    "scikit learn", "tensorflow", "pytorch",
    "pandas", "numpy", "matplotlib",
    "git", "github", "flask", "django",
    "data analysis", "power bi", "excel",
    "aws", "docker", "rest api", "api",
    "data structures", "algorithms", "oop"
]

KEYWORDS = [
    "developer", "engineer", "analyst", "internship", "intern",
    "software", "backend", "frontend", "full stack", "data",
    "machine learning", "artificial intelligence", "web",
    "database", "cloud", "project", "experience", "education",
    "certification", "communication"
]


def extract_skills(text):
    found = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text, re.IGNORECASE):
            found.append(skill)

    return sorted(set(found))


def extract_keywords(text):
    found = []

    for keyword in KEYWORDS:
        pattern = r"(?<!\w)" + re.escape(keyword) + r"(?!\w)"
        if re.search(pattern, text, re.IGNORECASE):
            found.append(keyword)

    return sorted(set(found))
