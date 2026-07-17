import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading datasets...")

departments = pd.read_excel("departments.xlsx")
complaints = pd.read_excel("category.xlsx")

print("Building TF-IDF index...")

# -------------------------------------------------------
# Department Search
# -------------------------------------------------------

department_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1,2)
)

department_matrix = department_vectorizer.fit_transform(
    departments["description"]
)

# -------------------------------------------------------
# Complaint Search
# -------------------------------------------------------

complaint_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1,2)
)

complaint_matrix = complaint_vectorizer.fit_transform(
    complaints["complaint_text"]
)

print("IR System Ready!\n")

# =======================================================
# Department Search
# =======================================================

def find_department(text):

    query = department_vectorizer.transform([text])

    scores = cosine_similarity(
        query,
        department_matrix
    )[0]

    idx = scores.argmax()

    return departments.iloc[idx], scores[idx]

# =======================================================
# Similar Complaints
# =======================================================

def find_similar_complaints(text, top_n=3):

    query = complaint_vectorizer.transform([text])

    scores = cosine_similarity(
        query,
        complaint_matrix
    )[0]

    complaints_copy = complaints.copy()

    complaints_copy["Similarity"] = scores

    complaints_copy = complaints_copy.sort_values(
        by="Similarity",
        ascending=False
    )

    return complaints_copy.head(top_n)

# =======================================================
# Test
# =======================================================

if __name__ == "__main__":

    while True:

        complaint = input("\nEnter Complaint (type exit): ")

        if complaint.lower() == "exit":
            break

        dept, score = find_department(complaint)

        print("\nDepartment")
        print("-------------------------")
        print(dept["department_name"])
        print("Confidence :", round(score,3))

        print("\nSimilar Complaints")
        print("-------------------------")

        print(
            find_similar_complaints(complaint)[
                [
                    "complaint_text",
                    "category",
                    "resolved",
                    "days_taken",
                    "Similarity"
                ]
            ]
        )