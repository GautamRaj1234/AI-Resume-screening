# 🤖 AI Resume Screening System

An AI-powered Resume Screening web application built using **Python & Flask**.  
The system analyzes resumes, extracts skills, compares them with job descriptions, and recommends the best-matching job role using **NLP and Machine Learning techniques**.

🔗 **Live Demo:**  
https://ai-resume-screening-4z58.onrender.com/

---

## 🚀 Features
- Upload resume in **PDF or DOCX format**
- Automatic **text extraction** from resume
- **Skill extraction** using NLP
- Matching resume with predefined **job roles**
- **TF-IDF & cosine similarity** based job scoring
- Displays:
  - Found skills
  - Missing skills
  - Best-matched job role
  - Match percentage
- Clean, responsive UI
- Deployed on **Render (Cloud Hosting)**

---

## 🧠 Technologies Used

### Backend
- Python
- Flask

### Machine Learning / NLP
- NLTK
- Scikit-learn (TF-IDF & cosine similarity)

### Resume Parsing
- pdfplumber (PDF parsing)
- python-docx (DOCX parsing)

### Frontend
- HTML
- CSS

### Deployment
- GitHub
- Render Cloud Platform
- Gunicorn

---

## 📦 Libraries Used

flask
gunicorn
pdfplumber
python-docx
nltk
scikit-learn

---

## 📂 Project Structure

AI-Resume-screening/
│
├── app.py # Main Flask application
├── resume_parser.py # Resume text extraction & preprocessing
├── matcher.py # Similarity calculation logic
├── skills.py # Skill dataset
├── jobs.py # Job descriptions
├── requirements.txt # Dependencies
│
├── templates/
│ ├── index.html # Upload page
│ └── result.html # Result page
│
├── static/
│ └── style.css # Styling
│
└── uploads/ # Uploaded resumes


---

## ⚙️ How It Works

1. User uploads a resume
2. Resume text is extracted (PDF/DOCX)
3. Text is cleaned and preprocessed
4. Skills are matched with predefined skill set
5. Resume is compared with job descriptions using **TF-IDF**
6. Best job role is recommended based on score

---

## 🚀 Deployment Note

This project is deployed on **Render Free Tier**.  
The server may take **30–60 seconds to wake up** on first request due to cold start.

---

## 🎓 Academic Relevance

- Demonstrates:
  - AI & NLP concepts
  - Machine Learning similarity models
  - Real-world problem solving
  - Full-stack deployment

---

## 📌 Future Improvements
- ML model based scoring
- Resume ranking system
- Login & user dashboard
- Database integration

---

## 👨‍💻 Author
**Gautam Raj**  
B.Tech – Computer Science (AI) 
GitHub: https://github.com/GautamRaj1234
