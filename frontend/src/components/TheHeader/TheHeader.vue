<template>
  <header
    class="h-[64px] flex flex-col justify-center bg-white shadow-[0_1px_4px_rgba(0,0,13,0.05)]"
  >
    <dynamic-content v-if="props.title" :title="props.title" />
    <default-content v-else />
  </header>
</template>

<script setup>
import { defineProps } from "vue";
import DefaultContent from "./DefaultContent.vue";
import DynamicContent from "./DynamicContent.vue";

const props = defineProps({
  title: String,
});
</script>
