<template>
  <router-link class="block" :to="{ name: 'newsDetails', params: { id: 1 } }">
    <div class="p-3 rounded-lg shadow-[0_0_2px_rgba(0,0,0,0.27)]">
      <div class="grid grid-cols-[92px,1fr] gap-3">
        <div class="rounded overflow-hidden">
          <img
            class="h-full object-cover"
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/640px-Image_created_with_a_mobile_phone.png"
          />
        </div>
        <div class="space-y-1">
          <h2 class="text-sm font-semibold text-[#24234C]">
            Meta's social media apps back up after brief outage
          </h2>
          <p class="text-xs text-[#636366]">
            Meta Platforms Inc said on Friday it has fixed the issue that was
            preventing users from accessing its social media platforms.
          </p>
          <div>
            <span class="text-[10px] font-medium text-[#48484A]"
              >March 23, 2022</span
            >
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>
