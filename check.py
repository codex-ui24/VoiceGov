import joblib

model = joblib.load("category_model.pkl")

print(model.n_features_in_)

model = joblib.load("urgency_model.pkl")

print(model.n_features_in_)

vectorizer = joblib.load("tfidf_vectorizer.pkl")

print(len(vectorizer.vocabulary_))