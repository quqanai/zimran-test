<template>
  <div class="max-w-[600px] mx-auto overflow-hidden">
    <router-view :key="$route.query" />
  </div>
</template>
