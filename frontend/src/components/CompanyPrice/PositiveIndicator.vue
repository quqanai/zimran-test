<template>
  <div
    class="px-2 py-1 flex items-center space-x-1 bg-[rgba(52,199,89,0.1)] rounded-full"
  >
    <font-awesome-icon
      class="text-xs text-[#34C759]"
      icon="fa-solid fa-caret-up"
      fixed-width
    />
    <span class="text-[#34C759] font-medium text-xs">+{{ props.value }}%</span>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  value: Number,
});
</script>
