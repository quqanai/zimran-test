<template>
  <div class="flex justify-between items-center space-x-2">
    <router-link :to="{ name: 'news', query: { page: page - 1 } }">
      <font-awesome-icon
        class="text-[#636366]"
        icon="fa-solid fa-angle-left"
        fixed-width
      />
    </router-link>
    <div class="grow flex space-x-2 justify-center items-center">
      <div
        class="rounded text-sm bg-[#EAEAFF] border border-[#5653FE] text-[#5653FE] px-3 py-1"
      >
        {{ props.page }}
      </div>
    </div>
    <router-link :to="{ name: 'news', query: { page: page + 1 } }">
      <font-awesome-icon
        class="text-[#636366]"
        icon="fa-solid fa-angle-right"
        fixed-width
      />
    </router-link>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  page: Number,
  total: Number,
  size: Number,
});
</script>
