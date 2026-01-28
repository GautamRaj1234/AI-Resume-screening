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
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if "resume" not in request.files:
                return redirect(url_for("index"))

            file = request.files["resume"]
            if file.filename == "":
                return redirect(url_for("index"))

            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            raw_text = extract_text(file_path)
            clean_text = preprocess(raw_text)

            found_skills = [s for s in SKILLS if s in clean_text]
            missing_skills = [s for s in SKILLS if s not in found_skills]

            results = {}
            for job, desc in JOBS.items():
                score = calculate_similarity(clean_text, desc)
                results[job] = score

            best_job = max(results, key=results.get)
            best_score = results[best_job]

            session["skills"] = found_skills
            session["missing_skills"] = missing_skills
            session["results"] = results
            session["best_job"] = best_job
            session["best_score"] = best_score

            return redirect(url_for("result"))

        except Exception as e:
            print("APP ERROR:", e)
            return "Internal Server Error", 500

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
