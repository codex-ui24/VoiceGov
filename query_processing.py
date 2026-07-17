import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

hindi_stopwords = ["hai", "ka", "ke", "ki", "se", "mein", "ko", "aur", "hain"]
stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)        # remove punctuation
    tokens = text.split()                       # tokenize
    tokens = [t for t in tokens if t not in hindi_stopwords]  # remove stopwords
    return " ".join(tokens)

# Test
print(clean_text("Mere ghar mein teen din se bijli nahi hai"))