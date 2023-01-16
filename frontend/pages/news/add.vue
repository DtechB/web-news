<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      class="bg-slate-900 p-[5%] rounded-lg grid grid-cols-2 justify-items-stretch gap-[5%] mb-4 shadow-lg"
    >
      <div
        class="col-span-2 xl:col-span-1 rounded-lg hover:bg-slate-800 md:cursor-pointer"
      >
        <ImagePicker @onSelect="setPicture" :size="17 / 9" />
      </div>
      <div class="col-span-2 xl:col-span-1">
        <BaseTextInput title="Title" input-name="input-title" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "default-layout",
  middleware: "auth",
});

const setPicture = () => {};
</script>
