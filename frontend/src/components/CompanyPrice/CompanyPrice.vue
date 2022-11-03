<template>
  <div class="space-y-4">
    <h2 class="text-xl font-semibold text-[#15152B]">
      {{ props.companyName }}
    </h2>
    <div
      class="bg-white p-4 rounded border shadow-[0_0_2px_rgba(0,0,0,0.27)] flex justify-between space-x-3"
    >
      <div class="flex space-x-3">
        <div class="rounded-full overflow-hidden">
          <img class="object-cover" :src="props.logoUrl" />
        </div>
        <div class="flex flex-col justify-center space-y-2">
          <h3 class="text-[#24234C] text-sm font-semibold">
            {{ props.companyName }}
          </h3>
          <span class="text-[#8A8A8E] text-sm">{{ props.symbol }}</span>
        </div>
      </div>
      <div class="flex flex-col justify-center space-y-2">
        <span class="text-base font-semibold text-[#24234C]">$2,123.34</span>
        <negative-indicator :value="13.14" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from "vue";
// import PositiveIndicator from "./PositiveIndicator.vue";
import NegativeIndicator from "./NegativeIndicator.vue";

const props = defineProps({
  companyName: String,
  logoUrl: String,
  symbol: String,
});
</script>
