<template>
  <div v-if="props.datetime" class="flex items-center space-x-1">
    <font-awesome-icon
      class="text-[#48484A]"
      icon="fa-regular fa-clock"
      fixed-width
    />
    <span class="text-[10px] font-medium text-[#48484A]">{{
      formattedDatetime
    }}</span>
  </div>
</template>

<script setup>
import { defineProps, computed } from "vue";
import { format } from "date-fns";

const props = defineProps({ datetime: String });

const formattedDatetime = computed(() => {
  const date = new Date(props.datetime);
  return format(date, "MMMM d, y");
});
</script>
