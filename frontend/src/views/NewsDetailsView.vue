<template>
  <the-header :title="String(state.news.company__name)" />
  <main class="px-6 pt-6 pb-[30vh]">
    <h1 class="capitalize text-xl font-semibold mb-2 text-[#15152B]">
      {{ state.news.title }}
    </h1>
    <time-stamp class="mb-4" :datetime="state.news.published_at" />
    <img class="rounded-lg mb-4" :src="state.news.image_url" />
    <p class="text-base text-[#636366] mb-6">{{ state.news.content }}</p>
    <company-price
      :companyName="state.news.company__name"
      :logoUrl="state.news.company__logo_url"
      :symbol="state.news.company__symbol"
    />
  </main>
  <bottom-sheet
    v-if="state.bottomSheetShown"
    :text="bottomSheetText"
    :email="state.email"
    :hasError="state.hasError"
    @handleClose="state.bottomSheetShown = false"
    @handleChange="handleInput"
  />
  <bottom-button @handleClick="handler" />
</template>

<script setup>
import { onMounted, reactive, computed } from "vue";
import { useRoute } from "vue-router";
import TheHeader from "@/components/TheHeader/TheHeader.vue";
import TimeStamp from "@/components/TimeStamp.vue";
import CompanyPrice from "@/components/CompanyPrice/CompanyPrice.vue";
import BottomSheet from "@/components/BottomSheet.vue";
import BottomButton from "@/components/BottomButton.vue";
import { fetchNewsDetails } from "@/api/newsApi";
import { createSubscription } from "@/api/subscriptionsApi";

const route = useRoute();
const state = reactive({
  news: {},
  bottomSheetShown: false,
  email: "",
  hasError: false,
});

onMounted(async () => {
  const { newsId } = route.params;
  state.news = await fetchNewsDetails(newsId);
});

const bottomSheetText = computed(() => {
  return `Get notified when something is published about ${state.news.company__name}`;
});

const handler = computed(() => {
  if (state.bottomSheetShown) {
    return handleSubmit;
  }

  return () => {
    state.bottomSheetShown = true;
  };
});

const handleInput = (event) => {
  const { value } = event.target;
  state.email = value;
  state.hasError = false;
};

const handleSubmit = async () => {
  const symbol = state.news.company__symbol;

  try {
    await createSubscription(state.email, symbol);
    state.email = "";
    state.bottomSheetShown = false;
    state.hasError = false;
  } catch (err) {
    state.hasError = true;
  }
};
</script>
