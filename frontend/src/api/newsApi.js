import axios from "axios";

const httpClient = axios.create({
  baseURL: process.env.VUE_APP_STOCK_MARKET_API_URL,
});

const fetchNews = async () => {
  const response = await httpClient.get("/news", {
    params: { page_size: 4 },
  });
  return response.data;
};

const fetchNewsDetails = async (newsId) => {
  const response = await httpClient.get(`/news/${newsId}`);
  return response.data;
};

export { fetchNews, fetchNewsDetails };
