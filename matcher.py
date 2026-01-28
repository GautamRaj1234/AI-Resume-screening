from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text, job_desc):
    try:
        if not text.strip() or not job_desc.strip():
            return 0

        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([text, job_desc])

        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        return round(similarity * 100, 2)

    except Exception as e:
        print("Similarity error:", e)
        return 0


