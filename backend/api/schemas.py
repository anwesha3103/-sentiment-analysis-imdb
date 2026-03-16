from pydantic import BaseModel, Field

class ReviewRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=10,
        max_length=5000,
        description="Movie review text to classify"
    )

class PredictionResponse(BaseModel):
    label:      str   # "positive" or "negative"
    confidence: float # 0.0 → 1.0
    text:       str   # echoed back, truncated to 200 chars

class MetricsResponse(BaseModel):
    accuracy:         float
    f1_score:         float
    precision:        float
    recall:           float
    confusion_matrix: list[list[int]]

class HealthResponse(BaseModel):
    status:       str
    model_loaded: bool
    vectorizer_loaded: bool