import axios from "axios";

const BASE = "http://localhost:8000/api";

export const predictSentiment = async (text) => {
  const res = await axios.post(`${BASE}/predict`, { text });
  return res.data;
};

export const fetchMetrics = async () => {
  const res = await axios.get(`${BASE}/metrics`);
  return res.data;
};