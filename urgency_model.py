import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# -------------------------------
# Load Dataset
# -------------------------------
data = pd.read_excel("category.xlsx")

# Features and Labels
X = data["complaint_text"]
y = data["urgency"]

# -------------------------------
# Convert Text to TF-IDF
# -------------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    lowercase=True,
    min_df=2
)

vectorizer = joblib.load("tfidf_vectorizer.pkl")

X = vectorizer.transform(X)

# -------------------------------
# Split Dataset
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
urgency_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
urgency_model.fit(X_train, y_train)

# -------------------------------
# Accuracy
# -------------------------------
accuracy = urgency_model.score(X_test, y_test)

print(f"Urgency Model Accuracy: {accuracy*100:.2f}%")

# -------------------------------
# Save Model
# -------------------------------
joblib.dump(vectorizer, "urgency_vectorizer.pkl")
joblib.dump(urgency_model, "urgency_model.pkl")

print("Urgency model saved successfully!")