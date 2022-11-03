<template>
  <the-container>
    <router-view :key="$route.query" />
  </the-container>
</template>

<script setup>
import TheContainer from "@/components/TheContainer.vue";
</script>
