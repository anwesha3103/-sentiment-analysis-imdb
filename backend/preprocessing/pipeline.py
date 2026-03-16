from .tokenizer import clean_text
from .vectorizer import load_vectorizer
import scipy.sparse

_vectorizer = None

def get_vectorizer():
    global _vectorizer
    if _vectorizer is None:
        _vectorizer = load_vectorizer()
    return _vectorizer

def preprocess_single(text: str) -> scipy.sparse.csr_matrix:
    """Clean and vectorize a single review for inference."""
    cleaned = clean_text(text)
    vec = get_vectorizer()
    return vec.transform([cleaned])

def preprocess_batch(texts: list[str]) -> scipy.sparse.csr_matrix:
    """Clean and vectorize a batch — used during training."""
    cleaned = [clean_text(t) for t in texts]
    vec = get_vectorizer()
    return vec.transform(cleaned)