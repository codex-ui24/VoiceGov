import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_excel("category.xlsx")

X = data["complaint_text"]
y = data["urgency"]

vectorizer = joblib.load("tfidf_vectorizer.pkl")

X = vectorizer.transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
urgency_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
urgency_model.fit(X_train, y_train)

accuracy = urgency_model.score(X_test, y_test)

print(f"Urgency Model Accuracy: {accuracy*100:.2f}%")

joblib.dump(vectorizer, "urgency_vectorizer.pkl")
joblib.dump(urgency_model, "urgency_model.pkl")

print("Urgency model saved successfully!")