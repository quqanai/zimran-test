<template>
  <router-link
    class="block"
    :to="{ name: 'newsDetails', params: { newsId: props.news.id } }"
  >
    <div class="p-3 rounded-lg shadow-[0_0_2px_rgba(0,0,0,0.27)]">
      <div class="grid grid-cols-[92px,1fr] gap-3">
        <div class="rounded overflow-hidden">
          <img class="h-full object-cover" :src="props.news.image_url" />
        </div>
        <div class="space-y-2">
          <h2 class="text-sm font-semibold text-[#24234C]">
            {{ props.news.title }}
          </h2>
          <p class="text-xs text-[#636366]">{{ props.news.content }}</p>
          <time-stamp :datetime="props.news.published_at" />
        </div>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { defineProps } from "vue";
import TimeStamp from "@/components/TimeStamp.vue";

const props = defineProps({
  news: Object,
});
</script>
