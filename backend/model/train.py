import os
import sys
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocessing.tokenizer import clean_text
from preprocessing.vectorizer import build_vectorizer, save_vectorizer

MODEL_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "saved", "lr_model.pkl"
))

DATA_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "data", "raw", "IMDB Dataset.csv"
))

def train():
    print("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    df = df[["review", "sentiment"]].dropna()
    df["label"] = (df["sentiment"] == "positive").astype(int)

    print(f"  Total samples : {len(df)}")
    print(f"  Positive      : {df['label'].sum()}")
    print(f"  Negative      : {len(df) - df['label'].sum()}")

    print("\nCleaning text...")
    df["cleaned"] = df["review"].apply(clean_text)

    print("Splitting dataset (80/20)...")
    X_train, X_test, y_train, y_test = train_test_split(
        df["cleaned"], df["label"],
        test_size=0.2,
        random_state=42,
        stratify=df["label"]
    )

    print("Fitting TF-IDF vectorizer...")
    vec = build_vectorizer(max_features=50000, ngram_range=(1, 2), min_df=2)
    X_train_vec = vec.fit_transform(X_train)
    X_test_vec  = vec.transform(X_test)
    save_vectorizer(vec)
    print(f"  Vocabulary size: {len(vec.vocabulary_)}")

    print("\nTraining Logistic Regression...")
    model = LogisticRegression(
        C=1.0,
        max_iter=1000,
        solver="lbfgs",
        n_jobs=-1,
        random_state=42
    )
    model.fit(X_train_vec, y_train)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"  Model saved to {MODEL_PATH}")

    return model, X_test_vec, y_test

if __name__ == "__main__":
    train()