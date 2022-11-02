<template>
  <div class="space-y-6">
    <div class="space-y-2">
      <news-card v-for="news in state.news" :key="news.id" :news="news" />
    </div>
    <the-pagination
      :page="props.page"
      :total="state.total"
      :size="state.size"
    />
  </div>
</template>

<script setup>
import { onMounted, reactive, defineProps } from "vue";
import NewsCard from "./NewsCard.vue";
import ThePagination from "@/components/ThePagination/ThePagination.vue";
import { fetchNews } from "@/api/newsApi";

const props = defineProps({
  page: Number,
});
const state = reactive({
  news: [],
  total: 0,
  size: 0,
});

onMounted(async () => {
  const { items, total, size } = await fetchNews(props.page);
  state.news = items;
  state.total = total;
  state.size = size;
});
</script>
