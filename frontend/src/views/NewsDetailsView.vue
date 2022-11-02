<template>
  <the-header :title="String(state.news.id)" />
  <main class="p-6">
    <h1 class="capitalize text-xl font-semibold mb-2 text-[#15152B]">
      {{ state.news.title }}
    </h1>
    <time-stamp class="mb-4" :datetime="state.news.published_at" />
    <img class="rounded-lg mb-4" :src="state.news.image_url" />
    <p class="text-base text-[#636366]">{{ state.news.content }}</p>
  </main>
</template>

<script setup>
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import TheHeader from "@/components/TheHeader/TheHeader.vue";
import TimeStamp from "@/components/TimeStamp.vue";
import { fetchNewsDetails } from "@/api/newsApi";

const route = useRoute();
const state = reactive({ news: {} });

onMounted(async () => {
  const { newsId } = route.params;
  state.news = await fetchNewsDetails(newsId);
});
</script>
