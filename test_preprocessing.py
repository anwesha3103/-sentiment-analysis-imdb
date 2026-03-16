import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.path.join(ROOT, "backend")
sys.path.insert(0, BACKEND)

from preprocessing.tokenizer import clean_text
from preprocessing.vectorizer import build_vectorizer, save_vectorizer

sample_reviews = [
    "This movie was absolutely brilliant! Loved every moment.",
    "Terrible film. Waste of time, completely boring and predictable.",
    "An okay watch, nothing special but not awful either.",
]

print("=== Testing tokenizer ===")
for r in sample_reviews:
    print(f"  IN : {r}")
    print(f"  OUT: {clean_text(r)}")
    print()

print("=== Testing vectorizer (fit + save) ===")
cleaned = [clean_text(r) for r in sample_reviews]
vec = build_vectorizer(max_features=500, min_df=1)   # min_df=1 for tiny test sample
vec.fit(cleaned)
save_vectorizer(vec)
print("  Vectorizer saved to backend/model/saved/tfidf_vectorizer.pkl")

print("=== Testing pipeline (transform) ===")
from preprocessing.pipeline import preprocess_single
result = preprocess_single("An amazing cinematic experience!")
print(f"  Output shape: {result.shape}")
print(f"  Non-zero features: {result.nnz}")
print("\nAll checks passed.")
