<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      class="bg-slate-900 p-[5%] rounded-lg grid grid-cols-2 justify-items-stretch gap-[5%] mb-4 shadow-lg"
    >
      <div class="col-span-2 xl:col-span-1 rounded-lg">
        <ImagePicker @onSelect="setPicture" :size="17 / 9" />
        <div class="mt-10 animate__animated animate__bounceInUp">
          <h3 class="mb-4 ml-7">Category</h3>
          <BaseSelect
            :options="['category', 'name', 'text', 'fake']"
            @on-select="selectCategory"
          />
        </div>
      </div>
      <div class="col-span-2 xl:col-span-1">
        <BaseTextInput
          title="Title"
          input-name="input-title"
          class="animate__animated animate__bounceInDown"
        />
        <div class="mt-10 animate__animated animate__bounceInRight">
          <h3 class="mb-4 ml-7">Description</h3>
          <textarea
            rows="7"
            class="border-2 border-blue-300 outline-none focus:border-blue-400 rounded-3xl px-5 py-2 bg-slate-900 w-full text-xl"
          ></textarea>
        </div>
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
};
</script>
