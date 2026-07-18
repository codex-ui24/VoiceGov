import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_excel("category.xlsx")

X = data["complaint_text"]
y = data["category"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1,2),
    lowercase=True,
    min_df=2
)

X = vectorizer.fit_transform(X)

joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Accuracy: {accuracy*100:.2f}%")

joblib.dump(model, "category_model.pkl")

print("Model saved successfully!")