<template>
  <the-header />
  <main class="p-6">
    <h1 class="capitalize text-xl font-semibold mb-4 text-[#15152B]">
      Discover market news
    </h1>
    <news-list :page="page" />
  </main>
</template>

<script setup>
import { useRoute } from "vue-router";
import TheHeader from "@/components/TheHeader/TheHeader.vue";
import NewsList from "@/components/NewsList/NewsList.vue";

const route = useRoute();
const page = Number(route.query.page) || 1;
</script>
