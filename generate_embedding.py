import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer

print("Loading multilingual embedding model...")

embed_model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

# Load datasets
departments = pd.read_excel("departments.xlsx")
complaints = pd.read_excel("category.xlsx")

print("Generating Department Embeddings...")

dept_embeddings = embed_model.encode(
    departments["description"].tolist(),
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

print("Generating Complaint Embeddings...")

complaint_embeddings = embed_model.encode(
    complaints["complaint_text"].tolist(),
    convert_to_numpy=True,
    normalize_embeddings=True,
    show_progress_bar=True
)

# Save embeddings
joblib.dump(dept_embeddings, "dept_embeddings.pkl")
joblib.dump(complaint_embeddings, "complaint_embeddings.pkl")

print("\nEmbeddings generated successfully!")