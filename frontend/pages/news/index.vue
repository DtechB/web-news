<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      class="bg-slate-900 p-4 rounded-lg flex items-center mb-4 shadow-lg sticky top-0 z-20"
    >
      <BaseIcon name="hint" color="orange" size="25px" />
      <h6 class="ml-2 text-orange">You can select multiple categories</h6>
    </div>
    <div class="grid grid-cols-2 justify-items-stretch gap-5">
      <NewsItem v-for="index in 10" :key="index" @click="isOpen = !isOpen" />
    </div>
    <BaseModal
      v-if="isOpen"
      :is-open="isOpen"
      @set-is-open="setIsOpen"
      title="Web news test"
      footer
    >
      <template #body>
        <div class="relative">
          <img
            src="@/assets/images/bg.jpg"
            alt=""
            class="w-full md:mr-5 mb-4 md:mb-0 rounded-xl"
          />
          <div
            class="absolute top-0 right-0 bg-gradient-to-t from-black to-transparent w-full h-full flex flex-col justify-end rounded-xl"
          >
            <div class="flex items-center justify-between p-[2%]">
              <h3 class="text-center">Web news test</h3>
              <div class="flex items-center bg-slate-800 rounded-full p-1 pr-3">
                <BaseIcon name="technology" size="30px" />
                <h6 class="ml-2">Technology</h6>
              </div>
            </div>
          </div>
        </div>
        <h6 class="text-justify mt-4 font-light">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero quod
          doloribus, officia esse in minus eius, illum perferendis magni ipsa
          sunt sint molestias reprehenderit sed praesentium adipisci, maiores
          nostrum sequi. Lorem ipsum dolor sit amet consectetur adipisicing
          elit. Est dolorum obcaecati esse repellendus deleniti, neque molestiae
          accusantium, enim, molestias reiciendis inventore quas placeat
          corrupti repellat hic dolor atque pariatur excepturi. Lorem ipsum
          dolor, sit amet consectetur adipisicing elit. Numquam inventore
          eligendi obcaecati ratione earum corrupti eveniet, sit unde id nostrum
          nesciunt voluptatum voluptatem sequi sunt necessitatibus, reiciendis
          quam autem pariatur.
        </h6>
      </template>
      <template #footer>
        <div class="flex justify-end w-full">
          <BaseButton
            text="edit"
            padding="0px 28px"
            right-icon-name="edit"
            background-icon-color="var(--color-blue-300)"
          />
        </div>
      </template>
    </BaseModal>
  </div>
</template>

<script setup lang="ts">
import type { Ref } from "vue";

definePageMeta({
  layout: "default-layout",
  middleware: "auth",
});

const isOpen: Ref<boolean> = ref(false);

const setIsOpen = (val: boolean) => {
  isOpen.value = val;
};
</script>
