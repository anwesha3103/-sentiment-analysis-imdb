export default function SentimentBadge({ label, confidence }) {
  const positive = label === "positive";
  const color = positive ? "#1D9E75" : "#D85A30";
  const bg = positive ? "#E1F5EE" : "#FAECE7";
  const border = positive ? "#5DCAA5" : "#F0997B";

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "12px", padding: "24px", borderRadius: "16px", background: bg, border: `1px solid ${border}` }}>
      <span style={{ fontSize: "13px", fontWeight: 500, color, letterSpacing: "0.08em", textTransform: "uppercase" }}>
        {positive ? "Positive" : "Negative"}
      </span>
      <span style={{ fontSize: "48px", fontWeight: 700, color, lineHeight: 1 }}>
        {(confidence * 100).toFixed(1)}%
      </span>
      <span style={{ fontSize: "12px", color }}>confidence</span>
      <div style={{ width: "100%", height: "6px", borderRadius: "3px", background: positive ? "#9FE1CB" : "#F5C4B3" }}>
        <div style={{ width: `${confidence * 100}%`, height: "100%", borderRadius: "3px", background: color, transition: "width 0.6s ease" }} />
      </div>
    </div>
  );
}