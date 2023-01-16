<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      class="bg-slate-900 p-[5%] rounded-lg grid grid-cols-2 justify-items-stretch gap-[5%] mb-4 shadow-lg"
    >
      <div class="col-span-2 xl:col-span-1 rounded-lg">
        <ImagePicker @onSelect="setPicture" :size="17 / 9" />
        <h3 class="mt-10 mb-4 ml-7">Category</h3>
        <BaseSelect
          :options="['category', 'name', 'text', 'fake']"
          @on-select="selectCategory"
        />
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

const selectedCategory = ref<string>("");

const setPicture = () => {};

const selectCategory = (category: string) => {
  selectedCategory.value = category.charAt(0).toUpperCase();
  console.log(selectedCategory.value);
};
</script>
