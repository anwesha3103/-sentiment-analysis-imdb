import { useEffect, useState } from "react";
import { fetchMetrics } from "../api/sentiment";
import ConfusionMatrix from "./ConfusionMatrix";
import { RadarChart, Radar, PolarGrid, PolarAngleAxis, ResponsiveContainer } from "recharts";

export default function MetricsDashboard() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetchMetrics().then(setMetrics).catch(console.error);
  }, []);

  if (!metrics) return <p style={{ color: "#888", fontSize: "13px" }}>Loading metrics...</p>;

  const radarData = [
    { metric: "Accuracy",  value: metrics.accuracy  * 100 },
    { metric: "F1 Score",  value: metrics.f1_score  * 100 },
    { metric: "Precision", value: metrics.precision * 100 },
    { metric: "Recall",    value: metrics.recall    * 100 },
  ];

  const statCards = [
    { label: "Accuracy",  value: (metrics.accuracy  * 100).toFixed(2) + "%" },
    { label: "F1 Score",  value: (metrics.f1_score  * 100).toFixed(2) + "%" },
    { label: "Precision", value: (metrics.precision * 100).toFixed(2) + "%" },
    { label: "Recall",    value: (metrics.recall    * 100).toFixed(2) + "%" },
  ];

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "12px" }}>
        {statCards.map((s) => (
          <div key={s.label} style={{ background: "#f8f8f8", border: "1px solid #e0e0e0", borderRadius: "12px", padding: "16px", textAlign: "center" }}>
            <div style={{ fontSize: "24px", fontWeight: 700, color: "#534AB7" }}>{s.value}</div>
            <div style={{ fontSize: "11px", color: "#888", marginTop: "4px" }}>{s.label}</div>
          </div>
        ))}
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "24px" }}>
        <div>
          <p style={{ fontSize: "13px", fontWeight: 500, marginBottom: "12px", color: "#444" }}>Model performance</p>
          <ResponsiveContainer width="100%" height={220}>
            <RadarChart data={radarData}>
              <PolarGrid stroke="#e0e0e0" />
              <PolarAngleAxis dataKey="metric" tick={{ fontSize: 11 }} />
              <Radar dataKey="value" stroke="#534AB7" fill="#534AB7" fillOpacity={0.2} />
            </RadarChart>
          </ResponsiveContainer>
        </div>
        <div>
          <p style={{ fontSize: "13px", fontWeight: 500, marginBottom: "12px", color: "#444" }}>Prediction breakdown</p>
          <ConfusionMatrix matrix={metrics.confusion_matrix} />
        </div>
      </div>
    </div>
  );
}