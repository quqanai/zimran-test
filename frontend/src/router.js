import { createRouter, createWebHashHistory } from "vue-router";
import NewsView from "@/views/NewsView.vue";

const routes = [
  {
    path: "/news",
    name: "news",
    component: NewsView,
  },
  {
    path: "/news/:id",
    name: "newsDetails",
    component: () =>
      import(
        /* webpackChunkName: "newsDetails" */ "@/views/NewsDetailsView.vue"
      ),
  },
  {
    path: "/",
    redirect: { name: "news" },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
