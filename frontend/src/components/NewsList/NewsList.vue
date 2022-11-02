<template>
  <div class="space-y-6">
    <div class="space-y-2">
      <news-card v-for="news in state.news" :key="news.id" :news="news" />
    </div>
    <the-pagination :page="props.page" />
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
const state = reactive({ news: [] });

onMounted(async () => {
  state.news = await fetchNews();
});
</script>
