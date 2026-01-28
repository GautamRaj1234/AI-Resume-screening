from flask import Flask, render_template, request, redirect, url_for

import os

from resume_parser import extract_text, preprocess
from skills import SKILLS
from jobs import JOBS
from matcher import calculate_similarity
from flask import session


app = Flask(__name__)
app.secret_key = "resume_ai_secret"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():

    found_skills = []
    missing_skills = []
    results = {}

    if request.method == "POST":
        file = request.files["resume"]
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        raw_text = extract_text(file_path)
        clean_text = preprocess(raw_text)

        found_skills = [skill for skill in SKILLS if skill in clean_text]
        missing_skills = [skill for skill in SKILLS if skill not in found_skills]

        results = {}

        for job, desc in JOBS.items():
    
            tfidf_score = calculate_similarity(clean_text, desc)

            # skill match percentage
            job_skills = desc.split()
            matched = len(set(found_skills).intersection(job_skills))
            skill_score = (matched / len(job_skills)) * 100 if job_skills else 0

            # weighted final score
            final_score = (0.7 * skill_score) + (0.3 * tfidf_score)

            results[job] = round(final_score, 2)


        best_job = max(results, key=results.get)
        best_score = results[best_job]


        session["skills"] = found_skills
        session["missing_skills"] = missing_skills
        session["results"] = results
        session["best_job"] = best_job
        session["best_score"] = best_score

        return redirect(url_for("result"))


    return render_template("index.html")

@app.route("/result")
def result():
    return render_template(
        "result.html",
        skills=session.get("skills", []),
        missing_skills=session.get("missing_skills", []),
        results=session.get("results", {}),
        best_job=session.get("best_job", ""),
        best_score=session.get("best_score", 0)
    )


if __name__ == "__main__":
    app.run()
