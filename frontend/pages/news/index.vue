<template>
  <div>
    <LayoutTheHeader>
      <BaseButton
        right-icon-name="plus"
        background-color="var(--color-slate-900)"
        color="var(--color-blue-300)"
      />
    </LayoutTheHeader>
    <div class="overflow-y-scroll main animate__animated animate__fadeIn mt-4">
      <div>
        <div class="h-60 bg-white mb-10"></div>
        <div class="h-60 bg-white mb-10"></div>
        <div class="h-60 bg-white mb-10"></div>
        <div class="h-60 bg-white mb-10"></div>
        <div class="h-60 bg-white mb-10"></div>
        <div class="h-60 bg-white mb-10"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "default-layout",
});
</script>
