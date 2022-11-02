<template>
  <div class="px-6 flex justify-center relative">
    <router-link class="absolute left-6" :to="{ name: 'news' }">
      <font-awesome-icon
        class="text-[#636366]"
        icon="fa-solid fa-angle-left"
        fixed-width
      />
    </router-link>
    <h2 class="text-[#15152B] font-semibold text-base">{{ props.title }}</h2>
  </div>
</template>

<script setup>
import { defineProps } from "vue";

const props = defineProps({
  title: String,
});
</script>
