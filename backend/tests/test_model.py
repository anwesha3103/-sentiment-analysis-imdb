import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.predict import predict

def test_predict_returns_label():
    result = predict("This movie was absolutely fantastic and brilliant.")
    assert result["label"] in ["positive", "negative"]

def test_predict_returns_confidence():
    result = predict("Terrible film, complete waste of time.")
    assert 0.0 <= result["confidence"] <= 1.0

def test_predict_positive_review():
    result = predict("One of the best films I have ever seen. A masterpiece.")
    assert result["label"] == "positive"

def test_predict_negative_review():
    result = predict("Awful, boring, and painfully bad. Hated every minute.")
    assert result["label"] == "negative"