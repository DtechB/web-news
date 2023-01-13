<template>
  <div class="p-2">
    <div class="bg-slate-900 p-4 rounded-lg flex items-center mb-4 shadow-lg">
      <BaseIcon name="hint" color="orange" size="25px" />
      <h6 class="ml-2 text-orange">You can select multiple categories</h6>
    </div>
    <div
      class="grid grid-cols-6 gap-16 justify-items-center bg-slate-900 rounded-xl py-[5%] shadow-xl"
    >
      <div
        v-for="item in categories"
        :key="item.id"
        :class="{ 'bg-blue-300': item.active }"
        class="aspect-square col-span-3 md:col-span-2 flex flex-col items-center rounded-2xl border-2 border-blue-300 p-[5%] shadow-blue-300 hover:shadow-md hover:scale-95 hover:shadow-blue-300 transition-all duration-200 md:cursor-pointer"
        @click="item.active = !item.active"
      >
        <div
          class="w-24 h-24 bg-slate-800 rounded-full flex justify-center items-center"
        >
          <BaseIcon :name="item.iconName" size="60px" />
        </div>
        <h4 class="mt-3" :class="{ 'text-slate-800': item.active }">
          {{ item.name }}
        </h4>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Ref } from "vue";
definePageMeta({
  layout: "default-layout",
});

const active: Ref<boolean> = ref(true);
const categories = ref([
  { id: 1, name: "Technology", iconName: "technology", active: false },
  { id: 2, name: "Economics", iconName: "economics", active: false },
  { id: 3, name: "Politics", iconName: "user", active: true },
  { id: 4, name: "Health", iconName: "health", active: false },
  { id: 5, name: "Sports", iconName: "sport", active: true },
]);
</script>
