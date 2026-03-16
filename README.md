# IMDB Sentiment Analysis

Full-stack NLP application classifying movie reviews as positive or negative using classical machine learning — no deep learning required.

## Results

Trained on 50,000 IMDB reviews (80/20 stratified split).

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 90.35% |
| F1 Score  | 90.43% |
| Precision | 89.71% |
| Recall    | 91.16% |

> Achieves **90%+ accuracy** using Logistic Regression — comparable to fine-tuned BERT baselines on the same dataset at a fraction of the compute cost.

## Stack

| Layer | Technology |
|-------|-----------|
| Model | Logistic Regression, TF-IDF bigrams (50k features) |
| Backend | FastAPI, uvicorn, scikit-learn, NLTK |
| Frontend | React, Vite, Recharts |
| DevOps | Docker, docker-compose, GitHub Actions CI/CD |

## Project Structure
```
sentiment-analysis-imdb/
├── backend/
│   ├── api/            # FastAPI routes and schemas
│   ├── model/          # Training, evaluation, inference
│   ├── preprocessing/  # Tokenizer, vectorizer, pipeline
│   ├── tests/          # Pytest unit tests
│   └── main.py         # App entry point
├── frontend/
│   └── src/
│       ├── components/ # SentimentBadge, MetricsDashboard, ConfusionMatrix
│       ├── hooks/      # useSentiment custom hook
│       └── api/        # Axios API calls
├── docker-compose.yml
└── .github/workflows/  # CI/CD pipeline
```

## Run Locally

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python model/evaluate.py
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Docker:**
```bash
docker compose up --build
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/predict | Classify a review — returns label + confidence score |
| GET | /api/metrics | F1, accuracy, precision, recall, confusion matrix |
| GET | /api/health | Model and vectorizer load status |
| GET | /docs | Interactive Swagger UI |

## Key Design Decisions

- **TF-IDF with bigrams** — captures two-word phrases like "not good" that unigrams miss
- **sublinear_tf scaling** — reduces dominance of high-frequency terms
- **Lemmatization over stemming** — cleaner vocabulary, better generalisation
- **Lazy model loading** — model and vectorizer load once at startup, not per request
- **Absolute path resolution** — all file paths use `os.path.abspath(__file__)` for environment independence

## Author

Anwesha — ML Engineer & SDE at Aspire Infolabs Global