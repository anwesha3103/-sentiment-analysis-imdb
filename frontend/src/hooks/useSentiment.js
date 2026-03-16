import { useState } from "react";
import { predictSentiment } from "../api/sentiment";

export const useSentiment = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const analyze = async (text) => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const data = await predictSentiment(text);
      setResult(data);
    } catch (e) {
      setError(e.response?.data?.detail || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return { result, loading, error, analyze };
};