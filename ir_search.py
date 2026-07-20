import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading datasets...")

departments = pd.read_excel("departments.xlsx")
complaints = pd.read_excel("category.xlsx")

print("Building TF-IDF index...")


department_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1,2),
    min_df=1,
    max_df=0.90,
    sublinear_tf=True
)

department_matrix = department_vectorizer.fit_transform(
    departments["description"]
)

complaint_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1,2),
    min_df=1,
    max_df=0.90,
    sublinear_tf=True
)

complaint_matrix = complaint_vectorizer.fit_transform(
    complaints["complaint_text"]
)

print("IR System Ready!\n")


def find_department(text, predicted_category=None):

    filtered_departments = departments

    if predicted_category is not None:

        filtered_departments = departments[
            departments["category"].str.lower() ==
            predicted_category.lower()
        ]

        if len(filtered_departments) == 0:
            filtered_departments = departments

    temp_matrix = department_vectorizer.transform(
        filtered_departments["description"]
    )

    query = department_vectorizer.transform([text])

    scores = cosine_similarity(
        query,
        temp_matrix
    )[0]

    idx = scores.argmax()

    return filtered_departments.iloc[idx], scores[idx]

def find_similar_complaints(
        text,
        predicted_category=None,
        top_n=3):
    filtered = complaints

    if predicted_category is not None:
        filtered = complaints[
            complaints["category"].str.lower() ==
             predicted_category.lower()
    ]

    if len(filtered) == 0:
        filtered = complaints
    
    query = complaint_vectorizer.transform([text])

    temp_matrix = complaint_vectorizer.transform(
        filtered["complaint_text"]
)
    scores = cosine_similarity(
        query,
        temp_matrix
    )[0]

    complaints_copy = filtered.copy()

    complaints_copy = complaints_copy.drop_duplicates(
        subset="complaint_text"
)

    complaints_copy["Similarity"] = scores

    complaints_copy = complaints_copy[
        complaints_copy["Similarity"] > 0.10
]
    if complaints_copy.empty:
        return pd.DataFrame(columns=complaints.columns)

    complaints_copy = complaints_copy.sort_values(
        by="Similarity",
        ascending=False
    )

    return complaints_copy.head(top_n)


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