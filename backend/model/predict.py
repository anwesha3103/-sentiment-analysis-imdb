import os
import sys
import joblib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocessing.pipeline import preprocess_single

MODEL_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "saved", "lr_model.pkl"
))

_model = None

def get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError("Model not found. Run train.py first.")
        _model = joblib.load(MODEL_PATH)
    return _model

def predict(text: str) -> dict:
    model = get_model()
    features = preprocess_single(text)
    label = int(model.predict(features)[0])
    confidence = float(np.max(model.predict_proba(features)))

    return {
        "label"     : "positive" if label == 1 else "negative",
        "confidence": round(confidence, 4),
        "text"      : text[:200]
    }