from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
from resume_parser import extract_text
from preprocessing import clean_text
from skills import extract_skills, extract_keywords
from matcher import calculate_match_score
from recommender import recommend_jobs

app = Flask(__name__)
app.secret_key = "resume_screening_secret"

UPLOAD_FOLDER = Path("resumes")
ALLOWED_EXTENSIONS = {"pdf", "docx"}
UPLOAD_FOLDER.mkdir(exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume = request.files.get("resume")

        if not resume or resume.filename == "":
            flash("Please select a resume.")
            return redirect(url_for("index"))

        if not allowed_file(resume.filename):
            flash("Only PDF and DOCX resumes are supported.")
            return redirect(url_for("index"))

        file_path = UPLOAD_FOLDER / resume.filename
        resume.save(file_path)

        try:
            raw_text = extract_text(str(file_path))

            if not raw_text.strip():
                flash("No readable text was found in the resume.")
                return redirect(url_for("index"))

            cleaned_resume = clean_text(raw_text)
            resume_skills = extract_skills(cleaned_resume)
            resume_keywords = extract_keywords(cleaned_resume)

            jobs = recommend_jobs(cleaned_resume)

            for job in jobs:
                job["match_score"] = calculate_match_score(
                    cleaned_resume, job["description"]
                )

            jobs.sort(key=lambda x: x["match_score"], reverse=True)

            result = {
                "filename": resume.filename,
                "summary": raw_text[:650].strip(),
                "skills": resume_skills,
                "keywords": resume_keywords[:15],
                "jobs": jobs[:5],
                "best_match": jobs[0] if jobs else None
            }

        except Exception as error:
            flash(f"Something went wrong while processing the resume: {error}")
            return redirect(url_for("index"))

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
