<template>
  <div
    class="px-2 py-1 flex items-center space-x-1 bg-[rgba(199,70,52,0.1)] rounded-full"
  >
    <font-awesome-icon
      class="text-xs text-[#C74634]"
      icon="fa-solid fa-caret-down"
      fixed-width
    />
    <span class="text-[#C74634] font-medium text-xs">-{{ props.value }}%</span>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  value: Number,
});
</script>
