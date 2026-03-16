import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from fastapi import APIRouter, HTTPException
from api.schemas import ReviewRequest, PredictionResponse, MetricsResponse, HealthResponse
from model.predict import predict, get_model
from preprocessing.vectorizer import load_vectorizer

router = APIRouter()

METRICS_PATH = os.path.normpath(os.path.join(
    ROOT, "model", "saved", "metrics.json"
))

@router.get("/health", response_model=HealthResponse)
def health_check():
    try:
        model_ok = get_model() is not None
    except Exception:
        model_ok = False
    try:
        vec_ok = load_vectorizer() is not None
    except Exception:
        vec_ok = False

    return HealthResponse(
        status="ok" if (model_ok and vec_ok) else "degraded",
        model_loaded=model_ok,
        vectorizer_loaded=vec_ok
    )

@router.post("/predict", response_model=PredictionResponse)
def predict_sentiment(request: ReviewRequest):
    try:
        result = predict(request.text)
        return PredictionResponse(**result)
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@router.get("/metrics", response_model=MetricsResponse)
def get_metrics():
    if not os.path.exists(METRICS_PATH):
        raise HTTPException(
            status_code=404,
            detail="Metrics not found. Run evaluate.py first."
        )
    with open(METRICS_PATH) as f:
        data = json.load(f)
    return MetricsResponse(**data)