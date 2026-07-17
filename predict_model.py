import joblib
from rule_engine import apply_rules

# Load models
vectorizer = joblib.load("tfidf_vectorizer.pkl")
category_model = joblib.load("category_model.pkl")  
urgency_model = joblib.load("urgency_model.pkl")


def predict_complaint(text):
    # Convert text to TF-IDF
    X = vectorizer.transform([text])

    # Predict category
    category = category_model.predict(X)[0]

    # Predict urgency using ML
    ml_urgency = urgency_model.predict(X)[0]

    # Apply rule engine
    final_urgency = apply_rules(text, ml_urgency)

    return category, final_urgency


if __name__ == "__main__":

    complaint = input("Enter Complaint:\n")

    category, urgency = predict_complaint(complaint)

    print("\nPredicted Category :", category)
    print("Predicted Urgency :", urgency)