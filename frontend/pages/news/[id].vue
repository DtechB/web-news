<template>
  <div class="pt-0 animate__animated animate__fadeIn">
    <div
      v-if="!loading"
      class="bg-slate-900 p-[5%] rounded-lg grid grid-cols-2 justify-items-stretch gap-[5%] mb-4 shadow-lg"
    >
      <div class="col-span-2 xl:col-span-1 rounded-lg">
        <ImagePicker
          :image="newData?.image"
          @onSelect="setPicture"
          :size="17 / 9"
        />
        <div class="mt-10 animate__animated animate__bounceInUp">
          <h3 class="mb-4 ml-7">Category</h3>
          <BaseSelect
            :options="['category', 'name', 'text', 'fake']"
            :select="newData?.category.name"
            @on-select="selectCategory"
          />
        </div>
      </div>
      <div class="col-span-2 xl:col-span-1">
        <BaseTextInput
          :init-value="newData?.title"
          title="Title"
          input-name="input-title"
          class="animate__animated animate__bounceInDown"
        />
        <div class="mt-10 animate__animated animate__bounceInRight">
          <h3 class="mb-4 ml-7">Description</h3>
          <textarea
            rows="7"
            class="border-2 border-blue-300 outline-none focus:border-blue-400 rounded-3xl px-5 py-2 bg-slate-900 w-full text-xl"
            >{{ newData?.body }}</textarea
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useToast } from "vue-toastification";

import { getSingleNew } from "@/api/news";
import { NewsData } from "@/constants/types";

definePageMeta({
  layout: "default-layout",
  middleware: "auth",
});

const route = useRoute();
const router = useRouter();
const toast = useToast();

const loading = ref<boolean>(true);
const newData = ref<NewsData | null>(null);
const selectedCategory = ref<string>("");

onMounted(async () => {
  await getNew();
});

const setPicture = () => {};

const selectCategory = (category: string) => {
  selectedCategory.value = category.charAt(0).toUpperCase();
};

const getNew = async () => {
  loading.value = true;
  await getSingleNew(+route.params.id)
    .then((res) => {
      newData.value = res.data;
    })
    .catch(() => {
      toast.error("there is no new with this id");
      router.replace("/news/");
    })
    .finally(() => {
      loading.value = false;
    });
};
</script>
