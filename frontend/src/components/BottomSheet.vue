<template>
  <div class="fixed inset-0">
    <div class="h-full w-full bg-[rgba(0,0,0,0.8)]"></div>
    <the-container class="absolute inset-x-0 bottom-0">
      <div
        class="relative bg-white rounded-t-2xl pt-16 pb-[30vh] px-6 flex flex-col"
      >
        <button class="absolute top-7 right-7" @click="$emit('handleClose')">
          <font-awesome-icon
            class="text-[#48484A]"
            icon="fa-solid fa-xmark"
            fixed-width
          />
        </button>
        <h2 class="text-[#24234C] font-semibold text-xl text-center mb-2">
          Subscribe to newsletter
        </h2>
        <p class="text-[#636366] text-base text-center mb-8">
          {{ props.text }}
        </p>
        <input
          class="py-[10px] px-3 border rounded text-[#0B0B1D]"
          :class="props.hasError ? 'border-[#C74634]' : 'border-[#C8CED7]'"
          type="email"
          placeholder="Enter your email"
          :value="email"
          @input="$emit('handleChange', $event)"
        />
      </div>
    </the-container>
  </div>
</template>

<script setup>
import { defineProps } from "vue";
import TheContainer from "@/components/TheContainer.vue";

const props = defineProps({
  text: String,
  email: String,
  hasError: Boolean,
});
</script>
