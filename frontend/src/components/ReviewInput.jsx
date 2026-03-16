import { useState } from "react";

const EXAMPLES = [
  "An absolute masterpiece. The performances were stunning and the direction was flawless.",
  "Terrible waste of time. Boring, predictable, and painfully acted throughout.",
  "A decent film with some great moments, though it loses steam in the second half.",
];

export default function ReviewInput({ onAnalyze, loading }) {
  const [text, setText] = useState("");

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste or type a movie review here..."
        rows={6}
        style={{ width: "100%", padding: "14px", borderRadius: "10px", border: "1px solid #d0d0d0", fontSize: "14px", lineHeight: "1.6", resize: "vertical", fontFamily: "inherit", boxSizing: "border-box", outline: "none" }}
      />
      <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
        {EXAMPLES.map((ex, i) => (
          <button key={i} onClick={() => setText(ex)}
            style={{ fontSize: "11px", padding: "4px 10px", borderRadius: "20px", border: "1px solid #d0d0d0", background: "transparent", cursor: "pointer", color: "#666" }}>
            Example {i + 1}
          </button>
        ))}
      </div>
      <button
        onClick={() => { if (text.trim().length >= 10) onAnalyze(text); }}
        disabled={loading || text.trim().length < 10}
        style={{ padding: "12px", borderRadius: "10px", border: "none", background: loading ? "#ccc" : "#534AB7", color: "#fff", fontSize: "14px", fontWeight: 500, cursor: loading ? "not-allowed" : "pointer" }}>
        {loading ? "Analysing..." : "Analyse sentiment"}
      </button>
    </div>
  );
}