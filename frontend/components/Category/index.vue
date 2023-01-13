<template>
  <div
    class="col-span-3 md:col-span-2 flex flex-col items-center rounded-2xl border-2 border-blue-400 p-[5%] shadow-blue-300 hover:shadow-md hover:shadow-blue-300 hover:-translate-y-2 transition-all duration-300 md:cursor-pointer"
    :class="{ 'bg-blue-300': active }"
  >
    <div
      class="w-24 h-24 bg-slate-800 rounded-full flex justify-center items-center"
    >
      <BaseIcon name="user" size="60px" />
    </div>
    <h4 class="mt-3" :class="{ 'text-slate-800': active }">Technology</h4>
  </div>
</template>

<script setup lang="ts">
const active = ref<boolean>(true);
</script>
