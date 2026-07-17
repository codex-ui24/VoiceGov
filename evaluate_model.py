import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ---------------------------------
# Load Dataset
# ---------------------------------
data = pd.read_excel("category.xlsx")

X = data["complaint_text"]
y = data["category"]

# ---------------------------------
# Load Saved TF-IDF Vectorizer
# ---------------------------------
vectorizer = joblib.load("tfidf_vectorizer.pkl")

X = vectorizer.transform(X)

# ---------------------------------
# Split Dataset (same as training)
# ---------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------
# Load Saved Model
# ---------------------------------
model = joblib.load("category_model.pkl")

# ---------------------------------
# Make Predictions
# ---------------------------------
y_pred = model.predict(X_test)

# ---------------------------------
# Evaluation
# ---------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))