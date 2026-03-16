export default function ConfusionMatrix({ matrix }) {
  if (!matrix) return null;
  const [[tn, fp], [fn, tp]] = matrix;
  const cells = [
    { label: "True Negative",  value: tn, color: "#1D9E75", bg: "#E1F5EE" },
    { label: "False Positive", value: fp, color: "#D85A30", bg: "#FAECE7" },
    { label: "False Negative", value: fn, color: "#D85A30", bg: "#FAECE7" },
    { label: "True Positive",  value: tp, color: "#1D9E75", bg: "#E1F5EE" },
  ];
  return (
    <div>
      <p style={{ fontSize: "12px", color: "#888", marginBottom: "12px" }}>
        Confusion matrix — {(tn+fp+fn+tp).toLocaleString()} test samples
      </p>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px" }}>
        {cells.map((c) => (
          <div key={c.label} style={{ background: c.bg, border: `1px solid ${c.color}40`, borderRadius: "10px", padding: "16px", textAlign: "center" }}>
            <div style={{ fontSize: "28px", fontWeight: 700, color: c.color }}>{c.value.toLocaleString()}</div>
            <div style={{ fontSize: "11px", color: c.color, marginTop: "4px" }}>{c.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
}