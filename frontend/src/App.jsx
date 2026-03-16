import { useState } from "react";
import ReviewInput from "./components/ReviewInput";
import SentimentBadge from "./components/SentimentBadge";
import MetricsDashboard from "./components/MetricsDashboard";
import { useSentiment } from "./hooks/useSentiment";

export default function App() {
  const { result, loading, error, analyze } = useSentiment();
  const [tab, setTab] = useState("predict");

  const tabStyle = (t) => ({
    padding: "8px 20px",
    borderRadius: "8px",
    border: "none",
    background: tab === t ? "#534AB7" : "transparent",
    color: tab === t ? "#fff" : "#666",
    fontWeight: 500,
    fontSize: "13px",
    cursor: "pointer",
  });

  return (
    <div style={{ minHeight: "100vh", background: "#f5f5f3", padding: "40px 20px", fontFamily: "system-ui, sans-serif" }}>
      <div style={{ maxWidth: "820px", margin: "0 auto" }}>

        <div style={{ marginBottom: "32px" }}>
          <h1 style={{ fontSize: "24px", fontWeight: 700, margin: 0, color: "#1a1a1a" }}>
            IMDB Sentiment Analysis
          </h1>
          <p style={{ color: "#888", fontSize: "13px", marginTop: "6px" }}>
            Logistic Regression · 50k reviews · F1 0.9043 · TF-IDF bigrams
          </p>
        </div>

        <div style={{ display: "flex", gap: "4px", marginBottom: "24px", background: "#ebebeb", padding: "4px", borderRadius: "10px", width: "fit-content" }}>
          <button style={tabStyle("predict")} onClick={() => setTab("predict")}>Predict</button>
          <button style={tabStyle("metrics")} onClick={() => setTab("metrics")}>Model metrics</button>
        </div>

        {tab === "predict" && (
          <div style={{ display: "grid", gridTemplateColumns: result ? "1fr 1fr" : "1fr", gap: "24px", alignItems: "start" }}>
            <div style={{ background: "#fff", borderRadius: "16px", padding: "24px", border: "1px solid #e8e8e8" }}>
              <ReviewInput onAnalyze={analyze} loading={loading} />
              {error && <p style={{ color: "#D85A30", fontSize: "13px", marginTop: "12px" }}>{error}</p>}
            </div>
            {result && (
              <div style={{ background: "#fff", borderRadius: "16px", padding: "24px", border: "1px solid #e8e8e8" }}>
                <SentimentBadge label={result.label} confidence={result.confidence} />
              </div>
            )}
          </div>
        )}

        {tab === "metrics" && (
          <div style={{ background: "#fff", borderRadius: "16px", padding: "24px", border: "1px solid #e8e8e8" }}>
            <MetricsDashboard />
          </div>
        )}

      </div>
    </div>
  );
}
