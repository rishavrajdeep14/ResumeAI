# AI Resume Screening & Job Recommendation System

An intermediate AIML project built with Python, NLP, machine learning and Scikit-learn.

## Features

- Upload resumes in PDF or DOCX format
- Extract readable resume text
- Clean and preprocess text
- Lowercase text and remove symbols
- Remove stop words
- Tokenize text
- Extract skills and keywords
- Convert resume/job descriptions into TF-IDF vectors
- Calculate cosine similarity
- Generate match scores
- Recommend suitable job roles
- Includes a small Logistic Regression evaluation example
- Simple Flask web interface

## Project Structure

```text
AIResumeScreening/
├── app.py
├── resume_parser.py
├── preprocessing.py
├── skills.py
├── matcher.py
├── recommender.py
├── evaluation.py
├── requirements.txt
├── README.md
├── data/
│   └── jobs.csv
├── resumes/
├── templates/
│   └── index.html
└── static/
    └── css/
        └── style.css
```

## How to Run

Create a virtual environment if you want one:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the local Flask address shown in the terminal.

## Evaluation

Run:

```bash
python evaluation.py
```

The evaluation file demonstrates Accuracy, Precision, Recall and F1-Score using a small labeled sample dataset.

The evaluation sample is intentionally small and is meant for demonstrating the ML workflow rather than claiming production-level model performance.
