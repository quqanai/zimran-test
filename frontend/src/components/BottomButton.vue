<template>
  <div class="fixed inset-x-0 bottom-0">
    <the-container class="px-6">
      <div class="py-7 bg-gradient-to-t from-white to-transparent">
        <button
          class="w-full p-[10px] rounded-lg bg-[#5653FE] text-white text-sm font-semibold"
          @click="$emit('handleClick')"
        >
          Subscribe to newsletter
        </button>
      </div>
    </the-container>
  </div>
</template>

<script setup>
import TheContainer from "@/components/TheContainer.vue";
</script>
