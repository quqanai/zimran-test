import axios from "axios";

const httpClient = axios.create({
  baseURL: process.env.VUE_APP_SUBSCRIPTIONS_API_URL,
});

const createSubscription = async (email, symbol) => {
  return await httpClient.post("/", { email, symbol });
};

export { createSubscription };
