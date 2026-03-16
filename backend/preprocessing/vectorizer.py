#backend/preprocessing/vectorizer.py
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer

VECTORIZER_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "model",
    "saved",
    "tfidf_vectorizer.pkl"
))
def build_vectorizer(max_features: int = 50000, ngram_range=(1, 2), min_df: int = 2) -> TfidfVectorizer:
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        sublinear_tf=True,
        min_df=min_df,
        strip_accents="unicode",
    )

def save_vectorizer(vec: TfidfVectorizer) -> None:
    os.makedirs(os.path.dirname(VECTORIZER_PATH), exist_ok=True)
    joblib.dump(vec, VECTORIZER_PATH)

def load_vectorizer() -> TfidfVectorizer:
    if not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError("Vectorizer not found. Run train.py first.")
    return joblib.load(VECTORIZER_PATH)