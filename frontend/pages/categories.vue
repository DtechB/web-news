<template>
  <div class="p-2">
    <div class="bg-slate-900 p-4 rounded-lg flex items-center mb-4 shadow-lg">
      <BaseIcon name="hint" color="orange" size="25px" />
      <h6 class="ml-2 text-orange">You can select multiple categories</h6>
    </div>
    <div
      class="grid grid-cols-6 gap-16 justify-items-center bg-slate-900 rounded-xl py-[5%] shadow-xl"
    >
      <Category v-for="index in 5" :key="index" />
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "default-layout",
});
</script>
