<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      class="bg-slate-900 p-4 rounded-lg flex items-center mb-4 shadow-lg sticky top-0 z-20"
    >
      <BaseIcon name="hint" color="orange" size="25px" />
      <h6 class="ml-2 text-orange">You can select multiple categories</h6>
    </div>
    <div class="grid grid-cols-2 justify-items-stretch gap-5">
      <NewsItem v-for="index in 10" :key="index" />
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "default-layout",
  middleware: "auth",
});
</script>
