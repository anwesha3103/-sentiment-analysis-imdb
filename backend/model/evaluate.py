import os
import sys
import json
import joblib
import numpy as np
from sklearn.metrics import (
    f1_score, accuracy_score, precision_score,
    recall_score, confusion_matrix, classification_report
)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "saved", "lr_model.pkl"
))

METRICS_PATH = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "saved", "metrics.json"
))

def evaluate(model, X_test, y_test):
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy"  : round(accuracy_score(y_test, y_pred), 4),
        "f1_score"  : round(f1_score(y_test, y_pred), 4),
        "precision" : round(precision_score(y_test, y_pred), 4),
        "recall"    : round(recall_score(y_test, y_pred), 4),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
    }

    print(f"  Accuracy  : {metrics['accuracy']}")
    print(f"  F1 Score  : {metrics['f1_score']}")
    print(f"  Precision : {metrics['precision']}")
    print(f"  Recall    : {metrics['recall']}")
    print(f"\n{classification_report(y_test, y_pred, target_names=['Negative','Positive'])}")
    print(f"  Confusion Matrix: {metrics['confusion_matrix']}")

    os.makedirs(os.path.dirname(METRICS_PATH), exist_ok=True)
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"\n  Metrics saved to {METRICS_PATH}")

    return metrics

if __name__ == "__main__":
    from train import train
    model, X_test, y_test = train()
    evaluate(model, X_test, y_test)